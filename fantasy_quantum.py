from qiskit import QuantumCircuit
from qiskit.quantum_info import SparsePauliOp
from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager
from qiskit_ibm_runtime import EstimatorV2 as Estimator
from qiskit_ibm_runtime import QiskitRuntimeService
from qiskit_ibm_runtime import SamplerV2 as Sampler
import numpy as np

f = open("NextWeekOdds.csv", "r")
lines = f.readlines()
f.close()

matchups = []
line_idx = 1
while line_idx < 7:
    line_arr = lines[line_idx].split(",")
    odds = float(line_arr[2].rstrip()) / 100.0
    matchups.append({"Q0": line_arr[0], "Q1": line_arr[1], "odds": odds})
    line_idx += 1
service = QiskitRuntimeService()


def submit_job():

    backend = service.least_busy(simulator=False, operational=True)
    pm = generate_preset_pass_manager(backend=backend, optimization_level=1)

    circuits = []
    for matchup in matchups:
        qc = QuantumCircuit(2)
        angle = np.arcsin(np.sqrt(matchup["odds"])) * 2
        qc.rx(np.pi - angle, 0)
        qc.rx(np.pi, 1)
        qc.cx(0, 1)
        qc.measure_all()
        isa_qc = pm.run(qc)

        circuits.append(isa_qc)

    sampler = Sampler(backend=backend)
    sampler.options.default_shots = 100

    job = sampler.run(circuits)
    print(f">>> Job ID: {job.job_id()}")
    print(f">>> Job Status: {job.status()}")


def get_results():
    job = service.job("cvn1wjaex53g008q9dp0")
    print(f">>> Job Status: {job.status()}")
    job_results = job.result()
    f = open("BambitronQuantum.csv", "w")
    f.write(
        "Team A,Team B, Team A Wins (Bambitron Classic), Team A Wins,Team B Wins,Both Win,Both Lose\n"
    )
    for matchup, pub_result in zip(matchups, job_results):
        print(matchup)

        class_dict = pub_result.data.meas.get_counts()
        for bit_string in ["01", "10", "00", "11"]:
            if bit_string not in class_dict:
                class_dict[bit_string] = 0
        print(f"Counts for the meas output register: {class_dict}")
        f.write(
            "{},{},{}%,{}%,{}%,{}%,{}%\n".format(
                matchup["Q0"],
                matchup["Q1"],
                matchup["odds"] * 100,
                class_dict["10"],
                class_dict["01"],
                class_dict["11"],
                class_dict["00"],
            )
        )
    f.close()


submit_job()
# get_results()

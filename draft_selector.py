from qiskit import QuantumCircuit
from qiskit.quantum_info import SparsePauliOp
from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager
from qiskit_ibm_runtime import EstimatorV2 as Estimator
from qiskit_ibm_runtime import QiskitRuntimeService
from qiskit_ibm_runtime import SamplerV2 as Sampler
import numpy as np

service = QiskitRuntimeService()


def submit_job():

    backend = service.least_busy(simulator=False, operational=True)
    pm = generate_preset_pass_manager(backend=backend, optimization_level=1)
    qc = QuantumCircuit(8)
    qc.h(range(8))
    qc.measure_all()
    isa_qc = pm.run(qc)
    
    sampler = Sampler(backend)
    sampler.options.default_shots = 12

    job = sampler.run([isa_qc])
    print(f">>> Job ID: {job.job_id()}")
    print(f">>> Job Status: {job.status()}")


def get_results():
    job = service.job("daa7de4jbipc73ffjj8g")
    print(f">>> Job Status: {job.status()}")
    job_results = job.result()
    pub_result = job_results[0]
    bit_arr = pub_result.data.meas.array
    teams = [
        "Maddie   ",
        "Gina     ",
        "Nicole   ",
        "Zach     ",
        "Sydney   ",
        "Parker   ",
        "Nathan   ",
        "Jason    ",
        "Kerri    ",
        "Danielle ",
        "Alan     ",
        "Robert   "
    ]

    print("Raw Results")
    result_tup = []
    for team, num in zip(teams, bit_arr):

        print(f"{team} {format(num[0], '08b')}: {num[0]}")
        result_tup.append((team, num[0]))


    print("\nDraft Order")
    def sorter(e):
        return e[1]
    
    result_tup.sort(key= sorter, reverse=True)
    for i, team in enumerate(result_tup):
        print(f"Pick {i + 1}: {team[0]}")


def login():
    from qiskit_ibm_runtime import QiskitRuntimeService
 
    QiskitRuntimeService.save_account(
    token=token,
    channel="ibm_quantum_platform", # `channel` distinguishes between different account types.
    instance="instance-CRN or instance-name", # Optionally copy the instance CRN or name from the Instance section on the dashboard.
    name="account-name", # Optionally name this set of credentials.
    overwrite=True, # Only needed if you already have Cloud credentials.
    set_as_default=True # Only needed if you want these credentials to be used as the default account.
    # This is recommended if you have an IQP classic account set as the default.
    )

# submit_job()
get_results()

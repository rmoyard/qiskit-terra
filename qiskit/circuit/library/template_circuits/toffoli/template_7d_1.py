from qiskit.circuit.quantumcircuit import QuantumCircuit


def template_7d_1():
    qc = QuantumCircuit(3)
    qc.cx(1, 0)
    qc.ccx(0, 2, 1)
    qc.cx(1, 2)
    qc.ccx(0, 1, 2)
    qc.ccx(0, 2, 1)
    qc.cx(1, 0)
    qc.ccx(0, 1, 2)
    return qc
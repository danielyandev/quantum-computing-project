from qiskit_aer import Aer
from qiskit import QuantumCircuit, transpile


class MasterMind:
    def __init__(self, secret=None):
        if secret is None:
            secret = [0, 1, 1, 0, 1, 1, 0, 0]

        self.secret = secret
        self.circuit = self.initialize_circuit()
        self.prepare_secret_qubits()
        self.prepare_guess_qubits()
        self.compare()
        self.measure_feedback()

    def get_circuit(self):
        return self.circuit

    @staticmethod
    def initialize_circuit():
        """
        Initialize the QuantumCircuit with 20 qubits and 4 classical bits for the output
        8 qubits for the guess, 8 for the secret, and 4 for feedback
        :return:
        """
        return QuantumCircuit(20, 4)

    def prepare_secret_qubits(self):
        """
        Apply X gates based on the secret
        :return:
        """
        for i in range(8):
            if self.secret[i] == 1:
                # Apply X gate if the value should be 1
                self.circuit.x(8 + i)

    def prepare_guess_qubits(self):
        """
        Create superpositions for guess qubits
        :return:
        """
        for i in range(8):
            self.circuit.h(i)

    def compare(self):
        """
        Simplified comparison logic to check for correct color and position
        :return:
        """
        for i in range(4):
            guess_bit_1 = i * 2
            guess_bit_2 = guess_bit_1 + 1

            secret_bit_1 = guess_bit_1 + 8
            secret_bit_2 = secret_bit_1 + 1

            feedback_bit = 16 + i

            self.circuit.cx(guess_bit_1, secret_bit_1)  # Flip the secret bit if guess bit is 1
            self.circuit.cx(guess_bit_2, secret_bit_2)  # Flip the second bit of the secret

            # Multi-controlled Toffoli to check if both bits are back to 0 (meaning they were originally the same)
            self.circuit.ccx(secret_bit_1, secret_bit_2, feedback_bit)

            # Reset secret bits back to original state
            self.circuit.cx(guess_bit_1, secret_bit_1)  # Flip the secret bit back
            self.circuit.cx(guess_bit_2, secret_bit_2)  # Flip the second bit of the secret back

    def measure_feedback(self):
        """
        Measurement of feedback qubits
        :return:
        """
        for i in range(4):
            self.circuit.measure(16 + i, i)


class Simulator:
    def __init__(self, circuit, shots):
        self.simulator = Aer.get_backend('qasm_simulator')
        self.circuit = circuit
        self.shots = shots
        
    def get_counts(self):
        job = transpile(self.circuit, self.simulator)
        result = self.simulator.run(job, shots=self.shots).result()
        return result.get_counts(self.circuit)


def main():
    game = MasterMind()
    circuit = game.get_circuit()

    shots = 1000
    simulator = Simulator(circuit, shots)
    counts = simulator.get_counts()

    correct_solutions_percentage = counts.get('1111', 0) / shots * 100

    print(circuit.draw())
    print(counts)
    print(f'Correct solutions: {correct_solutions_percentage}%')


if __name__ == '__main__':
    main()

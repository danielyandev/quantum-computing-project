# Master Mind game with quantum computing usage

## Task
Given n different colors, the first player – the keeper, secretly forms
a sequence of n colored pins, where several pins may share the same color, or all of them may be
of different colors. The task of the second player – the guesser, to disclose the hidden sequence
with minimal guesses.

This project will use Version 2 implementation:

Each guess is graded by the keeper with a single digit – the number of correct
pins in their correct positions. The game stops when the grade of the most recent guess is
n.

## Implementation

The game is described with 20 qubits:
- 1-8 guess qubits
- 9-16 secret qubits
- 17-20 feedback qubits

1. Secret is passed as an array of 8 bits, each 2 bits are 1 color. E.g.
```
[0, 0, 1, 1, 0, 1, 1, 0] -> 4 colors: 00, 11, 01, 10
```

2. Secret qubits are prepared using X gates
3. Guess qubits are put to superposition using Hadamard gates
4. Secret and guess qubits are compared using Toffoli (CCNOT) gates and the results are stored in feedback qubits
5. Finally, feedback qubits are measured to get the result

In this project 1000 shots were used, and as a result it shows a list of all measured states:
```
{'1011': 11, '1110': 16, '1111': 3, '1101': 15, '0111': 15, '1010': 24, '0001': 93, '0011': 48, '1001': 31, '1000': 107, '0100': 112, '1100': 23, '0101': 34, '0110': 40, '0010': 106, '0000': 322}

```

This means that '1011' state appeared 11 times out of 1000.
From the above example we extract that correct solution ('1111') appeared 3 times.

## P.S.

In this implementation secret qubits are compared to guess
qubits in superposition and only feedback qubits are measured.
I misunderstood the task and the solution assumed to be iteratively guessing.
So guess qubits should be measured each time to provide a guess.
For this approach we need:

1. Prepare guess qubits
2. Using Hadamard gate put them to superposition
3. Make first guess and a feedback from keeper to get the score as a matching count.
4. Perform XOR on all positions.
5. To maximize the probability of measuring a result that is far from the initial guess we need to increase aplitudes using qubit flipping.
6. Finally, we need to measure the result and repeat everything to find a solution.

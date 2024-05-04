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

## TODO

1. Estimate the complexity of the move search in different stages of the game.
2. Suggest a system of qubits that describes the game, and define the game states and state
vectors.
3. Design quantum gates that implement the operations of the sequential classical algorithm.
4. Apply the designed gates to superposition states aiming at parallelization of the move
search.

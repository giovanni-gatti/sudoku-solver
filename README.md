# Sudoku Solver

## Overview

This Python project shows how to implement a sudoku generator and solver using the Simulated Annealing algorithm. Simulated Annealing is a probabilistic optimization algorithm based on stochastic processes and Monte Carlo Markov Chain (MCMC) that is particularly effective in solving combinatorial optimization problems. The code can generate and solve sudoku problems of arbitrary size.

## Getting Started

These instructions will help you set up the project on your local machine for development and testing purposes.

### Prerequisites

Make sure you have the following installed on your system:

- Python 3.x
- Pip (Python package installer)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/giovanni-gatti/sudoku-solver.git
   ```

2. Navigate to the project directory:

    ```bash
    cd sudoku-solver
    ```

3. (Optional, recommended) Create and activate a virtual environment: 

	```bash
	python -m venv venv 
	source venv/bin/activate
	```

4. Install the required dependencies (using pip):
    ```bash
    pip install -r requirements.txt
    ```

## Usage
Run the project code with the following command:
```bash
python3 solve.py
```

The [src/SimAnn.py](src/SimAnn.py) file contains the functions to run the Simulated Annealing to sample from the Boltzmann distribution using the Metropolis-Hastings rule.
The constructor of the `Sudoku` class, defined in [src/Sudoku.py](src/Sudoku.py), accepts either an integer number or another Sudoku object as an argument. If the constructor gets a number, it initializes a sudoku table of size equal to the number. If instead it receives a Sudoku object, it chooses at random a fraction of the entries to keep fixed (defined by the argument `r`), and shuffles the rest.
In the [solve.py](solve.py) script, a valid sudoku table is first generated and filled up. Then, a sudoku problem to be solved is created from this valid sudoku table. Finally, the sudoku problem is solved.

## References
- [https://en.wikipedia.org/wiki/Metropolis%E2%80%93Hastings_algorithm](https://en.wikipedia.org/wiki/Metropolis%E2%80%93Hastings_algorithm)
- [https://en.wikipedia.org/wiki/Simulated_annealing](https://en.wikipedia.org/wiki/Simulated_annealing)






# 2d-ray-caster
2D ray casting project to simulate sound propagation

# Acoustic Foam Placement Optimiser
This project simulates sound reflections in closed off 2d spaces and identifies optimal locations for acoustic foam placement using a basic 2d ray tracing approach,
with the goal of reducing as much noise as possible while using as little material as possible

## Features
- **Ray Tracing Simulation**: Models sound as vectors, bouncing off walls and attenuating with each reflection.
- **Optimal Material Placement**: Identifies the most effective points to place foam based on reflected sound intensity.
- **Visualisation**: Displays seating locations, walls, sound paths, and foam placement with the help of matplotlib


## Installation
1. Clone the repository

2. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage
1. Run the simulation:
    ```bash
    python main.py
    ```

2. The script will simulate sound reflections from multiple source nodes and output a visualisation of foam placement based on acoustic reflection intensity.

3. Parameters such as initial decibel level, hearing threshold, and wall absorption coefficients can be modified in `config.py`.

## Files and Packages
- `objects`: Core ray tracing and foam placement logic.
- `setup`: Runs the simulation.
- `config.py`: Simulation constants and thresholds.
- `requirements.txt`: List of Python packages required for the project.
- `README.md`: This file.

[![cov](https://simonmarkwhittle.github.io/simulator_project/badges/coverage.svg)](https://github.com/simonmarkwhittle/simulator_project/actions)

# Simulator Project Test
This codebase is a test package with which I am practicing modern Python configuration management, optional dependencies management, and editable local package installation.  

It is set up as a mock simulation framework that coordinates the interactions of multiple mock simulation models. Basic implementations of the model types are provided in the simulator's codebase, but the use-case being replicated assumes that these will be replaced by more sophisticated models provided by external dependencies.  

The main thing being explored is how best to structure the codebase of the simulator and external model projects in order to allow the simulator to function whether or not the optional dependencies providing the external models are in fact installed.  

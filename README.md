# Ocean Gyre in a Tank (Numerical Experiment)

This is the MITgcm simulation for the Ocean General Circulation in a rotating tank.

## How to set up the experiment

1. Follow the [Getting Started](https://mitgcm.readthedocs.io/en/latest/getting_started/getting_started.html) section on MITgcm documentation to set up the model.
2. Clone this experiment to the MITgcm folder (you can also download the repository and extract it to MITgcm folder.)
3. Create the `build` and `run` folders inside `ocean_gyre_tank`. 
4. Go to `build` and compile the model with `mpi` (see the [MITgcm documentation](https://mitgcm.readthedocs.io/en/latest/)).
5. Copy the executable `mitgcmuv` to the `run` folder.
6. Create a symbolic link to the files in `input` for `run` folder.

## How to generate the initial conditions and forcing

In `notebooks` there is a file called `Init.ipynb` that creates the bathymetry and wind forcing.
The data will be saved to `input` folder. You may have to change the grid spacing in `input/data` or number of points in `code/SIZE.h` if you change the code on the notebooks.

## How to configure the experiment

The file `data` in `input` folder has all the parameters needed for the experiment.
You can change to the linear case setting `.FALSE.` for `momAdvection`.

## How to run the experiment

The current configuration on `code/SIZE.h` works in parallel using 4 cores (see [Documentation](https://mitgcm.readthedocs.io/en/latest/) to learn how to set up for a different number of cores).
If the experiment is already configured you just have to run `mpirun -np 4 ./mitgcmuv` in `run` folder.

## How to read the data from the output

The notebook `notebooks/Analysis.ipynb` its a tutorial that explains how to read and plot the output from this experiment.


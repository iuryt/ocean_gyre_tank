# Ocean Gyre in a Tank (Numerical Experiment)

This is the MITgcm simulation for the Ocean General Circulation in a rotating tank.

## How to set up the experiment

1. Follow the [Getting Started](https://mitgcm.readthedocs.io/en/latest/getting_started/getting_started.html) section on MITgcm documentation to set up the model.
2. Clone this experiment to the MITgcm folder (you can also download the repository and extract it to MITgcm folder.)
3. Create the `build` and `run` folders inside `ocean_gyre_tank`. 
4. Go to `build` and compile the model (see the MITgcm documentation).
5. Copy the executable `mitgcmuv` to the `run` folder.
6. Create a symbolic link to the files in `input` for `run` folder.

## How to generate the initial conditions and forcing

In `notebooks` there is a file called `init.ipynb` that creates the bathymetry and wind forcing.
The data will be saved to `input` folder.

## How to configure the experiment

The file `data` in `input` folder has all the parameters needed for the experiment.
You can change to the linear case setting `.FALSE.` for `momAdvection`.


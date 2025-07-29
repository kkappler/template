# template

This is an example of a src/ structure repo.

Previously it used requirements-dev.txt but that has been deprecated and instead we can install the dev requirements from the pyproject.toml file.

To install the environment:
> conda env create --file environment.yaml
> conda activate template

# make the enviromnent available in jupyter-lab
> python -m ipykernel install --user --name template
Because the environment will be in flux for sometime, we may need to periodically update.  Easier than deleteing and re-installing, you can 

> conda env update --name template --file environment.yaml

(optionally include --prune to remove anything not in the yaml)
> conda env update --name template --file environment.yaml --prune

# Add developer stuffs
# > pip install -r requirements-dev.txt # deprecated
> pip install -e ".dev"  # install from toml 
# Install the package 
> pip install -e .



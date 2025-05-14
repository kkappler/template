# template

This is an example of a src/ structure that I have lately been favoring for repo structure.

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
> pip install -r requirements-dev.txt

# Install the package 
> pip install -e .



# python-pyenv-pipenv
Using `pyenv` and `pipenv` on macOS BigSur for the development of numerical algorithms and other implementations.

## Resources

The `image` subproject is using the `pypng` package for generated images from arrays. Documentation for this package can be found [here](https://pypng.readthedocs.io/en/latest/png.html#png.from_array).

Using the matplotlib package, several types of data schemes must be implemented. The following sources can be used for documentation:

* [Plotting categorical variables — Matplotlib 3.3.3 documentation](https://matplotlib.org/gallery/lines_bars_and_markers/categorical_variables.html#sphx-glr-gallery-lines-bars-and-markers-categorical-variables-py)
* [Errorbar limit selection — Matplotlib 3.3.3 documentation](https://matplotlib.org/gallery/lines_bars_and_markers/errorbar_limits_simple.html#sphx-glr-gallery-lines-bars-and-markers-errorbar-limits-simple-py)
* [Python's map(): Processing Iterables Without a Loop – Real Python](https://realpython.com/python-map-function/)
* [Creating multiple subplots using plt.subplots — Matplotlib 3.1.2 documentation](https://matplotlib.org/3.1.1/gallery/subplots_axes_and_figures/subplots_demo.html)

## Issues

When using `pyenv` alongside `conda` package manager, several issues could appear. One issue is related to the virtual environments created via `pyenv`. Namely, the prompt does not show the current virtual environment, or it shows the environment at all times (that is the global). One can solve this issue by creating a condition that prompt adjusting should be ignored if the `cwd` is within system's python environment. However, if the global python environment is not the system's python, then the prompt will show that environment everywhere there is not a `.python-version` file (which is a file used for the setup process of local virtualenvs). **Solution** was mentioned [here](https://github.com/pyenv/pyenv-virtualenv/issues/135), and [this commit](https://github.com/basavyr/macos-devel-issues/commit/84f7524ea99b998515f3df3ba89eabbb604b8a4a) also contains a `.zshrc` file that properly hides the global&system python environments from the prompt.
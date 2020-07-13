# LRUCache

This LRU Cache module is intended to be used with Python 3.8 but it is likely backward compatible with other versions of Python 3. The module only uses the Python standard library so no packages need be installed to use it. It should be used by importing the `lru_cache` module and creating an instance of the `lru_cache.LRUCache` class. To use install the module you have two options:
1. Clone this repo and import the module from your local filesystem. 
2. Install the `lru_cache` package from PyPi (Test) with some variation of the following command (depending on your virtual environment manager): `python3 -m pip install -i https://test.pypi.org/simple/ lru-cache-lceames==0.0.2`

The unit tests use `pytest`, which can be installed using a virtual environment manager of your choosing. One option is to use `pipenv` and the `Pipfile` in this repo. To do so, use the following instructions. 

1. Install `pipenv` https://pypi.org/project/pipenv/ 
2. Navigate to the root directory of this repo
3. `pipenv shell`
4. `pipenv sync`
5. `pytest lru_cache_unittests.py`

# To-Do

1. Add versioning
2. Add PyPi deployment to CircleCI



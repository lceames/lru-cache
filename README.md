# LRUCache

This LRU Cache module is intended to be used with Python 3.8 but it is likely backward compatible with other versions of Python 3. The module only uses the Python standard library so not packages need be installed to use it. To use it, import the `lru_cache` module and create an instance of the `lru_cache.LRUCache` class. 

The unit tests use `pytest`, which can be installed using a virtual environment manager of your choosing. One option is to use `pipenv` and the `Pipfile` in this repo. To do so, use the following instructions. 

1. Install `pipenv` https://pypi.org/project/pipenv/ 
2. Navigate to the root directory of this repo
3. `pipenv shell`
4. `pipenv sync`
5. `pytest lru_cache_unittests.py`


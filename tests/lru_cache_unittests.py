from collections import Hashable

from cache import LRUCache, LRUCacheNotFoundException, LRUCacheArgumentTypeException

import pytest

@pytest.mark.parametrize("size", (5,10,1000,'20'))
def test_init(size):
    if type(size) is int:
        cache = LRUCache(size)
        assert cache.size == size
    else:
        with pytest.raises(LRUCacheArgumentTypeException):
            cache = LRUCache(size)

@pytest.mark.parametrize("key, value",[('testkey', 'testval'), (1, 2), ('keytolist', ['val']), ([1], 'val')])
def test_put(key, value):
    cache = LRUCache(3)
    if isinstance(key, Hashable) == True:
        cache.put(key, value)
    else:
        with pytest.raises(LRUCacheArgumentTypeException):
            cache.put(key, value)


def test_put_size_limit():
    cache = LRUCache(3)
    for i in range(4):
        cache.put(i, None)
    
    assert len(cache.items) == 3
    assert list(cache.items.keys()) == [1,2,3]
    with pytest.raises(LRUCacheNotFoundException):
        cache.get(0)


def test_put_reorder():
    cache = LRUCache(3)
    for i in range(3):
        cache.put(i, None)

    cache.put(0, 'newval')
    assert list(cache.items.keys()) == [1,2,0]

def test_get():
    cache = LRUCache(3)
    for i in range(3):
        cache.put(i, i)

    for i in range(3):
        assert cache.get(i) == i
    
    cache.get(0)
    assert list(cache.items.keys()) == [1,2,0]

def test_get_invalid_key():
    cache = LRUCache(3)
    with pytest.raises(LRUCacheNotFoundException):
        cache.get(1)


def test_delete():
    cache = LRUCache(3)
    for i in range(3):
        cache.put(i, i)

    cache.delete(0)

    assert list(cache.items.keys()) == [1,2]
    with pytest.raises(LRUCacheNotFoundException):
        cache.get(0)


def test_reset():
    cache = LRUCache(3)
    for i in range(3):
        cache.put(i, i)

    cache.reset()
    for i in range(3):
        with pytest.raises(LRUCacheNotFoundException):
            cache.get(i)
    
@pytest.mark.parametrize("size, items_to_insert, get_query",[
    (3, [(3,1), (1, 2), (3, 2)], (3, 2)),
    (3, [(1,2), (3,4), (5,6), (7,8)], (1, None))
    ])
def test_integration(size, items_to_insert, get_query):
    cache = LRUCache(size)
    for item in items_to_insert:
        cache.put(item[0], item[1])

    if get_query[1]:
        assert cache.get(get_query[0]) == get_query[1]
    else:
        with pytest.raises(LRUCacheNotFoundException):
            cache.get(get_query[0])


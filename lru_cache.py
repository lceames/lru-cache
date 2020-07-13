from collections import OrderedDict, Hashable

from typing import Any


class LRUCacheNotFoundException(Exception):
    pass


class LRUCacheArgumentTypeException(Exception):
    pass


class LRUCache:
    def __init__(self, size: int) -> None:
        size_type = type(size)
        if size_type is not int:
            raise LRUCacheArgumentTypeException(f"The size argument to the LRUCache class must be an integer. \
                The given argument is of type '{size_type}''")

        self.size = size
        self.items = OrderedDict()

    def put(self, key: Any, value: Any) -> None:
        if not isinstance(key, Hashable):
            key_type = str(type(key))
            raise LRUCacheArgumentTypeException(f"LRUCache keys must be immutable, hashable Python objects. \
                The provided key of type '{key_type} is not valid.'")
        
        self.items[key] = value
        self.items.move_to_end(key)

        if len(self.items) > self.size:
            self.items.popitem(last=False)

    def get(self, key) -> Any:
        if key not in self.items:
            raise LRUCacheNotFoundException(f"'{key}' is not a key in this LRUCache instance")
        self.items.move_to_end(key)
        return self.items[key]

    def delete(self, key: Any) -> None:
        try:
            del self.items[key]
        except KeyError:
            pass

    def reset(self) -> None:
        self.items = OrderedDict()


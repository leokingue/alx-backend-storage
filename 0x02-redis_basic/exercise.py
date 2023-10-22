#!/usr/bin/env python3
import redis
import uuid
from typing import Union, Optional, Callable
'''
0. Writing strings to Redis
'''


class Cache():
    '''
    Cache class for the implementation of management system caching
    '''
    def __init__(self):
        '''
        Initialize the cache
        '''
        self._redis = redis.Redis(host="localhost", port=6379)
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        '''
        Store the data
        '''
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, float, int]:
        '''
        get : Reading from Redis and recovering original type
        '''
        value = self._redis.get(key)
        if fn:
            value = fn(value)
        return value

    def get_str(self, key: str) -> str:
        '''
        Get a string from the cache.
        '''
        value = self._redis.get(key)
        return value.decode('UTF-8')

    def get_int(self, key: str) -> str:
        '''
        Get an int from the cache.
        '''
        value = self._redis.get(key)
        try:
            value = int(value.decode('UTF-8'))
        except Exception:
            value = 0
        return value

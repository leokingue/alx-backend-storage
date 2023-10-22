#!/usr/bin/env python3
import redis
import uuid
from typing import Union
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

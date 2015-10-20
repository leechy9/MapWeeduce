'''
The MIT License (MIT)

Copyright (c) 2015 Derek Menteer

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
'''
from collections import defaultdict

class MapWeeduce:

  def dict_wrapper(dict_, multi_value):
    def inner(key, value):
      if multi_value: dict_[key].append(value)
      else: dict_[key] = value
    return inner

  def __init__(self, map_, reduce_):
    self._map = map_
    self._reduce = reduce_
    # Create dictionaries for storing results
    self._map_output = defaultdict(list)
    self._reduce_output = dict()
    # Construct emitters
    self._map_emitter = MapWeeduce.dict_wrapper(self._map_output, True)
    self._reduce_emitter = MapWeeduce.dict_wrapper(self._reduce_output, False)
    # Add config to both emitters
    self._config = dict()
    self._map_emitter.config = self._config
    self._reduce_emitter.config = self._config

  def clear(self):
    self._map_data.clear()
    self._reduce_data.clear()

  def set_config(self, key, value):
    self._config[key] = value

  def map(self, key, value):
    staticmethod(self._map(self._map_emitter, key, value))
    return self._map_output

  def reduce(self):
    for key in self._map_output:
      staticmethod(self._reduce(\
       self._reduce_emitter, key, self._map_output[key]))
    return self._reduce_output


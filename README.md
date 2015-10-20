# Map Weeduce #

MapWeeduce is a single file that can be used to perform simple map-reduce tasks. It is only single threaded and not intended to be fast. It's intended to be used for learning and testing algorithms.

The shuffler does ensure values are in sorted order. If this is required, a simple call to `values.sort()` will sort them in-place.

This project for Python3.4+ and is released under the MIT License.

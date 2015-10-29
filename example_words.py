from mapweeduce import MapWeeduce

# Each line is considered a separate document.
strings = [
  'this is a bunch of words',
  'words are good',
  'they are good',
  'they should be counted',
  'words',
]

# Functions
def map_(emit, key, document):
  for word in document.split():
    emit(word, 1)

def reduce_(emit, key, values):
  emit(key, sum(values))

# Main
mr = MapWeeduce(map_, reduce_)

# Have each mapper perform a map operation on a document. No key used.
for document in strings:
  mr.map(None, document)

# Print the results of the entire mapreduce
for k,v in mr.reduce().items():
  print(k, v)

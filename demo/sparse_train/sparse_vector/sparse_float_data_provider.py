from paddle.trainer.PyDataProvider2 import *


# Define a py data provider
@provider(input_types=[
    sparse_vector(10000000),
    dense_vector(1)
])
def process(settings, filename):
    f = open(filename, 'r')
    for line in f:  # read each line
        splits = line.split(',')
        label = float(splits[0])
        splits.pop(0)
        sparse_float = []
        for value in splits:
            v = value.split(" ")
            sparse_float.append((long(v[0]), float(v[1])))
        # give data to paddle.
        yield sparse_float, [label]

    f.close()  # close file
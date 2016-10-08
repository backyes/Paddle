from paddle.trainer.PyDataProvider2 import *


# Define a py data provider
@provider(input_types=[
    sparse_binary_vector(18182296),
    integer_value(2)
])
def process(settings, filename):
    f = open(filename, 'r')

    for line in f:  # read each line
        splits = line.split(',')
        label = int(splits[1])
        splits.pop(0)
        splits.pop(0)
        sparse_non_values = []
        for value in splits:
            v = value.split(" ")
            sparse_non_values.append(long(v[0]))
        # give data to paddle.
        yield sparse_non_values, label


    f.close()  # close file
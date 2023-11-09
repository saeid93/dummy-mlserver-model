import numpy as np
import time
from typing import Tuple, List, Any
from packaging import version
import pydantic
from pydantic import TypeAdapter

def flatten_nested_list(input_data) -> List[Any]:
    flattened = []
    for item in input_data:
        if isinstance(item, list):
            flattened.extend(flatten_nested_list(item))
        else:
            flattened.append(item)
    return flattened


class TimeIt:
    k = 1024

    def __init__(
        self, data: List[Any], datatype: type, size: Tuple[int, int], flatten: bool = False
    ):
        self.data = data
        self.datatype = datatype
        self.size = size
        self.flatten = flatten

    def size_of_data_bytes(self):
        numpy_data = np.array(self.data)  # TODO: not possible in the server
        return numpy_data.size * numpy_data.itemsize

    def size_of_data_kbytes(self):
        return self.size_of_data_bytes() / self.k

    def size_of_data_mbytes(self):
        return self.size_of_data_kbytes() / self.k

    def flatting_time(self):
        start = time.time()
        flatten_nested_list(self.data)
        return time.time() - start

    def pydantic_type(self):
        start = time.time()
        if version.parse(pydantic.__version__) >= version.parse('2'):
            try:
                adapter = TypeAdapter(List[self.datatype])
                adapter.validate_python(self.data)
            except ValueError:
                print('not a valid entry')
        # transformation
        return time.time() - start

    def pydantic_size(self):
        start = time.time()
        # transformation
        return time.time() - start

    def for_loop_type(self):
        start = time.time()
        data = flatten_nested_list(self.data) if self.flatten else self.data
        for item in data:
            try:
                self.datatype(item)
            except ValueError:
                print(f"type mismatch: {item} for {self.datatype}")
        return time.time() - start

    def for_loop_size(self):
        # TODO not precise, it only checks for the entire size
        # it doesn't check in the nested loops
        start = time.time()
        data = flatten_nested_list(self.data) if self.flatten else self.data
        size_of = 1
        for item in self.size:
            size_of = size_of * item
        assert len(data) == size_of
        return time.time() - start

    def numpy_type(self):
        start = time.time()
        try:
            np.array(self.data, dtype=self.datatype)
        except ValueError as error:
            print(error)
        return time.time() - start

    def numpy_size(self):
        # TODO not precise, it only checks for the entire size
        # it doesn't check in the nested loops
        start = time.time()
        return time.time() - start

    def map_type(self):
        start = time.time()
        try:
            all(map(lambda l: self.datatype(l), self.data))
        except ValueError:
            print('not a valid entry')
        return time.time() - start

    def map_size(self):
        # TODO not precise, it only checks for the entire size
        # it doesn't check in the nested loops
        start = time.time()
        return time.time() - start


dimension = 1024  # TODO assume flatten TODO add to design doc
np.random.seed(53)
sample_data = np.random.random([dimension * dimension]).tolist()
sample_data[1024*1000] = 'ddd'
print(len(sample_data))

time_it = TimeIt(data=sample_data, datatype=float, size=(dimension, dimension))

# for loop timings
print("\n")
print(f"flatten the for_loop: {time_it.flatting_time()}")
print(f"data size in bytes: {time_it.size_of_data_bytes()}")

# for loop timings
print("\n")
print(f"validate type for_loop: {time_it.for_loop_type()}")
print(f"validate size for_loop: {time_it.for_loop_size()}")


# Pydantic v2
print("\n")
print(f"validate type pydantic v2: {time_it.pydantic_type()}")
print(f"validate size pydantic v2: {time_it.pydantic_size()}")

# numpy
print("\n")
print(f"validate type numpy: {time_it.numpy_type()}")
print(f"validate size numpy: {time_it.numpy_size()}")

# map
print("\n")
print(f"validate type map: {time_it.map_type()}")
print(f"validate size map: {time_it.map_size()}")

# 1. Find the datatype recieved at the grpc and rest entry points
# 2. Find Pydantic knobs that checks for their change
# 3. Time the difference between Pydantic V1, V2, for loop or any other similar methods
# 4. Use real data instad of dummy python
# 5. Check how Triton is doing it
# 6. Make sure the logic is consistent, e.g. for now I don't think what I am doing is exactly inline
#    with the excpected datatype check in the MLServer since I am checking a numpy string but there
#    it recieves an array

import numpy as np
import time
from typing import Tuple, List, Any


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
        self, data: List[Any], type: type, size: Tuple[int, int], flatten: bool = False
    ):
        self.data = data
        self.type = type
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
                self.type(item)
            except ValueError:
                print(f"type mismatch: {item} for {self.type}")
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


dimension = 1024  # TODO assume flatten TODO add to design doc
np.random.seed(53)
sample_data = np.random.random([dimension * dimension]).tolist()

print(len(sample_data))

time_it = TimeIt(data=sample_data, type=np.float64, size=(dimension, dimension))

print(f"flatten the for loop: {time_it.flatting_time()}")
print(f"validate type for loop: {time_it.for_loop_type()}")
print(f"validate size for loop: {time_it.for_loop_size()}")
print(f"data size in bytes: {time_it.size_of_data_bytes()}")

# 1. Find the datatype recieved at the grpc and rest entry points
# 2. Find Pydantic knobs that checks for their change
# 3. Time the difference between Pydantic V1, V2, for loop or any other similar methods
# 4. Use real data instad of dummy python
# 5. Check how Triton is doing it
# 6. Make sure the logic is consistent, e.g. for now I don't think what I am doing is exactly inline
#    with the excpected datatype check in the MLServer since I am checking a numpy string but there
#    it recieves an array

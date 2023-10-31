import requests
import numpy as np

dimension = 1024 * 1024
sample_data = np.random.random([dimension * dimension]).tolist()
sample_data[1024*1000] = 'ddd'

payload = {
    "inputs": [
        {
            "name": "INPUT0",
            "datatype": "FP32",
            "shape": [dimension * dimension],
            "data": sample_data
        },
        {
            "name": "INPUT1",
            "datatype": "FP32",
            "shape": [dimension * dimension],
            "data": sample_data
        }
    ]
}

# payload = {
#     "inputs": [
#         {
#             "name": "parameters-np",
#             "datatype": "INT32",
#             "shape": [2, 2],
#             "data": [1, 2, None, 4],
#             "parameters": {
#                 "content_type": "np"
#             }
#         }
#     ]
# }

response = requests.post(
    "http://localhost:8000/v2/models/add_sub/infer",
    json=payload
)
print(response.json())
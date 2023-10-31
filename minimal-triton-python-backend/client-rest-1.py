import requests

payload = {
    "inputs": [
        {"name": "INPUT0", "datatype": "FP32", "shape": [4], "data": [1, 4, 0, 1]},
        {"name": "INPUT1", "datatype": "FP3332", "shape": [4], "data": [1, 2, 0, 4]},
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

response = requests.post("/v2/models/sum-model/infer", json=payload)
print(response)
print(response.json())

import requests

payload = {
    "inputs": [
        {
            "name": "INPUT0",
            "datatype": "FP32",
            "shape": [4],
            "data": [1, 4, 0, 1]
        },
        {
            "name": "INPUT1",
            "datatype": "FP32",
            "shape": [4],
            "data": [1, 2, 0, 1]
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
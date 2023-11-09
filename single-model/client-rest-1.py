import requests

payload = {
    "inputs": [
        {
            "name": "parameters-np",
            "datatype": "FP16",
            "shape": [1, 4],
            "data": [1, 2, 0, 4],
            "parameters": {"content_type": "np", "models": "sdssds"},
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

# response = requests.post(
#     "http://localhost:8080/v2/models/content-type-example/infer",
#     json=payload
# )

response = requests.post(
    "http://localhost:8080/v2/models/content-type-example/infer", json=payload
)

print(response)
print(response.json())

import requests

payload = {
    "inputs": [
        {
            "name": "parameters-np",
            "datatype": "FP16",
            "shape": [2, 2],
            "data": [1, 2, None, 4],
            "parameters": {
                "content_type": "np"
            }
        },
        # {
        #     "name": "parameters-str",
        #     "datatype": "BYTES",
        #     "shape": [1],
        #     "data": "hello world 😁",
        #     "parameters": {
        #         "content_type": "str"
        #     }
        # }
    ]
}

# payload = """
# {
#     "inputs": [
#         {
#             "name": "parameters-np",
#             "datatype": "FP16",
#             "shape": [2, 2],
#             "data": [1, 2, null, 4],
#             "parameters": {
#                 "content_type": "np"
#             }
#         }
#     ]
#     }
# """

response = requests.post(
    "http://localhost:8080/v2/models/content-type-example/infer",
    json=payload
)
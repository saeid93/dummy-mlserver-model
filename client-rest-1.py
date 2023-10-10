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

payload = """
{
    "inputs": [
      {
        "name": "input-0",
        "shape": [1, 3],
        "datatype": "INT32",
        "data": [1, 2, 3]
      }
    ]
  }
"""

response = requests.post(
    "http://localhost:8080/v2/models/content-type-example/infer",
    # json=payload
    data=payload
)
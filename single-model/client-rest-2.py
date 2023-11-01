import requests

payload = """
{
    "inputs": [
      {
        "name": "input-0",
        "shape": [1, 3],
        "datatype": "INT32",
        "data": [1, 2, 3],
        "parameters": {
          "content_type": "np"
        }
      }
    ]
  }
"""

response = requests.post(
    "http://localhost:8080/v2/models/content-type-example/infer", data=payload
)

import click
import requests

def infer_from_model(model_name):
    payload = {
        "inputs": [
            {
                "name": "input-0",
                "datatype": "INT32",
                "shape": [1, 3],
                "data": [1, 2, 0],
                "parameters": {"content_type": "np"},
            },
            {
                "name": "input-1",
                "datatype": "INT32",
                "shape": [1, 3],
                "data": [1, 0, 4],
                "parameters": {"content_type": "np"},
            },
            # {
            #     "name": "paraameters-np",
            #     "datatype": "FP16",
            #     "shape": [1, 4],
            #     "data": [1, 2, 0, 4],
            #     "parameters": {"content_type": "np"},
            # }
        ]

    }

    response = requests.post(
        f"http://localhost:8080/v2/models/{model_name}/infer", json=payload
    )

    print(response)
    print(response.json())

@click.command()
@click.option('--model_name', prompt='Enter the model name', help='Name of the model')
def main(model_name):
    infer_from_model(model_name)

if __name__ == '__main__':
    main()
import click
import requests

def infer_from_model(model_name):
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
    response = requests.post(
        f"http://localhost:8080/v2/models/{model_name}/infer", json=payload
    )

    print(response)
    print(response.json())

@click.command()
@click.option('--model_name', prompt='Enter the model name', help='Name of the model')
def main(model_name):
    infer_from_model(model_name)

if __name__ == '__main__':
    main()

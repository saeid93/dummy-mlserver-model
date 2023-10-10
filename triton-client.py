import numpy as np
import tritonclient.http as httpclient
from tritonclient.utils import InferenceServerException

def test_infer(model_name, input_data):
    inputs = []
    outputs = []
    inputs.append(httpclient.InferInput("INPUT0", input_data.shape, "INT32"))
    inputs[0].set_data_from_numpy(input_data, binary_data=False)

    outputs.append(httpclient.InferRequestedOutput("INPUT0", binary_data=False))
    triton_client = httpclient.InferenceServerClient(url="localhost:8080")
    results = triton_client.infer(model_name, inputs, outputs=outputs)

    return results

if __name__ == "__main__":
    model_name = "content-type-example"

    input_data = np.arange(start=0, stop=16, dtype=np.int32)
    # input_data = np.expand_dims(input_data, axis=0)

    results = test_infer(model_name, input_data)
    # print(results.get_response())

    output_data = results.as_numpy("INPUT0")

    print(output_data)

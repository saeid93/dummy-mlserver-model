import numpy as np
import tritonclient.http as httpclient
from tritonclient.utils import InferenceServerException
import math

def test_infer(model_name, input_data):
    inputs = httpclient.InferInput("INPUT0", list(input_data.shape) + [1], "FP16")
    # inputs.append(httpclient.InferInput("INPUT0", input_data.shape, "BYTES"))
    inputs.set_data_from_numpy(input_data, binary_data=False)
    inputs._parameters = {"content_type": "np"}

    outputs = httpclient.InferRequestedOutput("INPUT0", binary_data=False)
    triton_client = httpclient.InferenceServerClient(url="localhost:8080")
    results = triton_client.infer(model_name, [inputs], outputs=[outputs])

    return results

if __name__ == "__main__":
    model_name = "content-type-example"

    # input_data = np.arange(start=0, stop=16, dtype=np.int32)
    # input_data = np.expand_dims(input_data, axis=0)
    # input_data = np.array([[ 1., math.nan,  0.]], dtype=np.float16)
    # input_data = np.array([1, 2, None, 4])
    input_data = np.array([[ 1., 2.,  0.]], dtype=np.float16)

    results = test_infer(model_name, input_data)
    # print(results.get_response())

    output_data = results.as_numpy("INPUT0")

    print(output_data)

import grpc
from mlserver.grpc.converters import ModelInferResponseConverter
import mlserver.grpc.dataplane_pb2_grpc as dataplane
import mlserver.grpc.converters as converters
from mlserver.codecs.numpy import NumpyCodec
import mlserver.types as types
import numpy as np
from pprint import PrettyPrinter

pp = PrettyPrinter(indent=4)

# single node mlserver
endpoint = "localhost:8081"
model = "model-one"
metadata = []
grpc_channel = grpc.insecure_channel(endpoint)
grpc_stub = dataplane.GRPCInferenceServiceStub(grpc_channel)

input_data = np.array([1, 2, 3], dtype=np.int32)


def send_requests(input_data):
    inference_request = types.InferenceRequest(
        inputs=[
            types.RequestInput(
                name="input-1",
                shape=[1, 3],
                datatype="INT32",
                data=input_data.tolist(),
                parameters=types.Parameters(content_type="np"),
            )
        ]
    )
    inference_request_g = converters.ModelInferRequestConverter.from_types(
        inference_request, model_name=model, model_version=None
    )
    response = grpc_stub.ModelInfer(request=inference_request_g, metadata=metadata)
    return response


# sync version
results = []
# for data_ins in input_data:
response = send_requests(input_data)
results.append(response)

# Note that here we just convert from the gRPC types to the MLServer types
inference_response = ModelInferResponseConverter.to_types(response)
raw_json = NumpyCodec.decode_output(inference_response.outputs[0])
pp.pprint(raw_json)

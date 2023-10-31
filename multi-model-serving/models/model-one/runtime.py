import json

from mlserver import MLModel
from mlserver.types import InferenceRequest, InferenceResponse, ResponseOutput
from mlserver.codecs import DecodedParameterName
from mlserver.settings import ModelSettings
from fastapi.encoders import jsonable_encoder

_to_exclude = {
    "parameters": {DecodedParameterName, "headers"},
    "inputs": {"__all__": {"parameters": {DecodedParameterName, "headers"}}},
}


class EchoRuntimeOne(MLModel):
    async def predict(self, payload: InferenceRequest) -> InferenceResponse:
        outputs = []
        for request_input in payload.inputs:
            print(f"request input name: {request_input.name}")
            decoded_input = self.decode(request_input)
            print(decoded_input)
            print(f"------ Encoded Input ({request_input.name}) ------")
            as_dict = request_input.dict(exclude=_to_exclude)  # type: ignore
            print(json.dumps(as_dict, indent=2))
            print(f"------ Decoded input ({request_input.name}) ------")
            print(decoded_input)

            outputs.append(
                ResponseOutput(
                    name=request_input.name,
                    datatype="FP16",
                    shape=request_input.shape,
                    data=request_input.data,
                )
            )

        return InferenceResponse(model_name=self.name, outputs=outputs)

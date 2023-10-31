import triton_python_backend_utils as pb_utils


class EchoModel(pb_utils.TritionPythonModel):
    def initialize(self, args):
        # No initialization is needed
        pass

    def finalize(self):
        # No finalization is needed
        pass

    def inference(self, model_input):
        # Simply echo the input
        model_output = [1, 2]
        return pb_utils.InferenceResult(output=model_output)

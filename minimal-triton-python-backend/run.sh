docker run -it --rm -p 8000:8000 --name triton_server \
    --mount type=bind,source=$(pwd)/python_backend,target=/models \
    nvcr.io/nvidia/tritonserver:21.11-py3 tritonserver --model-repository=/models
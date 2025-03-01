import os

import pytest


@pytest.mark.parametrize("model", ["meta-llama/Meta-Llama-3-8B"])
def test_full_graph(model):
    # make sure these models can be captured in full graph mode
    os.environ["APHRODITE_TEST_DYNAMO_GRAPH_CAPTURE"] = "1"

    from aphrodite import LLM, SamplingParams
    prompts = [
        "Hello, my name is",
        "The president of the United States is",
        "The capital of France is",
        "The future of AI is",
    ]
    sampling_params = SamplingParams(temperature=0)
    llm = LLM(model="meta-llama/Meta-Llama-3-8B")
    llm.generate(prompts, sampling_params)

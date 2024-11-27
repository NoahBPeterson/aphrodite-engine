import pytest
import torch

from aphrodite._custom_ops import permute_cols


@pytest.mark.parametrize('shape', [(1, 512), (544, 4096), (67, 8192)])
@pytest.mark.parametrize('dtype', [torch.bfloat16, torch.float16])
def test_permute_cols(shape, dtype):
    x = torch.randn(shape, dtype=dtype).cuda()
    perm = torch.randperm(x.shape[1]).to(torch.int).cuda()
    y = permute_cols(x, perm)
    torch.testing.assert_close(y, x[:, perm])

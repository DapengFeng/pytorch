# flake8: noqa: F401
r"""QAT Dynamic Modules.

This package is in the process of being deprecated.
Please, use `torch.ao.nn.qat.dynamic` instead.
"""
from . import dynamic, modules  # noqa: F403
from .modules import *  # noqa: F403


__all__ = [
    "Linear",
    "Conv1d",
    "Conv2d",
    "Conv3d",
    "Embedding",
    "EmbeddingBag",
]

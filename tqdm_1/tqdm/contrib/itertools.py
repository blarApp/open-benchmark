"""
Thin wrappers around `itertools`.
"""
from __future__ import absolute_import
from tqdm.auto import tqdm as tqdm_auto
from copy import deepcopy
import itertools


def product(*iterables, **tqdm_kwargs):
    """
    Equivalent of `itertools.product`.

    Parameters
    ----------
    tqdm_class  : [default: tqdm.auto.tqdm].
    """
    kwargs = deepcopy(tqdm_kwargs)
    tqdm_class = kwargs.pop("tqdm_class", tqdm_auto)
    try:
        lens = list(map(len, iterables))
    except TypeError:
        total = None
    else:
        total = 1
        for i in lens:
            total *= i
        kwargs.setdefault("total", total)
    with tqdm_class(**kwargs) as t:
        for i in itertools.product(*iterables):
            yield i
            t.update()

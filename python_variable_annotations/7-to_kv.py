from typing import Union, Tuple

def to_kv(k: str, v: Union[int, float]) -> Tuple[str, Union[int, float]]:
    return (k, v ** 2)

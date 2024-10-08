import pytest
from src.python.c_api import *
from src.python.utils import num_to_limbs
from src.python.elliptic_curve import field_order, curve_a


@pytest.fixture
def parameters():
    params = EC_parameters()
    params.Pmod.array[:] = num_to_limbs(field_order)
    params.A.array[:] = num_to_limbs(curve_a)

    return params

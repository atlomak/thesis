import ctypes
import pytest
from sage.all import GF, EllipticCurve
from pathlib import Path

LIMBS = 6


class cgbn_mem_t(ctypes.Structure):
    _fields_ = [("_limbs", ctypes.c_uint32 * 6)]


class EC_point(ctypes.Structure):
    _fields_ = [("x", cgbn_mem_t), ("y", cgbn_mem_t)]


class EC_parameters(ctypes.Structure):
    _fields_ = [
        ("Pmod", cgbn_mem_t),
        ("a", cgbn_mem_t),
        ("P", EC_point),
        ("Q", EC_point),
    ]


path = Path.cwd().parent
cuda_rho_pollard = ctypes.CDLL(str(path) + "/build/libtest_kernels.so")

cuda_rho_pollard.test_adding_points.argtypes = [
    ctypes.POINTER(EC_point),
    ctypes.c_size_t,
    ctypes.POINTER(EC_parameters),
]

cuda_rho_pollard.test_adding_points.restype = None


def num_to_limbs(number, limbs=6):
    number = int(number)
    result = []
    mask = (1 << 32) - 1
    for i in range(limbs):
        result.append(number & mask)
        number >>= 32
    return result


# ECC79p settings

p = 0x62CE5177412ACA899CF5
r = 0x1CE4AF36EED8DE22B99D

a = 0x39C95E6DDDB1BC45733C
b = 0x1F16D880E89D5A1C0ED1

n = 0x62CE5177407B7258DC31

P_x = 0x315D4B201C208475057D
P_y = 0x035F3DF5AB370252450A

Q_x = 0x0679834CEFB7215DC365
Q_y = 0x4084BC50388C4E6FDFAB

F = GF(p)
E = EllipticCurve(F, [a, b])

P = E(P_x, P_y)
Q = E(Q_x, Q_y)


@pytest.fixture
def parameters():
    params = EC_parameters()
    params.Pmod._limbs[:] = num_to_limbs(p)
    params.a._limbs[:] = num_to_limbs(a)
    params.P.x._limbs[:] = num_to_limbs(P[0])
    params.P.y._limbs[:] = num_to_limbs(P[1])

    params.Q.x._limbs[:] = num_to_limbs(Q[0])
    params.Q.y._limbs[:] = num_to_limbs(Q[1])

    return params

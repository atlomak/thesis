import ctypes

from settings import *


def test_add_points_debug(parameters):
    A = Q * 1001
    B = Q * 20

    R = A + B

    points = (EC_point * 2)()

    points[0].x._limbs[:] = num_to_limbs(A[0])
    points[0].y._limbs[:] = num_to_limbs(A[1])

    points[1].x._limbs[:] = num_to_limbs(B[0])
    points[1].y._limbs[:] = num_to_limbs(B[1])

    cuda_rho_pollard.test_adding_points(points, 1, ctypes.byref(parameters))

    expected_x = num_to_limbs(R[0])
    expected_y = num_to_limbs(R[1])

    result_x = list(points[0].x._limbs)
    result_y = list(points[0].y._limbs)

    assert expected_x == result_x
    assert expected_y == result_y


def test_add_points_2(parameters):
    A = P * 10
    B = Q

    R = A + B

    points = (EC_point * 2)()

    points[0].x._limbs[:] = num_to_limbs(A[0])
    points[0].y._limbs[:] = num_to_limbs(A[1])

    points[1].x._limbs[:] = num_to_limbs(B[0])
    points[1].y._limbs[:] = num_to_limbs(B[1])

    cuda_rho_pollard.test_adding_points(points, 1, ctypes.byref(parameters))

    expected_x = num_to_limbs(R[0])
    expected_y = num_to_limbs(R[1])

    result_x = list(points[0].x._limbs)
    result_y = list(points[0].y._limbs)

    assert expected_x == result_x
    assert expected_y == result_y


def test_add_points_3(parameters):
    A = P * 10
    B = Q * 10

    R = A + B

    points = (EC_point * 2)()

    points[0].x._limbs[:] = num_to_limbs(A[0])
    points[0].y._limbs[:] = num_to_limbs(A[1])

    points[1].x._limbs[:] = num_to_limbs(B[0])
    points[1].y._limbs[:] = num_to_limbs(B[1])

    cuda_rho_pollard.test_adding_points(points, 1, ctypes.byref(parameters))

    expected_x = num_to_limbs(R[0])
    expected_y = num_to_limbs(R[1])

    result_x = list(points[0].x._limbs)
    result_y = list(points[0].y._limbs)

    assert expected_x == result_x
    assert expected_y == result_y


def test_add_points_4(parameters):
    A = P * 20
    B = Q * 10

    R = A + B

    points = (EC_point * 2)()

    points[0].x._limbs[:] = num_to_limbs(A[0])
    points[0].y._limbs[:] = num_to_limbs(A[1])

    points[1].x._limbs[:] = num_to_limbs(B[0])
    points[1].y._limbs[:] = num_to_limbs(B[1])

    cuda_rho_pollard.test_adding_points(points, 1, ctypes.byref(parameters))

    expected_x = num_to_limbs(R[0])
    expected_y = num_to_limbs(R[1])

    result_x = list(points[0].x._limbs)
    result_y = list(points[0].y._limbs)

    assert expected_x == result_x
    assert expected_y == result_y

from continuous_gems.cgem_utils import (
    check_intersection,
)


def test_intersection():
    assert not check_intersection((0.0, 0.0), 1.0, (2.0, 2.0), 0.1)
    assert not check_intersection((0.0, 0.0), 1.0, (2.0, 2.0), 0.9)
    assert check_intersection((0.0, 0.0), 1.0, (2.0, 2.0), 1.0)
    assert check_intersection((0.0, 0.0), 0.1, (0.0, 0.0), 0.1)
    assert check_intersection((0.0, 0.0), 1.0, (2.0, 0.0), 1.0)

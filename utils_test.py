from utils import manhattan_distance


def test_manhattan_distance():
    assert manhattan_distance((1.0, 1.0), (1.0, 1.0)) == 0.0
    assert manhattan_distance((1.0, 2.0), (1.0, 1.0)) == 1.0
    assert manhattan_distance((1.0, 1.0), (2.0, 1.0)) == 1.0
    assert manhattan_distance((1.0, 1.0), (2.0, 2.0)) == 2.0

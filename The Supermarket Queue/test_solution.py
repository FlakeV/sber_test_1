import pytest
from solution import queue_time

test_data = [
    ([5, 3, 4], 1, 12),
    ([10, 2, 3, 3], 2, 10),
    ([2, 3, 10], 2, 12),
    ([4, 6, 2, 4, 6], 3, 10)
]


def test_func():
    queue_time(test_data[0][0], test_data[0][1])


def test_output_type():
    resp = queue_time(test_data[0][0], test_data[0][1])
    assert int == type(resp)


@pytest.mark.parametrize(['queue', 'tills_count', 'expected'], test_data)
def test_solution(queue, tills_count, expected):
    resp = queue_time(queue, tills_count)
    assert expected == resp

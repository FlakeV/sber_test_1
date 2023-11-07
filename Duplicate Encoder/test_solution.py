import pytest

from solution import duplicate_encoder_1, duplicate_encoder_2

test_data = [
    ([duplicate_encoder_1, duplicate_encoder_2], ('din', '(((')),
    ([duplicate_encoder_1, duplicate_encoder_2], ('recede', '()()()')),
    ([duplicate_encoder_1, duplicate_encoder_2], ('Success', ')())())')),
    ([duplicate_encoder_1, duplicate_encoder_2], ('(( @', '))((')),
]


@pytest.mark.parametrize(['functions', 'example'], test_data[0:1])
def test_def(functions, example):
    for func in functions:
        example = ''
        func(example)


@pytest.mark.parametrize(['functions', 'example'], test_data[0:1])
def test_output_type(functions, example):
    for func in functions:
        resp = func(example[0])
        assert type(example[1]) == type(resp)


@pytest.mark.parametrize(['functions', 'example'], test_data)
def test_solution(functions, example):
    for func in functions:
        resp = func(example[0])
        assert resp == example[1]

from part1 import silly_eval, tokenize


def test_tokenize():
    assert list(tokenize('1 + (22 * (3 + 4))\n')) == [
        '1', '+', '(', '22', '*', '(', '3', '+', '4', ')', ')'
    ]


def test_silly_eval():
    assert silly_eval('42') == 42
    assert silly_eval('1 + 2') == 3
    assert silly_eval('1 + 2 + 3') == 6
    assert silly_eval('2 * 3') == 6
    assert silly_eval('2 * 3 + 1') == 7
    assert silly_eval('1 + 2 * 3') == 9
    assert silly_eval('1 + 2 * 3 + 4 * 5 + 6') == 71
    assert silly_eval('(42)') == 42
    assert silly_eval('(4 + 2)') == 6
    assert silly_eval('2 * (4 + 2)') == 12
    assert silly_eval('2 * 3 + (4 * 5)') == 26
    assert silly_eval('5 + (8 * 3 + 9 + 3 * 4 * 3)') == 437
    assert silly_eval('5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))') == 12240
    assert silly_eval(
        '((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2') == 13632

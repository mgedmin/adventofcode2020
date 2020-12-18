from part2 import silly_eval, tokenize


def test_tokenize():
    assert list(tokenize('1 + (22 * (3 + 4))\n')) == [
        '1', '+', '(', '22', '*', '(', '3', '+', '4', ')', ')'
    ]


def test_silly_eval():
    assert silly_eval('42') == 42
    assert silly_eval('1 + 2') == 3
    assert silly_eval('1 + 2 + 3') == 6
    assert silly_eval('2 * 3') == 6
    assert silly_eval('2 * 3 + 1') == 8
    assert silly_eval('2 * (3) + 1') == 8
    assert silly_eval('1 + 2 * 3') == 9
    assert silly_eval('2 * 2 + 3') == 10
    assert silly_eval('(42)') == 42
    assert silly_eval('((42))') == 42
    assert silly_eval('1 + (2 * 3)') == 7
    assert silly_eval('1 + 2 * 3 + 4 * 5 + 6') == 231
    assert silly_eval('1 + (2 * 3) + (4 * (5 + 6))') == 51
    assert silly_eval('2 * 3 + (4 * 5)') == 46
    assert silly_eval('5 + (8 * 3 + 9 + 3 * 4 * 3)') == 1445
    assert silly_eval('5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))') == 669060
    assert silly_eval(
        '((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2') == 23340
    assert silly_eval(
        '((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2') == 23340

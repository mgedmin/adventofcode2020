from part1 import parse_seat


def test_parse_seat():
    assert parse_seat('FBFBBFFRLR') == 357
    assert parse_seat('BFFFBBFRRR') == 567
    assert parse_seat('FFFBBBFRRR') == 119
    assert parse_seat('BBFFBBFRLL') == 820

from part2 import parse_rule, count_bags


def test_parse_rule():
    assert parse_rule(
        'pale blue bags contain no other bags.\n'
    ) == ('pale blue', [])
    assert parse_rule(
        'pale blue bags contain 1 violent red bag.\n'
    ) == ('pale blue', [(1, 'violent red')])
    assert parse_rule(
        'pale blue bags contain 2 violent red bags, 1 slightly purple bag.\n'
    ) == ('pale blue', [(2, 'violent red'), (1, 'slightly purple')])
    assert parse_rule(
        'pale blue bags contain 1 violent red bag, 2 slightly purple bags,'
        ' 3 deeply yellow bags.\n'
    ) == ('pale blue', [
        (1, 'violent red'), (2, 'slightly purple'), (3, 'deeply yellow')
    ])


def test_count_bags():
    assert count_bags('a', {'a': []}) == 0
    assert count_bags('a', {'a': [(1, 'b')], 'b': []}) == 1

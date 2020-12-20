from part1 import parse_rule


def test_parse_rule():
    assert parse_rule(
        'pale blue bags contain no other bags.\n'
    ) == ('pale blue', [])
    assert parse_rule(
        'pale blue bags contain 1 violent red bag.\n'
    ) == ('pale blue', ['violent red'])
    assert parse_rule(
        'pale blue bags contain 2 violent red bags, 1 slightly purple bag.\n'
    ) == ('pale blue', ['violent red', 'slightly purple'])
    assert parse_rule(
        'pale blue bags contain 1 violent red bag, 2 slightly purple bags,'
        ' 3 deeply yellow bags.\n'
    ) == ('pale blue', ['violent red', 'slightly purple', 'deeply yellow'])

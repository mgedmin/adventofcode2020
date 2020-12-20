from part2 import Tile, flip, rotate, tile_edges


def test_tile_edges():
    tile = Tile([
        "123",
        "894",
        "765",
    ])
    assert tile_edges(tile) == [
        "123",
        "345",
        "567",
        "781",
    ]


def test_rotate():
    tile = Tile([
        "123",
        "894",
        "765",
    ])
    assert rotate(tile) == [
        "345",
        "296",
        "187",
    ]


def test_flip():
    tile = Tile([
        "123",
        "894",
        "765",
    ])
    assert flip(tile) == [
        "765",
        "894",
        "123",
    ]

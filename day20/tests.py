from part1 import tile_edges


def test_tile_edges():
    tile = [
        "123",
        "894",
        "765",
    ]
    assert set(tile_edges(tile)) == {
        "123",
        "345",
        "567",
        "781",
    }

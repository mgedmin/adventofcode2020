from part2 import valid_passport


def test_valid_passport():
    assert valid_passport({
        "pid": "087499704", "hgt": "74in", "ecl": "grn", "iyr": "2012", "eyr":
        "2030", "byr": "1980", "hcl": "#623a2f",
    })

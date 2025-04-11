"""Testing for dictionary function practice."""

__author__: str = "730654352"


from exercises.ex03.dictionary import invert, count, favorite_color, bin_len


def test_invert():
    assert invert({"a": "b", "c": "d"}) == {"b": "a", "d": "c"}


def test_invert2():
    assert invert({"P": "R", "H": "P", "B": "M"}) == {"R": "P", "P": "H", "M": "B"}


def test_invert3():
    assert invert({"a": "b", "b": "a", "z": "x"}) == {"b": "a", "a": "b", "x": "z"}


def test_count():
    assert count(["a", "a", "a", "b"]) == {"a": 3, "b": 1}


def test_count2():
    assert count([]) == {}


def test_count3():
    assert count(["a", "b", "c", "d"]) == {"a": 1, "b": 1, "c": 1, "d": 1}


def test_favorite_color():
    assert favorite_color({"Ron": "green", "Dan": "red", "Brian": "red"}) == "red"


def test_favorite_color2():
    assert favorite_color({"Ron": "green", "Dan": "red", "Brian": "green"}) == "green"


def test_favorite_color3():
    assert (
        favorite_color(
            {"Ron": "green", "Dan": "red", "Brian": "red", "Rachel": "green"}
        )
        == "green"
    )


def test_bin_len():
    assert bin_len(["the", "quick", "fox"]) == {3: {"the", "fox"}, 5: {"quick"}}


def test_bin_len2():
    assert bin_len(["the", "the", "fox"]) == {3: {"the", "fox"}}


def test_bin_len3():
    assert bin_len(["dog", "cat", "crow", "bunny"]) == {
        3: {"dog", "cat"},
        4: {"crow"},
        5: {"bunny"},
    }

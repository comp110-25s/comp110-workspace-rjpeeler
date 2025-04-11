"""Dictionary function practice."""

__author__: str = "730654352"


def invert(dictionary: dict[str, str]) -> dict[str, str]:
    inverted: dict[str, str] = {}
    for key in dictionary:
        value: str = dictionary[key]
        if value in inverted:
            raise KeyError
        else:
            inverted[value] = key
    return inverted


def count(list: list[str]) -> dict[str, int]:
    count_dict: dict[str, int] = {}
    for item in list:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1
    return count_dict


def favorite_color(namescolors: dict[str, str]) -> str:
    color_list: list[str] = []
    for name in namescolors:
        color_list.append(namescolors[name])
    color_counts: dict[str, int] = count(color_list)
    max_color: str = ""
    max_count: int = 0
    for color in color_counts:
        if color_counts[color] > max_count:
            max_color = color
            max_count = color_counts[color]
    return max_color


def bin_len(strings: list[str]) -> dict[int, set[str]]:
    bins: dict[int, set[str]] = {}
    for string in strings:
        length = len(string)
        if length not in bins:
            bins[length] = {string}
        else:
            bins[length].add(string)
    return bins

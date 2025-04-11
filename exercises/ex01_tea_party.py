"""Tea party planning program."""

__author__: str = "730654352"


def tea_bags(people: int) -> int:
    """Determine how many tea bags are needed for the party."""
    return 2 * people


def treats(people: int) -> int:
    """Determine how many treats are needed for the party."""
    return int(1.5 * tea_bags(people=people))


def cost(tea_count: int, treat_count: int) -> float:
    """Determine the total cost of the tea and the treats combined."""
    return tea_count * 0.5 + treat_count * 0.75


def main_planner(guests: int) -> None:
    """Prints information relevant to the tea party."""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party?")))

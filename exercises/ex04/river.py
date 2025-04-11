"""File to define River class."""

__author__: str = "730654352"

from exercises.ex04.bear import Bear
from exercises.ex04.fish import Fish


class River:
    day: int
    bears: list[Bear]
    fish: list[Fish]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears"""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        surviving_bears = []
        surviving_fish = []
        for bears in self.bears:
            if Bear.age <= 5:
                surviving_bears.append(bears)
        for fish in self.fish:
            if Fish.age <= 3:
                surviving_fish.append(fish)
        self.bears = surviving_bears
        self.fish = surviving_fish
        return None

    def bears_eating(self):
        for bears in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
                bears.eat(3)
        return None

    def check_hunger(self):
        surviving_bears = []
        for bears in self.bears:
            if Bear.hunger_score >= 0:
                surviving_bears.append(bears)
        self.bears = surviving_bears
        return None

    def repopulate_fish(self):
        return None

    def repopulate_bears(self):
        return None

    def view_river(self):
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None

    def one_river_day(self):
        """Simulate one day of life in the river"""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        """Simulate one week of life in the river"""
        n = 0
        while n < 7:
            self.one_river_day()
            n += 1
        return None

    def remove_fish(self, amount: int):
        i = amount - 1
        while i > -1:
            self.fish.pop(amount - 1)
            amount -= 1
        return None

# https://leetcode.com/problems/design-a-food-rating-system/
from heapq import heappop, heappush
from typing import List

from tester import ObjectTester


class FoodRatings:
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.items = {}
        self.food_to_cuisine = {}
        self.food_rating = {}
        for rating, food, cuisine in zip(ratings, foods, cuisines):
            if cuisine not in self.items:
                self.items[cuisine] = []
            heappush(self.items[cuisine], [-rating, food])
            self.food_rating[food] = -rating
            self.food_to_cuisine[food] = cuisine

    def changeRating(self, food: str, newRating: int) -> None:
        cuisine = self.food_to_cuisine[food]
        details = self.items[cuisine]
        heappush(details, [-newRating, food])
        self.food_rating[food] = -newRating

    def highestRated(self, cuisine: str) -> str:
        details = self.items[cuisine]
        while details[0][0] != self.food_rating[details[0][1]]:
            heappop(details)
        return details[0][1]


if __name__ == "__main__":
    o = ObjectTester(__file__)
    o.test(
        [
            None,
            None,
            None,
            None,
            None,
            None,
            None,
        ],
        [
            "FoodRatings",
            "changeRating",
            "changeRating",
            "changeRating",
            "highestRated",
            "highestRated",
            "highestRated",
        ],
        [
            [
                ["xucxenyckh", "rmzka", "kiesprtv"],
                ["oqinnmfsaf", "tgeb", "onzfzqjw"],
                [8, 4, 3],
            ],
            ["rmzka", 8],
            ["rmzka", 8],
            ["rmzka", 5],
            ["onzfzqjw"],
            ["oqinnmfsaf"],
            ["onzfzqjw"],
        ],
    )
    o.test(
        [None, "kimchi", "ramen", None, "sushi", None, "ramen"],
        [
            "FoodRatings",
            "highestRated",
            "highestRated",
            "changeRating",
            "highestRated",
            "changeRating",
            "highestRated",
        ],
        [
            [
                ["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"],
                ["korean", "japanese", "japanese", "greek", "japanese", "korean"],
                [9, 12, 8, 15, 14, 7],
            ],
            ["korean"],
            ["japanese"],
            ["sushi", 16],
            ["japanese"],
            ["ramen", 16],
            ["japanese"],
        ],
    )
    o.report()

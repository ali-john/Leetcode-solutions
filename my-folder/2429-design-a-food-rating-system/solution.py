from sortedcontainers import SortedSet
class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.foods_table = defaultdict(list)
        self.cuisines_table  = defaultdict(SortedSet)

        for food,rating,cuisine in zip(foods,ratings, cuisines):
            self.foods_table[food] = [rating, cuisine]
            self.cuisines_table[cuisine].add((-rating, food))
        

    def changeRating(self, food: str, newRating: int) -> None:
        prev_rating, cuisine = self.foods_table[food][0], self.foods_table[food][1]
        self.foods_table[food][0] = newRating
        self.cuisines_table[cuisine].remove((-prev_rating, food))
        self.cuisines_table[cuisine].add((-newRating, food))
        

 
    def highestRated(self, cuisine: str) -> str:
        return self.cuisines_table[cuisine][0][1]
        


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)

class Client:
    def __init__(self, index, likedIngredients, dislikedIngredients):
        tmp = likedIngredients.split(" ")
        tmpD = dislikedIngredients.split(" ")
        self.index = int(index + 1)
        self.likedIngredientsCount = int(tmp[0])
        self.dislikedIngredientsCount = int(tmpD[0])
        self.likedIngredients = tmp[1:]
        self.dislikedIngredients = tmpD[1:]

    def __repr__(self) -> str:
        print(f"Client {self.index}  likes {self.likedIngredientsCount} ingredients")
        for i in range(self.likedIngredientsCount):
            print(self.likedIngredients[i])
        print(f"Client {self.index} dislikes {self.dislikedIngredientsCount} ingredients")
        for i in range(self.dislikedIngredientsCount):
            print(self.dislikedIngredients[i])
        return ''

    def hasdislikedingredient(self):
        return self.dislikedIngredientsCount > 0

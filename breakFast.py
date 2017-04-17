
def makeBreakFast(ingredients, foodType):
    for ingredient in ingredients:
        print ingredient
    return 'Yummy '+foodType

ingredients = []
ingredientsEgg = ('Collect the ingredients', 
'mix the ingredients','heat the frying pan',
'add oil and when it\'s warm add the mixture',
'when one side is ready flip the egg to the other side',
'when both sides are ready, remove the pan from the heat')
ingredientsPancake = ('Collect the ingredients', 
'mix the ingredients','heat the frying pan',
'add oil and when it\'s warm add the mixture',
'when one side is ready flip the egg to the other side',
'when both sides are ready, remove the pan from the heat')

print makeBreakFast(ingredientsEgg, 'pancake')

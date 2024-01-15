import requests

# Function to search for recipes based on ingredient
def search_recipes(ingredient, max_ingredients):
    # Edamam API credentials
    app_id = 'bac70829'
    app_key = '282294319c61281527dce5129865c2cc'

    # API URL for recipe search
    url = 'https://api.edamam.com/search?q={}&app_id={}&app_key={}'.format(ingredient,app_id,app_key)

    # Send retrieval request to the API
    response = requests.get(url)

    # Check that the response was successful. If response status code was not 200, this means there was an error.
    if response.status_code == 200:
        data = response.json()

        # Filter based on number of ingredients
        filtered_hits = [hit for hit in data['hits'] if len(hit['recipe']['ingredientLines']) <= max_ingredients]

        # Extract and display the recipe information
        # Number of Calories rounded to two decimal places
        for hit in filtered_hits:
            recipe = hit['recipe']
            calories = round(recipe['calories'], 2)
            print('---')
            print('Title:', recipe['label'])
            print('URL:', recipe['url'])
            print('Image:', recipe['image'])
            print('Number of Ingredients: ', len(recipe['ingredientLines']))
            print('Calories', calories)
            print('---')

    else:
        print('Error occurred while accessing the API.')

# Ask the user to enter an ingredient
ingredient = input("Enter an ingredient: ")

# Ask the user to enter a maximum number of ingredients
max_ingredients = int(input("Enter the maximum number of ingredients: "))

# Call the search_recipes function (line 5)
search_recipes(ingredient, max_ingredients)

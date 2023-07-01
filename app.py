from flask import Flask, render_template
import time

app = Flask(__name__)

recipes = [
    {
        'title': 'Pasta Carbonara',
        'ingredients': ['spaghetti', 'bacon', 'eggs', 'cheese', 'black pepper'],
        'instructions': 'Lorem ipsum dolor sit amet...'
    },
    {
        'title': 'Chicken Parmesan',
        'ingredients': ['chicken breasts', 'breadcrumbs', 'marinara sauce', 'mozzarella cheese'],
        'instructions': 'Lorem ipsum dolor sit amet...'
    },
    # Add more recipe data as needed
]

@app.route('/')
def home():
    start_time = time.time()
    # Your application logic here
    # ...
    return render_template('index.html', recipes=recipes)
    response = render_template('index.html', recipes=recipes)
    end_time = time.time()
    response_time = end_time - start_time
    # Log the response time
    app.logger.info(f"Response time for home route: {response_time} seconds")
    return response
    
@app.route('/recipe/<title>')
def recipe(title):
    # Find the recipe with the given title
    start_time = time.time()

    # Your application logic here
    # ...

    # Find the recipe with the given title
    recipe = next((r for r in recipes if r['title'].lower() == title.lower()), None)

    if recipe:
        response = render_template('recipe.html', recipe=recipe)
    else:
        response = 'Recipe not found'

    end_time = time.time()
    response_time = end_time - start_time

    # Log the response time
    app.logger.info(f"Response time for recipe route: {response_time} seconds")

    return response

if __name__ == '__main__':
    app.run(debug=True)

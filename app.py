from flask import Flask, render_template

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
    return render_template('index.html', recipes=recipes)

@app.route('/recipe/<title>')
def recipe(title):
    # Find the recipe with the given title
    recipe = next((r for r in recipes if r['title'].lower() == title.lower()), None)

    if recipe:
        return render_template('recipe.html', recipe=recipe)
    else:
        return 'Recipe not found'

if __name__ == '__main__':
    app.run(debug=True)

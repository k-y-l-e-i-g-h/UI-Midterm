from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)
app.static_folder = 'static'

current_id = 11

data = [
    {
        "id": 1,
        "title": "Octopus Toy",
        "description" : "This is an octopus cat toy that I bought for Mimi at the local pet store a year or two ago. It is about the size of a cup of yogurt, and colored in purple and pink with soft, corduroy-like material with two large eyeballs. It has a fun crinkle sound to encourage play, and supposedly came infused with catnip for extra excitement.",
        "image": "https://image.chewy.com/is/image/catalog/91353_MAIN._AC_SL1200_V1539005297_.jpg",
        "price": "$8.99",
        "review": "While the initial meet and greet with the octopus went well due to the catnip infusion, Mimi has not touched this toy since that day. The dog seems to enjoy it more, so we let him play with it instead.",
        "rating": 3.4,
        "alternatives": ["Bottle cap", "Rubber band", "Earrings", "Small scraps of paper"]
    },
    {
        "id": 2,
        "title": "Electric Lady Bug Toy",
        "description" : "This is a lady bug cat toy that I bought for Mimi at the local pet store a year or two ago. It is about the size of a healthy cockroach, and colored in black and red, made of hard plastic material. It comes with a small battery that makes the toy vibrate, making it travel along the floor like a real bug. Meant to provide stimulation and exercise without the hassle of tossing a string in the air.",
        "image": "https://m.media-amazon.com/images/I/31A4NAQiJEL._AC_SX679_.jpg",
        "price": "$12.99",
        "review": "I will say Mimi found this toy very interesting, however she never chased after it-- she simply sat and watched it buzz around the floor. It ran out of battery quite quickly and I have not found a replacement since.",
        "rating": 4.0,
        "alternatives": ["Real bug", "Coins"]
    },
    {
        "id": 3,
        "title": "Wand Toy",
        "description" : "This toy will probably go down in history as the quintissential cat toy. This one in particular was a clear string attached to a long platsic stick with a fuzzy, brightly-colored worm-like animal on the end of it. It is meant to stimulates your kitty's natural hunting instincts to spark up play and exercise. This toy is the perfect way to provide cats with the daily exercise and mental stimulation they need.",
        "image": "https://m.media-amazon.com/images/I/615Ccf+wziL._AC_SX679_.jpg",
        "price": "$9.98",
        "review": "This toy was probably one of Mimi's favorites when she was young. She would chase that worm like nothing I had ever seen. Unofortunately, the worm did brak off of the string after a month or two.",
        "rating": 4.8,
        "alternatives": ["Shoe lace", "Hempwick", "Thread"]
    },
    {
        "id": 4,
        "title": "Cat Tree",
        "description" : "This cat tree (along with every other one in my house) was found on the bountiful streets of NYC. This cat tree provides your feline friends with a cozy place to lounge and play. The freestanding design features an engineered wood frame wrapped in textured faux fur and sisal rope for a scratch-resistant surface. With three tiers, it includes a condo, three perches, and a scratching pad for endless entertainment. The brown and lime green color scheme adds a touch of tropical warmth to your home decor.",
        "image": "https://assets.wfcdn.com/im/27838570/timg-h1000-w1000%5Ecompr-r85/1978/197825567/43.31%27%27+H+Timms+Cat+Tree.jpg",
        "price": "FREE!",
        "review": "Similar to everything else I buy her, Mimi loved this tree for a few days-- I never saw her sit any where else for a good 72 hours. However, this effect did not last as she will not so much as look at it unless I smother the fabric in catnip. But it does look very cute and chique in the corner of my bedroom!",
        "rating": 3.0,
        "alternatives": ["Couch", "Bed", "Kitchen table"]
    },
    {
        "id": 5,
        "title": "Premium Pet Water Fountain",
        "description" : "This item is an automatic water fountain that I found on Amazon's website. It holds 2.5 liters of water and constantly filters it. It is equipped with a water level window and fountain mode, matching the drinking habits of cats and dogs from the faucet. The fountain is made of food-grade BPA-free plastic to ensure pet safety.",
        "image": "https://m.media-amazon.com/images/I/81-YlzDxojL._AC_SX679_.jpg",
        "price": "$35.99",
        "review": "Besides her automatic feeder, this has probably been the best purchase I have made for Mimi. She has always been an avid water drinker, and this product allows for unlimited supply, and even filters out her fur from pawing at the pool. Only complaint is that it is hard to clean.",
        "rating": 4.8,
        "alternatives": ["Bowl", "Large mug", "* Nothing really beats it though *"]
    },
    {
        "id": 6,
        "title": "Cat Dancer Toy",
        "description" : "This toy, gifted to me by a friend, is a very unique one-- the 'dancer' has a natural curve makes it bounce erratically when you wiggle it around to get your cat excited about play. It helps provide daily exercise and mental stimulation for cats by activating their hunting instincts, plus it's an excellent bonding activity.",
        "image": "https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=1200,height=672,format=auto/https://doordash-static.s3.amazonaws.com/media/photosV2/f30d732a-f0f6-4010-ad6e-26cf90a9b53a-retina-large.png",
        "price": "$2.99",
        "review": "Mimi loves this toy! While the best part about it is that she can play with it by herself, it does take some initiation from me to get her going. It also comes with an attachment mechanism, making it easy to place on a wall or sturdy furniture.",
        "rating": 4.6,
        "alternatives": ["Shoe lace tied to a bottlecap", "Chord with loose tape", "Flowers"]
    },
    {
        "id": 7,
        "title": "Temptations Cat Treats",
        "description" : "These treats I have bought a few packs of from CVS. They come in multiple flavors, each of which has less than 2 calories and provides a combination of both crunchy and soft textures. These healthy cat treats also come in a cat-proof, stay-fresh pouch, so your feline friend can enjoy their favorite snack when you open it, but never when they shouldn't!",
        "image": "https://www.temptationstreats.com/cdn-cgi/image/width=600,height=600,f=auto,quality=90/sites/g/files/fnmzdf3061/files/migrate-product-files/images/jraobbkkworgewjstr9s.png",
        "price": "$2.58",
        "review": "When I first adopted Mimi, I came to realize that she doesn't really f**k with manufactured cat treats. These especially, with the hard exterior, are difficult for her to chew, leading to her discarding them on the floor.",
        "rating": 1.7,
        "alternatives": ["Cheese", "Canned tuna", "Baked Salmon", "Roasted chicken"]
    },
    {
        "id": 8,
        "title": "LickiMat",
        "description" : "This item I found at a local pet store when Mimi was experiencing vomiting due to eat too fats. It helps to mimic feeding like your kitty would experience in the wild with a natural crouch and prolonged meal experience. It is whisker friendly and promotes slower eating to reduce gulping.",
        "image": "https://image.chewy.com/is/image/catalog/654654_PT1._AC_SL1200_V1667241319_.jpg",
        "price": "$21.99",
        "review": "This item was the answer to our prayers (or so we thought). Turns out Mimi eats her dry food too fast, not the wet food which we so delicately spread onto this mat every evening. I don't even know why we still use it, but I have faith in the desciption!",
        "rating": 3.0,
        "alternatives": ["Small plate", "Bowl", "Any dish really"]
    },
    {
        "id": 9,
        "title": "PETLIBRO Automatic Feeder",
        "description" : "This item I ordered off Amazon when I knew I would be out of town for a while. The PETLIBRO AIR automatic cat feeder's top lid has a press-to-lock button to firmly lock the food tank and features a control panel cover to prevent accidental button presses from pets. It can run on both batteries and wall power.",
        "image": "https://m.media-amazon.com/images/I/61xZGeIJgiL._AC_SY879_.jpg",
        "price": "$44.07",
        "review": "This has got to be my #1 purchase for Mimi thus far. It took her a while to understand that I was no longer the one she needed to beg for dry food, but now she is a changed woman and runs for the bowl as soon as she hears the auto-feeder dispense her kibble. It saved a lot of stress for both of us.",
        "rating": 5.0,
        "alternatives": ["Bowl and scooper", "Just buy it already!"]
    },
    {
        "id": 10,
        "title": "Reusable Pet Hair Remover",
        "description" : "This item I ordered through an Instagram advertisment is quite immpecable. It helps to quickly and easily remove cat and dog hair from furniture, carpet, car seats and more by simply dragging the metal edge across the furry area. The special edges collect pet hair, lint, and dust in seconds, as well as easy to use and infinitely reusable.",
        "image": "https://img.kwcdn.com/product/1e23311c28/adc81f2e-d7a4-4eca-bf9a-dbcefe3db6be_800x800.png?imageView2/2/w/800/q/70",
        "price": "$5.99",
        "review": "This tool is fantastic! It helps to clean excess fur off of Mimi's cat trees and other spots she tends to frequent around the house. My main complaint would just be how tired my arm gets while trying the rid the entire living room area rug of cat fur. Mimi does not care much for it, however.",
        "rating": 4.5,
        "alternatives": ["Vacuum", "Hands", "Duct tape"]
    },
]

# Define the highlight filter
def highlight(text, query):
    return text.replace(query, f'<span class="highlight">{query}</span>')

# Register the filter with Jinja2
app.jinja_env.filters['highlight'] = highlight

# ROUTES
@app.route('/')
def home():
   return render_template('home.html')   

@app.route('/search', methods=['GET'])
def search():

    query = request.args.get('query').strip()
    if not query:  # If search query is empty or whitespace
        return render_template('search.html', query="", results=[], message="Please enter a valid search query.")
    
    # Search for items containing the search query in their title, description, or review
    search_results = []
    for item in data:
        # Check if the query matches the title, description, or any review
        if (query.lower() in item['title'].lower() or 
            query.lower() in item['description'].lower() or 
            query.lower() in item['review'].lower()):
            search_results.append(item)
    
    if not search_results:
        message = "No results found."
    else:
        message = f"Showing results for '{query}'."
    
    return render_template('search.html', query=query, results=search_results, message=message)

@app.route('/view/<int:id>')
def view_item(id):
    item = next((item for item in data if item['id'] == id), None)
    if item:
        return render_template('view_item.html', item=item)
    else:
        return "Item not found", 404
    
# Define the route for adding data
@app.route('/add', methods=['GET', 'POST'])
def add_item():
    if request.method == 'POST':
        # Handle form submission
        title = request.form.get('title')
        description = request.form.get('description')
        image = request.form.get('image')
        price = request.form.get('price')
        review = request.form.get('review')
        rating = request.form.get('rating')
        alternatives = request.form.get('alternatives')
        
        if not title or not description:
            # Return error response if required fields are empty
            return jsonify({'error': 'Title and description are required.'}), 400
        
        alternatives_list = alternatives.split(',')
        # Generate a unique ID for the new item
        global current_id
        current_id += 1
        new_item = {
            "id": current_id,
            "title": title,
            "description": description,
            "image": image,
            "price": price,
            "review": review,
            "rating": rating,
            "alternatives": alternatives_list
        }
        
        # Append the new item to the data list
        data.append(new_item)
        
        # Return success response
        return render_template('add_item.html', success_message='New item successfully created.', new_item_id=current_id)

    # Render the template for adding a new item
    return render_template('add_item.html')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_item(id):
    # Find the item to edit based on the provided ID
    item = next((item for item in data if item['id'] == id), None)
    if not item:
        return "Item not found", 404
    
    if request.method == 'POST':
        # Handle form submission to update the item
        title = request.form.get('title')
        description = request.form.get('description')
        image = request.form.get('image')
        price = request.form.get('price')
        review = request.form.get('review')
        rating = request.form.get('rating')
        alternatives = request.form.get('alternatives')
        
        if not title or not description:
            return jsonify({'error': 'Title and description are required.'}), 400
        
        alternatives_list = alternatives.split(',')
        # Update the item's data
        item.update({
            "title": title,
            "description": description,
            "image": image,
            "price": price,
            "review": review,
            "rating": rating,
            "alternatives": alternatives_list
        })
        
        # Return success response
        return render_template('view_item.html', item=item)
    
    # Check if the discard changes button was clicked
    if request.args.get('action') == 'discard':
        # Redirect to the view item page without making any changes
        return render_template('view_item.html', item=item)
    
    # Render the template for editing the item
    return render_template('edit_item.html', item=item)

if __name__ == '__main__':
   app.run(debug = True)

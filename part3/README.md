cat > README.md << 'EOF'
# HBnB - Part 3

This is the same AirBnB-style app from Part 2, but now with login and a real
database.

Part 2 kept everything in memory. Part 3 adds:
- Passwords that are hashed (not saved as plain text)
- Login with JWT tokens, so only the right user can change their stuff
- A real database with SQLAlchemy instead of in-memory storage

## What it does

Four main things: users, places, reviews, and amenities.
You can create, read, list, and update them. Reviews can also be deleted.
Now some actions also need you to be logged in.

## How it is built

- `app/api/` - the API endpoints
- `app/models/` - the classes (User, Place, Review, Amenity)
- `app/services/` - the facade that connects the layers
- `app/persistence/` - where the data is stored
- `config.py` - the app settings, loaded in the app factory

## How to run it

Install the requirements:

    pip install -r requirements.txt

Run the app:

    python3 run.py

Then open http://127.0.0.1:5000/api/v1/ to see the API docs.

## How to test it

    python3 -m unittest discover

## Author

Karen Navarro
EOF
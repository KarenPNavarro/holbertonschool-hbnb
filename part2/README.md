# HBnB - Part 2

This is a simple AirBnB-style app. It is a REST API built with Flask.

You can manage users, places, reviews, and amenities through the API.

## What it does

There are four main things:
- Users – people who use the app
- Places – properties a user lists
- Reviews – feedback a user leaves on a place
- Amenities – features a place can have, like wifi

For each one you can create it, read it, list them all, and update it.
Reviews can also be deleted.

## How it is built

The code is split into layers:
- `app/api/` – the API endpoints
- `app/models/` – the classes (User, Place, Review, Amenity)
- `app/services/` – the facade that connects the layers
- `app/persistence/` – where the data is stored (in memory for now)

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
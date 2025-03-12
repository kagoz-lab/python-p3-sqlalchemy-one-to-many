#!/usr/bin/env python3

from faker import Faker
import random

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Game, Review, Base

engine = create_engine('sqlite:///one_to_many.db')
Session = sessionmaker(bind=engine)
session = Session()

fake = Faker()

# Create sample games
games = []
for _ in range(10):  # Increased from 5 to 10
    game = Game(
        title=fake.catch_phrase(),
        genre=fake.word(),
        platform=fake.word(),
        price=random.randint(20, 60)
    )
    games.append(game)
    session.add(game)

# Create tables in the database
Base.metadata.create_all(engine)

# Commit games to the database
session.commit()

# Create sample reviews with variability
for game in games:
    num_reviews = random.randint(1, 5)  # Random number of reviews between 1 and 5
    for _ in range(num_reviews):
        review = Review(
            score=random.randint(1, 10),
            comment=fake.sentence(),
            game_id=game.id
        )
        session.add(review)

# Commit reviews to the database
session.commit()

print("Database seeded with sample data.")

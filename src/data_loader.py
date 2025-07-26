# IMPORTANT ! DO NOT MODIFY THIS FILE AS THIS CONTAINS THE SOURCE OF DATASETS

import pandas as pd

def _load_listings_data():
    """
    Returns the Airbnb listings dataset as a pd.DataFrame.
    """
    return pd.read_csv("https://storage.googleapis.com/public-data-337819/listings%202%20reduced.csv", low_memory=False)

def _load_reviews_data():
    """
    Returns the Airbnb reviews dataset as a pd.DataFrame.
    """
    return pd.read_csv("https://storage.googleapis.com/public-data-337819/reviews%202%20reduced.csv", low_memory=False)

def load_data():
    """
    Returns the Airbnb listings and reviews datasets as a tuple of pd.DataFrame.
    """
    return _load_listings_data(), _load_reviews_data()
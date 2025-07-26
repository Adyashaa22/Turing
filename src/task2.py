import pandas as pd
from data_loader import load_data

# Write your code here
def review_score_with_highest_correlation_to_price(df_listings: pd.DataFrame, df_reviews: pd.DataFrame) -> str:
    # Clean the 'price' column
    df_listings['price'] = df_listings['price'].replace('[\$,]', '', regex=True).astype(float)

    # Select relevant columns
    score_columns = [
        'review_scores_rating',
        'review_scores_accuracy',
        'review_scores_cleanliness',
        'review_scores_checkin',
        'review_scores_communication',
        'review_scores_location',
        'review_scores_value'
    ]

    # Drop rows with NaN in any relevant column
    df_clean = df_listings[['price'] + score_columns].dropna()

    # Compute correlations with price
    correlations = df_clean[score_columns + ['price']].corr()['price'].drop('price')

    # Get column with highest absolute correlation
    result = correlations.abs().idxmax()

    return result
''' 
MANDATORY - Explain your solution in plain english here
This function calculates the correlation between the price and each review score column.
It first cleans the price column and removes missing data.
Then it computes correlations and identifies the review score that has the strongest (positive or negative) relationship with price.


COMMENTS END
'''

if __name__ == '__main__':
    print('Review score with max correlation to price is: ', review_score_with_highest_correlation_to_price(*load_data()))
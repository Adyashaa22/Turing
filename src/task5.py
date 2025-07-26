import pandas as pd
from data_loader import load_data

# Write your code here
def listing_with_best_expected_revenue(df_listings: pd.DataFrame, df_reviews: pd.DataFrame) -> int:
    df_listings['price'] = df_listings['price'].replace('[\$,]', '', regex=True).astype(float)

    # Filter listings with minimum nights <= 7
    df_listings = df_listings[df_listings['minimum_nights'] <= 7]

    # Count number of reviews in past 12 months per listing
    df_reviews['date'] = pd.to_datetime(df_reviews['date'])
    recent_reviews = df_reviews[df_reviews['date'] >= pd.Timestamp.now() - pd.DateOffset(months=12)]
    review_counts = recent_reviews.groupby('listing_id').size().rename('review_count')

    # Merge review counts into listings
    df = df_listings.merge(review_counts, left_on='id', right_on='listing_id', how='left')
    df['review_count'] = df['review_count'].fillna(0)

    # Calculate expected revenue
    df['expected_revenue'] = df['price'] * (df['review_count'] / 0.6) * df['minimum_nights']

    # Get listing ID with highest expected revenue
    result = df.loc[df['expected_revenue'].idxmax(), 'id']
    return int(result)

''' 
MANDATORY - Explain your solution in plain english here

We estimate expected revenue by multiplying price, adjusted guest count, and minimum nights.
We filter listings with minimum_nights ≤ 7 and use reviews from the last 12 months to estimate guest count.
Then we return the listing with the highest expected revenue.









COMMENTS END
'''

if __name__ == '__main__':
    print('Listing with best expected revenue is: ', listing_with_best_expected_revenue(*load_data()))
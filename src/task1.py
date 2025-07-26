import pandas as pd
from data_loader import load_data

# Write your code here
def neighbourhood_with_highest_median_price_diff(df_listings: pd.DataFrame, df_reviews: pd.DataFrame) -> str:
    # Clean 'price' column to convert to float
    df_listings['price'] = df_listings['price'].replace('[\$,]', '', regex=True).astype(float)

    # Group by neighbourhood and superhost status, calculate median
    median_prices = df_listings.groupby(['neighbourhood_cleansed', 'host_is_superhost'])['price'].median().unstack()

    # Drop rows where either 't' or 'f' is missing
    median_prices = median_prices.dropna()

    # Calculate absolute difference between superhost and non-superhost median prices
    median_prices['diff'] = (median_prices['t'] - median_prices['f']).abs()

    # Get the neighbourhood with the highest difference
    result = median_prices['diff'].idxmax()

    return result

''' 
MANDATORY - Explain your solution in plain english here
This function calculates the median rental price for superhosts and non-superhosts in each neighborhood.
It first cleans the price column, then groups the data by neighborhood and host type to compute medians.
It calculates the absolute difference in median prices and returns the neighborhood with the largest difference.

COMMENTS END
'''

if __name__ == '__main__':
    print('Neighborhood with highest price difference: ', neighbourhood_with_highest_median_price_diff(*load_data()))
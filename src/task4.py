import pandas as pd
from data_loader import load_data

# Write your code here
def price_premium_for_entire_homes(df_listings: pd.DataFrame, df_reviews: pd.DataFrame) -> float:
    # Clean price column
    df_listings['price'] = df_listings['price'].replace('[\$,]', '', regex=True).astype(float)

    # Filter out rows with nulls in important columns
    df_listings = df_listings.dropna(subset=['price', 'room_type', 'neighbourhood_cleansed'])

    premium_diffs = []

    for neighborhood, group in df_listings.groupby('neighbourhood_cleansed'):
        entire_home_prices = group[group['room_type'] == 'Entire home/apt']['price']
        other_prices = group[group['room_type'] != 'Entire home/apt']['price']

        if not entire_home_prices.empty and not other_prices.empty:
            median_entire = entire_home_prices.median()
            median_other = other_prices.median()
            premium_diffs.append(median_entire - median_other)

    if premium_diffs:
        return round(sum(premium_diffs) / len(premium_diffs), 2)
    else:
        return 0.0


''' 
MANDATORY - Explain your solution in plain english here
This function compares median prices of "Entire home/apt" listings with other listing types within each neighborhood.
It calculates the premium (difference) in median price for each neighborhood and then averages those differences.
The final result is the average price premium for entire homes across all neighborhoods.


COMMENTS END
'''

if __name__ == '__main__':
    print('Price premium for entire homes is: ', price_premium_for_entire_homes(*load_data()))
import pandas as pd
from data_loader import load_data

# Write your code here
def prof_nonprof_host_price_diff(df_listings: pd.DataFrame, df_reviews: pd.DataFrame) -> float:
    df_listings['price'] = df_listings['price'].replace('[\$,]', '', regex=True).astype(float)

    # Count number of unique neighborhoods per host
    host_neigh_count = df_listings.groupby('host_id')['neighbourhood_cleansed'].nunique()

    # Identify professional hosts
    prof_hosts = host_neigh_count[host_neigh_count > 5].index

    # Label listings as professional or not
    df_listings['is_professional'] = df_listings['host_id'].isin(prof_hosts)

    # Calculate average price for both groups
    avg_prof = df_listings[df_listings['is_professional'] == True]['price'].mean()
    avg_nonprof = df_listings[df_listings['is_professional'] == False]['price'].mean()

    # Return the price difference
    return round(abs(avg_prof - avg_nonprof), 2)

''' 
MANDATORY - Explain your solution in plain english here

This function identifies professional hosts as those who have listings in more than 5 unique neighborhoods.
It calculates the average price of listings for both professional and non-professional hosts.
Then it returns the absolute difference between the two averages.

COMMENTS END
'''

if __name__ == '__main__':
    print('Professional Host Analysis: ', prof_nonprof_host_price_diff(*load_data()))
import pandas as pd
from data_loader import load_data

# Write your code here
def listing_with_best_expected_revenue(df_listings: pd.DataFrame, df_reviews: pd.DataFrame) -> int:
    return -1

''' 
MANDATORY - Explain your solution in plain english here



COMMENTS END
'''

if __name__ == '__main__':
    print('Listing with best expected revenue is: ', listing_with_best_expected_revenue(*load_data()))
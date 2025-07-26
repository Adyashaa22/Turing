import pandas as pd
from data_loader import load_data

# Write your code here
def host_attribute_with_second_highest_correlation_to_reviews(df_listings: pd.DataFrame, df_reviews: pd.DataFrame) -> str:
    return ''


''' 
MANDATORY - Explain your solution in plain english here



COMMENTS END
'''

if __name__ == '__main__':
    print('Host attribute with second highest correlation to reviews is: ', host_attribute_with_second_highest_correlation_to_reviews(*load_data()))
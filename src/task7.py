import pandas as pd
from data_loader import load_data

# Write your code here
def host_attribute_with_second_highest_correlation_to_reviews(df_listings: pd.DataFrame, df_reviews: pd.DataFrame) -> str:
    columns = [
        'host_since',
        'host_listings_count',
        'host_identity_verified',
        'calculated_host_listings_count',
        'host_is_superhost'
    ]

    df = df_listings[columns + ['number_of_reviews']].copy()

    # Preprocess non-numeric columns
    df['host_since'] = pd.to_datetime(df['host_since'], errors='coerce').astype('int64')  # Convert to numeric (timestamp)
    df['host_identity_verified'] = df['host_identity_verified'].map({'t': 1, 'f': 0})
    df['host_is_superhost'] = df['host_is_superhost'].map({'t': 1, 'f': 0})

    # Drop rows with NaN values
    df.dropna(subset=columns + ['number_of_reviews'], inplace=True)

    # Calculate correlation of all attributes with number_of_reviews
    corr = df.corr(numeric_only=True)['number_of_reviews'].drop('number_of_reviews')

    # Get the second highest absolute correlation
    second_highest = corr.abs().sort_values(ascending=False).index[1]

    return second_highest

''' 
MANDATORY - Explain your solution in plain english here

- First, we selected the required host-related attributes along with 'number_of_reviews'.
- We converted categorical and datetime columns to numeric values so that we can calculate correlation.
- We cleaned the data by removing rows with missing values.
- Then, we calculated the correlation of each attribute with 'number_of_reviews'.
- After sorting the correlations by absolute strength, we picked the second-highest correlated attribute.
-Finally, we returned its name.

COMMENTS END
'''

if __name__ == '__main__':
    print('Host attribute with second highest correlation to reviews is: ', host_attribute_with_second_highest_correlation_to_reviews(*load_data()))
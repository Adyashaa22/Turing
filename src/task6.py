import pandas as pd
from data_loader import load_data

# Write your code here
def average_diff_superhost_nonsuperhost_review_score(df_listings: pd.DataFrame, df_reviews: pd.DataFrame) -> float:
    df = df_listings[['host_is_superhost', 'review_scores_rating']].dropna()

    # Split into superhosts and non-superhosts
    superhosts = df[df['host_is_superhost'] == 't']['review_scores_rating']
    non_superhosts = df[df['host_is_superhost'] == 'f']['review_scores_rating']

    # Calculate average difference
    diff = superhosts.mean() - non_superhosts.mean()

    return round(abs(diff), 2)

''' 
MANDATORY - Explain your solution in plain english here
We compare average 'review_scores_rating' for superhosts and non-superhosts.
After filtering missing values, we compute the difference in their mean scores and return the absolute value.

COMMENTS END
'''

if __name__ == '__main__':
    print('Average difference in review scores between super and non super hosts is: ', average_diff_superhost_nonsuperhost_review_score(*load_data()))
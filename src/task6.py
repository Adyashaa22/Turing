import pandas as pd
from data_loader import load_data

# Write your code here
def average_diff_superhost_nonsuperhost_review_score(df_listings: pd.DataFrame, df_reviews: pd.DataFrame) -> float:
    
    return 0.00

''' 
MANDATORY - Explain your solution in plain english here



COMMENTS END
'''

if __name__ == '__main__':
    print('Average difference in review scores between super and non super hosts is: ', average_diff_superhost_nonsuperhost_review_score(*load_data()))
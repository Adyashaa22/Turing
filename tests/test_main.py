## This file contains tests for each task, you can add custom tests if you want, but DO NOT MODIFY EXISTING TESTS.

import numpy as np
import pandas as pd
import unittest

import sys
sys.path.append('.')
sys.path.append('..')

class TestMain(unittest.TestCase):
    def setUpClass():
        
        TestMain.df_listings = pd.DataFrame({
            'id': [1, 2, 3, 4, 5],
            'name': ['Cozy Apartment', 'Modern House', 'Beachside Retreat', 'City Center Studio', 'Family Friendly Home'],
            'description': ['Charming apartment in the heart of the city', 'Spacious house with modern amenities', 'Relaxing beachside retreat with stunning views', 'Convenient studio in the city center', 'Spacious home perfect for families'],
            'host_id': [123, 456, 789, 1011, 1213],
            'host_is_superhost': ['f', 't', 'f', 'f', 'f'],
            'host_identity_verified': ['t', 't', 't', 'f', 't'],
            'host_since': ['2011-04-10', '2011-04-10', '2010-07-17', '2010-07-04', '2011-08-03'],
            'host_listings_count': [10, 20, 30, 15, 25],
            'calculated_host_listings_count': [10, 20, 28, 15, 22],
            'price': ['$100.00', '$1,500.00', '$200.00', '$25.00', '$180.00'],
            'neighbourhood_cleansed': ['Hollywood', 'Hollywood', 'South Beach', 'The Loop', 'Pacific Heights'],
            'country': ['US', 'US', 'US', 'US', 'US'],
            'property_type': ['Apartment', 'House', 'Condo', 'Studio', 'House'],
            'room_type': ['Private room', 'Entire home/apt', 'Entire home/apt', 'Private room', 'Entire home/apt'],
            'minimum_nights': [3, 5, 7, 3, 5],
            'review_scores_rating': [4.5, 4.8, 4.9, 4.7, 4.6],
            'review_scores_cleanliness': [4.5, 4.8, 4.9, 4.7, 4.6],
            'review_scores_checkin': [4.5, 4.8, 4.9, 4.7, 4.6],
            'review_scores_communication': [4.5, 4.8, 4.9, 4.7, 4.6],
            'review_scores_location': [4.5, 4.8, 4.9, 4.7, 4.6],
            'review_scores_value': [4.5, 4.8, 4.9, 4.7, 4.6],
            'review_scores_accuracy': [4.5, 4.8, 4.9, 4.7, 4.6],
            'number_of_reviews': [10, 20, 30, 15, 25],
        })

        TestMain.df_reviews = pd.DataFrame({
            'id': [10, 20, 30, 40, 50],
            'listing_id': [1, 2, 3, 4, 5],
            'date': ['2020-01-01', '2020-01-15', '2020-02-01', '2020-03-01', '2020-03-15'],
            'reviewer_id': [123, 456, 789, 1011, 1213],
            'reviewer_name': ['John', 'Jane', 'Bob', 'Alice', 'Mike'],
            'review': ['Great place!', 'Awesome host!', 'Clean and comfortable', 'Perfect location', 'Cozy apartment'],
            'rating': [5, 5, 4, 5, 4]
        })

    def _float_equals( a, b, epsilon=1e-9):
        return abs(a - b) < epsilon
    _float_equals = staticmethod(_float_equals)

    def test_task1(self):
        task1 = __import__('src.task1').task1
        result = task1.neighbourhood_with_highest_median_price_diff(TestMain.df_listings.copy(), TestMain.df_reviews.copy())
        self.assertEqual(result, 'Hollywood')

    def test_task2(self):
        task2 = __import__('src.task2').task2
        result = task2.review_score_with_highest_correlation_to_price(TestMain.df_listings.copy(), TestMain.df_reviews.copy())
        self.assertEqual(result, 'review_scores_rating')

    def test_task3(self):
        task3 = __import__('src.task3').task3
        result = task3.prof_nonprof_host_price_diff(TestMain.df_listings.copy(), TestMain.df_reviews.copy())
        self.assertTrue(TestMain._float_equals(result, -401.00, 0.1))

    def test_task4(self):
        task4 = __import__('src.task4').task4
        result = task4.price_premium_for_entire_homes(TestMain.df_listings.copy(), TestMain.df_reviews.copy())
        self.assertTrue(TestMain._float_equals(result, 1400.00, 0.1) )

    def test_task5(self):
        task5 = __import__('src.task5').task5
        result = task5.listing_with_best_expected_revenue(TestMain.df_listings.copy(), TestMain.df_reviews.copy())
        self.assertEqual(result, 0)
    
    def test_task6(self):
        task6 = __import__('src.task6').task6
        result = task6.average_diff_superhost_nonsuperhost_review_score(TestMain.df_listings.copy(), TestMain.df_reviews.copy())
        self.assertTrue(TestMain._float_equals(result, 0.12, 0.1) )
    
    def test_task7(self):
        task7 = __import__('src.task7').task7
        result = task7.host_attribute_with_second_highest_correlation_to_reviews(TestMain.df_listings.copy(), TestMain.df_reviews.copy())
        self.assertEqual(result, 'calculated_host_listings_count')

if __name__ == "__main__":
    unittest.main()

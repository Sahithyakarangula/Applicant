# Put your unit tests here
import unittest
import pandas as pd
import transform_data

class TestTransformData(unittest.TestCase):
    def setUp(self):
        # Sample posts data
        self.posts_data = [
            {"userId": 1, "id": 1, "title": "Test Post 1", "body": "This is a test post."},
            {"userId": 1, "id": 2, "title": "Test Post 2", "body": "This is another test post."},
            {"userId": 2, "id": 3, "title": "Test Post 3", "body": "Yet another test post."},
        ]
        # Sample users data
        self.users_data = [
            {"id": 1, "name": "User 1", "email": "user1@example.com"},
            {"id": 2, "name": "User 2", "email": "user2@example.com"},
        ]

    def test_parse_embedded_json(self):
        # Test if parse_embedded_json function works without errors
        posts = self.posts_data
        transform_data.parse_embedded_json(posts)
        # No assertion as it doesn't change data structure

    def test_add_status_field(self):
        # Test if add_status_field function correctly adds status field to posts
        posts = self.posts_data
        transform_data.add_status_field(posts)
        self.assertIn('status', posts[0])
        self.assertEqual(posts[0]['status'], 'concise')
        self.assertEqual(posts[1]['status'], 'concise')
        self.assertEqual(posts[2]['status'], 'lengthy')  # Longer than 100 characters

    def test_combine_posts_with_users(self):
        # Test if combine_posts_with_users function correctly combines posts with users
        posts = self.posts_data
        users = self.users_data
        combined_posts = transform_data.combine_posts_with_users(posts, users)
        self.assertIn('user', combined_posts[0])
        self.assertEqual(combined_posts[0]['user']['name'], 'User 1')
        self.assertEqual(combined_posts[1]['user']['name'], 'User 1')
        self.assertEqual(combined_posts[2]['user']['name'], 'User 2')

    def test_flatten_posts(self):
        # Test if flatten_posts function correctly flattens posts data into DataFrame
        posts = self.posts_data
        flattened_df = transform_data.flatten_posts(posts)
        self.assertIsInstance(flattened_df, pd.DataFrame)
        self.assertEqual(len(flattened_df), len(posts))
        self.assertIn('user_name', flattened_df.columns)
        self.assertIn('user_email', flattened_df.columns)

if __name__ == '__main__':
    unittest.main()
# Put your unit tests here

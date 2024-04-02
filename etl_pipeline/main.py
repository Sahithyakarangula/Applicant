import api_client
import transform_data

def main():
    """
    Orchestrates the ETL process by fetching data, transforming it, and loading it into SQLite database.
    """
    # Fetch data
    posts_data = api_client.fetch_posts()
    users_data = api_client.fetch_users()

    if posts_data and users_data:
        # Transform data
        transformed_posts_df = transform_data.transform_posts(posts_data)
        transformed_users_df = transform_data.transform_users(users_data)

        # Load data into SQLite database
        transform_data.load_data_to_sqlite(transformed_posts_df, transformed_users_df)
        print("Data loaded into SQLite database.")
    else:
        print("Failed to fetch data. Please check your internet connection or the API URL.")

if __name__ == "__main__":
    main()

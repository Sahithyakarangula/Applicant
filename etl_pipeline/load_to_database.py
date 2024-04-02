import sqlite3

def create_table(conn, dataframe, table_name):
    """
    Create a table in the SQLite database from a pandas DataFrame.

    Args:
        conn (sqlite3.Connection): SQLite database connection.
        dataframe (pandas.DataFrame): DataFrame containing the data.
        table_name (str): Name of the table to be created.
    """
    dataframe.to_sql(table_name, conn, if_exists='replace', index=False)

def load_data_to_sqlite(posts_df, users_df):
    """
    Load posts and users data into SQLite tables.

    Args:
        posts_df (pandas.DataFrame): DataFrame containing flattened posts data.
        users_df (pandas.DataFrame): DataFrame containing flattened users data.
    """
    # Connect to SQLite database
    conn = sqlite3.connect('your_database.db')

    # Create tables for posts and users
    create_table(conn, posts_df, 'js_posts')
    create_table(conn, users_df, 'js_users')

    # Commit changes and close connection
    conn.commit()
    conn.close()

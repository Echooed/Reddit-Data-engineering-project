import pandas as pd
import sys
import os

# Add project root directory to Python's path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from etls.reddit_etl import connect_reddit, extract_posts, load_data_to_csv


def reddit_pipeline(file_name: str, subreddit: str, time_filter='day', limit=None) -> str:
    """
    Reddit ETL pipeline: Connect, extract, transform, and save posts to CSV.
    """
    try:
        # Connect to Reddit
        reddit_instance = connect_reddit(CLIENT_ID, SECRET, 'Airscholar Agent')
        
        # Extract posts
        posts = extract_posts(reddit_instance, subreddit, time_filter, limit)
        
        # Transform posts into DataFrame
        posts_df = pd.DataFrame(posts)
        
        # Save DataFrame to CSV
        file_path = f'{OUTPUT_PATH}/{file_name}.csv'
        load_data_to_csv(posts_df, file_path)
        
        return file_path

    except Exception as e:
        print(f"Error in Reddit pipeline: {e}")
        raise
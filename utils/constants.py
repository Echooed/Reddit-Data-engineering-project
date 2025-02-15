import configparser
import os 

# Initialize the ConfigParser to read .conf files
parser = configparser.ConfigParser()

# Construct the absolute path to the config file
config_path = os.path.join(os.path.dirname(__file__), '../config/config.conf')

# Check if the configuration file exists before proceeding
if not os.path.exists(config_path):
    raise FileNotFoundError(f"Configuration file not found at: {config_path}")

# Read the config file
parser.read(config_path)

# Read API keys from the config file
SECRET = parser.get('api_keys', 'reddit_secret_key', fallback=None)
CLIENT_ID = parser.get('api_keys', 'reddit_client_id', fallback=None)

# Read Database Configuration
DATABASE_HOST = parser.get('database', 'database_host', fallback='localhost')
DATABASE_NAME = parser.get('database', 'database_name', fallback='airflow_reddit')
DATABASE_PORT = parser.get('database', 'database_port', fallback='5432')
DATABASE_USER = parser.get('database', 'database_username', fallback='postgres')
DATABASE_PASSWORD = parser.get('database', 'database_password', fallback=None)  

# Read AWS Credentials
AWS_ACCESS_KEY_ID = parser.get('aws', 'aws_access_key_id', fallback=None)
AWS_ACCESS_KEY = parser.get('aws', 'aws_secret_access_key', fallback=None)
AWS_REGION = parser.get('aws', 'aws_region', fallback='us-east-1')
AWS_BUCKET_NAME = parser.get('aws', 'aws_bucket_name', fallback=None)

# Read File Paths
INPUT_PATH = parser.get('file_paths', 'input_path', fallback='/default/input/path')
OUTPUT_PATH = parser.get('file_paths', 'output_path', fallback='/default/output/path')

# Define fields for Reddit post extraction
POST_FIELDS = (
    'id',
    'title',
    'score',
    'num_comments',
    'author',
    'created_utc',
    'url',
    'over_18',
    'edited',
    'spoiler',
    'stickied'
)

# Print confirmation for debugging purposes (should be removed in production)
print("Configuration loaded successfully!")
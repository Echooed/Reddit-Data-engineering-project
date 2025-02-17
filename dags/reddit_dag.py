import os
import sys
from datetime import datetime
from airflow import DAG

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from airflow.operators.python import PythonOperator
try:
    from pipelines.reddit_pipeline import reddit_pipeline
except ImportError:
    from pipelines.reddit_pipeline import reddit_pipeline
#from upload_s3_pipeline import upload_s3_pipeline



default_args = {
    'owner': 'Michael Akindele',
    'start_date': datetime(2025, 1, 15),
    'retries': 2,
}

file_postfix = datetime.now().strftime('%Y%m%d%H%M%S')

dag = DAG(
    dag_id='etl_reddit_pipeline_dag',
    default_args=default_args,
    description='DAG to extract, transform and load Reddit data',  
    schedule_interval='@daily',
    catchup=False,
    tags=['reddit', 'etl', 'pipeline']
)

# extraction from reddit
extract = PythonOperator(
    task_id='reddit_extract',
    python_callable=reddit_pipeline,
    op_kwargs={
        'file_name': f'reddit_{file_postfix}',
        'subreddit': 'dataengineering',
        'time_filter': 'day',
        'limit': 100
    },
    dag=dag
)

'''# upload to s3
upload_s3 = PythonOperator(
    task_id='s3_upload',
    python_callable=upload_s3_pipeline,
    dag=dag
)

extract >> upload_s3'''
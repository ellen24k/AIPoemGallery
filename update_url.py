import psycopg2
import os

conn = None

def get_postgrest_client():
    global conn
    if conn is None:
        PG_HOST = os.getenv('PG_HOST')
        PG_DBNAME = os.getenv("PG_DBNAME")
        PG_USER = os.getenv("PG_USER")
        PG_PASSWORD = os.getenv("PG_PASSWORD")
        PG_PORT = os.getenv("PG_PORT")

        try:
            conn = psycopg2.connect(host=PG_HOST, dbname=PG_DBNAME, user=PG_USER, password=PG_PASSWORD, port=PG_PORT)
        except:
            print("db conn failed")
            return None
    return conn


def fetchItems():
    print('fetchItems 함수 실행됨')
    try:
        conn = get_postgrest_client()
        with conn.cursor() as cursor:
            cursor.execute(f'SELECT date, img_url from data where moved = false;')
            items = cursor.fetchall()
        print('fetchItems - items:' + str(items))

        return items
    except Exception as e:
        print('fetchItems error: ' + str(e))
        return []


def update_pg_url(date, minio_url):
    print('update_pg_url 함수 실행됨')
    print(f'date: {date}\n minio_url: {minio_url}')
    try:
        conn = get_postgrest_client()
        with conn.cursor() as cursor:
            cursor.execute(f'UPDATE public.data SET img_url = \'{minio_url}\', moved = True WHERE date = \'{date}\';')
            conn.commit()
        return True
    except Exception as e:
        print('update_url error: ' + str(e))
        return False

###########################################
# import os
import requests
import io

from minio import Minio


minio_client = None

def get_minio_client():
    global minio_client

    MINIO_ENDPOINT = os.getenv("MINIO_ENDPOINT")
    MINIO_ACCESS_KEY = os.getenv("MINIO_ACCESS_KEY")
    MINIO_SECRET_KEY = os.getenv("MINIO_SECRET_KEY")

    if minio_client is None:
        minio_client = Minio(
            endpoint=MINIO_ENDPOINT,
            access_key=MINIO_ACCESS_KEY,
            secret_key=MINIO_SECRET_KEY,
            secure=True
        )
    return minio_client

def download_and_upload_image(dalle_url, file_name):
    minio_cli = get_minio_client()
    response = requests.get(dalle_url)

    if response.status_code == 200:
        image_data = response.content

        file_like_object = io.BytesIO(image_data)

        minio_cli.put_object(
            bucket_name='ai-poem-gallery',
            object_name=f'{file_name}.png',
            data=file_like_object,
            length=len(image_data)
        )

        return minio_cli.presigned_get_object('ai-poem-gallery', f'{file_name}.png')
    else:
        print(f"Failed to download dalle image, status code: {response.status_code}")
        return dalle_url

##########################################
from apscheduler.schedulers.blocking import BlockingScheduler

def update_url():
    items = fetchItems()
    for item in items:
        date = item[0]
        dalle_url = item[1]

        minio_url = download_and_upload_image(
            dalle_url,
            date.strftime('%Y%m%d%H%M%S%f')
        )
        print('minio url: ' + minio_url)
        if update_pg_url(date, minio_url) is False: print('url update failed')
    print('update_url completed')

scheduler = BlockingScheduler()
scheduler.add_job(update_url, 'interval', minutes=60)
scheduler.start()
import psycopg2
import os
import streamlit as st

# from postgrest import APIError
# from supabase import create_client, Client

import requests
import io
from minio import Minio

# supabase_url = os.getenv('SUPABASE_URL')
# supabase_key = os.getenv('SUPABASE_KEY')
# bucket_name = os.getenv("BUCKET_NAME")

# supabase_client: Client = create_client(supabase_url, supabase_key)

minio_client = None


def get_minio_client():
    global minio_client
    if minio_client is None:
        MINIO_ENDPOINT = os.getenv("MINIO_ENDPOINT")
        MINIO_ACCESS_KEY = os.getenv("MINIO_ACCESS_KEY")
        MINIO_SECRET_KEY = os.getenv("MINIO_SECRET_KEY")

        try:
            minio_client = Minio(
                endpoint=MINIO_ENDPOINT,
                access_key=MINIO_ACCESS_KEY,
                secret_key=MINIO_SECRET_KEY,
                secure=True
            )
        except:
            print('minio conn failed')
            return None
    return minio_client


conn = None


# db
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


# admin, gallery
def fetch_all_data():
    try:
        conn = get_postgrest_client()
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM data ORDER BY date DESC;")
            response = cursor.fetchall()  # [(data), (data)]
            responce_dict_list = []
            for item in response:
                responce_dict_list.append(
                    {'date': item[0], 'img_url': item[1], 'title': item[2], 'content': item[3], 'wav_url': item[4],
                     'moved': item[5]})
            conn.commit()
        return responce_dict_list
    except Exception as e:
        st.error('db.fetch_all_data: ' + str(e))
        return []


# admin
def delete_data(date):
    try:
        conn = get_postgrest_client()
        with conn.cursor() as cursor:
            cursor.execute(f"DELETE FROM data WHERE date = '{date}';")
            conn.commit()
            return True
    except Exception as e:
        st.error(e)
        return False


# def file_delete(file_name: str): #todo it's ver supabase
#     try:
#         response = supabase_client.storage.from_(bucket_name).remove(file_name)
#         print(response)
#         return response
#     except APIError as e:
#         return f'Error deleting file: {e.message}'
#     except Exception as e:
#         return f'An unexpected error occurred: {str(e)}'

def file_delete(file_name: str):
    try:
        minio = get_minio_client()
        response = minio.remove_object('ai-poem-gallery', file_name)
        return response
    # except APIError as e:
    #     return f'Error deleting file: {e.message}'
    except Exception as e:
        return f'An unexpected error occurred: {str(e)}'


# chatbot.py
# def file_upload(src_file_path, dest_file_name): # todo it's ver supabase
#     try:
#         with open(src_file_path, 'rb') as file:
#             file_content = file.read()
#         response = supabase_client.storage.from_(bucket_name).upload(dest_file_name, file_content)
#         public_url = supabase_client.storage.from_(bucket_name).get_public_url(dest_file_name)
#         print(public_url)
#         return public_url
#     except APIError as e:
#         return f'Error uploading file: {e.message}'
#     except Exception as e:
#         return f'Unexpected error occurred: {str(e)}'

def file_upload(src_file_path, dest_file_name):
    try:
        minio = get_minio_client()
        minio.fput_object(bucket_name='ai-poem-gallery',
                          object_name=dest_file_name,
                          file_path=src_file_path
                          # content_type='image/png' # 'audio/wav'
        )
        url = get_image_url('ai-poem-gallery', dest_file_name)
        print('minio url: ' + url)
        return url
    # except APIError as e:
    #     return f'Error uploading file: {e.message}'
    except Exception as e:
        return f'Unexpected error occurred: {str(e)}'

def get_image_url(bucket_name: str, object_name: str) -> str:
    # url = minio_client.presigned_get_object(bucket_name, object_name)
    url = f'https://minio-data.ellen24k.kro.kr/{bucket_name}/{object_name}'

    return url


def insert_data(date, img_url, wav_url, title, content, moved=False):
    print(f'insert data: \ndate: {date}\nimg: {img_url}\nwav: {wav_url}\ntitle: {title}\n content: {content}\n\n')
    print(f'INSERT INTO data (date, img_url, title, content, wav_url, moved) values ({date, img_url, title, content, wav_url, moved})')
    try:
        conn = get_postgrest_client()
        with conn.cursor() as cursor:
            cursor.execute('INSERT INTO data (date, img_url, title, content, wav_url, moved) values (%s, %s, %s, %s, %s, %s);',
                           (date, img_url, title, content, wav_url, moved))
            conn.commit()
    except Exception as e:
        print('insert_data error: ' + str(e))
        st.error(e)
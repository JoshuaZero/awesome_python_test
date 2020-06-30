import datetime
import os

import boto
import boto.s3.connection
from retrying import retry

import src.library.config as config
from src.library.logger import logger


class Client:
    def __init__(self):
        self._conn = boto.connect_s3(aws_access_key_id=config.get('ceph', 's3_access_key'),
            aws_secret_access_key=config.get('ceph', 's3_secret_key'), host=config.get('ceph', 's3_host'),
            is_secure=False,  # uncomment if you are not using ssl
            port=int(config.get('ceph', 's3_port')), calling_format=boto.s3.connection.OrdinaryCallingFormat(), )

    def bucket(self, name):
        try:
            b = self._conn.get_bucket(name)
        except Exception as e:
            logger.warning(e)
            b = self._conn.create_bucket(name)
        return Bucket(b)


class Bucket:
    def __init__(self, bucket):
        self._bucket = bucket

    @retry()
    def put(self, key, data):
        k = self._bucket.new_key(key)
        k.set_contents_from_filename(data)

    @retry()
    def get_key(self, key):
        return self._bucket.get_key(key)


def add_dates(date, add):
    date = datetime.datetime.strptime(date, '%Y%m%d')
    date = date + datetime.timedelta(days=add)
    return date.strftime('%Y%m%d')


def download_ceph_image(date, bucket, face_ids, img_dir):
    for face_id in face_ids:
        img_path = "{}/{}.jpg".format(img_dir, face_id)
        if os.path.exists(img_path):
            continue
        try:
            res = bucket.get_key(face_id)
            img = res.get_contents_as_string()
            with open(img_path, "wb") as f:
                f.write(img)
        except Exception as e:
            logger.info("face_id {}: {}".format(face_id, e))

import json

from impala.dbapi import connect
from impala.hiveserver2 import HiveServer2Connection
from retrying import retry

import src.repository.constant as const
from src.library.logger import logger
from src.library.shell import run_system_command


def kinit():
    keytab_path = "{}/hadoop_configs/keytab/sjyw.keytab".format(const.CONFIG_DIR)
    run_system_command("kinit -kt {} sjyw".format(keytab_path))


class HiveConfig:
    def __init__(self, host, user, db, ):
        self.host = host
        self.username = user
        self.database = db


class HiveOp(object):
    def __init__(self, hive_config: HiveConfig):
        self._hive_config = hive_config
        self._connection = None

    def get_connection(self) -> HiveServer2Connection:
        if self._connection is None:
            logger.info("begin connect hive addr {} and database is {}".format(self._hive_config.host,
                                                                               self._hive_config.database))
            kinit()
            self._connection = connect(host=self._hive_config.host, port=10000, auth_mechanism='GSSAPI',
                                       kerberos_service_name=self._hive_config.username,
                                       database=self._hive_config.database)
        return self._connection

    def close_connection(self):
        if self._connection is not None and isinstance(self._connection, HiveServer2Connection):
            self._connection.close()

    @staticmethod
    def get_fields(description):
        fields = {}
        fields_list = []
        idx = 0
        for field in description:
            f = field[0].split('.')[-1]
            fields[f] = idx
            idx += 1
            fields_list.append(f)
        return fields, fields_list

    def query(self, hql):
        cursor = self.get_connection().cursor()
        logger.info("execute hql {}".format(hql))
        cursor.execute(hql)
        all_data = cursor.fetchall()
        request_id = set()
        for data in all_data:
            request_id.add(data[0])
        fields, fields_list = self.get_fields(cursor.description)
        cursor.close()
        return fields, fields_list, all_data

    @retry(stop_max_attempt_number=3)
    def query_and_write(self, hql, local_file, chunk_size=100000):
        """ 分块查询结果并将其写入文件 """
        cursor = self.get_connection().cursor()
        logger.info("execute hql {}".format(hql))
        with open(local_file, "w+") as f:
            cursor.execute(hql)
            columns = [column[0].split('.')[-1] for column in cursor.description]
            while True:
                chunk_data = cursor.fetchmany(chunk_size)
                if not chunk_data:
                    break
                for data in chunk_data:
                    f.write(json.dumps(dict(zip(columns, data))) + "\n")
        cursor.close()
        return local_file

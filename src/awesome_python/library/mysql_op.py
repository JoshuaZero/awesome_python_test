import MySQLdb
from MySQLdb.connections import Connection


class MysqlConfig:
    def __init__(self, host, user, password, db, port, charset="utf8"):
        self.host = host
        self.user = user
        self.passwd = password
        self.db = db
        self.charset = charset
        self.port = int(port)


class MysqlOp(object):
    def __init__(self, mysql_config: MysqlConfig):
        self._mysql_config = mysql_config
        self._connection = None

    def get_connection(self) -> Connection:
        if self._connection is None:
            self._connection = MySQLdb.connect(**self._mysql_config.__dict__)
        return self._connection

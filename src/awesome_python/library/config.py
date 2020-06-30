import os

conf_dict = {
    'kafka': {
        'bootstrap.servers': '106.12.11.34:30091,106.12.35.226:30092,106.12.27.21:30093',
        'group.id': 'online_recognition_cg',
        'auto.offset.reset': 'earliest',
        'security.protocol': 'sasl_plaintext',
        'sasl.mechanisms': 'PLAIN',
        'sasl.username': 'account1',
        'sasl.password': 'xm%h6Ot4'
    },
    'baidu_kafka': {
        'bootstrap.servers': 'kafka.su.baidubce.com:9091',
        'group.id': 'online_recognition_cg',
        'auto.offset.reset': 'earliest',
        'security.protocol': 'ssl',
        'ssl.ca.location': '/work/dependency/kafka-cert/ca.pem',
        'ssl.certificate.location': '/work/dependency/kafka-cert/client.pem',
        'ssl.key.location': '/work/dependency/kafka-cert/client.key'
    },
    'influxdb': {
        'server': 'bj-influxdb.aibee.cn',
        'port': 80,
        'user': '',
        'password': '',
        'db': 'face_data_pipeline'
    },
}


def get(*args):
    """
    优先从环境变量获取配置
    :param args:
    :return:
    """
    env_name = ('_'.join(args)).upper()
    val = os.getenv(env_name)
    if val is None:
        _conf_dict = conf_dict
        for idx in range(len(args)):
            k = args[idx]
            if type(_conf_dict[k]) is dict:
                if idx == len(args) - 1:
                    return _conf_dict[k]
                else:
                    _conf_dict = _conf_dict[k]
        return _conf_dict[k]
    return val

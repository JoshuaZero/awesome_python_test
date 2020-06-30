import os

REDSTAR_PROJECT_ID_TO_SITE_ID = {
    'REDSTAR_sh_jq': 10062,
}
REDSTAR_SITE_ID_TO_PROJECT_ID = {
    '10062': 'REDSTAR_sh_jq',
}

# 需要一城一档的城市和店铺
NEED_UNION_PROJECT = {
    "REDSTAR": {
        "chongqing": ["REDSTAR_chongqing_el", "REDSTAR_chongqing_cy", "REDSTAR_chongqing_jb", "REDSTAR_chongqing_np"],
        "nanjing": ["REDSTAR_nanjing_kzm", "REDSTAR_nanjing_pk"]
    },
    "AIBEE": {
        "beijing": ["AIBEE_beijing_test_trafficlite", "AIBEE_beijing_office_trafficlite", ]
    }
}

# 工作目录 face_data_pipeline
WORK_DIR = ""
# 数据存放目录，可自定义
DATA_DIR = ""
# 日志存放目录
LOG_DIR = ""
# 标志workflow运行步骤目录
WORKFLOW_MARK_DIR = ""
# bin文件存放路径
BINARY_DIR = ""

""" CONFIG 相关"""
# 配置文件 face_data_pipeline/config
CONFIG_DIR = ""
# pipeline 配置目录 face_data_pipeline/config/pipeline
PIPELINE_CONFIG_DIR = ""
# workflow 配置相关 face_data_pipeline/config/workflow
WORKFLOW_CONFIG_DIR = ""
# workflow params 配置相关 face_data_pipeline/config/workflow_params
WORKFLOW_PARAMS_CONFIG_DIR = ""
# 配置文件的检查列表的路径 face_data_pipeline/config/param_check
PARAM_CHECK_DIR = ""
# 检查配置文件名
CONFIG_CHECK_LIST_POSTFIX = "config_check_list.yaml"

""" FEATURE 相关"""
# feature_type
GENERAL_FEATURE_TYPE = "general_model_feature"
BASE_FEATURE_TYPE = "base_model_feature"
UPPER_BODY_FEATURE_TYPE = "upper_body_feature"
MASK_FEATURE_TYPE = "mask_feature"
HEAD_FEATURE_TYPE = "head_feature"
# 有可能会有history库和daily所用的feature不一样的情况
HIS_BASE_FEATURE_TYPE = "his_base_model_feature"
FEATURE_TYPE_LIST = [GENERAL_FEATURE_TYPE, BASE_FEATURE_TYPE, UPPER_BODY_FEATURE_TYPE, MASK_FEATURE_TYPE,
    HIS_BASE_FEATURE_TYPE, HEAD_FEATURE_TYPE]

""" 数据类型相关 """
DATA_TYPE_MYSQL = "mysql"
DATA_TYPE_SQLLITE = "sqllite"
DATA_TYPE_TEXT = "text"
DATA_TYPE_PB = "pb"
DATA_TYPE_HIVE = "hive"


def init(**kwargs):
    global WORK_DIR, DATA_DIR, LOG_DIR, CONFIG_DIR, WORKFLOW_MARK_DIR, PARAM_CHECK_DIR, PIPELINE_CONFIG_DIR, WORKFLOW_CONFIG_DIR, WORKFLOW_PARAMS_CONFIG_DIR, BINARY_DIR

    _work_dir = os.path.abspath(kwargs.get("work_dir", os.getcwd()))
    WORK_DIR = _work_dir
    BINARY_DIR = "{}/bin".format(_work_dir)
    CONFIG_DIR = "{}/config".format(_work_dir)
    PARAM_CHECK_DIR = "{}/param_check".format(CONFIG_DIR)
    PIPELINE_CONFIG_DIR = "{}/pipeline".format(CONFIG_DIR)
    WORKFLOW_CONFIG_DIR = "{}/workflow".format(CONFIG_DIR)
    WORKFLOW_PARAMS_CONFIG_DIR = "{}/workflow_params".format(CONFIG_DIR)

    _data_dir = os.path.abspath(kwargs.get("data_dir", os.getcwd()))
    WORKFLOW_MARK_DIR = "{}/workflow_mark".format(_data_dir)
    DATA_DIR = "{}/data".format(_data_dir)
    LOG_DIR = "{}/log".format(_data_dir)

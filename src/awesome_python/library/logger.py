import json
import os
import sys

import psutil
from loguru import logger
from pygments import highlight, lexers, formatters
from termcolor import colored

import src.repository.constant as const


def init(project_id, curr_date):
    env = os.getenv("AIBEE_IDC", "")
    log_level = "DEBUG"
    if env == "dev":
        log_level = "DEBUG"
    logger.configure(handlers=[{
        "sink": sys.stdout,
        "level": log_level,
    }])
    logger.add("{}/{}_{}.log".format(const.LOG_DIR, project_id, curr_date))


def mem_log(mark=""):
    mem = psutil.virtual_memory()
    process = psutil.Process(os.getpid())
    use_mem = process.memory_info()
    total = float(mem.total) / 1024 / 1024 / 1024
    used = float(use_mem.rss) / 1024 / 1024 / 1024
    logger.info("{} memory usage total: {:.3f} GB, used: {:.3f}GB".format(mark, total, used))


def format_dict(data: [dict, list]):
    data = json.dumps(data, cls=json.JSONEncoder, indent=2, ensure_ascii=False)
    if sys.stdout.isatty():
        data = highlight(data, lexers.JsonLexer(), formatters.TerminalFormatter())
    return data


def format_text(text: str, color='cyan'):
    if sys.stdout.isatty():
        text = colored(text, color)
    return text

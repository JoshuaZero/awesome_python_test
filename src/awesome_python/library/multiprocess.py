import concurrent
import math
import threading
from concurrent.futures import ThreadPoolExecutor
from multiprocessing import Pool, cpu_count, Process

import src.repository.global_params as global_params
from src.library.logger import logger
from src.library.shell import run_system_command_with_res


class MultiProcess(object):
    def __init__(self, work_num: int = 0):
        if not work_num:
            work_num = cpu_count()
        self.work_num = work_num
        self.pool = Pool(self.work_num)
        self.params = []
        self.func = None
        self.res = None

    def add_params(self, params):
        self.params = params

    def add_func(self, func):
        self.func = func

    def deal(self):
        logger.info("generate {} worker pool for {}".format(self.work_num, self.func))
        self.res = self.pool.starmap_async(self.func, self.params)

    def wait(self):
        logger.info("wait process finish")
        if self.res:
            self.res.get()
        if self.pool:
            self.pool.close()


def multiprocess_deal(func, deal_list, work_num: int = 0):
    if not work_num:
        work_num = cpu_count()
    work_num = min(work_num, len(deal_list), 80)
    logger.info("generate {} worker pool for {}".format(work_num, func))
    pool = Pool(work_num)
    res = pool.starmap(func, deal_list)
    pool.close()
    return res


def multiprocess_run(func, deal_list, work_num: int = 0):
    if not work_num:
        work_num = cpu_count()
    work_num = min(work_num, 80)
    logger.info("generate {} worker pool for {}".format(work_num, func))
    pool = Pool(work_num)
    res = pool.map(func, deal_list)
    pool.close()
    return res


def chunk(data_list: list, chunk_num):
    item_num = len(data_list)
    if item_num <= chunk_num:
        return [data_list]
    step = int(math.ceil(item_num / chunk_num))
    res = []
    if step <= 0:
        return res
    for i in range(0, item_num, step):
        res.append(data_list[i:i + step])
    return res


def multiprocess_exe(func, deal_list, work_num: int = 0):
    if not work_num:
        work_num = cpu_count()
    process_list = []
    deal_list = chunk(deal_list, work_num)
    logger.info("generate {} worker pool for {}".format(work_num, func))
    for i in range(work_num):
        process_list.append(Process(target=func, args=(deal_list[i],)))
    for process in process_list:
        process.start()
    for process in process_list:
        process.join()


def get_process_num() -> int:
    process_num = global_params.get("process_num", cpu_count())
    process_num = int(process_num)
    return min(process_num, cpu_count())


def get_gpu_num() -> int:
    gpu_config_num = len(global_params.get("gpu_config", "0 1 2 3 4 5 6 7").split(" "))
    gpu_num = gpu_config_num
    try:
        _, online_num = run_system_command_with_res("nvidia-smi -L |wc -l")
        gpu_num = int(online_num)
    except Exception as ex:
        logger.error('get nvidia-smi num error: {}'.format(ex))
    return min(gpu_config_num, gpu_num)


def multithread_run(func, deal_list, work_num: int = 0, max_execute_time=10):
    if not work_num:
        work_num = cpu_count()
    work_num = min(work_num, 200)
    logger.info("generate {} thread worker pool for {}".format(work_num, func))
    res = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=work_num) as executor:
        thread_tasks = {executor.submit(func, *params): params for params in deal_list}
        for task in concurrent.futures.as_completed(thread_tasks):
            try:
                data = task.result(timeout=max_execute_time)
                res.append(data)
            except Exception as exc:
                logger.error('generated an exception: {}'.format(exc))
    return res


class Thread(threading.Thread):
    def __init__(self, target, *args):
        super().__init__()
        self._target = target
        self._args = args
        self._result = None

    def run(self):
        self._result = self._target(*self._args)

    def get_result(self):
        return self._result

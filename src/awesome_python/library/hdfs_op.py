from retrying import retry

import src.repository.global_params as global_params
from src.library.shell import run_system_command, run_system_command_with_res
from src.repository import constant

auth_status = False


def hdfs_auth(*dargs):
    def wrap_simple(f):
        def wrapped_f(*args, **kw):
            global auth_status
            if not auth_status:
                cmd = "hdfscli initkrb5 -k {}/hadoop_configs/keytab/sjyw.keytab sjyw".format(constant.CONFIG_DIR)
                run_system_command(cmd)
                auth_status = True
            return f(*args, **kw)

        return wrapped_f

    return wrap_simple(dargs[0])


@hdfs_auth
def hdfs_get(remote_file, local_file):
    cmd = "hdfscli download /{}{} {}".format(global_params.get("hdfs_idc", "bj"), remote_file, local_file)
    run_system_command(cmd)


@hdfs_auth
@retry(stop_max_attempt_number=3)
def hdfs_put(local_file, remote_file, force=True):
    # hdfscli upload -f 存在一些问题
    full_path = "/{}{}".format(global_params.get("hdfs_idc", "bj"), remote_file)
    temp_full_path = "{}_backup".format(full_path)
    temp_remote_file = "{}_backup".format(remote_file)
    if force and hdfs_file_exist(remote_file):
        if hdfs_file_exist(temp_remote_file):
            del_cmd = "hdfscli delete -f {}".format(temp_full_path)
            run_system_command(del_cmd)
        rename_cmd = "hdfscli rename {} {}".format(full_path, temp_full_path)
        run_system_command(rename_cmd)

    cmd = "hdfscli upload {} {}".format(local_file, full_path)
    run_system_command(cmd)

    cmd = "hdfscli setacl 'group:supergroup:rw-' {}".format(full_path)
    run_system_command(cmd)


@hdfs_auth
def hdfs_file_exist(file_path):
    cmd = "hdfscli list /{}{}".format(global_params.get("hdfs_idc", "bj"), file_path)
    status, _ = run_system_command_with_res(cmd, ignore_err=True)
    if status != 0:
        return False
    return True


@hdfs_auth
def hdfs_mkdir(dir_path):
    cmd = "hdfscli mkdir /{}{}".format(global_params.get("hdfs_idc", "bj"), dir_path)
    run_system_command(cmd)
    cmd = "hdfscli setacl 'group:supergroup:rw-' /{}{}".format(global_params.get("hdfs_idc", "bj"), dir_path)
    run_system_command(cmd)


@hdfs_auth
def hdfs_copy(source_path, dst_path):
    cmd = "hdfscli copy -f {} {}".format(source_path, dst_path)
    run_system_command(cmd)

@hdfs_auth
def hdfs_delete(dst_path):
    cmd = "hdfscli delete -f /{}{}".format(global_params.get("hdfs_idc", "bj"), dst_path)
    run_system_command(cmd)

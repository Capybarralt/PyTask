import os

from appdirs import user_config_dir, user_data_dir


def get_dir(path):
    if not os.path.exists(path):
        os.makedirs(path, 0o755) # 111 101 101 rwx rwx rwx
    return path


def get_config_dir(app_name):
    return get_dir(user_config_dir(app_name))


def get_data_dir(app_name):
    return get_dir(user_data_dir(app_name))

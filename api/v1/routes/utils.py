import os
import logging
from typing import Dict, List

class Logger:
    def __init__(self, name: str):
        self.name = name
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)
        handler = logging.FileHandler(os.path.join(os.getcwd(), f'{name}.log'))
        handler.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def debug(self, message: str):
        self.logger.debug(message)

    def info(self, message: str):
        self.logger.info(message)

    def warning(self, message: str):
        self.logger.warning(message)

    def error(self, message: str):
        self.logger.error(message)

    def critical(self, message: str):
        self.logger.critical(message)


def get_environment_variables() -> Dict[str, str]:
    env_variables = {}
    for key, value in os.environ.items():
        env_variables[key] = value
    return env_variables


def get_system_info() -> Dict[str, str]:
    system_info = {}
    system_info['platform'] = os.name
    system_info['python_version'] = sys.version
    system_info['os_version'] = platform.system()
    return system_info


def get_system_date() -> str:
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')


def load_json_file(file_path: str) -> Dict[str, List[str]]:
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data


def save_json_file(file_path: str, data: Dict[str, List[str]]) -> None:
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)


def validate_email(email: str) -> bool:
    try:
        from email.utils import parseaddr
        _, email = parseaddr(email)
        return '@' in email
    except Exception as e:
        return False
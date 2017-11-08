import yaml
import logging

log = logging.getLogger(__name__)


def parse_file(file_name):
    with open(file_name, 'r') as stream:
        try:
            config = yaml.load(stream)
        except yaml.YAMLError:
            log.exception()

    return config


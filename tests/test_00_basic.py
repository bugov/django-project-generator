import os
from django_project_generator.parser import parse_file

DIR = os.path.dirname(os.path.abspath(__file__))


def test_parse_file():
    config = parse_file(os.path.join(DIR, '00_basic.yaml'))
    assert {'Post': {'Model': {'name': 'Char', 'text': 'Text'}}} == config

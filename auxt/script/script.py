from pathlib import Path
from auxt.util.load import load_config

import sys
import logging
from logging import getLogger, Formatter, StreamHandler
logger = getLogger(__name__)
logging.basicConfig(
        format = '[%(asctime)s] (%(levelname)s) %(message)s',
        datefmt = '%Y/%m/%d %H:%M:%S',
        level = logging.INFO,
        stream = sys.stdout)

class Script(list):
    def __init__(self):
        super().__init__()
        self.config = load_config()
        self.path = self.make_path()
        self.prepare()
        self.header()
        self.make()
        self.footer()
        self.make_dir()
        self.save()
        logging.info('{}: {}'.format(type(self).__name__, self.path))

    def prepare(self):
        pass

    def header(self):
        self.append('#!/bin/bash')
        self.append('')
        self.append('set -ex')
        self.append('')

    def footer(self):
        self.append('')

    def make_dir(self):
        Path(self.path).parent.mkdir(parents=True, exist_ok=True)

    def save(self):
        with open (Path(self.path), 'w') as f:
            print(str(self), file=f)

    def __str__(self):
        return '\n'.join(self)


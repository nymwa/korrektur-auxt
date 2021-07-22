from pathlib import Path
from .script import Script
from .util import add_await_script

class RunScript(Script):
    def __init__(self, script_list):
        self.script_list = script_list
        super().__init__()

    def is_await(self):
        return self.config.get('await', False)

    def get_job(self):
        return self.config.get('jobs', 1)

    def header(self):
        self.append('#!/bin/bash')
        self.append('')
        self.append('set -ex')
        self.append('')
        if self.is_await():
            self = add_await_script(self, self.get_job())

    def add_job(self, path):
        path = Path(path).resolve()
        if self.is_await():
            line = 'bash {} & await'
            self.append('bash {} & await'.format(path))
        else:
            self.append('bash {}'.format(path))

    def make(self):
        for script in self.script_list:
            self.add_job(script.path)

    def footer(self):
        if self.is_await():
            self.append('wait')
        self.append('')


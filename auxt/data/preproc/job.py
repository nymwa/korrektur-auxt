from pathlib import Path
from auxt.data.job import DataJobScript

class PreprocJobScript(DataJobScript):
    def __init__(self, index, first_index = None):
        self.first_index = first_index
        super().__init__(index)

    def make_path(self):
        return '{}/preproc.sh'.format(self.index)

    def is_following(self):
        return (self.first_index is not None) and (self.first_index != self.index)

    def make_following_dict_path(self, side):
        return '{}/data-bin/dict.{}.txt'.format(self.first_index, side)

    def make_prepared_dict_path(self, side):
        key = '{}_dict_path'.format(side)
        if key in self.config:
            dict_path = self.config[key]
        else:
            dict_path = None
        return dict_path

    def make_dict_path(self, side):
        if self.is_following():
            dict_path = self.make_following_dict_path(side)
        else:
            dict_path = self.make_prepared_dict_path(side)

        if dict_path is not None:
            dict_path = str(Path(dict_path).resolve())
        return dict_path

    def make_src_dict_path(self):
        return self.make_dict_path('src')

    def make_trg_dict_path(self):
        return self.make_dict_path('trg')


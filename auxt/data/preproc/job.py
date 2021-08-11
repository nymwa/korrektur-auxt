from pathlib import Path
from auxt.data.job import DataJobScript

def make_encode_last_line(output_path, overwrite, background):
    line = '   '

    if overwrite:
        line += '>> '
    else:
        line += '> '

    line += str(output_path)

    if background:
        line += ' &'

    return line


class PreprocJobScript(DataJobScript):

    def make_bpe_model(self):
        model = self.get_bpe_model_path()
        self.append('MODELPATH={}'.format(model))
        self.append('')

    def make_encode(self, input_path,
            spm_command, output_path, 
            overwrite = False,
            background = False,
            postprocessing = None):

        self.append('cat {} \\'.format(input_path))
        self.append('   | {} \\'.format(spm_command))
        if self.config.get('r2l', False):
            self.append('   | renversi \\')
        if postprocessing:
            self.append('   | {} \\'.format(postprocessing))
        self.append('   | progress \\')
        self.append(make_encode_last_line(output_path, overwrite, background))

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


class TrainPreprocJobScript(PreprocJobScript):

    def __init__(self, index, first_index = None):
        self.index = index
        self.first_index = first_index
        super().__init__()

    def make_path(self):
        return '{}/preproc.sh'.format(self.index)

    def is_following(self):
        if self.first_index is None:
            return False
        return self.first_index != self.index


class EvalPreprocJobScript(PreprocJobScript):

    def __init__(self, first_index):
        self.first_index = first_index
        super().__init__()

    def make_path(self):
        return '{}/preproc.sh'.format(self.name)

    def is_following(self):
        if self.first_index is None:
            return False
        return True


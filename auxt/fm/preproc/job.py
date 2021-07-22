from pathlib import Path
from auxt.data.preproc.job import PreprocJobScript
from auxt.data.preproc.fairseq import fairseq_preprocess_command

class FalkoMerlinPreprocJobScript(PreprocJobScript):
    def make(self):
        base_path = Path(str(self.index))

        model = self.get_bpe_model_path()
        self.append('MODELPATH={}'.format(model))
        self.append('')

        src_spm_command, trg_spm_command = self.make_spm_commands(parallel = False)
        train_input_path = Path(self.config['train_path']).resolve()
        train_source_input = str(train_input_path) + '.src'
        train_target_input = str(train_input_path) + '.trg'
        train_pref = (base_path / 'train').resolve()
        train_source_output = (base_path / 'train.src').resolve()
        train_target_output = (base_path / 'train.trg').resolve()

        self.append('cat {} \\'.format(train_source_input))
        self.append('   | {} \\'.format(src_spm_command))
        if self.config.get('r2l', False):
            self.append('   | renversi \\')
        self.append('   | progress \\')
        self.append('   > {} &'.format(train_source_output))

        self.append('cat {} \\'.format(train_target_input))
        self.append('   | {} \\'.format(trg_spm_command))
        if self.config.get('r2l', False):
            self.append('   | renversi \\')
        self.append('   | progress \\')
        self.append('   > {} &'.format(train_target_output))

        self.append('wait')

        valid_pref = Path(self.config['valid_pref']).resolve()

        dest_dir = Path('{}/data-bin'.format(self.index)).resolve()
        threads = self.config['threads']
        src_dict = self.make_dict_path('src')
        command = fairseq_preprocess_command(
                source_lang = 'src',
                target_lang = 'trg',
                train_pref = train_pref,
                valid_pref = valid_pref,
                dest_dir = dest_dir,
                threads = threads,
                src_dict = src_dict,
                trg_dict = None,
                joined_dict = True)
        self.append(command)


from pathlib import Path
from auxt.data.preproc.job import TrainPreprocJobScript, EvalPreprocJobScript
from auxt.util.fairseq.preproc import fairseq_preprocess_command

class FMMTPreprocJobScriptInterface:

    def make_command(self, dest_dir, train_pref, valid_pref, test_pref, src_dict):
        command = fairseq_preprocess_command(
                source_lang = 'src',
                target_lang = 'trg',
                dest_dir = dest_dir,
                threads = self.config['threads'],
                train_pref = train_pref,
                valid_pref = valid_pref,
                test_pref = test_pref,
                src_dict = src_dict,
                trg_dict = None,
                joined_dict = True)
        self.append(command)


class FMMTTrainPreprocJobScript(
        FMMTPreprocJobScriptInterface,
        TrainPreprocJobScript):

    def make_fm_encode(self, input_path, side, spm_command):
        if side == 'src':
            postprocessing = 'gec-tag'
        else:
            postprocessing = None

        base_dir = Path(str(self.index))
        self.make_encode(str(input_path) + '.' + side, spm_command, (base_dir / ('train.' + side)).resolve(),
                overwrite = False, background = True, postprocessing = postprocessing)

    def make_mt_encode(self, input_path, side, lang, spm_command):
        if side == 'src':
            if lang == 'de':
                postprocessing = 'd2e-tag'
            else:
                postprocessing = 'e2d-tag'
        else:
            postprocessing = None

        base_dir = Path(str(self.index))
        self.make_encode(str(input_path) + '.' + lang, spm_command, (base_dir / ('train.' + side)).resolve(),
                overwrite = True, background = True, postprocessing = postprocessing)

    def make_text_preprocess(self):
        src_spm_command, trg_spm_command = self.make_spm_commands(parallel = False)
        fm_train_path = Path(self.config['fm_train_path']).resolve()
        mt_train_path = Path(self.config['mt_train_path']).resolve()

        self.make_fm_encode(fm_train_path, 'src', src_spm_command)
        self.make_fm_encode(fm_train_path, 'trg', trg_spm_command)
        self.append('wait')
        self.append('')
        self.make_mt_encode(mt_train_path, 'src', 'de', src_spm_command)
        self.make_mt_encode(mt_train_path, 'trg', 'en', trg_spm_command)
        self.append('wait')
        self.append('')
        self.make_mt_encode(mt_train_path, 'src', 'en', src_spm_command)
        self.make_mt_encode(mt_train_path, 'trg', 'de', trg_spm_command)
        self.append('wait')
        self.append('')

    def make_preprocess_command(self):
        base_dir = Path(str(self.index)).resolve()
        dest_dir = base_dir / 'data-bin'
        train_pref = (base_dir / 'train').resolve()
        valid_pref = Path(self.config['valid_pref']).resolve()
        src_dict = self.make_dict_path('src')
        self.make_command(dest_dir, train_pref, valid_pref, None, src_dict)

    def make(self):
        self.make_bpe_model()
        self.make_text_preprocess()
        self.make_preprocess_command()


class FMMTEvalPreprocJobScript(
        FMMTPreprocJobScriptInterface,
        EvalPreprocJobScript):

    def make_preprocess_command(self):
        base_dir = Path(self.name).resolve()
        dest_dir = base_dir / 'data-bin'
        false_pref = Path(self.config['false_pref']).resolve()
        test_pref = self.make_test_pref()
        src_dict = self.make_dict_path('src')
        self.make_command(dest_dir, false_pref, false_pref, test_pref, src_dict)

    def make(self):
        self.make_bpe_model()
        self.make_preprocess_command()


class FMMTValidPreprocJobScript(FMMTEvalPreprocJobScript):

    name = 'fm-valid'

    def make_test_pref(self):
        return Path(self.config['valid_pref']).resolve()


class FMMTTestPreprocJobScript(FMMTEvalPreprocJobScript):

    name = 'fm-test'

    def make_test_pref(self):
        return Path(self.config['test_pref']).resolve()


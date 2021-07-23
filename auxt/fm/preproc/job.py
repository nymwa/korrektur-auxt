from pathlib import Path
from auxt.data.preproc.job import TrainPreprocJobScript, EvalPreprocJobScript
from auxt.data.preproc.fairseq import fairseq_preprocess_command

class FalkoMerlinPreprocJobScriptInterface:

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


class FalkoMerlinTrainPreprocJobScript(
        FalkoMerlinPreprocJobScriptInterface,
        TrainPreprocJobScript):

    def make_text_preprocess(self):
        src_spm_command, trg_spm_command = self.make_spm_commands(parallel = False)
        train_input_path = Path(self.config['train_path']).resolve()
        base_dir = Path(str(self.index))

        self.make_encode(
                str(train_input_path) + '.src',
                src_spm_command,
                (base_dir / 'train.src').resolve(),
                background = True)
        self.make_encode(
                str(train_input_path) + '.trg',
                trg_spm_command,
                (base_dir / 'train.trg').resolve(),
                background = True)
        self.append('wait')

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


class FalkoMerlinEvalPreprocJobScript(
        FalkoMerlinPreprocJobScriptInterface,
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


class FalkoMerlinValidPreprocJobScript(FalkoMerlinEvalPreprocJobScript):

    name = 'fm-valid'

    def make_test_pref(self):
        return Path(self.config['valid_pref']).resolve()


class FalkoMerlinTestPreprocJobScript(FalkoMerlinEvalPreprocJobScript):

    name = 'fm-test'

    def make_test_pref(self):
        return Path(self.config['test_pref']).resolve()


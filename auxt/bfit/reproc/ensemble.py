from pathlib import Path
from auxt.script.run import RunScript
from .util import (
        FMValidEnsembleReprocJobScriptInterface,
        FMTestEnsembleReprocJobScriptInterface,
        CoNLLValidEnsembleReprocJobScriptInterface,
        CoNLLTestEnsembleReprocJobScriptInterface)
from auxt.expt.job import ExptJobScript, EvalExptJobScriptInterface
from auxt.generator.run import EnsembleR2LRerankRunScriptGenerator
from auxt.util.fairseq.preproc import fairseq_preprocess_command

class EnsembleReprocJobScript(
        EvalExptJobScriptInterface,
        ExptJobScript):

    def make_path(self):
        return self.outdir.make_path('reproc.sh')

    def make_src_dict_path(self):
        return Path(self.config['rerank']['r2l_vocab']).resolve()

    def make_reversed_data(self):
        self.append('yaml2tsv < {} > {}'.format(
            self.make_output_yaml_path(),
            self.make_tsv_path()))
        self.append('cut -f 1 {} | renversi{}> {}'.format(
            self.make_tsv_path(),
            ' --with-tag ' if self.config['rerank']['with_tag'] else ' ',
            self.make_source_path()))
        self.append('cut -f 2 {} | renversi > {}'.format(
            self.make_tsv_path(),
            self.make_target_path()))
        self.append('renversi{}< {} > {}'.format(
            ' --with-tag ' if self.config['rerank']['with_tag'] else ' ',
            self.get_false_source_input_path(),
            self.make_false_source_output_path()))
        self.append('renversi < {} > {}'.format(
            self.get_false_target_input_path(),
            self.make_false_target_output_path()))

    def make_command(self):
        dest_dir = self.outdir.make_path('data-bin')
        false_pref = self.make_false_pref_path()
        command = fairseq_preprocess_command(
                source_lang = 'src',
                target_lang = 'trg',
                dest_dir = dest_dir,
                threads = self.config.get('threads', 1),
                train_pref = false_pref,
                valid_pref = false_pref,
                test_pref = self.make_test_pref(),
                src_dict = self.make_src_dict_path(),
                trg_dict = None,
                joined_dict = True)
        self.append(command)

    def make(self):
        self.make_reversed_data()
        self.make_command()


class FMValidEnsembleReprocJobScript(
        FMValidEnsembleReprocJobScriptInterface,
        EnsembleReprocJobScript):
    pass


class FMTestEnsembleReprocJobScript(
        FMTestEnsembleReprocJobScriptInterface,
        EnsembleReprocJobScript):
    pass


class FMEnsembleReprocRunScript(RunScript):

    def make_path(self):
        return 'r2l_reproc_fm_ensemble.sh'


class CoNLLValidEnsembleReprocJobScript(
        CoNLLValidEnsembleReprocJobScriptInterface,
        EnsembleReprocJobScript):
    pass


class CoNLLTestEnsembleReprocJobScript(
        CoNLLTestEnsembleReprocJobScriptInterface,
        EnsembleReprocJobScript):
    pass


class CoNLLEnsembleReprocRunScript(RunScript):

    def make_path(self):
        return 'r2l_reproc_conll_ensemble.sh'


class FMEnsembleReprocRunScriptGenerator(
        EnsembleR2LRerankRunScriptGenerator):

    def __init__(self):
        self.dataset, self.valid_job_class, self.test_job_class, self.run_class = (
                'fm',
                FMValidEnsembleReprocJobScript,
                FMTestEnsembleReprocJobScript,
                FMEnsembleReprocRunScript)
        super().__init__()


class CoNLLEnsembleReprocRunScriptGenerator(
        EnsembleR2LRerankRunScriptGenerator):

    def __init__(self):
        self.dataset, self.valid_job_class, self.test_job_class, self.run_class = (
                'wf',
                CoNLLValidEnsembleReprocJobScript,
                CoNLLTestEnsembleReprocJobScript,
                CoNLLEnsembleReprocRunScript)
        super().__init__()


def bfit_ensemble_r2l_reproc(fm):
    FMEnsembleReprocRunScriptGenerator().make()

    if not fm:
        CoNLLEnsembleReprocRunScriptGenerator().make()


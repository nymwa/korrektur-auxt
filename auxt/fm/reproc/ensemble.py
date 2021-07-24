from pathlib import Path
from auxt.script.run import RunScript
from .util import (
        FalkoMerlinValidEnsembleReprocJobScriptInterface,
        FalkoMerlinTestEnsembleReprocJobScriptInterface)
from auxt.expt.job import ExptJobScript, EvalExptJobScriptInterface
from auxt.generator.run import EnsembleR2LRescoreRunScriptGenerator
from auxt.util.fairseq.preproc import fairseq_preprocess_command

class FalkoMerlinEnsembleReprocJobScript(
        EvalExptJobScriptInterface,
        ExptJobScript):

    def __init__(self, outdir):
        super().__init__(outdir)

    def make_path(self):
        return self.outdir.make_path('r2l_reproc.sh')

    def make_src_dict_path(self):
        return Path(self.config['rescore']['r2l_vocab']).resolve()

    def make_reversed_data(self):
        self.append('yaml2tsv {} {} > {}'.format(
            self.get_source_input_path(),
            self.make_output_yaml_path(),
            self.make_tsv_path()))
        self.append('cut -f 1 {} | renversi > {}'.format(
            self.make_tsv_path(),
            self.make_source_path()))
        self.append('cut -f 2 {} | renversi > {}'.format(
            self.make_tsv_path(),
            self.make_target_path()))
        self.append('renversi < {} > {}'.format(
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


class FalkoMerlinValidEnsembleReprocJobScript(
        FalkoMerlinValidEnsembleReprocJobScriptInterface,
        FalkoMerlinEnsembleReprocJobScript):
    pass


class FalkoMerlinTestEnsembleReprocJobScript(
        FalkoMerlinTestEnsembleReprocJobScriptInterface,
        FalkoMerlinEnsembleReprocJobScript):
    pass


class FalkoMerlinEnsembleReprocRunScript(RunScript):

    def make_path(self):
        return 'r2l_reproc_fm_ensemble.sh'


class FalkoMerlinEnsembleReprocRunScriptGenerator(
        EnsembleR2LRescoreRunScriptGenerator):

    def __init__(self):
        self.dataset = 'fm'
        self.valid_job_class = FalkoMerlinValidEnsembleReprocJobScript
        self.test_job_class = FalkoMerlinTestEnsembleReprocJobScript
        self.run_class = FalkoMerlinEnsembleReprocRunScript
        super().__init__()


def fm_ensemble_r2l_reproc():
    FalkoMerlinEnsembleReprocRunScriptGenerator().make()


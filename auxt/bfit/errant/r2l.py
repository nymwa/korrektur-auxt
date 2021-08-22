from auxt.expt.result.m2 import M2ResultTableFactory
from auxt.directory.expt.outdir import EnsembleR2LRerankOutDir
from auxt.expt.score.run import ScoreRunScriptInterface
from auxt.util.prod import make_train_indices
from auxt.script.run import RunScript
from .util import ErrantJobScript

class FMValidErrantJobScript(ErrantJobScript):

    def original_path(self):
        return self.eval_config['fm']['valid_src']

    def reference_path(self):
        return self.eval_config['fm']['valid_m2']


class FMTestErrantJobScript(ErrantJobScript):

    def original_path(self):
        return self.eval_config['fm']['test_src']

    def reference_path(self):
        return self.eval_config['fm']['test_m2']


class FMR2LErrantRunScript(
        ScoreRunScriptInterface,
        RunScript):

    def make_path(self):
        return 'errant_fm_r2l.sh'


def fm_r2l_errant():
    script_list = []

    valid_outdir = EnsembleR2LRerankOutDir('fm', 'valid')
    test_outdir = EnsembleR2LRerankOutDir('fm', 'test')

    FMR2LErrantRunScript([
        FMValidErrantJobScript(valid_outdir),
        FMTestErrantJobScript(test_outdir)])


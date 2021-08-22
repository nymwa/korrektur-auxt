from auxt.expt.result.m2 import M2ResultTableFactory
from auxt.directory.expt.outdir import SingleOutDir
from auxt.expt.score.run import ScoreRunScriptInterface
from auxt.util.prod import make_train_indices
from auxt.script.run import RunScript
from .util import ErrantJobScript

class FMValidErrantJobScript(ErrantJobScript):

    def original_path(self):
        return self.eval_config['fm']['valid_src']

    def reference_path(self):
        return self.eval_config['fm']['valid_m2']


class FMValidErrantRunScript(
        ScoreRunScriptInterface,
        RunScript):

    def make_path(self):
        return 'errant_fm_valid.sh'


def fm_valid_errant():
    valid_result_table = M2ResultTableFactory().make('fm', 'valid')

    script_list = []
    for index in make_train_indices():
        best_epoch = max(valid_result_table[index]).outdir.epoch
        outdir = SingleOutDir(index, 'fm', 'valid', best_epoch)
        script = FMValidErrantJobScript(outdir)
        script_list.append(script)
    FMValidErrantRunScript(script_list)


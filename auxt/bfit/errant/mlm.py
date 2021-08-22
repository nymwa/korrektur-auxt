from auxt.util.load import load_config
from auxt.expt.result.m2 import M2ResultTableFactory
from auxt.directory.expt.outdir import EnsembleMLMRerankOutDir
from auxt.expt.score.run import ScoreRunScriptInterface
from auxt.util.prod import make_train_indices
from auxt.script.run import RunScript
from .util import ErrantJobScript

class NamedErrantJobScript(ErrantJobScript):

    def __init__(self, outdir, name):
        self.name = name
        super().__init__(outdir)

    def make_m2_name(self):
        return 'errant.{}.m2'.format(self.name)

    def result_name(self):
        return 'errant.{}.txt'.format(self.name)

    def cat1_name(self):
        return 'errant.{}.cat1'.format(self.name)

    def cat2_name(self):
        return 'errant.{}.cat2'.format(self.name)

    def cat3_name(self):
        return 'errant.{}.cat3'.format(self.name)

    def corrected_path(self):
        x = 'best.{}.txt'.format(self.name)
        return self.outdir.make_path(x)

    def make_path(self):
        x = 'errant.{}.sh'.format(self.name)
        return self.outdir.make_path(x)


class FMValidNamedErrantJobScript(NamedErrantJobScript):

    def original_path(self):
        return self.eval_config['fm']['valid_src']

    def reference_path(self):
        return self.eval_config['fm']['valid_m2']


class FMTestNamedErrantJobScript(NamedErrantJobScript):

    def original_path(self):
        return self.eval_config['fm']['test_src']

    def reference_path(self):
        return self.eval_config['fm']['test_m2']


class FMMLMErrantRunScript(
        ScoreRunScriptInterface,
        RunScript):

    def make_path(self):
        return 'errant_fm_mlm.sh'


def fm_mlm_errant():
    config = load_config()

    script_list = []
    for arch in config['rerank']['fm']['mlm_arch_list']:
        for l in config['rerank']['lambda']:
            script_list.append(
                    FMValidNamedErrantJobScript(
                        EnsembleMLMRerankOutDir(
                            'fm', 'valid', arch),
                        int(l * 1000)))
            script_list.append(
                    FMTestNamedErrantJobScript(
                        EnsembleMLMRerankOutDir(
                            'fm', 'test', arch),
                        int(l * 1000)))

    FMMLMErrantRunScript(script_list)


from auxt.script.run import RunScript
from .util import (
        FalkoMerlinValidEnsembleR2LRerankJobScriptInterface,
        FalkoMerlinTestEnsembleR2LRerankJobScriptInterface,
        FalkoMerlinEnsembleR2LRerankRunScriptGeneratorInterface)
from auxt.expt.job import ExptJobScript
from auxt.generator.run import EnsembleR2LRerankRunScriptGenerator
from auxt.expt.r2l_rerank.job import EnsembleR2LRerankJobScript

class FalkoMerlinEnsembleR2LRerankJobScript(EnsembleR2LRerankJobScript):

    def get_score_reference(self):
        return True

    def get_max_tokens(self):
        return self.config['rerank'].get('max_tokens', 20000)

    def make_path(self):
        return self.outdir.make_path('rerank.sh')

    def make(self):
        command = self.make_generate_command()

        self.append('{} \\'.format(command))
        self.append('   | r2l2tsv \\')
        self.append('   | merge-r2l {} \\'.format(self.outdir.make_path('../output.yaml')))
        self.append('   | tee {} \\'.format(self.outdir.make_path('output.yaml')))
        self.append('   | select-best --r2l \\')
        self.append('   > {}'.format(self.outdir.make_path('best.txt')))


class FalkoMerlinValidEnsembleR2LRerankJobScript(
        FalkoMerlinValidEnsembleR2LRerankJobScriptInterface,
        FalkoMerlinEnsembleR2LRerankJobScript):
    pass


class FalkoMerlinTestEnsembleR2LRerankJobScript(
        FalkoMerlinTestEnsembleR2LRerankJobScriptInterface,
        FalkoMerlinEnsembleR2LRerankJobScript):
    pass


class FalkoMerlinEnsembleR2LRerankRunScript(RunScript):

    def make_path(self):
        return 'r2l_rerank_fm_ensemble.sh'


class FalkoMerlinEnsembleR2LRerankRunScriptGenerator(
        FalkoMerlinEnsembleR2LRerankRunScriptGeneratorInterface,
        EnsembleR2LRerankRunScriptGenerator):

    def __init__(self):
        self.dataset = 'fm'
        self.valid_job_class = FalkoMerlinValidEnsembleR2LRerankJobScript
        self.test_job_class = FalkoMerlinTestEnsembleR2LRerankJobScript
        self.run_class = FalkoMerlinEnsembleR2LRerankRunScript
        super().__init__()


def fm_ensemble_r2l_rerank():
    FalkoMerlinEnsembleR2LRerankRunScriptGenerator().make()


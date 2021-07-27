from auxt.script.run import RunScript
from auxt.expt.mlm_rerank.job import EnsembleMLMRerankJobScript
from auxt.generator.run import EnsembleMLMRerankRunScriptGenerator

class FalkoMerlinEnsembleMLMRerankJobScript(EnsembleMLMRerankJobScript):

    def make_is_detokenized(self):
        return self.config['rerank'].get('detokenize', False)


class FalkoMerlinEnsembleMLMRerankRunScript(RunScript):

    def make_path(self):
        return 'mlm_rerank_fm_ensemble.sh'


class FalkoMerlinEnsembleMLMRerankRunScriptGenerator(
        EnsembleMLMRerankRunScriptGenerator):

    def __init__(self):
        self.dataset = 'fm'
        self.valid_job_class = FalkoMerlinEnsembleMLMRerankJobScript
        self.test_job_class = self.valid_job_class
        self.run_class = FalkoMerlinEnsembleMLMRerankRunScript
        super().__init__()


def fm_ensemble_mlm_rerank():
    FalkoMerlinEnsembleMLMRerankRunScriptGenerator().make()


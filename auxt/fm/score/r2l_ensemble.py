from auxt.script.run import RunScript
from .util import FalkoMerlinScoreRunScriptGeneratorInterface
from auxt.expt.score.run import ScoreRunScriptInterface
from auxt.generator.run import EnsembleR2LRerankRunScriptGenerator
from .ensemble import (
        FalkoMerlinValidEnsembleScoreJobScript,
        FalkoMerlinTestEnsembleScoreJobScript)

class FalkoMerlinEnsembleR2LRerankScoreRunScript(
        ScoreRunScriptInterface,
        RunScript):

    def make_path(self):
        return 'score_fm_r2l_reranked_ensemble.sh'


class FalkoMerlinEnsembleR2LRerankScoreRunScriptGenerator(
        FalkoMerlinScoreRunScriptGeneratorInterface,
        EnsembleR2LRerankRunScriptGenerator):

    def __init__(self):
        self.valid_job_class = FalkoMerlinValidEnsembleScoreJobScript
        self.test_job_class = FalkoMerlinTestEnsembleScoreJobScript
        self.run_class = FalkoMerlinEnsembleR2LRerankScoreRunScript
        super().__init__()


def fm_ensemble_r2l_reranked_score():
    FalkoMerlinEnsembleR2LRerankScoreRunScriptGenerator().make()


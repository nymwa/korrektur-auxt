from auxt.script.run import RunScript
from .util import FalkoMerlinScoreRunScriptGeneratorInterface
from auxt.expt.score.run import ScoreRunScriptInterface
from auxt.generator.run import EnsembleMLMRerankScoreRunScriptGenerator
from auxt.expt.score.m2 import M2ScoreJobInterface
from auxt.expt.score.job import NamedGECScoreJobScript
from .util import (
        FalkoMerlinValidScoreJobScriptInterface,
        FalkoMerlinTestScoreJobScriptInterface)

class FalkoMerlinValidEnsembleMLMRerankScoreJobScript(
        FalkoMerlinValidScoreJobScriptInterface,
        M2ScoreJobInterface,
        NamedGECScoreJobScript):
    pass


class FalkoMerlinTestEnsembleMLMRerankScoreJobScript(
        FalkoMerlinTestScoreJobScriptInterface,
        M2ScoreJobInterface,
        NamedGECScoreJobScript):
    pass


class FalkoMerlinEnsembleMLMRerankScoreRunScript(
        ScoreRunScriptInterface,
        RunScript):

    def make_path(self):
        return 'score_fm_mlm_reranked_ensemble.sh'


class FalkoMerlinEnsembleMLMRerankScoreRunScriptGenerator(
        FalkoMerlinScoreRunScriptGeneratorInterface,
        EnsembleMLMRerankScoreRunScriptGenerator):

    def __init__(self):
        self.valid_job_class = FalkoMerlinValidEnsembleMLMRerankScoreJobScript
        self.test_job_class = FalkoMerlinTestEnsembleMLMRerankScoreJobScript
        self.run_class = FalkoMerlinEnsembleMLMRerankScoreRunScript
        super().__init__()


def fm_ensemble_mlm_reranked_score():
    FalkoMerlinEnsembleMLMRerankScoreRunScriptGenerator().make()


from auxt.expt.job import ExptJobScript

class ScoreJobScript(ExptJobScript):
    def make_path(self):
        return self.outdir.make_path('score.sh')

class GECScoreJobScript(ScoreJobScript):
    def corrected_path(self):
        return self.outdir.make_path('best.txt')


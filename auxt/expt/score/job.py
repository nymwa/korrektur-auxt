from auxt.expt.job import ExptJobScript

class ScoreJobScript(ExptJobScript):

    def make_path(self):
        return self.outdir.make_path('score.sh')


class GECScoreJobScript(ScoreJobScript):

    def corrected_path(self):
        return self.outdir.make_path('best.txt')

    def make_result_name(self):
        return 'result'


class NamedGECScoreJobScript(GECScoreJobScript):

    def __init__(self, outdir, name):
        self.name = name
        super().__init__(outdir)

    def corrected_path(self):
        return self.outdir.make_path('best.{}.txt'.format(self.name))

    def make_path(self):
        return self.outdir.make_path('score.{}.sh'.format(self.name))

    def make_result_name(self):
        return 'result.{}'.format(self.name)


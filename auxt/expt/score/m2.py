from auxt.expt.job import EvalExptJobScriptInterface

class M2ScoreJobInterface(EvalExptJobScriptInterface):

    def make_output_name(self):
        return self.make_result_name() + '.txt'

    def make(self):
        scorer_path = self.eval_config['m2scorer']
        output_name = self.make_output_name()
        self.append('python2 {} {} {} > {}'.format(
            scorer_path,
            self.corrected_path(),
            self.reference_path(),
            self.outdir.make_path(output_name)))


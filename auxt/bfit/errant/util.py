from auxt.expt.job import (
        EvalExptJobScriptInterface,
        ExptJobScript)

class ErrantJobScript(EvalExptJobScriptInterface, ExptJobScript):

    def make_environment_source_path(self):
        return self.eval_config['errant_source']

    def make_path(self):
        return self.outdir.make_path('errant.sh')

    def make_m2_name(self):
        return 'errant.m2'

    def corrected_path(self):
        return self.outdir.make_path('best.txt')

    def result_name(self):
        return 'errant.txt'

    def cat1_name(self):
        return 'errant.cat1'

    def cat2_name(self):
        return 'errant.cat2'

    def cat3_name(self):
        return 'errant.cat3'

    def make(self):
        m2_path = self.outdir.make_path(self.make_m2_name())

        self.append('OMP_NUM_THREADS=1 python {} -orig {} -cor {} -out {} -lang de'.format(
            self.eval_config['errant_parallel_to_m2'],
            self.original_path(),
            self.corrected_path(),
            m2_path))

        compare_path = self.eval_config['errant_compare_to_m2']
        reference = self.reference_path()

        self.append('python {} -hyp {} -ref {} > {}'.format(
            compare_path, m2_path, reference,
            self.outdir.make_path(self.result_name())))
        self.append('python {} -hyp {} -ref {} -cat 1 > {}'.format(
            compare_path, m2_path, reference,
            self.outdir.make_path(self.cat1_name())))
        self.append('python {} -hyp {} -ref {} -cat 2 > {}'.format(
            compare_path, m2_path, reference,
            self.outdir.make_path(self.cat2_name())))
        self.append('python {} -hyp {} -ref {} -cat 3 > {}'.format(
            compare_path, m2_path, reference,
            self.outdir.make_path(self.cat3_name())))


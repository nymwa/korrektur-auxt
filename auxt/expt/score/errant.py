#from auxt.expt.job import EvalExptJobScriptInterface
#
#class ErrantScoreJobInterface(ErrantScoreJobInterface):
#
#    def make_environment_source_path(self):
#        return self.eval_config['errant_source_path']
#
#    def make_output_name(self):
#        return 
#
#    def make(self):
#        scorer_path = self.eval_config['errant_scorer']
#
#        self.append('OMP_NUM_THREADS=1 python {} -orig {} -cor {} -out {} -land de'.format(
#            self.eval_config['errant_parallel_to_m2'],
#            self.original_path(),
#            self.corrected_path(),
#            output_path))
#
#        reference = self.reference_path()
#        self.append('python {} -hyp {} -ref {} > {}'.format(
#            reference, output_path,
#            self.outdir.make_path('
#

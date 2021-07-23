from .util import (
        FalkoMerlinValidEnsembleReprocJobScriptInterface,
        FalkoMerlinTestEnsembleReprocJobScriptInterface)
from auxt.expt.job import ExptJobScript, EvalExptJobScriptInterface
from auxt.generator.run import EnsembleRunScriptGenerator

class FalkoMerlinEnsembleReprocJobScript(ExptJobScript):

    def make_path(self):
        return self.outdir.make_path('r2l_reproc.sh')



class FalkoMerlinValidEnsembleReprocJobScript:

    def make(self):
        self.append('ls')


#class FalkoMerlinEnsembleReprocRunScriptGenerator(
#        
#        EnsembleRunScriptGenerator):

from auxt.expt.result.m2 import M2ResultTableFactory

def fm_ensemble_r2l_reproc():
    factory = M2ResultTableFactory()
    l2r_valid_result_table = factory.make('fm', 'valid')
    r2l_valid_result_table = factory.make('fm', 'valid',
            base = '../trgonly_r2l')
    print(l2r_valid_result_table.show(ndigits = 4))
    print(r2l_valid_result_table.show(ndigits = 4))


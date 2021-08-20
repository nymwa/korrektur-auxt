from auxt.expt.result.fscore import FScoreResultList
from auxt.expt.result.m2 import M2Result, M2ResultTableFactory
from auxt.expt.result.printer import print_result

def conll_result():
    print_result('wf', M2Result, FScoreResultList, M2ResultTableFactory, 4,
            'CoNLL 13 (valid)', 'CoNLL 14 (test)')


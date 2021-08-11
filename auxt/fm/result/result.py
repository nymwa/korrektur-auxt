from auxt.expt.result.fscore import FScoreResultList
from auxt.expt.result.m2 import M2Result, M2ResultTableFactory
from auxt.expt.result.printer import print_result

def fm_result():
    print_result('fm', M2Result, FScoreResultList, M2ResultTableFactory, 4,
            'Falko Merlin Valid', 'Falko Merlin Test')


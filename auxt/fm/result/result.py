from auxt.expt.result.fscore import FScoreResultList
from auxt.expt.result.m2 import M2Result, M2ResultTableFactory
from auxt.expt.result.util import (
        show_test_single_result,
        show_valid_ensemble_result,
        show_test_ensemble_result,
        show_valid_r2l_reranked_ensemble_result,
        show_test_r2l_reranked_ensemble_result)

def fm_result():
    print('----- Falko Merlin Valid -----')
    valid_result_table = M2ResultTableFactory().make('fm', 'valid')
    print(valid_result_table.show())
    show_valid_ensemble_result('fm', M2Result)
    show_valid_r2l_reranked_ensemble_result('fm', M2Result)

    print('\n----- Falko Merlin Test -----')
    show_test_single_result('fm', valid_result_table, M2Result, FScoreResultList)
    show_test_ensemble_result('fm', M2Result)
    show_test_r2l_reranked_ensemble_result('fm', M2Result)


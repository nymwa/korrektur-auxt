from auxt.parser.score.valid import set_valid_fm_score
from auxt.parser.score.test import set_test_fm_score
from auxt.parser.score.ensemble import set_ensemble_fm_score
from auxt.parser.score.r2l import set_r2l_fm_score
from auxt.parser.score.mlm import set_mlm_fm_score

def set_fm_score(second):
    parser = second.add_parser('fm')
    third = parser.add_subparsers()
    set_valid_fm_score(third)
    set_test_fm_score(third)
    set_ensemble_fm_score(third)
    set_r2l_fm_score(third)
    set_mlm_fm_score(third)


def set_score(first):
    parser = first.add_parser('score')
    second = parser.add_subparsers()
    set_fm_score(second)


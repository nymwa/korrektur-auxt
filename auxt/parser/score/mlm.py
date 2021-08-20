from .mlm_ensemble import (
        set_mlm_ensemble_fm_score,
        set_mlm_ensemble_bfit_score)

def set_mlm_fm_score(third):
    parser = third.add_parser('mlm')
    fourth = parser.add_subparsers()
    set_mlm_ensemble_fm_score(fourth)


def set_mlm_bfit_score(third):
    parser = third.add_parser('mlm')
    fourth = parser.add_subparsers()
    set_mlm_ensemble_bfit_score(fourth)


from .mlm_ensemble import set_mlm_ensemble_fm_score

def set_mlm_fm_score(third):
    parser = third.add_parser('mlm')
    fourth = parser.add_subparsers()
    set_mlm_ensemble_fm_score(fourth)


from .r2l_ensemble import set_r2l_ensemble_fm_score

def set_r2l_fm_score(third):
    parser = third.add_parser('r2l')
    fourth = parser.add_subparsers()
    set_r2l_ensemble_fm_score(fourth)


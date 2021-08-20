from auxt.fm.score.ensemble import fm_ensemble_score
from auxt.bfit.score.ensemble import bfit_ensemble_score

def fm_ensemble_score_command(args):
    fm_ensemble_score()


def set_ensemble_fm_score(third):
    parser = third.add_parser('ensemble')
    parser.set_defaults(handler = fm_ensemble_score_command)


def bfit_ensemble_score_command(args):
    bfit_ensemble_score(fm = args.fm)


def set_ensemble_bfit_score(third):
    parser = third.add_parser('ensemble')
    parser.add_argument('-f', '--fm', action = 'store_true')
    parser.set_defaults(handler = bfit_ensemble_score_command)


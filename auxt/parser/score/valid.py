from auxt.fm.score.valid import fm_valid_score
from auxt.bfit.score.valid import bfit_valid_score

def fm_valid_score_command(args):
    fm_valid_score()


def set_valid_fm_score(third):
    parser = third.add_parser('valid')
    parser.set_defaults(handler = fm_valid_score_command)


def bfit_valid_score_command(args):
    bfit_valid_score(fm = args.fm)


def set_valid_bfit_score(third):
    parser = third.add_parser('valid')
    parser.add_argument('-f', '--fm', action = 'store_true')
    parser.set_defaults(handler = bfit_valid_score_command)


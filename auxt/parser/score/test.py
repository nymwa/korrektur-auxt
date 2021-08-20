from auxt.fm.score.test import fm_test_score
from auxt.bfit.score.test import bfit_test_score

def fm_test_score_command(args):
    fm_test_score()


def set_test_fm_score(third):
    parser = third.add_parser('test')
    parser.set_defaults(handler = fm_test_score_command)


def bfit_test_score_command(args):
    bfit_test_score(fm = args.fm)


def set_test_bfit_score(third):
    parser = third.add_parser('test')
    parser.add_argument('-f', '--fm', action = 'store_true')
    parser.set_defaults(handler = bfit_test_score_command)


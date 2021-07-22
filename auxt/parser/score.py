from auxt.fm.score.valid import fm_valid_score
from auxt.fm.score.test import fm_test_score
from auxt.fm.score.ensemble import fm_ensemble_score

def fm_valid_score_command(args):
    fm_valid_score()


def set_valid_fm_score(third):
    parser = third.add_parser('valid')
    parser.set_defaults(handler = fm_valid_score_command)


def fm_test_score_command(args):
    fm_test_score()


def set_test_fm_score(third):
    parser = third.add_parser('test')
    parser.set_defaults(handler = fm_test_score_command)


def fm_ensemble_score_command(args):
    fm_ensemble_score()


def set_ensemble_fm_score(third):
    parser = third.add_parser('ensemble')
    parser.set_defaults(handler = fm_ensemble_score_command)


def set_fm_score(second):
    parser = second.add_parser('fm')
    third = parser.add_subparsers()
    set_valid_fm_score(third)
    set_test_fm_score(third)
    set_ensemble_fm_score(third)


def set_score(first):
    parser = first.add_parser('score')
    second = parser.add_subparsers()
    set_fm_score(second)


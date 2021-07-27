from auxt.fm.score.test import fm_test_score

def fm_test_score_command(args):
    fm_test_score()


def set_test_fm_score(third):
    parser = third.add_parser('test')
    parser.set_defaults(handler = fm_test_score_command)


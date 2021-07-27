from auxt.fm.score.valid import fm_valid_score

def fm_valid_score_command(args):
    fm_valid_score()


def set_valid_fm_score(third):
    parser = third.add_parser('valid')
    parser.set_defaults(handler = fm_valid_score_command)


from auxt.fm.score.ensemble import fm_ensemble_score

def fm_ensemble_score_command(args):
    fm_ensemble_score()


def set_ensemble_fm_score(third):
    parser = third.add_parser('ensemble')
    parser.set_defaults(handler = fm_ensemble_score_command)


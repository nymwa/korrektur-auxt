from auxt.fm.score.mlm_ensemble import fm_ensemble_mlm_reranked_score

def fm_ensemble_mlm_reranked_score_command(args):
    fm_ensemble_mlm_reranked_score()


def set_mlm_ensemble_fm_score(fourth):
    parser = fourth.add_parser('ensemble')
    parser.set_defaults(handler = fm_ensemble_mlm_reranked_score_command)


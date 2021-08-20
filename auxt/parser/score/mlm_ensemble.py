from auxt.fm.score.mlm_ensemble import fm_ensemble_mlm_reranked_score
from auxt.bfit.score.mlm_ensemble import bfit_ensemble_mlm_reranked_score

def fm_ensemble_mlm_reranked_score_command(args):
    fm_ensemble_mlm_reranked_score()


def bfit_ensemble_mlm_reranked_score_command(args):
    bfit_ensemble_mlm_reranked_score(fm = args.fm)


def set_mlm_ensemble_fm_score(fourth):
    parser = fourth.add_parser('ensemble')
    parser.set_defaults(handler = fm_ensemble_mlm_reranked_score_command)


def set_mlm_ensemble_bfit_score(fourth):
    parser = fourth.add_parser('ensemble')
    parser.add_argument('-f', '--fm', action = 'store_true')
    parser.set_defaults(handler = bfit_ensemble_mlm_reranked_score_command)


from auxt.fm.r2l.rerank.ensemble import fm_ensemble_r2l_rerank
from auxt.fm.mlm.rerank.ensemble import fm_ensemble_mlm_rerank
from auxt.bfit.r2l.rerank.ensemble import bfit_ensemble_r2l_rerank
from auxt.bfit.mlm.rerank.ensemble import bfit_ensemble_mlm_rerank

def fm_ensemble_r2l_rerank_command(args):
    fm_ensemble_r2l_rerank()

def set_ensemble_fm_r2l_rerank(fourth):
    parser = fourth.add_parser('ensemble')
    parser.set_defaults(handler = fm_ensemble_r2l_rerank_command)


def set_fm_r2l_rerank(third):
    parser = third.add_parser('fm')
    fourth = parser.add_subparsers()
    set_ensemble_fm_r2l_rerank(fourth)


def bfit_ensemble_r2l_rerank_command(args):
    bfit_ensemble_r2l_rerank(fm = args.fm)


def set_ensemble_bfit_r2l_rerank(fourth):
    parser = fourth.add_parser('ensemble')
    parser.add_argument('-f', '--fm', action = 'store_true')
    parser.set_defaults(handler = bfit_ensemble_r2l_rerank_command)


def set_bfit_r2l_rerank(third):
    parser = third.add_parser('bfit')
    fourth = parser.add_subparsers()
    set_ensemble_bfit_r2l_rerank(fourth)


def set_r2l_rerank(second):
    parser = second.add_parser('r2l')
    third = parser.add_subparsers()
    set_fm_r2l_rerank(third)
    set_bfit_r2l_rerank(third)


def fm_ensemble_mlm_rerank_command(args):
    fm_ensemble_mlm_rerank()


def set_ensemble_fm_mlm_rerank(fourth):
    parser = fourth.add_parser('ensemble')
    parser.set_defaults(handler = fm_ensemble_mlm_rerank_command)


def set_fm_mlm_rerank(third):
    parser = third.add_parser('fm')
    fourth = parser.add_subparsers()
    set_ensemble_fm_mlm_rerank(fourth)


def bfit_ensemble_mlm_rerank_command(args):
    bfit_ensemble_mlm_rerank(fm = args.fm)


def set_ensemble_bfit_mlm_rerank(fourth):
    parser = fourth.add_parser('ensemble')
    parser.add_argument('-f', '--fm', action = 'store_true')
    parser.set_defaults(handler = bfit_ensemble_mlm_rerank_command)


def set_bfit_mlm_rerank(third):
    parser = third.add_parser('bfit')
    fourth = parser.add_subparsers()
    set_ensemble_bfit_mlm_rerank(fourth)


def set_mlm_rerank(second):
    parser = second.add_parser('mlm')
    third = parser.add_subparsers()
    set_fm_mlm_rerank(third)
    set_bfit_mlm_rerank(third)


def set_rerank(first):
    parser = first.add_parser('rerank')
    second = parser.add_subparsers()
    set_r2l_rerank(second)
    set_mlm_rerank(second)


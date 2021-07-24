from auxt.fm.r2l.rescore.ensemble import fm_ensemble_r2l_rescore

def fm_ensemble_r2l_rescore_command(args):
    fm_ensemble_r2l_rescore()

def set_ensemble_fm_r2l_rescore(fourth):
    parser = fourth.add_parser('ensemble')
    parser.set_defaults(handler = fm_ensemble_r2l_rescore_command)


def set_fm_r2l_rescore(third):
    parser = third.add_parser('fm')
    fourth = parser.add_subparsers()
    set_ensemble_fm_r2l_rescore(fourth)


def set_r2l_rescore(second):
    parser = second.add_parser('r2l')
    third = parser.add_subparsers()
    set_fm_r2l_rescore(third)


def set_rescore(first):
    parser = first.add_parser('rescore')
    second = parser.add_subparsers()
    set_r2l_rescore(second)


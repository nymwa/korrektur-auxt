from auxt.fm.reproc.ensemble import fm_ensemble_r2l_reproc

def fm_ensemble_r2l_reproc_command(args):
    fm_ensemble_r2l_reproc()


def set_ensemble_fm_r2l_reproc(fourth):
    parser = fourth.add_parser('ensemble')
    parser.set_defaults(handler = fm_ensemble_r2l_reproc_command)


def set_fm_r2l_reproc(third):
    parser = third.add_parser('fm')
    fourth = parser.add_subparsers()
    set_ensemble_fm_r2l_reproc(fourth)


def set_r2l_reproc(second):
    parser = second.add_parser('r2l')
    third = parser.add_subparsers()
    set_fm_r2l_reproc(third)


def set_reproc(first):
    parser = first.add_parser('reproc')
    second = parser.add_subparsers()
    set_r2l_reproc(second)


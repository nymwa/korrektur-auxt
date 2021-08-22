from auxt.bfit.errant.valid import fm_valid_errant
from auxt.bfit.errant.test import fm_test_errant
from auxt.bfit.errant.ensemble import fm_ensemble_errant
from auxt.bfit.errant.r2l import fm_r2l_errant
from auxt.bfit.errant.mlm import fm_mlm_errant
from auxt.bfit.errant.show import fm_show_errant

def fm_valid_errant_command(args):
    fm_valid_errant()


def fm_test_errant_command(args):
    fm_test_errant()


def fm_ensemble_errant_command(args):
    fm_ensemble_errant()


def fm_r2l_errant_command(args):
    fm_r2l_errant()


def fm_mlm_errant_command(args):
    fm_mlm_errant()


def fm_show_errant_command(args):
    fm_show_errant()


def set_valid_fm_errant(third):
    parser = third.add_parser('valid')
    parser.set_defaults(handler = fm_valid_errant_command)


def set_test_fm_errant(third):
    parser = third.add_parser('test')
    parser.set_defaults(handler = fm_test_errant_command)


def set_ensemble_fm_errant(third):
    parser = third.add_parser('ensemble')
    parser.set_defaults(handler = fm_ensemble_errant_command)


def set_r2l_fm_errant(third):
    parser = third.add_parser('r2l')
    parser.set_defaults(handler = fm_r2l_errant_command)


def set_mlm_fm_errant(third):
    parser = third.add_parser('mlm')
    parser.set_defaults(handler = fm_mlm_errant_command)


def set_show_fm_errant(third):
    parser = third.add_parser('show')
    parser.set_defaults(handler = fm_show_errant_command)


def set_fm_errant(second):
    parser = second.add_parser('fm')
    third = parser.add_subparsers()
    set_valid_fm_errant(third)
    set_test_fm_errant(third)
    set_ensemble_fm_errant(third)
    set_r2l_fm_errant(third)
    set_mlm_fm_errant(third)
    set_show_fm_errant(third)


def set_errant(first):
    parser = first.add_parser('errant')
    second = parser.add_subparsers()
    set_fm_errant(second)


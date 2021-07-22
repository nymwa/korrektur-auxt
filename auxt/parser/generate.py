from auxt.fm.generate.valid import fm_valid_generate
from auxt.fm.generate.test import fm_test_generate
from auxt.fm.generate.ensemble import fm_ensemble_generate

def fm_valid_generate_command(args):
    fm_valid_generate()


def set_valid_fm_generate(third):
    parser = third.add_parser('valid')
    parser.set_defaults(handler = fm_valid_generate_command)


def fm_test_generate_command(args):
    fm_test_generate()


def set_test_fm_generate(third):
    parser = third.add_parser('test')
    parser.set_defaults(handler = fm_test_generate_command)


def fm_ensemble_generate_command(args):
    fm_ensemble_generate()


def set_ensemble_fm_generate(third):
    parser = third.add_parser('ensemble')
    parser.set_defaults(handler = fm_ensemble_generate_command)


def set_fm_generate(second):
    parser = second.add_parser('fm')
    third = parser.add_subparsers()
    set_valid_fm_generate(third)
    set_test_fm_generate(third)
    set_ensemble_fm_generate(third)


def set_generate(first):
    parser = first.add_parser('generate')
    second = parser.add_subparsers()
    set_fm_generate(second)


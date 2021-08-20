from auxt.fm.result.result import fm_result
from auxt.conll.result.result import conll_result

def fm_result_command(args):
    fm_result()


def set_fm_result(second):
    parser = second.add_parser('fm')
    parser.set_defaults(handler = fm_result_command)


def conll_result_command(args):
    conll_result()


def set_conll_result(second):
    parser = second.add_parser('conll')
    parser.set_defaults(handler = conll_result_command)


def set_result(first):
    parser = first.add_parser('result')
    second = parser.add_subparsers()
    set_fm_result(second)
    set_conll_result(second)


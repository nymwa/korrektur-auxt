from auxt.fm.preproc.main import fm_preproc
from auxt.fmmt.preproc.main import fmmt_preproc

def fm_preproc_command(args):
    fm_preproc()


def set_fm_preproc(second):
    parser = second.add_parser('fm')
    parser.set_defaults(handler = fm_preproc_command)


def fmmt_preproc_command(args):
    fmmt_preproc()


def set_fmmt_preproc(second):
    parser = second.add_parser('fmmt')
    parser.set_defaults(handler = fmmt_preproc_command)


def set_preproc(first):
    parser = first.add_parser('preproc')
    second = parser.add_subparsers()
    set_fm_preproc(second)
    set_fmmt_preproc(second)


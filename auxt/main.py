from argparse import ArgumentParser
from auxt.conv.eval_config import convert_eval_config
from auxt.data.preproc.fm.main import fm_preproc
from auxt.train.main import train
from auxt.expt.generate.fm.valid import fm_valid_generate
from auxt.expt.generate.fm.test import fm_test_generate
from auxt.expt.generate.fm.ensemble import fm_ensemble_generate
from auxt.expt.score.fm.valid import fm_valid_score
from auxt.expt.score.fm.test import fm_test_score
from auxt.expt.score.fm.ensemble import fm_ensemble_score
from auxt.expt.result.fm.result import fm_result

def eval_config_conv_command(args):
    convert_eval_config()


def set_eval_config_conv(second):
    parser = second.add_parser('eval-config')
    parser.set_defaults(handler = eval_config_conv_command)


def set_conv(first):
    parser = first.add_parser('conv')
    second = parser.add_subparsers()
    set_eval_config_conv(second)

def fm_preproc_command(args):
    fm_preproc()


def set_fm_preproc(second):
    parser = second.add_parser('fm')
    parser.set_defaults(handler = fm_preproc_command)


def set_preproc(first):
    parser = first.add_parser('preproc')
    second = parser.add_subparsers()
    set_fm_preproc(second)


def train_command(args):
    train()


def set_train(first):
    parser = first.add_parser('train')
    parser.set_defaults(handler = train_command)


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


def fm_valid_score_command(args):
    fm_valid_score()


def set_valid_fm_score(third):
    parser = third.add_parser('valid')
    parser.set_defaults(handler = fm_valid_score_command)


def fm_test_score_command(args):
    fm_test_score()


def set_test_fm_score(third):
    parser = third.add_parser('test')
    parser.set_defaults(handler = fm_test_score_command)


def fm_ensemble_score_command(args):
    fm_ensemble_score()


def set_ensemble_fm_score(third):
    parser = third.add_parser('ensemble')
    parser.set_defaults(handler = fm_ensemble_score_command)


def set_fm_score(second):
    parser = second.add_parser('fm')
    third = parser.add_subparsers()
    set_valid_fm_score(third)
    set_test_fm_score(third)
    set_ensemble_fm_score(third)


def set_score(first):
    parser = first.add_parser('score')
    second = parser.add_subparsers()
    set_fm_score(second)


def fm_result_command(args):
    fm_result()


def set_fm_result(second):
    parser = second.add_parser('fm')
    parser.set_defaults(handler = fm_result_command)


def set_result(first):
    parser = first.add_parser('result')
    second = parser.add_subparsers()
    set_fm_result(second)


def add_first_parsers(first):
    set_conv(first)
    set_preproc(first)
    set_train(first)
    set_generate(first)
    set_score(first)
    set_result(first)


def main():
    parser = ArgumentParser()
    first = parser.add_subparsers()
    add_first_parsers(first)
    args = parser.parse_args()
    if hasattr(args, 'handler'):
        args.handler(args)


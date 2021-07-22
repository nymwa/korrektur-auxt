from argparse import ArgumentParser
from auxt.parser.conv import set_conv
from auxt.parser.preproc import set_preproc
from auxt.parser.train import set_train
from auxt.parser.generate import set_generate
from auxt.parser.score import set_score
from auxt.parser.result import set_result

def add_first_parsers(first):
    set_conv(first)
    set_preproc(first)
    set_train(first)
    set_generate(first)
    set_score(first)
    set_result(first)


def parse_args():
    parser = ArgumentParser()
    first = parser.add_subparsers()
    add_first_parsers(first)
    return parser.parse_args()


def main():
    args = parse_args()

    if hasattr(args, 'handler'):
        args.handler(args)


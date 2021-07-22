from auxt.conv.eval_config import convert_eval_config

def eval_config_conv_command(args):
    convert_eval_config()


def set_eval_config_conv(second):
    parser = second.add_parser('eval-config')
    parser.set_defaults(handler = eval_config_conv_command)


def set_conv(first):
    parser = first.add_parser('conv')
    second = parser.add_subparsers()
    set_eval_config_conv(second)


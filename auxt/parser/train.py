from auxt.train.main import train

def train_command(args):
    train()


def set_train(first):
    parser = first.add_parser('train')
    parser.set_defaults(handler = train_command)


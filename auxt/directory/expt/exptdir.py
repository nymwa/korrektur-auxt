from pathlib import Path
from auxt.directory.base import BaseDir

class ExptDir(BaseDir):

    def __init__(self, dataset, phase,
            base = None, checkpoint_base = None):

        self.dataset = dataset
        self.phase = phase

        if checkpoint_base is None:
            self.checkpoint_base = None
        else:
            self.checkpoint_base = Path(checkpoint_base).resolve()

        super().__init__(base = base)

    def make_single_checkpoint_path(self, index, epoch):
        if self.checkpoint_base is not None:
            base = self.checkpoint_base
        else:
            base = self.base

        checkpoint_path = (base
                / str(index)
                / 'checkpoints'
                / 'checkpoint{}.pt'.format(epoch))

        return str(checkpoint_path.resolve())


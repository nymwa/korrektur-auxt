from auxt.util.prod import make_epoch_indices
from auxt.directory.expt.exptdir import ExptDir
from auxt.directory.expt.outdir import SingleOutDir

class SinglePhaseDir(ExptDir):

    def __init__(self, index, dataset, phase,
            base = None, checkpoint_base = None):

        self.index = index
        self.epoch_indices = list(make_epoch_indices())
        super().__init__(dataset, phase, base = base)

    def make_outdir(self, epoch):
        return SingleOutDir(
                self.index,
                self.dataset,
                self.phase,
                epoch,
                base = self.base)

    def make_dir_path(self):
        return '{}/{}/{}'.format(
                self.index,
                self.dataset,
                self.phase)


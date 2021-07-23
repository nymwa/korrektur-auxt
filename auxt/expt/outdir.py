from pathlib import Path
from auxt.util.prod import make_epoch_indices

class OutDir:
    def __init__(self, dataset, base = None):
        self.dataset = dataset

        if base is None:
            self.base = Path('')
        else:
            self.base = Path(base)

    def make_path(self, file_name):
        path = self.base / self.make_outdir_path() / file_name
        return str(path.resolve())


class PhaseOutDir(OutDir):
    def __init__(self, dataset, phase, base = None):
        self.phase = phase
        super().__init__(dataset, base = base)


class SingleOutDir(PhaseOutDir):
    def __init__(self, index, dataset, phase, epoch, base = None):
        self.index = index
        self.epoch = epoch
        super().__init__(dataset, phase, base = base)

    def get_checkpoint_path(self):
        checkpoint_path = (self.base
                / str(self.index)
                / 'checkpoints'
                / 'checkpoint{}.pt'.format(self.epoch))
        return str(checkpoint_path.resolve())

    def make_outdir_path(self):
        return '{}/{}/{}/{}'.format(
                self.index,
                self.dataset,
                self.phase,
                self.epoch)


class EnsembleOutDir(PhaseOutDir):
    def __init__(self, dataset, phase, epoch_list = None, base = None):
        self.epoch_list = epoch_list
        super().__init__(dataset, phase, base = base)

    def get_single_checkpoint_path(self, index, epoch):
        checkpoint_path = (self.base
                / str(index)
                / 'checkpoints'
                / 'checkpoint{}.pt'.format(epoch))
        return str(checkpoint_path.resolve())

    def get_checkpoint_path(self):
        checkpoint_path_list = [
                self.get_single_checkpoint_path(index, epoch)
                for index, epoch in enumerate(self.epoch_list)]
        return ':'.join(checkpoint_path_list)

    def make_outdir_path(self):
        return 'ensemble/{}/{}'.format(
                self.dataset,
                self.phase)


class EnsembleRerankingOutDir(PhaseOutDir):
    def __init__(self, dataset, phase, arch, base = None):
        self.arch = arch
        super().__init__(dataset, phase, base = base)

    def make_outdir_path(self):
        return 'ensemble/{}/{}/{}'.format(
                self.dataset,
                self.phase,
                self.arch)


class SinglePhaseDir(PhaseOutDir):
    def __init__(self, index, dataset, phase, base = None):
        self.index = index
        self.epoch_indices = list(make_epoch_indices())
        super().__init__(dataset, phase, base = base)

    def make_outdir(self, epoch):
        return SingleOutDir(self.index, self.dataset,
                self.phase, epoch, base = self.base)


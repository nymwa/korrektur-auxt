from auxt.directory.expt.exptdir import ExptDir

class SingleOutDir(ExptDir):

    def __init__(self, index, dataset, phase, epoch,
            base = None, checkpoint_base = None):

        self.index = index
        self.epoch = epoch
        super().__init__(dataset, phase,
                base = base, checkpoint_base = checkpoint_base)

    def get_checkpoint_path(self):
        return self.make_single_checkpoint_path(self.index, self.epoch)

    def make_dir_path(self):
        return '{}/{}/{}/{}'.format(
                self.index,
                self.dataset,
                self.phase,
                self.epoch)


class EnsembleOutDir(ExptDir):

    def __init__(self, dataset, phase, epoch_list = None,
            base = None, checkpoint_base = None):

        self.epoch_list = epoch_list
        super().__init__(dataset, phase,
                base = base, checkpoint_base = checkpoint_base)

    def get_checkpoint_path(self):
        checkpoint_path_list = [
                self.make_single_checkpoint_path(index, epoch)
                for index, epoch in enumerate(self.epoch_list)]
        return ':'.join(checkpoint_path_list)

    def make_dir_path(self):
        return 'ensemble/{}/{}'.format(
                self.dataset,
                self.phase)


class EnsembleR2LRescoreOutDir(EnsembleOutDir):

    def make_dir_path(self):
        return 'ensemble/{}/{}/r2l'.format(
                self.dataset,
                self.phase)


class EnsembleMLMRescoreOutDir(ExptDir):

    def __init__(self, dataset, phase, arch,
            base = None,
            checkpoint_base = None):
        self.arch = arch
        super().__init__(dataset, phase,
                base = base, checkpoint_base = checkpoint_base)

    def make_dir_path(self):
        return 'ensemble/{}/{}/{}'.format(
                self.dataset,
                self.phase,
                self.arch)


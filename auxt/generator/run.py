from .generator import ScriptGenerator
from auxt.util.prod import make_train_indices, make_epoch_indices
from auxt.directory.expt.outdir import (
        SingleOutDir,
        EnsembleOutDir,
        EnsembleR2LRescoreOutDir)

class RunScriptGenerator(ScriptGenerator):

    def get_best_epoch(self, index):
        result_list = self.valid_result_table[index]
        return max(result_list).outdir.epoch


class SingleRunScriptGenerator(RunScriptGenerator):
    def __init__(self):
        self.script_table = self.make_script_table()
        super().__init__()

    def make_outdir_table(self):
        return [self.make_outdir_list(index)
                for index in make_train_indices()]

    def make_script_list(self, outdir_list):
        return [self.job_class(outdir)
                for outdir in outdir_list]

    def make_script_table(self):
        outdir_table = self.make_outdir_table()
        return [self.make_script_list(outdir_list)
                for outdir_list in outdir_table]

    def make_expt_run(self):
        for index, script_list in enumerate(self.script_table):
            self.expt_run_class(index, script_list)

    def make_all_run(self):
        script_list = [script
            for script_list in self.script_table
            for script in script_list]
        self.all_run_class(script_list)

    def make(self):
        self.make_expt_run()
        self.make_all_run()


class ValidSingleRunScriptGenerator(SingleRunScriptGenerator):

    def __init__(self):
        self.phase = 'valid'
        super().__init__()

    def make_outdir_list(self, index):
        return [SingleOutDir(index, self.dataset, self.phase, epoch)
                for epoch in make_epoch_indices()]


class TestSingleRunScriptGenerator(SingleRunScriptGenerator):

    def __init__(self):
        self.phase = 'test'
        super().__init__()

    def make_outdir_list(self, index):
        best_epoch = self.get_best_epoch(index)
        return [SingleOutDir(index, self.dataset, self.phase, best_epoch)]


class EnsembleRunScriptGenerator(RunScriptGenerator):

    def get_epoch_indices(self):
        if hasattr(self, 'valid_result_table'):
            epoch_indices = [self.get_best_epoch(index)
                    for index in make_train_indices()]
        else:
            epoch_indices = None
        return epoch_indices

    def valid_make(self, epoch_indices):
        outdir = EnsembleOutDir(self.dataset, 'valid', epoch_indices)
        job_script = self.valid_job_class(outdir)
        return job_script

    def test_make(self, epoch_indices):
        outdir = EnsembleOutDir(self.dataset, 'test', epoch_indices)
        job_script = self.test_job_class(outdir)
        return job_script

    def make(self):
        epoch_indices = self.get_epoch_indices()
        script_list = []

        if hasattr(self, 'valid_job_class'):
            script_list.append(self.valid_make(epoch_indices))

        if hasattr(self, 'test_job_class'):
            script_list.append(self.test_make(epoch_indices))

        self.run_class(script_list)


class EnsembleR2LRescoreRunScriptGenerator(RunScriptGenerator):

    def valid_make(self):
        outdir = EnsembleR2LRescoreOutDir(self.dataset, 'valid')
        job_script = self.valid_job_class(outdir)
        return job_script

    def test_make(self):
        outdir = EnsembleR2LRescoreOutDir(self.dataset, 'test')
        job_script = self.test_job_class(outdir)
        return job_script

    def make(self):
        script_list = []

        if hasattr(self, 'valid_job_class'):
            script_list.append(self.valid_make())

        if hasattr(self, 'test_job_class'):
            script_list.append(self.test_make())

        self.run_class(script_list)


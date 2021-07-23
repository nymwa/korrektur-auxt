from auxt.util.prod import make_train_indices
from auxt.expt.outdir import SinglePhaseDir

class Result:
    def __init__(self, outdir, filename = None, l = None):
        self.outdir = outdir
        if filename is None:
            self.filename = 'result.txt'
        else:
            self.filename = filename
        self.l = l
        self.init_attr(self.read_result())

    def get_result_path(self):
        return self.outdir.make_path(self.filename)

    def read_result(self):
        result_path = self.get_result_path()
        with open(result_path) as f:
            x = f.readlines()
        return x


class ResultList(list):
    pass


class ResultListFactory:
    def make(self, phasedir):
        result_list = self.init_result_list()

        for epoch in phasedir.epoch_indices:
            try:
                outdir = phasedir.make_outdir(epoch)
                result = self.make_result(outdir)
                result_list.append(result)
            except FileNotFoundError:
                pass
            except IndexError:
                pass

        return result_list


class ResultTable(list):
    def maximum_list(self):
        return [max(result_list)
                for result_list in self
                if len(result_list) > 0]

    def get_best_epoch_list(self):
        return [max(result_list).outdir.epoch
                for result_list in self
                if len(result_list) > 0]


class ResultTableFactory:
    def __init__(self):
        self.result_list_factory = self.make_result_list_factory()

    def make(self, dataset, phase, base = None):
        result_table = self.init_result_table()

        for index in make_train_indices():
            phasedir = SinglePhaseDir(index, dataset, phase, base = base)
            result_list = self.result_list_factory.make(phasedir)
            result_table.append(result_list)

        return result_table


from auxt.util.load import load_config
from auxt.expt.result.m2 import M2ResultTableFactory
from auxt.util.prod import make_train_indices
from auxt.directory.expt.outdir import (
        SingleOutDir,
        EnsembleOutDir,
        EnsembleR2LRerankOutDir,
        EnsembleMLMRerankOutDir)

class ErrantResult:

    def __init__(self, outdir, l = None):
        self.outdir = outdir
        self.l = l
        self.filename = self.make_filename()
        self.init_attr(self.read_result())

    def make_filename(self):
        if self.l is None:
            filename = 'errant.cat2'
        else:
            filename = 'errant.{}.cat2'.format(int(self.l * 1000))
        return filename

    def get_result_path(self):
        return self.outdir.make_path(self.filename)

    def read_result(self):
        result_path = self.get_result_path()
        with open(result_path) as f:
            x = f.readlines()
        return x

    def init_attr(self, x):
        self.star = float(x[3].strip().split()[6])
        self.adj = float(x[4].strip().split()[6])
        self.adj_form = float(x[5].strip().split()[6])
        self.adp = float(x[6].strip().split()[6])
        self.adv = float(x[7].strip().split()[6])
        self.adv_form = float(x[8].strip().split()[6])
        self.aux = float(x[9].strip().split()[6])
        self.aux_form = float(x[10].strip().split()[6])
        self.conj = float(x[11].strip().split()[6])
        self.det = float(x[12].strip().split()[6])
        self.det_form = float(x[13].strip().split()[6])
        self.morph = float(x[14].strip().split()[6])
        self.noun = float(x[15].strip().split()[6])
        self.noun_form = float(x[16].strip().split()[6])
        self.orth = float(x[17].strip().split()[6])
        self.other = float(x[18].strip().split()[6])
        self.part = float(x[19].strip().split()[6])
        self.pnoun = float(x[20].strip().split()[6])
        self.pron = float(x[21].strip().split()[6])
        self.pron_form = float(x[22].strip().split()[6])
        self.punct = float(x[23].strip().split()[6])
        self.sconj = float(x[24].strip().split()[6])
        self.spell = float(x[25].strip().split()[6])
        self.verb = float(x[26].strip().split()[6])
        self.verb_form = float(x[27].strip().split()[6])
        self.wo = float(x[28].strip().split()[6])
        res = x[32].strip().split()
        self.p = float(res[3])
        self.r = float(res[4])
        self.f = float(res[5])

    def as_dict(self):
        return {
                '*': self.star,
                'ADJ': self.adj,
                'ADJ:FORM': self.adj_form,
                'ADP': self.adp,
                'ADV': self.adv,
                'ADV:FORM': self.adv_form,
                'AUX': self.aux,
                'AUX:FORM': self.aux_form,
                'CONJ': self.conj,
                'DET': self.det,
                'DET:FORM': self.det_form,
                'MORPH': self.morph,
                'NOUN': self.noun,
                'NOUN:FORM': self.noun_form,
                'ORTH': self.orth,
                'OTHER': self.other,
                'PART': self.part,
                'PNOUN': self.pnoun,
                'PRON': self.pron,
                'PRON:FORM': self.pron_form,
                'PUNCT': self.punct,
                'SCONJ': self.sconj,
                'SPELL': self.spell,
                'VERB': self.verb,
                'VERB:FORM': self.verb_form,
                'WO': self.wo,
                'p': self.p,
                'r': self.r,
                'f': self.f,
                }


def show_valid():
    result_table = M2ResultTableFactory().make('fm', 'valid')

    lst = []
    print('# valid')
    for index in make_train_indices():
        best_epoch = max(result_table[index]).outdir.epoch
        outdir = SingleOutDir(index, 'fm', 'valid', best_epoch)
        result = ErrantResult(outdir)
        print('valid_{} = '.format(index) + str(result.as_dict()))


def show_test():
    result_table = M2ResultTableFactory().make('fm', 'valid')

    lst = []
    print('# test')
    for index in make_train_indices():
        best_epoch = max(result_table[index]).outdir.epoch
        outdir = SingleOutDir(index, 'fm', 'test', best_epoch)
        result = ErrantResult(outdir)
        print('test_{} = '.format(index) + str(result.as_dict()))


def show_ensemble():
    print('# ensemble')
    valid_result = ErrantResult(EnsembleOutDir('fm', 'valid'))
    test_result = ErrantResult(EnsembleOutDir('fm', 'test'))
    print('valid_ens = ' + str(valid_result.as_dict()))
    print('test_ens = ' + str(test_result.as_dict()))


def show_r2l():
    print('# r2l')
    valid_result = ErrantResult(EnsembleR2LRerankOutDir('fm', 'valid'))
    test_result = ErrantResult(EnsembleR2LRerankOutDir('fm', 'test'))
    print('valid_r2l = ' + str(valid_result.as_dict()))
    print('test_r2l = ' + str(test_result.as_dict()))


def show_mlm():
    print('# mlm')
    config = load_config()
    for phase in ['valid', 'test']:
        for arch in config['rerank']['fm']['mlm_arch_list']:
            for l in config['rerank']['lambda']:
                result = ErrantResult(EnsembleMLMRerankOutDir('fm', phase, arch), l = l)
                print('{}_mlm_{} = '.format(phase, int(l * 1000)) + str(result.as_dict()))


def fm_show_errant():
    show_valid()
    show_test()
    show_ensemble()
    show_r2l()
    show_mlm()


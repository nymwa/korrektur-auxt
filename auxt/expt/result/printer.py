from auxt.util.prod import make_mlm_arch_list
from .util import (
        get_single_test_outdir_list,
        make_single_test_result_list,
        show_single_test_result,
        show_ensemble_result,
        show_r2l_reranked_ensemble_result,
        make_valid_mlm_reranked_ensemble_result_list,
        show_valid_mlm_reranked_ensemble_result,
        show_test_mlm_reranked_ensemble_result)

class ResultPrinter:

    def __init__(self, dataset, result_class, result_list_class, result_table_factory):
        self.dataset = dataset
        self.result_class = result_class
        self.result_list_class = result_list_class
        self.result_table_factory = result_table_factory

    def show_valid_single_result(self, ndigits = None):
        self.valid_result_table = self.result_table_factory().make(self.dataset, 'valid')
        print(self.valid_result_table.show(ndigits = ndigits))

    def show_test_single_result(self, ndigits = None):
        try:
            outdir_list = get_single_test_outdir_list(self.dataset, self.valid_result_table)
        except RuntimeError:
            return

        result_list = make_single_test_result_list(outdir_list, self.result_class, self.result_list_class)

        if result_list:
            show_single_test_result(result_list, ndigits = ndigits)

    def show_valid_ensemble_result(self):
        show_ensemble_result(self.dataset, 'valid', self.result_class)

    def show_test_ensemble_result(self):
        show_ensemble_result(self.dataset, 'test', self.result_class)

    def show_valid_r2l_reranked_ensemble_result(self):
        show_r2l_reranked_ensemble_result(self.dataset, 'valid', self.result_class)

    def show_test_r2l_reranked_ensemble_result(self):
        show_r2l_reranked_ensemble_result(self.dataset, 'test', self.result_class)

    def show_valid_mlm_reranked_ensemble_result(self):
        arch_list = make_mlm_arch_list()
        if arch_list is None:
            return

        self.best_lambda_dict = {}
        for arch in arch_list:
            result_list = make_valid_mlm_reranked_ensemble_result_list(
                    self.dataset, arch, self.result_class, self.result_list_class)
            if result_list:
                best_lambda = max(result_list).l
                show_valid_mlm_reranked_ensemble_result(arch, best_lambda, result_list)
                self.best_lambda_dict[arch] = best_lambda

    def show_test_mlm_reranked_ensemble_result(self):
        arch_list = make_mlm_arch_list()
        if arch_list is None:
            return

        for arch in arch_list:
            if arch in self.best_lambda_dict:
                try:
                    l = self.best_lambda_dict[arch]
                    show_test_mlm_reranked_ensemble_result(self.dataset, arch, l, self.result_class)
                except FileNotFoundError:
                    pass


def print_result(dataset,
        result_class, result_list_class, result_table_factory,
        ndigits = None, valid_message = None, test_message = None):

    printer = ResultPrinter(dataset, result_class, result_list_class,
            result_table_factory)

    print('----- {} -----'.format(valid_message))
    printer.show_valid_single_result(ndigits = ndigits)
    printer.show_valid_ensemble_result()
    printer.show_valid_r2l_reranked_ensemble_result()
    printer.show_valid_mlm_reranked_ensemble_result()

    if test_message is None:
        return

    print('')
    print('----- {} -----'.format(test_message))
    printer.show_test_single_result(ndigits = ndigits)
    printer.show_test_ensemble_result()
    printer.show_test_r2l_reranked_ensemble_result()
    printer.show_test_mlm_reranked_ensemble_result()


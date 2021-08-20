from auxt.util.prod import (
        make_train_indices,
        make_mlm_arch_list,
        make_lambda_list)
from auxt.directory.expt.outdir import (
        SingleOutDir,
        EnsembleOutDir,
        EnsembleR2LRerankOutDir,
        EnsembleMLMRerankOutDir)

def get_single_test_outdir_list(dataset, valid_result_table):
    best_epoch_list = valid_result_table.get_best_epoch_list()
    train_indices = make_train_indices()

    if len(train_indices) != len(best_epoch_list):
        raise RuntimeError

    return [SingleOutDir(index, dataset, 'test', epoch)
            for index, epoch in zip(train_indices, best_epoch_list)]


def make_single_test_result_list(outdir_list, result_class, result_list_class):
    result_list = result_list_class()
    for outdir in outdir_list:
        try:
            result = result_class(outdir)
            result_list.append(result)
        except IndexError:
            pass
        except FileNotFoundError:
            pass
    return result_list


def show_single_test_result(result_list, ndigits = None):
    for result in result_list:
        line = 'index {} ({}): {}'.format(
                result.outdir.index,
                result.outdir.epoch,
                result.show())
        print(line)
    print(result_list.show_avg(ndigits = ndigits))


def show_ensemble_result(dataset, phase, result_class):
    try:
        outdir = EnsembleOutDir(dataset, phase, epoch_list = None)
        result = result_class(outdir)
        print('ensemble: {}'.format(result.show()))
    except IndexError:
        pass
    except FileNotFoundError:
        pass


def show_r2l_reranked_ensemble_result(dataset, phase, result_class):
    try:
        outdir = EnsembleR2LRerankOutDir(dataset, phase)
        result = result_class(outdir)
        print('ensemble+r2l: {}'.format(result.show()))
    except IndexError:
        pass
    except FileNotFoundError:
        pass


def make_mlm_reranked_result(outdir, result_class, l):
    lmil = int(l * 1000)
    filename = 'result.{}.txt'.format(lmil)
    result = result_class(outdir, filename = filename, l = l)
    return result


def make_valid_mlm_reranked_ensemble_result_list(dataset, arch, result_class, result_list_class):
    lambda_list = make_lambda_list()
    result_list = result_list_class()
    outdir = EnsembleMLMRerankOutDir(dataset, 'valid', arch)
    for l in lambda_list:
        try:
            result = make_mlm_reranked_result(outdir, result_class, l)
            result_list.append(result)
        except IndexError:
            pass
        except FileNotFoundError:
            pass
    return result_list


def show_valid_mlm_reranked_ensemble_result(arch, best_lambda, result_list):
    line = 'rerank ({}, l={}, {}):\t{}'.format(
            arch, best_lambda, len(result_list), result_list.show_best())
    print(line)


def show_test_mlm_reranked_ensemble_result(dataset, arch, l, result_class):
    outdir = EnsembleMLMRerankOutDir(dataset, 'test', arch)
    result = make_mlm_reranked_result(outdir, result_class, l)
    line = 'rerank ({}, l={}):\t{}'.format(arch, l, result.show())
    print(line)


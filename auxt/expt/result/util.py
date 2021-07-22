from auxt.util.prod import make_train_indices
from auxt.expt.outdir import SingleOutDir, EnsembleOutDir

def get_single_test_outdir_list(dataset, valid_result_table):
    best_epoch_list = valid_result_table.get_best_epoch_list()
    train_indices = make_train_indices()

    if len(train_indices) != len(best_epoch_list):
        raise RuntimeError

    return [SingleOutDir(index, dataset, 'test', epoch)
            for index, epoch in zip(train_indices, best_epoch_list)]


def show_test_single_result(dataset, valid_result_table, result_class, result_list_class):
    test_outdir_list = get_single_test_outdir_list(dataset, valid_result_table)

    test_result_list = result_list_class()
    for outdir in test_outdir_list:
        try:
            result = result_class(outdir)
            test_result_list.append(result)
        except FileNotFoundError:
            pass

    if test_result_list:
        for result in test_result_list:
            line = 'index {} ({}): {}'.format(
                    result.outdir.index,
                    result.outdir.epoch,
                    result.show())
            print(line)
        print(test_result_list.show_avg())


def show_ensemble_result(dataset, phase, result_class):
    try:
        outdir = EnsembleOutDir(dataset, phase, epoch_list = None)
        result = result_class(outdir)
        print('ensemble: {}'.format(result.show()))
    except FileNotFoundError:
        pass


def show_valid_ensemble_result(dataset, result_class):
    show_ensemble_result(dataset, 'valid', result_class)


def show_test_ensemble_result(dataset, result_class):
    show_ensemble_result(dataset, 'test', result_class)


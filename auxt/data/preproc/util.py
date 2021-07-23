from auxt.util.load import load_config
from .run import PreprocRunScript

def get_first_index(config):
    if 'src_dict_path' in config:
        first_index = None
    elif 'first_index' in config:
        first_index = config['first_index']
    else:
        first_index = 0
    return first_index


def preproc_main_template(train_job_class, eval_job_class_list):
    config = load_config()
    num_iter = config['iter']

    first_index = get_first_index(config)

    # first train job
    if first_index is not None:
        first_script = train_job_class(first_index, first_index = first_index)

    script_list = []

    # valid / test job
    for job_class in eval_job_class_list:
        job = job_class(first_index)
        script_list.append(job)

    # rest train job
    for index in range(num_iter):
        if index != first_index:
            job = train_job_class(index, first_index = first_index)
            script_list.append(job)

    # first train run
    if first_index is not None:
        first_run = PreprocRunScript([first_script], first = True)

    # rest train & valid / test run
    rest_run = PreprocRunScript(script_list)


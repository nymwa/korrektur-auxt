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

def preproc_main_template(job_class):
    config = load_config()
    num_iter = config['iter']

    first_index = get_first_index(config)

    if first_index is not None:
        first_script = job_class(
                first_index, first_index = first_index)
    script_list = [
            job_class(
                index, first_index = first_index)
            for index in range(num_iter)
            if index != first_index]

    if first_index is not None:
        first_run = PreprocRunScript([first_script], first = True)
    rest_run = PreprocRunScript(script_list)


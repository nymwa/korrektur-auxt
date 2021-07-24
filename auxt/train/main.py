from pathlib import Path
from auxt.util.load import load_config, check_sub_config, load_sub_config
from auxt.util.num_iter import get_num_train_iter
from .worker import WorkerJobScript
from .job import TrainJobScript
from .run import TrainRunScript

def get_node_attributes():
    if check_sub_config():
        sub_config = load_sub_config()
        num_node = sub_config['train']['num_node']
        gpu_per_node = sub_config['train'].get('gpu_per_node', None)
        port = sub_config['train'].get('port', None)
    else:
        num_node = 1
        gpu_per_node = None
        port = None
    return num_node, gpu_per_node, port

def make_worker_scripts(num_node, gpu_per_node, port, num_iter):
    if num_node > 1:
        worker_script_list = [
                WorkerJobScript(index, num_node, gpu_per_node, port)
                for index in range(num_iter)]
    else:
        worker_script_list = [WorkerJobScript(index, num_node) for index in range(num_iter)]


def train():
    config = load_config()
    num_node, gpu_per_node, port = get_node_attributes()
    num_iter = get_num_train_iter()

    make_worker_scripts(num_node, gpu_per_node, port, num_iter)

    train_script_list = [TrainJobScript(index, num_node) for index in range(num_iter)]

    if check_sub_config():
        assert False
    else:
        run_script = TrainRunScript(train_script_list)


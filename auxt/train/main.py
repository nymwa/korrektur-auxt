from pathlib import Path
from auxt.util.load import load_config
from auxt.util.num_iter import get_num_train_iter
from .worker import WorkerJobScript
from .job import TrainJobScript
from .run import TrainRunScript

def train():
    config = load_config()
    sub_config = None
    num_node = 1

    num_iter = get_num_train_iter()

    if num_node > 1:
        worker_script_list = [
                WorkerJobScript(index, num_node, gpu_per_node, port)
                for index in range(num_iter)]
    else:
        worker_script_list = [WorkerJobScript(index, num_node) for index in range(num_iter)]

    train_script_list = [TrainJobScript(index, num_node) for index in range(num_iter)]

    run_script = TrainRunScript(train_script_list)


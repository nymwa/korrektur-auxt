from auxt.data.preproc.util import preproc_main_template
from .job import (
        FalkoMerlinTrainPreprocJobScript,
        FalkoMerlinValidPreprocJobScript,
        FalkoMerlinTestPreprocJobScript)

def fm_preproc():
    train_job_class = FalkoMerlinTrainPreprocJobScript
    eval_job_class_list = [
            FalkoMerlinValidPreprocJobScript,
            FalkoMerlinTestPreprocJobScript]
    preproc_main_template(train_job_class, eval_job_class_list)


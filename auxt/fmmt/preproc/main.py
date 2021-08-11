from auxt.data.preproc.util import preproc_main_template
from .job import (
        FMMTTrainPreprocJobScript,
        FMMTValidPreprocJobScript,
        FMMTTestPreprocJobScript)

def fmmt_preproc():
    train_job_class = FMMTTrainPreprocJobScript
    eval_job_class_list = [
            FMMTValidPreprocJobScript,
            FMMTTestPreprocJobScript]
    preproc_main_template(train_job_class, eval_job_class_list)


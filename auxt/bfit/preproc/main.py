from pathlib import Path
from auxt.util.load import load_config
from auxt.data.preproc.util import preproc_main_template
from .job import (
        BFITTrainPreprocJobScript,
        BFITEvalPreprocJobScript)

class FMValidPreprocJobScript(BFITEvalPreprocJobScript):

    name = 'fm-valid'

    def make_false_pref(self):
        return Path(self.config['fm_false_pref']).resolve()

    def make_test_pref(self):
        return Path(self.config['fm_valid_pref']).resolve()

class FMTestPreprocJobScript(BFITEvalPreprocJobScript):

    name = 'fm-test'

    def make_false_pref(self):
        return Path(self.config['fm_false_pref']).resolve()

    def make_test_pref(self):
        return Path(self.config['fm_test_pref']).resolve()

class WFValidPreprocJobScript(BFITEvalPreprocJobScript):

    name = 'wf-valid'

    def make_false_pref(self):
        return Path(self.config['wf_false_pref']).resolve()

    def make_test_pref(self):
        return Path(self.config['wf_valid_pref']).resolve()

class WFTestPreprocJobScript(BFITEvalPreprocJobScript):

    name = 'wf-test'

    def make_false_pref(self):
        return Path(self.config['wf_false_pref']).resolve()

    def make_test_pref(self):
        return Path(self.config['wf_test_pref']).resolve()

def bfit_preproc():
    config = load_config()
    train_job_class = BFITTrainPreprocJobScript
    eval_job_class_list = [
            FMValidPreprocJobScript,
            FMTestPreprocJobScript]

    if 'wf_valid_pref' in config:
        eval_job_class_list.append(WFValidPreprocJobScript)

    if 'wf_test_pref' in config:
        eval_job_class_list.append(WFTestPreprocJobScript)

    preproc_main_template(train_job_class, eval_job_class_list)


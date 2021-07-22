from auxt.data.preproc.util import preproc_main_template
from .job import FalkoMerlinPreprocJobScript

def fm_preproc():
    preproc_main_template(FalkoMerlinPreprocJobScript)


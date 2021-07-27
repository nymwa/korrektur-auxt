import yaml
from auxt.script.job import JobScript

class ExptJobScript(JobScript):
    def __init__(self, outdir):
        self.outdir = outdir
        super().__init__()


class EvalExptJobScriptInterface:
    def prepare(self):
        with open(self.config['eval_config']) as f:
            self.eval_config = yaml.safe_load(f)
        super().prepare()


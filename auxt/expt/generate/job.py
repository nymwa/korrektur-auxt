from auxt.expt.job import ExptJobScript, EvalExptJobScriptInterface
from auxt.util.fairseq_generate import fairseq_generate_command

class GenerationJobScript(ExptJobScript):
    def make_path(self):
        return self.outdir.make_path('generate.sh')

    def get_lenpen(self):
        return self.config['generate'].get('lenpen', 0.6)

    def get_score_reference(self):
        return False

    def make_generate_command(self):
        data_bin = self.get_data_bin()
        beam, nbest = self.get_beam_attributes()
        lenpen = self.get_lenpen()
        max_tokens = self.get_max_tokens()
        score_reference = self.get_score_reference()
        command = fairseq_generate_command(
                data_bin,
                self.outdir.get_checkpoint_path(),
                beam,
                nbest,
                lenpen,
                max_tokens,
                score_reference = score_reference)
        return command


class GECGenerationJobScript(
        EvalExptJobScriptInterface,
        GenerationJobScript):

    def get_beam_attributes(self):
        beam = self.config['generate'].get('beam', 12)
        nbest = self.config['generate'].get('nbest', beam)
        return beam, nbest

    def make(self):
        command = self.make_generate_command()
        output_path = self.outdir.make_path('outdir.yaml')
        best_text = self.outdir.make_path('best.txt')

        self.append('{} \\'.format(command))
        self.append('   | 2yaml \\')
        self.append('   | tee {} \\'.format(output_path))

        if self.config['generate'].get('r2l', False):
            self.append('   | select-best --reverse \\')
        else:
            self.append('   | select-best \\')

        self.append('   > {}'.format(best_text))


class GECSingleGenerationJobScript(GECGenerationJobScript):
    def get_max_tokens(self):
        return self.config['generate'].get('max_tokens', 10000)


class GECEnsembleGenerationJobScript(GECGenerationJobScript):
    def get_max_tokens(self):
        return self.config['generate'].get('ensemble_max_tokens',
                self.config['generate'].get('max_tokens', 2000))


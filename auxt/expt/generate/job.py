from pathlib import Path
from auxt.expt.job import ExptJobScript, EvalExptJobScriptInterface
from auxt.util.fairseq_interactive import fairseq_interactive_command

class GenerationJobScript(ExptJobScript):
    def make_path(self):
        return self.outdir.make_path('generate.sh')

    def get_data_bin(self):
        path = Path(self.config['data']) / '0' / 'data-bin'
        return str(Path(path).resolve())

    def get_generation_attributes(self):
        beam, nbest = self.get_beam_attributes()
        buffer_size, batch_size = self.get_batch_size_attributes()
        lenpen = self.config['generate'].get('lenpen', 0.6)
        return beam, nbest, buffer_size, batch_size, lenpen

    def make_interactive_command(self):
        data_bin = self.get_data_bin()
        beam, nbest, buffer_size, batch_size, lenpen = self.get_generation_attributes()

        command = fairseq_interactive_command(
                data_bin,
                self.outdir.get_checkpoint_path(),
                beam,
                nbest,
                buffer_size, 
                batch_size,
                lenpen)
        return command


class GECGenerationJobScript(
        EvalExptJobScriptInterface,
        GenerationJobScript):

    def get_beam_attributes(self):
        beam = self.config['generate'].get('beam', 12)
        nbest = self.config['generate'].get('nbest', beam)
        return beam, nbest

    def make(self):
        command = self.make_interactive_command()
        input_path = self.get_input_path()
        self.append('{} \\'.format(command))
        self.append('   < {} \\'.format(input_path))
        self.append('   | 2yaml \\')
        self.append('   | tee {} \\'.format(
            self.outdir.make_path('output.yaml')))
        if self.config['generate'].get('r2l', False):
            self.append('   | select-best --reverse \\')
        else:
            self.append('   | select-best \\')
        self.append('   > {}'.format(self.outdir.make_path('best.txt')))


class GECSingleGenerationJobScript(GECGenerationJobScript):
    def get_batch_size_attributes(self):
        buffer_size = self.config['generate'].get('buffer_size', 1024)
        batch_size = self.config['generate'].get('batch_size', 32)
        return buffer_size, batch_size


class GECEnsembleGenerationJobScript(GECGenerationJobScript):
    def get_batch_size_attributes(self):
        buffer_size = self.config['generate'].get('buffer_size', 1024)
        batch_size = self.config['generate'].get('ensemble_batch_size',
                self.config['generate'].get('batch_size', 32))
        return buffer_size, batch_size


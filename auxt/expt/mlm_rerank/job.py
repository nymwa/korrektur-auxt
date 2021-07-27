from auxt.expt.job import ExptJobScript

def mlm_rescore_command(arch, detokenize, max_tokens):
    command = ['mlm-scoring',
            '--arch {}'.format(arch)]
    if detokenize:
        command.append('--detokenize')
    command.append('--max-tokens {}'.format(max_tokens))
    return ' '.join(command)


def rerank_command(l, input_path, output_path, back_ground = False):
    command = 'select-best -l {} --r2l --mlm < {} > {}'.format(l, input_path, output_path)
    if back_ground:
        command = command + ' &'
    return command


class MLMRerankJobScript(ExptJobScript):

    def make_path(self):
        return self.outdir.make_path('rerank.sh')

    def make_rescore_command(self):
        command = mlm_rescore_command(
                self.outdir.arch,
                self.make_is_detokenized(),
                self.config['rerank'].get('max_tokens', 10000))
        self.append('{} \\'.format(command))
        self.append('   < {} \\'.format(self.make_input_path()))
        self.append('   > {}'.format(self.make_output_yaml_path()))

    def make_rerank_command(self, l):
        lmil = int(l * 1000)
        command = rerank_command(l,
                self.make_output_yaml_path(),
                self.make_best_text_path(lmil),
                back_ground = True)
        self.append(command)

    def make(self):
        self.make_rescore_command()

        for l in self.config['rerank']['lambda']:
            self.make_rerank_command(l)
        self.append('wait')


class EnsembleMLMRerankJobScript(MLMRerankJobScript):

    def make_input_path(self):
        return self.outdir.make_path('../r2l/output.yaml')

    def make_output_yaml_path(self):
        return self.outdir.make_path('output.yaml')

    def make_best_text_path(self, lmil):
        return self.outdir.make_path('best.{}.txt'.format(lmil))


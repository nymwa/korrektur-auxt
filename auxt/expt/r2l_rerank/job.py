from auxt.expt.generate.job import GenerationJobScript

class R2LRerankJobScript(GenerationJobScript):

    def get_score_reference(self):
        return True

    def make_path(self):
        return self.outdir.make_path('rerank.sh')


class EnsembleR2LRerankJobScript(R2LRerankJobScript):

    def get_max_tokens(self):
        return self.config['rerank'].get('max_tokens', 20000)

    def make(self):
        command = self.make_generate_command()

        self.append('{} \\'.format(command))
        self.append('   | r2l2tsv \\')
        self.append('   | merge-r2l {} \\'.format(
            self.outdir.make_path('../output.yaml')))
        self.append('   | tee {} \\'.format(
            self.outdir.make_path('output.yaml')))
        self.append('   | select-best --r2l \\')
        self.append('   > {}'.format(self.outdir.make_path('best.txt')))


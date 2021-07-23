from pathlib import Path
from auxt.script.job import JobScript
from auxt.util.command import spm_command, parallel_command

class DataJobScript(JobScript):
    # localdir = True

    def get_bpe_model_path(self):
        return Path(self.config['bpe_model']).resolve()

    def get_source_language(self):
        return self.config.get('source_lang', 'src')

    def get_target_language(self):
        return self.config.get('target_lang', 'trg')

    def get_language_pair(self):
        source_lang = self.get_source_language()
        target_lang = self.get_target_language()
        return source_lang, target_lang

    def get_threads(self):
        return self.config['threads']

    def get_lines(self):
        return self.config['lines']

    def get_source_dropout_probability(self):
        return self.config.get('source_dropout', None)

    def get_target_dropout_probability(self):
        return self.config.get('target_dropout', None)

    def get_dropout_probabilities(self):
        source_dropout = self.get_source_dropout_probability()
        target_dropout = self.get_target_dropout_probability()
        return source_dropout, target_dropout

    def make_spm_commands(self, parallel = False):
        src_dropout, trg_dropout = self.get_dropout_probabilities()
        src_command = spm_command('${MODELPATH}', dropout = src_dropout)
        trg_command = spm_command('${MODELPATH}', dropout = trg_dropout)

        if parallel and 'threads' in self.config:
            j = self.get_threads()
            L = self.get_lines()
            src_command = parallel_command(j, L, '"{}"'.format(src_command))
            trg_command = parallel_command(j, L, '"{}"'.format(trg_command))

        return src_command, trg_command


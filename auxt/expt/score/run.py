class ScoreRunScriptInterface:
    def is_await(self):
        if ('score' in self.config) and ('await' in self.config['score']):
            p = self.config['score']['await']
        else:
            p = super().is_await()
        return p

    def get_job(self):
        if ('score' in self.config) and ('jobs' in self.config['score']):
            n = self.config['score']['jobs']
        else:
            n = super().get_job()
        return n


class FairseqTrainCommand(list):
    def __init__(self, data_bin_path, log_file=None):
        super().__init__(['fairseq-train', data_bin_path])
        self.log_file = log_file

    def restore_file(self, restore_file):
        self.append('--restore-file {}'.format(restore_file))

    def seed(self, seed):
        self.append('--seed {}'.format(seed))

    def log(self):
        self += ['--log-interval 1', '--log-format simple']

    def save_interval(self, interval):
        self.append('--save-interval {}'.format(interval))

    def fp16(self):
        self.append('--fp16')

    def no_c10d(self):
        self.append('--ddp-backend=no_c10d')

    def epoch(self, max_epoch):
        self.append('--max-epoch {}'.format(max_epoch))

    def batch(self, update_freq, max_tokens):
        self += [
            '--update-freq {}'.format(update_freq),
            '--max-tokens {}'.format(max_tokens)]

    def dimensions_template(self, embed_dim, ffn_embed_dim, attention_heads):
        self += [
                '--encoder-embed-dim {}'.format(embed_dim),
                '--encoder-ffn-embed-dim {}'.format(ffn_embed_dim),
                '--encoder-attention-heads {}'.format(attention_heads),
                '--decoder-embed-dim {}'.format(embed_dim),
                '--decoder-ffn-embed-dim {}'.format(ffn_embed_dim),
                '--decoder-attention-heads {}'.format(attention_heads)]

    def dimensions_arch_template(self, embed_dim_default, ffn_embed_dim_default, attention_heads_default, ffn_embed_dim, attention_heads):
        if ffn_embed_dim is None:
            ffn_embed_dim = ffn_embed_dim_default
        if attention_heads is None:
            attention_heads = attention_heads_default
        self.dimensions_template(embed_dim_default, ffn_embed_dim, attention_heads)

    def dimensions(self, arch, ffn_embed_dim = None, attention_heads = None):
        if arch == 'tiny':
            self.dimensions_arch_template(128, 512, 2, ffn_embed_dim, attention_heads)
        elif arch == 'small':
            self.dimensions_arch_template(256, 1024, 4, ffn_embed_dim, attention_heads)
        elif arch == 'base':
            self.dimensions_arch_template(512, 2048, 8, ffn_embed_dim, attention_heads)
        elif arch == 'big':
            self.dimensions_arch_template(1024, 4096, 16, ffn_embed_dim, attention_heads)
        else:
            assert False

    def arch(self, prenorm, arch, share_all_embeddings, dropout, attention_dropout, activation_dropout, activation_fn,
            encoder_layers = 6, decoder_layers = 6,
            ffn_embed_dim = None, attention_heads = None):
        self.append('--arch transformer')

        if prenorm:
            self += [
                '--encoder-normalize-before',
                '--decoder-normalize-before']

        self.dimensions(arch, ffn_embed_dim, attention_heads)
        self.append('--encoder-layers {}'.format(encoder_layers))
        self.append('--decoder-layers {}'.format(decoder_layers))

        if share_all_embeddings:
            self.append('--share-all-embeddings')

        self += [
            '--dropout {}'.format(dropout),
            '--attention-dropout {}'.format(attention_dropout),
            '--activation-dropout {}'.format(activation_dropout),
            '--activation-fn {}'.format(activation_fn)]

    def adam(self, beta1, beta2):
        self += [
            '--optimizer adam',
            "--adam-betas '({}, {})'".format(beta1, beta2)]

    def inverse_sqrt(self, lr, warmup_updates, warmup_init_lr):
        self += [
            '--lr {}'.format(lr),
            '--lr-scheduler inverse_sqrt',
            '--warmup-updates {}'.format(warmup_updates),
            '--warmup-init-lr {}'.format(warmup_init_lr)]

    def constant(self, lr):
        self += [
            '--lr {}'.format(lr),
            '--lr-scheduler fixed']

    def clip_norm(self, clip_norm=1.0):
        self.append('--clip-norm {}'.format(clip_norm))

    def weight_decay(self, weight_decay):
        self.append('--weight-decay {}'.format(weight_decay))

    def label_smoothed_cross_entropy(self, label_smoothing=0.1):
        self += [
            '--criterion label_smoothed_cross_entropy',
            '--label-smoothing {}'.format(label_smoothing)]

    def reset_meters(self):
        self.append('--reset-meters')

    def reset_dataloader(self):
        self.append('--reset-dataloader')

    def reset_optimizer(self):
        self.append('--reset-optimizer')

    def reset_lr_scheduler(self):
        self.append('--reset-lr-scheduler')

    def distributed(self, num_nodes, gpus_per_node, port=54849):
        self += [
            '--distributed-world-size {}'.format(num_nodes * gpus_per_node),
            '--distributed-rank $(expr {} \* $OMPI_COMM_WORLD_RANK)'.format(gpus_per_node),
            '--distributed-init-method "tcp://${{1}}:{}"'.format(port),
            '--distributed-port {}'.format(port)]

    def __str__(self):
        if self.log_file is None:
            lst = self
        else:
            lst = self + ['| tee {}'.format(self.log_file)]
        return ' '.join(lst)


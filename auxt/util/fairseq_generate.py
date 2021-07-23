def fairseq_generate_command(
        data_bin,
        path,
        beam,
        nbest,
        lenpen,
        max_tokens,
        score_reference = False):
    lst = ['fairseq-generate',
            str(data_bin),
            '--path {}'.format(path),
            '--beam {}'.format(beam),
            '--nbest {}'.format(nbest),
            '--lenpen {}'.format(lenpen),
            '--max-tokens {}'.format(max_tokens)]
    if score_reference:
        lst.append('--score-reference')
    return ' '.join(lst)


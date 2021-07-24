def fairseq_generate_command(
        data_bin,
        path,
        lenpen,
        max_tokens,
        beam = None,
        nbest = None,
        score_reference = False):
    lst = ['fairseq-generate',
            str(data_bin),
            '--path {}'.format(path)]

    if score_reference:
        lst.append('--score-reference')
    else:
        lst.append('--beam {}'.format(beam))
        lst.append('--nbest {}'.format(nbest))

    lst.append('--lenpen {}'.format(lenpen))
    lst.append('--max-tokens {}'.format(max_tokens))

    return ' '.join(lst)


def fairseq_preprocess_command(
        source_lang,
        target_lang,
        dest_dir,
        threads,
        train_pref,
        valid_pref,
        test_pref = None,
        src_dict = None,
        trg_dict = None,
        joined_dict = True):

    lst = ['fairseq-preprocess',
            '--source-lang {}'.format(source_lang),
            '--target-lang {}'.format(target_lang),
            '--trainpref {}'.format(train_pref),
            '--validpref {}'.format(valid_pref)]

    if test_pref is not None:
        lst.append('--testpref {}'.format(test_pref))


    lst.append('--destdir {}'.format(dest_dir))
    lst.append('--workers {}'.format(threads))

    if src_dict is not None:
        lst.append('--srcdict {}'.format(src_dict))

    if trg_dict is not None:
        lst.append('--tgtdict {}'.format(trg_dict))

    if joined_dict:
        lst.append('--joined-dictionary')

    return ' '.join(lst)


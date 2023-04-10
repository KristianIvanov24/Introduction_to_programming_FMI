def validateSeq(sq):
    for seq in sq:
        if seq != 'A' and seq != 'C' and seq != 'T' and seq != 'G':
            return False
    return True


def revseq(sq):
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    result = ''
    for s in sq:
        result += complement[s]
    return result


def revcompseq(sq_lst):
    for sq in sq_lst:
        if not validateSeq(sq):
            return None

    return list(map(lambda seq: revseq(seq), sq_lst))

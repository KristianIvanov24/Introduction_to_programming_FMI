def validateSeq(sq):
    for seq in sq:
        if seq != 'A' and seq != 'C' and seq != 'T' and seq != 'G':
            return False
    return True


def revseq(sq):
    if not validateSeq(sq):
        return None

    if len(sq) == 1:
        return sq

    return sq[-1] + revseq(sq[:-1])

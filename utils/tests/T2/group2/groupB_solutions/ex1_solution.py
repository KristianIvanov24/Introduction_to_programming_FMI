def validateSeq(sq):
    for seq in sq:
        if seq != 'A' and seq != 'C' and seq != 'T' and seq != 'G':
            return False
    return True


def complseq(sq):
    if not validateSeq(sq):
        return None

    if len(sq) == 0:
        return ''

    if sq[0] == 'A':
        return 'T' + complseq(sq[1:])

    if sq[0] == 'T':
        return 'A' + complseq(sq[1:])

    if sq[0] == 'C':
        return 'G' + complseq(sq[1:])

    if sq[0] == 'G':
        return 'C' + complseq(sq[1:])

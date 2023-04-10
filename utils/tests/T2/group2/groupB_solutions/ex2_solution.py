def validateSeq(sq):
    for seq in sq:
        if seq != 'A' and seq != 'C' and seq != 'T' and seq != 'G':
            return False
    return True


def isATTinSeq(sq):
    return "ATT" in sq


def findAllATTinLst(sq_lst):
    for sq in sq_lst:
        if not validateSeq(sq):
            return None

    return list(filter(lambda s: isATTinSeq(s), sq_lst))

def search(self, reader, target):
    hi = 1
    while reader.get(hi) < target: 
        hi *= 2
    lo = int(hi/2)

    # find the first element which equals the target
    while lo<=hi:
        mid = lo + int((hi-lo)/2)
        v = reader.get(mid)
        if v == target: 
            return mid

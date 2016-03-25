def rvt(s):
    sl = s.split()
    sl.sort(reverse=Flase)
    print ''.join(sl)

def rv(s):
    sl = list(s)
    start, end = 0, len(sl) - 1
    while start < end:
        sl[start], sl[end] = sl[end], sl[start]
        start += 1
        end -= 1
    return ''.join(sl)


print rv('abc')

print rv('acccgavac')
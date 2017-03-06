def do_n(f, n):
    """
    """
    if n <= 0:
        return
    else:
        f
        do_n(f, n-1)
        print f

do_n(len('123456789'), 100)

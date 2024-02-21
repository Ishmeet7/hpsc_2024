def test_1():
    from numpy import cbrt
    from calc_cubrt import my_cubrt
    small=1.0e-10
    xvalues=[27,1000,0.001,0,1e9]
    for x in xvalues:
        s=mycubrt(x)
        s_numpy=cbrt(x)
        assert (s-s_numpy)<small ,f"cube root failed"

def test_2():
    from numpy import cbrt
    from calc_cubrt import my_cubrt
    small=1.0e-10
    xvalues=[-27,-90,"10"]
    for x in xvalues:
        s=mycubrt(x)
        s_numpy=cbrt(x)
        assert (s-s_numpy)<small ,f"cube root failed"
        

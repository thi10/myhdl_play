import myhdl as mhd

def IntSig(min, max):
    return mhd.Signal(mhd.intbv(val=0, min=min, max=max))

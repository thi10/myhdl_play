import myhdl as mhd

class design_interface(object):
	def __init__(self):
		self.sel = mhd.Signal(bool(0))
		self.A =  mhd.Signal(bool(0))
		self.B = mhd.Signal(bool(0))
		self.out = mhd.Signal(bool(0))

def top_design(circuit_ports):

	@mhd.always_comb
	def mux():
		if circuit_ports.sel == 0:
			circuit_ports.out.next = circuit_ports.A 
		else:
			circuit_ports.out.next = circuit_ports.B 
	return mux



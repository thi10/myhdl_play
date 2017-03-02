import myhdl as mhd
import led_counter.instar.instar as instar

class design_interface(object):
    def __init__(self, nleds):
        self.leds = instar.IntSig(min=0, max=(2**nleds)-1)
        self.clk = mhd.Signal(bool(0))
        self.reset = mhd.ResetSignal(0, 
                                     active=0,
                                     async=True)


def top_design(circuit_ports):

    @mhd.always_seq(circuit_ports.clk.posedge,
                    reset=circuit_ports.reset )
    def counter():
        circuit_ports.leds.next = circuit_ports.leds + 1

    return counter



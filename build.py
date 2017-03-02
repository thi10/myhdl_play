import myhdl as mhd
from led_counter import led_counter

def convert():
    circuit_ports = led_counter.design_interface(8)
    mhd.toVerilog(led_counter.top_design, circuit_ports)

if __name__ == '__main__':
    convert()

    


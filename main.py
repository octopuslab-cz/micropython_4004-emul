# emulator i4004 for specific hardware
# i2c expapder + inputs

import sys
from time import sleep
from intel4004_emu import translator
from intel4004_emu import executor
from intel4004_emu import consolex
from intel4004_interface import Enhanced_executor, interface_test, read_input, load_source


def run_src(src_file):    
    print("="*39)
    print("File: " + src_file)
    print("="*39)
    try:
        src = load_source(src_file)
        prg = translator.translate(src)
        cpu = Enhanced_executor()
        fetchState(cpu)
        cpu.run(prg)
    except Exception as e:
        sys.stderr.write("Error: %s\n" % e)
    print()
    print()


def fetchState(cpu):
    for i in range(2, len(sys.argv)):
        cpu.regs[i - 2] = int(sys.argv[i])


print("--- i4004 (e/si)mulator ---")
interface_test()

# run_src("examples4004/test.asm")
run_src("examples4004/simple.asm")
run_src("examples4004/hellow.asm")
# run_src("examples4004/toupper.asm")
# run_src("examples4004/strrev.asm")
run_src("examples4004/endless.asm")


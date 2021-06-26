# --- main "execut" class
# OctopusLab 2021

from time import sleep
from machine import Pin
from intel4004_emu import executor
from intel4004_emu import consolex

from utils.octopus import i2c_init
#from utils.i2c_expander import Expander8
from components.i2c_expander import Expander8
from utils.bits import neg, reverse, int2bin, get_bit, set_bit
# int2bin(reverse(b1))   >   '10011111'

DELAY = 0.5

INPUTS4 = True
i1 = Pin(39, Pin.IN)
i2 = Pin(34, Pin.IN)
i4 = Pin(35, Pin.IN)
i8 = Pin(26, Pin.IN)

I2C_EXP = True
byte8 = 0


if I2C_EXP:
   print("--- i2c 8bit expander init ---")
   i2c = i2c_init(True,200)
   # i2c.scan() > devices: [35, 58, 62, 60]

   exp8 = Expander8(60)
   exp8.write_8bit(255)
   sleep(1)
   exp8.write_8bit(0)

   for j in range(3):
    for i in range(4):
      byte8 = set_bit(byte8,i,1)
      exp8.write_8bit(byte8)
      sleep(0.2)
      byte8 = set_bit(byte8,i,0)

   print("--- ready ---")
   exp8.write_8bit(byte8)


def interface_test():
   print("--- interface: test---")
   inp4 = read_input()
   print("input", inp4, int2bin(inp4))
   exp8.write_8bit(inp4)
   sleep(2)
   exp8.write_8bit(0)


def load_source(src_file):
    f = open(src_file)
    lines = f.readlines()
    f.close()
    return lines


def read_input():
    return i8.value()*8 + i4.value()*4 + i2.value()*2 + i1.value()



class Enhanced_executor(executor.Executor, consolex.Consolex):
    
    def printRegs(self):
        print(' '.join([str(r) for r in self.regs]))
        print("acc=%d | cy=%d | ip=%d | dp=%d | cycles=%d" % (self.acc, self.cy, self.ip, self.dp, self.cycles))

    
    def printMemory(self, rows, cols):
        print("-"*39)
        print("Memory: ", rows, cols)
        for row in range(rows):
            for col in range(cols):
                print(self.memory[row * cols + col],end=" ")
            if (row * cols + col) % 16:
                print()
        print()


    def outputAcc(self):
        print("--- outputReg > ", self.acc)
        if I2C_EXP:
           exp8.write_8bit(self.acc)
        sleep(DELAY)


    def inputReg(self):
        print("--- inputReg:")
        self.acc = int(input())
        # print("--- o.reg ---", self.acc)
        sleep(1)


    def inputRead(self):
        inp4 = read_input()
        print("inputRead", inp4, int2bin(inp4))
        self.acc = inp4
        sleep(1)
   

    def c_3ff(self):
        self.printRegs()


    def c_3fe(self):
        self.printMemory(8, 32)


    def c_3fd(self):
        self.printMemory(4, 16)


    def c_3fc(self):
        sleep(1)


    def c_3fb(self):
        print("test")


    def c_3fa(self):
        self.inputReg()


    def c_3f1(self):
        self.inputRead()


    def c_3f0(self):
        self.outputAcc()

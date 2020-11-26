import sys
from intel4004_emu import translator
from intel4004_emu import executor
from intel4004_emu import consolex


class EnhancedExecutor(executor.Executor, consolex.Consolex):
    
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
        

    def c_3ff(self):
        self.printRegs()


    def c_3fe(self):
        self.printMemory(8, 32)


    def c_3fd(self):
        self.printMemory(4, 16)


def loadSource(src_file):
    f = open(src_file)
    lines = f.readlines()
    f.close()
    return lines


def fetchState(cpu):
    for i in range(2, len(sys.argv)):
        cpu.regs[i - 2] = int(sys.argv[i])


def run_src(src_file):
    print("="*39)
    print("File: " + src_file)
    print("="*39)
    try:
        src = loadSource(src_file)
        prg = translator.translate(src)
        cpu = EnhancedExecutor()
        fetchState(cpu)
        cpu.run(prg)
    except Exception as e:
        sys.stderr.write("Error: %s\n" % e)
    print()
    print()


run_src("examples4004/test.asm")
run_src("examples4004/simple.asm")
run_src("examples4004/hellow.asm")
run_src("examples4004/toupper.asm")
run_src("examples4004/strrev.asm")


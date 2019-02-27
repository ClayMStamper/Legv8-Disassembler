import sys
import os
import fileinput

global opcodeStr
global arg1
global arg2
global arg3
global arg1Str
global arg2Str
global arg3Str
global mem
global binMem
global opcode

arg1 = [] # <type 'list'>: [0, 0, 0, 0, 0, 1, 1, 10, 10, 0, 3, 4, 152, 4, 10, 1, 0, 112, 0]
arg2 = [] # <type 'list'>: [0, 1, 1, 0, 1, 0, 10, 3, 4, 5, 0, 5, 0, 5, 6, 1, 1, 0, 0]
arg3 = [] # <type 'list'>: [0, 10, 264, 0, 264, 48, 2, 172, 216, 260, 8, 6, 0, 6, 172, -1, 264, 0, 0]
arg1Str = [] # <type 'list'>: ['', '\tR1', '\tR1', '', '\tR1', '\tR1', '\tR10', '\tR3', '\tR4', .....]
arg2Str = [] # <type 'list'>: ['', ', R0', ', 264', '', ', 264', ', #48', ', R1', ', 172', ', 216', ...]'
arg3Str = [] # <type 'list'>: ['', ', #10', '(R0)', '', '(R0)', '', ', #2', '(R10)', '(R10)', '(R0)',...]
mem = [] # <type 'list'>: [-1, -2, -3, 1, 2, 3, 0, 0, 5, -5, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]
binMem = [] # <type 'list'>: ['11111111111111111111111111111111', '11111111111111111111111111111110', ...] opcode = []
opcode = []
opcodeStr = []
instructions = []
instrSpaced = []

#masks
rnMask = 0x3e0  # 1st argument ARM Rn
rmMask = 0x1F0000  # second argument ARM Rm
rdMask = 0x1F  # destination ARM Rd
imMask = 0x3FFC00  # ARM I immediate
shmtMask = 0xFC00  # ARM shamt
addrMask = 0x1FF000  # ARM address for id and st
addr2Mask = 0xFFFFE0  # addr for CB format
imsftMask = 0x600000  # shift for IM formatw
imdataMask = 0x1FFFE0  # data for IM type

#input/output file paths
input = "input"
output = "output"

class Disassembler:

    #def_init_(self):
    def run(self):
        setup()
        disassemble()

def setup():
    # get file names
    for i in range(len(sys.argv)):
        if (sys.argv[i] == '-i' and i < (len(sys.argv) - 1)):
            input = sys.argv[i + 1]
        elif (sys.argv[i] == '-o' and i < (len(sys.argv) - 1)):
            output = sys.argv[i + 1]

    # open file for reading
    with open(input, 'r') as fin:
        for line in fin:
            instructions.append(line)

def disassemble():
    i = -1
    for instr in instructions:
        i += 1
        if (str(bin(1112))[2:] in instr):
            opcodeStr.append("ADD")
            arg1.append((int(instr, base=2) & rnMask) >> 5)
            arg2.append((int(instr, base=2) & rnMask) >> 16)
            arg3.append((int(instr, base=2) & rnMask) >> 0)
            arg1Str.append("\tR" + str(arg3[i]))
            arg2Str.append(", R" + str(arg1[i]))
            arg3Str.append(", R" + str(arg2[i]))


def unsingedToTwos(bitString):

    firstOne = False
    newBitString = ''

    for bit in bitString:

        if not firstOne: #don't flip yet
            newBitString += bit
            if bit == '1':
                firstOne = True
        elif firstOne: #flip the bit
            if bit == '0':
                newBitString += '1'
            elif bit == '1':
                newBitString += '0'
       # print "bit string now = " + newBitString

    return newBitString

def bitStringToArm (bits):
    mem.append(bits)

if __name__=="__main__":

    dis = Disassembler()
    dis.run()

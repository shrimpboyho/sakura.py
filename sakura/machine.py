# The main virtual machine object

class Machine(object):

    def __init__(self, program):
        # The program--a tuple of tuples which represent instructions.
        self.program = program

        # Registers
        self.a = self.b = self.t = None

        # Whether to branch
        self.flag = False

        # Code pointer
        self.pc = 0
    
        # Set up the table output
        print("\nPC\t%A\t%B\t%T\tFLAG\tInstruction:\n")
        
    def execute(self):
        while self.pc is not None:
            i = self.program[self.pc]
            print str(self.pc) + "\t" + str(self.a) + "\t" + str(self.b) + "\t" + str(self.t) + "\t" + str(self.flag) + "\t" , i
            instr, rest = i[0], i[1:]
            self.pc += 1 # Don't forget to increment the counter
            getattr(self, 'i_'+instr)(*rest)

    def i_copy(self, a, b):
        """Duplicates register b in register a"""
        setattr(self, a, getattr(self, b))

    def i_set(self, a, b):
        """Sets register a to the value b"""
        setattr(self, a, b)

    def i_exec(self, reg, op, *args):
        """Calls op and stores the result in reg."""
        setattr(self, reg, getattr(self, 'o_'+op)(*args))

    def i_test(self, op, *rest):
        if getattr(self, 'o_'+op)(*rest):
            self.flag = True
        else:
            self.flag = False

    def i_branch(self, line):
        """Jump to line if flag is set"""
        if self.flag: self.pc = line

    def i_jump(self, line):
        """Jump to line"""
        self.pc = line

    def o_zero(self, reg):
        """Is reg zero?"""
        return getattr(self, reg) == 0

    def o_lt(self, a, b):
        return getattr(self, a) < getattr(self, b)

    def o_sub(self, a, b):
        """reg a - reg b"""
        return getattr(self, a) - getattr(self, b)
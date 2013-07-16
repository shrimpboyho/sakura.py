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

    def execute(self):
        while self.pc is not None:
            i = self.program[self.pc]
            print self.pc, self.a, self.b, self.t, self.flag, i
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

m = Machine((
    # If b is zero, then we are done.
    ('test', 'zero', 'b'),      # if b == 0
    ('branch', None),           # We're done
    ('copy', 't', 'a'),         # t <- a

    # If a < b, then we swap out b and a.
    ('test', 'lt', 't', 'b'),   # t < b?
    ('branch', 7),

    # Subtract out b from a.              
    ('exec', 't', 'sub', 't', 'b'), # t <- t-b
    ('jump', 3),

    ('copy', 'a', 'b'),         # a <- b
    ('copy', 'b', 't'),         # b <- t
    ('jump', 0),
    ))
m.a = 56
m.b = 12
m.execute()
print m.a

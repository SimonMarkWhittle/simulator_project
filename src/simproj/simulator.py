

class Simulator:

    def __init__(self, outputter, numberstream, rearranger):
        self.stepnum = 0
        self.outputter = outputter
        self.numberstream = numberstream
        self.rearranger = rearranger

    def step(self):

        stream = self.numberstream.get_numbers(5)

        rearranged = self.rearranger.rearrange(stream)

        self.outputter.log_outputs(self.stepnum, rearranged)
        self.stepnum += 1

    def run(self, numsteps):

        for _ in range(numsteps):
            self.step()

        self.outputter.write_outputs()

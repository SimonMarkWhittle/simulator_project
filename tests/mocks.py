
class MockOutputter():

    def __init__(self, _):
        self.output_rows = 0
        self.output_volume = 0

    def write_outputs(self):
        pass

    def log_outputs(self, _, outputs):

        self.output_rows += 1
        self.output_volume += 1 + len(outputs)

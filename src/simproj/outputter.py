import datetime as dt
from os.path import join as pjoin

import pandas as pd

class Outputter:

    MAX_OUTPUT_LEN = 100

    def __init__(self, out_dir):

        output_name = f"run_{dt.datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        self.out_path = pjoin(out_dir, output_name)

        self._clear_outputs()

    def _clear_outputs(self):
        self.outputs = [(
            "step", "out1", "out2", "out3", "out4", "out5"
        )]

    def write_outputs(self):

        out_df = pd.DataFrame(
            columns=self.outputs[0],
            data=self.outputs[1:]
        )

        out_df.to_csv(self.out_path, mode='a', index=False)

        self._clear_outputs()

    def log_outputs(self, stepnum, outputs):

        self.outputs.append(
            (stepnum, *outputs)
        )

        if len(self.outputs) > Outputter.MAX_OUTPUT_LEN:
            self.write_outputs()


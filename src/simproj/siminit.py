import os

from simproj.simulator import Simulator


class SimConfigurator():

    def __init__(self, config):
        self.config = config

        if not isinstance(self.config, dict):
            raise TypeError("config needs to be a valid dictionary!")

    def configure_sim(self):

        match self.config:
            case {
                "run": dict(),
                "scenario": dict(),
                "sim": {"numberstream": dict(), "rearrangement": dict()}
            }:
                pass
            case _:
                raise ValueError("Invalid configuration passed to 'SimConfigurator'!")

        outputter = self._configure_outputter()
        numberstream = self._configure_numberstream()
        rearranger = self._configure_rearranger()

        return Simulator(
            outputter,
            numberstream,
            rearranger
        )

    def _configure_outputter(self):
        run = self.config["run"]

        out_path = run["out_dir"]
        create_out_dir = run.get("out_dir", False)

        if not os.path.isdir(out_path) and create_out_dir:
            os.mkdir(out_path)
        elif not os.path.isdir(out_path):
            raise ValueError("Nonexistent out_dir passed to 'SimConfigurator'!")

        from simproj.outputter import Outputter
        return Outputter(out_path)

    def _configure_numberstream(self):
        numstream = self.config["sim"]["numberstream"]

        match numstream:
            case {"model": "Base", "minrange": int(), "maxrange": int()}:
                from simproj.models.numberstream.base import BasicNumberstream
                numberstream = BasicNumberstream(
                    numstream["minrange"],
                    numstream["maxrange"]
                )
            case {"model": "Base"}:
                from simproj.models.numberstream.base import BasicNumberstream
                numberstream = BasicNumberstream()
            case {"model": "Numberstreamator", "minrange": int(), "maxrange": int()}:
                from simproj.models.numberstream.numberstreamator_adaptor import NumberstreamatorAdaptor
                numberstream = NumberstreamatorAdaptor(
                    numstream["minrange"],
                    numstream["maxrange"]
                )
            case {"model": "Numberstreamator"}:
                from simproj.models.numberstream.numberstreamator_adaptor import NumberstreamatorAdaptor
                numberstream = NumberstreamatorAdaptor()
            case _:
                raise ValueError("Invalid numberstream configuration passed to 'SimConfigurator'!")

        return numberstream

    def _configure_rearranger(self):
        rearrange = self.config["sim"]["rearrangement"]

        match rearrange:
            case {"model": "Base"}:
                from simproj.models.rearrangement.base import BasicRearrangement
                rearranger = BasicRearrangement()
            case _:
                raise ValueError("Invalid rearrangement configuration passed to 'SimConfigurator'")

        return rearranger

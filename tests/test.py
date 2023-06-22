
import os
from os.path import join as pjoin

import pytest as pt
import tomli as tm

from simproj.models.numberstream.base import BasicNumberstream
from simproj.models.numberstream.numberstreamator_adaptor import NumberstreamatorAdaptor
from simproj.models.rearrangement.base import BasicRearrangement
from simproj.outputter import Outputter
from simproj.siminit import SimConfigurator
from simproj.simulator import Simulator

from tests.mocks import MockOutputter

OUTDIR = pjoin(os.path.dirname(__file__), 'outputs')
CONFIGDIR = pjoin(os.path.dirname(__file__), 'config_files')


def test_simulator_outputs_volume():

    mockout = MockOutputter(None)

    sim = Simulator(
        mockout,
        BasicNumberstream(),
        BasicRearrangement()
    )

    sim.run(100)

    assert mockout.output_rows == 100
    assert mockout.output_volume == 600


def test_base_numberstream():
    import random
    random.seed = 8675309
    nbst = BasicNumberstream(minrange=10, maxrange=20)

    res = nbst.get_numbers(1000)
    assert len(res) == 1000
    assert all([r <= 20 for r in res])
    assert all([r >= 10 for r in res])


def test_noout_configurator():

    filepath = pjoin(CONFIGDIR, 'nooutconfig.toml')

    with open(filepath, 'rb') as config_file:
        config = tm.load(config_file)

    configurator = SimConfigurator(config)

    os.rmdir(OUTDIR)
    with pt.raises(ValueError) as e_info:
        configurator.configure_sim()


def test_invalid_configurator():

    with pt.raises(TypeError) as e_info:
        SimConfigurator(None)

    with pt.raises(ValueError) as e_info:
        configurator = SimConfigurator({})
        configurator.configure_sim()


def test_basic_configurator():
    filepath = pjoin(CONFIGDIR, 'basicconfig.toml')

    with open(filepath, 'rb') as config_file:
        config = tm.load(config_file)

    configurator = SimConfigurator(config)

    sim = configurator.configure_sim()

    assert isinstance(sim.numberstream, BasicNumberstream)
    assert isinstance(sim.rearranger, BasicRearrangement)
    assert isinstance(sim.outputter, Outputter)


def test_module_configurator():
    filepath = pjoin(CONFIGDIR, 'modelconfig.toml')

    with open(filepath, 'rb') as config_file:
        config = tm.load(config_file)

    configurator = SimConfigurator(config)

    try:
        sim = configurator.configure_sim()
    except ImportError:
        return

    assert isinstance(sim.numberstream, NumberstreamatorAdaptor)
    assert isinstance(sim.rearranger, BasicRearrangement)
    assert isinstance(sim.outputter, Outputter)


def test_minimal_configurator():
    filepath = pjoin(CONFIGDIR, 'minimalconfig.toml')

    with open(filepath, 'rb') as config_file:
        config = tm.load(config_file)

    configurator = SimConfigurator(config)

    try:
        sim = configurator.configure_sim()
    except ImportError:
        return

    assert isinstance(sim.numberstream, BasicNumberstream)
    assert isinstance(sim.rearranger, BasicRearrangement)
    assert isinstance(sim.outputter, Outputter)


if __name__ == '__main__':

    test_simulator_outputs_volume()
    test_base_numberstream()
    test_invalid_configurator()

    test_noout_configurator()
    test_basic_configurator()
    test_module_configurator()
    test_minimal_configurator()

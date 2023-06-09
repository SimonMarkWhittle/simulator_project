
from simproj.simulator import Simulator
from simproj.models.numberstream.base import BasicNumberstream
from simproj.models.rearrangement.base import BasicRearrangement

from tests.mocks import MockOutputter


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
    assert all([ r <= 20 for r in res ])
    assert all([ r >= 10 for r in res ])


if __name__ == '__main__':
    test_simulator_outputs_volume()

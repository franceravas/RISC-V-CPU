import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, Timer
import random


async def reset(dut):
    await RisingEdge(dut.clk)
    dut.reset_n.value = 0
    await RisingEdge(dut.clk)
    dut.reset_n.value = 1
    await Timer(1, units="ns")

    dut._log.info("reset done!")

    assert dut.data_out.value == 0


@cocotb.test()
async def initial_read_test(dut):
    cocotb.start_soon(Clock(dut.clk, 1, units="ns").start())

    await RisingEdge(dut.clk)

    # call reset coroutine
    await reset(dut)

    N_TESTS = 1000
    for _ in range(N_TESTS):
        test_value = random.randint(0, 1)
        dut.data_in.value = test_value

        await RisingEdge(dut.clk)

        assert int(dut.data_out.value) == test_value
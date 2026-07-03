import cocotb
from cocotb.clock import Clock
from cocotb.triggers import Timer, RisingEdge

@cocotb.test()
async def test_dummy(dut):
    # Start clock
    cocotb.start_soon(Clock(dut.clk, 10, units='ns').start())
    
    # Let it run for a bit
    await Timer(100, units='ns')
    
    # Check counter incremented
    assert dut.count.value > 0, "Counter didn't increment!"
    dut._log.info(f"Counter value: {dut.count.value}")
    dut._log.info("Test passed! ✅")
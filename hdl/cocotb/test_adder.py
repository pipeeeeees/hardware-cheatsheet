import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def test_adder(dut):
    """Test the adder module."""

    # Initialize inputs
    dut.a.setimmediatevalue(0)
    dut.b.setimmediatevalue(0)

    for i in range(10):
        # Apply test inputs
        dut.a <= i
        dut.b <= i * 2
        await Timer(1, units="ns")  # Wait for a clock cycle

        # Check the output
        expected_sum = i + (i * 2)
        assert dut.sum.value == expected_sum, \
            f"Test failed for a={i}, b={i*2}: Expected {expected_sum}, got {dut.sum.value}"

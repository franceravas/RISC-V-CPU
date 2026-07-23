# Simulator
SIM ?= verilator

# HDL language
TOPLEVEL_LANG ?= verilog

# Extra Verilator arguments
EXTRA_ARGS += --trace --trace-structs

# Source file
VERILOG_SOURCES += $(PWD)/../../src/memory.sv

# Top-level module name
TOPLEVEL = memory

# Cocotb test module
COCOTB_TEST_MODULES = test_memory

# Include Cocotb make rules
include $(shell cocotb-config --makefiles)/Makefile.sim
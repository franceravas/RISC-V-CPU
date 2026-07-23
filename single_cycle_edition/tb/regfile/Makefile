# Simulator
SIM ?= verilator

# HDL language
TOPLEVEL_LANG ?= verilog

# Extra Verilator options
EXTRA_ARGS += --trace --trace-structs
# WAVES = 1

# SystemVerilog source file
VERILOG_SOURCES += $(PWD)/../../src/regfile.sv

# Top-level module inside regfile.sv
TOPLEVEL = regfile

# Python testbench (test_regfile.py)
MODULE = test_regfile

# Cocotb build system
include $(shell cocotb-config --makefiles)/Makefile.sim
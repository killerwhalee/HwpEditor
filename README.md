# Editor.hwp

EDITOR.HWP by CHAEMIN LIM && JUNHYUK YU

## Introduction

Editor.hwp is API for hwp file by using hml parsing.
Since nothing is inside this repository, there's nothing to write on readme.md.
As I don't like empty readme, I just add sample readme specification here. Edit below when it's ready.

ps) Below readme was from Chaemin Lim's MIPS Pipelining project assignment

### 1. util.h

We have setup the basic CPU_State that is sufficient to implement the project.
However, you may decide to add more variables, and modify/remove any misleading variables.

### 2. run.h

You may add any additional functions that will be called by your implementation of `process_instruction()`.
In fact, we encourage you to split your implementation of `process_instruction()` into many other helping functions.
You may decide to have functions for each stages of the pipeline.
Function(s) to handle flushes (adding bubbles into the pipeline), etc.

### 3. run.c

**Implement** the following function:

    void process_instruction()

The `process_instruction()` function is used by the `cycle()` function to simulate a `cycle` of the pipelined simulator.
Each `cycle()` the pipeline will advance to the next instruction (if there are no stalls/hazards, etc.).
Your internal register, memory, and pipeline register state should be updated according to the instruction
that is being executed at each stage.

## Details of Register Contents

This is details of Fields newly introduced on `util.h`.

### 1. Signal Set

- `BR_SIGNAL` is signal which indicates that **branch operation** occurred.
- `STALL_SIGNAL` is signal which indicates that pipeline **IF, ID** stalls by lw operation branching.
- `FORWARD_SIGNAL` is signal which indicates that forwarding in **EX_MEM** level occurred.
- `PIPE_FLUSH_SIGNAL` is signal which indicates that last instruction is at IF stage. Which means that PC goes over .text region
- `JUMP_SIGNAL` is signal which indicates that jump operation is observed. JUMP_SIGNAL is transferred by pipeline registers.
-

### 2. IF_ID_latch

- `IF_ID_INST` saves current **program counter**.
- `IF_ID_NPC` saves **next PC** address. When this value goes over .text address region, it turns on `PIPE_FLUSH_SIGNAL`.

### 3. ID_EX_latch

In this stage, instruction information is saved. To accomplish this, instruction address from IF_ID_INST is interpreted.  
Regardless of instruction type, every data is interpreted since only valid data will be selected and used at EX stage.

- `ID_EX_NPC` saves `NPC` value from **IF_ID_latch**.
- `ID_EX_OPCODE` saves **Operation Code** value.
- `ID_EX_RS` saves **rs** register number.
- `ID_EX_RT` saves **rt** register number.
- `ID_EX_REG1` saves data saved in **rs** register number.
- `ID_EX_REG2` saves data saved in **rt** register number.
- `ID_EX_SHAMT` saves **Shift Amount** value.
- `ID_EX_IMM` saves **Immediate** value.
- `ID_EX_FUNCT` saves **Function Code** value.
- `ID_EX_TARGET` saves **Jump Target** value
- `ID_EX_DEST` saves **Destination Register** value. Two cases are possible.
  - Value is **rd** register number when R-type.
  - Value is **rt** register number when I-type or J-type. Since J-type does not have destination register, but it just saves some data in `ID_EX_DEST`.
- `ID_EX_TYPE_FLAG` saves which type the instruction is.
  - Value is **zero** when instruction is **R-type** except **jr** instruction.
  - Value is **one** when instruction is **I-type**.
  - Value is **two** when instruction is **J-type** or it's **jr** instruction.

### 4. EX_MEM_latch

Regardless of instruction type, every data is operated(e.g. branch target). But only valid and appropriate data will be selected.

- `EX_MEM_NPC` saves `NPC` value from **ID_EX_latch**.
- `EX_MEM_ALU_OUT` saves output value from **ALU**.
- `EX_MEM_BR_TARGET` saves target branch address calculated from immediate value in branch operation.
- `EX_MEM_BR_TAKE` saves whether branch operation is **TRUE**. This data is transferred to turn on the `BR_SIGNAL`.
- `EX_MEM_TAKE` saves read/write option for MEM stage.
  - Value is **zero** for default.
  - Value is **one** for lw operation.
  - Value is **two** for sw operation.
- `EX_MEM_REGLOCK` saves **Lock State** of WB. If `REGLOCK` is true, WB would not write data to register.
- `EX_MEM_DEST` saves `DEST` value from **ID_EX_latch**.
- `EX_MEM_TYPE_FLAG` saves `TYPE_FLAG` value from **ID_EX_latch**.
- `EX_MEM_JUMP_SIGNAL` saves when instruction is **jr**.

### 5. MEM_WB_latch

- `MEM_WB_NPC` saves `NPC` value from **EX_MEM_latch**.
- `MEM_WB_ALU_OUT` saves `ALU_OUT` value from **EX_MEM_latch**.
- `MEM_WB_MEM_OUT` saves data from **Memory** refer to `ALU_OUT`.
- `MEM_WB_TAKE` saves `TYPE_FLAG` value from **EX_MEM_latch**.
- `MEM_WB_REGLOCK` saves `REGLOCK` value from **EX_MEM_latch**.
- `MEM_WB_DEST` saves `DEST` value from **EX_MEM_latch**.
- `MEM_WB_TYPE_FLAG` saves `TYPE_FLAG` value from **EX_MEM_latch**.
- `MEM_WB_JUMP_SIGNAL` saves `JUMP_SIGNAL` value from **EX_MEM_latch**.

### 6. Forwarding

There exists **four** fields for forwarding.

- `EX_MEM_FORWARD_REG` saves **rd** register number at `EX_MEM` stage.
- `EX_MEM_FORWARD_VALUE` saves data saved in **rd** register number at `EX_MEM` stage.
- `MEM_WB_FORWARD_REG` saves **rd** register number at `MEM_WB` stage.
- `MEM_WB_FORWARD_VALUE` saves data saved in **rd** register number at `MEM_WB` stage.

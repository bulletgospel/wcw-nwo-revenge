# Wrestler Definition Pointer Investigation

Research Status: Active

ROM Version: WCW/nWo Revenge NTSC-U (NW2E)

==================================================
PURPOSE
==================================================

Determine what Revenge Stable Definitions mean when they store WrestlerPointers.

Current unknown:

80039390 = ?

==================================================
CONFIRMED DISCOVERY
==================================================

Stable Definitions do NOT store Wrestler ID2 values.

Stable Definitions store 32-bit WrestlerPointers.

Evidence from VPW Studio source:

GameSpecific\Revenge\StableDefinition.cs contains:

- WrestlerPointerStart
- WrestlerPointers[]

Editors\Revenge\StableDefs_Revenge.cs displays:

- WrestlerPointerStart
- WrestlerPointers[]

==================================================
CURRENT THEORY
==================================================

Stable

↓

WrestlerPointerStart

↓

WrestlerPointers[]

↓

WrestlerDefinition

↓

Wrestler data

==================================================
KNOWN EXAMPLE
==================================================

Stable 0 first pointer:

80039390

Hollywood Hogan visible pointers from Wrestler Editor:

Name Pointer: 80039368

Height Pointer: 8003937C

Weight Pointer: 80039384

Observation:

80039390 is near Hogan's visible pointer range, but it is not the same as Name, Height, or Weight Pointer.

Possible meaning:

80039390 may point into or near Hogan's wrestler definition block.

==================================================
NEXT TASK
==================================================

Inspect:

GameSpecific\Revenge\WrestlerDefinition.cs

Goal:

Determine the field order, field sizes, and whether any field explains the Stable WrestlerPointers.

==================================================
STATUS
==================================================

Stable pointer architecture: Partially decoded

Exact WrestlerPointer target: Unknown

==================================================
WRESTLER DEFINITION STRUCTURE CONFIRMED
==================================================

Source:

GameSpecific\Revenge\WrestlerDefinition.cs

Confirmed record size:

26 bytes

Field layout:

2 bytes  - WrestlerID4
1 byte   - WrestlerID2
1 byte   - Unknown1
2 bytes  - Unknown2
2 bytes  - Unknown3
4 bytes  - NamePointer
4 bytes  - HeightPointer
4 bytes  - WeightPointer
1 byte   - Unknown4
1 byte   - ManagerID2
1 byte   - Unknown5
1 byte   - Unknown6
2 bytes  - Terminator

Important discovery:

Stable WrestlerPointers are NOT direct pointers to the parsed WrestlerDefinition record.

Reason:

WrestlerDefinition.cs does not contain a field matching the stable pointer.

Example:

Hollywood Hogan visible pointers:

Name Pointer: 80039368
Height Pointer: 8003937C
Weight Pointer: 80039384

Stable pointer observed:

80039390

Conclusion:

80039390 likely points to a nearby wrestler-related data block, but not to the main WrestlerDefinition record parsed by VPW Studio.

Working theory:

Stable WrestlerPointers may point to:

- wrestler display data
- wrestler menu data
- costume/appearance block
- runtime wrestler object
- another struct adjacent to name/height/weight strings
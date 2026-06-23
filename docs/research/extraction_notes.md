# Revenge Extraction Notes

Finding:

VPW2 extract_baserom.sh cannot be used directly for WCW/nWo Revenge.

Reason:

- VPW2 ROM is 32 MB
- Revenge ROM is 16 MB
- VPW2 filetable/soundtable offsets point beyond the end of the Revenge ROM

Useful VPW2 concept:

- extract boot code from 0x40
- identify graphics microcode
- identify filetable data
- identify filetable index
- extract soundtables

Needed for Revenge:

- Revenge boot code offset/size
- Revenge filetable data offset
- Revenge filetable index offset
- Revenge soundtable offsets
- Revenge linker layout

Next investigation:

Use VPWStudio or AKI docs to locate WCW/nWo Revenge file table structure.

==================================================
UNKNOWN2 / UNKNOWN3 INVESTIGATION
==================================================

10 wrestler sample:

Hollywood Hogan

Unknown2 = 1D22

Unknown3 = 1D36

Sting

Unknown2 = 1D0E

Unknown3 = 1D34

Kevin Nash

Unknown2 = 1D24

Unknown3 = 1D3F

Goldberg

Unknown2 = 1D16

Unknown3 = 1D36

Scott Hall

Unknown2 = 1D25

Unknown3 = 1D36

Diamond Dallas Page

Unknown2 = 1D11

Unknown3 = 1D36

Chris Benoit

Unknown2 = 1D15

Unknown3 = 1D36

Booker T

Unknown2 = 1D17

Unknown3 = 1D36

Rey Mysterio Jr.

Unknown2 = 1D13

Unknown3 = 1D36

Ultimo Dragon

Unknown2 = 1D2C

Unknown3 = 1D36

--------------------------------------------------

OBSERVATIONS

Unknown2

- Appears unique per wrestler.

- No duplicate values found.

Unknown3

- 9 of 10 wrestlers use 1D36.

- Sting uses 1D34.

- Kevin Nash uses 1D3F.

--------------------------------------------------

WORKING THEORY

Unknown2

Possible:

- Wrestler package assignment

- Entrance package assignment

- Voice assignment

Unknown3

Possible:

- Shared animation class

- Skeleton class

- Entrance class

--------------------------------------------------

STATUS

Unknown2

⚠ Partially decoded

Unknown3

⚠ Partially decoded
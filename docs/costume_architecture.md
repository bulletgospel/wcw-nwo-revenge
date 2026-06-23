# Costume Architecture

Research Status: Active

ROM Version: WCW/nWo Revenge NTSC-U (NW2E)

==================================================
PURPOSE
==================================================

Decode how wrestler appearances are constructed.

Determine how visual assets are assembled and how they connect to wrestler definitions.

==================================================
DISCOVERY #1
==================================================

VPW Studio Wrestler Editor does NOT expose costume data.

The Wrestler Editor only contains wrestler definition data.

Current fields:

- Wrestler ID4
- Wrestler ID2
- Unknown 1
- Unknown 2
- Unknown 3
- Name Pointer
- Height Pointer
- Weight Pointer
- Unknown 4
- Manager ID2
- Unknown 5
- Unknown 6

No costume, attire, texture, palette, model, or color fields are present.

Conclusion:

Costume data exists independently from wrestler definitions.

==================================================
DISCOVERY #2
==================================================

Wrestler visuals are built from three regions.

Architecture:

Wrestler

↓

Head

↓

Neck

↓

Face

Each region is composed of three asset types.

Region

↓

Palette

↓

Model

↓

Texture

Overall structure:

Wrestler

↓

Head
├── Palette
├── Model
└── Texture

↓

Neck
├── Palette
├── Model
└── Texture

↓

Face
├── Palette
├── Model
└── Texture

==================================================
DISCOVERY #3
==================================================

Wrestlers are stored sequentially inside the ROM.

Examples:

Lex Luger

0A86 - Head Palette

0A87 - Head Model

0A88 - Head Texture

0A89 - Neck Palette

0A8A - Neck Model

0A8B - Neck Texture

0A8C - Face Palette

0A8D - Face Model

0A8E - Face Texture

--------------------------------------------------

Diamond Dallas Page

0A8F - Head Palette

0A90 - Head Model

0A91 - Head Texture

0A92 - Neck Palette

0A93 - Neck Model

0A94 - Neck Texture

0A95 - Face Palette

0A96 - Face Model

0A97 - Face Texture

--------------------------------------------------

Rick Steiner

0A98 - Head Palette

0A99 - Head Model

0A9A - Head Texture

0A9B - Neck Palette

0A9C - Neck Model

0A9D - Neck Texture

0A9E - Face Palette

0A9F - Face Model

0AA0 - Face Texture

--------------------------------------------------

Roddy Piper

0AA1 - Head Palette

0AA2 - Head Model

0AA3 - Head Texture

0AA4 - Neck Palette

0AA5 - Neck Model

0AA6 - Neck Texture

0AA7 - Face Palette

0AA8 - Face Model

0AA9 - Face Texture

==================================================
DISCOVERY #4
==================================================

Some wrestlers have multiple appearances.

Examples:

Scott Steiner

- New Version

- Old Version

Bret Hart

- Normal

- Sunglasses

Sting

- White Paint

- Red Paint

- Surfer Paint

This suggests the game supports multiple costume variants.

==================================================
DISCOVERY #5
==================================================

Special characters use the same architecture.

Examples:

AKI Man

THQ Man

They also use:

Head

Neck

Face

Palette

Model

Texture

==================================================
WORKING THEORY
==================================================

Wrestler Definition

↓

Visual Asset Group

↓

Head

↓

Neck

↓

Face

↓

Costume Variant

↓

Final Wrestler Appearance

==================================================
OPEN QUESTIONS
==================================================

Where is body geometry stored?

Where are arm textures stored?

Where are leg textures stored?

Where are entrance attires stored?

Where are alternate costumes assigned?

How are costume variants linked to wrestlers?

==================================================
STATUS
==================================================

Head System

✓ Decoded

Neck System

✓ Decoded

Face System

✓ Decoded

Alternate Costumes

⚠ Partially Decoded

Costume Assignment Logic

✗ Unknown

Body Architecture

✗ Unknown

DISCOVERY #6

Searching for:

Body

Arm

Leg

Torso

Chest

Boot

does not produce obvious wrestler visual assets in File Table.

Current evidence suggests wrestler visuals are NOT organized as complete body regions.

Only these regions have been positively identified:

✓ Head

✓ Neck

✓ Face

The remainder of the wrestler body architecture is still unknown.

Possibilities:

1. Body geometry is stored inside a shared model.

2. Body parts are embedded inside another archive.

3. Wrestlers share body assets.

4. Body assets use different naming conventions.
# WCW/nWo Revenge Asset Registry

Last Updated: 2026-06-21

==================================================
SECTION 1 - VPW STUDIO STATUS
==================================================

WORKING

✓ File Table

✓ Wrestlers

✓ Championships

✓ Stables

NOT IMPLEMENTED

✗ Arenas

✗ Menus

✗ Moves

✗ Sound/Music

✗ Weapons

✗ Demo Matches

PARTIALLY IMPLEMENTED

⚠ Match Rulesets

==================================================
SECTION 2 - ARCHITECTURE DISCOVERIES
==================================================

Current wrestler structure appears to be:

Wrestler

├── Params

├── Move Damage

├── Moveset

├── Animations

├── Head Palette

├── Head Model

├── Head Texture

├── Neck Palette

├── Neck Model

├── Neck Texture

├── Face Palette

├── Face Model

└── Face Texture

Notes:

- VPW Studio already understands a large portion of Revenge.

- File Table is currently the most valuable research tool.

==================================================
SECTION 3 - INTRO SEQUENCE
==================================================

Core Intro Assets

0025 - Intro Part 1

0026 - Intro Part 2

0027 - Sting/Hogan Tombstones

0028 - Fire Textures

0029 - Unknown Intro Package

002A - Truck and Light

002B - Backstage Door

002C - Backstage Stairs and White Sting

002D - City Skyline

002E - Red Sting

002F - Heartbeat Line and Dot

0030 - Hogan, Sting, and Eye Lightning

0038 - Intro Textures/Palettes

003A - Sting Textures/Palettes

Observation:

The intro is modular and assembled from multiple AkiArchive packages rather than a single movie.

==================================================
SECTION 4 - MUSIC
==================================================

0210 - Main Menu Music

0223 - Intro Music

==================================================
SECTION 5 - WEAPONS
==================================================

0402 - Black Baseball Bat

0405 - Barbed Wire Baseball Bat

0408 - Chair 1

040B - Chair 2

040E - Chair Side

0410 - Table Front

0412 - Table Back

0414 - Table Side

0416 - Belt Model

==================================================
SECTION 6 - HOLLYWOOD HOGAN
==================================================

Character Data

017F - Params

0180 - Move Damage

0181 - Moveset

Animations

1D1B - Hogan Guitar Taunt

1D7C - Hogan 3 Pose

==================================================
SECTION 7 - STING
==================================================

Character Data

01F7 - Params

01F8 - Move Damage

01F9 - Moveset

White Sting

0A62 - Head Palette

0A63 - Head Model

0A64 - Head Texture

0A65 - Neck Palette

0A66 - Neck Model

0A67 - Neck Texture

0A68 - Face Palette

0A69 - Face Model

0A6A - Face Texture

Red Sting

0A6B - Head Palette

0A6C - Head Model

0A6D - Head Texture

0A6E - Neck Palette

0A6F - Neck Model

0A70 - Neck Texture

0A71 - Face Palette

0A72 - Face Model

0A73 - Face Texture

Surfer Sting

0A74 - Head Palette

0A75 - Head Model

0A76 - Head Texture

0A77 - Neck Palette

0A78 - Neck Model

0A79 - Neck Texture

0A7A - Face Palette

0A7B - Face Model

0A7C - Face Texture

==================================================
SECTION 8 - HIDDEN / BONUS CHARACTERS
==================================================

34 - AKI Man

35 - Shogun

36 - Executioner

37 - Dr. Frank

38 - Jekel

39 - Maya Inca Boy

3A - Hawk Hana

3B - Kim Chee

3C - Dake Ken

3D - Brickowski

3E - Han Zo Mon

3F - Black Ninja

2A - Wrath (GameShark only)

==================================================
SECTION 9 - BLOCKERS
==================================================

Stable Definitions

- View Wrestler button is not implemented.

- Stable member pointers cannot currently be resolved to wrestler names.

Future investigation required.

VPW Studio

- Arenas dialog not implemented.

- Menus dialog not implemented.

- Moves dialog not implemented.

- Sound/Music dialog not implemented.

- Weapons dialog not implemented.

- Demo Matches dialog not implemented.
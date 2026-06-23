# Music Architecture

Research Status: Active

ROM Version: WCW/nWo Revenge NTSC-U (NW2E)

==================================================
PURPOSE
=======

Decode how music is organized, stored, and assigned throughout the game.

Determine how menu music, intro music, arena music, wrestler themes, and match music are connected.

==================================================
KNOWN MUSIC FILES
=================

==================================================
KNOWN MUSIC FILES
=================

0210 - Main Menu

0211 - Costume Change

0212 - Options Menu

0213 - Results

0214 - Entrance Music 1

0215 - Entrance Music 2

0216 - Wrestler Unlocked

0217 - Championship Loss

0218 - Monday Nitro

0219 - Souled Out

021A - SuperBrawl

021B - Bash at the Beach

021C - Halloween Havoc

021D - Starrcade

021E - Championship BGM 1

021F - Championship BGM 2

0220 - New Champion

0221 - Championship - Final Match

0222 - "Made it to Championship"

0223 - Intro

0224 - Credits


==================================================
NEW OBSERVATIONS
================

Arena themes are stored as independent music files.

Each PPV has its own dedicated music.

Music appears to be grouped into categories:

* Menus
* Arena themes
* Championship mode
* Entrance themes
* Intro
* Credits

No evidence yet that wrestler themes exist as standalone files.

Entrance music may be shared rather than unique per wrestler.



==================================================
ARCHITECTURE
============

Music

↓

Menu

↓

Arena

↓

Wrestler

↓

Match

↓

Intro

==================================================
CONFIRMED DISCOVERIES
=====================

✓ Main Menu Music identified

✓ Intro Music identified

Current known files:

0210 - Main Menu Music

0223 - Intro Music

==================================================
OPEN QUESTIONS
==============

Where is wrestler entrance music stored?

Where is arena music stored?

How are wrestler themes assigned?

How is match music assigned?

How is music loaded into memory?

==================================================
WORKING THEORIES
================

==================================================
CONFIRMED DISCOVERIES
=====================

✓ Main Menu Music identified

✓ Intro Music identified

✓ Arena themes identified

✓ Championship mode music identified

✓ Entrance music identified

Important discovery:

WCW/nWo Revenge does NOT have unique wrestler entrance themes.

All wrestlers use shared generic entrance music.

0214 - Entrance Music 1

0215 - Entrance Music 2

are generic entrance tracks rather than wrestler-specific themes.

==================================================
MUSIC CATEGORIES
================

Menu

0210 - Main Menu

0211 - Costume Change

0212 - Options Menu

0213 - Results

Entrance

0214 - Entrance Music 1

0215 - Entrance Music 2

Championship Mode

0216 - Wrestler Unlocked

0217 - Championship Loss

021E - Championship BGM 1

021F - Championship BGM 2

0220 - New Champion

0221 - Championship - Final Match

0222 - "Made it to Championship"

Arena Themes

0218 - Monday Nitro

0219 - Souled Out

021A - SuperBrawl

021B - Bash at the Beach

021C - Halloween Havoc

021D - Starrcade

Miscellaneous

0223 - Intro

0224 - Credits


==================================================
INVESTIGATION TARGETS
=====================

Need to locate:

* Arena music assignments

* Wrestler theme assignments

* Match music assignments

* Music loading behavior

==================================================
STATUS
======

Main Menu Music

✓ Decoded

Intro Music

✓ Decoded

Wrestler Themes

✗ Unknown

Arena Music

✗ Unknown

Match Music

✗ Unknown

Music Assignment Logic

✗ Unknown

Music Loading Behavior

✗ Unknown


STATUS

Music File Bank

✓ Decoded

Unique Wrestler Themes

✓ Confirmed absent

Music Assignment Logic

⚠ Partially decoded

Overall Music Architecture

90%
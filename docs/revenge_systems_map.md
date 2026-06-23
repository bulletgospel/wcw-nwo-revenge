# WCW/nWo Revenge Systems Map

Version: v1.1 (6/21/26)

Research Status: Active

ROM Version: WCW/nWo Revenge NTSC-U (NW2E)

---

# Purpose

This document is the high-level architecture map for WCW/nWo Revenge.

It is NOT an asset registry.

It is NOT a wrestler database.

It is NOT a discovery notebook.

This document exists to answer one question:

**"What systems exist in the game and how do they connect to one another?"**

Detailed discoveries belong inside their dedicated documents.

---

# Status Legend

✓ = Mostly documented

⚠ = Partially documented

✗ = Not yet investigated

? = Unknown

---

# Game Architecture

```text
Game
│
├── Wrestlers
├── Managers
├── Stables
├── Championships
├── Arenas
├── Intro Sequence
├── Music
├── Menus
├── Weapons
├── Costumes
├── Movesets
├── AI Logic
└── Hidden Content
```

---

# System Progress

| System         | Status | Documentation                      |
| -------------- | ------ | ---------------------------------- |
| Wrestlers      | ✓      | wrestler_cross_reference.md        |
| Managers       | ⚠      | manager_cross_reference.md         |
| Stables        | ✗      | stable_cross_reference.md (future) |
| Championships  | ✓      | championship_architecture.md       |
| Arenas         | ✓      | revenge_asset_registry.md          |
| Intro Sequence | ✓      | revenge_asset_registry.md          |
| Music          | ⚠      | music_architecture.md (future)     |
| Menus          | ⚠      | revenge_asset_registry.md          |
| Weapons        | ⚠      | revenge_asset_registry.md          |
| Costumes       | ✗      | costume_architecture.md (future)   |
| Movesets       | ⚠      | future documentation               |
| AI Logic       | ✗      | future documentation               |
| Hidden Content | ⚠      | wrestler_cross_reference.md        |

---

# Wrestler System

Current discoveries:

* Params
* Move Damage
* Movesets
* Animations
* Head assets
* Neck assets
* Face assets
* Manager IDs

Architecture:

```text
Wrestler
│
├── Params
├── Move Damage
├── Moveset
├── Animations
├── Manager ID
└── Costume
```

Primary document:

wrestler_cross_reference.md

---

# Championship System

Current discoveries:

* 5 championships
* Championship rosters
* Champion IDs
* Defending champion IDs
* Flags
* Belt graphics
* Intro graphics
* Victory graphics
* Defense graphics

Architecture:

```text
Championship
│
├── Definitions
├── Intro Graphics
├── Belt Graphics
├── Menu Graphics
└── Championship Mode Graphics
```

Primary document:

championship_architecture.md

---

# Arena System

Documented arenas:

* Monday Nitro
* Souled Out
* Halloween Havoc
* Bash at the Beach
* Starrcade
* SuperBrawl

Architecture:

```text
Arena
│
├── Stage Package
├── Arena Select Graphic
├── Arena Music
└── Arena Components
    ├── Ring Assets
    ├── Entrance Assets
    ├── Event Decorations
    └── Lighting Assets
```

Primary document:

revenge_asset_registry.md

---

# Intro System

Current discoveries:

* Part 1
* Part 2
* Tombstones
* Fire
* Truck
* Backstage
* Skyline
* Sting assets
* Eye lightning

Observation:

The intro is assembled from multiple AkiArchive packages.

Architecture:

```text
Intro Sequence
│
├── Part 1
├── Part 2
├── Tombstones
├── Fire
├── Truck
├── Backstage
├── Skyline
├── Sting Assets
└── Eye Lightning
```

Primary document:

revenge_asset_registry.md

---

# Music System

Current discoveries:

* Main Menu Music
* Intro Music
* Arena Music

Unknown:

* Match music assignments
* Character music assignments
* Loading behavior

Primary document:

music_architecture.md (future)

---

# Manager System

Known manager IDs:

40 = Hollywood Hogan

42 = Barbarian / Meng

43 = Curt Hennig

44 = Scott Hall

47 = Brian Adams / Scott Norton / Scott Steiner

48 = Eric Bischoff

49 = Diamond Dallas Page

Unknown:

* Stable relationships
* Entrance relationships
* AI relationships
* Cutscene relationships

Primary document:

manager_cross_reference.md

---

# Research Priorities

1. Complete Manager Architecture

2. Create Stable Cross Reference

3. Decode Costume Architecture

4. Decode Music Assignments

5. Decode Moveset Architecture

6. Decode AI Logic

7. Build Final System Diagram

---

# Current Project Status

Documentation Progress:

55%

Architecture Understanding:

75%

Current Phase:

Documentation & Decoding Phase

Next Task:

Manager Architecture


# Stable Architecture (Confirmed)

Stable

│

├── Header Graphic

├── Wrestler Count

├── WrestlerPointerStart

└── WrestlerPointers[]

Observation:

Stable definitions do NOT store Wrestler ID2 values.

Stable definitions store WrestlerPointers.

Stable editor code loads WrestlerPointers from WrestlerPointerStart.

Relationship:

Stable

↓

WrestlerPointerStart

↓

WrestlerPointers[]

↓

Unknown Wrestler Structure
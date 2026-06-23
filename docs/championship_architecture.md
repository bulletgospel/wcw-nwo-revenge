# Championship Architecture

Research Status: Active

ROM Version: WCW/nWo Revenge NTSC-U (NW2E)

==================================================
PURPOSE
=======

This document exists to decode the Championship system architecture.

It documents:

* Championship definitions
* Championship rosters
* Champion IDs
* Defending champion IDs
* Graphics
* Unknown flags
* Relationships between systems

==================================================
CHAMPIONSHIPS
=============

1. U.S. Heavyweight

2. Cruiserweight

3. Tag Team

4. World Heavyweight

5. TV Title

==================================================
KNOWN SYSTEMS
=============

✓ Championship rosters

✓ Champion IDs

✓ Defending champion IDs

✓ Belt graphics

✓ Intro graphics

✓ Menu graphics

✓ Victory graphics

✓ Defense graphics

==================================================
CHAMPIONSHIP PRESENTATION ASSETS
================================

Intro Assets

0118 - WCW Logo

0119 - U.S. Heavyweight Championship

011A - Cruiserweight Championship

011B - Tag Team Titles

011C - World Heavyweight Championship

011D - TV Title

Menu Assets

0094 - U.S. Heavyweight

0095 - Cruiserweight

0096 - Tag Team

0097 - World Heavyweight

0098 - TV Title

==================================================
CHAMPIONSHIP ROSTERS
====================

US HEAVYWEIGHT

1F Eric Bischoff

32 Lodi

2E Kidman

0F Larry Zbyszko

27 La Parka

22 Chris Jericho

21 Eddie Guerrero

28 Psychosis

23 Rey Mysterio Jr.

25 Dean Malenko

24 Juventud Guerrera

20 Ultimo Dragon

26 Chavo Guerrero Jr.

14 Alex Wright

34 AKI Man

35 Shogun

36 Executioner

37 Dr. Frank

38 Jekel

39 Maya Inca Boy

3A Hawk Hana

3B Kim Chee

3C Dake Ken

3D Brickowski

---

CRUISERWEIGHT

08 Chris Benoit

22 Chris Jericho

21 Eddie Guerrero

28 Psychosis

0B Booker T

23 Rey Mysterio Jr.

25 Dean Malenko

24 Juventud Guerrera

20 Ultimo Dragon

26 Chavo Guerrero Jr.

14 Alex Wright

2E Kidman

32 Lodi

27 La Parka

---

TAG TEAM

17 Kevin Nash

16 Randy Savage

01 Sting

03 Lex Luger

15 Hollywood Hogan

07 Bret Hart

02 Giant

1E Brian Adams

2C Raven

33 Saturn

2E Kidman

2F Riggs

04 Diamond Dallas Page

08 Chris Benoit

0A Goldberg

10 Verify Later

13 Ernest Miller

11 Scott Putski

0D Meng

0E Barbarian

30 Van Hammer

24 Juventud Guerrera

27 La Parka

28 Psychosis

22 Chris Jericho

21 Eddie Guerrero

23 Rey Mysterio Jr.

20 Ultimo Dragon

2D Perry Saturn

2B Kanyon

1A Scott Steiner

1D Scott Norton

06 Roddy Piper

0F Larry Zbyszko

0B Booker T

14 Alex Wright

---

WORLD HEAVYWEIGHT

1E Brian Adams

1D Scott Norton

1B Curt Hennig

1F Eric Bischoff

32 Lodi

2F Riggs

31 Sick Boy

2E Kidman

0C Disco Inferno

0B Booker T

29 Glacier

30 Van Hammer

12 Yuji Nagata

0F Larry Zbyszko

2A Wrath

27 La Parka

22 Chris Jericho

21 Eddie Guerrero

28 Psychosis

23 Rey Mysterio Jr.

25 Dean Malenko

24 Juventud Guerrera

---

TV TITLE

15 Hollywood Hogan

02 Giant

18 Scott Hall

1F Eric Bischoff

17 Kevin Nash

01 Sting

03 Lex Luger

16 Randy Savage

00 Verify Later

07 Bret Hart

0F Larry Zbyszko

34 AKI Man

35 Shogun

36 Executioner

37 Dr. Frank

38 Jekel

39 Maya Inca Boy

3A Hawk Hana

3B Kim Chee

3C Dake Ken

3D Brickowski

3E Han Zo Mon

3F Black Ninja

==================================================
ARCHITECTURE
============

Championship

↓

Definitions

↓

Roster

↓

Champion

↓

Defending Champion

↓

Belt Graphics

↓

Intro Graphics

↓

Menu Graphics

↓

Victory Graphics

↓

Defense Graphics

==================================================
UNKNOWN FIELDS
==============

Identifier

Unknown1

Flags1

Flags2

Unknown4

Unknown5

Unknown6

Unknown7

Unknown8

==================================================
VERIFY LATER
============

TV Title

00 -> Unknown wrestler

Tag Team

10 -> Unknown wrestler

==================================================
OPEN QUESTIONS
==============

Does championship eligibility pull from:

* Stables?

* Managers?

* Wrestler IDs only?

* Hidden flags?

How are champions stored?

How are defending champions stored?

How are title defenses tracked?

==================================================
STATUS
======

Roster Decoding: 100%

Presentation Assets: 100%

Architecture: 80%

Unknown Fields: Unsolved

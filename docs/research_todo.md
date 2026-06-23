==================================================
VERIFY LATER
==================================================

TV Title

00 -> Unknown wrestler

Tag Team

10 -> Unknown wrestler

Han Zo Mon

Verify VPW ID

Black Ninja

Verify VPW ID

Wrath

Exists in ROM.
GameShark only.

==================================================
OPEN INVESTIGATIONS
==================================================

Arena architecture

Championship architecture

Stable architecture

Manager system

Costume architecture

Intro architecture

Music architecture



## Blocked: Stable Membership Resolution

Stable Definitions show wrestler definition pointers, but VPW Studio's View Wrestler button is not implemented.

Current blocker:

Stable member pointers cannot be resolved to wrestler names from the UI.

Do not assume pointer-to-wrestler matches.

Next possible solutions:

- Search VPW Studio source code for stable pointer handling
- Find where wrestler definition structs are stored
- Compare stable pointers to wrestler definition table addresses
- Use code or export data to resolve pointers later

## Investigate Stable Member Pointers

Stable member values do not match Wrestler Editor's visible Name, Height, or Weight pointers.

Example:

Hollywood Hogan visible pointers:

- Name Pointer: 80039368
- Height Pointer: 8003937C
- Weight Pointer: 80039384

Stable 0 first member pointer:

- 80039390

Observation:

The stable pointer is close to Hogan's visible pointer range, but it is not the same as any visible pointer.

Working theory:

Stable member pointers may point to wrestler definition structs or nearby wrestler data blocks.

Status:

Blocked until source code or memory layout is inspected.

## AI Logic Investigation

Searches in File Table returned no obvious AI-related entries.

Terms searched:

- AI
- Difficulty
- CPU
- Logic
- Behavior

Conclusion:

AI logic is likely stored in code/behavior tables, not labeled assets.

Status:

Blocked until deeper ROM/code analysis.
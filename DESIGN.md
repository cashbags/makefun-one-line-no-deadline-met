# Design — One Line, No Deadline Met

## What the entry is

A tiny program that writes exactly one sentence to `/output/entry.txt`: a
joke that excuses a missed deadline. The sentence is the whole entry. There
is no image, no link, no second line, no setup. The program takes no input,
takes no arguments, and produces the same bytes on every run.

## The line

> Someone asked me a quick question at nine and it only let go of me at
> noon, by which time the deadline had filed a missing-persons report.

138 characters, 138 bytes, one sentence, one period at the end.

## Why this line

The competition's judge is a comedy editor weighing five things in order:
whether the line is a one-line joke excusing a missed deadline; whether it
is a real joke with a turn; whether it reads cleanly aloud with the punch
at the end; whether it sounds like a cornered person; whether it is fresh.

The line is built to answer each of those in turn:

1. **It is an excuse for a missed deadline.** The missed deadline is named
   in the sentence itself, and the sentence explains why it was missed: the
   speaker was held up from nine until noon. Nothing in the line is about
   anything else.
2. **It is a joke with a turn, not an apology.** The setup sounds like an
   ordinary complaint about a meeting ("a quick question"), and the turn
   flips the roles: the deadline stops being a date on a calendar and
   becomes a person who has gone to the police about the speaker. The
   speaker is not sorry; the deadline is the one taking action.
3. **It reads cleanly aloud with the punch at the end.** One sentence, one
   clause after another, no commas piling up, and the funny image — the
   missing-persons report — is the last thing the listener hears.
4. **It sounds like a cornered person.** "It only let go of me at noon" is
   how someone talks when they have just escaped a meeting that ate their
   morning. The exaggeration is one step past literal: the question did not
   literally hold the speaker hostage, and the deadline did not literally
   file a report, but both feel true to anyone who has lost a morning to
   "a quick question".
5. **It is fresh.** The field's submitted titles (checked in `detail.json`
   at build time) show no "quick question" angle, no missing-persons
   angle, and nothing in this lane at all. The banned lanes — the dog, the
   alarm that did not go off, bad traffic, a plain apology — are nowhere
   near it.

## Why the "quick question" lane

Twelve candidate lines were drafted across twelve empty lanes (deadline
moved itself, calendar ate the day, build passed locally, linter complaint,
deadline unionised, autosave betrayal, deploy overtime, meeting ate the
afternoon, timezone, spellchecker, printer ate the draft, and the quick
question). They were judged pairwise against the exact judge brief, bracket
plus a rematch of the top two; the full table is in `CANDIDATES.md`.

The quick-question line won because its end punch is the biggest of the
field and its lane is the emptiest. The runner-up was the calendar line
("My calendar ate the whole workday in one bite and then sent me a
reminder to finish the thing it had just swallowed"), which has a strong
double turn but a slightly more familiar image. The printer line was cut in
the final round despite a good courtroom punch, because "the printer ate
the draft" sits too close to the banned dog-ate-it lane.

## How the program works

`main.py` holds the line as a single string constant and writes it to
`/output/entry.txt` with no trailing newline, so the file is exactly the
line: 138 bytes. It creates `/output` if it does not exist. It opens no
network connection, reads no file, consults no clock, and takes no
environment input, so two runs in two fresh directories produce
byte-identical output. That is verified before every bundle by running it
twice and comparing sha256 hashes.

## What is not in the entry

- No picture, no link, no second line — the rules forbid all three.
- No text addressed to the judge. The rules allow it, but the line is
  stronger standing on its own joke than on a plea for a verdict.
- No apology. The brief explicitly demotes plain apologies; the line
  explains the miss by blaming the question, not by saying sorry.

## Limits and risks

- The line was self-judged, not judge-tested. Its real win rate is unknown
  until the first blind round after submission.
- The field is small (10 submissions at build time) and the top five places
  pay, so a good line has a real shot — but a small field also means a
  handful of strong entries can crowd it out.
- The judge is a model, and the same pair can be answered differently on a
  re-ask. The line is built to win on the first criterion where two lines
  differ, which is the brief's own instruction to the judge.

## Revision notes

- The entry program was run twice in fresh `/output` directories on
  2026-11-25; both runs wrote byte-identical `entry.txt`
  (sha256 `c042956219788b38838a3a320d6b7e66d616db2a19f23323e5d80332c5fcf6ee`,
  138 bytes). No change to `main.py` was needed after the first run.
- This section was added after the tournament table was written, to record
  the determinism check and the final choice in the design doc itself.

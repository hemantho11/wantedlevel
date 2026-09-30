# Handoff — Phase 1 done here, Phases 1b–4 run on the Mac

This folder was produced by `/longform "GTA 6 Is Going to Change Open-World Games Forever — Here's Why"` in a cloud Linux
session that has none of the pipeline's prerequisites (no source footage, no ffmpeg, no Swift/AVFoundation, no macOS).
Only **Phase 1 (topic + script)** of `longform/PROMPT_LONGFORM.md` could be completed. No ElevenLabs credits were spent.

## What is here
- `chapters.json` — cold open + 7 chapters + recap, Leo audio tags, keyword callouts. Validated locally: every key trigger
  and every plan anchor resolves with the exact lookup `gen_longform.py` uses; all chapters are 80–100 words and ≤ 600 chars.
- `plan.py` — v4 / "rank" / Sept-29 settings baked in. Every timestamp is one already used in `examples/story-explained`
  or `examples/realism-remake` (same cut lists), except lines tagged `# SCOUT`.
- `project.json` — final file name.
- `upload-notes.md` — title + 2 alternates, description, tags, chapter list, thumbnail brief (4 variants).

## To finish (Mac, in `~/GTA6 Videos _Claude/`)
1. Copy this folder to `~/GTA6 Videos _Claude/GTA6 Long-form - Changing Open World/` and `mkdir voiceovers`.
2. Set `SRC` at the top of `plan.py` to the 4K files in `~/GTA6 Videos _Claude/4k trailers/` (see the comment there).
3. Scout the `# SCOUT` beats with `tools/fine` (t1 11.0, t1 36.0, t1 63.62–65.66, t2 6.2, el 812.9) and swap if wrong.
4. Phase 1b: ElevenLabs Leo (`TLC61WvtioR7PrhxZ1RH`, `eleven_v3`), `estimate_only` first (9 chunks ≈ 5,000 credits,
   under the 8,000 no-ask limit), max 5 concurrent, `curl` each to `voiceovers/<id>.mp3`; `tools/rms` −15…−19,
   `tools/pauses <mp3> 0.25`; re-record any `[whispers]` line that is > ~3 dB quieter than its take.
5. `python3 longform/gen_longform.py "<project>"`, fix every WARN, `longform/editor_long edit-list.json --validate`, render.
6. Phase 3 viewer QA on `tools/fine` sheets, Phase 4 thumbnails (brief in `upload-notes.md`), final report.

## Judgement calls to review
- **b-roll under place names (c6):** while Leo reads "Grassrivers. Port Gellhorn. Mount Kalaga." the plan shows Keys footage
  (t2 20.5–27.4). It is not those places. If a scout finds trailer aerials of them, swap those in.
- **Theory labelling:** the hollow-star meaning (c5) is voiced as "it seems to mean… that's a theory". "No mission title,
  no loading screen" (c7) is hedged with "none that Rockstar has shown".
- **Rockstar-site facts used:** Leonida, the Keys (Jason lives there), Grassrivers, Port Gellhorn, Mount Kalaga; release
  November 19. "Fifty-three thousand viewers" and the live chat are on screen at el 1106.0.
- **Recap keys:** the recap chapter carries 8 keyword callouts (7 numbered reasons + the comment question), like the
  numbered recap in `examples/story-explained`; other chapters carry 5.
- **No readable-text keys:** no callout is placed on the "Guys everywhere" text-message zooms (c7).
- The estimated runtime at 0.36 s/word is about 5:35 before card leads and tails, inside the 5–10 min target.

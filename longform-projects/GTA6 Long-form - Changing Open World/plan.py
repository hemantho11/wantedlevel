# Shot plan for "GTA 6 Is Going to Change Open-World Games Forever - Here's Why" — loaded by longform/gen_longform.py
# (anchor word or None, kind m|c|z|p|q, source t1|t2|el, time or [chain], focus (x,y) | region R(...) | rect box169(...))
#
# DRAFT written off-Mac: every timestamp below is one already used and verified in examples/story-explained/plan.py or
# examples/realism-remake/plan.py (same footage, same cut lists). Beats marked "# SCOUT" use a timestamp whose content
# was not verified on a fine sheet — check them with tools/fine before rendering.

# ---- user rules, Sept 29 (PROMPT_LONGFORM.md) ----
STYLE = "v4"                                    # live footage at real speed, freeze-then-zoom, q montages in the hook
TEXT_STYLE = "rank"; CARD = 1.9; CH_HOLD = 4.4; CH_FLASH = False   # lower-third chapter titles over live footage
CH_PREFIX = ""                                  # not a ranked list
SFX_MODE = "chapters"; CH_WHOOSH = 0.22; CH_IMPACT = 0.26            # quiet transition sounds on chapter cards only
KW_PLATE = False                                # keywords as plain text
VO_VOL = 0.76; HOOK_VOL = 0.17; RISER_VOL = 0.2; LETTERBOX_C0 = False
# Sources: gen_frame_by_frame.py still defaults SRC to ~/Downloads. The 4K files now live in
# "~/GTA6 Videos _Claude/4k trailers/" — override here once the exact file names are confirmed, e.g.
# SRC = {"t1": f"{HOME}/GTA6 Videos _Claude/4k trailers/<Trailer 1>.mp4", "t2": ..., "el": ...}

STARS = box169(1745, 60, 420)                   # wanted stars, top right (README v6 note)
VIEWERS = R(1120, 60, 800, 450); CHAT = R(1120, 470, 800, 450)   # livestream overlay (el 1106.0)
HURRY = R(1700, 940, 210, 125)                  # "hurry" button prompt (el 428.0)
LOGO = R(440, 250, 1040, 585)                   # GTA VI logo + date (el 1594.0)

PLAN = {
 # cold open: fast-cut hook on the first sentence, then the reveals it names, then a montage that teases the chapters
 "c0": [(None, "q", "el", [("el", 1104.2), ("el", 1073.0), ("el", 847.5), ("el", 1085.5), ("el", 1504.0)], False),
        ("fifty-three", "z", "el", 1106.0, VIEWERS), ("outrun", "m", "el", 1106.5, (960, 700)),
        ("Lucia", "m", "el", 1073.0, (1000, 540)), ("whole", "m", "el", 1075.5, (1300, 520)),
        ("flips,", "m", "el", 847.5, (960, 520)), ("underside", "z", "el", 849.9, box169(760, 620, 900)),
        ("None", "q", "el", [("el", 1229.1), ("el", 561.0), ("el", 1127.6), ("el", 436.3)], False),
        ("Rockstar", "m", "t1", [3.4, 5.1], (1100, 500)), ("three", "m", "t2", 6.2, (960, 540)),
        ("hidden", "m", "el", [40.2, 43.4], (1100, 540)), ("So", "m", "el", [1249.4, 1252.0], (1100, 500)),
        ("seven", "q", "el", [("el", 593.5), ("el", 911.0), ("el", 1176.0), ("el", 1432.0)], False)],
 "c1": [(None, "m", "el", [1096.5, 1100.5], (1100, 540)), ("most", "m", "el", 1264.0, (960, 540)), ("ignore", "m", "el", 1276.0, (960, 540)),
        ("Watch", "m", "el", 1070.3, (960, 540)), ("Lucia", "m", "el", 1073.0, (1000, 540)), ("people", "m", "el", 1075.5, (1300, 520)),
        ("hides", "m", "el", 1077.5, (1000, 540)), ("Inside", "m", "el", [1080.1, 1081.4], (1100, 600)), ("hero", "m", "el", 1083.5, (1000, 540)),
        ("moment", "z", "el", 1081.4, box169(1450, 350, 900)), ("outnumbered,", "p", "el", 1081.4, box169(1450, 350, 640)),
        ("Even", "m", "el", 43.4, (1100, 540)), ("hips", "z", "el", 44.8, box169(1150, 520, 1000)),
        ("That's", "m", "el", [1083.5, 1085.5], (1000, 540)), ("city", "m", "el", [1249.4, 1252.0], (1100, 500))],
 "c2": [(None, "m", "el", 1096.5, (1100, 540)), ("world", "m", "el", 1100.5, (1100, 540)), ("livestreaming", "m", "el", 1104.2, (960, 560)),
        ("Fifty-three", "z", "el", 1106.0, VIEWERS), ("chat", "p", "el", 1106.0, CHAT), ("cops", "m", "el", 1106.5, (960, 700)),
        ("Back", "m", "el", 455.5, (1300, 520)), ("nature", "z", "el", 459.4, box169(1600, 500, 900)), ("nobody's", "p", "el", 459.4, box169(1600, 500, 600)),
        ("whole", "m", "t1", [41.4, 43.95, 46.6, 49.95, 51.17], (960, 540)), ("clips,", "m", "t1", [55.05, 57.4], (960, 540)),
        ("Most", "m", "el", 1276.0, (960, 540)), ("This", "m", "t1", [63.62, 65.66, 66.7, 67.7], (960, 500))],   # SCOUT t1 63.62-67.7 (social clips?)
 "c3": [(None, "m", "el", 488.0, (960, 560)), ("drops", "m", "el", 492.5, (900, 560)), ("rocks", "m", "el", 495.5, (900, 600)),
        ("starts", "m", "el", 500.5, (900, 600)), ("smoke", "z", "el", 503.2, box169(1150, 800, 900)),
        ("Lucia", "m", "el", 560.9, (700, 540)), ("kicks", "z", "el", 561.6, box169(700, 520, 1100)), ("spent", "m", "el", 563.0, (700, 540)),
        ("raid,", "m", "el", [280.0, 282.5], (960, 540)), ("rips", "m", "el", 286.1, (1300, 500)), ("dust", "m", "el", 288.0, (1000, 500)),
        ("police", "m", "el", 847.5, (960, 520)), ("underside", "z", "el", 849.9, box169(760, 620, 900)),
        ("None", "m", "el", [840.2, 842.0], (960, 540)), ("All", "m", "el", 845.0, (960, 560))],
 "c4": [(None, "m", "el", [396.0, 413.0], (960, 540)), ("Every", "m", "t2", [8.2, 9.8], (1100, 500)), ("Now", "m", "el", 382.7, (1060, 500)),
        ("Sticky", "z", "el", 383.5, box169(1040, 600, 700)), ("She", "m", "el", 405.5, (560, 540)), ("button", "c", "el", 428.0, HURRY),
        ("He", "m", "el", 436.0, (960, 540)), ("light", "m", "el", 438.2, (900, 600)),
        ("Then", "m", "el", 578.0, (960, 540)), ("Effluvia,", "z", "el", 640.5, box169(1200, 430, 900)), ("holding", "m", "el", 593.5, (960, 540)),
        ("That's", "m", "el", 594.5, (960, 540)), ("life,", "m", "el", 602.0, (960, 540))],
 "c5": [(None, "m", "el", [1080.1, 1081.4], (1100, 600)), ("After", "m", "el", 1083.4, (1000, 540)), ("sprints", "m", "el", 1085.5, (1200, 560)),
        ("Look", "z", "el", 1084.2, box169(1745, 60, 800)), ("Some", "p", "el", 1084.2, STARS), ("It", "m", "el", 1076.3, (1300, 520)), ("but", "m", "t1", [76.6, 68.8], (800, 450)),
        ("That's", "m", "el", [1087.0, 1088.8], (960, 540)), ("Later,", "m", "el", [894.5, 898.1], (900, 540)), ("cop", "m", "el", 911.0, (900, 540)),
        ("In", "m", "el", [840.2, 847.0], (960, 520)), ("Here,", "m", "el", 908.6, (1000, 540))],
 "c6": [(None, "m", "el", 1207.5, (960, 540)), ("Lucia", "m", "el", 1127.6, (960, 500)), ("below", "m", "el", 1129.5, (960, 600)),
        ("canals,", "z", "el", 1131.5, box169(960, 700, 1300)),
        ("But", "m", "t1", [11.0, ("t2", 6.2)], (960, 540)),                     # SCOUT: t1 11.0 / t2 6.2 should be establishing aerials
        ("Keys,", "m", "t2", [8.2, 11.5], (1100, 500)),
        ("Grassrivers.", "m", "t2", [20.5, 23.3, 27.4], (960, 540)),            # SCOUT: Keys b-roll under the place names, not those places
        ("In", "m", "el", 1115.0, (960, 540)), ("dirt", "m", "el", 1117.4, (900, 560)), ("private", "m", "el", 1176.0, (960, 540)),
        ("party", "m", "el", [1264.0, 1276.0], (960, 540)), ("Other", "m", "el", [1148.0, 1151.2], (960, 540)),
        ("This", "m", "el", [1122.5, 1124.5], (960, 540))],
 "c7": [(None, "m", "el", [636.3, 639.4], (1200, 420)), ("There's", "m", "el", 646.0, (960, 540)), ("date", "m", "el", 664.0, (960, 540)),
        ("offer", "m", "el", 672.0, (700, 540)), ("Deliver", "m", "el", 738.0, (960, 540)), ("It", "m", "el", 754.0, (960, 540)),
        ("stranger", "m", "el", [810.7, 812.9], (1000, 540)),                    # SCOUT el 812.9 (should still be the car interior)
        ("masks", "m", "el", 828.3, (760, 540)), ("gun", "m", "el", [838.2, 840.2, 845.0], (900, 540)),
        ("Then", "m", "el", 1427.5, (700, 500)), ("Guys", "z", "el", 1432.0, box169(1420, 440, 820)), ("Ten-plus", "z", "el", 1435.0, box169(360, 690, 820)),
        ("And", "m", "el", [1490.7, 1504.0, 1510.6], (960, 540)), ("No", "m", "el", [1513.0, 1515.3], (960, 540)), ("Just", "m", "el", 1525.9, (960, 540))],
 "c8": [(None, "m", "el", [1548.6, 1550.8, 1552.5], (960, 540)), ("reacts", "m", "el", 1075.5, (1300, 520)), ("running", "m", "el", 1104.2, (960, 560)),
        ("Physics", "m", "el", 561.0, (700, 540)), ("Downtime", "m", "el", 593.5, (960, 540)), ("Cops", "m", "el", 911.0, (900, 540)),
        ("whole", "m", "el", 1129.5, (960, 600)), ("story", "m", "el", 672.0, (700, 540)),
        ("Most", "m", "t1", [68.8, 70.3], (960, 420)), ("GTA", "m", "t2", [123.0, 124.6, 125.8], (960, 540)),
        ("So", "m", "el", [1249.4, 1252.0], (960, 540)), ("Tell", "m", "t1", 36.0, (960, 540)),   # SCOUT t1 36.0
        ("GTA", "z", "el", 1594.0, LOGO), ("subscribe", "m", "t2", [66.3, 63.2], (960, 540)), ("because", "m", "t1", [3.4, 5.1, 6.6, 8.5], (1100, 500))],
}

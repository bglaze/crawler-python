#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Treasure Generators for Crawler I
#  by Brock Glaze
#
#  crCalc_Treasure_Scrolls.py


import crawler
import crDice
import random
import string
import wx


all_scrolls = {

# Arcane Spells

"arcane_0": {
4: {"name": "acid splash", "value": 13},
8: {"name": "arcane mark", "value": 13},
13: {"name": "dancing lights", "value": 13},
17: {"name": "daze", "value": 13},
24: {"name": "detect magic", "value": 13},
28: {"name": "detect poison", "value": 13},
32: {"name": "disrupt undead", "value": 13},
37: {"name": "flare", "value": 13},
42: {"name": "ghost sound", "value": 13},
44: {"name": "know direction", "value": 13},
50: {"name": "light", "value": 13},
52: {"name": "lullaby", "value": 13},
57: {"name": "mage hand", "value": 13},
62: {"name": "mending", "value": 13},
67: {"name": "message", "value": 13},
72: {"name": "open/close", "value": 13},
77: {"name": "prestidigitation", "value": 13},
81: {"name": "ray of frost", "value": 13},
87: {"name": "read magic", "value": 13},
94: {"name": "resistance", "value": 13},
96: {"name": "summon instrument", "value": 13},
100: {"name": "touch of fatigue", "value": 13},
},

"arcane_1": {
3: {"name": "alarm", "value": 25},
5: {"name": "animate rope", "value": 25},
7: {"name": "burning hands", "value": 25},
9: {"name": "cause fear", "value": 25},
12: {"name": "charm person", "value": 25},
14: {"name": "chill touch", "value": 25},
16: {"name": "color spray", "value": 25},
19: {"name": "comprehend languages", "value": 25},
20: {"name": "confusion, lesser", "value": 50},
21: {"name": "cure light wounds", "value": 50},
24: {"name": "detect secret doors", "value": 25},
26: {"name": "detect undead", "value": 25},
29: {"name": "disguise self", "value": 25},
32: {"name": "endure elements", "value": 25},
35: {"name": "enlarge person", "value": 25},
37: {"name": "erase", "value": 25},
40: {"name": "expeditious retreat", "value": 25},
41: {"name": "feather fall", "value": 25},
43: {"name": "grease", "value": 25},
45: {"name": "hold portal", "value": 25},
47: {"name": "hypnotism", "value": 25},
49: {"name": "identify", "value": 125},
51: {"name": "jump", "value": 25},
54: {"name": "mage armor", "value": 25},
56: {"name": "magic missile", "value": 25},
59: {"name": "magic weapon", "value": 25},
62: {"name": "mount", "value": 25},
64: {"name": "Nystul's magic aura", "value": 25},
66: {"name": "obscuring mist", "value": 25},
74: {"name": "protection from chaos/evil/good/law", "value": 25},
76: {"name": "ray of enfeeblement", "value": 25},
78: {"name": "reduce person", "value": 25},
80: {"name": "remove fear", "value": 50},
82: {"name": "shield", "value": 25},
84: {"name": "shocking grasp", "value": 25},
86: {"name": "silent image", "value": 25},
88: {"name": "sleep", "value": 25},
90: {"name": "summon monster I", "value": 25},
93: {"name": "Tenser's floating disk", "value": 25},
95: {"name": "true strike", "value": 25},
96: {"name": "undetectable alignment", "value": 50},
98: {"name": "unseen servant", "value": 25},
100: {"name": "ventriloquism", "value": 25},
},

"arcane_2": {
1: {"name": "animal messenger", "value": 200},
2: {"name": "animal trance", "value": 200},
3: {"name": "arcane lock", "value": 175},
6: {"name": "bear's endurance", "value": 150},
8: {"name": "blindness/deafness", "value": 150},
10: {"name": "blur", "value": 150},
13: {"name": "bull's strength", "value": 150},
14: {"name": "calm emotions", "value": 200},
17: {"name": "cat's grace", "value": 150},
19: {"name": "command undead", "value": 150},
20: {"name": "continual flame", "value": 200},
21: {"name": "cure moderate wounds", "value": 200},
22: {"name": "darkness", "value": 150},
25: {"name": "darkvision", "value": 150},
26: {"name": "daze monster", "value": 150},
27: {"name": "delay poison", "value": 200},
29: {"name": "detect thoughts", "value": 150},
31: {"name": "disguise self", "value": 150},
34: {"name": "eagle's splendor", "value": 150},
35: {"name": "enthrall", "value": 200},
37: {"name": "false life", "value": 150},
39: {"name": "flaming sphere", "value": 150},
40: {"name": "fog cloud", "value": 150},
43: {"name": "fox's cunning", "value": 150},
44: {"name": "ghoul touch", "value": 150},
46: {"name": "glitterdust", "value": 150},
47: {"name": "gust of wind", "value": 150},
49: {"name": "hypnotic pattern", "value": 150},
52: {"name": "invisibility", "value": 150},
55: {"name": "knock", "value": 150},
56: {"name": "Leomund's trap", "value": 200},
58: {"name": "levitate", "value": 150},
59: {"name": "locate object", "value": 150},
60: {"name": "magic mouth", "value": 160},
62: {"name": "Melf's acid arrow", "value": 150},
63: {"name": "minor image", "value": 150},
65: {"name": "mirror image", "value": 150},
66: {"name": "misdirection", "value": 150},
67: {"name": "obscure object", "value": 150},
70: {"name": "owl's wisdom", "value": 150},
73: {"name": "protection from arrows", "value": 150},
75: {"name": "pyrotechnics", "value": 150},
78: {"name": "resist energy", "value": 150},
79: {"name": "rope trick", "value": 150},
80: {"name": "scare", "value": 150},
82: {"name": "scorching ray", "value": 150},
85: {"name": "see invisibility", "value": 150},
86: {"name": "shatter", "value": 150},
87: {"name": "silence", "value": 200},
88: {"name": "sound burst", "value": 200},
89: {"name": "spectral hand", "value": 150},
91: {"name": "spider climb", "value": 150},
93: {"name": "summon monster II", "value": 150},
95: {"name": "summon swarm", "value": 150},
96: {"name": "Tasha's hideous laughter", "value": 150},
97: {"name": "touch of idiocy", "value": 150},
99: {"name": "web", "value": 150},
100: {"name": "spering win", "value": 150},
},

"arcane_3": {
2: {"name": "arcane sight", "value": 375},
4: {"name": "blink", "value": 375},
6: {"name": "clairaudience/clairvoyance", "value": 375},
7: {"name": "cure serious wounds", "value": 525},
10: {"name": "daylight", "value": 525},
12: {"name": "deep slumber", "value": 375},
15: {"name": "dispel magic", "value": 375},
17: {"name": "displacement", "value": 375},
18: {"name": "explosive runes", "value": 375},
20: {"name": "fireball", "value": 375},
22: {"name": "flame arrow", "value": 375},
25: {"name": "fly", "value": 375},
27: {"name": "gaseous form", "value": 375},
29: {"name": "gentle repose", "value": 375},
30: {"name": "glibness", "value": 525},
31: {"name": "good hope", "value": 525},
33: {"name": "halt undead", "value": 375},
36: {"name": "haste", "value": 375},
38: {"name": "heroism", "value": 375},
40: {"name": "hold person", "value": 375},
41: {"name": "illusory script", "value": 425},
44: {"name": "invisibility sphere", "value": 375},
47: {"name": "keen edge", "value": 375},
49: {"name": "Leomund's tiny hut", "value": 375},
51: {"name": "lightning bolt", "value": 375},
59: {"name": "magic circle against chaos/evil/good/law", "value": 375},
62: {"name": "magic weapon, greater", "value": 375},
64: {"name": "major image", "value": 375},
66: {"name": "nondetection", "value": 425},
68: {"name": "phantom steed", "value": 375},
71: {"name": "protection from energy", "value": 375},
73: {"name": "rage", "value": 375},
75: {"name": "ray of exhaustion", "value": 375},
76: {"name": "sculpt sound", "value": 525},
77: {"name": "secret page", "value": 375},
78: {"name": "sepia snake sigil", "value": 875},
79: {"name": "shrink item", "value": 375},
81: {"name": "sleet storm", "value": 375},
83: {"name": "slow", "value": 375},
84: {"name": "speak with animals", "value": 525},
86: {"name": "stinking cloud", "value": 375},
88: {"name": "suggestion", "value": 375},
90: {"name": "summon monster III", "value": 375},
93: {"name": "tongues", "value": 375},
95: {"name": "vampiric touch", "value": 375},
98: {"name": "water breathing", "value": 375},
100: {"name": "wind wall", "value": 375},
},

"arcane_4": {
2: {"name": "animate dead", "value": 1050},
5: {"name": "arcane eye", "value": 700},
7: {"name": "bestow curse", "value": 700},
10: {"name": "charm monster", "value": 700},
13: {"name": "confusion", "value": 700},
15: {"name": "contagion", "value": 700},
17: {"name": "crushing despair", "value": 700},
18: {"name": "cure critical wounds", "value": 1000},
19: {"name": "detect scrying", "value": 700},
23: {"name": "dimension door", "value": 700},
26: {"name": "dimensional anchor", "value": 700},
28: {"name": "enervation", "value": 700},
30: {"name": "enlarge person, mass", "value": 700},
32: {"name": "Evard's black tentacles", "value": 700},
34: {"name": "fear", "value": 700},
37: {"name": "fire shield", "value": 700},
39: {"name": "fire trap", "value": 725},
42: {"name": "freedom of movement", "value": 1000},
43: {"name": "geas, lesser", "value": 700},
46: {"name": "globe of invulnerability, lesser", "value": 700},
48: {"name": "hallucinatory terrain", "value": 700},
50: {"name": "ice storm", "value": 700},
52: {"name": "illusory wall", "value": 700},
55: {"name": "invisibility, greater", "value": 700},
57: {"name": "Leomund's secure shelter", "value": 700},
58: {"name": "locate creature", "value": 700},
60: {"name": "minor creation", "value": 700},
61: {"name": "modify memory", "value": 1000},
62: {"name": "neutralize poison", "value": 1000},
64: {"name": "Otiluke's resilient sphere", "value": 700},
66: {"name": "phantasmal killer", "value": 700},
68: {"name": "polymorph", "value": 700},
70: {"name": "rainbow pattern", "value": 700},
71: {"name": "Rary's mnemonic enhancer", "value": 700},
73: {"name": "reduce person, mass", "value": 700},
76: {"name": "remove curse", "value": 700},
77: {"name": "repel vermin", "value": 1000},
79: {"name": "scrying", "value": 700},
81: {"name": "shadow conjuration", "value": 700},
83: {"name": "shout", "value": 700},
85: {"name": "solid fog", "value": 700},
86: {"name": "speak with plants", "value": 1000},
88: {"name": "stone shape", "value": 700},
91: {"name": "stoneskin", "value": 950},
93: {"name": "summon monster IV", "value": 700},
96: {"name": "wall of fire", "value": 700},
99: {"name": "wall of ice", "value": 700},
100: {"name": "zone of silence", "value": 1000},
},

"arcane_5": {
2: {"name": "animal growth", "value": 1125},
5: {"name": "baleful polymorph", "value": 1125},
7: {"name": "Bigby's interposing hand", "value": 1125},
9: {"name": "blight", "value": 1125},
12: {"name": "break enchantment", "value": 1125},
14: {"name": "cloudkill", "value": 1125},
17: {"name": "cone of cold", "value": 1125},
19: {"name": "contact other plane", "value": 1125},
20: {"name": "cure light wounds, mass", "value": 1625},
23: {"name": "dismissal", "value": 1125},
26: {"name": "dispel magic, greater", "value": 1625},
28: {"name": "dominate person", "value": 1125},
29: {"name": "dream", "value": 1125},
31: {"name": "fabricate", "value": 1125},
33: {"name": "false vision", "value": 1375},
35: {"name": "feeblemind", "value": 1125},
39: {"name": "hold monster", "value": 1125},
40: {"name": "Leomund's secret chest", "value": 1125},
41: {"name": "magic jar", "value": 1125},
43: {"name": "major creation", "value": 1125},
45: {"name": "mind fog", "value": 1125},
47: {"name": "mirage arcana", "value": 1125},
49: {"name": "Mordenkainen's faithful hound", "value": 1125},
51: {"name": "Mordenkainen's private sanctum", "value": 1125},
53: {"name": "nightmare", "value": 1125},
57: {"name": "overland flight", "value": 1125},
60: {"name": "passwall", "value": 1125},
61: {"name": "permanency", "value": 10125},
63: {"name": "persistent image", "value": 1125},
65: {"name": "planar binding, lesser", "value": 1125},
67: {"name": "prying eyes", "value": 1125},
69: {"name": "Rary's telepathic bond", "value": 1125},
71: {"name": "seeming", "value": 1125},
74: {"name": "sending", "value": 1125},
76: {"name": "shadow evocation", "value": 1125},
77: {"name": "song of discord", "value": 1625},
79: {"name": "summon monster V", "value": 1125},
80: {"name": "symbol of pain", "value": 2125},
81: {"name": "symbol of sleep", "value": 2125},
83: {"name": "telekinesis", "value": 1125},
88: {"name": "teleport", "value": 1125},
90: {"name": "transmute mud to rock", "value": 1125},
92: {"name": "transmute rock to mud", "value": 1125},
95: {"name": "wall of force", "value": 1125},
98: {"name": "wall of stone", "value": 1125},
100: {"name": "waves of fatigue", "value": 1125},
},

"arcane_6": {
2: {"name": "acid fog", "value": 1650},
5: {"name": "analyze dweomer", "value": 1650},
6: {"name": "animate objects", "value": 2400},
9: {"name": "antimagic field", "value": 1650},
12: {"name": "bear's endurance, mass", "value": 1650},
14: {"name": "Bigby's forceful hand", "value": 1650},
17: {"name": "bull's strength, mass", "value": 1650},
20: {"name": "cat's grace, mass", "value": 1650},
23: {"name": "chain lightning", "value": 1650},
25: {"name": "circle of death", "value": 2150},
26: {"name": "contingency", "value": 1650},
28: {"name": "control water", "value": 1650},
29: {"name": "create undead", "value": 2350},
30: {"name": "cure moderate wounds, mass", "value": 2400},
33: {"name": "disintegrate", "value": 1650},
37: {"name": "dispel magic, greater", "value": 1650},
40: {"name": "eagle's splendor, mass", "value": 1650},
42: {"name": "eyebite", "value": 1650},
43: {"name": "find the path", "value": 2400},
45: {"name": "flesh to stone", "value": 1650},
48: {"name": "fox's cunning, mass", "value": 1650},
49: {"name": "geas/quest", "value": 1650},
52: {"name": "globe of invulnerability", "value": 1650},
53: {"name": "guards and wards", "value": 1650},
54: {"name": "heroes' feast", "value": 2400},
56: {"name": "heroism, greater", "value": 1650},
57: {"name": "legend lore", "value": 1900},
59: {"name": "mislead", "value": 1650},
60: {"name": "Mordenkainen's lucubration", "value": 1650},
62: {"name": "move earth", "value": 1650},
64: {"name": "Otiluke's freezing sphere", "value": 1650},
67: {"name": "owl's wisdom, mass", "value": 1650},
69: {"name": "permanent image", "value": 1650},
71: {"name": "planar binding", "value": 1650},
73: {"name": "programmed image", "value": 1675},
75: {"name": "repulsion", "value": 1650},
78: {"name": "shadow walk", "value": 1650},
81: {"name": "stone to flesh", "value": 1650},
83: {"name": "suggestion, mass", "value": 1650},
85: {"name": "summon monster VI", "value": 1650},
86: {"name": "symbol of fear", "value": 2650},
87: {"name": "symbol of persuasion", "value": 6650},
88: {"name": "sympathetic vibration", "value": 2400},
90: {"name": "Tenser's transformation", "value": 1950},
93: {"name": "true seeing", "value": 1900},
95: {"name": "undeath to death", "value": 2150},
97: {"name": "veil", "value": 1650},
100: {"name": "wall of iron", "value": 1700},
},

"arcane_7": {
3: {"name": "arcane sight, greater", "value": 2275},
7: {"name": "banishment", "value": 2275},
10: {"name": "Bigby's grasping hand", "value": 2275},
13: {"name": "control undead", "value": 2275},
16: {"name": "control weather", "value": 2275},
19: {"name": "delayed blast fireball", "value": 2275},
21: {"name": "Drawmij's instant summons", "value": 3275},
25: {"name": "ethereal jaunt", "value": 2275},
28: {"name": "finger of death", "value": 2275},
31: {"name": "forcecage", "value": 23775},
35: {"name": "hold person, mass", "value": 2275},
38: {"name": "insanity", "value": 2275},
42: {"name": "invisibility, mass", "value": 2275},
43: {"name": "limited wish", "value": 3775},
45: {"name": "Mordenkainen's magnificent mansion", "value": 2275},
48: {"name": "Mordenkainen's sword", "value": 2275},
51: {"name": "phase door", "value": 2275},
54: {"name": "plane shift", "value": 2275},
57: {"name": "power word blind", "value": 2275},
61: {"name": "prismatic spray", "value": 2275},
64: {"name": "project image", "value": 2280},
67: {"name": "reverse gravity", "value": 2275},
70: {"name": "scrying, greater", "value": 2275},
73: {"name": "sequester", "value": 2275},
76: {"name": "shadow conjuration, greater", "value": 2275},
77: {"name": "simulacrum", "value": 7275},
80: {"name": "spell turning", "value": 2275},
82: {"name": "statue", "value": 2275},
85: {"name": "summon monster VII", "value": 2275},
86: {"name": "symbol of stunning", "value": 7275},
87: {"name": "symbol of weakness", "value": 7275},
90: {"name": "teleport object", "value": 2275},
95: {"name": "teleport, greater", "value": 2275},
97: {"name": "vision", "value": 2775},
100: {"name": "waves of exhaustion", "value": 2275},
},

"arcane_8": {
2: {"name": "antipathy", "value": 3000},
5: {"name": "Bigby's clenched fist", "value": 3000},
8: {"name": "binding", "value": 8500},
12: {"name": "charm monster, mass", "value": 3000},
13: {"name": "clone", "value": 4000},
16: {"name": "create greater undead", "value": 3000},
19: {"name": "demand", "value": 3600},
22: {"name": "dimensional lock", "value": 3000},
26: {"name": "discern location", "value": 3000},
29: {"name": "horrid wilting", "value": 3000},
32: {"name": "incendiary cloud", "value": 3000},
35: {"name": "iron body", "value": 3000},
38: {"name": "maze", "value": 3000},
41: {"name": "mind blank", "value": 3000},
44: {"name": "moment of prescience", "value": 3000},
48: {"name": "Otiluke's telekinetic sphere", "value": 3000},
51: {"name": "Otto's irresistible dance", "value": 3000},
54: {"name": "planar binding, greater", "value": 3000},
57: {"name": "polar ray", "value": 3000},
60: {"name": "polymorph any object", "value": 3000},
63: {"name": "power word stun", "value": 3000},
66: {"name": "prismatic wall", "value": 3000},
70: {"name": "protection from spells", "value": 3500},
73: {"name": "prying eyes, greater", "value": 3000},
76: {"name": "scintillating pattern", "value": 3000},
78: {"name": "screen", "value": 3000},
81: {"name": "shadow evocation, greater", "value": 3000},
84: {"name": "shout, greater", "value": 3000},
87: {"name": "summon monster VIII", "value": 3000},
90: {"name": "sunburst", "value": 3000},
91: {"name": "symbol of death", "value": 8000},
92: {"name": "symbol of insanity", "value": 8000},
94: {"name": "sympathy", "value": 4500},
98: {"name": "temporal stasis", "value": 3500},
100: {"name": "trap the soul", "value": 13000},
},

"arcane_9": {
3: {"name": "astral projection", "value": 4870},
7: {"name": "Bigby's crushing hand", "value": 3825},
12: {"name": "dominate monster", "value": 3825},
16: {"name": "energy drain", "value": 3825},
21: {"name": "etherealness", "value": 3825},
25: {"name": "foresight", "value": 3825},
31: {"name": "freedom", "value": 3825},
36: {"name": "gate", "value": 8825},
40: {"name": "hold monster, mass", "value": 3825},
44: {"name": "imprisonment", "value": 3825},
49: {"name": "meteor swarm", "value": 3825},
53: {"name": "Mordenkainen's disjunction", "value": 3825},
58: {"name": "power word kill", "value": 3825},
62: {"name": "prismatic sphere", "value": 3825},
66: {"name": "refuge", "value": 3825},
70: {"name": "shades", "value": 3825},
76: {"name": "shapechange", "value": 3825},
79: {"name": "soul bind", "value": 3825},
83: {"name": "summon monster IX", "value": 3825},
86: {"name": "teleportation circle", "value": 4825},
91: {"name": "time stop", "value": 3825},
95: {"name": "wail of the banshee", "value": 3825},
99: {"name": "weird", "value": 3825},
100: {"name": "wish", "value": 28825},
},

# Divine Spells

"divine_0": {
7: {"name": "create water", "value": 13},
14: {"name": "cure minor wounds", "value": 13},
22: {"name": "detect magic", "value": 13},
29: {"name": "detect poison", "value": 13},
36: {"name": "flare", "value": 13},
43: {"name": "guidance", "value": 13},
50: {"name": "inflict minor wounds", "value": 13},
57: {"name": "know direction", "value": 13},
65: {"name": "light", "value": 13},
72: {"name": "mending", "value": 13},
79: {"name": "purify food and drink", "value": 13},
86: {"name": "read magic", "value": 13},
93: {"name": "resistance", "value": 13},
100: {"name": "virtue", "value": 13},
},

"divine_1": {
1: {"name": "alarm", "value": 100},
3: {"name": "bane", "value": 25},
6: {"name": "bless", "value": 25},
9: {"name": "bless water", "value": 50},
10: {"name": "bless weapon", "value": 100},
12: {"name": "calm animals", "value": 25},
14: {"name": "cause fear", "value": 25},
16: {"name": "charm animal", "value": 25},
19: {"name": "command", "value": 25},
21: {"name": "comprehend languages", "value": 25},
26: {"name": "cure light wounds", "value": 25},
28: {"name": "curse water", "value": 50},
30: {"name": "deathwatch", "value": 25},
32: {"name": "detect animals or plants", "value": 25},
35: {"name": "detect chaos/evil/good/law", "value": 25},
37: {"name": "detect snares and pits", "value": 25},
39: {"name": "detect undead", "value": 25},
41: {"name": "divine favor", "value": 25},
43: {"name": "doom", "value": 25},
48: {"name": "endure elements", "value": 25},
50: {"name": "entangle", "value": 25},
52: {"name": "entropic shield", "value": 25},
54: {"name": "faerie fire", "value": 25},
56: {"name": "goodberry", "value": 25},
58: {"name": "hide from animals", "value": 25},
60: {"name": "hide from undead", "value": 25},
62: {"name": "inflict light wounds", "value": 25},
64: {"name": "jump", "value": 25},
66: {"name": "longstrider", "value": 25},
68: {"name": "magic fang", "value": 25},
72: {"name": "magic stone", "value": 25},
74: {"name": "magic weapon", "value": 25},
78: {"name": "obscuring mist", "value": 25},
80: {"name": "pass without trace", "value": 25},
82: {"name": "produce flame", "value": 25},
86: {"name": "protection from chaos/evil/good/law", "value": 25},
88: {"name": "remove fear", "value": 25},
90: {"name": "sanctuary", "value": 25},
92: {"name": "shield of faith", "value": 25},
94: {"name": "shillelagh", "value": 25},
96: {"name": "speak with animals", "value": 25},
98: {"name": "summon monster I", "value": 25},
100: {"name": "summon nature's ally I", "value": 25},
},

"divine_2": {
1: {"name": "animal messenger", "value": 150},
2: {"name": "animal trance", "value": 150},
4: {"name": "augury", "value": 175},
6: {"name": "barkskin", "value": 150},
9: {"name": "bear's endurance", "value": 150},
12: {"name": "bull's strength", "value": 150},
14: {"name": "calm emotions", "value": 150},
17: {"name": "cat's grace", "value": 150},
18: {"name": "chill metal", "value": 150},
20: {"name": "consecrate", "value": 200},
24: {"name": "cure moderate wounds", "value": 150},
26: {"name": "darkness", "value": 150},
27: {"name": "death knell", "value": 150},
30: {"name": "delay poison", "value": 150},
32: {"name": "desecrate", "value": 200},
35: {"name": "eagle's splendor", "value": 150},
37: {"name": "enthrall", "value": 150},
39: {"name": "find traps", "value": 150},
40: {"name": "fire trap", "value": 175},
42: {"name": "flame blade", "value": 150},
44: {"name": "flaming sphere", "value": 150},
46: {"name": "fog cloud", "value": 150},
47: {"name": "gentle repose", "value": 150},
48: {"name": "gust of wind", "value": 150},
49: {"name": "heat metal", "value": 150},
51: {"name": "hold animal", "value": 150},
54: {"name": "hold person", "value": 150},
56: {"name": "inflict moderate wounds", "value": 150},
58: {"name": "make whole", "value": 150},
61: {"name": "owl's wisdom", "value": 150},
62: {"name": "reduce animal", "value": 150},
64: {"name": "remove paralysis", "value": 150},
67: {"name": "resist energy", "value": 150},
70: {"name": "restoration, lesser", "value": 150},
72: {"name": "shatter", "value": 150},
74: {"name": "shield other", "value": 150},
76: {"name": "silence", "value": 150},
77: {"name": "snare", "value": 150},
78: {"name": "soften earth and stone", "value": 150},
80: {"name": "sound burst", "value": 150},
81: {"name": "speak with plants", "value": 150},
83: {"name": "spider climb", "value": 150},
85: {"name": "spiritual weapon", "value": 150},
86: {"name": "status", "value": 150},
88: {"name": "summon monster II", "value": 150},
90: {"name": "summon nature's ally II", "value": 150},
92: {"name": "summon swarm", "value": 150},
93: {"name": "tree shape", "value": 150},
95: {"name": "undetectable alignment", "value": 150},
97: {"name": "warp wood", "value": 150},
98: {"name": "wood shape", "value": 150},
100: {"name": "zone of truth", "value": 150},
},

"divine_3": {
2: {"name": "animate dead", "value": 625},
4: {"name": "bestow curse", "value": 375},
6: {"name": "blindness/deafness", "value": 375},
8: {"name": "call lightning", "value": 375},
10: {"name": "contagion", "value": 375},
12: {"name": "continual flame", "value": 425},
14: {"name": "create food and water", "value": 375},
18: {"name": "cure serious wounds", "value": 375},
19: {"name": "darkvision", "value": 375},
21: {"name": "daylight", "value": 375},
23: {"name": "deeper darkness", "value": 375},
25: {"name": "diminish plants", "value": 375},
27: {"name": "dispel magic", "value": 375},
29: {"name": "dominate animal", "value": 375},
31: {"name": "glyph of warding", "value": 575},
32: {"name": "heal mount", "value": 375},
34: {"name": "helping hand", "value": 375},
36: {"name": "inflict serious wounds", "value": 375},
38: {"name": "invisibility purge", "value": 375},
40: {"name": "locate object", "value": 375},
46: {"name": "magic circle against chaos/evil/good/law", "value": 375},
48: {"name": "magic fang, greater", "value": 375},
50: {"name": "magic vestment", "value": 375},
52: {"name": "meld into stone", "value": 375},
55: {"name": "neutralize poison", "value": 375},
57: {"name": "obscure object", "value": 375},
59: {"name": "plant growth", "value": 375},
62: {"name": "prayer", "value": 375},
64: {"name": "protection from energy", "value": 375},
66: {"name": "quench", "value": 375},
69: {"name": "remove blindness/deafness", "value": 375},
71: {"name": "remove curse", "value": 375},
73: {"name": "remove disease", "value": 375},
76: {"name": "searing light", "value": 375},
78: {"name": "sleet storm", "value": 375},
80: {"name": "snare", "value": 375},
83: {"name": "speak with dead", "value": 375},
85: {"name": "speak with plants", "value": 375},
87: {"name": "spike growth", "value": 375},
89: {"name": "stone shape", "value": 375},
91: {"name": "summon monster III", "value": 375},
93: {"name": "summon nature's ally III", "value": 375},
96: {"name": "water breathing", "value": 375},
98: {"name": "water walk", "value": 375},
100: {"name": "wind wall", "value": 375},
},

"divine_4": {
5: {"name": "air walk", "value": 700},
7: {"name": "antiplant shell", "value": 700},
9: {"name": "blight", "value": 700},
11: {"name": "break enchantment", "value": 700},
13: {"name": "command plants", "value": 700},
15: {"name": "control water", "value": 700},
21: {"name": "cure critical wounds", "value": 700},
26: {"name": "death ward", "value": 700},
31: {"name": "dimensional anchor", "value": 700},
34: {"name": "discern lies", "value": 700},
37: {"name": "dismissal", "value": 700},
39: {"name": "divination", "value": 725},
42: {"name": "divine power", "value": 700},
47: {"name": "freedom of movement", "value": 700},
49: {"name": "giant vermin", "value": 700},
51: {"name": "holy sword", "value": 700},
54: {"name": "imbue with spell ability", "value": 700},
57: {"name": "inflict critical wounds", "value": 700},
60: {"name": "magic weapon, greater", "value": 700},
62: {"name": "nondetection", "value": 750},
64: {"name": "planar ally, lesser", "value": 1200},
67: {"name": "poison", "value": 700},
69: {"name": "reincarnate", "value": 700},
71: {"name": "repel vermin", "value": 700},
76: {"name": "restoration", "value": 800},
78: {"name": "rusting grasp", "value": 700},
81: {"name": "sending", "value": 700},
85: {"name": "spell immunity", "value": 700},
87: {"name": "spike stones", "value": 700},
90: {"name": "summon monster IV", "value": 700},
93: {"name": "summon nature's ally IV", "value": 700},
98: {"name": "tongues", "value": 700},
100: {"name": "tree stride", "value": 700},
},

"divine_5": {
3: {"name": "animal growth", "value": 1125},
5: {"name": "atonement", "value": 3625},
6: {"name": "awaken", "value": 2375},
9: {"name": "baleful polymorph", "value": 1125},
13: {"name": "break enchantment", "value": 1125},
16: {"name": "call lightning storm", "value": 1125},
20: {"name": "command, greater", "value": 1125},
21: {"name": "commune", "value": 1625},
22: {"name": "commune with nature", "value": 1125},
24: {"name": "control winds", "value": 1125},
30: {"name": "cure light wounds, mass", "value": 1125},
34: {"name": "dispel chaos/evil/good/law", "value": 1125},
38: {"name": "disrupting weapon", "value": 1125},
41: {"name": "flame strike", "value": 1125},
43: {"name": "hallow", "value": 6125},
46: {"name": "ice storm", "value": 1125},
49: {"name": "inflict light wounds, mass", "value": 1125},
52: {"name": "insect plague", "value": 1125},
53: {"name": "mark of justice", "value": 1125},
56: {"name": "plane shift", "value": 1125},
58: {"name": "raise dead", "value": 6125},
61: {"name": "righteous might", "value": 1125},
63: {"name": "scrying", "value": 1125},
66: {"name": "slay living", "value": 1125},
69: {"name": "spell resistance", "value": 1125},
71: {"name": "stoneskin", "value": 1375},
74: {"name": "summon monster V", "value": 1125},
77: {"name": "summon nature's ally V", "value": 1125},
78: {"name": "symbol of pain", "value": 2125},
79: {"name": "symbol of sleep", "value": 2125},
82: {"name": "transmute mud to rock", "value": 1125},
85: {"name": "transmute rock to mud", "value": 1125},
89: {"name": "true seeing", "value": 1375},
91: {"name": "unhallow", "value": 6125},
94: {"name": "wall of fire", "value": 1125},
97: {"name": "wall of stone", "value": 1125},
100: {"name": "wall of thorns", "value": 1125},
},

"divine_6": {
3: {"name": "animate objects", "value": 1650},
6: {"name": "antilife shell", "value": 1650},
9: {"name": "banishment", "value": 1650},
13: {"name": "bear's endurance, mass", "value": 1650},
16: {"name": "blade barrier", "value": 1650},
20: {"name": "bull's strength, mass", "value": 1650},
24: {"name": "cat's grace, mass", "value": 1650},
25: {"name": "create undead", "value": 1650},
29: {"name": "cure moderate wounds, mass", "value": 1650},
33: {"name": "dispel magic, greater", "value": 1650},
37: {"name": "eagle's splendor, mass", "value": 1650},
40: {"name": "find the path", "value": 1650},
43: {"name": "fire seeds", "value": 1650},
44: {"name": "forbiddance", "value": 4650},
45: {"name": "geas/quest", "value": 1650},
46: {"name": "glyph of warding, greater", "value": 1650},
49: {"name": "harm", "value": 1650},
52: {"name": "heal", "value": 1650},
55: {"name": "heroes' feast", "value": 1650},
58: {"name": "inflict moderate wounds, mass", "value": 1650},
61: {"name": "ironwood", "value": 1650},
62: {"name": "liveoak", "value": 1650},
65: {"name": "move earth", "value": 1650},
69: {"name": "owl's wisdom, mass", "value": 1650},
71: {"name": "planar ally", "value": 2400},
74: {"name": "repel wood", "value": 1650},
77: {"name": "spellstaff", "value": 1650},
80: {"name": "stone tell", "value": 1650},
83: {"name": "summon monster VI", "value": 1650},
86: {"name": "summon nature's ally VI", "value": 1650},
87: {"name": "symbol of fear", "value": 2650},
88: {"name": "symbol of persuasion", "value": 6650},
91: {"name": "transport via plants", "value": 1650},
94: {"name": "undeath to death", "value": 2150},
97: {"name": "wind walk", "value": 1650},
100: {"name": "word of recal", "value": 1650},
},

"divine_7": {
5: {"name": "animate plants", "value": 2275},
9: {"name": "blasphemy", "value": 2275},
14: {"name": "changestaff", "value": 2275},
16: {"name": "control weather", "value": 2275},
21: {"name": "creeping doom", "value": 2275},
27: {"name": "cure serious wounds, mass", "value": 2275},
32: {"name": "destruction", "value": 2275},
36: {"name": "dictum", "value": 2275},
41: {"name": "ethereal jaunt", "value": 2275},
45: {"name": "holy word", "value": 2275},
50: {"name": "inflict serious wounds, mass", "value": 2275},
55: {"name": "refuge", "value": 3775},
60: {"name": "regenerate", "value": 2275},
65: {"name": "repulsion", "value": 2275},
69: {"name": "restoration, greater", "value": 4775},
71: {"name": "resurrection", "value": 12275},
76: {"name": "scrying, greater", "value": 2275},
81: {"name": "summon monster VII", "value": 2275},
85: {"name": "summon nature's ally VII", "value": 2275},
90: {"name": "sunbeam", "value": 2275},
91: {"name": "symbol of stunning", "value": 7275},
92: {"name": "symbol of weakness", "value": 7275},
97: {"name": "transmute metal to wood", "value": 2275},
100: {"name": "word of chaos", "value": 2275},
},

"divine_8": {
4: {"name": "animal shapes", "value": 3000},
10: {"name": "antimagic field", "value": 3000},
13: {"name": "cloak of chaos", "value": 3000},
17: {"name": "control plants", "value": 3000},
20: {"name": "create greater undead", "value": 3600},
27: {"name": "cure critical wounds, mass", "value": 3000},
32: {"name": "dimensional lock", "value": 3000},
36: {"name": "discern location", "value": 3000},
41: {"name": "earthquake", "value": 3000},
45: {"name": "finger of death", "value": 3000},
49: {"name": "fire storm", "value": 3000},
52: {"name": "holy aura", "value": 3000},
56: {"name": "inflict critical wounds, mass", "value": 3000},
60: {"name": "planar ally, greater", "value": 5500},
65: {"name": "repel metal or stone", "value": 3000},
69: {"name": "reverse gravity", "value": 3000},
72: {"name": "shield of law", "value": 3000},
76: {"name": "spell immunity, greater", "value": 3000},
80: {"name": "summon monster VIII", "value": 3000},
84: {"name": "summon nature's ally VIII", "value": 3000},
89: {"name": "sunburst", "value": 3000},
91: {"name": "symbol of death", "value": 8000},
93: {"name": "symbol of insanity", "value": 8000},
96: {"name": "unholy aura", "value": 3000},
100: {"name": "whirlwind", "value": 3000},
},

"divine_9": {
4: {"name": "antipathy", "value": 3825},
7: {"name": "astral projection", "value": 4870},
13: {"name": "elemental swarm", "value": 3825},
19: {"name": "energy drain", "value": 3825},
25: {"name": "etherealness", "value": 3825},
31: {"name": "foresight", "value": 3825},
37: {"name": "gate", "value": 8825},
46: {"name": "heal, mass", "value": 3825},
53: {"name": "implosion", "value": 3825},
55: {"name": "miracle", "value": 28825},
61: {"name": "regenerate", "value": 3825},
66: {"name": "shambler", "value": 3825},
72: {"name": "shapechange", "value": 3825},
77: {"name": "soul bind", "value": 3825},
83: {"name": "storm of vengeance", "value": 3825},
89: {"name": "summon monster IX", "value": 3825},
95: {"name": "summon nature's ally IX", "value": 3825},
99: {"name": "sympathy", "value": 5325},
100: {"name": "true resurrection", "value": 28825},
},

}


#-----------------------------------------------------------------------
#------ Generate Scrolls (Table 7-20 - 7-24, Page 238) -----------------
#-----------------------------------------------------------------------

def GetOneSpell(s_type, s_level):

    s_key = "%s_%d" % (string.lower(s_type), s_level)

    if all_scrolls[s_key]:
        dct_level = all_scrolls[s_key]

        percentage_roll = crDice.RollPercentage()[1]

        for ref in sorted(dct_level.keys()):
            if percentage_roll <= ref:
                name = "%s" % (dct_level[ref]["name"])
                value = dct_level[ref]["value"]

                if "chaos/evil/good/law" in name:
                    percentage_roll_2 = crDice.RollPercentage()[1]

                    if percentage_roll_2 <= 25:
                        alignment = "chaos"
                    elif percentage_roll_2 <= 50:
                        alignment = "evil"
                    elif percentage_roll_2 <= 75:
                        alignment = "good"
                    elif percentage_roll_2 <= 100:
                        alignment = "law"

                    name = "%s %s" % (name[:-20], alignment)

                dct_scroll = {}
                dct_scroll["name"] = name
                dct_scroll["value"] = value

                return dct_scroll


def GetOneScroll(m_type, s_type=None, spell_only=False):

    minor = False
    medium = False
    major = False

    if string.upper(m_type) == "MINOR": minor = True
    elif string.upper(m_type) == "MEDIUM": medium = True
    elif string.upper(m_type) == "MAJOR": major = True

    percentage_roll_1 = crDice.RollPercentage()[1]

    if not s_type:
        if percentage_roll_1 <= 70:
            s_type = "arcane"
        elif percentage_roll_1 <= 100:
            s_type = "divine"

    percentage_roll_2 = crDice.RollPercentage()[1]

    if percentage_roll_2 <= 5 and minor:
        s_level = 0
    elif percentage_roll_2 <= 50 and minor:
        s_level = 1
    elif (percentage_roll_2 <= 95 and minor
    or percentage_roll_2 <= 5 and medium):
        s_level = 2
    elif (percentage_roll_2 <= 100 and minor
    or percentage_roll_2 <= 65 and medium):
        s_level = 3
    elif (percentage_roll_2 <= 95 and medium
    or percentage_roll_2 <= 5 and major):
        s_level = 4
    elif (percentage_roll_2 <= 100 and medium
    or percentage_roll_2 <= 50 and major):
        s_level = 5
    elif percentage_roll_2 <= 70 and major:
        s_level = 6
    elif percentage_roll_2 <= 85 and major:
        s_level = 7
    elif percentage_roll_2 <= 95 and major:
        s_level = 8
    elif percentage_roll_2 <= 100 and major:
        s_level = 9

    if minor:
        num_spells = crDice.RollDice(1, 3)[1]
    elif medium:
        num_spells = crDice.RollDice(1, 4)[1]
    elif major:
        num_spells = crDice.RollDice(1, 6)[1]

    dct_scroll = GetOneSpell(s_type, s_level)
    dct_scroll["name"] += " (scroll, %s, w/%d spell" % (s_type, num_spells)
    if num_spells > 1:
        dct_scroll["name"] += "s)"
    else:
        dct_scroll["name"] += ")"

    return dct_scroll


#-----------------------------------------------------------------------
#------ Format Text from a Scroll Table to Dictionary Format -----------
#-----------------------------------------------------------------------


def FormatScrollFile(file_name, gp, neg_gp_idx):


    f = open("scrolls\%s" % file_name, "r")
    lines = f.readlines()
    f.close()


    f2 = open("scrolls\%s-2.txt" % file_name[:-4], "w")

    text = ""
    text += '"%s": {\n' % (file_name[:-4])
    for line in lines:
        is_6_digit = False
        is_2_digit = False
        is_3_digit = False

        if line[2] == " " or line[3] == " ":
            if line[0] == "0":
                text += line[1]
                is_2_digit = True
            elif line[0:3] == "100":
                text += "100"
                is_3_digit = True
            else:
                text += line[0:2]
                is_2_digit = True

        elif line[3] == "0":
            text += line[4]

        elif "100" in line[0:7]:
            text += "100"
            is_6_digit = True

        else:
            text += line[3:5]

        start_idx = 6
        if is_2_digit: start_idx = 3
        elif is_3_digit: start_idx = 4
        elif is_6_digit: start_idx = 7

        text += ': {"name": "'
        text += line[start_idx:-(neg_gp_idx+1)]
        text += '", "value": %d},\n' % gp
    text += "},\n"

    f2.write(text)
    f2.close()


#***********************************************************************


if __name__ == "__main__":
    #~ crawler.Main()
    #~ FormatScrollFile("divine_9.txt", 3825, 9)
    for x in xrange(10000):
        scroll = GetOneScroll("Major")
        print scroll["name"], scroll["value"]

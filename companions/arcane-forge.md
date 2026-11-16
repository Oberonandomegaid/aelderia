<style>
/* ARCANE FORGE — Homebrewery v3, 5ePHB base with a forge house style */
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@500;700&display=swap');
.page h1 {font-family:'Cinzel',serif;font-weight:700;color:#5a2416;font-size:0.8cm;line-height:1.05em;letter-spacing:0.01em;}
.page h2 {font-family:'Cinzel',serif;font-weight:500;color:#7a3b1d;}
.page h3 {color:#7a3b1d;}
.page .note {border-left:3px solid #997448;}
.page table {font-size:0.88em;}
/* Chapter header band across both columns */
.page .chapterhead {border-bottom:2px solid #c9ad6a;padding-bottom:6px;margin-bottom:12px;}
.page .chapterhead p {font-size:0.33cm;line-height:1.3em;}
/* Forgemaster's note: purple GM advice box */
.page .forge {break-inside:avoid;background:#ece3f2;border:1px solid #bba6cf;border-left:5px solid #5b2d82;padding:7px 11px 6px;margin:8px 0 12px;}
.page .forge h5 {font-family:'Cinzel',serif;color:#4a2370;font-size:0.34cm;margin:0 0 3px;letter-spacing:0.03em;}
.page .forge p {font-size:0.3cm;line-height:1.28em;margin:0;}
.page .forge p + p {margin-top:4px;text-indent:0;}
/* Part divider caption */
.page .partcap {position:absolute;left:55px;bottom:80px;width:360px;padding:14px 20px 12px;background:rgba(30,16,34,0.80);border-left:5px solid #b58bd6;color:#f1e4c8;z-index:5;}
.page .partcap h5 {color:#d9bff0;margin:0;font-family:'Cinzel',serif;font-size:0.34cm;letter-spacing:0.14em;}
.page .partcap h2 {color:#f6ead2;margin:2px 0 6px;font-size:1.0cm;border:none;}
.page .partcap p {color:#e6d6b5;font-size:0.34cm;margin:0;}
/* In-column art: soft watercolour edge, fills the space it is given */
.page .art {break-inside:avoid;margin:6px 0 0;-webkit-mask-image:url(/assets/waterColorMasks/center/0001.webp);mask-image:url(/assets/waterColorMasks/center/0001.webp);-webkit-mask-size:118% 135%;mask-size:118% 135%;-webkit-mask-position:center;mask-position:center;-webkit-mask-repeat:no-repeat;mask-repeat:no-repeat;}
.page .art p {margin:0;height:100%;}
.page .art img {width:100%;height:100%;object-fit:cover;display:block;}
/* Right-hand column art */
.page .sideart {position:absolute;top:70px;right:45px;width:340px;height:880px;-webkit-mask-image:url(/assets/waterColorMasks/center/0002.webp);mask-image:url(/assets/waterColorMasks/center/0002.webp);-webkit-mask-size:118% 125%;mask-size:118% 125%;-webkit-mask-position:center;mask-position:center;-webkit-mask-repeat:no-repeat;mask-repeat:no-repeat;}
.page .sideart p {margin:0;height:100%;}
.page .sideart img {width:100%;height:100%;object-fit:cover;display:block;}
/* Legal notice on the title page */
.page .legal {position:absolute;left:55px;right:55px;bottom:40px;font-size:0.29cm;line-height:1.34em;color:#3a2a20;text-align:center;overflow-wrap:anywhere;word-break:break-word;}
.page .legal p {margin:0 0 5px;overflow-wrap:anywhere;word-break:break-word;}
.page .legal a {overflow-wrap:anywhere;word-break:break-word;}
.page .tightpage {display:none;}
.page:has(.tightpage) .columnWrapper p, .page:has(.tightpage) .columnWrapper li {line-height:1.13em;}
.page:has(.tightpage) .columnWrapper td {line-height:1.1em;}
.page:has(.tightpage) .columnWrapper h3 {margin-top:0.12cm;}

/* ARCANE FORGE — production art direction, 19 October 2026.
   All game text and page anchors retained. */
.page {color:#2e261f;width:210mm;height:297mm;}
.page h1 {font-size:.74cm;letter-spacing:.015em;}
.page h1,.page h1+h2 {column-span:all;}
.page h1+h2 {font-size:.47cm;line-height:1.15;margin-bottom:12px;letter-spacing:.025em;}
.page h3 {border-bottom:1px solid #ad8b57;padding-bottom:2px;}
.page table tr:nth-child(odd) {background-color:rgba(150,111,61,.11);}
.page table thead tr {background-color:rgba(106,62,32,.16);border-bottom:1px solid #9b7445;}
.page table th {color:#4e2d1f;}
.page .note {background:#eee4ce;border:1px solid #baa078;border-left:4px solid #997448;box-shadow:none;}
.page .forge {background:linear-gradient(115deg,#e8dfed,#f1eaf1);border:1px solid #b6a0be;border-left:4px solid #654571;box-shadow:0 2px 4px #513c2518;}
.page .forge h5 {color:#51305f;}
.page .footnote {color:#7c6141;font-size:8px;letter-spacing:.09em;}
.page .pageNumber {color:#6f482b;}
.page .art,.page .sideart {mask-size:105% 110%;-webkit-mask-size:105% 110%;}
.page .art img,.page .sideart img {object-position:center;}
.page .partcap {background:linear-gradient(110deg,rgba(28,20,30,.95),rgba(28,20,30,.72));border-left:3px solid #d3b475;border-top:1px solid #d3b475;border-bottom:1px solid #d3b475;bottom:65px;}
.page .partcap h5 {color:#dfc48b;}
.page .partcap h2 {font-size:.86cm;}
.page .titleArt {position:absolute;top:245px;left:120px;width:555px;height:655px;mask-image:url(/assets/waterColorMasks/center/0001.webp);mask-size:100% 100%;mask-repeat:no-repeat;}
.page .titleArt img {width:100%;height:100%;object-fit:cover;}
.page .titleArt p {margin:0;height:100%;}
.page .legal {font-size:10px;line-height:1.35;bottom:35px;}
.page .forgeSequence {position:absolute;right:43px;top:180px;width:345px;}
.page .forgeSequence .art {margin-bottom:35px;}
.page .storyPair {position:absolute;right:40px;top:185px;width:350px;}
.page .storyPair .art {margin-bottom:18px;}
.page .workbenchPanorama {position:absolute;bottom:65px;left:65px;width:665px;height:190px;mask-image:url(/assets/waterColorMasks/center/0001.webp);mask-size:105% 120%;mask-position:center;}
.page .workbenchPanorama img {width:100%;height:100%;object-fit:cover;object-position:center 60%;}
.page .workbenchPanorama p {margin:0;height:100%;}
#p1 .coverShade {position:absolute;inset:0;z-index:-1;background:linear-gradient(180deg,#0d0907d9,transparent 36%,transparent 62%,#0d0907ed);}
#p1 h1 {font-family:'Cinzel',serif;font-size:1.62cm;letter-spacing:.04em;color:#f5e2b6;text-shadow:0 3px 5px #000;line-height:1.05;margin-top:35px;}
#p1 h2 {color:#f5e2b6;font-size:.43cm;text-shadow:0 2px 3px #000;letter-spacing:.12em;}
#p1 hr {border-color:#d5b97a;}
#p1 .banner {background:none;border:1px solid #c9aa65;box-shadow:none;transform:none;left:60px;right:60px;width:auto;padding:12px;text-align:center;color:#f3dfb7;font-family:'Cinzel',serif;font-size:.46cm;bottom:140px;}
#p1 .banner:before,#p1 .banner:after {display:none;}
#p1 .footnote {font-size:12px;color:#f4e8d2;line-height:1.35;letter-spacing:0;bottom:45px;}
#p2 h1 {font-size:1.18cm;letter-spacing:.07em;}
#p2 h2 {font-size:.38cm;letter-spacing:.17em;}
#p2 hr {border-color:#a77b3f;}
#p4 .toc h3 {border-bottom:none;}
#p43 table td {height:26px;border-bottom:1px solid #bba58177;}
#p44 table td {height:25px;border-bottom:1px solid #bba58177;}
#p62 {background:#19120e;}
#p62 .columnWrapper {background:linear-gradient(90deg,#17110beF,#17110bd9);padding:30px 23px;width:355px;height:auto;border:1px solid #bb965d;position:absolute;left:45px;top:70px;column-count:1;}
#p62 .columnWrapper p,#p62 .columnWrapper li {font-size:12px;line-height:1.4;color:#f4e8d4;}
#p62 .columnWrapper h5 {color:#e5c98f;font-family:'Cinzel',serif;font-size:19px;line-height:1.15;}
#p62 .columnWrapper hr {border-color:#cba96a;}

#p62 {background-image:url("https://raw.githubusercontent.com/Omegaoliverid/Arcane-Forge-/929584c986ec54a4163f99de0b38b8aff455d61a/af-45.jpg");background-size:cover;background-position:center;}

.page .art,.page .sideart {mask-size:160% 165%;-webkit-mask-size:160% 165%;}
.page table tbody tr:nth-child(odd) {background-color:rgba(150,111,61,.12);}
.page table tbody tr:nth-child(even) {background-color:transparent;}
.page h3 {break-after:avoid;}
.page h2 {font-family:'Cinzel',serif;}
.page .titleArt {mask-size:145% 140%;mask-position:center;}
.page .legal {width:auto!important;left:55px!important;right:55px!important;}
#p1 h2,#p2 h2 {font-family:'Cinzel',serif!important;font-size:.43cm!important;line-height:1.3!important;}
#p2 h1 {font-family:'Cinzel',serif!important;}
#p1 hr,#p2 hr {background-image:none!important;background:#bc965c;height:1px;border:0;}
#p29 .art {position:absolute;right:55px;bottom:70px;width:310px;height:280px!important;}
#p1 .footnote {width:auto;left:70px;right:70px;}

.page .art,.page .sideart,.page .titleArt,.page .workbenchPanorama {mask-image:url("https://raw.githubusercontent.com/Omegaoliverid/Arcane-Forge-/85f6f9ae3e15b84a8b4be68ded8c3645d26888e9/af-parchment-edge.png");-webkit-mask-image:url("https://raw.githubusercontent.com/Omegaoliverid/Arcane-Forge-/85f6f9ae3e15b84a8b4be68ded8c3645d26888e9/af-parchment-edge.png");mask-size:100% 100%;-webkit-mask-size:100% 100%;mask-position:center;mask-repeat:no-repeat;}

#p13 .art {height:auto!important;aspect-ratio:1448/1086;}

#p16 .art {height:auto!important;aspect-ratio:1448/1086;}

#p19 .art {height:auto!important;aspect-ratio:1448/1086;}

#p21 .art {height:auto!important;aspect-ratio:1448/1086;}

#p23 .art {height:auto!important;aspect-ratio:1448/1086;}

#p24 .art {height:auto!important;aspect-ratio:1672/941;}

#p25 .art {height:auto!important;aspect-ratio:1536/1024;}

#p30 .art {height:auto!important;aspect-ratio:1447/1087;}

#p32 .art {height:auto!important;aspect-ratio:1448/1086;}

#p34 .art {height:auto!important;aspect-ratio:1448/1086;}

#p38 .art {height:auto!important;aspect-ratio:1448/1086;}

#p40 .art {height:auto!important;aspect-ratio:1536/1024;}


/* Second production pass: balanced editorial panels and expansive art. */
.page .editorialText {column-count:2;column-gap:28px;column-fill:balance;}
.page .editorialText h3 {break-inside:avoid;break-after:avoid;}
.page .editorialText > .wide {column-span:all;}
.page .featureArt {position:relative!important;top:auto!important;right:auto!important;left:auto!important;width:100%!important;aspect-ratio:auto!important;margin:12px 0 0!important;}
.page .featureArt img {object-fit:cover;}

#p15 .binderStock {position:absolute;right:58px;bottom:60px;width:315px;height:360px;}
#p24 .art {position:absolute;right:55px;bottom:100px;width:310px;height:175px!important;aspect-ratio:auto!important;}
#p25 .art {position:absolute;right:55px;bottom:70px;width:310px;height:300px!important;aspect-ratio:auto!important;}
#p36 .art {position:absolute;right:55px;bottom:70px;width:310px;height:400px!important;}
#p12 .art {height:515px!important;}
#p18 .art {height:450px!important;}


#p34 .art {height:420px!important;aspect-ratio:auto;}

#p1 {background-color:#20180e;background-image:linear-gradient(180deg,#0d0907d9,transparent 36%,transparent 62%,#0d0907ed),url("https://raw.githubusercontent.com/Omegaoliverid/Arcane-Forge-/929584c986ec54a4163f99de0b38b8aff455d61a/af-01.jpg");background-size:cover;background-position:center;}
#p1 .coverShade {display:none;}
#p1:before,#p1:after {display:none!important;}

#p13 .featureArt {height:335px!important;}

#p16 .featureArt {height:332px!important;}

#p19 .featureArt {height:210px!important;}

#p21 .featureArt {height:235px!important;}

#p22 .featureArt {height:490px!important;}

#p23 .featureArt {height:250px!important;}

#p30 .featureArt {height:260px!important;}

#p38 .featureArt {height:290px!important;}

#p40 .featureArt {height:265px!important;}


/* Publication typography: keep detached tables and captions readable. */
.page table th, .page table td { overflow-wrap: break-word; }
.page table th { line-height: 1.15; }
.page .binder-stock table { table-layout: fixed; }
.page .binder-stock th:nth-child(1) { width: 34%; }
.page .binder-stock th:nth-child(2) { width: 10%; }
.page .binder-stock th:nth-child(3) { width: 14%; }
.page .binder-stock th:nth-child(4) { width: 9%; }
.page .binder-stock th:nth-child(5) { width: 14%; }
.page .binder-stock th:nth-child(6) { width: 19%; }
.page .binder-stock td, .page .binder-stock th { padding: 3px 4px; }
.page .footnote { font-size: 9px !important; letter-spacing: .06em; }
.page:has(.frontCover) h1, .page:has(.frontCover) h2 { text-shadow: none !important; }
.page#p83 .backpanel h5 { color: #6b4a2b !important; }
.page#p4 .ritual { grid-template-columns: repeat(2, 1fr); gap: 10px; }
.page#p4 .ritual .step { padding: 8px 10px; }
.page .tdtitle .tdtext:after { top: 540px !important; right: 40px !important; }
.page .scar:after { right: 15px !important; width: 18px !important; opacity: .35; }
.page#p61 .tagpanel h3 { font: normal 18px/1.25 'Crimson Pro', serif !important; }
.page#p20 p { text-indent: 0 !important; }
.page#p20 .optional-hopes { margin: 14px 0 !important; }
.page#p64 .evo h4 { color: #dbc596 !important; font-weight: 700 !important; }
.page#p2 .legal { line-height: 1.18 !important; font-size: 9px !important; }
.page#p61 .tagpanel { left: 37% !important; width: 56% !important; bottom: 60px !important; padding: 14px 18px !important; }
.page#p61 .tagpanel h3 { font-size: 16px !important; }
.page#p31 .pimg { clip-path: inset(0 0 2px 0); }
.page .zamp-inline { font: inherit !important; display: inline !important; }

</style>

{{frontCover}}

# ARCANE FORGE
## Unique Armour, Weapons & Accessories
___

{{banner FORGE YOUR STORY. CRAFT YOUR LEGACY.}}

{{footnote
An independent fifth-edition-compatible monster-harvesting and magical-crafting supplement. Player imagination, earned craftsmanship, and GM judgement at the heart of every creation.
}}




{{coverShade}}
\page
{{insideCover}}

# ARCANE FORGE
## Unique Armour, Weapons & Accessories
___

{{titleArt
![](https://raw.githubusercontent.com/Omegaoliverid/Arcane-Forge-/929584c986ec54a4163f99de0b38b8aff455d61a/af-02.jpg)
}}

{{legal
**Arcane Forge** is an independent fifth-edition-compatible supplement. It is not published by, endorsed by or affiliated with Wizards of the Coast.

This work includes material taken from the System Reference Document 5.1 (“SRD 5.1”) by Wizards of the Coast LLC and available at https://dnd.wizards.com/resources/systems-reference-document. The SRD 5.1 is licensed under the Creative Commons Attribution 4.0 International License available at https://creativecommons.org/licenses/by/4.0/legalcode.

Written and designed by Oberon & Omega. Illustrations: Oberon & Omega.

Publication edition · 31 October 2026.

Text and illustrations © 2026 Oberon & Omega. All rights reserved, except SRD 5.1 material, which remains under its licence.
}}

\page
{{wide,chapterhead
# THE CORE OF CRAFT

*Steel has a memory. Bone has a history. Every scale taken from a fallen dragon has a story to tell. A forger's gift is persuading these things to become something new.*

**Arcane Forge** adds monster harvesting, experimental equipment, family-based blueprints, Guild trials, and a lifelong crafting profession to fifth-edition fantasy campaigns. It is meant to reward an adventurous player who wants to make something personal rather than merely purchase the next magic sword.
}}

**This book is divided into three parts.** Give the **Forger's Guide** and **Forger's Field Guide** to players. The balance decisions, hidden outcomes, GM quick-reference sheets and adjudication material belong with the GM. Give new crafters the blank player tracker and starting rules. Share a found diary separately; reveal the twin-dagger reference and GM worksheet only when their discoveries belong in play. A GM may share as much or as little as suits the table.

{{forge
##### A word to the GM
The rules provide consistent starting points, **not permission to demand a specific magical benefit**. The player proposes a creation, the ingredients make possibilities plausible, you approve its rarity and potential, and the dice decide how well the crafter realises the ambition. When uncertain, ask what the player values most and offer a workable route rather than a flat rejection.
}}

**Edition:** Designed for fifth-edition play, with familiar 2014-style equipment and encounter terms. Some 2024 magic-item details differ. Compatibility with other game systems would require independent adaptation and testing.

**Rarity language:** Arcane Forge uses **Common, Uncommon, Rare, Very Rare, and Legendary**. Item rarity and professional rank are separate measures: a Master can work at more than one rarity. **A qualified Master may still create Very Rare and Legendary items, including a +3 weapon**; rank, meaningful crafting XP, trials, materials, binder access and the completed item's balance remain real requirements. Published fifth-edition item rarities are comparison points, not compulsory character-level gates.

{{note
##### The forger's promise
Craftspeople earn their skill through genuine practice, risk and invention. The rarity tables provide consistent guidance, while the GM may make deliberate exceptions for memorable creatures, extraordinary sources and compelling stories. Agree the risks and rewards **before** the work begins.
}}

{{sideart,top:217px,height:740px
![](https://raw.githubusercontent.com/Omegaoliverid/Arcane-Forge-/929584c986ec54a4163f99de0b38b8aff455d61a/af-03.jpg)
}}

{{footnote ARCANE FORGE | INTRODUCTION}}
{{pageNumber,auto}}

\page
{{toc,wide
# Contents

- ### [{{ Introduction: The Core of Craft}}{{ 3}}](#p3)
- ### [{{ Part One — For the Forger}}{{ 5}}](#p5)
  - #### [{{ The Forger's Guide}}{{ 6}}](#p6)
  - #### [{{ The Forger's Field Guide}}{{ 7}}](#p7)
- ### [{{ Part Two — Rules of the Forge}}{{ 9}}](#p10)
  - #### [{{ Harvesting Monster Parts}}{{ 10}}](#p11)
  - #### [{{ Made from Monsters}}{{ 11}}](#p12)
  - #### [{{ Weapon Material Quantities}}{{ 12}}](#p13)
  - #### [{{ The Language of Blueprints}}{{ 13}}](#p14)
  - #### [{{ Magical Ingredients & Binders}}{{ 14}}](#p15)
  - #### [{{ The Four Stages of Creation}}{{ 16}}](#p17)
  - #### [{{ Experience Changes the Roll}}{{ 18}}](#p19)
  - #### [{{ Three Possible Creations}}{{ 19}}](#p20)
  - #### [{{ Time at the Workbench}}{{ 20}}](#p21)
  - #### [{{ Ranks, XP & Specialisation}}{{ 21}}](#p22)
  - #### [{{ Guild Trials}}{{ 23}}](#p24)
  - #### [{{ Mentors & the Grandmaster Trial}}{{ 24}}](#p25)
  - #### [{{ Costs, Barter & Reputation}}{{ 25}}](#p26)
  - #### [{{ An Adventure in the Forge}}{{ 26}}](#p27)
- ### [{{ Part Three — GM Reference}}{{ 27}}](#p28)
  - #### [{{ GM Quick Reference 01: Magical Weapons}}{{ 28}}](#p29)
  - #### [{{ GM Quick Reference 02: Body Armour & Shields}}{{ 29}}](#p30)
  - #### [{{ GM Quick Reference 03: Accessories & Everything Else}}{{ 30}}](#p31)
  - #### [{{ GM Rules & Arbitration}}{{ 31}}](#p32)
    - [{{ 1. Judging rarity and overall power}}{{ 31}}](#p32)
    - [{{ 2. Weapon damage, accuracy and effects}}{{ 32}}](#p33)
    - [{{ 3. AC, mitigation and retaliation}}{{ 33}}](#p34)
    - [{{ 4. Unusual items, movement and utility}}{{ 34}}](#p35)
    - [{{ 5. Preparing outcomes and edge cases}}{{ 35}}](#p36)
  - #### [{{ The Monster Material Atlas}}{{ 36}}](#p37)
  - #### [{{ Example Creations}}{{ 37}}](#p38)
  - #### [{{ Legendary Inspirations}}{{ 38}}](#p39)
  - #### [{{ Reverse Engineering Legends}}{{ 39}}](#p40)
  - #### [{{ Dreams of Greater Magic}}{{ 40}}](#p41)
  - #### [{{ The Stories Behind the Materials}}{{ 41}}](#p42)
  - #### [{{ Final Rules at a Glance}}{{ 42}}](#p43)
- ### [{{ Record Sheets}}{{ 43}}](#p44)
  - #### [{{ Player Crafting Tracker}}{{ 43}}](#p44)
  - #### [{{ GM Worksheet}}{{ 44}}](#p45)
- ### [{{ The Diary of Tomas Brack}}{{ 46}}](#p47)
  - #### [{{ Light's Embrace & Shadow's Bane}}{{ 61}}](#p62)
}}

{{wide
{{note
##### How to use the book
For an everyday project, agree a finished item and make the appropriate check. For a new, memorable invention, optionally use **Three Possible Creations**: the GM writes three balanced possibilities before crafting, the player rolls the usual stages, and the item reveals its final nature. Nothing requires a three-card setup for routine work.
}}
}}

{{footnote ARCANE FORGE | CONTENTS}}
{{pageNumber,auto}}

\page
![For the Forger](https://raw.githubusercontent.com/Omegaoliverid/Arcane-Forge-/929584c986ec54a4163f99de0b38b8aff455d61a/af-05.jpg){position:absolute,top:0px,left:0px,width:100%,height:100%,object-fit:cover}

{{partcap
##### PART ONE
## For the Forger
*Duskclaw Vestments — made from duneshade prowler hide*
}}

\page
# THE FORGER'S GUIDE
## An old master's welcome

{{descriptive
*Well, well. Another bright-eyed initiate with a hammer and a dream. Welcome to the forge. Any fool can swing a sword; it takes skill to make one. And it takes something altogether rarer to forge a blade whose name will outlive its wielder.*

*Look at a monster and see more than a monster. Its hide may become your armour; its horn, the edge of your spear; its heart, the secret of an enchanted ring. But first you'll need to learn which end of the hammer to hold.*
}}

### 1. Hunt, harvest, gather

After a creature falls, name the parts you hope to recover. The GM decides what's anatomically possible, calls for suitable checks and awards the usable quantity. Keep track of the material, creature, rarity and any **Pristine** quality.

### 2. Learn the craft

A blueprint teaches you how to work an **item family** with a **material family**, up to a particular rarity. Learn metal swords rather than buying one blueprint for every conceivable metal sword. Guilds, masters, lost workshops and dangerous expeditions can teach you more.

### 3. Collect enough to build

**Crafting Units (CU)** describe amounts of usable metal, timber, leather, scales, bone and similar structural materials. A dagger needs fewer CU than a greatsword; a gilet needs fewer than a full suit of armour. Special magical organs and binders are counted separately. Consult the Field Guide.

### 4. Tell the GM what you want

*An axe that strikes Giants with thunder. A leather coat that refuses the point of a spear. Bracers that launch webs across a ravine.* Your idea matters. The GM will help decide what your knowledge, materials and intended rarity could achieve.

\column

### 5. Forge and risk it

New, difficult work usually uses **four crafting stages**. The result may be a success, a setback or a catastrophe. An extraordinary natural 20 can make a remarkable difference. Treasure placed on the forge is treasure placed at risk.

### 6. Earn your name

Learn new techniques, seek difficult projects, and qualify for a witnessed Guild or mentor trial. Become an **Initiate, Apprentice, Journeyman, Master** and finally a **Grandmaster**. Experience opens the door; your trial earns the title.

*And should a king ask for a sword one day? Perhaps you'll be famous enough to tell him to make an appointment.*

**FORGE YOUR STORY. CRAFT YOUR LEGACY.**

{{art,height:470px
![](https://raw.githubusercontent.com/Omegaoliverid/Arcane-Forge-/929584c986ec54a4163f99de0b38b8aff455d61a/af-06.jpg)
}}

{{footnote ARCANE FORGE | FORGER'S GUIDE}}
{{pageNumber,auto}}

\page
# THE FORGER'S FIELD GUIDE
## Keep this by your character sheet

### A. Harvest a useful part

1. Name the part and describe your approach.
2. Roll **d20 + relevant ability modifier + one applicable proficiency bonus**, as the GM directs. Do not add proficiency twice.
3. The GM says what you recover and how much.
4. Write down the source, rarity, condition and quantity.

| Creature CR | Material tier | Harvest DC |
|:--|:--|--:|
| 0–2 | Common | 10 |
| 3–6 | Uncommon | 15 |
| 7–12 | Rare | 20 |
| 13–16 | Very Rare | 23 |
| 17+ | Legendary | 25 |

**Pristine:** On a successful harvest check, a natural 20 or a final total at least 10 over the harvest DC makes the recovered component Pristine, increasing effective material rarity **one tier**, capped at Legendary: Rare becomes Very Rare; Very Rare becomes Legendary. It does not automatically add powers, enchantments or fix the final item's rarity.

### B. Count Crafting Units

| Usable material | CU |
|:--|--:|
| One standard 2 lb metal billet | 1 |
| One standard prepared timber billet | 1 |
| Small / Medium / Large usable scale or plate | 0.5 / 1 / 2 |
| Small / Medium / Large prepared hide | 4 / 8 / 16 |
| 0.05 square metres prepared cloth, hide, leather, silk | 1 |
| 2 lb usable bone, horn, tooth, stone or crystal | 1 |

An eye, gland, magical essence or venom dose may be a **special ingredient**, with no structural CU value. The GM decides whether your materials physically suit your project.

### C. Quick construction amounts

| Creation | CU |
|:--|--:|
| Dagger | 1 |
| Shortsword | 2 |
| Longsword | 3 |
| Greatsword | 5 |
| Medium helmet | 3 |
| Medium shield facing | 4 |
| Medium torso gilet | 12 |
| Medium complete suit | 30 |

These figures represent usable structural material, not finished AC, monetary value or guaranteed magical properties. Reinforcing an existing item generally needs **half its coverage CU**, rounded up.

### D. Before you begin

**Ask yourself:** What is it? What blueprint knowledge do I have? Which parts do I need, and is a binder appropriate or required? What am I hoping it will do? Do I have a suitable workshop and enough time?

**Record:** rank, crafting XP, specialisation, taught blueprints, inventory in CU, named magical ingredients, active project, finished recipes and maker's marks. Routine work needs materials and time even when your experience makes the roll simpler.

{{art,height:620px
![](https://raw.githubusercontent.com/Omegaoliverid/Arcane-Forge-/929584c986ec54a4163f99de0b38b8aff455d61a/af-07.jpg)
}}

{{footnote ARCANE FORGE | FIELD GUIDE}}
{{pageNumber,auto}}

\page
![](https://raw.githubusercontent.com/Omegaoliverid/Arcane-Forge-/929584c986ec54a4163f99de0b38b8aff455d61a/af-08.jpg){position:absolute,top:0px,left:0px,width:100%,height:100%,object-fit:cover}

\page
![Rules of the Forge](https://raw.githubusercontent.com/Omegaoliverid/Arcane-Forge-/929584c986ec54a4163f99de0b38b8aff455d61a/af-08.jpg){position:absolute,top:0px,left:0px,width:100%,height:100%,object-fit:cover}

{{partcap
##### PART TWO
## Rules of the Forge
*Skyclaw Blade — carved from a single blue dragon claw*
}}

\page
{{wide,chapterhead
# HARVESTING MONSTER PARTS
## Rules for the GM
}}

### Eligibility and checks

A creature normally must be dead before harvesting; circumstances and the creature's nature may alter this. Some magical bodies decay or vanish rapidly without preservation. The player names **which anatomical part** they want. Each distinct meaningful type of part may require a separate harvesting check; collecting twelve scales does not require twelve separate rolls.

Choose the most appropriate **Survival, Nature, Medicine**, or relevant tool check: smith's tools for suitable plates or ore-like remains, leatherworker's tools for hides, alchemist's supplies for glands and essences, poisoner's kit for venoms, and so on. A character adds proficiency **once**, not once for a skill and again for tools. If both relevant skill and relevant tools apply, the GM may grant advantage instead. One suitable helper may assist. Missing specialised tools when genuinely necessary imposes **–2**.

| CR | Tier | DC |
|:--|:--|--:|
| 0–2 | Common | 10 |
| 3–6 | Uncommon | 15 |
| 7–12 | Rare | 20 |
| 13–16 | Very Rare | 23 |
| 17+ | Legendary | 25 |

**Success:** Recover a reasonable amount of that usable component, determined by the GM. **Failure:** The attempted part is ruined; other parts aren't automatically spoiled. **Pristine:** On a successful harvest check, a natural 20 or a check result at least 10 above the DC makes the recovered material Pristine, upgrading its **effective material rarity one tier**, up to Legendary. A Pristine Rare part is Very Rare, a Pristine Very Rare part is Legendary, and a Pristine Legendary part remains Legendary. It does not automatically create a magic item or extra power.

**CR is a default, never an absolute treasure ceiling.** The GM can award a uniquely empowered CR 9 campaign boss a Very Rare or Legendary heart when a singular narrative cause justifies it, without making every scale and claw Legendary. Such an exceptional piece might come from an ancient curse, implanted relic, planar accident or extraordinary organ. The GM should establish the treasure intentionally rather than upgrading everything merely because the fight felt long. Characters may also **buy, barter, commission, steal, discover or be gifted** parts; they need not kill the source creature themselves. Storytelling flexibility is permitted, but consistent baseline bands keep ordinary rewards predictable.

**GM discretion:** DC 23 offers an intermediate harvesting challenge for CR 13–16 creatures. A GM may apply a harder or easier DC when the anatomy, hazards or story justify it; such a choice changes the challenge, not the default material-rarity category.

### Yield and anatomy

The GM decides how much of each part exists and how much survived the fight. Rolling a **d10** for usable claws or a **d12** for scales can be entertaining, but neither is a mandatory quantity rule. Counts mean **usable recovered pieces**, not every part that ever existed on the creature. Parties decide how to share harvests.

For a homebrew monster without CR, **the GM who created it assigns the closest CR band**, comparing its threat with existing creatures. Even with a printed CR, a uniquely empowered creature may carry an **exceptional, specifically identified higher-tier part** if the story warrants it. The GM decides the part and the reason; CR is a default, not an absolute prohibition or automatic magical power.

### Creature material examples

| Component | Plausible construction or use |
|:--|:--|
| Tooth, claw, horn, talon | Blade, piercing tip, hook, handle, magic accent |
| Hide, fur, skin, membrane | Leatherwork, garments, wraps, linings |
| Scales, shell, chitin, scutes | Shield facings, plates, hard reinforcement |
| Bone, tusk, cartilage | Structural pieces, ornament, magical focus |
| Tendon, sinew, web, silk | Bowstring, lashing, magical mechanism |
| Feather, whisker | Fletching, detection focus, ornament |
| Gland, blood, venom, eye, core | Individually measured magical ingredient or binder |

{{note
##### Optional: Monster core
For creatures whose body would swiftly dissolve or vanish, the GM may allow a timely extraction of a condensed essence. This is an alternative storytelling tool, not a mandatory rule stripping every magical creature of its normal harvestable anatomy.
}}

{{footnote ARCANE FORGE | HARVESTING}}
{{pageNumber,auto}}

\page
# MADE FROM MONSTERS
## One quantity language for every material

**Crafting Unit (CU)** measures *usable physical input*, not enchantment strength, AC, CR, market value or the number of magical abilities. The GM may adjust for unusual anatomy, shape, fit, density and design. Materials are recorded **after harvesting damage and preparation**, so there is no automatic second waste deduction.

### Standard material units

| Material | 1 CU represents |
|:--|:--|
| Iron, steel, alloy | **One 2 lb workable billet** (roughly 900 g) |
| Prepared timber | A suitable straight hardwood billet about 1 m × 3.5 cm × 3.5 cm |
| Bone, claw, horn, tooth, stone, crystal | 2 lb **usable structural** material |
| Hide, leather, cloth, monster silk | 0.05 m² prepared usable sheet material |
| Small scale or armour plate | 0.5 CU |
| Medium scale or armour plate | 1 CU |
| Large scale or armour plate | 2 CU |
| Small / Medium / Large prepared whole hide | 4 / 8 / 16 CU |
| Eyes, venom, organs, essences, glands | Magical ingredients, not automatically structural CU |

A standard timber billet is an **inventory unit**, not permission to join short scraps into an uninterrupted spear shaft or bow stave. Stone, wood, bone and metal are not universally interchangeable. The GM checks physical suitability.

### Armour coverage

| Armour part | Small wearer | Medium wearer |
|:--|--:|--:|
| Helmet or hood | 2 | 3 |
| Pair of pauldrons | 2 | 3 |
| Pair of bracers or gauntlets | 2 | 3 |
| Pair of greaves or boots | 3 | 4 |
| Shield facing | 3 | 4 |
| Torso gilet / sleeveless facing | 8 | 12 |
| Complete suit, including standard coverage | 20 | 30 |

For **full construction**, supply the full coverage CU plus suitable backing, straps, lining, joins and framework. For **reinforcing existing equipment**, supply half the corresponding coverage CU, rounding upward to a whole CU. A full suit **already includes ordinary constituent pieces**: do not add helm, pauldrons and gauntlets again to the full-suit total.

An exterior full plate, scale facing, flexible leather garment and complete metal harness do not all have the same mechanical armour statistics. Match the finished item to an appropriate fifth-edition armour type and its proper physical design. CU alone never transforms light armour into heavy plate.

{{art,height:650px
![](https://raw.githubusercontent.com/Omegaoliverid/Arcane-Forge-/929584c986ec54a4163f99de0b38b8aff455d61a/af-10.jpg)
}}

{{footnote ARCANE FORGE | MATERIALS}}
{{pageNumber,auto}}

\page
# WEAPON MATERIAL QUANTITIES
## Workable standards, not rigid recipes

{{wide
| Weapon / implement | Total CU | Typical structural inputs |
|:--|--:|:--|
| Dagger | 1 | 1 metal / suitable bone or horn |
| Shortsword | 2 | 2 metal |
| Longsword | 3 | 3 metal |
| Greatsword | 5 | 5 metal |
| Spear | 2 | 1 timber + 1 metal or suitable point |
| Handaxe | 2 | 1 metal + 1 timber |
| Battleaxe | 3 | 2 metal + 1 timber |
| Greataxe | 5 | 3 metal + 2 timber |
| Warhammer | 3 | 2 metal + 1 timber |
| Quarterstaff | 2 | 2 timber, continuous suitable length |
| Shortbow | 2 | Suitable bow timber plus string |
| Longbow | 3 | Suitable continuous stave plus string |
}}

Bowstrings, grips, rivets, leather lining, binding and finishing materials normally count as **supporting supplies** rather than an extra full CU unless the design makes them a major element. The GM may revise unusual weapons, ranged mechanisms and armour forms.

### Example: Frank's dragon-scale gilet

Frank harvested **13 usable Medium scales**. Each is 1 CU, so he has **13 CU**. A Medium torso gilet needs **12 CU** for full scale facing. Frank has enough, leaving 1 CU. Reinforcing an existing Medium leather torso facing needs **6 CU**. The player can begin with that, then add more scales later through a new crafting project.

### Mixed materials and evolving equipment

Suitable scales from different creatures may count together for *structural coverage*. They don't each automatically award another elemental resistance, AC enhancement or saving throw bonus. The player and GM can agree on **one strong property, multiple smaller properties or a new emergent property** whose power is balanced as a whole.

For example, fire-bearing red dragon scales and acid-bearing black dragon scales might inspire a brief **caustic steam** retaliation dealing **1d6 fire plus 1d6 acid**. The activation cost, saving throw, uses and item rarity are set by the GM. This is an **example**, not a default reward for mixing colours.

An existing item may be reinforced or upgraded repeatedly. Previously installed components count toward the construction where they remain useful; newly added components are counted normally. A **setback** leaves the original item intact even if new materials are lost; **catastrophe** risks the original item as well.

### Rarity, strength and appearance

Monster armour built entirely from rare dragon scales is not automatically statistically superior to excellent steel armour *infused* with those scales. The design, final rarity, construction knowledge, magical components and GM balance decision determine its mechanics.

{{art,height:410px
![](https://raw.githubusercontent.com/Omegaoliverid/Arcane-Forge-/929584c986ec54a4163f99de0b38b8aff455d61a/af-11.jpg)
}}

{{footnote ARCANE FORGE | MATERIALS}}
{{pageNumber,auto}}

\page
{{wide,editorialText
{{wide,chapterhead
# THE LANGUAGE OF BLUEPRINTS
## Reading a blueprint

A **standard blueprint** is the combination of **item family + structural material family + maximum rarity taught**. It covers sensible forms within that family and **all lower rarities**, but no higher. It does not independently teach every magical power a creature might provide. Knowledge of a blueprint does not raise a character's crafting rank.
}}

### Item families

**Weapons (eight):** Short Blades; Swords; Axes; Polearms; Blunt Weapons; Bows; Crossbows; Staves & Magical Implements.

**Armour (six):** Flexible Armour; Mail & Linked Armour; Plate & Scale Armour; Shields; Helmets & Headgear; Armoured Accessories.

**Other items (three):** Jewellery & Adornments; Clothing & Garments; Utility Trinkets.

### Standard structural material families

| Family | Illustrative members |
|:--|:--|
| Metal & Alloys | Iron, steel, bronze, mithral and other alloys |
| Bone, Horn & Natural Armour | Bone, tooth, claw, tusk, horn, scales, shell, chitin, scutes |
| Stone, Glass & Crystal | Obsidian, quartz, gem, glass, ceramic |
| Wood & Plant | Timber, bark, vines, roots, petrified wood |
| Hide, Leather & Textiles | Fur, cured hide, cloth, leather, feathers, webbing, silk, sinew |

Not every pairing is physically sensible. **A stone bow** is not automatically possible because Stone is a material family; GM approval of the actual form is still required.

\column

### Blueprint pricing — established guide

| Maximum blueprint tier | Price |
|:--|--:|
| Common | 40 gp |
| Uncommon | 200 gp |
| Rare | 1,000 gp |
| Very Rare | **2,500 gp** |
| Legendary | 5,000 gp |

These are **knowledge prices**, not the cost of constructing or magically empowering an item. Availability is determined by the world: routine training might be purchasable locally, Rare knowledge may be Guild-guarded or quest-earned, Very Rare is the province of established specialists, and Legendary instruction may never be sold openly. Learning a higher blueprint replaces the need to track lower copies for the same item/material family.

{{note
##### Specialist Organics — separate from the standard blueprint catalogue
Truly functioning organic machinery—living spinnerets, responsive ooze tissues, breathing coral and other biological mechanisms—may require a specialist tutor rather than a normal blueprint. A GM determines what **specific materials**, **equipment categories** and **maximum rarity** that tutor teaches. Training acts as suitable knowledge across the taught scope and lower rarities. Without it, experimental work may still be attempted with the normal no-blueprint disadvantage. There is no mandatory catalogue or fixed specialist price.
}}
}}

{{wide,art,featureArt,height:305px
![](https://raw.githubusercontent.com/Omegaoliverid/Arcane-Forge-/929584c986ec54a4163f99de0b38b8aff455d61a/af-12.jpg)
}}{{footnote ARCANE FORGE | BLUEPRINTS}}
{{pageNumber,auto}}

\page
# MAGICAL INGREDIENTS & BINDERS
## The design belongs to the player

A physical blueprint teaches **how to make the object**. A harvested organ, shard, bone, enchanted ore or other substance suggests **what magic the item could express**. A **binder** is a stabilising magical reagent that can hold, channel or elevate that potential. The GM approves the finished item's **total rarity and powers** before any work starts. No separate mandatory enchantment blueprint is required.

### When is a binder required?

| Intended magic item | Binder guidance |
|:--|:--|
| Mundane item | **Never required**: ordinary smithing, leatherwork and carpentry do not need one. |
| Common / minor magic | Normally **optional** when the materials and small effect make sense; GM discretion. |
| Uncommon | Recommended for ambitious enchantments; may be omitted if the source already supports a modest power. |
| Rare | **Normally required if lower-tier ingredients are being elevated** to support a Rare magical result; otherwise GM discretion. |
| Very Rare | **Normally required**, especially where lesser materials must sustain stronger magic. |
| Legendary | **Normally required**, with the rare exception of a singular self-stabilising legendary source approved by the GM. |

**One suitable binder ordinarily serves the agreed item as a whole**, not one binder for each descriptive flourish or magical property. A binder should typically match the **intended finished item's rarity** where required; it does **not** itself grant that rarity or add powers. The GM considers the entire design, other ingredients and the crafter's capability. **Crafting DC, time, blueprint and rank rules use the item's final rarity**, including whenever the binder helps elevate lesser materials.

### Where binders come from

- **Harvest and exploration:** a distinctive organ, planar condensation, living resin, magical crystal or well-preserved monster core may qualify. Use the normal harvest framework where applicable; no mandatory second binder-loot roll.
- **Trade and Guilds:** ordinary reagent dealers supply small binders; specialist enchanters and Guilds trade, commission or occasionally sell rarer ones. Price does not guarantee availability.
- **Artisan preparation:** an appropriate specialist can refine supplied magical components into a usable binder, spending actual work hours and other inputs. This is **not** an automatic free upgrade of a material's effective rarity. Apply an appropriate tool check only when the preparation is uncertain; it need not trigger another obligatory four-stage sequence.
- **Story rewards:** a magical spring, old ruin, recovered formula, grateful patron, planar crossing, fey bargain or long quest can grant a binder without forcing the party to defeat a particular creature.

### Optional price and market guide

{{wide
| Binder quality | Illustrative market asking price | Likely market access |
|:--|--:|:--|
| Common | 5–25 gp | Usually available in settlements with magic trade |
| Uncommon | 25–150 gp | Skilled alchemists, Guild shops, local commissions |
| Rare | 250–1,000 gp | Specialist suppliers, limited stock or adventure rewards |
| Very Rare | 2,000–8,000 gp | Major Guilds, patrons, distant trade or exceptional discovery |
| Legendary | 10,000 gp or more; often not for sale | Singular adventures, unique sources and extraordinary bargains |
}}

Prices are **per useful binder**, not a fixed creature-part valuation, crafting-unit replacement or automatic surcharge. Characters supplying one via harvesting have already paid in risk and opportunity; **do not charge them its retail value a second time**. Supply is finite. A Guild may refuse a sale, offer barter, ask a favour or set a quest. For recurring work, the GM should track how many suitable binders can actually be acquired rather than permit infinite inexpensive production. These are illustrative asking prices for an ordinary high-fantasy market, **not fixed prices, guaranteed availability or published fifth-edition values**; adjust them for the campaign economy.

{{art,height:190px
![](https://raw.githubusercontent.com/Omegaoliverid/Arcane-Forge-/929584c986ec54a4163f99de0b38b8aff455d61a/af-13.jpg)
}}

{{footnote ARCANE FORGE | MAGICAL DESIGN}}
{{pageNumber,auto}}

\page
{{wide
### Guild binder stock — suggested monthly availability
}}

{{wide,binder-stock
| Settlement and Guild market | Common | Uncommon | Rare | Very Rare | Legendary |
|:--|--:|--:|--:|--:|:--|
| Small town | 2–6 | 0–2 | 0 | 0 | 0 |
| Large town | 5–10 | 2–5 | 0–1 | 0 | 0 |
| City | 10–20 | 5–10 | 1–3 | 0–1 | 0 |
| Major magical capital | 20+ | 10+ | 3–6 | 1–2 | Special acquisition |
}}

These figures describe the **total suitable stock accessible through the settlement's magical trade and Guild network in a typical month**, not the inventory of every individual merchant. Stock is an opportunity to negotiate or commission, **not a guaranteed sale**. Replenishment depends on genuine imports, artisan preparation, harvesting and adventure events: it does not automatically refill after 30 days in a depleted or isolated market. Legendary binders may be acquired by auction, barter, patrons or quests without appearing on ordinary shelves. The GM can alter these quantities freely for high- or low-magic worlds. A crafter may still obtain a binder from an extraordinary creature, a treasure hoard or a narrative reward even when local market stock is zero.

### Let the material suggest its magic

| Binder inspiration | Suggested magical direction |
|:--|:--|
| Elemental Binding Coil | Fire, cold, storms and elemental force |
| Basilisk Gallstone | Petrification, restraint and flesh-change |
| Voidglass Sliver | Space, illusion and displacement |
| Moonstone Pearl | Dreams, emotion and illusion |
| Ancient Amber / living resin | Growth, restraint and nature |
| Psionic Foci Crystal | Memory, thought and telepathy |
| Infernal Binding Ink | Curses, contracts and infernal workings |
| Feydust Resin | Glamour, charm and trickery |
| Time-Scarred Vellum | Preservation, time and foresight |
| Planar Convergence Shard | Exceptional planar crossings |

A name doesn't determine a permanent price, CR or power score. One of these might be a lesser or stronger exemplar depending on provenance and preparation. The player and GM can invent other binders; their function must follow from the story and be judged before crafting begins.

{{forge
##### The Rule of the Story
An Uncommon monster part can inspire a Rare cloak when supplemented by a suitable Rare binder and a fair complete design; it cannot automatically become a Legendary relic merely by adding an expensive crystal. As a useful starting point, a binder most readily bridges **one tier** beyond the strongest pertinent magical source. Larger leaps require additional exceptional components or clear story justification. This is GM guidance, not a compulsory ladder or a formula that automatically grants power.
}}


### Judge the complete design

The GM and player agree on the **whole item** and its reasonable potential. A dragon fang, spider gland and fey thread do not automatically grant three full powers. They may inspire a single combined ability or several smaller abilities if the entire item fits the intended rarity.

**Potential GM questions:**

- What do you most want the item to accomplish?
- Does it work against every creature or one specific threat?
- Is the power always available or limited by action, charges, rests, range or duration?
- Does it duplicate a spell or add extra turns, attacks or unrestricted movement?
- What does the item's other equipment do, and can these bonuses accumulate?

### Bought bases and existing magic items

An already-made weapon, armour suit or accessory can be infused or upgraded. The original item's structure does not need to be purchased or forged again. The GM assesses the **resulting combined rarity**, time, **binder if called for**, and added materials before work starts. No automatic entitlement to retain every previous magical benefit exists when the intended new effect would exceed the final rarity.

{{art,binderStock
![](https://raw.githubusercontent.com/Omegaoliverid/Arcane-Forge-/08012b577047a13dd18bf698cb84cd5106d59595/af-14.jpg)
}}

{{footnote ARCANE FORGE | MAGICAL DESIGN}}
{{pageNumber,auto}}

\page
{{wide,editorialText
# THE FOUR STAGES OF CREATION
## One project. Four rolls. A real risk.

For the first attempt at a challenging or unfamiliar **specific creation**, the crafter makes **four d20 checks** using relevant abilities and tools. This is **one integrated project**; magical infusion occurs during the stages rather than requiring an additional independent enchanting sequence.

The GM chooses sensible stages for the project. Examples:

{{wide
| Item | Stage 1 | Stage 2 | Stage 3 | Stage 4 |
|:--|:--|:--|:--|:--|
| Metal weapon | Prepare and heat | Shape and forge | Temper and align | Finish and bind magic |
| Leather armour | Prepare and cut | Fit and shape | Stitch and reinforce | Treat and weave magic |
| Jewellery | Prepare components | Form the setting | Set and engrave | Seal and bind magic |
| Bought item infusion | Prepare the base | Infuse materials | Stabilise effects | Complete final binding |
}}

The stages can be narrated differently. Each uses **d20 + suitable ability modifier + one applicable proficiency bonus + approved Arcane Forge specialisation**. Some stages may call for different attributes/tools. Don't add proficiency multiple times to one check. A GM may vary staging to suit the character's inventiveness, without imposing more than the agreed four integrated rolls.

### Stage difficulty

| Intended item | DC per stage | Required four-stage total |
|:--|--:|--:|
| Common | 12 | 48 |
| Uncommon | 14 | 56 |
| Rare | 17 | 68 |
| Very Rare | **18** | **72** |
| Legendary | 20 | 80 |
| Bespoke Grandmaster Legendary masterpiece | 25 | 100 |

**Calculate success from the sum of all four modified stage results**, not by forcing each stage to pass separately. This allows a brilliant recovery during a difficult project. An exceptional bespoke Legendary masterpiece remains **DC 25 / total 100** and does **not** also take an above-rank penalty when attempted by a properly promoted Master; it is still Legendary.

### Distinct difficulties that can stack

- **No suitable blueprint or qualifying organic-specialist training:** roll **each stage at disadvantage**. Same DC otherwise.
- **One item rarity above the crafter's current rank capability:** **+5 to each stage DC**, so the four-stage total increases by **20**. This is intentional and challenging.
- **Both apply:** disadvantage on every stage **and** +5 to each stage DC. Disadvantage is not applied twice.
- Crafting more than one rarity above the current capability is **not a standard permitted attempt**; the GM may create extraordinary story exceptions, not an automatic access rule.

**Example:** An Apprentice attempting a Rare sword with its blueprint rolls four stages against DC **22 each**, total **88**. Without that blueprint, each stage is also at disadvantage.
}}

{{wide,art,featureArt,height:320px
![](https://raw.githubusercontent.com/Omegaoliverid/Arcane-Forge-/08012b577047a13dd18bf698cb84cd5106d59595/af-15-v2.jpg)
}}{{footnote ARCANE FORGE | CRAFTING CORE}}
{{pageNumber,auto}}

\page
### Natural 1 and natural 20

All four **kept** natural die results count at face value in the sum. For each **natural 20**, cancel one **natural 1** within that same four-stage attempt. Resolve cancellations **after all four stages**. A natural 20 is **not automatic overall success**. An **uncancelled natural 1 causes catastrophic failure**, even when the arithmetic target was met. Under disadvantage, only the **lower kept die** can count as a 20 or 1.

**Master's Steady Hand:** Once per crafting **project**, a **Master or Grandmaster** may reroll **one natural 1** from the crafting checks. The new die result stands, even if it is another 1. For four-stage crafting, use the reroll **before** resolving natural-20 cancellations; other uncancelled 1s still cause catastrophe. When a check had disadvantage, replace one die showing 1 and then apply disadvantage to that check using its other original die. This use is **once per whole project**, not once per stage, and applies equally to a qualifying single-roll familiar project.

If the attempt succeeds and a natural 20 remains **uncancelled and unused**, it triggers the optional **Exceptional / Crafter's Choice** reward. This celebrates the twenty without overriding the existing catastrophe rules.

### Ordinary failures and catastrophe

| Margin below required total | Outcome |
|:--|:--|
| Meets or exceeds target, no uncancelled natural 1 | Successful creation |
| 1 point | Partial success; reduced function pending re-tuning or GM-described shortfall |
| 2–3 points | Delay or rework; usually 1d4 additional hours |
| 4–5 points | Flawed result; an approved quirk or impairment |
| 6–9 points | Significant setback; lose time and potentially part of the added material value |
| 10+ points | Catastrophe: the project and committed materials may be destroyed |
| Any uncancelled natural 1 | Catastrophe regardless of total |

**An ordinary setback does not automatically destroy every material.** Failed magical infusion normally protects a purchased or existing base item until a true catastrophe, though some new materials may be consumed. The GM can determine which magical input survives an ordinary non-catastrophic failure (see Arbitration 5, p. 35).

{{forgeSequence
{{art,height:305px
![](https://raw.githubusercontent.com/Omegaoliverid/Arcane-Forge-/929584c986ec54a4163f99de0b38b8aff455d61a/af-16-1.jpg)
}}

{{art,height:305px
![](https://raw.githubusercontent.com/Omegaoliverid/Arcane-Forge-/929584c986ec54a4163f99de0b38b8aff455d61a/af-16-2.jpg)
}}
}}

{{footnote ARCANE FORGE | CRAFTING CORE}}
{{pageNumber,auto}}

\page
{{wide,chapterhead
# EXPERIENCE CHANGES THE ROLL
## Familiar work should feel familiar

The four-stage process is for difficult **new creations**, major ambitious upgrades and witnessed promotion tests. Familiar or far-below-rank work is simpler. **All work costs time, materials and workshop access.**
}}

| Crafter's relationship to design | Procedure |
|:--|:--|
| New unfamiliar design at own tier or one below | Four integrated stages |
| Exact recipe successfully made before | **One d20 with advantage** vs the item's ordinary single-stage rarity DC |
| New design at least two rarity tiers below current capability | One d20 with advantage vs rarity DC |
| Exact familiar recipe at least two tiers below current capability | **Automatic success** when proper inputs, time and conditions exist |
| Guild or mentor examination | Always four stages, even for a familiar form |

A single-roll success uses the item's **single-stage DC: 12 / 14 / 17 / 18 / 20**, as applicable. A kept **natural 1** is catastrophic. If rolling with advantage, the kept result is the higher d20, so an actual kept 1 requires both dice to show 1. The four-die natural-20 cancellation process does not apply to one roll. Without suitable blueprint or organic-specialist knowledge, apply disadvantage to the project's actual check(s); on a single familiar-recipe check it cancels the normal advantage.

**A familiar formula is an exact successfully completed design**, not every possible item falling under the same construction blueprint. Making one Rare metal sword does not automatically make every new Rare metal sword a familiar recipe. Familiar work at the crafter's **current rank tier** can earn **1d20 XP on success** under the current XP rules, even for an exact recipe repeated many times, provided the full time and materials are committed. **Work below the crafter's current rank earns 0 XP**, even when successful. XP from a failed project is handled in the XP section.

### One project at a time

One character may have one active crafting project underway. Other projects wait or pause. A GM may approve a worker or helper on a different project, but does not grant the same crafter multiple simultaneous full-time work shifts.

### Improving beloved equipment

A crafter can add a new dragon-scale plate to existing armour, reinforce an old sword or combine freshly recovered components with equipment already worn. The GM assesses the **new total item**, not merely the added fragment. New projects require fresh work, suitable knowledge, the newly required materials, and a suitable binder **when the approved complete design calls for one**.

**Setback:** The original item remains intact; added materials may fail to bond and be lost, and rework or delays may follow. **Catastrophe:** The entire project, including treasured existing gear, may be damaged or destroyed. This is the risk of taking an heirloom back to the anvil.

### Recovering magical inputs after a setback

When it matters which experimental ingredients survive a noncatastrophic failed magical infusion, the GM may decide narratively or roll:

| d6 | What survives |
|:--|:--|
| 1–2 | Binder and magical component are lost |
| 3–4 | Binder remains, monster component is lost |
| 5–6 | Monster component remains, binder is lost |

This table is optional **when a binder was actually used**. It does **not** overrule catastrophic destruction and it does not automatically damage the established base item. A project without a binder cannot lose a nonexistent binder.

{{art,height:375px
![](https://raw.githubusercontent.com/Omegaoliverid/Arcane-Forge-/929584c986ec54a4163f99de0b38b8aff455d61a/af-17.jpg)
}}

{{footnote ARCANE FORGE | EXPERIENCE}}
{{pageNumber,auto}}

\page
{{wide,editorialText
# THREE POSSIBLE CREATIONS
## GM only - an optional moment of discovery

A player's ambition defines the story. Crafting expertise determines how fully that ambition is realised. When an original project deserves a dramatic reveal, the GM can write three **short, hidden results** before rolling.

**Sound:** A worthwhile version that delivers the creation's essential purpose.

**Refined:** The same creation with a meaningful improvement or more fully developed expression.

**Exceptional:** A superb interpretation that comes closest to the character's complete original ambition, yet remains within the **same approved item rarity**.

All three must be things the GM is willing to grant **before the player touches the dice**. The player should hear the range of possible outcomes, but need not see the precise statistics. More favourable crafting never obliges the GM to add a surprise fourth ability after the roll.

### Determine the result after success

These total-based quality bands apply to **four-stage projects**. For a familiar recipe resolved with one roll, agree one finished result before rolling; use its normal shortcut success and failure rules.

| Final successful total | Hidden result |
|:--|:--|
| Required total to +9 | Sound |
| Required total +10 to +19 | Refined |
| Required total +20 or more | Exceptional |
| Successful attempt with an unused, uncancelled natural 20 | **Reveal all three; the player chooses.** In a progressive sequence this naturally means Exceptional. |

First apply natural-one cancellation, target and catastrophe rules. An unused twenty **does not** turn failure into success. A cancelled twenty **does not** also unlock the choice reward.

**Genuine alternatives are allowed.** Sometimes the three possibilities lean toward accuracy, elemental magic or battlefield control rather than strictly increasing bonuses. On an uncancelled natural 20, the player chooses the version that most appeals to them. When one result is simply stronger, let the player celebrate and claim it.

### One-line GM preparation

{{wide
| A: Sound | B: Refined | C: Exceptional | Limits |
|:--|:--|:--|:--|
| +1 against all; +1 further against Giants | A + 2d6 thunder against Giants | B + once/rest knockdown chance | Only Giants receive extra thunder; knockdown 1/long rest |
}}

That's enough to begin. After success the player can write the complete item entry. The GM needn't draft three pages only to throw two away.

### The Giantbreaker's Wrath, Rare

**Materials:** A well-made axe, suitable Giant bone, a thunder-bearing creature component and a **Rare binder**. The player dreams of an axe that finds a Giant's weakness, thunders on impact and might throw the brute down.

- **Sound:** +1 to attack and damage against all creatures; **another +1** against Giants (**+2 total** against Giants).
- **Refined:** Sound benefits, plus **2d6 thunder damage on every successful hit against a Giant**.
- **Exceptional:** Refined benefits, plus **once per long rest** after hitting a Giant, attempt a **Strength (Athletics) check with advantage** contested by the Giant's Strength (Athletics). If the wielder succeeds, the Giant is knocked prone. This magical power can affect a Giant despite ordinary size restrictions, if the GM approved that exception.

All three are Rare creations **at the high, creature-specific end** of that category. The GM should reconsider the limits if the campaign largely consists of Giants. Four-stage Rare target: **68**, or higher if the crafter is working above rank.
}}

{{wide,art,featureArt,height:300px
![](https://raw.githubusercontent.com/Omegaoliverid/Arcane-Forge-/929584c986ec54a4163f99de0b38b8aff455d61a/af-18.jpg)
}}{{footnote ARCANE FORGE | HIDDEN OUTCOMES}}
{{pageNumber,auto}}

\page
{{tightpage
&nbsp;
}}

# TIME AT THE WORKBENCH
## Plan the work and the downtime

### Magical crafting and infusion

| Rarity | Weapons, body armour, shields | Jewellery, clothing, trinkets, accessories |
|:--|:--|:--|
| Common | 1d6 hours | 1d4 hours |
| Uncommon | 2d8 hours | 2d6 hours |
| Rare | 3d10 hours | 3d8 hours |
| Very Rare | **4d10 hours** | **4d8 hours** |
| Legendary | 4d12 hours | 4d10 hours |

Add **one die of the same type for each distinct approved magical property/enhancement**. One integrated ability described in colourful language is not several chargeable properties simply because it has multiple adjectives. The GM fixes the cost **before the roll**, budgeting for the most demanding of the three possible outcomes if using the hidden method. Exceptional crafting does not unexpectedly require more materials or labour after success.

Magical properties are integrated into the **same four-stage checks**. More hours do not mean extra mandatory roll sequences. A powered Portable Forge provides an appropriate workplace for these hours; it does **not** give the crafter free personal labour time or materials.

### Mundane manufacture

Making a weapon or armour **from raw billets, hides or scales** also takes practical manufacturing time and mundane workshop inputs. Bought or previously completed suitable base equipment **skips that initial construction work**, but magical infusion still takes the appropriate time above. A Medium full plate harness fabricated from raw material might reasonably occupy roughly **80 working hours** before magical work, depending on skill, tooling and support. This is an **illustration**, not a mandatory rate for every suit of armour.

A purely mundane item needs no binder or magically infused labour period, and uses agreed normal work hours. When mundane construction and enchantment are one substantial new magical project, the four rolls **cover the integrated endeavour**, not two separate full test sequences.

\column

### Workspaces

**Town/city workshop:** rented or borrowed; negotiated access and charges.

**Player workshop or bastion:** installed facilities and appropriate tools; upkeep and security as the GM sees fit.

**Portable Arcane Forge:** a fist-sized device unfolding into a **20 ft × 20 ft** workshop after a one-minute activation. One spell-slot level powers **12 operating hours** (second-level slot, 24 hours, etc.). A partly used twelve-hour block is not automatically refunded. An unfinished project can remain paused safely while the workshop folds; **living creatures cannot be stored** in it. The GM sets the device’s rarity, whether it requires attunement, and how it can be acquired before introducing it into play.

### Assistance

A suitably qualified helper grants **+2 to a check for a stage they actually assist**, or may instead **halve mundane construction time**. The same assistance does not provide both benefits. Combined helper assistance is capped at **+2 per check**, regardless of helper count; it replaces advantage from that assistance. Other sources of advantage or disadvantage follow the normal rules. Magical assistance does **not reduce infusion hours**. A Guild or mentor examination can forbid helpers.

NPCs working **9 hours/day** usually take the work hours divided by nine, rounded up, plus waiting time, material delivery and setbacks. The timeline is not an automatic guarantee of NPC success.

### Parallel downtime for several player crafters

When several PCs craft during the same downtime, **declare all projects first**. Confirm each crafter’s hours, workshop access, intended rarity, materials and binder requirements. Resolve the checks together, record results, losses and XP, and advance the campaign by the time actually spent. Keep one project line per PC. Give remarkable outcomes or requested scenes the spotlight; summarise routine commissions. This creates no extra hours and waives no material costs, Guild trials or the limit of **one active project per crafter**.

{{wide,workbenchPanorama
![](https://raw.githubusercontent.com/Omegaoliverid/Arcane-Forge-/929584c986ec54a4163f99de0b38b8aff455d61a/af-19.jpg)
}}

{{footnote ARCANE FORGE | TIME & WORKSHOP}}
{{pageNumber,auto}}

\page
{{wide,editorialText
# RANKS, XP & SPECIALISATION
## Practice opens the door. A trial earns the title.

{{wide
| Rank | Crafting XP threshold | Normal rarity capability | Specialisation |
|:--|--:|:--|:--|
| Initiate | 0 | Common | None |
| Apprentice | 100 | Uncommon | None |
| Journeyman | 300 | Rare | Choose first: +2 |
| Master | 750 | Very Rare **and** Legendary | Chosen trade becomes +3; Master's Steady Hand |
| Grandmaster | 1,000 | Very Rare, Legendary and exceptional masterpieces | First trade becomes +5; choose second at +5; retains Steady Hand |
}}

**These XP totals make a crafter eligible to test, not automatically promoted.** The character must pass an actual Guild or mentor trial. Higher-rank crafting ability is available **after** promotion. The rank specialisation bonus is added on appropriate stages **alongside** normal ability and one proficiency bonus, not in place of them. The specialisation bonuses are fixed at **+2 / +3 / +5**; they do not grant a second proficiency bonus.

### Crafting XP — learning by practice

| Outcome (at your current crafting rank's rarity or one above) | Crafting XP |
|:--|:--|
| **First successful completion of a genuinely new design**, at current rarity or one above | **2d20** |
| **Successful repetition** of an item/design **at the crafter's current rarity** | **1d20** |
| **Meaningful failed attempt** at current rarity or one above | **1d10** |
| **Any work below current rank rarity**, successful or failed | **0** |

A repeated eligible project still costs its **full actual hours, components, binder if required and workshop access**. There is no XP cap on genuinely repeated at-rank successes; a blacksmith improves through real practice. Each substantially new design earns its first-time **2d20** award only once; renaming an existing formula or changing decoration does not count. A later exact repeat at current rank instead earns **1d20**. **An above-rank success earns no additional multiplier**: the first successful eligible new design earns 2d20 in total.

The crafter's current rank is determined by **passed Guild or mentor promotion**, not by XP eligibility alone. **For XP eligibility**, treat these as current-rank item categories: Initiate = Common; Apprentice = Uncommon; Journeyman = Rare; Master = Very Rare **or** Legendary; Grandmaster = Legendary. A Grandmaster's lesser-rarity commissions do not become an XP loophole. Below-rank items **never** earn XP. Failure XP requires an actual meaningful attempt with its normal time, risk and material commitment, not intentionally throwing a trivial roll or cancelling a project without work. Use the crafting failure table normally; earning 1d10 XP does not reverse lost resources. A repeat of a design that remains **above rank** does not meet the 1d20 repeat-XP condition (which requires work at the crafter's current rank). The GM may recognise an actually new above-rank design with the ordinary first-success 2d20, but relabelling or remaking the same object is not a new design.

At **100 / 300 / 750 / 1,000 cumulative XP**, the character is **eligible** for the next rank but must still complete the agreed Guild or mentor trial. Above-rank attempts add **+5 to each stage DC** and, when lacking a suitable blueprint, disadvantage as usual. This does not turn that dangerous option into an easy XP shortcut.

**Five item rarities, five crafter ranks:** These are two distinct ladders. A **Master** has normal access to **both Very Rare and Legendary** and can make a +3 weapon if the ingredients, blueprint and full design are approved. Grandmaster advancement remains a special masterwork trial, not the only possible source of a +3 weapon.
}}

{{wide,art,featureArt,height:250px
![](https://raw.githubusercontent.com/Omegaoliverid/Arcane-Forge-/929584c986ec54a4163f99de0b38b8aff455d61a/af-20.jpg)
}}{{footnote ARCANE FORGE | RANKS & XP}}
{{pageNumber,auto}}

\page
{{wide,editorialText
### Specialisations

Choose a meaningful field: Weaponsmith, Armoursmith, Jeweller, Artificer or another suitably bounded craft. The trade chosen must actually apply to the work being rolled. A Grandmaster may have **two** fields. Proficiency with necessary tools remains separate; do not count the same proficiency twice.

### One rarity above rank

A crafter may attempt **one rarity beyond the rank's normal capability** at **+5 DC per stage** on the full four-stage attempt. If the character also lacks suitable blueprint/training, **each stage is at disadvantage**. It is difficult on purpose. **Warn the player plainly about the chance of catastrophic loss before committing materials, especially an heirloom.** This exception permits ambition; it does not grant premature promotion or an automatic higher-rank blueprint. A Journeyman can attempt Very Rare at +5/stage; an Apprentice can attempt Rare. A Master already has both Very Rare and Legendary as normal capabilities and **does not** treat Legendary as above rank.

{{descriptive
##### A master's warning before ambitious work
*The Guildmaster runs a thumb over the scar across his palm. "The forge respects neither titles nor courage. This plan is beyond what you have proved you can bind. Bring it to the anvil if you wish, but know that a single mistake may leave you holding nothing at all."*
}}

**Player-facing danger:** A one-tier-above item increases the target **by 20 over four stages**, and an absent blueprint also imposes disadvantage on **all four rolls**. Catastrophe can destroy committed materials and even an existing treasured item. An Apprentice attempting an above-rank Rare item can face a **very low chance of success** and a **severe catastrophe risk**. Actual odds depend on ability and tool modifiers, blueprint knowledge, assistance and other circumstances; the GM should make the danger clear before materials are committed.

### Exams and reputation

An exam project still uses **four stages** regardless of experience with the item shape. A finished item can bear the maker's mark and develop a history. Renown may attract patrons and interesting offers, but rank never guarantees that merchants will pay full retail value for every creation.
}}

{{wide,art,featureArt
![](https://raw.githubusercontent.com/Omegaoliverid/Arcane-Forge-/08012b577047a13dd18bf698cb84cd5106d59595/af-21-v2.jpg)
}}{{footnote ARCANE FORGE | RANKS & XP}}
{{pageNumber,auto}}

\page
{{wide,editorialText
{{wide,chapterhead
# GUILD TRIALS
## The costly route to recognition

A Guild's exam is not a simple paperwork fee. It is a witnessed craft, a public promise of standards and often a costly creation the Guild will **retain**. The crafter must first meet the crafting XP threshold for the intended promotion.
}}

### High-fee Guild schedule

These are the **default Guild assessment fees** for a campaign in which professional recognition is costly. A GM can adjust them to the economy of the campaign. **Fees and material provision are separate.**

{{wide
| Promotion | Guild examination fee | Illustrative materials allowance | Total if Guild supplies them |
|:--|--:|--:|--:|
| Initiate → Apprentice | 20 gp | 40 gp | **60 gp** |
| Apprentice → Journeyman | 1,000 gp | 500 gp | **1,500 gp** |
| Journeyman → Master | 5,000 gp | 2,000 gp | **7,000 gp** |
| Master → Grandmaster | 20,000 gp | 5,000 gp | **25,000 gp** |
}}

The **exam fee is never waived simply because the candidate brings materials**. The materials allowance is an example of how much the Guild may charge to supply an appropriate assessment project's ingredients; **not** a universal resale price or a compulsory charge on top of materials the candidate already owns. When the candidate supplies suitable required components, subtract the corresponding supply purchase, never the assessment fee.

### Conduct of the assessment

1. Reach the XP threshold for the next rank.
2. Accept a commission **one rarity above rank**: **Uncommon** (Initiate), **Rare** (Apprentice), or **Very Rare** (Journeyman). A Master's Grandmaster Guild exam instead uses a **Legendary** item, already within Master capability. Agree materials and binder.
3. Pay the assessment fee; procure materials personally or from the Guild.
4. Make the normal **four crafting checks**: **+5 DC/stage (+20 total)** when above rank; disadvantage on each stage without suitable blueprint/training. A Master's Legendary Guild item uses **DC 20/stage (total 80)**, with **no extra Guild DC**.
5. The Guild examines the outcome. On passing, the crafter earns promotion. The **Guild keeps the finished examination item** under its charter.

**Fees, materials and surrendering the finished item are the added challenge.** The GM may enrich the story, but should not require extra checks or unrelated tasks.

### Retakes

For an ordinary failed Guild examination, the **repeat assessment fee is half the standard fee**. Replacement materials are still needed if the original inputs were consumed. A catastrophe makes the repeat fee **the full Guild fee**, plus whatever fresh materials are required. The normal crafting failure rules determine the fate of the submitted materials and work.



### Guilds as worldbuilding

A Guild might be a single citywide organisation, a dwarven smithing order, elven gemcutters, itinerant artificers, a group of coastal living-coral artisans, or competing craft houses. Institutions teach and examine only what they plausibly know. Local politics, patronage and reputation may affect invitations and negotiations, not rewrite the mechanical foundation unnoticed.
}}

{{wide,art,featureArt,height:300px
![](https://raw.githubusercontent.com/Omegaoliverid/Arcane-Forge-/929584c986ec54a4163f99de0b38b8aff455d61a/af-22.jpg)
}}{{footnote ARCANE FORGE | THE GUILD}}
{{pageNumber,auto}}

\page
# MENTORS & THE GRANDMASTER TRIAL
## Another path, no easier to earn

A mentor may examine a qualifying student **instead of** a Guild. There is **no formal Guild examination fee**. The mentor may demand precise materials, difficult standards, a valuable **Pristine** component or an unusual location; the candidate finds, trades for or buys those ingredients. The student works **without helper assistance** in the mentor’s presence. A successful normal mentor examination leaves the finished work with the **student**. An interested mentor may also teach a blueprint or organic technique within their knowledge, but that instruction is not automatic.

### The Grandmaster forge-off

The ultimate mentor challenge creates **one complete Legendary masterpiece** in **two meaningful, comparable halves**. These might be a greatsword’s blade and hilt, or matching pieces of armour. The candidate supplies suitable materials for **both** halves, including any stipulated Pristine materials. Both smiths forge their components under fair conditions.

Each contestant makes **four integrated crafting rolls** for their own substantial component; an especially bespoke Legendary masterpiece may use the **DC 25 / total 100** challenge target. This target reflects the special difficulty **within Legendary**: a qualified Master attempting this official trial does **not** add another +5 above-rank DC. Both candidates face the same declared contest standard. The normal natural-1 and natural-20 cancellation rules operate **within each person’s four rolls**, not across contestants. Both halves must meet the declared target and avoid catastrophe before the student can earn promotion. Compare the **four-roll combined totals**: the student must **strictly exceed** the mentor’s score. A tie belongs to the mentor. **Read the stakes aloud before anyone commits material:** on an ordinary loss the mentor keeps the assembled masterpiece, even though the candidate supplied both halves. The student may instead pursue the Guild examination route where allowed.

| Trial outcome | Consequence |
|:--|:--|
| Student completes work and strictly wins | Gains Grandmaster rank and the completed assembled masterpiece |
| Student loses or ties without catastrophe | No promotion; the mentor keeps the complete assembled work; no forced waiting period |
| Student catastrophically fails | The ruined half is destroyed; no promotion; mentor forbids another attempt for **three full moons** |

Mentor ranking for an encounter is narrative as well as mechanical. State the mentor’s **complete applicable bonus** before the duel, as with any NPC crafting check: suitable ability modifier + one tool proficiency bonus + relevant specialisation. A typical Grandmaster mentor specialising in that craft has **+5 specialisation**, added to the other legitimate modifiers. For a particularly formidable examiner, the GM may use a **renowned mentor with roughly +2 more** to the normal complete bonus or a **legendary mentor with roughly +5 more**. These figures are suggested NPC abilities, not extra student penalties. The GM assesses the opponent fairly and communicates the gravity of the challenge.

**Mentor catastrophe:** No automatic free Grandmaster title is awarded merely because the mentor fails. Use the normal requirement for a completed masterpiece and a won contest, and resolve an interrupted or failed mentor half as a story event with the GM; do not fabricate a guaranteed victory from an incomplete item.

### A gift worth risking

A truly great mentor may secretly offer a newly elevated Grandmaster a **single Pristine Legendary-quality material** for some later creation. It is a story gift, not a guaranteed additional attack/AC bonus; the next forging attempt can still catastrophically destroy it.

### Three short read-aloud endings

{{descriptive
**Victory:** *The two halves meet. For one breath, even the forge falls silent. Your master’s hand lingers on the work—and then withdraws. “No longer my apprentice. You have made something the world will remember.”*

**Ordinary loss:** *The master fits the two halves, tests their balance, then places the piece on the rack. “The joint runs wide here. Come back when you can show me a cleaner fit.”*

**Catastrophe:** *The metal parts with a sharp report. The master lifts the broken edge into the light. “Put down your tools. Three full moons. Bring new material when you return.”*
}}

{{art,height:205px
![](https://raw.githubusercontent.com/Omegaoliverid/Arcane-Forge-/929584c986ec54a4163f99de0b38b8aff455d61a/af-23.jpg)
}}

{{footnote ARCANE FORGE | MENTOR TRIALS}}
{{pageNumber,auto}}

\page
# COSTS, BARTER & REPUTATION
## Materials have value. Artistry has a story.

### Construction quantities are not retail prices

A **2 lb iron billet = 1 CU**, and ordinary raw iron is priced at **1 sp per pound** in the 2014 fifth-edition trade goods list; such a billet is approximately **2 sp** at that baseline. This does **not** mean two silver pieces of raw iron is a completed magical dagger, or that a 30-CU full suit of armour costs only thirty billets. Skilled labour, fittings, forge supplies, quality of steel, shaping losses already accounted for in usable CU, fitting, workshop access and magical components all matter.

**Avoid charging twice.** If a character already owns the qualifying material, count it as supplied. A purchased base item includes its existing structure and workmanship. For new plate armour, charge the agreed materials, fittings, labour and workshop costs—not an additional blanket surcharge drawn from another crafting system. Likewise, making armour comparable to a costly shop item does not guarantee a buyer at that retail price.

### Optional market prices for small parts

Use these only for **ordinary small harvested components**, not entire hides, buckets of scales or major legendary organs. Columns below are explicitly from the **merchant's perspective**.

| Part rarity | Merchant pays party | Merchant charges party |
|:--|--:|--:|
| Common | 1d10 cp | 2d10 cp |
| Uncommon | 2d10 sp | 4d10 sp |
| Rare | 3d10 gp | 6d10 gp |
| Very Rare | **GM-valued** | **GM-valued** |
| Legendary | **GM-valued** | **GM-valued** |

A Pristine part counts one rarity tier higher in these optional pricing prompts (**Rare → Very Rare → Legendary**), capped at Legendary. Very Rare parts are individually valued here rather than priced as inexpensive minor components. A whole dragon hide or exceptional binder receives an **individual GM valuation**, rather than one flat small-part roll regardless of size or rarity.

\column

### Optional barter

For an uncertain market negotiation, player and merchant may roll opposed **d20 + Charisma modifier**. On a tie, keep the quoted price. On a player win, the GM may modestly improve the deal; on a merchant win, improve the merchant's terms. Any adjustment should fit the **actual transaction's value**. A successful bargain might lower a small fee, win a better offer or earn future favour; it should not turn a major magical component into a trivial purchase. Direct conversation and negotiated favours are equally valid.

### Selling completed creations

There is **no automatic buyer** for every magic item. A known master's commissioned work can command higher prices than an anonymous smith's stock; a legendary item may be essentially unsaleable through ordinary shops. Consider reputation, provenance, demand, scarcity, identification and the buyer's actual wealth. Forger rank alone is not a fixed resale multiplier. **Repeated production at the crafter's current rank does award 1d20 XP for real successful work** under the progression rules; lower-rank production does not award XP. Regardless of XP, there is **no guaranteed profitable buyer**, unlimited binder supply or risk-free resale loop.

### Commissioning an NPC

Ordinary mundane artisans are not automatically ranked magical Journeymen. Choose the NPC's actual craft rank, blueprint knowledge, materials, time, labour quote and willingness. A Master does **not** automatically succeed; a failed job is not automatically retried with advantage every few days. NPCs use the same risk principles unless the GM narratively resolves genuinely routine work.

{{art,height:245px
![](https://raw.githubusercontent.com/Omegaoliverid/Arcane-Forge-/929584c986ec54a4163f99de0b38b8aff455d61a/af-24.jpg)
}}

{{footnote ARCANE FORGE | ECONOMY}}
{{pageNumber,auto}}

\page
# AN ADVENTURE IN THE FORGE
##### GM ONLY
## Three scenes to teach the full system

### Scene I — Taking the material

The party brings down a dangerous beast. Frank wants the usable scales. The GM checks the creature's CR, chooses the proper harvesting DC and calls for an appropriate check. Frank succeeds and recovers **six Medium scales**. He records **6 CU**, their source and their rarity. One excellent roll could make a specific harvest **Pristine**. The GM does not promise a magical bonus simply because a scale is Pristine.

### Scene II — Making protection

Frank owns plain leather armour and wants its front facing reinforced with the harvested scales. A Medium gilet would require **12 CU** from scratch, but reinforcing existing armour needs **6 CU**. He has enough for the physical project. The GM checks the correct **Plate & Scale or Flexible Armour construction knowledge**, whichever fits the physical design, plus magic ingredients/binder if the intended upgrade is magical.

Frank asks for protection against spears. The GM refers to **Armour GM Quick Reference 02**, confirms that a narrow AC enhancement might fit the appropriate rarity, and explains what the materials plausibly permit. If they choose the optional three-hidden-outcome method, the GM prepares those outcomes **before the first roll**.

The crafter completes the four integrated stages and receives the final creation based on the sum, unless failure or catastrophe intervenes. An unused uncancelled natural 20, after a successful project, permits the player to select from the three pre-approved outcomes.

### Scene III — The armour evolves

Later, the party recovers more scales of a different dragon. Frank proposes a new combination of the scales on his existing armour. He only needs the **newly required CU** and whatever fresh magical ingredients/binder are appropriate for the **whole upgraded design**. The GM may approve mixed fire-and-acid defence or a caustic reaction, not both dragons' entire spell lists.

A setback means Frank's original armour survives; the new scales may be wasted. A catastrophe can destroy the original armour too. The forge does not promise safety to sentimental equipment. Frank chooses whether the potential achievement justifies that risk.

\column

### What this scene illustrates

- Harvested quantity and harvest quality are different measurements.
- The CU chart answers **"Do I have enough?"**, not **"What bonus do I receive?"**
- The blueprint teaches the physical craft, not an automatic magical recipe.
- Magical rarity and binder support must match the approved ambition.
- Four stages are one integrated project, not separate forging/enchanting sequences.
- The item may evolve, but accumulated abilities must still be balanced as **one complete item**.

{{art,height:550px
![](https://raw.githubusercontent.com/Omegaoliverid/Arcane-Forge-/929584c986ec54a4163f99de0b38b8aff455d61a/af-25.jpg)
}}

{{footnote ARCANE FORGE | PLAY EXAMPLES}}
{{pageNumber,auto}}

\page
![Behind the GM Screen](https://raw.githubusercontent.com/Omegaoliverid/Arcane-Forge-/929584c986ec54a4163f99de0b38b8aff455d61a/af-26.jpg){position:absolute,top:0px,left:0px,width:100%,height:100%,object-fit:cover}

{{partcap
##### PART THREE
## Behind the GM Screen
*Starweaver's Robes — woven from ethereal thread*
}}

\page
# GM QUICK REFERENCE 01
## MAGICAL WEAPONS

**A player's imagination. Your judgement. Their creation.** This is an optional table-side guide. The detailed rationale appears in the GM Rules & Arbitration chapters.

{{wide
| Step | The GM asks | Do this |
|:--|:--|:--|
| **1 — IDEA** | What should the weapon do? | Accuracy, damage, poison, elemental force, disarming, control? |
| **2 — MATERIALS** | What supports that effect? | Match physical parts, special components and any required binder. |
| **3 — BALANCE** | How strong and how broad? | Compare full item with rarity, frequency and enemies. |
| **4 — POSSIBILITIES** | One outcome or three? | Agree one result, or hide Sound / Refined / Exceptional. |
| **5 — FORGE** | How does it emerge? | Roll normal craft stages, resolve, reveal and name. |
}}

### Weapon rarity guide

| Rarity | Enhancement | Possible magical effects |
|:--|:--|:--|
| Common | No permanent +1 | Minor flavour, utility or narrowly situational magic |
| Uncommon | Up to +1 to **attack and damage** | Useful effect **instead**, sometimes +1 with narrow minor extra |
| Rare | Up to +2 to **attack and damage** | Substantial effect instead; or +1 plus suitable narrower ability |
| Very Rare | Up to +3 to **attack and damage** | Strong effects approaching legendary scope; a plain +3 weapon belongs here |
| Legendary | Up to +3 to **attack and damage** | Exceptional theme-driven abilities; combinations judged as a whole, not an automatic +4 |

**Check the whole item:** Every hit versus once/turn? Every enemy versus Giants only? Unlimited versus rest recharge? Does it require attunement or an action? What other magic is equipped? There is **no automatic trade of +1 for a particular fixed die**; negotiate at the table.

### Example — The Giantbreaker's Wrath (Rare)

*"With your present understanding, you might forge an axe that finds a Giant's weakness; with finer work, it might thunder on impact, or even topple a mighty foe."*

| GM's hidden card | Planned item, all within Rare |
|:--|:--|
| **Sound** | +1 attack/damage generally; **another +1** against Giants (total +2 there) |
| **Refined** | Sound plus **2d6 thunder** every hit against Giants |
| **Exceptional** | Refined plus **once/long rest**, after a hit against a Giant, a **Strength (Athletics) contest with advantage** to knock it prone |

**Rare target 68:** Sound 68–77; Refined 78–87; Exceptional 88+. An **unused, uncancelled natural 20 on a successful four-stage craft** reveals all three; player chooses. Apply catastrophe rules before rewards.

{{forge
##### GM's golden rule
Ask what matters most to the player. Where a proposed weapon overreaches, narrow its targets, lower a universal bonus, restrict use, exchange benefits or make a higher-tier project. Multiple monster parts give inspiration, not automatic cumulative statistics.
}}

**Details:** Arbitration 2 — Weapons, Conditions and Damage (p. 32).

{{art,height:490px
![](https://raw.githubusercontent.com/Omegaoliverid/Arcane-Forge-/929584c986ec54a4163f99de0b38b8aff455d61a/af-27.jpg)
}}

{{footnote ARCANE FORGE | GM · WEAPONS}}
{{pageNumber,auto}}

\page
# GM QUICK REFERENCE 02
## BODY ARMOUR & SHIELDS

**What should the character survive?** Build the defence around the player's answer rather than automatically combining every protective property.

{{wide
| Step | The GM asks | Do this |
|:--|:--|:--|
| **1 — IDEA** | What are you defending against? | Piercing, spells, Giants, fire, grapples, fear? |
| **2 — MATERIALS** | Why should the item protect this way? | Examine hide, chitin, bone, shell, scales, organs and binder if required. |
| **3 — BALANCE** | Avoid, absorb, resist or retaliate? | Compare AC, reduction, resistance and actions. |
| **4 — POSSIBILITIES** | One outcome or three? | Prepare Sound / Refined / Exceptional if desired. |
| **5 — FORGE** | Did the defence take shape? | Apply crafting and hidden-result rules. |
}}

### Protection rarity guide

| Tier | Body armour | Shields | Illustrative defensive magic |
|:--|:--|:--|:--|
| Common | No permanent enhancement | No permanent enhancement | Minor/situational protection |
| Uncommon | Normally no general AC +1 | Up to +1 magical AC | Useful narrow defence or limited reduction |
| Rare | Up to +1 magical AC | Up to +2 magical AC | Strong protection, resistance or balanced combinations |
| Very Rare | Up to +2 magical AC | Up to +3 magical AC | Stronger defences with exceptional restrictions or themes |
| Legendary | Up to +3 magical AC | Up to +3 magical AC | Exceptional powers; outright immunity is extraordinary |

**Most broad AC bonuses come from body armour and shields**, but the published 2014 fifth-edition rules also include a **Rare Ring of Protection** and an **Uncommon Cloak of Protection**, each giving +1 AC and +1 to saving throws while attuned. Preserve published items' actual rarity and attunement requirements. New, bespoke accessories that grant broad permanent AC normally require **attunement** and explicit approval of the character's combined AC; do not impose a mandatory cap on how many such items may exist.

### Example — The Piercing Ward (Rare)

*"You've had enough of arrows and stabbing weapons. Your materials suggest tougher leather, perhaps something that can turn a point and—if the stitching holds—absorb the worst of a blow."*

| GM's hidden card | Planned item, all within Rare |
|:--|:--|
| **Sound** | Normal leather armour plus **+2 magical AC** against an attack roll whose **basic hit deals piercing damage as its primary damage type**, before added elemental or magical riders |
| **Refined** | Sound plus **1/long rest**, reaction after taking piercing damage: reduce it by **1d6** |
| **Exceptional** | Sound plus **1/short or long rest**, reaction after taking piercing damage: reduce it by **2d6** |

**Rare target 68:** Sound 68–77; Refined 78–87; Exceptional 88+; an unused uncancelled 20 on successful craft allows a choice. Note that the Exceptional replaces the Refined reaction benefit with a stronger version; it does not give two separate reductions.

{{forge
##### GM's golden rule
AC can cause an attack to miss. Damage reduction works after a hit. Resistance halves qualifying damage. These are **not equivalent**, and permanent resistance is a major benefit on its own. A narrow piercing-only defence may still be extremely useful in an archer-heavy campaign.
}}

**Details:** Arbitration 3 — AC, Mitigation and Retaliation (p. 33).

{{art,height:320px
![](https://raw.githubusercontent.com/Omegaoliverid/Arcane-Forge-/929584c986ec54a4163f99de0b38b8aff455d61a/af-28.jpg)
}}

{{footnote ARCANE FORGE | GM · ARMOUR}}
{{pageNumber,auto}}

\page
{{wide,editorialText
# GM QUICK REFERENCE 03
## ACCESSORIES & EVERYTHING ELSE

**What capability should this item grant?** This includes jewellery, clothing, helmets, gauntlets, boots, bracers, cloaks, talismans and inventions that are neither body armour/shields nor weapons.

{{wide
| Step | The GM asks | Do this |
|:--|:--|:--|
| **1 — IDEA** | What new thing can they do? | Explore, move, summon, sense, heal, control? |
| **2 — MATERIALS** | Do ingredients plausibly enable it? | Match creature anatomy, structural components and binder if required. |
| **3 — BALANCE** | What challenge can it bypass? | Range, duration, speed, use, actions and attunement. |
| **4 — POSSIBILITIES** | One or three results? | Approve one or prepare three hidden short lines. |
| **5 — FORGE** | How fully was it realised? | Roll, resolve, celebrate, record. |
}}

### Utility rarity guide

| Tier | Typical magical scope |
|:--|:--|
| Common | Sensory or cosmetic trick, convenient minor utility |
| Uncommon | Meaningful but manageable movement, exploration or small combat utility |
| Rare | Substantial mobility, information, protection, restraint or limited support |
| Very Rare | Significant encounter-changing abilities with clear limits |
| Legendary | Extraordinary signature abilities, potentially multiple complementary powers |

No rarity automatically grants unrestricted flight, invisibility, teleportation, regeneration, summons or AC. Evaluate the actual use. **Movement limits** can be range/speed for smaller powers, or duration and limited uses for encounter- or adventure-changing abilities.

### Example — Webspinner Bracers (Rare)

*"The spinnerets and silk suggest a usable web-line. You might swing across a gap; with finer work you could hinder prey; perfect work might bind it altogether."*

| GM's hidden card | Planned item, all within Rare |
|:--|:--|
| **Sound** | As a **bonus action**, launch web-line up to **60 ft** to suitable anchor; use normal movement to climb/swing, no extra movement or flight |
| **Refined** | Sound plus **2 uses/long rest**: as an **action**, target one creature within **30 ft**; failed **DC 15 Dexterity save** halves its speed until the end of its next turn |
| **Exceptional** | Refined plus **1 use/long rest**: as an **action**, target one **Large or smaller** creature within **30 ft**; failed **DC 15 Dexterity save** restrains it until the end of its next turn |

**Rare target 68:** 68–77 Sound; 78–87 Refined; 88+ Exceptional. Successful craft and unused uncancelled natural 20 = reveal all and choose.

**Organic specialist:** Harvested spinnerets can be ordinary monster ingredients, but a *functioning living web-launcher* may require optional specialist-organic knowledge. Without taught knowledge, no-blueprint disadvantage applies.

{{forge
##### GM's golden rule
Utility power is measured by **what it accomplishes**, not by damage dice. Agree on limits before crafting; then honour what the finished item actually promises, even when it changes your planned adventure.
}}

**Details:** Arbitration 4 — Utility, Movement and Summons (p. 34).
}}

{{wide,art,featureArt,height:310px
![](https://raw.githubusercontent.com/Omegaoliverid/Arcane-Forge-/929584c986ec54a4163f99de0b38b8aff455d61a/af-29.jpg)
}}{{footnote ARCANE FORGE | GM · ACCESSORIES}}
{{pageNumber,auto}}

\page
{{tightpage
&nbsp;
}}

{{wide,chapterhead
# GM RULES & ARBITRATION
## 1. Judging rarity and overall power

**The player decides what they would love to create. The GM decides which versions the world and its rules can support.** Begin with that ambition before looking at bonuses. The GM can ask: *"Which part of that is most important to you?"*
}}

| Rarity | Expected scope |
|:--|:--|
| Common | Small quality-of-life or narrow situational benefit |
| Uncommon | One useful ability or modest enhancement, perhaps a narrow secondary trait |
| Rare | A major combat/defensive/utility ability, or a balanced combination of smaller abilities |
| Very Rare | Strong, broadly useful magic, or potent abilities with appropriate limits |
| Legendary | Extraordinary signature capability, sometimes multiple strong complementary effects |

### Attunement and final ownership

**Crafted items use the table's ordinary 2014 fifth-edition attunement rules.** Some crafted items require attunement and some do not; crafting does **not** automatically waive or impose it. The GM states whether **each possible approved result** requires attunement **before crafting begins**. A creature normally cannot be attuned to more than **three** magic items. Extra items worn or carried do not bypass that limit. A simple +3 weapon need not acquire attunement solely from its rarity; a powerful combination of ongoing abilities may warrant it. A binder is not an attunement slot and does not grant extra equipment slots.

### Five questions for any new magical item

1. **Power:** How much damage, attack, AC, healing, control or utility does it provide?
2. **Frequency:** Every hit, every turn, once per day or on charges?
3. **Scope:** Every opponent, one damage type or very specific targets?
4. **Cost:** Action, bonus action, reaction, attunement, concentration-like constraints, charges?
5. **Combination:** How does this interact with existing items, spells and class abilities?

These are **prompts**, not a numerical points budget.

### Use published fifth-edition items for scale

| Reference point | Published rarity | What it illustrates |
|:--|:--|:--|
| +1 weapon | Uncommon | General attack **and** damage +1 |
| +2 weapon | Rare | Reliable general attack and damage +2 |
| +3 weapon | Very Rare | A qualified Master may make this; it is not automatically Legendary |
| +1 shield | Uncommon | General defensive enhancement |
| +2 shield | Rare | More substantial general defensive enhancement |
| +3 shield | Very Rare | A substantial magical defence |
| +1 body armour | Rare | Broad permanent AC is valuable |
| +2 body armour | Very Rare | Higher broad AC defence |
| Flame Tongue | Rare | Substantial additional fire damage per successful hit |
| Giant Slayer | Rare | +1 and additional strong effect against Giants |

These references aren't rules that every creation may copy exactly; some published items require **attunement** and have particular activation rules. Edition text may differ, so the GM compares the exact item used by the table.

### Target-specific power is context-specific

A weapon that deals 2d6 thunder only against Giants is narrow in a varied campaign and nearly universal in an adventure entirely about Giants. A +2 AC modifier against piercing attack rolls may apply frequently in a campaign dominated by archers. **Do not award a huge bonus merely because the design includes the word "only."**

### Multiple monster ingredients

One powerful effect, two modest effects, or one **new emergent combination** may all be fair. None is automatic. A red-and-black dragon armour blend might produce heat and acid protection or a scalding reaction, but no player receives two complete sets of dragon powers by default.

### If the proposal is too strong

Preserve the theme by narrowing a target, restricting uses, adding activation cost, reducing a universal numerical bonus or increasing the rarity and adventure requirements. Set the **potential outcomes before rolling**, never after seeing a surprisingly high score.

{{footnote ARCANE FORGE | ARBITRATION · 1}}
{{pageNumber,auto}}

\page
# GM ARBITRATION
## 2. Weapon damage, accuracy and effects

A weapon's **enhancement bonus** normally adds to **attack and damage** rolls. This affects not just damage magnitude, but how often the character hits, so it must be weighed differently from extra elemental dice. Let player and GM decide whether accuracy, damage or special powers matter more. There is **no mandatory exchange rate** between +1 and 1d6.

### Illustrative rarity envelope

| Tier | General-purpose example | Specialist or limited example |
|:--|:--|:--|
| Common | No lasting attack enhancement | Glows at undead, small situational use |
| Uncommon | +1 to attack/damage **or** a useful small magical effect | Narrow +1 weapon with modest creature-specific bonus damage; short limited elemental burst |
| Rare | +2 to attack/damage **or** a substantial magical weapon ability | +1 with 2d6 vs a particular creature type; no +hit but 2d6 fire per hit with proper balancing |
| Very Rare | Up to +3 attack/damage | Strong bounded magic comparable to Very Rare published items |
| Legendary | Up to +3 attack/damage | Powerful themed abilities or balanced combinations worthy of a unique relic |

**Example maths:** A fighter landing three hits with **1d6 once per turn** adds 1d6. With **1d6 on every hit**, three hits add 3d6. With **2d6 every hit**, three hits add 6d6. That is why the number of attacks, action economy and frequency of enemies who trigger the effect must be checked before approval.

{{art,height:230px
![](https://raw.githubusercontent.com/Omegaoliverid/Arcane-Forge-/929584c986ec54a4163f99de0b38b8aff455d61a/af-31.jpg)
}}

### Magical conditions can outweigh damage

| Tier | Possible effects | Check before approving |
|:--|:--|:--|
| Common | Visual warning, harmless sound or light | No hidden combat dominance |
| Uncommon | Modest slowing, limited shove, mild poison | Short duration, save, limited use |
| Rare | Brief restraint, knockdown, jumping lightning, stronger toxin | Target restriction, save, rest limit |
| Very Rare | Powerful control or major magical conditions with meaningful limits | Uses, saves, concentration-like trade-offs |
| Legendary | Stunning, broad zones, extraordinary control | Very careful action-economy and use limits |

**Loss-of-turn effects** (stunned, paralysed, incapacitated, etc.) are potentially much stronger than modest damage. Do not give unconditional repeated disables merely because they are thematically justified by a rare claw or gland.

### Suggested saving throw DCs

| Rarity | Suggested DC |
|:--|--:|
| Uncommon | 13 |
| Rare | 15 |
| Very Rare | **16–17 (guidance)** |
| Legendary | 17–18 |

These are adjustable **reference points**, not a second mandatory scaling formula. If the ability uses an **opposed Athletics check**, as in Giantbreaker's knockdown, this DC table does not apply.

### When a charge is used

For an activated on-hit effect, declare and spend the charge after the attack connects and **before the target's saving throw**. If the target succeeds on the save, the charge is **still used**. Abilities with different activation wording should clearly say when the resource is expended. A miss does not normally spend an *on-hit activated* charge because the ability never triggered.

### Material flavour

A fang could inspire bleeding, a venom gland toxic damage, a thunder horn concussive force, a scale a cold strike, or an ooze strand a grabbing blade. The material **suggests** a property; it doesn't grant a fixed prewritten effect. Combine carefully and evaluate the finished weapon, not each ingredient in isolation.

{{footnote ARCANE FORGE | ARBITRATION · 2}}
{{pageNumber,auto}}

\page
{{tightpage
&nbsp;
}}

# GM ARBITRATION
## 3. AC, mitigation and retaliation

An armour creation may prevent a hit, reduce damage after a hit, grant resistance, protect against a saving-throw condition or retaliate. **They are not interchangeable.**

| Protection | What happens |
|:--|:--|
| **AC enhancement** | The attack may miss altogether; if it hits, damage is unchanged |
| **Damage reduction** | The attack hits; reduce damage by a stated die or number |
| **Resistance** | Halve relevant damage, using normal fifth-edition resistance rules |
| **Immunity** | Negate relevant damage entirely; extremely powerful |

**Example:** A spear attack would deal **16 piercing**. A specific AC increase might make it miss; a reaction reducing damage **1d6** leaves a variable amount; piercing resistance reduces the 16 to **8**. A Rare suit that combines broad AC, permanent resistance and another unrestricted defensive effect requires exceptional scrutiny.

### Broad AC benchmarks

- **Body armour:** General +1 at **Rare**, +2 at **Very Rare**, +3 at **Legendary** (use the full item and campaign context).
- **Shields:** General +1 at **Uncommon**, +2 at **Rare**, +3 at **Very Rare** (or Legendary with exceptional effects).
- **Other slots:** Prefer distinctive utility or situational defence rather than automatically stacking extra AC. Published protection rings and cloaks provide familiar, attunement-based +1 AC examples at their printed rarities. A **newly invented accessory granting broad, permanent AC normally requires attunement** and prior GM review of the character's **final combined AC**. Separate custom items do not obtain automatic stacking permission just because they were forged separately. No universal numerical cap is imposed.

Use **the appropriate item rarity and the complete item design**; physical pieces added to a single armour suit don't independently provide separate +AC per dragon scale, gauntlet or plate.

\column

### Advisory total-AC review thresholds

| Character level | Total AC prompting GM review |
|:--|--:|
| 1–4 | 21+ |
| 5–10 | 23+ |
| 11–16 | 25+ |
| 17–20 | 27+ |

**These are review triggers, never hard AC caps.** Before approving a new item that reaches or exceeds a threshold, consider the character's **complete equipped AC**, class features, fighting styles, spells or lasting buffs, attuned equipment, and likely enemy attacks and saving-throw effects. An invested armoursmith may legitimately attain a high AC. The GM may approve any total that fits the campaign; the threshold exists to prompt a deliberate check, not to veto an earned reward. Official published items retain their normal rules.

### Specialist defences

A conditional **+2 AC against qualifying piercing attack rolls** can be a Rare design even where +2 general body armour is too powerful for Rare. Its true benefit varies across campaigns. For the Piercing Ward example, the attack's **basic hit must deal primarily piercing damage**, assessed before added elemental or magical riders. Other bespoke defences may use a different restriction if the GM approves it in advance.

### Retaliation

- **Active retaliation:** A reaction on being struck (for example, a Rare shield biting back for **1d6 piercing** once the wielder spends their reaction) is a useful starting point.
- **Passive retaliation:** Automatic damage every time an enemy lands a melee hit may trigger several times each round and is much stronger. Scrutinise frequency, targets and stacking.

### Saving throw protection

Use targeted advantages and limited defensive powers rather than handing out unchecked permanent **+3 or +6 to saves**. A basilisk helm might resist petrification; an eldritch lining might help against fear. A broad anti-condition benefit should normally be rated higher than resistance to a very narrow source.

### Resistance and immunity

**Permanent resistance to one meaningful damage type is a substantial effect**, as illustrated by published Rare Armour of Resistance. Full damage **immunity** should be an **exceptional Legendary, extraordinarily rare and entirely GM-approved** benefit. Prefer temporary immunity, charges or narrowly defined dangers when possible. It can fundamentally change encounters and should never be automatically awarded for a monster material's origin.

{{footnote ARCANE FORGE | ARBITRATION · 3}}
{{pageNumber,auto}}

\page
{{wide,chapterhead
# GM ARBITRATION
## 4. Unusual items, movement and utility

An item that deals no damage can still bypass an encounter, reveal a mystery or trivialise an adventure. Evaluate **what the character can achieve**, both in and out of combat.
}}

### Movement and travel

| Scope | Potential constraints |
|:--|:--|
| Modest jump, crawl or climb | Speed, distance, terrain or anchor limitation |
| Reusable swing or significant mobility | Reach, movement spent, anchor availability, direction |
| Encounter-changing flight or teleport | Duration, action economy, charges, rest recharge |
| Adventure-changing travel | Destination restrictions, frequency, rarity and story consequences |

A web-line that requires an anchor and spends movement is not unrestricted flight. **Published Uncommon fifth-edition items can already grant flight**, so do not automatically classify *all* flying abilities as Legendary. Judge limits and the exact power.

### Stealth and invisibility

Camouflage in a particular setting is not the same as temporary invisibility; temporary invisibility is not unrestricted invisibility. Invisible characters are not automatically silent or impossible to track. Permanent, unrestricted invisibility deserves far more scrutiny than a short, clearly limited stealth ability.

### Information and detection

Ask what is detected, **how far away**, **how accurately**, **how often** and how much detail it reveals. If a completed item genuinely detects nearby magic, **honour that ability**, even if it changes a prepared plot. Avoid secretly disabling an approved item solely to hide a story secret. Set sensible boundaries *during design*.

### Healing and support

Assess amount of restoration, activation action, targets and rest limits. Continuous regeneration during combat is a very substantial benefit, more dangerous than a small once-daily burst of healing. Buffs affecting an entire party may be stronger than benefits limited to one wearer.

### Summoning and companions

A player may create an item that summons **one substantial companion** or **several minions**. Both are legal design concepts at GM discretion, with no compulsory hard creature caps from Arcane Forge. The GM judges power, count, turns, durability, duration, control and rest uses.

**Optional minion procedure:** Small fragile summons use simplified statistics and act together, perhaps with one coordinated attack or group task. This avoids five powerful independent action sets. One named guardian can instead use an appropriate monster stat block and an agreed command cost, possibly a bonus action.

Giving a summoned creature 1 HP **does not** make it harmless if it still grants powerful extra attacks every round. Treat total action-economy gain as a central power cost.

### Additional AC from trinkets

Use the printed rarity and attunement of published protection items: a **Ring of Protection (Rare)** and **Cloak of Protection (Uncommon)** each provide +1 AC and +1 to saving throws while attuned. For a **bespoke** accessory granting a broad and permanent AC bonus, **normally require attunement** and review the final equipped AC against the advisory thresholds in *GM Arbitration: AC, mitigation and retaliation*. There is **no mandatory one-item cap** and the thresholds are **not absolute ceilings**. The GM may refuse, narrow or redesign a new stacking benefit **before** crafting; previously approved benefits are not secretly rewritten.

{{art,height:300px
![](https://raw.githubusercontent.com/Omegaoliverid/Arcane-Forge-/929584c986ec54a4163f99de0b38b8aff455d61a/af-33.jpg)
}}

{{footnote ARCANE FORGE | ARBITRATION · 4}}
{{pageNumber,auto}}

\page
{{tightpage
&nbsp;
}}

# GM ARBITRATION
## 5. Preparing outcomes and resolving edge cases

### Optional quick-preparation protocol

If the player wants a major bespoke magical creation, invite them to declare **the design goal and proposed ingredients at the end of a session or before the next downtime scene**. The GM may then draft three **one-line** Sound / Refined / Exceptional results in advance; for simple or spontaneous creations, **one agreed result is always acceptable**. This preparation protocol is recommended, **not** a compulsory multi-session delay or a new skill check. The GM should state binder, attunement, DC, hours, expected final rarity and special losses *before* the dice are rolled. Record these in one place instead of renegotiating hidden powers afterward.

### A minute at the table

1. Player describes ambition and relevant materials.
2. GM considers the finished item's **entire** rarity and acceptable power.
3. GM chooses **one agreed result** or writes **three one-line hidden versions**.
4. Requirements are checked: tools, rank, blueprint/training, CU, magical components, **binder if required**, attunement, workshop, time.
5. The crafter makes the normal rolls and the GM applies catastrophe/setback rules **before** any hidden-card reward.
6. Reveal the result; the player records the item's complete rules.

### A simple card template

| Project | Rarity | A — Sound | B — Refined | C — Exceptional |
|:--|:--|:--|:--|:--|
| __________ | ______ | __________ | __________ | __________ |

Underneath, record **limits**: attacks per turn / targets / uses / DC / range / duration / concentration-like condition / attunement. **All three are pre-approved**; the GM should be prepared for the player to earn C through a great total or an unused 20.

\column

### Item outcome versus crafting catastrophe

A total that barely misses the four-stage target is **not** the same as meeting the target and receiving Sound. The existing partial/flawed/rework setback tables apply; the GM may describe a partially functioning item, but does not pretend a failed creation earned its standard fully successful hidden result. A nat 20 unused after cancelling ones rewards **choice after success**, not retroactive elimination of a catastrophe caused by a low total.

### Rolls with disadvantage

If there is no suitable blueprint, roll **two d20 at each stage and keep the lower**. Only the kept die is checked for natural one/twenty cancellation and added to the total. The separate +5 DC penalty for crafting above rank still applies if relevant. Disadvantage is never stacked on itself.

### Repeated recipes

Only an **exact successful recipe** becomes familiar. A change in material identity or substantial magical abilities may produce a new unfamiliar recipe, even within a known family blueprint. Guild and mentor trials always retain four stages. The GM may simplify trivial established mundane work without inventing extra dice.

### Highly unusual requests

When an item grants total protection, repeated stunning, unrestricted spellcasting, limitless regeneration, many extra creatures or campaign-spanning teleportation, return to the five arbitration questions and comparable fifth-edition abilities. If no balanced version exists at the proposed rarity, explain the higher-tier project or material quest that could eventually make it viable.

### Difficult adjudication at the table

The GM may use these pages in full, in part or not at all. If an edge case remains unclear, make a fair transparent provisional ruling, record what was agreed, and review it with the player after the session. Do not rewrite a revealed reward secretly because it performed better than expected.

{{footnote ARCANE FORGE | ARBITRATION · 5}}
{{pageNumber,auto}}

\page
# THE MONSTER MATERIAL ATLAS
## Inspiration, never automatic bonuses

Every recovered part carries clues to the creature it once belonged to. A horn remembers impact; silk remembers tension; a heart may still hum with an impossible power. The material's **physical form**, the creature's abilities, **any binder the design requires**, the maker's intent and the approved item rarity determine what the finished work can achieve.

{{wide
| Harvested part | Physical use | Magical or narrative directions |
|:--|:--|:--|
| Claw / talon | Blade, fang hook, striking edge | Precision, ferocity, bleeding, grip |
| Horn / tusk | Spearhead, pommel, reinforcement | Impact, thunder, charges, strength |
| Tooth / fang | Dagger, points, ornament | Poison, hunting, piercing, predator sense |
| Bone | Reinforcing core, grip, engraved focus | Spirit, necrotic resonance, protection |
| Hide / fur | Armour, lining, gloves, cloak | Camouflage, warmth, toughness, scent |
| Scale | Facing, plates, shield covering | The creature's environment or element |
| Shell | Rigid defence, shield face | Absorption, barriers, resilience |
| Chitin / scute | Lightweight plate, serration | Segmentation, poison, acid, escape |
| Feather | Fletching, mantle, charm | Wind, gliding, sight, radiant themes |
| Tendon / sinew | Bowstring, moving joints | Flexibility, reach, speed, reflex |
| Spines / spikes | Armour edging, hooked weapon | Retaliation, intimidation, grappling |
| Whiskers / antennae | Sensor charm, focus threads | Detection, warning, awareness |
| Spider silk / web | Textile, lashings, line launcher | Binding, climbing, movement |
| Pseudopod / ooze | Magical seal, lining, reagent | Corrosion, slipperiness, reshaping |
| Eye / gland / organ | Special ingredient, focus | Creature-specific sense, venom or essence |
| Heart / magical core | Major special ingredient or binder | Signature extraordinary property |
}}

### How a material changes across rarity

A low-tier fang may make a distinctive dagger that glows near its prey. A stronger monster's fang might plausibly be worked into a weapon with modest creature-specific damage or a limited poison effect. A Rare design might deliver a strong poison or short restraint. Legendary may combine an extraordinary predator-themed ability with another signature effect. **None of these is guaranteed by merely owning the fang.**

### Pristine doesn't create magic

Pristine signifies exceptional recovery and preparation. It increases **effective material rarity one tier**, capped at Legendary. It does not turn mundane bone into a spellcasting relic by itself. A Pristine Legendary trophy can support an extraordinary conversation, but offers no mandatory additional damage die or AC bonus.

### Material quantity and magical quality are separate

**One CU of Common bone** and **one CU of Legendary bone** represent the same standard *amount*, not the same magical possibilities. Conversely, possessing 30 CU of Legendary material does not automatically make a Legendary item: rank, suitable knowledge, **binder when required**, balance and crafting risk remain.

{{forge
##### Ask at the workbench
Ask the player: "What did the monster do that you want your creation to remember?" Then ask: "What must the finished item give up, or under what circumstances must it work, to stay within the intended rarity?" This often creates more interesting equipment than a list of flat bonuses.
}}

{{art,height:330px
![](https://raw.githubusercontent.com/Omegaoliverid/Arcane-Forge-/929584c986ec54a4163f99de0b38b8aff455d61a/af-35.jpg)
}}

{{footnote ARCANE FORGE | MATERIAL ATLAS}}
{{pageNumber,auto}}

\page
# EXAMPLE CREATIONS
## Three creatures, many possible creations

A single harvest can suggest a charm, a weapon or a more ambitious work. These examples give each material a different purpose across the rarity tiers; no creature part guarantees a particular magic merely by being recovered.

### The Basilisk's Legacy

**Uncommon — Eye-Watcher Pendant:** The wearer can recognise a carved likeness of a basilisk or sense a petrified creature within a short, GM-defined distance, provided no thick barrier blocks the effect. No attack or AC bonus.

**Rare — Petrifier's Edge:** A weapon with no universal attack enhancement, but a **once-per-long-rest** magical attack ability that can briefly restrain one eligible creature on a failed **DC 15 Constitution save**, themed as stiffening stone. A target's type and duration are fixed during design.

**Legendary — Stonewarden Mantle:** A thematically powerful mantle whose wearer receives strong petrification protection, with a limited power to protect one nearby ally. The GM sets duration and uses, compares against published equipment and avoids automatic all-damage immunity.

### The Storm Hunter

**Common — Static-Finder:** A small charm hums faintly before an approaching natural storm. Useful roleplay, not a guaranteed combat warning of every lightning-based monster.

**Uncommon — Lightning-Kissed Spear:** +1 to attack and damage; at GM discretion a very narrow creature-specific secondary effect may be possible instead of more general power.

**Rare — Thundercoil Lance:** No universal enhancement; a significant thunder effect with limited uses, or a +1 version with a narrower sonic strike. A GM could use **DC 15** for an associated saving throw.

### From a Giant Spider

**Common — Spinner's Thread:** Produces small quantities of harmless adhesive thread useful in craftwork or travel.

**Uncommon — Reach-Line Bracers:** Limited short-range web line that pulls a small object or reaches a nearby anchor; restrained targets are **not** automatic.

**Rare — Webspinner Bracers:** Refer to GM Quick Reference 03 for the complete Sound, Refined and Exceptional progression. Functioning organic machinery may require specialist training.

\column

### A mixed-scale experiment

Red and black dragon scales layered into a shield could be used for a **single stronger thematic protection** or the emergent **Caustic Steam** ability described earlier. The GM may decide that the mixed shield is unusual but not more powerful than a simpler single-dragon design of the same rarity.

{{art,height:650px
![](https://raw.githubusercontent.com/Omegaoliverid/Arcane-Forge-/929584c986ec54a4163f99de0b38b8aff455d61a/af-36.jpg)
}}

{{footnote ARCANE FORGE | EXAMPLES}}
{{pageNumber,auto}}

\page
{{wide,editorialText
{{wide,chapterhead
# LEGENDARY INSPIRATIONS
## Names whispered in the guild halls

Some commissions are passed down as stories long before a smith finds the courage to attempt them. Six such works are described below. Each begins with a rare creature, an impossible material and a maker's own ambition.
}}

### Ashrender, Fang of the Molten Wyrm

The tooth of an elder fire-wyrm forms its blackened edge; molten glandstone is sealed beneath the grip with scales that still hold furnace heat. When drawn, a thin seam of fire wakes in the steel. A master might pursue a **+3 blade**, or trade some of that raw enhancement for a limited eruption of dragon-flame. Its power is chosen **before** forging, not accumulated after success.

### Gravetongue, the Maw That Feeds

Twin daggers of gravebone and night-fed fangs, wound with dark heart-sinew and a scarce funerary binder. They hunger most keenly when a foe is near defeat. The enchantment might offer **limited life-draining strikes** or a brief pulse of borrowed vitality; its healing needs a declared use limit and cannot endlessly multiply with extra attacks.

### Starspike, Spear of the Rift Treader

The haft contains sky-fallen timber; a splinter of folded voidglass rests inside the spearhead. On a true thrust, the tip seems to reach a heartbeat farther than it ought. A Legendary design might permit a **short spatial step**, a bounded psychic wound or a momentary displacement of one foe—not all three without restraint.

### Mantle of the Emberborn

A cloak woven from heat-proof salamander silk, lined with wyrm scale dust and fastened by an emberglass clasp. Its wearer could walk through a blaze, answer one killing strike with an eruption or briefly take on a furnace-lit aspect. The maker decides whether its highest purpose is **survival, retaliation or transformation**.



### Sea-King Scale Armour

Long plates shed by a leviathan are sewn over flexible deepwater leather, each seam sealed with tide-resin. The suit might carry its wearer through black ocean trenches and provide a **powerful but limited defence** against the pressure or violence found there. One royal scale is not enough: a full suit still demands the necessary structural CU.

### Aegis of the Oathkeeper

Radiant fragments set into a battle-worn harness are joined with silver oathwire and a single dawn-crystal. When a companion falters, the armour answers. A finished Aegis might shelter an ally from one blow or raise a brief radiant ward; **target, reaction cost and uses** belong to the approved design.

{{forge
##### A legend begins with a choice
These are legendary **design possibilities**, not fixed recipes or bundles of bonuses. For each commission, agree the complete effect, rarity, attunement, saving throws, charges and crafting requirements before the first roll. Every material must justify the story of the finished item.
}}
}}

{{wide,art,featureArt,height:300px
![](https://raw.githubusercontent.com/Omegaoliverid/Arcane-Forge-/929584c986ec54a4163f99de0b38b8aff455d61a/af-37.jpg)
}}{{footnote ARCANE FORGE | LEGENDS}}
{{pageNumber,auto}}

\page
{{wide,chapterhead
# REVERSE ENGINEERING LEGENDS
## What lies at the heart of a wonder?

The oldest Guild cabinet contains sketches of marvels no living master claims to have built. Beneath each drawing are notes on the creature hunted, the substance sought and the unlikely work that might bind them together. These are **original Arcane Forge commissions**, each with its own limits and character.
}}

| The commission | A trail of materials and a possible wonder |
|:--|:--|
| **Wayfarer's Fold-Satchel** | Folded void-moth silk, a cavern-shell hinge and duskglass seal. Carries more than its size suggests, but must unfold at a stable resting place to surrender its contents. |
| **Vitalheart Torque** | A phoenix-fern root, warmstone and silver pulse-wire. Steadies a faltering body for a short spell; it cannot erase every wound or illness. |
| **Crown of Borrowed Thought** | Thoughtglass flakes set into a circlet of memory-bark. Lets its wearer recall one carefully studied pattern with uncanny clarity, then goes quiet. |
| **Manyweather Ewer** | Rain-imp pearl, mineral-spring clay and a coil of changing copper. Condenses a few useful liquids, but not an endless supply or any chosen poison. |
| **Snowward Striders** | Frostmarten pelt and winterglass beads stitched into heavy soles. Preserve a traveller's footing on ice and give brief shelter from deadly cold. |
| **Whisperglass Signet** | A dreaming oyster's pearl and a sliver of silent crystal. Blurs one probing thought, while leaving ordinary words and faces untouched. |
| **Blinkstitch Mantle** | Rift-moth thread and a single shard of stepstone. Once awakened, slips its wearer across a short visible gap before the weave needs rest. |
| **Stillpoint Pin** | Anchor-ore, gravitic shell and a locking star-rune. Holds one small object motionless for a little while; the enchantment falters under excessive load. |
| **Revealer's Emberlantern** | Clear basilisk glass and a flicker stolen from a truth-flame. Briefly outlines concealed tracks or veiled objects within its light. |
| **Skyweb Soles** | Giant-spider adhesion glands, white silk and resin of the cliff-root. Permit a short, deliberate climb on sound surfaces rather than effortless endless wall-walking. |

A blueprint teaches the **item and material families**, not these names as automatic recipes. The GM and player agree the finished rarity, range, duration, uses and any binder **when required**, then apply the normal CU, time, rank and crafting rules. One discovery may be enough to turn a rumour into a commission.

{{forge
##### From a rumour to a quest
A merchant owns the Fold-Satchel's empty brass hinge, but not the moth-silk that makes it work. The last colony breeds in an abandoned observatory where the stairs change direction every dusk. The hinge is for sale; the secret of the weave is not.
}}

{{art,height:580px
![](https://raw.githubusercontent.com/Omegaoliverid/Arcane-Forge-/929584c986ec54a4163f99de0b38b8aff455d61a/af-38.jpg)
}}

{{footnote ARCANE FORGE | ITEM INSPIRATION}}
{{pageNumber,auto}}

\page
{{wide,editorialText
# DREAMS OF GREATER MAGIC
## The impossible shelf

*In every Grandmaster's workshop sits a shelf for things that have not been made. A sketch pinned beneath a dragon scale. A crystal that refuses to cast a shadow. A promise written in a hand long dead. One day, someone will gather the right materials and dare to try.*

| Dreamed-of wonder | What a maker might seek — and what it might become |
|:--|:--|
| **Hollowstar Veil** | Dusk-moth silk, mirror-eel oil and a lightless geode clasp. It dims the wearer's outline while still, but quick motion disturbs its secret. |
| **Meridian Mantle** | Moon-bleached starworm silk, seven prism scales and ink drawn at an eclipse. Its stitched constellations might briefly turn a hostile spell aside. |
| **Skyroot Sceptre** | Heartwood from a storm-struck sky-tree, bottled aurora and a lightning-knot binder. Stores a small number of captured sparks for a ward or a thunderous answer. |
| **Stormwake Blade** | Fulgurite heart, rain-tempered alloy and a ribbon of wind-thread. Its edge can wake the storm in a chosen strike rather than calling endless lightning. |
| **Wyrmcrest Bracers** | Naturally shed elder-dragon scales, carved horn rings and emberglass. They lend the wearer's hands a fleeting draconic resilience, not an entire dragon's defences. |
| **Hearthkeeper's Gauntlets** | Healing-vine fibre, warmstone and living resin from a kindly hearth-spirit. Their stored warmth might close one desperate wound or shelter a companion from the cold. |
| **Tempest's Promise Girdle** | A thunder-giant's discarded chain link, storm-sinew and cloudstone buckle. Once in a while, its wearer can bear an impossible weight or deliver a mighty shove. |
| **Orbit of the Unwritten Name** | Astral pumice, a precision-cut memory crystal and an empty silver ring. A tiny stone circles the maker, preserving one learned insight until deliberately released. |



### Smaller wonders with stories of their own

| Commission | Beginning of an adventure |
|:--|:--|
| **Graspvine Anklets** | Cliff-root fibres that awaken on bare stone; rescue the gatherer stranded above the ravine. |
| **Whisperpin Earring** | A matched pair cut from one singing pearl; the second half went down with a courier ship. |
| **Evercoil Rope** | Living marshvine spliced with spider silk; the rope only obeys the knot it was taught. |
| **Shroudcap Mask** | Veilmoss leather and a shed mimic-skin; disguises a silhouette, not a voice or history. |
| **Driftfeather Sandals** | Rare sky-bird plumes and wind-resin; a few heartbeats of lift may cross the broken bridge. |
| **Bulwark of the Undying Shell** | A shell from the oldest sea-tortoise; its promise is one last stand, never permanent invulnerability. |

The materials open a possibility; **the finished item is decided before the forge is lit**. Its actual powers, rarity, activation, limits and attunement are settled using the normal GM creation guidance.
}}

{{wide,art,featureArt,height:255px
![](https://raw.githubusercontent.com/Omegaoliverid/Arcane-Forge-/929584c986ec54a4163f99de0b38b8aff455d61a/af-39.jpg)
}}{{footnote ARCANE FORGE | GREATER MAGIC}}
{{pageNumber,auto}}

\page
{{wide,chapterhead
# THE STORIES BEHIND THE MATERIALS
## Three journeys from rumour to forge
}}

**The Bell Beneath Asterdeep.** The last coral-smith works in a drowned arcade where seawater shines through broken arches. Her apprentice vanished while trying to free a *breathing pearl* from the bell tower of a sunken shrine. The pearl is not a trinket to steal: it keeps a colony of living coral from suffocating. The party must reach the tower, learn why the bell has fallen silent and return with a way to divide the pearl's living light without killing the reef. In gratitude, the smith will teach **living-coral jewellery up to Rare**. She cannot teach a breathing breastplate or every other living mechanism simply because they, too, grew beneath the sea.

**The Spiderwright's Unfinished Loom.** In a half-submerged tower above the blackwater marsh, a young silkweaver has kept a harvested spinneret alive for thirteen nights. The thread it produces is strong enough to anchor a bridge, yet breaks whenever the morning mist rises. Her former tutor knew how to bind the strands, but his tools lie beyond a flooded causeway where the old web-bridges have fallen. Recover the brass tension combs and a vial of moon-resin, then help her save the spinneret before it fails. She offers **specialist training in functioning silk-launching bracers**, not a general blueprint for all chitin armour. The final enchantment still has to survive the crafter's own rolls.

**The Mark Beneath the Ash.** A smith recognises the maker's mark on a battered family blade offered for scrap. It belongs to the apprentice who disappeared after a Guildmaster's disastrous final commission. Inside the hilt is a slender strip of Pristine metal, enough for one extraordinary upgrade if the old blade can be saved. The Guild will pay handsomely to reclaim the relic; the family wants it restored; the player might be the only forger willing to risk its destruction. Following the mark reveals the lost workshop and a rival who knows why the last attempt failed. The choice is not simply what to make, but **whose story the finished item will carry**.

### Let the work change the world

Knowledge can be a teacher, stolen design or rediscovered technique; reputation can become a commission, an enemy or a debt repaid. Neither cancels the ordinary requirements of materials, suitable training, crafting risk or GM approval. A great creation should leave a mark beyond its statistics.

{{storyPair
{{art,height:360px
![](https://raw.githubusercontent.com/Omegaoliverid/Arcane-Forge-/929584c986ec54a4163f99de0b38b8aff455d61a/af-40-1.jpg)
}}

{{art,height:360px
![](https://raw.githubusercontent.com/Omegaoliverid/Arcane-Forge-/929584c986ec54a4163f99de0b38b8aff455d61a/af-40-2.jpg)
}}
}}

{{footnote ARCANE FORGE | ADVENTURE IDEAS}}
{{pageNumber,auto}}

\page
# FINAL RULES AT A GLANCE
## Keep these standards consistent

{{wide
| Question | Authoritative answer |
|:--|:--|
| What is the harvesting DC? | CR 0–2:10; 3–6:15; 7–12:20; 13–16:**23**; 17+:25 |
| How does Pristine work? | **Successful harvest**, with natural 20 or total ≥DC+10; one material tier up, including Rare → Very Rare |
| How much material is needed? | CU coverage / weapon chart and sensible supporting supplies |
| What is a metal CU? | One **2 lb workable billet** |
| What does a blueprint cover? | Item family + material family + max rarity, and lower rarities |
| Can players try without a blueprint? | Yes. Apply disadvantage to the **required checks**: four stages for new work, or the single check for eligible familiar work |
| Can they forge above rank? | One rarity up, **+5 DC each stage**; penalties stack |
| Is there an enchanting roll? | No separate mandatory set; four integrated stages |
| Core targets? | Common 48 / Uncommon 56 / Rare 68 / Very Rare **72** / Legendary 80; special masterpiece 100 |
| When should a GM review combined AC? | Advisory only: levels 1–4 AC 21+, 5–10 AC 23+, 11–16 AC 25+, 17–20 AC 27+; **not caps** |
| What does an uncancelled natural 1 do? | Catastrophe (after four-stage natural20 cancellations) |
| When is total failure catastrophic? | Final result at least 10 below target |
| What if they have unused nat20 and succeed? | If using three pre-approved results, reveal them; **player chooses** |
| Do all failed attempts destroy the base? | No. Setbacks usually protect base; catastrophe risks it |
| Do repeats grant XP? | At-rank success **1d20**; first new at/above **2d20**; meaningful failure **1d10**; below rank **0** |
| Is advancement automatic at an XP threshold? | No. Requires actual Guild or mentor test |
| Does a Master mitigate bad luck? | Once/project reroll a natural 1 (Grandmasters too); new result stands |
| Do all magic items need a binder? | No. Minor magic may omit; elevation and high-tier enchantments normally need one |
| Can a Master make a +3 weapon? | Yes. Very Rare +3 weapon is within Master capability |
| Does an item need attunement? | GM declares before crafting; normal 2014 attunement rules apply |
| Does Guild keep the exam item? | Yes, generally |
| Does mentor keep the student's normal exam item? | No; successful student keeps it |
| Can mixed monster materials combine? | Yes, GM judges the **whole** result |
| Does physical coverage guarantee magical benefits? | No |
| Can a character upgrade equipment later? | Yes, with new work and real risk |
| Are GM quick-reference sheets compulsory? | No; useful optional decision aids |
}}

{{note
##### Compatibility
These are **independent 5E-compatible homebrew rules**, not an official publisher's rulebook. They intentionally depart from published magic-item manufacturing and downtime economics. Compatibility with other game systems would require independent adaptation and testing.
}}

*An unmade legend is just an idea. Pick up the hammer.*

## Forge Your Story. Craft Your Legacy.

{{footnote ARCANE FORGE | AT A GLANCE}}
{{pageNumber,auto}}

\page
{{wide
# PLAYER CRAFTING TRACKER
## Reproduce as often as needed

### The forger

**Character:** __________________________   **Maker's mark:** __________________________

**Rank:** __________________   **Crafting XP:** ______ / ______   **Primary trade:** ________________

**Secondary trade (Grandmaster):** __________________  **Relevant tools:** _____________________

### Blueprints and training

| Item family | Material family / specialist scope | Highest rarity known | Teacher / source |
|:--|:--|:--|:--|
| &nbsp; | | | |
| &nbsp; | | | |
| &nbsp; | | | |
| &nbsp; | | | |
| &nbsp; | | | |

### Material inventory

| Component and creature source | Material tier / Pristine? | Count, weight or CU | Notes |
|:--|:--|:--|:--|
| &nbsp; | | | |
| &nbsp; | | | |
| &nbsp; | | | |
| &nbsp; | | | |
| &nbsp; | | | |
| &nbsp; | | | |
| &nbsp; | | | |

### Known successful exact recipes

| Finished creation | Item / material family | Rarity | Familiar? |
|:--|:--|:--|:--|
| &nbsp; | | | |
| &nbsp; | | | |
| &nbsp; | | | |

### Active project

**Name / concept:** _________________________________________________________

**Current base item:** ________________ **Intended rarity:** ________________

**Blueprint / training:** ______________ **Binder (if required) / source:** ___________________

**CU committed:** __________ **Special ingredients:** _____________________________

**Workshop / time allocated:** __________________________________________________

**Finished abilities:** _________________________________________________________
}}

{{footnote ARCANE FORGE | PLAYER TRACKER}}
{{pageNumber,auto}}

\page
{{wide
# GM WORKSHEET
## One minute before the hammers fall

**Player's ambition:** ________________________________________________________

**Item shape / family:** __________________ **Material family:** _____________________

**Rank:** __________ **Knowledge:** __________ **Item tier:** ______________________

**Which monster parts justify the effect?** ______________________________________

**Binder needed? Why/why not? Tier, source and availability:** ________________________

**CU and other structural materials:** __________________________________________

**Activation, range, targets, rest limits, saving DC and attunement:**

___________________________________________________________________________

### Fast five-step reminder

| Step | Ask / do |
|:--|:--|
| **Imagine** | What does the player want most? |
| **Match** | Do the materials support the effect? |
| **Balance** | Is the complete item fair for the rarity and campaign? |
| **Prepare** | Agree one result, or write three short hidden cards. |
| **Forge** | Check eligibility, DC, time, roll and reveal. |

### Optional three creation cards

| A — Sound | B — Refined | C — Exceptional |
|:--|:--|:--|
| &nbsp; | | |
| &nbsp; | | |
| &nbsp; | | |

### Four-stage result register

| Stage | Kept natural d20 | Full modified result | Observations |
|:--|:--|:--|:--|
| 1 | | | |
| 2 | | | |
| 3 | | | |
| 4 | | | |

**Rarity DC/stage:** _________  **Above rank +5/stage?** _________  **Disadvantage without blueprint?** _________

**Target:** _________ **Total:** _________  **Natural 1s:** _________ **Natural 20s:** _________

**Master reroll used?** ______ **20s cancel 1s:** ______ **Unused 20s:** ______ **Catastrophe?** ______

**Final outcome / chosen card:** __________________________________________________

**Materials consumed / returned:** _______________________________________________

**Experience awarded (2d20 new / 1d20 repeat at rank / 1d10 meaningful failure / 0 below rank):** ______
}}

{{footnote ARCANE FORGE | GM WORKSHEET}}
{{pageNumber,auto}}

\page
![The Artisan](https://raw.githubusercontent.com/Omegaoliverid/Arcane-Forge-/929584c986ec54a4163f99de0b38b8aff455d61a/af-44.jpg){position:absolute,top:0px,left:0px,width:100%,height:100%,object-fit:cover}

\page {tdiary,tdtitle}

{{tdtext
<h1>The Diary of Tomas Brack</h1>

<p data-source="1" class="subtitle"><em>The Measure of a Craftsman.</em></p>

<p class="editor">A battered leather journal, its corners darkened by heat. The first pages are filled with a boy’s careful measurements, diagrams and lists of mistakes. Later come sketches of strange materials, broken tools, finished commissions and the occasional letter tucked between the pages. The handwriting grows firmer with the years. The entries grow fewer, but rarely less precise.</p>
}}

{{footnote ARCANE FORGE | THE DIARY OF TOMAS BRACK}}
{{pageNumber,auto}}
\page {tdiary,boy,twocol}

{{tdtext
<h2>I. The Initiate</h2>

<p data-source="4" class=""><strong class="date">First week, Holloway’s workshop.</strong> Mother says I am fortunate. Old Holloway takes one Initiate a year, and this year he chose me.</p>

<p data-source="5" class="">His workshop is nothing like I imagined. No great furnace, no racks of shining swords. Mostly rings, clasps, buckles, cloak pins and little charms that travellers buy to remind themselves of home.</p>

<p data-source="6" class="">I asked when we would begin the important work. He handed me a file and a crooked brass ring.</p>

<p data-source="7" class="">“When you can tell me why that is crooked, we’ll begin.”</p>

<p data-source="8" class="">I spent the morning filing it. He made me start again.</p>

<p data-source="9" class=""><strong class="date">Third week.</strong> I understand the ring now. Not entirely, but enough to know I was wrong. The shape was never the problem. The metal had been worked unevenly, with more tension on one side than the other. Every time I forced it straight, it tried to bend back.</p>

<p data-source="10" class="">Holloway heated it, made one careful adjustment, and set it on the bench. Perfect. He didn’t say anything.</p>

<p data-source="11" class="">I asked how long it had taken him to learn that. “Longer than it should have.” Then he went back to his work.</p>

<p data-source="12" class=""><strong class="date">Second month.</strong> My first proper commission: a ring set with a single scale. I had the blueprint, Holloway checked the materials, and everything was laid out correctly. The work went well, right up until the very end.</p>

<p data-source="13" class="">Then the scale split. A hairline fracture first, then a sharp crack through the setting. I tried to catch it, but I was too late. The whole piece was ruined.</p>

<p data-source="14" class="">I stood at the bench for several minutes, staring at what remained. Holloway came over and asked what had happened. I told him my hand had slipped.</p>

<p data-source="15" class="">“Why?”</p>

<p data-source="16" class="">I didn’t know.</p>

<p data-source="17" class="">“Then that’s what you need to find out.”</p>

<p data-source="18" class="">He made me draw the ruined setting in this journal from memory. I thought he was being cruel. By evening I realised the scale had been seated against a ridge I hadn’t properly removed.</p>

<p data-source="19" class="">The failure began long before my hand slipped.</p>

<p data-source="20" class=""><strong class="date">Fourth month.</strong> Six rings finished. One hums very faintly near running water. Holloway says the scale came from a creature that lived beside a river, and something of that life may remain in it. I don’t know whether he’s right, but the sound changes when the ring is turned. I’ve recorded the angle, distance and strength of the humming.</p>

<p data-source="21" class="">Holloway watched me for half an hour. Then he said something worth remembering.</p>

<p data-source="22" class="">“Steel has a memory, Tomas. Bone has a history. A good craftsman learns what the material can bear before asking it to become something else.”</p>

<p data-source="23" class="">I wrote it above my bench.</p>

<p data-source="24" class=""><strong class="date">First winter.</strong> Holloway gave me back the broken ring. Both halves. I asked why he’d kept them.</p>

<p data-source="25" class="">“Because you’ve been looking for that mistake in every piece you’ve made since.”</p>

<p data-source="26" class="">He was right. I check every setting twice. Sometimes three times. He said that was good, as long as I didn’t become so frightened of mistakes that I stopped trying anything new. Then he handed me a complicated design for a clasp.</p>

<p data-source="27" class="">Four days. Failed. Another four days. Succeeded.</p>

<p data-source="28" class="">He placed the finished clasp beside the broken ring. “Now tell me what you learned from both.”</p>

<p data-source="29" class="">We talked until the furnace went cold.</p>
}}

{{footnote ARCANE FORGE | THE DIARY OF TOMAS BRACK}}
{{pageNumber,auto}}
\page {tdiary,boy}

{{tdtext
<h2>II. The Wider Craft</h2>

<p data-source="31" class=""><strong class="date">Second year, spring.</strong> I thought becoming a craftsman meant learning to make things. It turns out it also means learning why things fail.</p>

<p data-source="32" class="">Metal cracks because it was worked badly. Leather tears because it was cut against its strength. Stone breaks because the stress was placed where it couldn’t carry it. Holloway says the mistake young smiths make is believing the hammer is always the answer.</p>

<p data-source="33" class="">Today he gave me a strip of leather and told me to make a fastening that wouldn’t tear. I asked where the hammer was.</p>

<p data-source="34" class="">He laughed. I haven’t heard him laugh before.</p>

<p data-source="35" class=""><strong class="date">Second year, autumn.</strong> Holloway took me to meet Wenna Thrale. She works with silk, sinew and the peculiar materials taken from creatures most sensible people avoid touching. Her workshop smells of oil, damp timber and something sweet I haven’t identified.</p>

<p data-source="36" class="">There is a very large spider in the cellar. I was told it was dead. I have decided not to investigate.</p>

<p data-source="37" class="">Wenna gave me three lengths of silk and asked which would bear the most weight. I chose the thickest. Wrong. She showed me how the fibres had been spun, then hung weights from each strand. The narrowest held almost twice as much.</p>

<p data-source="38" class="">I’ve spent years learning to work against the strength of metal. Wenna says that with silk, I must learn to work alongside it.</p>

<p data-source="39" class="">I asked if she would teach me. She looked at my hands, then at the strand I had chosen.</p>

<p data-source="40" class="">“Come back tomorrow. Bring your journal.”</p>

<p data-source="41" class=""><strong class="date">Third year, early spring.</strong> The Guild has accepted me for the Apprentice examination. Holloway says time at the bench doesn’t make an Apprentice. I must prove the work.</p>

<p data-source="42" class="">The fee is two years of saved wages. Holloway offered to lend me what I lacked. I declined. He looked pleased. Then he slipped five gold into my tool chest anyway.</p>

<p data-source="43" class="">I put it back. We have been doing this for three days.</p>

<p data-source="44" class=""><strong class="date">Examination day.</strong> Passed.</p>

<p data-source="45" class="">The examiners barely spoke. I made a cloak clasp that keeps the rain out. A small enchantment, but a precise one: there’s no point keeping a traveller’s shoulders dry if the water simply runs into their boots.</p>

<p data-source="46" class="">The Guild kept the clasp. I watched an examiner place it in a wooden case beside pieces made by other candidates. For some reason, that felt more important than the certificate.</p>

<p data-source="47" class="">Holloway met me outside and asked how it went. I showed him the certificate. He nodded, then handed me the five gold again.</p>

<p data-source="48" class="">“For your next lesson.”</p>

<p data-source="49" class="">I kept it.</p>
}}

{{footnote ARCANE FORGE | THE DIARY OF TOMAS BRACK}}
{{pageNumber,auto}}
\page {tdiary,apprentice}

{{tdtext
<h2>III. The Apprentice</h2>

<p data-source="51" class=""><strong class="date">Third year, summer.</strong> A full season back at Wenna’s. Holloway says I’ve learned enough about metal to begin understanding how little I know about everything else. Wenna seems to agree.</p>

<p data-source="52" class="">She has me working with silk, horn, scales, hardened chitin and something she calls living fibre. It shrinks slightly when warmed. It has ruined three pairs of gloves. The fourth pair fits perfectly.</p>

<p data-source="53" class="">Wenna says I’m beginning to listen. I think she means I’m learning not to force every material into the shape I imagined before I’d even touched it.</p>

<p data-source="54" class=""><strong class="date">Fourth year.</strong> A hunter brought a manticore’s tail spike to Holloway’s and asked for it to be set in a ring. It was curved, heavy and hard along one edge. I sketched four ring designs before admitting none of them made sense.</p>

<p data-source="55" class="">I asked him what he wanted the ring to do. “Keep me safe.” I asked what had nearly killed him. He said the manticore had pinned his brother to a tree with its tail.</p>

<p data-source="56" class="">I looked at the spike again. Not as an ornament. As a point.</p>

<p data-source="57" class="">I made him a hunting dagger instead, with the spike as its cutting point. It took several attempts to balance. When I handed it over, he held it for a long time without speaking. Then he tested the weight, turned it in his hand and smiled.</p>

<p data-source="58" class="">He said his brother would have liked it. I don’t think I’ve ever been prouder of a commission.</p>

<p data-source="59" class="">Holloway examined the dagger before it left. He said nothing about the ring. That evening he brought me a book of weapon designs. Not as a declaration of what I should become. As another thing I needed to learn.</p>

<p data-source="60" class=""><strong class="date">Fourth year, winter.</strong> I’ve been studying blades. Two swords of the same length and metal can handle entirely differently, depending on where the weight sits. A narrow blade can still strike heavily. A broad one can move quickly, if it’s balanced. And a weapon made from a monster must do more than look impressive. The person holding it needs to trust it.</p>

<p data-source="61" class="">Holloway noticed I’d spent three evenings sketching the same sword and asked whether I meant to make it. I said not yet.</p>

<p data-source="62" class="">“Good.” Then he sat beside me and pointed out six problems with the design. We corrected four. The other two will take more thought.</p>
}}

{{footnote ARCANE FORGE | THE DIARY OF TOMAS BRACK}}
{{pageNumber,auto}}
\page {tdiary,apprentice}

{{tdtext
<p data-source="63" class=""><strong class="date">Fifth year, Anvil Row.</strong> Holloway has arranged for me to study under Master Orrin Vey, a weaponsmith respected across the city. Vey read Holloway’s letter of introduction. Then he handed me a broom.</p>

<p data-source="64" class="">The first week, I swept. The second, I sorted billets. The third, I cleaned tools and recorded heat damage. By the fourth I was wondering whether he meant to teach me anything at all.</p>

<p data-source="65" class="">Then he asked why I’d separated two nearly identical billets. I explained the difference in their grain and impurities. He put down his hammer.</p>

<p data-source="66" class="">“Brack. Tomorrow, bring your tools.”</p>

<p data-source="67" class="">I slept badly.</p>

<p data-source="68" class=""><strong class="date">Fifth year, later.</strong> Met Callum Reave. He trained under Vey before me and knows the workshop better than anyone. He’s faster than me at shaping metal and infuriatingly good at telling when a blade is properly balanced.</p>

<p data-source="69" class="">The first time we worked together, he finished while I was still checking my measurements. He leaned over and asked whether I meant to forge the sword or write it a love letter. I told him he should try writing something down occasionally.</p>

<p data-source="70" class="">He laughed. We haven’t stopped arguing since.</p>

<p data-source="71" class="">Today I finished a blade before him. Mine needed less correction. His looked better. Vey told us they were both equally useless until properly tempered.</p>

<p data-source="72" class="">We spent the afternoon working side by side.</p>
}}

{{footnote ARCANE FORGE | THE DIARY OF TOMAS BRACK}}
{{pageNumber,auto}}
\page {tdiary,apprentice,twocol}

{{tdtext
<h2>IV. The Journeyman</h2>

<p data-source="74" class=""><strong class="date">Sixth year.</strong> Failed my Journeyman examination.</p>

<p data-source="75" class="">A longsword, and the hardest thing I’d attempted. Vey lent me half the fee. I had the right blueprint, the right tools, and everything prepared. My measurements were correct. My shaping was sound.</p>

<p data-source="76" class="">But I hurried the final binding. The blade survived. The enchantment didn’t fully take.</p>

<p data-source="77" class="">The examiner wrote two words beneath my name: <em><span class="guildslip">Promising. Impatient.</span></em></p>

<p data-source="78" class="">I wanted to argue. Vey read the report and asked whether it was accurate. I said yes. He told me to be back at the workshop in the morning.</p>

<p data-source="79" class="">I asked whether he was disappointed. “Of course. I expected you to pass.” Then he tapped the report. “But this tells me what we work on next.”</p>

<p data-source="80" class=""><strong class="date">Sixth year, winter.</strong> Callum has been helping me with timing. Not by teaching me to move faster. By making me stop. He works a piece beside mine and calls out every time I try to correct something before the metal is ready.</p>

<p data-source="81" class="">I find this deeply irritating. It is also working.</p>

<p data-source="82" class="">Vey says timing isn’t the same as speed. A fast craftsman finishes quickly. A skilled craftsman knows when to act. The best manage both. I’m not there yet.</p>

<p data-source="83" class=""><strong class="date">Seventh year.</strong> Passed.</p>

<p data-source="84" class="">Another sword, another fee I could barely afford. This time I didn’t hurry. The core came from a manticore’s spike, for luck as much as strength. At the last moment I felt the urge to push the binding further, to force a better result.</p>

<p data-source="85" class="">Instead, I waited until the metal was ready. The sword held. The Guild kept it.</p>

<p data-source="86" class="">The examiner studied the blade, then my old record. She crossed out <em><span class="correction"><s>impatient</s></span></em> and wrote <em><span class="correction learned">learning patience</span></em> beneath it.</p>

<p data-source="87" class="">I’ll take that.</p>

<p data-source="88" class=""><strong class="date">Seventh year, a choice.</strong> My Journeyman certificate arrived today, and with it the right to declare a specialisation.</p>

<p data-source="89" class="">I’ve spent years on rings, clasps, silk, leather, shields, tools and ornaments. There’s something in every craft I admire. Holloway’s tiny settings demand extraordinary care. Wenna’s living fibres can do things metal never will.</p>

<p data-source="90" class="">But when I work on a weapon, all those lessons come together. The fit of the hand. The balance of the blade. The purpose of its edge. The knowledge that someone may depend on it when they’re frightened, exhausted, or facing something stronger than themselves.</p>

<p data-source="91" class="">I told Holloway. He asked whether I was certain. I said I was.</p>

<p data-source="92" class="">He smiled. “Then you’ve made your first choice as a Journeyman.”</p>

<p data-source="93" class="">Today the Guild wrote it down: <em><span class="register">Tomas Brack, Journeyman Weaponsmith.</span></em></p>

<p data-source="94" class="">Not the end of my education. The beginning of learning one craft properly.</p>
}}

{{footnote ARCANE FORGE | THE DIARY OF TOMAS BRACK}}
{{pageNumber,auto}}
\page {tdiary,scar}

{{tdtext
<h2>V. Lessons Beyond the Blade</h2>

<p data-source="96" class=""><strong class="date">Eighth year, Wenna’s bracers.</strong> Back to Wenna Thrale. She’d heard about my specialisation. “Still making things with sharp ends?”</p>

<p data-source="97" class="">I said I was. She gave me a box of spider silk, prepared spinnerets and a design for a pair of bracers. I asked why she wanted a weaponsmith to make them.</p>

<p data-source="98" class="">“Because you think everything is a blade. Let’s see whether that’s still true.”</p>

<p data-source="99" class="">None of my weaponsmithing helped. It all came down to what she’d taught me about silk years before. Before I began, she laid three folded cards on the bench and wouldn’t tell me what was written on them. “What the bracers become depends on you.”</p>

<p data-source="100" class="">The final binding was the cleanest organic work I have ever managed. Wenna unfolded all three cards. “Your choice.”</p>

<p data-source="101" class="">I picked the one that could fire a line of web and hold fast to whatever it struck. Not the most aggressive. The most useful. She seemed pleased.</p>

<p data-source="102" class=""><strong class="date">One week later.</strong> Tried the Webspinner Bracers over the river. The line held. The anchor held. The bracers worked beautifully.</p>

<p data-source="103" class="">I did not. I misjudged the swing, struck the far bank and fell in. Wenna pulled me out with a pole. Callum had come along and was laughing so hard he could barely stand.</p>

<p data-source="104" class="">I pointed out that the invention had worked exactly as intended. Wenna nodded. “Then perhaps we should work on the inventor.”</p>

<p data-source="105" class="">Callum has mentioned it every time he’s seen me since. I’ve recorded the correct approach angle for future reference.</p>

<p data-source="106" class=""><strong class="date">Ninth year, the Midsummer forge-off.</strong> Callum challenged me to a public contest. Same materials, same time, same conditions: a hellhound’s jaw and dark iron. He chose an axe. I chose a sword.</p>

<p data-source="107" class="">Callum worked quickly, as always. His axe was taking shape while I was still preparing the jaw. By the second day his weapon looked magnificent. Mine was only beginning to come together.</p>

<p data-source="108" class="">I thought I had the better design. I still think so. But the forge doesn’t reward a design that never survives being made.</p>
}}

{{footnote ARCANE FORGE | THE DIARY OF TOMAS BRACK}}
{{pageNumber,auto}}
\page {tdiary,scar,injured}

{{tdtext
<p data-source="109" class="shaky"><strong class="date">Ninth year, third day.</strong> I knew the binding was failing a moment before it happened. There was heat beneath the steel that shouldn’t have been there. I tried to correct it. Too late.</p>

<p data-source="110" class="shaky">The magic let go all at once. The jaw fractured, the blade twisted, and fire leapt across the bench.</p>

<p data-source="111" class="shaky">I caught the falling metal in my right hand. A stupid thing to do. But the crowd was too close, and I wasn’t thinking about my hand. Only about where the blade might land.</p>

<p data-source="112" class="shaky">The sword was destroyed. So was most of the skin across my palm.</p>

<p data-source="113" class="shaky">Callum won. I don’t remember the judging. Only the healer’s tent and the smell of burnt cloth.</p>

<p data-source="114" class="shaky"><strong class="date">A few days later.</strong> Callum visited. He brought food, then set a small wooden grip on the table: an adjustable handle he’d made so I could practise with tools while my hand healed.</p>

<p data-source="115" class="shaky">I told him it was badly finished. He said he’d made it in a hurry. I said that explained a great deal. He smiled.</p>

<p data-source="116" class="shaky">After a while he asked why I’d caught the blade. I told him I didn’t want it falling into the crowd. He nodded. Then, quietly: “Next time, let me help.”</p>

<p data-source="117" class="shaky">We sat for another hour without saying much. He left the grip beside my journal. I use it every morning.</p>

<p data-source="118" class=""><strong class="date">Tenth year.</strong> The hand works again. Not perfectly. The scar is thick, and some mornings I can barely close my fingers until they’ve warmed.</p>

<p data-source="119" class="">Callum helped me change the grips on my tools. Vey rebuilt one workbench so I wouldn’t strain my wrist. Holloway sent a small ring to keep my damaged finger warm. Wenna sent a length of silk that bends without pulling at the scar.</p>

<p data-source="120" class="">None of them asked whether I meant to stop forging. They already knew the answer.</p>

<p data-source="121" class="">I used to think mastery meant becoming good enough to need no one’s help. I was wrong.</p>
}}

{{footnote ARCANE FORGE | THE DIARY OF TOMAS BRACK}}
{{pageNumber,auto}}
\page {tdiary,master,twocol}

{{tdtext
<h2>VI. The Master</h2>

<p data-source="123" class=""><strong class="date">Fourteenth year, the trial.</strong> My Master examination: a war pick built around a purple worm’s tooth. The most expensive thing I have ever attempted.</p>

<p data-source="124" class="">I spent weeks preparing. Checking the tooth. Studying the blueprint. Testing the fit of every part.</p>

<p data-source="125" class="">Vey watched me one evening and asked what I was afraid of.</p>

<p data-source="126" class="">“Failing.”</p>

<p data-source="127" class="">“You’ve done that.”</p>

<p data-source="128" class="">“Losing the materials.”</p>

<p data-source="129" class="">“Done that too.”</p>

<p data-source="130" class="">I looked at my right hand. He followed my gaze. “That as well.”</p>

<p data-source="131" class="">I asked what his point was. He smiled. “You’re still here.”</p>

<p data-source="132" class=""><strong class="date">Examination day.</strong> Passed.</p>

<p data-source="133" class="">I won’t pretend it was easy. The tooth resisted shaping. One joint needed correcting. The binding was difficult to settle. But I didn’t rush. I recognised the trouble before it became a failure and gave the material the time it needed. The pick held.</p>

<p data-source="134" class="">The examiner was the same woman who had judged my first Journeyman attempt. She remembered me. I knew she did when she looked at the scar across my palm. Then she wrote one word: <em><span class="guildslip">Steady.</span></em></p>

<p data-source="135" class="">Enough.</p>

<p data-source="136" class="">I am now Master Tomas Brack. The title doesn’t mean I’ve stopped making mistakes. It means I’ve learned more ways to recognise them.</p>

<p data-source="137" class=""><strong class="date">Later.</strong> Holloway congratulated me. So did Wenna. Callum arrived with a bottle of something expensive and said it was only fair that one of us finally became respectable.</p>

<p data-source="138" class="">Vey said nothing until the others had gone. Then he handed me a flawed blade he’d kept beneath his bench. “Tell me what’s wrong with it.”</p>

<p data-source="139" class="">Halfway through examining it, I noticed him smiling. The old bastard had been keeping that blade for years.</p>

<p data-source="140" class=""><strong class="date">Fifteenth year.</strong> Vey has died.</p>

<p data-source="141" class="">His workshop feels strange without him. Tools hanging exactly where he left them. Half-finished commissions. A cup on the shelf beside his chair.</p>

<p data-source="142" class="">He left the shop to me, with a short note: <em><span class="scrap">Sweep the floor.</span></em></p>

<p data-source="143" class="">So I did. Callum came that evening and picked up the second broom. We swept together. The shop opened the next morning.</p>

<p data-source="144" class=""><strong class="date">Sixteenth year.</strong> My first apprentice asked why I keep broken pieces. I showed her the ring from Holloway’s, the blade from my failed Journeyman exam, and what was left of the hellhound jaw.</p>

<p data-source="145" class="">She asked why I didn’t throw them away. I told her some lessons are expensive enough that you should keep the receipt.</p>

<p data-source="146" class="">She laughed, then asked if I would teach her. I gave her a file and a crooked brass ring.</p>

<p data-source="147" class="">Holloway would have enjoyed that.</p>
}}

{{footnote ARCANE FORGE | THE DIARY OF TOMAS BRACK}}
{{pageNumber,auto}}
\page {tdiary,master,sunrise}

{{tdtext
<h2>VII. Dawnsplitter</h2>

<p data-source="149" class=""><strong class="date">Seventeenth year, early autumn.</strong> A company of adventurers arrived with a material unlike anything I’ve worked: the horn of a sun-wyrm, a gold-scaled creature they had hunted for weeks along the eastern ridge. Two of them were wounded. One carried the horn wrapped in three layers of cloth.</p>

<p data-source="150" class="">They wanted a single weapon made from it. They’d pooled their reward, sold most of their spare kit, and come to me because another smith had told them it couldn’t be done.</p>

<p data-source="151" class="">The horn was warm despite the cold. At first light its heart glowed faintly, as if something inside it remembered the sun.</p>

<p data-source="152" class="">I told them I couldn’t promise success. One said they’d been warned. Before leaving, their leader set the horn on my bench.</p>

<p data-source="153" class="">“We don’t need you to make it quickly,” she said. “We need you to make it right.”</p>

<p data-source="154" class=""><strong class="date">Late autumn.</strong> The horn is remarkable. Its fibres run almost its whole length, growing denser towards the base. Heat changes how it bends, but not the way I expected. It doesn’t want to be forced around a metal core.</p>

<p data-source="155" class="">I’ve spent weeks on samples and sketches. Callum suggested abandoning the usual blade shape. Wenna agreed. Holloway, old enough now that his hands tremble in the mornings, studied my drawings and pointed to a narrow section near the hilt.</p>

<p data-source="156" class="">“That part will break.”</p>

<p data-source="157" class="">He was right. We redesigned the support. At last the design is possible. Not certain. Possible.</p>

<p data-source="158" class=""><strong class="date">The long winter.</strong> I’ve begun. Everything has to fit: the iron, the horn, the binding, the weight, the way the blade will move in its wielder’s hands.</p>

<p data-source="159" class="">For the first time in years, I feel like the boy staring at Holloway’s crooked ring. I’ve missed that feeling. Not the uncertainty. The discovery.</p>

<p data-source="160" class=""><strong class="date">Before dawn.</strong> Finished.</p>

<p data-source="161" class="">I should write it down while I still remember it clearly. The early work was hard but controlled. The horn responded once I stopped trying to make it behave like ordinary horn.</p>

<p data-source="162" class="">During the final binding, the glow inside the blade began moving towards the fuller. For a moment I thought the enchantment was escaping. Then I realised it was following the shape we’d designed. Not resisting it. Completing it.</p>

<p data-source="163" class="">The first sunlight came through the eastern window. The blade caught it, and two narrow beams spread across the floor, split by the greatsword’s edge.</p>

<p data-source="164" class="">I stood there for some time. I could hear the furnace, the birds outside, Callum breathing beside me. Then he said, very softly:</p>

<p data-source="165" class="">“Well, Brack. That’s quite a sword.”</p>
}}

{{footnote ARCANE FORGE | THE DIARY OF TOMAS BRACK}}
{{pageNumber,auto}}
\page {tdiary,master,sunrise}

{{tdtext
<p data-source="166" class=""><strong class="date">The naming.</strong> The adventurers came back three days later. Their leader lifted the greatsword, tested its balance, and raised it to the morning light. The light divided around the blade.</p>

<p data-source="167" class="">“Dawnsplitter,” she said. The others agreed at once.</p>

<p data-source="168" class="">I’d written several names in the margins of this journal. None was as good. I engraved <em>Dawnsplitter</em> beneath the guard, beside my maker’s mark.</p>

<p data-source="169" class="">When they had gone, I went back to the bench. For the first time, the workshop felt larger than the man standing in it.</p>

<p data-source="170" class=""><strong class="date">Eighteenth year, a name earned.</strong> People have begun calling me Dawnsplitter’s smith. Some just call me Dawnsplitter.</p>

<p data-source="171" class="">Last week a young apprentice came asking to meet the man who forged the greatsword. I told her my name was Tomas Brack. She looked disappointed.</p>

<p data-source="172" class="">I thought about Holloway. Wenna. Vey. Callum. The hunter and his manticore spike. The adventurers who trusted me with their most precious find. The broken ring still in my drawer. It took all of them, and years of work, to make that blade.</p>

<p data-source="173" class="">I went to the Guildhall and asked the clerk to change my maker’s name. He looked up. “To what?”</p>

<p data-source="174" class="register"><em>Tomas Dawnsplitter.</em></p>

<p data-source="175" class="">Brack stays on the first page of this journal. It is where I began. Dawnsplitter is what I have chosen to become.</p>

<p data-source="176" class=""><strong class="date">A letter from Mother.</strong> She asked whether I was ashamed of Brack. I wrote back that I wasn’t: the old name will always be mine, and I chose the new one because of something I made with the hands she raised.</p>

<p data-source="177" class="">Her reply was one sentence. <em><span class="motherletter">Then make it a name worth keeping.</span></em></p>

<p data-source="178" class="">I’ve pinned it above the bench.</p>
}}

{{footnote ARCANE FORGE | THE DIARY OF TOMAS BRACK}}
{{pageNumber,auto}}
\page {tdiary,master}

{{tdtext
<h2>VIII. The Night Before</h2>

<p data-source="180" class=""><strong class="date">Twenty-first year.</strong> I’ve started putting money aside for the Grandmaster examination. A little from every commission, in a box beneath Vey’s old bench. At this rate it will take me another three years.</p>

<p data-source="181" class="">Callum says I could ask the Guild for a loan. I could. I won’t. Holloway taught me better than that.</p>

<p data-source="182" class=""><strong class="date">Twenty-second year, spring.</strong> A letter from Wenna, the first in a long while.</p>

<p data-source="183" class="wennaletter"><em>I hear you are saving for the Guild’s examination. Don’t. Come and forge beside me instead. You have learned what steel can do. Show me what you have learned from everything else.</em></p>

<p data-source="184" class="">Wenna has been a Grandmaster for longer than I’ve been a smith. She has invited me to a qualifying mentor trial, under the agreed conditions for Grandmaster promotion. I must complete my part and strictly better her work. I’ve heard of it happening twice in my lifetime.</p>

<p data-source="185" class="">I read the letter four times. Then I emptied the box beneath the bench and bought new tools.</p>

<p data-source="186" class=""><strong class="date">Twenty-second year, summer.</strong> Wenna came to Anvil Row to set out the challenge.</p>

<p data-source="187" class="">Twin daggers. One each, forged side by side: the two matched halves of our complete masterpiece. I will supply the materials for both, including the sun-wyrm’s two fangs, a matched pair the adventurers kept back from the Dawnsplitter commission and have given me now. The same binder in both, from the same flask, enough for the whole paired work. The remaining components, we each choose for our own design.</p>

<p data-source="188" class="">“Same bones,” she said. “Different hands. Let’s see whose blade the fang prefers.”</p>

<p data-source="189" class=""><strong class="date">Morning.</strong> Tomorrow I forge against Wenna Thrale.</p>

<p data-source="190" class="">Callum came by and looked over everything spread across the bench. My fang, wrapped in cloth. The binder, sealed. Dark iron from Vey’s old stock. A strip of the silk Wenna first taught me to work. And Holloway’s river ring, which I mean to set into the pommel.</p>

<p data-source="191" class="">The ring won’t make the dagger stronger. It’s there because I want it to be part of the finished piece. A small memory, carried inside something greater.</p>

<p data-source="192" class="">Callum checked my materials twice. He found nothing missing. I took that as a compliment.</p>
}}

{{footnote ARCANE FORGE | THE DIARY OF TOMAS BRACK}}
{{pageNumber,auto}}
\page {tdiary,master}

{{tdtext
<p data-source="193" class=""><strong class="date">Evening.</strong> Holloway visited. He is very old now. His hands shake too badly for the smallest settings, but he can still spot a bad joint from across the room.</p>

<p data-source="194" class="">He studied my design for a long time, then pointed to where the hilt meets the blade. “Too much strain there.” He was right. We moved the support.</p>

<p data-source="195" class="">He asked whether I was nervous. I said yes.</p>

<p data-source="196" class="">“Good. Means you’re paying attention.”</p>

<p data-source="197" class="">He stayed until the light faded. We talked about the first ring. He still remembers it. So do I.</p>

<p data-source="198" class=""><strong class="date">Late evening.</strong> Wenna came to look at the forge she’ll be using. She examined my fang, then the silk, then the old ring.</p>

<p data-source="199" class="">“Still carrying that thing around?”</p>

<p data-source="200" class="">I nodded. She smiled. “You always did hold on to the little things.”</p>

<p data-source="201" class="">She has made no promise to go easy on me. I wouldn’t want her to.</p>

<p data-source="202" class="">After she’d gone, I realised how much of my life I’ve spent in her workshop, or thinking about what she taught me there. A weaponsmith is still a craftsman. I might never have learned that without her.</p>

<p data-source="203" class=""><strong class="date">Midnight.</strong> Couldn’t sleep, so I’ve been reading back through this journal. Holloway told me to record every failure, and I did.</p>

<p data-source="204" class="">The first ring. The clasp that wouldn’t close. The silk I ruined. The Journeyman sword that never woke. The hellhound blade, and the scar on my hand. And three Master projects I’ve never described, because I was ashamed: a spear that was too heavy, a bow that bent the wrong way, and a shield that hummed so loudly its owner begged me to undo it.</p>

<p data-source="205" class="">I’m writing them down now.</p>

<p data-source="206" class="">There are other things I nearly didn’t record because they seemed too ordinary. Callum staying late to help me temper a blade. Wenna teaching me to listen to silk. Vey teaching me to work slowly enough to see what I was doing. Holloway keeping a broken ring instead of throwing it away. My first apprentice finishing her first clasp. The adventurers lifting Dawnsplitter into the morning light.</p>

<p data-source="207" class="">They belong here too. Success has taught me things. So has failure. But almost everything worth knowing, I learned with someone standing beside me.</p>
}}

{{footnote ARCANE FORGE | THE DIARY OF TOMAS BRACK}}
{{pageNumber,auto}}
\page {tdiary,master}

{{tdtext
<p data-source="208" class=""><strong class="date">Before dawn.</strong> The materials are ready. The tools are clean. The floor has been swept. Vey would approve.</p>

<p data-source="209" class="">Callum will be there tomorrow. So will Holloway. And Wenna will stand at the forge beside mine, the other fang in her hand. For the first time we’ll work as rivals rather than teacher and student. I wonder whether I’ll recognise the moment that changes. Perhaps it already has.</p>

<p data-source="210" class="">My right hand aches. Cold morning coming. I used to resent the scar. Now it reminds me to pay attention.</p>

<p data-source="211" class="">There’s no certainty. A good piece can still fail at the very end, and a lifetime of experience can’t change that. But I know how to prepare. I know how to listen. And if something goes wrong, I know I can begin again.</p>

<p data-source="212" class="">That’s enough.</p>

<p data-source="213" class="">One last thing. Holloway used to say successes teach us nothing and failures must be remembered. I don’t think he entirely believed it. What he wanted was for me never to stop learning.</p>

<p data-source="214" class="">If this journal finds its way into another young craftsman’s hands:</p>

<p data-source="215" class="">Make the ring. Break the ring. Learn why. Make another. And when somebody offers to show you a better way, listen.</p>

<p data-source="216" class="">The first light is touching the workshop windows. Time to begin.</p>

<p data-source="217" class="signature"><em>— Tomas Dawnsplitter. Formerly Tomas Brack, Initiate of Holloway’s workshop.</em></p>
}}

{{footnote ARCANE FORGE | THE DIARY OF TOMAS BRACK}}
{{pageNumber,auto}}
\page {tdiary,master,tdlast}

{{tdtext
<p class="editor">Inside the back cover, in the same steady hand:</p>

<p data-source="219" class="">If the next page is blank, it doesn’t mean the story ended here. It means I went back to the forge.</p>
}}

{{footnote ARCANE FORGE | THE DIARY OF TOMAS BRACK}}
{{pageNumber,auto}}
\page {twinfangs}

{{wide,chapterhead
##### GM ONLY - POSSIBLE LEGENDARY MASTERWORK
# Light's Embrace & Shadow's Bane
Twin-dagger designs for Tomas Dawnsplitter and Grandmaster Wenna Thrale's trial, presented here as one possible completed version. Their completion, the trial's result and present whereabouts remain for the GM to decide.
}}

{{tdweaponrow
{{tdblade
#### Light's Embrace
*Weapon (dagger), legendary (requires attunement)*

Tomas Dawnsplitter's blade. A slender dagger with a white and silver grip, the sun-wyrm fang left bare along the edge so its warm glow shows through. Holloway's old river ring sits in the pommel, set with small clear stones that catch the light. It feels warm in the hand, and frightened people find it oddly comforting to hold.

You gain a +1 bonus to attack and damage rolls made with this magic weapon. It deals **1d8 piercing** damage instead of the normal dagger damage, plus an extra **1d6 radiant** damage on a hit.

**Warm Light.** As a bonus action, you can make the blade shed bright light in a 10-foot radius and dim light for a further 10 feet, or end the light.

}}
{{tdblade
#### Shadow's Bane
*Weapon (dagger), legendary (requires attunement)*

Grandmaster Wenna Thrale's blade. A darker, more menacing weapon, its grip wrapped in black leather, its edge jagged and serrated in a wicked curve. Venom from the great spider in Wenna's cellar was worked into the fang, and the blade seems to drink the light around it.

You gain a +1 bonus to attack and damage rolls made with this magic weapon. It deals **1d8 piercing** damage instead of the normal dagger damage, plus an extra **1d6 necrotic** damage on a hit.

**Sapping Edge.** A creature that takes necrotic damage from this dagger can't regain hit points until the start of your next turn.

}}
}}

{{note
##### The Twins Together
You can attune to either dagger on its own, or to both together. Either a single dagger or the attuned pair uses one attunement slot in total. The normal rules for ending attunement apply to each dagger. If your attunement to one ends, you remain attuned to the other using one slot. While you are attuned to both and holding one in each hand, you gain the following benefits.

**Twin Strike.** When you score a critical hit with either dagger, you can immediately make one additional attack with the other dagger against a target within its reach or range. This attack requires no action, bonus action or reaction, automatically hits, and is a critical hit. The attack granted by Twin Strike cannot itself trigger Twin Strike.

**Eclipse.** When you score a critical hit on the same creature with both daggers in the same turn, the target must succeed on a DC 15 Constitution saving throw or be stunned until the end of the target's next turn. Once this saving throw is triggered, you can't trigger Eclipse again until you finish a short or long rest, whether the target succeeds or fails. Twin Strike's granted critical hit can satisfy the paired-critical trigger.
}}

> *"Every light needs something to push against, Tomas."*
> — Grandmaster Wenna Thrale

{{gm
##### GM Note: Finding the Twins
The diary ends before the trial, so who won is yours to decide. The daggers may still hang in the Guildhall, be carried by Tomas and Wenna, or have been given away to a pair of adventurers they both trusted. Folk tales have already begun to say the daggers were made for two siblings, one a beacon of hope and the other a harbinger of doom. Tomas finds this very funny. Wenna does not correct anyone.
}}


{{footnote ARCANE FORGE | LEGENDARY MASTERWORK}}
{{pageNumber,auto}}
\page
{{backCover}}

##### Final Thread: A Maker's Mark

The beast falls. Others see a trophy. The forger sees a fang that could become a blade, a scale that could save a life, or a fragment of impossible magic waiting for the right hands.

Every mark on the metal has a story. Every secret learned from a master has a cost. And every creation placed on the anvil asks the same question: **what are you willing to risk to make something the world has never seen?**

##### **Now go craft some legends.**

___

##### The Arcane Forge

**Slay it. Salvage it. Shape your story.**

Inside you'll find:
- Monster harvesting and material discoveries
- Blueprints, binders and four-stage forging
- Crafting ranks, Guild trials and the Grandmaster forge-off
- GM guides for weapons, armour and accessories
- The freedom to invent creations with a story of their own

**Forge Your Story. Craft Your Legacy.**




<style>
/* TYPOGRAPHY ONLY — 21 October 2026; original colours and artwork retained. */
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;0,700;1,500;1,600&family=Crimson+Pro:ital,wght@0,400;0,600;0,700;1,400&family=Inter:wght@400;500;600;700&display=swap');
.page {font-family:'Crimson Pro',serif;}
.page p,.page li,.page td,.page dd,.page dt {font-family:'Crimson Pro',serif!important;}
.page h1,.page h2,.page h3,#p1 h1,#p1 h2,#p2 h1,#p2 h2,.page:has(.frontCover) h1,.page:has(.frontCover) h2 {font-family:'Cormorant Garamond',serif!important;}
.page h4,.page h5,.page th,.page .footnote,.page .pageNumber,.page .banner,.page .forge h5,.page .partcap h5,#p62 .columnWrapper h5 {font-family:'Inter',sans-serif!important;}
</style>

<style>
@import url('https://fonts.googleapis.com/css2?family=Caveat:wght@400;500;600;700&family=IM+Fell+English:ital@0;1&family=Marck+Script&display=swap');
.page.tdiary{background-color:#e9ddbd!important;background-image:radial-gradient(ellipse at 0% 65%,#34211255,transparent 13%),radial-gradient(ellipse at 100% 18%,#6d452c40,transparent 17%),repeating-linear-gradient(0deg,transparent 0px,transparent 23px,#75644219 23px,#75644219 24px),linear-gradient(100deg,#c4af83,#f0e4c8 7%,#eadfc4 91%,#b59b70)!important;box-shadow:inset 0 0 38px #50331a80; padding:58px 70px 72px!important;color:#352b24!important;}
.page.tdiary .columnWrapper{column-count:1!important;display:block!important;}
.page.tdiary:before{content:'';position:absolute;left:27px;top:80px;width:13px;height:84%;border-left:2px solid #5d422941;border-right:1px solid #5d42291c;pointer-events:none;}
.page.tdiary:after{background:none!important;border:0!important;}
.page.tdiary .tdtext{position:relative;z-index:1;}
.page.tdiary .tdtext p{font-family:'Caveat',cursive!important;font-size:19px!important;line-height:1.2!important;margin:0 0 7px!important;text-indent:0!important;text-align:left!important;}
.page.tdiary.boy .tdtext p{font-size:18.5px!important;letter-spacing:-.12px;}
.page.tdiary .tdtext h1,.page.tdiary .tdtext h2{font-family:'Caveat',cursive!important;color:#413226!important;letter-spacing:0;text-transform:none;border:0;}
.page.tdiary .tdtext h2{font-size:34px;line-height:1.1;margin:0 0 22px;border-bottom:1px solid #6b523849;padding-bottom:12px;}
.page.tdiary .date{display:block;font-weight:700;margin:13px 0 4px;font-size:1.06em;}
.page.tdiary.master .tdtext p{font-family:'IM Fell English',serif!important;font-size:17px!important;line-height:1.32!important;margin-bottom:8px!important;}
.page.tdiary.master .tdtext h2{font-family:'IM Fell English',serif!important;font-size:31px;}
.page.tdiary .tdtext .editor{font-family:'Crimson Pro',serif!important;font-size:14px!important;line-height:1.45!important;letter-spacing:0;color:#5b5145;}
.page.tdiary .footnote{font-family:'Inter',sans-serif!important;font-size:8px!important;letter-spacing:1px;color:#655745;bottom:30px;z-index:3;}
.page.tdiary .pageNumber{color:#655745;z-index:3;}
.page.tdiary.tdtitle .tdtext{padding:165px 35px 0;}
.page.tdiary.tdtitle h1{font-size:62px;line-height:1.05;margin-bottom:24px;transform:rotate(-2deg);}
.page.tdiary.tdtitle .subtitle{font-size:29px!important;margin-bottom:100px!important;}
.page.tdiary.tdtitle .editor{padding-top:25px;border-top:1px solid #6b523850;}
.page.tdiary.tdtitle .tdtext:after{content:'';position:absolute;width:80px;height:67px;border:2px solid #5c4b3277;border-radius:48% 53% 42% 50%;right:75px;top:440px;transform:rotate(18deg);box-shadow:3px 2px 0 -1px #5c4b3233,inset -3px -2px 0 -1px #5c4b3233;}
.page.tdiary.boy:after{content:'';display:block;position:absolute;left:34px;top:520px;width:24px;height:46px;border-radius:60%;background:repeating-radial-gradient(ellipse,#30251b17 0 1px,transparent 2px 4px);transform:rotate(-19deg);}
.page.tdiary.apprentice:after{content:'';display:block;position:absolute;right:15px;top:300px;width:90px;height:90px;border:7px double #784a1d16;border-radius:50%;box-shadow:2px 3px 8px #70451b14;}
.page.tdiary.scar{box-shadow:inset 0 -24px 50px #2b140ca6,inset 0 0 25px #5e38187a;}
.page.tdiary.injured:after{content:'';display:block;position:absolute;bottom:83px;right:14px;width:35px;height:180px;background:radial-gradient(ellipse,#7b38194a,transparent 70%);}
.page.tdiary .shaky:nth-child(3n){transform:rotate(-.8deg) translateX(2px);}
.page.tdiary .shaky:nth-child(3n+1){transform:rotate(.7deg);letter-spacing:.25px;}
.page.tdiary .shaky:nth-child(3n+2){transform:rotate(-.3deg) translateX(-1px);}
.page.tdiary.sunrise{background-image:radial-gradient(ellipse at 65% 0%,#ffdd7377,transparent 63%),repeating-linear-gradient(0deg,transparent 0px,transparent 23px,#75644213 23px,#75644213 24px),linear-gradient(100deg,#c4af83,#f0e4c8 7%,#eadfc4 91%,#b59b70)!important;}
.page.tdiary .guildslip,.page.tdiary .scrap,.page.tdiary .motherletter{display:block;width:max-content;max-width:95%;padding:11px 25px;margin:14px auto;background:#f3ead4;box-shadow:2px 4px 5px #34271c26;transform:rotate(-1.4deg);font-family:'Marck Script',cursive!important;font-size:23px;font-style:normal;}
.page.tdiary .guildslip{border:2px double #7c5e4b;color:#563b35;}
.page.tdiary .correction{font-family:'Marck Script',cursive!important;background:#f3ead4;padding:2px 7px;}
.page.tdiary .learned{border-bottom:1px solid #7c5e4b;}
.page.tdiary .scrap{clip-path:polygon(1% 3%,98% 0,100% 95%,3% 100%);transform:rotate(2deg);}
.page.tdiary .motherletter{position:relative;font-family:'Marck Script',cursive!important;padding:18px 26px;background:linear-gradient(177deg,#faf2df 49%,#ded1b5 50%,#f5e9d0 52%);}
.page.tdiary .motherletter:before{content:'';position:absolute;top:3px;left:50%;width:5px;height:5px;border-radius:50%;background:#6c3028;box-shadow:1px 2px 2px #0006;}
.page.tdiary .tdtext p.wennaletter{font-family:'Marck Script',cursive!important;font-size:21px!important;line-height:1.3!important;background:#f7edda;padding:20px 25px;margin:16px 14px 20px!important;transform:rotate(-.7deg);box-shadow:2px 4px 5px #34271c26;border-top:1px solid #fff9;}
.page.tdiary .register{font-family:'IM Fell English',serif!important;display:block;width:max-content;max-width:100%;border-block:1px solid #73624e;padding:7px 12px;margin:12px auto;letter-spacing:.6px;color:#493f35;}
.page.tdiary .tdtext p.signature{font-family:'Caveat',cursive!important;font-size:25px!important;line-height:1.1!important;margin-top:22px!important;}
.page.tdiary.tdlast .tdtext{padding-top:285px;}
.page.tdiary.tdlast .tdtext p:last-child{font-size:24px!important;line-height:1.45!important;margin-top:35px!important;max-width:440px;}
.page.tdiary.master:before{border:0;width:12px;height:10px;left:35px;top:160px;background:#3d241b;box-shadow:0 0 5px 5px #7c4d2b80;border-radius:47% 35% 60% 40%;}
.page.twinfangs .chapterhead{margin-bottom:20px;}
.page.twinfangs h1{font-size:33px;line-height:1.05;}
.page.twinfangs h4{margin-top:17px;}
.page.twinfangs h4#shadows-bane{border-top:2px solid transparent;border-image:linear-gradient(90deg,#c59a4b,#302736) 1;padding-top:15px;}
</style>

<style>
.page.tdiary .tdtext p{margin-bottom:4px!important;}
.page.tdiary .date{margin-top:8px;}
.page.tdiary.master .tdtext p{font-family:'Caveat',cursive!important;font-size:19px!important;line-height:1.18!important;font-weight:600;margin-bottom:5px!important;}
.page.tdiary.master .tdtext h2{font-family:'Caveat',cursive!important;}
.page.tdiary.twocol .tdtext{column-count:2;column-gap:28px;column-fill:balance;}
.page.tdiary.twocol .tdtext h2{column-span:all;}
.page.tdiary.twocol .tdtext p{break-inside:avoid;}
.page.tdiary .tdtext .editor{font-family:'Crimson Pro',serif!important;font-size:14px!important;font-weight:400;}
.page.tdiary .tdtext p.wennaletter{font-family:'Marck Script',cursive!important;font-size:21px!important;font-weight:400;}
.page.tdiary .tdtext p.signature{font-size:25px!important;}
.page.tdiary.boy.twocol .tdtext p{font-size:17.5px!important;}
.page.tdiary.scar{box-shadow:inset 0 -25px 45px #2b140ca6,inset 0 0 25px #5e38187a!important;}
.page.tdiary .tdtext:before{pointer-events:none;}
.page.tdiary.apprentice:not(.twocol) .tdtext:after{content:'';position:absolute;bottom:-115px;right:20px;width:110px;height:12px;border:1px solid #51443977;clip-path:polygon(0 50%,70% 0,70% 35%,100% 35%,100% 65%,70% 65%,70% 100%);transform:rotate(-15deg);background:linear-gradient(0deg,transparent 45%,#51443955 48%,transparent 55%);}
</style>
<style>
.page.tdiary .tdtext p::first-letter{font:inherit!important;color:inherit!important;float:none!important;margin:0!important;padding:0!important;background:none!important;line-height:inherit!important;}
.page.tdiary .tdtext p{font-variant:normal!important;text-transform:none!important;}
#p55.tdiary .tdtext p{font-size:18px!important;line-height:1.17!important;}
.page.tdiary.scar:after{content:''!important;display:block!important;position:absolute!important;right:0!important;left:auto!important;top:auto!important;bottom:0!important;width:32px!important;height:330px!important;background:linear-gradient(90deg,#91602d44,#3a2019 70%,#17120e)!important;clip-path:polygon(80% 0,100% 0,100% 100%,0 100%,12% 88%,3% 79%,21% 67%,9% 52%,36% 39%,24% 28%,60% 15%);border:0!important;}
.page.tdiary.injured .tdtext:after{content:'';position:absolute;left:-51px;top:190px;width:30px;height:120px;background:radial-gradient(ellipse,#82422155,transparent 72%);transform:rotate(-15deg);}
.page.tdiary.apprentice:after{border:6px double #784a1d26!important;background:transparent!important;}
.page.tdiary.boy:after{background:repeating-radial-gradient(ellipse,#30251b26 0 1px,transparent 2px 4px)!important;}
.page.twinfangs .columnWrapper{column-count:1!important;}
.page.twinfangs .tdweaponrow{display:grid;grid-template-columns:1fr 1fr;gap:28px;margin:20px 0 25px;}
.page.twinfangs .tdblade{border-top:2px solid #b29054;padding-top:8px;}
.page.twinfangs .tdblade:nth-child(2){border-color:#423846;}
.page.twinfangs .tdblade h4{border:0!important;padding-top:0!important;margin-top:0;}
.page.twinfangs .note,.page.twinfangs .gm{margin-top:15px;}
</style>
<style>
.page.tdiary .footnote,.page.twinfangs .footnote{width:auto!important;left:80px!important;right:80px!important;white-space:nowrap;font-size:8px!important;}
</style>

<style>
/* Page 18: preserve the complete three-path artwork. */
#p19 .featureArt{height:270px!important;width:360px!important;max-width:100%;aspect-ratio:4/3!important;margin:14px auto 0!important;}
#p19 .featureArt img{object-fit:contain!important;object-position:center!important;}
</style>

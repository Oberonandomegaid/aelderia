<style>
/* =====================================================
   GENESIS EGGS — house style (Homebrewery V3, 5ePHB base)
   A4 pages. Palette: parchment, midnight indigo, amethyst, muted copper.
   ===================================================== */
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@500;700&family=IM+Fell+English:ital@0;1&family=IM+Fell+English+SC&family=Noto+Sans+Runic&display=swap');

/* ---- A4 page size (print with paper size A4, margins none, background graphics on) ---- */
.page { width: 210mm; height: 296.8mm; }

/* ---- Collection palette ---- */
.page {
  --HB_Color_HeaderText: #2f2552;
  --HB_Color_HeaderUnderline: #b8874f;
  --HB_Color_HorizontalRule: #7a5aa6;
  --HB_Color_Accent: #e9e0f0;
  --HB_Color_CaptionText: #6b4a2b;
}
.page h1 { font-family: 'Cinzel', serif; font-weight: 700; color: #2f2552; font-size: 0.82cm; line-height: 1.08em; letter-spacing: 0.01em; margin-bottom: 0.2cm; }
.page h2 { font-family: 'Cinzel', serif; font-weight: 500; color: #3f2f6b; font-size: 0.56cm; line-height: 1.1em; }
.page h3 { color: #3f2f6b; font-size: 0.47cm; }
.page h4, .page h5 { color: #7a4a24; }
.page * + h2 { margin-top: 0.38cm; }
.page h2 + * { margin-top: 0.12cm; }
.page * + h3 { margin-top: 0.3cm; }
.page h1 + p::first-letter { float: none; padding: 0; margin: 0; font-family: inherit; font-size: inherit; line-height: inherit; color: inherit; background-image: none; -webkit-background-clip: border-box; background-clip: border-box; }
.page h1 + p::first-line { font-variant: normal; }
.page table { width: 100%; }
.page table th, .page table td { padding: 3px 6px; vertical-align: top; }
.page table th { color: #2f2552; }
.page table + * { margin-top: 0.28cm; }
.page .note { border-left: 3px solid #9a6a3c; }

/* ---- Chapter opening band (spans both columns) ---- */
.page .chapterhead { border-bottom: 2px solid #b8874f; padding-bottom: 6px; margin-bottom: 12px; }
.page .chapterhead p { font-size: 0.36cm; line-height: 1.35em; }
.page .chapterhead h5 { font-family: 'Cinzel', serif; color: #8a5a2b; letter-spacing: 0.14em; font-size: 0.3cm; margin: 0 0 2px; }

/* ---- GM-only marker: small tab at the top edge instead of a watermark ---- */
.page .gmtab { position: absolute; top: 0; right: 1.4cm; left: auto; width: max-content; background: #2f2552; color: #f3e8d2; font-family: 'Cinzel', serif; font-size: 0.24cm; letter-spacing: 0.16em; padding: 0.42cm 0.22cm 0.16cm; border-radius: 0 0 5px 5px; z-index: 5; }
.page .gmtab p { margin: 0; }

/* ---- GM guidance panel (purple) — used sparingly ---- */
.page .gm { break-inside: avoid; background: #ece3f2; border: 1px solid #bba6cf; border-left: 5px solid #5b3d8a; padding: 7px 12px 7px; margin: 10px 0 12px; }
.page .gm h5 { font-family: 'Cinzel', serif; color: #3f2370; font-size: 0.32cm; letter-spacing: 0.04em; margin: 0 0 3px; }
.page .gm p { font-size: 0.33cm; line-height: 1.32em; margin: 0; text-indent: 0; }
.page .gm p + p { margin-top: 4px; }

/* ---- Rules page sizes ---- */
.page.rules { font-size: 0.37cm; }
.page.rules p, .page.rules ul, .page.rules ol { line-height: 1.36em; }
.page.rules li + li { margin-top: 0.06cm; }
.page.rules table { font-size: 0.34cm; line-height: 1.3em; }
.page.rules.dense { font-size: 0.35cm; }
.page.rules.dense p, .page.rules.dense ul { line-height: 1.3em; }

/* ---- Four-step ritual path ---- */
.page .ritual { display: grid; grid-template-columns: repeat(4, 1fr); gap: 9px; margin: 6px 0 10px; }
.page .ritual .step { background: rgba(255,255,255,0.35); border: 1px solid #c8b08a; border-top: 4px solid #5b3d8a; padding: 6px 8px 7px; break-inside: avoid; }
.page .ritual h4 { font-family: 'Cinzel', serif; color: #2f2552; font-size: 0.34cm; margin: 0 0 4px; line-height: 1.15em; }
.page .ritual h4 em { display: block; font-style: normal; color: #8a5a2b; font-size: 0.26cm; letter-spacing: 0.12em; }
.page .ritual ul { padding-left: 0.9em; margin: 0; }
.page .ritual li { font-size: 0.32cm; line-height: 1.3em; }
.page .ritual p { font-size: 0.32cm; line-height: 1.3em; margin: 0; }

/* ---- Aspect family strip ---- */
.page .families { display: grid; grid-template-columns: repeat(4, 1fr); gap: 8px; margin: 4px 0 8px; }
.page .families p { margin: 0; font-size: 0.32cm; line-height: 1.3em; border-left: 3px solid #b8874f; padding-left: 7px; }

/* ---- Write-in worksheets ---- */
.page.sheet { font-size: 0.36cm; }
.page.sheet table td { height: 0.95cm; }
.page.sheet .lines p { line-height: 2.05em; }
.page.sheet h3 { margin-top: 0.3cm; }
.page .writebox { border: 1px solid #b9a27a; background: rgba(255,255,255,0.32); min-height: 2.3cm; margin: 4px 0 10px; padding: 4px 8px; font-size: 0.3cm; color: #7a6a55; }
.page .writebox p { margin: 0; }
.page li:has(> input[type=checkbox]) { list-style: none; margin-left: -1.1em; }

/* ---- Blank stat sheet ---- */
.page.blankSheet h3 { font-size: 0.5cm; }
.page.blankSheet li { line-height: 1.8em; }
.page.blankSheet p { line-height: 1.6em; }
.page.blankSheet .statLine table { text-align: center; margin: 0.3cm 0; }
.page.blankSheet .statLine td { height: 1.05cm; }

/* ---- The Magister's notebooks: journal pages ---- */
.page.journal { font-family: 'IM Fell English', serif; font-size: 0.36cm; }
.page.journal p { line-height: 1.24em; }
.page.journal p + p { text-indent: 0; margin-top: 0.1cm; }
.page.journal li { line-height: 1.28em; }
.page.journal h1 { font-size: 0.74cm; }
.page.journal h2 { font-family: 'IM Fell English SC', serif; font-weight: 400; font-size: 0.5cm; color: #4b2e1a; margin-top: 0.34cm; }
.page.journal h3 { font-family: 'IM Fell English SC', serif; font-weight: 400; color: #4b2e1a; border-bottom: 1px solid #b8874f; font-size: 0.44cm; }
.page.journal h5 { font-family: 'IM Fell English', serif; font-style: italic; font-weight: 400; color: #8a5a2b; font-size: 0.32cm; margin-top: 0; }
.page.journal hr { border: none; height: 10px; margin: 6px auto; width: 40%; background: radial-gradient(circle, #b8874f 2px, transparent 3px) center/14px 10px repeat-x; }
.page.journal em { color: #3a2a1e; }
.page .runhead { position: absolute; top: 0.62cm; left: 0; right: 0; text-align: center; font-family: 'Cinzel', serif; font-size: 0.22cm; letter-spacing: 0.22em; color: #8a6a45; }
.page .runhead p { margin: 0; }
.page .subject { border-top: 1px solid #b8874f; border-bottom: 1px solid #b8874f; padding: 4px 0 3px; margin: 0 0 8px; }
.page .subject h3 { border: none; margin: 0; font-size: 0.42cm; }
.page .subject p { margin: 0; font-size: 0.3cm; color: #6b4a2b; }
.page .pull { break-inside: avoid; margin: 8px 6px 10px; padding: 6px 4px; border-top: 1px solid #b8874f; border-bottom: 1px solid #b8874f; text-align: center; font-family: 'IM Fell English', serif; font-style: italic; font-size: 0.47cm; line-height: 1.25em; color: #3f2f6b; }
.page .pull p { margin: 0; line-height: 1.25em; }

/* ---- Figures with captions (journal sketches, in-column art) ---- */
.page .fig { break-inside: avoid; margin: 6px 0 8px; text-align: center; }
.page .fig img { display: block; margin: 0 auto; max-width: 100%; mix-blend-mode: multiply; }
.page .fig h5 { font-family: 'IM Fell English SC', serif; color: #4b2e1a; font-size: 0.34cm; margin: 3px 0 0; }
.page .fig p { margin: 0; font-size: 0.27cm; color: #6b4a2b; font-style: italic; line-height: 1.25em; }
.page .art { break-inside: avoid; margin: 6px 0 4px; -webkit-mask-image: url(/assets/waterColorMasks/center/0001.webp); mask-image: url(/assets/waterColorMasks/center/0001.webp); -webkit-mask-size: 112% 125%; mask-size: 112% 125%; -webkit-mask-position: center; mask-position: center; -webkit-mask-repeat: no-repeat; mask-repeat: no-repeat; }
.page .art p { margin: 0; height: 100%; }
.page .art img { width: 100%; height: 100%; object-fit: cover; display: block; }
.page .art.artc { margin-left: auto; margin-right: auto; }

/* ---- Rune alphabet ---- */
.page .runeTable table { font-size: 0.32cm; }
.page .runeTable tbody td { font-family: 'Noto Sans Runic', serif; font-size: 0.42cm; color: #5a1f1a; }

/* ---- Example companions: case files ---- */
.page.casefile { font-size: 0.335cm; }
.page.casefile p, .page.casefile li { line-height: 1.27em; }
.page .caseinfo table { font-size: 0.33cm; margin-bottom: 6px; }
.page .caseinfo td:nth-child(odd) { font-family: 'Cinzel', serif; color: #2f2552; font-size: 0.27cm; letter-spacing: 0.06em; white-space: nowrap; }
.page .stage { background: rgba(255,255,255,0.33); border: 1px solid #cbb48d; border-left: 4px solid #8a5a2b; padding: 5px 9px 6px; margin: 0 0 9px; -webkit-box-decoration-break: clone; box-decoration-break: clone; }
.page .stage h4 { break-after: avoid; }
.page .block.stage { display: block; break-inside: auto !important; }
.page .stage h4 { font-family: 'Cinzel', serif; color: #2f2552; font-size: 0.33cm; margin: 0 0 3px; }
.page .stage ul { margin: 0; padding-left: 1.0em; }
.page .stage blockquote { margin: 3px 0; padding: 3px 7px; font-size: 0.31cm; }
.page .evo { break-inside: avoid; background: #2f2552; color: #f1e6cf; padding: 7px 12px; margin: 4px 0 8px; }
.page .evo h4 { color: #e3c99a; font-family: 'Cinzel', serif; margin: 0 0 3px; font-size: 0.33cm; }
.page .evo p, .page .evo li { color: #f1e6cf; font-size: 0.32cm; line-height: 1.3em; margin: 0; }
.page .evo strong { color: #ffffff; }
.page .evo ul { margin: 2px 0 0; padding-left: 1em; }
.page .evo.evocap { display: block; position: absolute; left: 55px; width: 684px; box-sizing: border-box; bottom: 80px; z-index: 5; background: rgba(24,18,44,0.86); border-left: 5px solid #b58bd6; padding: 12px 18px; }
.page .evo.evocap p, .page .evo.evocap li { font-size: 0.34cm; }

/* ---- Stat cards ---- */
.page .monster.frame.wide { font-size: 0.335cm; margin-bottom: 0.4cm; }
.page .monster.frame.wide p, .page .monster.frame.wide dl { line-height: 1.32em; }

/* ---- Aspect tables ---- */
.page.aspectPage table { font-size: 0.32cm; line-height: 1.22em; }
.page.aspectPage table td, .page.aspectPage table th { padding: 2px 5px; }
.page.aspectPage table td:first-child, .page.aspectPage table th:first-child { width: 0.5cm; text-align: center; }
.page .aspect { display: block; break-inside: avoid; margin-bottom: 0.3cm; }
.page .aspect h4 { font-family: 'Cinzel', serif; color: #2f2552; font-size: 0.38cm; margin: 0 0 2px; }
.page .aspect h4 em { font-style: normal; color: #8a5a2b; font-size: 0.26cm; letter-spacing: 0.1em; }
.page .keyband { background: #2f2552; color: #f1e6cf; padding: 6px 12px; margin: 0 0 10px; }
.page .keyband p { color: #f1e6cf; margin: 0; font-size: 0.31cm; line-height: 1.32em; }
.page .keyband strong { color: #e3c99a; }

/* ---- Full-page art and part openers ---- */
.page .partcap { position: absolute; left: 55px; bottom: 90px; width: 380px; padding: 14px 20px 13px; background: rgba(24,18,44,0.82); border-left: 5px solid #b58bd6; color: #f1e4c8; z-index: 5; }
.page .partcap h5 { color: #d9c3ef; margin: 0; font-family: 'Cinzel', serif; font-size: 0.32cm; letter-spacing: 0.16em; }
.page .partcap h2 { color: #f6ead2; margin: 2px 0 6px; font-size: 0.95cm; border: none; }
.page .partcap p { color: #e8dcc0; font-size: 0.34cm; line-height: 1.35em; margin: 0; }
.page .partcap p + p { margin-top: 5px; }
.page .partcap.top { bottom: auto; top: 70px; }
.page .spellcard { position: absolute; right: 50px; bottom: 90px; width: 300px; padding: 11px 15px 10px; background: rgba(246,238,222,0.93); border-top: 4px solid #5b3d8a; z-index: 5; }
.page .spellcard h5 { font-family: 'Cinzel', serif; color: #3f2370; margin: 0 0 4px; font-size: 0.3cm; letter-spacing: 0.08em; }
.page .spellcard p { font-size: 0.29cm; line-height: 1.3em; margin: 0 0 4px; color: #2b2233; }

/* ---- Covers and front matter ---- */
.page .imprint { position: absolute; top: 0.9cm; left: 0; right: 0; text-align: center; font-family: 'Cinzel', serif; letter-spacing: 0.3em; font-size: 0.3cm; color: #f3e6c8; text-shadow: 0 0 6px #000, 0 0 3px #000; z-index: 3; }
.page .imprint p { margin: 0; }
.page .frontCover .banner, .page .banner { background: #2f2552; color: #f3e6c8; font-family: 'Cinzel', serif; letter-spacing: 0.12em; }
.page .legal { border-top: 2px solid #b8874f; padding-top: 6px; margin-top: 10px; font-size: 0.26cm; line-height: 1.35em; color: #3a2a20; }
.page .legal h5 { font-family: 'Cinzel', serif; color: #2f2552; font-size: 0.3cm; letter-spacing: 0.1em; margin: 0 0 4px; }
.page .legal p { margin: 0 0 4px; }
.page .closing { font-size: 0.4cm; }
.page .closing p { line-height: 1.45em; }
.page .backpanel { position: absolute; left: 60px; width: 674px; box-sizing: border-box; top: 60px; padding: 18px 24px 16px; background: rgba(18,14,32,0.84); border-top: 4px solid #b8874f; z-index: 5; }
.page .backpanel h1 { color: #f3e6c8; font-size: 0.9cm; margin: 0 0 8px; }
.page .backpanel p, .page .backpanel li { color: #efe4cc; font-size: 0.35cm; line-height: 1.4em; }
.page .backpanel h5 { color: #e3c99a; font-family: 'Cinzel', serif; letter-spacing: 0.08em; font-size: 0.32cm; margin: 8px 0 3px; }
.page .backpanel strong { color: #ffffff; }
.page .backfoot { position: absolute; left: 60px; width: 674px; bottom: 40px; text-align: center; font-family: 'Cinzel', serif; font-size: 0.26cm; letter-spacing: 0.2em; color: #f3e6c8; text-shadow: 0 0 5px #000, 0 0 2px #000; z-index: 5; }
.page .backfoot p { margin: 0; }
.page .toc li h4 { font-size: 0.36cm; }
.page .footnote { bottom: 0.62cm; color: #6b4a2b; }

/* Production layout pass — 16 October 2026. Original rules and prose retained. */
.page .footnote {left:1.45cm;right:1.45cm;width:auto;text-align:left;font-size:9px;letter-spacing:.045em;white-space:nowrap;}
.page .pageNumber {z-index:8;}
.page .studyCrop {position:relative;overflow:hidden;margin:0 auto;max-width:100%;mix-blend-mode:multiply;mask-image:linear-gradient(transparent,#000 5%,#000 94%,transparent);}
.page .studyCrop img {position:absolute;max-width:none;margin:0;}
.page .stageGallery {display:flex;justify-content:center;gap:20px;margin:8px 0;break-inside:avoid;}
.page .stageGallery img {min-width:0;max-width:100%;height:100%;object-fit:contain;flex:0 1 auto;}
.page .block.stage {break-inside:avoid!important;}
.page .trackerGrid {display:grid;grid-template-columns:1fr 1fr;gap:10px 16px;align-items:start;}
.page .trackerGrid .stage {margin:0;}
.page .monster.frame.wide {background:rgba(250,245,232,.94);border-image:none;border:1px solid #b99d77;border-top:3px solid #59406d;box-shadow:0 2px 5px #49332620;padding:8px 12px;}
.page .art img {object-fit:contain;}
.page:has(.frontCover) .banner {bottom:160px!important;left:70px!important;width:654px!important;box-sizing:border-box;background:#2f2552!important;color:#f3e6c8!important;font:17px 'Cinzel',serif!important;padding:14px 10px!important;text-align:center;}
.page:has(.frontCover) .banner::before,.page:has(.frontCover) .banner::after {display:none!important;}
.page:has(.frontCover) .footnote {bottom:45px!important;left:70px!important;right:70px!important;width:auto!important;white-space:normal!important;font:12px/1.3 'IM Fell English',serif!important;text-align:center;padding:10px;background:rgba(17,16,31,.84);color:#f4e7ce!important;z-index:5;}
.page:has(.frontCover) h1,.page:has(.frontCover) h2 {color:#f7ead2!important;text-shadow:0 2px 8px #090812!important;font-family:'Cinzel',serif!important;-webkit-text-stroke:0!important;}
.page:has(.frontCover) h1 {font-size:52px!important;}
.page:has(.frontCover) h2 {font-size:25px!important;}
.page.production20 .partcap {left:70px;right:70px;width:auto;bottom:115px;background:#2f2552;}
.page.production20 .partcap h2 {font-size:.8cm;}
.page.production34 .partcap {width:330px;box-sizing:border-box;}
.page.production34 .spellcard {width:310px;box-sizing:border-box;}
.page.production41 {background-color:#21182e;}
.page.production41 .evo.evocap {bottom:95px;}
.page.production46 .art,.page.production47 .art,.page.production57 .art {column-span:all;width:100%;margin-left:auto;margin-right:auto;}
.page.production59 {background-color:#20172c;}
.page.production59 .backpanel {top:45px;padding:15px 22px;}

/* Final production pass. fp numbers refer to the reviewed 79-page baseline. */
.page.rn .ring,.page.diary .ring {display:none!important;}
.page.fp11 .art,.page.fp12 .art {mix-blend-mode:multiply;mask-image:linear-gradient(transparent,#000 4%,#000 96%,transparent);}
.page.fp18 .writebox {background:rgba(255,255,255,.22);}
.page.fp20 {background-color:#e8dcc3;}
.page.fp20:before {content:'';position:absolute;inset:38px;border:1px solid #947347;pointer-events:none;}
.page.fp20 .notebookTitle {position:absolute;top:90px;left:70px;width:654px;text-align:center;}
.page.fp20 .notebookTitle h5 {font:12px 'Cinzel',serif;letter-spacing:.3em;color:#82613b;margin:0 0 18px;}
.page.fp20 .notebookTitle h1 {font:40px/1.13 'Cinzel',serif;color:#332747;}
.page.fp20 .partcap {bottom:100px;left:100px;right:100px;padding:24px 28px;background:transparent;border:0;border-top:1px solid #947347;border-bottom:1px solid #947347;text-align:center;}
.page.fp20 .partcap p {font:18px/1.45 'IM Fell English',serif;color:#463621;}
.page.fp21 {column-count:1;padding:65px 94px;}
.page.fp21:before {content:'';position:absolute;inset:38px;border:1px solid #b69b70;pointer-events:none;}
.page.fp21 .treatiseTitle {text-align:center;border-bottom:2px solid #8e7048;padding:0 10px 24px;margin-bottom:25px;}
.page.fp21 .treatiseTitle h1 {font:30px/1.16 'IM Fell English SC',serif;color:#3b2c26;}
.page.fp21 .treatiseTitle h5 {font:11px/1.6 'Cinzel',serif;letter-spacing:.1em;margin-top:14px;}
.page.fp21 .columnWrapper {display:block;columns:unset!important;}
.page.fp21 .wide {column-span:none;}
.page.fp21 .treatiseLetter {font:17px/1.38 'IM Fell English',serif;}
.page.fp21 .treatiseLetter h2 {font:29px 'IM Fell English SC',serif;margin:18px 0;}
.page.fp21 .treatiseLetter p {line-height:1.38;margin:0 0 10px;text-indent:0;}
.page.fp21 .treatisePath>p {display:contents;}
.page.fp21 .treatisePath span {display:block;}
.page.fp21 .treatisePath {display:grid;grid-template-columns:repeat(4,1fr);border-top:1px solid #aa895a;border-bottom:1px solid #aa895a;padding:16px 0;margin:30px 0 18px;text-align:center;font:13px/1.7 'Cinzel',serif;color:#725331;}
.page.fp21 .treatisePath span+span {border-left:1px solid #c1ac8d;}
.page.fp21 .scholarMark {text-align:center;font:22px 'Cinzel',serif;color:#7e6243;letter-spacing:.18em;}
.page.fp21 .scholarMark small {font-size:10px;letter-spacing:.1em;}
.page.rn .e2-f3,.page.rn .e3-f4,.page.diary .dfig1,.page.diary .dfig10,.page.diary .dfig14,.page.diary .dfig15,.page.diary .dfig21,.page.diary .dfig33,.page.diary .dfig34,.page.diary .epf10 {background-size:contain!important;background-position:center!important;background-repeat:no-repeat!important;mask-image:linear-gradient(transparent,#000 3%,#000 97%,transparent)!important;mix-blend-mode:multiply;}
.page.rn .e2-f3 {left:28px!important;top:548px!important;width:182px!important;height:122px!important;}
.page.rn .e3-f4 {left:625px!important;top:440px!important;width:137px!important;height:176px!important;}
.page.diary .dfig1 {width:155px!important;height:110px!important;}
.page.diary .dfig10 {width:220px!important;height:160px!important;}
.page.diary .dfig15 {width:230px!important;height:150px!important;}
.page.diary .dfig21 {width:210px!important;height:140px!important;}
.page.diary .dfig33 {width:205px!important;height:138px!important;transform:none!important;}
.page.diary .dfig34 {width:155px!important;height:110px!important;}
.page.diary .epf10 {left:125px!important;width:544px!important;height:170px!important;top:790px!important;transform:none!important;}
.page.fp57 .art {height:480px!important;mask-image:linear-gradient(transparent,#000 4%,#000 96%,transparent);mask-size:100% 100%;}
.page.fp57 .art img {object-fit:contain;mix-blend-mode:multiply;}
.page.fp58 .evo {column-span:all;margin-top:12px;}
.page.fp59 .stageGallery,.page.fp60 .stageGallery {height:330px!important;gap:4px;margin-top:2px;}
.page.fp59 .stageGallery img,.page.fp60 .stageGallery img,.page.fp63 .stageGallery img,.page.fp64 .stageGallery img,.page.fp66 .stageGallery img,.page.fp68 .stageGallery img {mask-image:linear-gradient(transparent,#000 7%,#000 92%,transparent),linear-gradient(90deg,transparent,#000 7%,#000 93%,transparent);mask-composite:intersect;mix-blend-mode:multiply;}
.page.fp61 {background-color:#efe3c9;}
.page.fp61 img {mask-image:linear-gradient(transparent,#000 4%,#000 95%,transparent),linear-gradient(90deg,transparent,#000 4%,#000 96%,transparent);mask-composite:intersect;}
.page.fp61 .evo.evocap {bottom:90px;background:#2f2552;}
.page.fp63 .stageGallery {height:320px!important;margin-top:0;}
.page.fp64 .stageGallery {height:300px!important;margin-top:0;}
.page.fp66 .stageGallery {height:360px!important;margin-top:0;}
.page.fp68 .stageGallery {height:220px!important;margin-top:-3px;}
.page.fp69 .ascensionTitle {position:absolute;top:55px;left:70px;width:654px;text-align:center;}
.page.fp69 .ascensionTitle h5 {letter-spacing:.2em;font:12px 'Cinzel',serif;margin-bottom:10px;}
.page.fp69 .ascensionTitle h1 {font-size:30px;}
.page.fp69 img {mask-image:linear-gradient(transparent,#000 8%,#000 90%,transparent),linear-gradient(90deg,transparent,#000 5%,#000 95%,transparent);mask-composite:intersect;mix-blend-mode:multiply;}
.page.fp69 .evo.evocap {bottom:90px;background:#2f2552;}
.page.fp73 .fig img,.page.fp74 .fig img,.page.fp75 .fig img {mask-image:linear-gradient(transparent,#000 4%,#000 97%,transparent);}
.page.fp77 .closing {position:absolute;left:50px;right:auto;width:694px;box-sizing:border-box;bottom:64px;padding:20px 24px;background:rgba(247,238,215,.97);border-top:3px solid #6b4c35;column-count:2;column-gap:24px;font:13px 'IM Fell English',serif;box-shadow:0 -10px 35px #32231822;}
.page.fp77 .closing h1 {column-span:all;font-size:26px;margin:0 0 13px;}
.page.fp77 .closing p {line-height:1.36;margin:0 0 6px;text-indent:0;}
.page.fp77 .footnote {color:#eee4cd;text-shadow:0 1px 4px #000;}
.page.fp79 {background-color:#e7d9bb;column-count:1;}
.page.fp79:before {content:'';position:absolute;inset:35px;border:1px solid #937047;pointer-events:none;}
.page.fp79 .backpanel {top:65px;left:70px;width:654px;padding:0 10px 22px;background:transparent;border:0;border-bottom:1px solid #947347;}
.page.fp79 .backpanel h1 {font-size:32px;line-height:1.16;color:#332747;margin-bottom:20px;text-align:center;}
.page.fp79 .backpanel p,.page.fp79 .backpanel li {font:14px/1.4 'IM Fell English',serif;color:#342a24;}
.page.fp79 .backpanel h5 {color:#77532f;font-size:12px;margin-top:12px;}
.page.fp79 .backpanel strong {color:#332747;}
.page.fp79 .backfoot {color:#604626;text-shadow:none;bottom:57px;font-size:10px;letter-spacing:.15em;}
.page.fp79 img,.page.fp20 img {mask-image:linear-gradient(transparent,#000 4%,#000 96%,transparent),linear-gradient(90deg,transparent,#000 4%,#000 96%,transparent);mask-composite:intersect;}
.page.diary .dfig0 {background-size:contain!important;background-position:center!important;background-repeat:no-repeat!important;width:155px!important;height:115px!important;}
.page.fp12 .art,.page.fp57 .art {mask-image:linear-gradient(transparent,#000 7%,#000 93%,transparent),linear-gradient(90deg,transparent,#000 7%,#000 93%,transparent);mask-composite:intersect;mask-size:100% 100%;}
.page.rn .e2-f3,.page.rn .e3-f4,.page.diary .dfig0,.page.diary .dfig10,.page.diary .dfig14,.page.diary .dfig15,.page.diary .dfig21,.page.diary .dfig33,.page.diary .dfig34,.page.diary .epf10 {mask-image:linear-gradient(transparent,#000 7%,#000 93%,transparent),linear-gradient(90deg,transparent,#000 7%,#000 93%,transparent)!important;mask-composite:intersect!important;}


/* Rules revision: scoped reflow for expanded mechanics only. */
.page.fp2 .toc li h4 {font-size:0.33cm;line-height:1.1;}
.page.fp2 .toc li {margin-top:0;}
.page.fp19 p {line-height:1.35em;}
.page.fp19 li {line-height:1.45em;}
.page.fp19 h3 {margin-top:0.2cm;}
.page.fp55 .trackerGrid,.page.fp58 .trackerGrid,.page.fp62 .trackerGrid,.page.fp65 .trackerGrid {gap:6px;}
.page.fp55 .trackerGrid li,.page.fp58 .trackerGrid li,.page.fp62 .trackerGrid li,.page.fp65 .trackerGrid li {line-height:1.17em;}
.page.fp64 .stageGallery {height:130px!important;}
.page.fp68 .stageGallery {height:130px!important;}


/* Audit fit: expanded training rules, page 8 only. */
.page#p8 h2 {margin-top:4px;margin-bottom:2px;}
.page#p8 p {margin-top:0;margin-bottom:2px;}
.page#p8 {padding-top:30px;}
.page#p8 table {margin-top:2px;margin-bottom:2px;}
.page#p8 table td,.page#p8 table th {padding-top:2px;padding-bottom:2px;}

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
.page#p84 .backpanel h5 { color: #6b4a2b !important; }
.page#p4 .ritual { grid-template-columns: repeat(2, 1fr); gap: 10px; }
.page#p4 .ritual .step { padding: 8px 10px; }
.page .tdtitle .tdtext:after { top: 540px !important; right: 40px !important; }
.page .scar:after { right: 15px !important; width: 18px !important; opacity: .35; }
.page#p60 .tagpanel h3 { font: normal 18px/1.25 'Crimson Pro', serif !important; }
.page#p19 p { text-indent: 0 !important; }
.page#p19 .optional-hopes { margin: 14px 0 !important; }
.page#p64 .evo h4 { color: #dbc596 !important; font-weight: 700 !important; }
.page#p2 .legal { line-height: 1.18 !important; font-size: 9px !important; }
.page#p60 .tagpanel { left: 37% !important; width: 56% !important; bottom: 60px !important; padding: 14px 18px !important; }
.page#p60 .tagpanel h3 { font-size: 16px !important; }
.page#p30 .pimg { clip-path: inset(0 0 2px 0); }
.page .zamp-inline { font: inherit !important; display: inline !important; }

</style>

{{frontCover}}

{{imprint
}}

# Genesis Eggs
## The Endless Possibilities
___

{{banner A COMPANION CREATURE SUPPLEMENT}}

{{footnote
*“Creation is not a science, nor solely a magic. It is a dialogue—between soul and spark, between dreamer and dream. These creatures are not tools, nor pets, nor summoned things. They are the echo of intent, shaped by bond and belief. Treat them as such, and they may become more than you imagined.”*
}}

![](https://raw.githubusercontent.com/Omegaoliverid/Public-images/main/Genesis-Eggs/approved/cover-elemental-egg.png){position:absolute,top:0px,left:0px,width:100%,height:100%,object-fit:cover,object-position:center}

\page {production2,fp2}
{{toc,wide
# Contents

- ### [{{ Part One — Raising a Genesis Egg}}{{ 3}}](#p3)
  - #### [{{ GM Notes on How to Infuse}}{{ 4}}](#p4)
  - #### [{{ The GM Determines the Creature}}{{ 5}}](#p5)
  - #### [{{ Growth & Progression}}{{ 7}}](#p7)
  - #### [{{ Training, Commands and Individuality}}{{ 8}}](#p8)
  - #### [{{ Genesis Egg Tracker}}{{ 9}}](#p9)
  - #### [{{ Creating a Balanced Companion}}{{ 11}}](#p11)
  - #### [{{ Unlocking Abilities and Evolution}}{{ 12}}](#p12)
  - #### [{{ Flight and Gliding}}{{ 13}}](#p13)
  - #### [{{ GM Cheat Sheets}}{{ 14}}](#p14)
  - #### [{{ GM Toolkit}}{{ 16}}](#p16)
  - #### [{{ Desired Final Form & Abilities}}{{ 19}}](#p19)
  - #### [{{ Blank Companion Sheet}}{{ 20}}](#p20)
- ### [{{ Part Two — The Magister's Notebooks}}{{ 21}}](#p21)
  - #### [{{ The Genesis Egg: A Treatise}}{{ 22}}](#p22)
  - #### [{{ Hatchery Ledger: Fire}}{{ 23}}](#p23)
  - #### [{{ Hatchery Ledger: Celestial}}{{ 24}}](#p24)
  - #### [{{ Hatchery Ledger: Eldritch}}{{ 25}}](#p25)
  - #### [{{ Hatchery Ledger: Dream}}{{ 26}}](#p26)
  - #### [{{ Hatchery Ledger: Infernal}}{{ 27}}](#p27)
  - #### [{{ Hatchery Ledger: Chrono}}{{ 28}}](#p28)
  - #### [{{ Private Journals of Magister Othrelis Var}}{{ 29}}](#p29)
- ### [{{ Part Three — Example Companions}}{{ 55}}](#p55)
  - #### [{{ Original Spells — Complete Reference}}{{ 56}}](#p56)
  - #### [{{ Bramblegut, the Chitin Guardian}}{{ 57}}](#p57)
  - #### [{{ Bramblegut — Protection Reference}}{{ 60}}](#p60)
  - #### [{{ Rynnix, the Arc-Shard}}{{ 61}}](#p61)
  - #### [{{ Flubbs, the Shimmer-slime}}{{ 64}}](#p64)
  - #### [{{ Elysian, the Runic Hatchling}}{{ 68}}](#p68)
  - #### [{{ Elysian — Arcane Techniques}}{{ 71}}](#p71)
- ### [{{ Part Four — Aspect Flavour Tables}}{{ 73}}](#p73)
- ### [{{ Companions That Shape the Story}}{{ 80}}](#p80)
- ### [{{ Threads from the Notebooks}}{{ 81}}](#p81)
}}

{{wide,legal
##### CREDITS & LICENCE
**Genesis Eggs: The Endless Possibilities.** Written and designed by Oberon & Omega. Illustrations: Oberon & Omega.

**Genesis Eggs** is an independent fifth-edition-compatible supplement.

This work includes material taken from the System Reference Document 5.1 (“SRD 5.1”) by Wizards of the Coast LLC and available at https://dnd.wizards.com/resources/systems-reference-document. The SRD 5.1 is licensed under the Creative Commons Attribution 4.0 International License available at https://creativecommons.org/licenses/by/4.0/legalcode.

Text and illustrations © 2026 Oberon & Omega. All rights reserved, except SRD 5.1 material, which remains under its licence.
}}

\page {production3,fp3}
![](https://raw.githubusercontent.com/Omegaoliverid/Public-images/main/Genesis-Eggs/approved/frog-hatchling.png){position:absolute,top:0px,left:0px,width:100%,height:100%,object-fit:cover,object-position:center}

{{partcap
##### PART ONE
## Raising a Genesis Egg
The four infusions, the creature that answers them, and the GM tools that keep a companion memorable without letting it outshine the heroes.
}}

\page {rules,production4,fp4}
{{gmtab
GAME MASTER
}}

{{wide,chapterhead
# Genesis Egg: GM Notes on How to Infuse
The egg is shaped by **four infusions**, the environment, and the care of its future companion. Choose one guiding Aspect, but let the player's imagination influence the result.
}}

{{wide,ritual
{{step
#### *STAGE ONE* Initial Infusion
- **Bond:** Choose an Aspect and expend one currently available Hit Die **or** expend one available spell slot. Gain **one level of exhaustion**.
- **GM tracks:** Aspect, resource, delivery, environment and first response.
}}
{{step
#### *STAGE TWO* Sustained Care
- For the **second** infusion, expend one currently available Hit Die or spell slot; gain one exhaustion level.
- Note changing colour, texture, sounds, behaviour, and the balance of Health and Magic.
- Consider how the player handles and nurtures the egg, not merely how often.
}}
{{step
#### *STAGE THREE* Visualisation
- For the **third** infusion, expend one currently available Hit Die or spell slot; gain one exhaustion level.
- Ask the player for the creature's imagined shape, temperament, hopes, fears and name ideas. This vision guides but never guarantees the result.
}}
{{step
#### *STAGE FOUR* Naming & Birth
- For the **fourth** infusion, expend one currently available Hit Die or spell slot; gain one exhaustion level.
- The player names the creature. The GM finalises its Hatchling form, care score, abilities and training potential.
}}
}}

{{wide
## The Aspect Families

{{families
**Elemental:** Fire, Water, Earth, Air, Ice, Lightning, Storm.

**Planar/Spiritual:** Celestial, Infernal, Fey, Shadow, Undead.

**Magical/Ethereal:** Eldritch, Arcane, Dream, Chrono, Illusion, Psionic, Divination.

**Physical/Natural:** Poison, Acid, Plant, Beast, Metal.

**Mythic/Bloodline:** Draconic.
}}

A player may suggest another Aspect, such as Music, Void or Emotion. An Aspect establishes *theme*, not extra spells, immunities or attacks.

{{gm
##### GM Note — The price of haste
Four infusions mean **four exhaustion levels** if made without recovery. This is a serious danger. Each infusion needs a resource the character actually has available. A spent Hit Die cannot be used for short-rest healing until recovered. Recover spell slots, Hit Dice and exhaustion under the normal 2014 rest rules; no exception restores all spent Hit Dice after one long rest. A long rest normally removes only one exhaustion level. A player can hatch an egg slowly or rush the ritual and accept the consequences. Four infusions are the normal total, so most eggs take at least four days to hatch safely. Any spell slot counts as one Magic infusion, whatever its level.

**No spell slots?** One charge from a magic item, or one spell scroll used up, can count as a Magic infusion. Other characters may help by spending their own Hit Die, spell slot, charge or scroll for an infusion, but the bonded character still gains the level of exhaustion.
}}
}}

{{footnote GENESIS EGGS | INFUSING THE EGG}}
{{pageNumber,auto}}

\page {rules,production5,fp5}
{{gmtab
GAME MASTER
}}

# The GM Determines the Creature

{{wide
The GM interprets the chosen Aspect, **four-item Health/Magic infusion ratio**, player's vision and quality of care. Its form and abilities should feel earned. The egg does not automatically grant high-level spells because a strong spell was used during an infusion.

## Infusion Examples

{{gmTable

| Infusions | Outcome | Personality and form |
|:--|:--|:--|
| 4 Magic, Fire Aspect | d4 Hit Die; magical focus | An obsidian drakelet with smoke at its nostrils; one cantrip at hatching, more magic only as it matures and learns. |
| 4 Health, Acid Aspect | d12 Hit Die; no spells | A sturdy, corrosive python; its acid may be a natural attack, but cannot bypass combat limits. |
| 3 Health / 1 Magic | d10 Hit Die; one cantrip maximum | A defensive guardian that may learn minor magic and protective behaviour. |
}}
}}

## Tracking the Care Score

| Score | Bond | Typical behaviour |
|:--:|:--|:--|
| **9–10** | Deep, enduring loyalty | Protects the bonded player; gains **Charmed immunity** while the bond is sustained. Never mindless obedience. |
| **7–8** | Strong affection | Generally reliable, but can question unreasonable or dangerous commands. |
| **4–6** | Uncertain bond | May hesitate, misunderstand, refuse or withdraw. |
| **1–3** | Serious distrust | May flee or turn hostile after sustained betrayal or neglect. |

**Care is story-driven.** Affection, training, shared danger and protection matter. A forgotten meal or one missed roleplay moment is not an automatic penalty. Serious or repeated mistreatment may harm loyalty; good care can gradually repair it. **Changing the score:** the GM raises or lowers it by 1 after a significant act of care or neglect, or by 2 after a defining moment. Charmed immunity at sustained Care 9–10 can be lost and regained through the story, but does not grant immunity to fear or every mental effect.

\column

## Thematic Influences

| Influence | GM use |
|:--|:--|
| Element or spell source | Suggest an appearance, damage type or affinity, not unearned spell levels. |
| Gentle or forceful delivery | Shape confidence, temperament and responses to commands. |
| Surroundings | Suggest a suitable natural sense, movement or narrative quirk. |
| Player's vision | Shape future growth milestones and one or two potential signature traits. |

## GM Principle

The creature is an independent living companion, not equipment. Reward meaningful care through the relationship and earned capabilities, **not through stacking free bonuses**.

{{footnote GENESIS EGGS | THE GM DETERMINES THE CREATURE}}
{{pageNumber,auto}}

\page {production6,fp6}
![](https://raw.githubusercontent.com/Omegaoliverid/Public-images/main/Genesis-Eggs/final-2026-10-17/ember-lynx.jpg){position:absolute,top:0px,left:0px,width:100%,height:100%,object-fit:cover,object-position:center}

\page {rules,production7,fp7}
{{gmtab
GAME MASTER
}}

{{wide
# Genesis Creature Growth & Progression

## Two Separate Kinds of Growth

**Level:** A Genesis Creature has the **same level and proficiency bonus as its bonded player**, including if it hatches halfway through a campaign. It gains HP each level; proficiency improves attacks, skills and spell DCs.  
**Evolution:** The GM chooses when the creature becomes **Hatchling → Juvenile → Adult**. The rare **Ascended** stage requires a major, exceptional story event. Evolution is never automatic at a particular character level.

## Hit Points — Fixed by Infusion

| Health / Magic infusions | Hit Die | Adult spell ceiling |
|:--|:--:|:--|
| 4 Health | d12 | No cantrips or spells |
| 3 Health / 1 Magic | d10 | 1 cantrip only |
| 2 Health / 2 Magic | d8 | 2 cantrips; 1 level-1 and 1 level-2 casting/long rest |
| 1 Health / 3 Magic | d6 | 3 cantrips; 2 level-1, 1 level-2, 1 level-3 casting/long rest |
| 4 Magic | d4 | 3 cantrips; 2 level-1, 2 level-2, **one level-3 OR level-4** casting/long rest |

The Hit Die remains fixed throughout life. **One Hit Die plus the current Constitution modifier is gained at each level**. By default, use the maximum Hit Die value at the first level and the fixed average for each level after, as the example companions do. Later Constitution increases affect new levels only; never retroactively recalculate previous HP. When an egg hatches late, calculate starting HP at the bonded player's current level using its initial Constitution, then track later increases prospectively.

## Ability Score Improvements

At bonded character levels **4, 8, 12, 16 and 19**, the creature becomes eligible for an ASI. The number it can **use** is capped by its current stage: **Hatchling 1, Juvenile 2, Adult 3** (cumulative). A normal ASI grants +2 to one score or +1 to two, or may be exchanged for one modest GM-approved mutation/trait. Evolution also grants **+1 to one suitable score on becoming Juvenile** and another **+1 on becoming Adult**. No other free evolution stat increases stack on top; scores normally cannot exceed **20**. Ascension grants no automatic fourth ASI.

{{gm
**GM Note — Late Hatching and Replacement:** Eligibility uses the bonded character’s **current level**, including thresholds reached before this creature hatched. If a level-10 character legitimately replaces a lost companion, the new creature has two eligible ASIs: it may use **one as a Hatchling**, then **both cumulatively as a Juvenile**, without waiting for level 12. Apply these to the new creature’s own starting scores; the former companion’s traits do not transfer. HP and proficiency likewise use the character’s current level, while attacks, magic and evolution remain stage-limited.
}}
}}

{{footnote GENESIS EGGS | GROWTH AND PROGRESSION}}
{{pageNumber,auto}}

\page {rules,dense,production8,fp8}
{{gmtab
GAME MASTER
}}

{{wide
# Training, Commands and Individuality

## Learning and Mastery

A creature's **growth stage** determines what it can physically do, **training** determines what it understands, and its **Care Score** helps determine whether it chooses to obey.

A creature may complete one points-earning training session per long rest, normally about 30 minutes. The player explains **what** they wish the creature to learn and **how** they teach it. The GM classifies the training as **Simple, Advanced or Complex**, sets an appropriate difficulty, and requests an **ability check reflecting the teaching method**. Add proficiency in a relevant skill when justified. Animal Handling is one possible approach, **not a requirement**. A Barbarian wrestling with a creature to demonstrate a grapple may attempt Strength (Athletics); a Wizard teaching vocabulary may attempt an Intelligence check, adding an appropriate proficiency if justified. Training improves understanding and control; it does **not** grant a new attack, language, spell or special ability beyond the creature’s anatomy, stage and GM-approved feature limits.

| Command difficulty | Suggested cumulative training points |
|:--|--:|
| Simple | 20 |
| Advanced | 35 |
| Complex | 50 |

**Recording training:** Roll **d20 + the relevant ability modifier**, adding a justified skill proficiency for the teaching method. Record that total as points toward the **named command’s cumulative target: Simple 20, Advanced 35 or Complex 50**. A natural 1 earns 0 points and never removes earned points; a natural 20 adds 5 bonus points to the normal total. The roll measures progress toward the cumulative target; it does not bypass anatomy, growth-stage or feature limits.

Once learned, a command becomes **mastered after three separate, meaningful successful demonstrations** that the GM recognises. Advanced is further training of an already mastered Simple command. Complex commands are a separate category and still cost the player an action. Repeating trivial demonstrations does not count. The GM can adapt these benchmarks to the creature's intelligence, nature and story.

## Command Cost — Player Action

| Command trained to | Player's cost | Creature's cost |
|:--|:--|:--|
| Untrained or Simple (learned) | Action | Its action |
| Advanced (a short, trained command) | Bonus action | Its action |
| Complex (multi-step orders and tricks) | Action | Its action |

Untrained instructions require a **full action** and clear directions. For unfamiliar instructions the GM may call for an ability check suited to the instruction and the player’s method (suggested DC 10 for a simple instruction or DC 15 for an advanced instruction). Animal Handling is optional, not mandatory. Complex abilities normally must be learned first. Failed instructions may cause hesitation or defence, **not a free offensive action**. Combat commands earn no training points.

## Standing Orders

Once a creature has been trained in an attack, you can order it to attack a target (such as *attack that goblin*) and it keeps attacking that target each round, spending only its own action. You don't need to repeat the order. Cantrips work the same way. Ordinary instructions such as *guard this doorway* also carry on. The order ends when the target is defeated, or when the GM rules that the creature breaks off: for example after a critical hit or heavy damage from that target, or because its Care Score is low. **To attack again, or to attack a new target, give a new command.** A fleeing assigned enemy can provoke the creature's normal opportunity attack.

**Spells of 1st level or higher never carry on.** Each casting needs a fresh command (your action, or your bonus action if that command is trained to Advanced), plus the creature's action and one of its **own** daily spell castings. A creature may continue concentrating normally on a spell already cast. No spell, ability or language can be commanded before it has been learned.

## Communicating

Speech, trained gestures or a genuinely learned telepathic ability may transmit instructions, if perceptible in context. The bond itself does not give universal telepathy.
}}

{{footnote GENESIS EGGS | TRAINING AND COMMANDS}}
{{pageNumber,auto}}

\page {sheet,rules,production9,fp9}

{{wide,chapterhead
# Genesis Egg Tracker
}}

{{wide
| | | | |
|:--|:--|:--|:--|
| **Egg Name** | | **Aspect** | |
| **Bonded Character / Level** | | **Campaign** | |

### Four Infusions

| Stage | Hit Die or Spell Slot spent | Aspect, care, surroundings | Exhaustion received |
|:--|:--|:--|:--|
| 1 — Initial Infusion | | | +1 |
| 2 — Sustained Care | | | +1 |
| 3 — Visualisation | | | +1 |
| 4 — Naming & Birth | | | +1 |

### Hatching

| | |
|:--|:--|
| **Infusion result** | ____ Health + ____ Magic = **Hit Die** ____ |
| **Creature's first form** | |
| **Imagined temperament / personality** | |
| **Starting Care Score (1–10)** | |
| **Environmental quirks** | |

### Maturity and Growth

| | |
|:--|:--|
| **Current stage** | ☐ Hatchling ☐ Juvenile ☐ Adult ☐ Ascended |
| **Bonded player's current level / PB** | ____ / ____ |
| **Current HP and Hit Die** | ____ HP / d____ |
| **Level-eligible ASIs / applied at current stage** | ____ / ____ |
| **Banked ASI eligibility** | ____ |
| **Juvenile +1 natural score / Adult +1 natural score** | ____ / ____ |
}}

{{footnote GENESIS EGGS | TRACKER}}
{{pageNumber,auto}}

\page {sheet,rules,production10,fp10}

{{wide,chapterhead
# Genesis Egg Tracker — Training & Magic

{{gmtab
GAME MASTER
}}
}}

{{wide
### Training and Magic

| Command/ability | Simple / Advanced / Complex | Points earned | Learned? | Mastery successes (0–3) |
|:--|:--|--:|:--:|:--:|
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |

| | |
|:--|:--|
| **Cantrips actually learned** | |
| **Fixed levelled spells actually learned** | |
| **Today's remaining levelled castings** | L1 ____ / L2 ____ / L3 ____ / L4 ____ |
| **Care Score developments** | |
| **GM-only evolution milestones** | |
| **Teaching method / ability check** | |
| **Custom reaction uses remaining** | Feature ____ / uses ____ |
| **Flight stage / rider restrictions** | See [Flight and Gliding](#p13) |

> Training targets are **20 / 35 / 50**, with one points-earning session per long rest and three meaningful mastery demonstrations. Use a check suited to the teaching method; Animal Handling is optional. Reaction spells consume both the reaction and an existing casting, with a fresh instruction for each casting.

> Track only abilities the creature genuinely has. Its current infusion/stage spell ceilings are the **most** it can know; it learns spells up to them on reaching each new stage. Evolution and mastery are decided by the GM.
}}

{{footnote GENESIS EGGS | TRACKER}}
{{pageNumber,auto}}

\page {rules,production11,fp11}
{{gmtab
GAME MASTER
}}

# Creating a Balanced Companion

## Step 1 — Starting Ability Scores

Genesis Creatures are neither full player characters nor ordinary monsters. For a normal Hatchling start with **13, 12, 12, 10, 10, 8**, assigning scores to fit its anatomy, Aspect and intended role. GM-approved point buy or rolled scores are possible, but the normal **starting ceiling is 14**. Later ASIs and natural evolution may raise scores towards the overall cap of 20. The four example companions in Part Three use bespoke GM-approved starting scores to illustrate their roles; they are not standard point-buy build recipes.

## Step 2 — Give It a Clear Role

Choose one mechanical **creature type** at hatching; terms such as insectoid or storm describe its form.

Choose one **primary role**: Physical Striker, Guardian, Balanced Support/Controller, Magical Striker or Noncombat/Utility. Avoid making a creature excel at all of them. It is proficient in one saving throw and one or two skills that fit its role and Aspect.

A newly hatched companion normally has one primary natural attack, a minor aspect expression and perhaps one simple role-appropriate trait. Significant effects must spend creature actions and obey the resource limits. Not every creature needs combat magic.

## Step 3 — Level and Stage

Its **level and proficiency match its bonded player** from the day it hatches. Use the fixed infusion Hit Die and its Constitution when calculating HP. Its **growth stage remains GM-controlled**. HP and proficiency may rise while the Hatchling retains its modest stage abilities.

\column

## Step 4 — Select Features

The GM and player may discuss a few potential future traits, but wishes are not guarantees. Unlock new capabilities through meaningful bonding, study, challenge and evolution. **Learning spells:** when a creature reaches a new stage, it learns spells up to that stage's limit (see the magic table on page 14). The player and GM choose them together from any spell list that fits its Aspect. It casts using its highest mental ability (Intelligence, Wisdom or Charisma). A new spell's selection becomes fixed after it is gained, barring a major GM-approved story arc.

Hoped-for wings do not grant Hatchling flight. See [Flight and Gliding by Growth Stage](#p13).

## Quick Build Checklist

☐ Four available-resource infusions recorded  
☐ Hit Die and level-appropriate HP calculated  
☐ Starting scores, proficiency and Care Score assigned  
☐ Primary attack, movement, senses and role chosen  
☐ Stage-appropriate magic and traits only  
☐ Command training and development goals noted  
☐ No duplicate spell resources or extra combat turns

{{gm
**GM Tip:** A creature with a strong defensive wall should not also have the most damaging attack, unlimited magic and a powerful always-on aura. Specialisation makes each bond unique and keeps players in the spotlight.
}}

{{art,height:250px
![](https://raw.githubusercontent.com/Omegaoliverid/Public-images/main/Genesis-Eggs/final-2026-10-17/guardian.jpg)
}}

{{footnote GENESIS EGGS | CREATING A BALANCED COMPANION}}
{{pageNumber,auto}}

\page {rules,production12,fp12}
{{gmtab
GAME MASTER
}}

# Unlocking Abilities and Evolution

{{wide
| Path | Appropriate story example | Mechanical treatment |
|:--|:--|:--|
| Training | Creature practises an attack or learns a hand signal | Earn command points and demonstrations; no new spell resource. |
| Bond | Creature shields its companion in danger | May develop an appropriate protective reaction. |
| Study | Rune-winged drakelet reads rare manuscripts | Learns knowledge or languages, without automatic magical translation. |
| Aspect | Acid creature endures corrosive conditions | Develops a natural adaptation within its role. |
| Evolution | Creature saves the party in a defining moment | GM permits the next physical stage and its defined unlocks. |
}}

The GM may secretly track goals, but should not require arbitrary damage totals or successful dice rolls as the *only* way to evolve. A meaningful story event can be enough.

## Example — Fire-Aligned Hatchling

**Kaelthos, an obsidian drakelet:** d4, as all four of its infusions were Magic; initially a modest ember-themed creature with one learned cantrip, a natural scratch or bite, and a cold-resistance-themed quirk if the GM allows it. Later its wings and special fire abilities can develop through training and story milestones. Any levelled fire technique consumes the appropriate learned spell casting; it is not a free rechargeable extra attack.

\column

## Special Ability Safeguards

- **Natural attack:** One main attack action, growing with Hatchling/Juvenile/Adult size and stage; no automatic Extra Attack.
- **Cantrip:** Repeatable, but still uses the creature's action; damage normally scales by stage (roughly one die, two dice, three dice) rather than PC level.
- **Spell-equivalent power:** Benchmarked against an existing spell, charged to an existing daily casting, obeys saves, concentration, commands and the stage ceiling.
- **Harmless expression:** Light, colour, warmth, chirping or decorative illusion may be free roleplay if it has no consequential effect.
- **Exceptional Ascension:** One GM-approved fifth-level-equivalent signature casting **once per long rest**; no legendary actions or general spell levels 5–9.

{{art,height:260px
![](https://raw.githubusercontent.com/Omegaoliverid/Public-images/main/Genesis-Eggs/final-2026-10-17/growth.jpg)
}}

{{footnote GENESIS EGGS | UNLOCKING ABILITIES}}
{{pageNumber,auto}}

\page {rules,dense,mechanicsReference}
{{gmtab
GAME MASTER
}}

{{wide
# Flight and Gliding by Growth Stage

**Hatchling:** Cannot fly or hover. Where the creature has appropriate anatomy or a GM-approved magical means of controlled descent, it may **glide while descending**; gliding cannot gain height or sustain level flight.

**Juvenile:** May make short flights and may glide while descending. It cannot hover or remain airborne indefinitely; it must land or reach a supporting surface at the end of its turn.

**Adult:** May have sustained flight if its developed anatomy or earned Aspect traits justify it. **May not be used as a flying mount**, regardless of carrying capacity.

**Ascended:** May fly. Carrying a rider is **never automatic**: it requires GM approval, suitable anatomy, sufficient size relative to the rider, and ordinary carrying-capacity and mount rules.

**Scouting:** Flying or gliding does not grant telepathy, perfect vision or safety. A scouting creature can be separated, spotted, ambushed, captured, injured or killed. Apply ordinary perception, stealth, communication, distance and encounter procedures.

## Controlled Movement

A controlled glide converts each **5 feet descended into up to 10 feet of horizontal movement**; no climbing or hovering. An uninterrupted controlled glide ending on a safe surface avoids ordinary falling damage; if gliding is disrupted, apply the ordinary falling rules. A Juvenile can use **up to 20 feet of flight during its turn** and must end on support; it cannot carry a rider. Movement may be more restrictive for unusual forms at the GM’s discretion.
}}

{{footnote GENESIS EGGS | RULES REFERENCE}}
{{pageNumber,auto}}
\page {rules,production13,fp13}
{{gmtab
GAME MASTER
}}

{{wide
# GENESIS CREATURE — GM CHEAT SHEET

## Egg Infusion and Magic, at a Glance

| Infusions | Hit Die | Hatchling maximum | Juvenile maximum | Adult maximum |
|:--|:--:|:--|:--|:--|
| 4 Health | d12 | No magic | No magic | No magic |
| 3H / 1M | d10 | 1 cantrip | 1 cantrip | 1 cantrip |
| 2H / 2M | d8 | 1 cantrip | 1 cantrip + one L1 | 2 cantrips + one L1 + one L2 |
| 1H / 3M | d6 | 1 cantrip | 2 cantrips + one L1 + one L2 | 3 cantrips + two L1 + one L2 + one L3 |
| 4 Magic | d4 | 1 cantrip | 2 cantrips + one L1 + one L2 | 3 cantrips + two L1 + two L2 + one L3 **or** L4 |

**L1–L4 mean levelled spell castings per long rest;** they are not spell levels automatically known. The optional L3 **or** L4 casting is a shared resource. A cantrip may be repeated when learned, but each use still needs the creature's action.

## Four Moments in the Egg's Story

| Infusion | Ask the player | GM records |
|:--|:--|:--|
| 1 | What Aspect shapes the egg? | Health/Magic, Aspect, exhaustion |
| 2 | How are you caring for it? | Continued care, visible changes |
| 3 | What creature do you imagine? | Vision, bond, temperament |
| 4 | What do you name it? | Final ratio, Hatchling form and score |

Each infusion spends **one available Hit Die or spell slot** and gives one exhaustion level; normal 2014 resting rules apply.

## Attack and Magic Formula

**Attack bonus** = proficiency bonus + relevant ability modifier.  
**Saving throw DC** = 8 + proficiency bonus + relevant ability modifier.  
Avoid invented high DCs and stacked damage-plus-control as routine attacks. Significant concentration effects use normal spell rules. A creature and its bonded PC can concentrate on separate spells.

**Movement:** Hatchlings cannot fly/hover; Juveniles use at most 20 ft. of flight and end on support; Adults cannot be flying mounts; Ascended riding requires approval, anatomy, size and capacity. See [Flight and Gliding](#p13).

## Defence and Utility

A modest protective instinct can spend the creature's reaction. Strong magic protection requires that reaction **and** an appropriate remaining levelled spell casting. A creature has one reaction between refreshes. Language learning, ordinary knowledge and harmless roleplay are not free spellcasting.

Custom reactions that prevent or redirect damage, impose a new defensive penalty on an attack, or add retaliatory damage must have a clearly written trigger, range, target, timing and **uses per long rest** or consume an existing finite spell resource. The ordinary one-reaction-per-round rule is **not by itself** a sufficient limit for unusually strong custom features. An ordinary opportunity attack or other normal 5e reaction does not acquire a special daily cap merely because it is a reaction. Spell-equivalent reactions still spend the appropriate spell casting.
}}

{{footnote GENESIS EGGS | GM CHEAT SHEET}}
{{pageNumber,auto}}

\page {rules,dense,production14,fp14}
{{gmtab
GAME MASTER
}}

{{wide
# GENESIS CREATURE — GM CHEAT SHEET

## Command and Turn Reference

- The player and companion **share initiative**, choose who finishes a turn first, and do not interleave turns.
- The creature has **one main action**, ordinary movement and its normal reaction; no extra actions, legendary actions or automatically free attacks.
- **Command cost:** a learned command costs your action; once trained to Advanced it costs your bonus action; Complex orders cost your action. The creature always spends its own action.
- Untrained commands require clear instructions and **player action**, using a check suited to the teaching/instruction method; Animal Handling is optional. They cannot unlock unknown abilities.
- **Standing attacks:** once trained, an attack or cantrip order continues against its target each round for the creature's action only, until the target is defeated or the GM rules the creature breaks off (a critical hit, heavy damage or low Care). A new target needs a new command. **Every levelled spell** needs a fresh command (bonus action if trained to Advanced), the creature's action and one of its own daily castings; reaction spells still require fresh direction. Runic Shield directions expire at the start of the player’s next turn.
- If the bonded PC falls, the companion can defend, protect, retreat, continue suitable orders or seek help by instinct; GM judges its personality.

## Death, Recovery and Care

Genesis Creatures make **normal death saving throws**, secretly or openly as agreed by the GM and table. They can die permanently. Normal eligible healing, short-rest Hit Die recovery and long-rest recovery apply. Ordinary resurrection works if its spell requirements are met; rare story rebirth is optional and never guaranteed. A creature survives its bonded PC's death and retains its mind and experience. A new bond is exceptional, never automatic.

## One Stable Bond

Each player character normally sustains **one stable Genesis Creature bond at a time**. A later egg may be discovered or raised, but attempting simultaneous stable bonds invites GM-driven, hidden story consequences. A new bond after death, release or permanent separation is possible with GM approval. There is **no arbitrary party-wide companion cap**.

{{gm
##### Var’s Extraordinary Connections
Var’s case files describe overlapping connections, intrusions and an infernal contract, not six ordinary stable bonds. Seraphiel chose to remain at the temple; no deliberate release occurred and their connection persisted. These unresolved narrative anomalies do not change the normal one-stable-bond rule or grant player characters additional bonds.
}}

## GM's Hidden Evolution Prompts

| Player's hope | Narrative opportunity |
|:--|:--|
| A protector | Risks itself to shield someone |
| A scholar | Learns through genuine study and discovery |
| A storm spirit | Channels power responsibly in a crisis |
| A performer | Builds trust through important shared performances |

Do not announce fixed evolution thresholds. Choose what the creature's journey has genuinely earned.
}}

{{footnote GENESIS EGGS | GM CHEAT SHEET}}
{{pageNumber,auto}}

\page {rules,dense,production15,fp15}
{{gmtab
GAME MASTER
}}

{{wide
# GM Toolkit — Building a Creature That Works

## Begin With the Story

1. Record the **four infusions** to set the permanent Hit Die and maximum magical allowance.
2. Choose one primary role and **one primary natural attack**.
3. Give the creature its bonded player's **level and proficiency**. Its physical stage is a separate story decision.
4. Give starting abilities (normally no score above 14), level-eligible ASIs (subject to stage limits), and earned evolution bonuses. Example: a creature beginning with a 14 in its main ability can reach 17 as a level-7 Juvenile (+2 earned ASI, +1 evolution), or 20 by level 12 as an Adult (+2 further earned ASI and +1 evolution); the third available ASI can improve another score.
5. Add a manageable selection of senses, movement, an Aspect trait and one role trait. Every consequential feature must have an action, reaction, resource or meaningful limit. Custom protective/offensive reactions need finite uses or an existing casting, not only the normal reaction limit.
6. Record commands, Care Score, training progress and future story goals.

## Practical Role Benchmarks

| Role | Strongest contribution | Avoid also giving it... |
|:--|:--|:--|
| Physical Striker | Reliable natural damage | Exceptional protection or repeated battlefield control |
| Guardian | HP, protection, cover | Striker damage and strong offensive magic |
| Balanced Support/Controller | Moderate damage plus one role utility | Dominating either damage or spellcasting |
| Magical Striker | A few learned spells within a strict daily budget | Extra recharge-based spell-equivalent attacks |
| Noncombat/Utility | Knowledge, scouting, companionship | Treating every social ability as a hidden combat buff |

**Natural-attack benchmarks when an attack hits (Adult):** Guardian about `2d10 + 4`; dedicated striker about `3d10 + 4` if it gives up major control/defence; balanced about `2d8 + 3`; magical repeatable attack about `3d4 + 3`. These are GM comparisons, not mandatory builds. Hatchlings start far below those values.

## AC, HP, Attack Bonus and DC

Use the campaign's normal HP rolling/fixed method and the creature's assigned Hit Die. Avoid treating a high AC or a collection of resistances as a free gift. Sample AC bands for ordinary builds might be 12–14 Hatchling, 14–17 Juvenile and 15–19 Adult, with the upper end reserved for a genuinely defensive concept. Attack bonuses and save DCs always follow proficiency + ability, not invented fixed values.

> A companion should be useful, memorable and capable of being hurt. The players remain the main heroes.
}}

{{footnote GENESIS EGGS | GM TOOLKIT}}
{{pageNumber,auto}}

\page {rules,dense,production16,fp16}
{{gmtab
GAME MASTER
}}

{{wide
# GM Toolkit — Protection, Control and Magic

## Control Is Not Free Extra Damage

A guardian might knock enemies prone as it matures, then learn a separate grapple or restraint technique. Powerful restraint is usually its **own action**, rather than an extra condition on a maximum-damage attack. A creature can generally restrain up to its size; a target one size larger has advantage on the initial save and escape; two sizes larger is ordinarily impossible. Maintaining strong restraint usually costs the creature's action each round. Enemies can attempt to escape using the encounter's normal action rules.

## Custom Reaction Budgets

**Suggested non-spell custom reaction budgets (suggested guidelines):** Hatchling 1/long rest; Juvenile 2/long rest; Adult 2/long rest for major protection or 3/long rest for modest protection; Ascended normally no more than the Adult budget unless an exceptional story reward explicitly changes it. Reduce uses when the effect is more powerful, transfers damage at a discount, gives broad protection, or adds substantial off-turn damage. These are GM design guidelines, not automatic new abilities. Explicit use limits in a creature’s stat block govern.

## Bramblegut's Illustrative Guardian Abilities

**Interception:** Guardian Instinct (1/long rest), Guardian Interception (2/long rest) and Guardian’s Vow (2/long rest) prevent at most the actual damage from one attack. Bramblegut must be conscious, able to react and in reach. No interception while maintaining its wall. Use the complete [Protection Reference](#p60).

**Verdant Shield Wall (Adult; 2/long rest):** Adjacent, opaque 10-foot-wide by 10-foot-high physical shield; AC 17, 25 HP, at most two rounds. Create and maintain with actions; no enclosing dome, movement, attack, casting or interception. Own AC 22 while maintaining. Full cover and ending conditions: [Protection Reference](#p60).

## Auras

Harmless light or scent can be constant; a consequential aura is not. A mild zone might allow movement, while a strong battlefield-control aura should usually require **activation and continued creature action** every round, appropriate concentration and restricted movement. Do not give an always-on party-wide defence plus a damaging attack as another free benefit.

## Magical Techniques

If an effect functions like a spell, compare it to a published spell's targeting, damage, duration, saves and concentration. A special magical technique consumes one existing casting of the matching level (or stronger), even when given a thematic name. A significant magical protective reaction uses both a **reaction** and an appropriate casting. No double concentration; no unlimited spell-equivalent recharge abilities.

## Ascension

Ascension is a GM-created exceptional story reward, not a level milestone. It may grant **one fifth-level-equivalent signature ability, once per long rest**. This normally needs a player **action** to command; exceptional mastery can later make that player command a **bonus action**, but the creature still spends its own action and the one daily use. Add modest flavour changes, not legendary actions, blanket immunities or immortality.
}}

{{footnote GENESIS EGGS | GM TOOLKIT}}
{{pageNumber,auto}}

\page {rules,production17,fp17}
{{gmtab
GAME MASTER
}}

{{wide
# GM Toolkit — Encounters and Hidden Bonds

## Genesis Companions: Encounter Adjustment

Build a challenging encounter for the **player characters alone** using the campaign’s ordinary 2014 5e encounter-building method. Then consider **only Genesis Creatures that meaningfully contribute to that encounter**: attacking, defending allies, healing, controlling the battlefield, or using practical utility that changes the fight. A creature used for companionship, social interaction or out-of-combat scouting and **not participating in the battle** adds **no combat adjustment**. Judge the **role and impact**, not simply the number of bonded eggs: an offensive striker, a guardian intercepting damage and a support/control caster alter the fight in different ways. A noncombat companion forced into danger does not automatically count as a combat contributor.

If active companions make the encounter too easy, adjust the **overall encounter XP budget, number of enemies, objectives and tactics** in measured steps rather than simply raising one monster’s CR. Re-check attack accuracy, saving throws, area damage, available spell castings, defensive uses and the action economy. Never increase a single enemy's CR mechanically by the numbers below: monster XP is non-linear and single-boss lethality can spike. Do not target companions unfairly to cancel their benefits. Start conservatively, observe, revise and record.

**Quick rule:** when building an encounter, count each **Juvenile or older** companion that will actively fight as **half a character**. Hatchlings, and companions that stay out of the fight, count as nothing. Adjust from there once you've seen how your table plays.

## One Bond — Secret GM Story Hooks

Players may *find* more than one egg, but normally keep **only one stable bonded companion**. If someone tries to foster a second, the GM may weave in jealousy, distance, changed loyalties, rival behaviour, separation, a creature leaving, a strange illness requiring care, or a former companion returning later as an antagonist. **None is an automatic punishment.** Preserve the story, fair warning through roleplay, and the creature's agency. Keep the precise consequences hidden from players.

A PC whose bond ends through death, genuine release or permanent separation may form a new bond with GM approval. Six PCs can each have one companion. The GM need not impose a party-wide participation cap.
}}

{{footnote GENESIS EGGS | GM TOOLKIT}}
{{pageNumber,auto}}

\page {sheet,production18,fp18}

{{wide,chapterhead
# Desired Form & Abilities
##### STAGE THREE — VISUALISATION
*This section is to be completed by the player as they begin bonding with the egg. It helps the GM align creature growth with the player's hopes and dreams.*
}}

**Creature Name (or Working Name):**
{{writebox,min-height:1.1cm
&nbsp;
}}

**Visual Description:**
{{writebox,min-height:2.6cm
*(Colour, size, posture, features — feathers, scales, wings, claws, etc.)*
}}

**Movement Type:**
- [ ] Walking
- [ ] Flying
- [ ] Burrowing
- [ ] Climbing
- [ ] Swimming
- [ ] Teleporting/Phasing

**Temperament/Personality Goals:**
{{writebox,min-height:2.2cm
*(Kind? Fierce? Stoic? Trickster?)*
}}

**Draw them:**
{{writebox,min-height:5.2cm
&nbsp;
}}

\column

**Primary Role (choose one):**
- [ ] Physical Striker
- [ ] Guardian
- [ ] Balanced Support/Controller
- [ ] Magical Striker
- [ ] Noncombat/Utility

<p class="optional-hopes"><strong>Other hopes (optional):</strong> ____________________</p>

**Magical Focus (if applicable):**
{{writebox,min-height:3.4cm
Desired Schools:

Thematic Spells (suggested or invented):

1. ______________________________
2. ______________________________
3. ______________________________
}}

**Special Features Hoped For (Pick 2–3):**
{{writebox,min-height:3.0cm
*(e.g., breath weapon, teleportation, healing aura, time stop, illusion cloak)*
}}

**Ultimate Vision / "Ascended" Form Dream:**
{{writebox,min-height:3.0cm
*(What is the peak version of this creature? Let your imagination go big — wings that leave stardust, a roar that freezes time, etc.)*
}}

> This is a dream, not a contract. The GM will interpret this to create a satisfying and balanced progression path.

Hoped-for wings do not grant Hatchling flight. See [Flight and Gliding by Growth Stage](#p13).


{{footnote GENESIS EGGS | PLAYER VISION WORKSHEET}}
{{pageNumber,auto}}

\page {blankSheet,sheet,production19,fp19}
# Creature Name: ______________________________
*Small/Medium/Large [Type], [Alignment]*

### **Armor Class**: __  
### **Hit Points**: __ 
(Creature level \_\_; fixed infusion Hit Die d\_\_; track Constitution changes by level)  
### **Speed**: __ ft.

### **Visual Characteristic:**
- __

{{statLine
| STR | DEX | CON | INT | WIS | CHA |
|-----|-----|-----|-----|-----|-----|
|     |     |     |     |     |     |
}}

### Saving Throws:
- __

### Skills:
- __

### Damage Resistances:
- __

### Damage Immunities:
- __

### Condition Resistances & Immunities:
- __

### Senses:
- Passive Perception __  

### Languages:
- (Can communicate with bonded PC? ☐ Yes ☐ No) 

\column

### Traits & Temperament
- __

**Bonded Companion.**  
This creature shares initiative with its bonded PC. Its normal actions and standing orders obey the Genesis command rules; the GM decides instincts, loyalty and refusal.

**Aspect Infused.**  
This creature was formed by the [Aspect] influence. It **may** gain GM-approved Aspect traits or resistances within its role and balance limits; an Aspect is not a free grant of resistance, immunity or spellcasting.

**(Custom Trait):**  
_Description._

### Actions

**[Primary Attack Name].**      
*Melee/Ranged Weapon Attack:* +__ to hit, reach __ ft., one target.  
Hit: __ (__ damage type__) damage.

**[Special Ability].** (action / reaction / remaining spell casting: __)  
_Description of a magical or aspect-based ability._

### Reactions (if applicable)

**[Reaction Name].** _Trigger; perceived target; range; before/after-roll timing; effect; reaction cost; uses per long rest or existing casting spent._

### Bonus Actions (if applicable)

**Optional Bonus Action:**  
_Description._

### Development Notes
- Hatched from: Genesis Egg (Aspect: ____________)  
- Infusion mix: ____ Health / ____ Magic (d__)  
- Personality Notes: ____________________  
- Current Care Score (1–10): __  
- Bond Quirks: _________________________
- ASIs used (level / score): __________________
- Juvenile evolution +1: ____; Adult evolution +1: ____  

{{footnote GENESIS EGGS | BLANK COMPANION SHEET}}
{{pageNumber,auto}}

\page {production20,fp20}
{{wide,notebookTitle
##### PART TWO
# The Magister’s Notebooks
}}

![](https://raw.githubusercontent.com/Omegaoliverid/Public-images/main/Genesis-Eggs/approved/first-egg-forge-study.png){position:absolute,top:230px,left:18px,width:758px,height:620px,object-fit:contain,mix-blend-mode:multiply}

{{partcap
Six eggs, six hatchings, and one scholar who learned — slowly, and at some cost — that a Genesis Egg is never only an experiment.
}}

\page {journal,production21,fp21}

{{wide,treatiseTitle
# The Genesis Egg: A Treatise on Incubation, Bonding, and Becoming
##### BY MAGISTER OTHRELIS VAR, DEAN EMERITUS OF LIVING THAUMATURGY
}}

{{wide,treatiseLetter
## Foreword
To the Bearer of the Egg,

What you now hold is no trinket, no mere bauble of arcane curiosity. It is a Genesis Egg—an artefact of unfathomable potential and equally perilous consequence.

These eggs do not choose lightly. If one has found you, then consider yourself part of a process far older and more deliberate than you may suspect. You are not a keeper. You are not a master. You are a participant.

In this document, I have outlined the known stages of incubation, from the initial spark of connection to the final moment of hatching. I urge you to follow this process not as a formula—but as a ritual. Each stage is an invitation. How you respond will shape what is born.

The creature that will emerge is no mere summon. It is a reflection. Of what, you ask?

That remains to be seen.

May your path be careful, and your choices true.

— *Magister Othrelis Var*  
Dean Emeritus, College of Living Thaumaturgy  
Last Custodian of Chronis, the Gilded Wing  


}}

<div class="treatisePath"><span>I<br>Initial Infusion</span><span>II<br>Sustained Care</span><span>III<br>Visualisation</span><span>IV<br>Naming & Birth</span></div>
<div class="scholarMark">O · V<br><small>College of Living Thaumaturgy</small></div>
\page {rn,fp22}
<style>

@import url('https://fonts.googleapis.com/css2?family=Caveat:wght@400;600;700&family=Reenie+Beanie&family=Nanum+Pen+Script&family=IM+Fell+English+SC&display=swap');
.page.rn, .page.diary { width: 210mm; height: 296.8mm; padding: 0; font-family: 'Caveat', cursive; color: #2a1d14; background-color: #eadbbb;
  box-shadow: inset 0 0 90px rgba(110,70,25,0.55), inset 0 0 22px rgba(90,55,20,0.45); }
.page.rn .columnWrapper { column-count: 1; height: 100%; }
.page.rn p, .page.diary p { font-family: 'Caveat', cursive; font-size: 18.5px; line-height: 1.12em; margin: 0 0 4px; text-indent: 0; color: inherit; }
.page.rn p + p, .page.diary p + p { text-indent: 0; margin-top: 2px; }
.page.rn h1 + p::first-letter, .page.diary h1 + p::first-letter, .page.diary h2 + p::first-letter { float: none; padding: 0; margin: 0; font-family: inherit; font-size: inherit; line-height: inherit; color: inherit; background-image: none; -webkit-background-clip: border-box; background-clip: border-box; }
.page.rn h1 + p::first-line, .page.diary h1 + p::first-line, .page.diary h2 + p::first-line { font-variant: normal; }
.page.rn strong, .page.diary strong { font-weight: 700; }
.page.rn del, .page.diary del { text-decoration: none; background: linear-gradient(transparent 48%, #8b2e1a 48%, #8b2e1a 60%, transparent 60%); }
.page.rn .blk { position: absolute; }
.page.rn .footnote, .page.diary .footnote, .page.rn .pageNumber, .page.diary .pageNumber { display: none; }
.page .ring { position: absolute; width: 150px; height: 150px; border-radius: 50%; pointer-events: none;
  background: radial-gradient(circle, transparent 58%, rgba(120,75,30,0.16) 61%, rgba(120,75,30,0.05) 66%, transparent 70%); }
.page .blot { position: absolute; width: 34px; height: 26px; border-radius: 48% 52% 45% 55%; background: radial-gradient(circle at 40% 40%, rgba(30,20,12,0.75), rgba(30,20,12,0.55) 55%, transparent 70%); }
/* header */
.page.rn .hdr { left: 52px; top: 34px; width: 690px; }
.page .ledger { font-family: 'IM Fell English SC', serif; font-size: 13px; letter-spacing: 0.28em; color: #6b5233; margin: 0; }
.page .ledger p { font-family: inherit; font-size: inherit; letter-spacing: inherit; color: inherit; margin: 0; }
.page.rn .hdr h1 { font-family: 'Caveat', cursive; font-weight: 700; font-size: 58px; line-height: 1em; color: #22160e; margin: 0 0 2px; padding-bottom: 10px; border: none;
  background: url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='300' height='12' viewBox='0 0 300 12'><path d='M2 8 C 60 2, 120 11, 180 6 S 270 3, 298 7' stroke='%237a2a17' stroke-width='2.2' fill='none' stroke-linecap='round'/></svg>") no-repeat left bottom / 270px 12px; }
.page.rn .hdr p { font-size: 20px; margin: 0; }
.page .anno { font-family: 'Reenie Beanie', cursive; color: #8b2e1a; font-size: 25px; line-height: 0.9em; }
.page .anno::before { content: '\2190\00a0'; font-family: 'Caveat'; }
.page.rn .hdr .anno { position: absolute; left: 330px; top: 70px; transform: rotate(-3deg); white-space: nowrap; }
.page .stamp { position: absolute; padding: 6px 8px; border: 3px double rgba(139,46,26,0.6); border-radius: 6px;
  text-align: center; font-family: 'IM Fell English SC', serif; color: rgba(139,46,26,0.72); font-size: 15px; letter-spacing: 0.1em; line-height: 1.15em; }
.page .stamp { width: max-content; }
.page .stamp p { font-family: inherit; color: inherit; font-size: inherit; margin: 0; letter-spacing: inherit; line-height: 1.2em; }
/* entries */
.page .date { font-family: 'Caveat', cursive; font-weight: 700; font-size: 20px; color: #5a1f12; margin: 8px 0 1px;
  border-bottom: 1px solid rgba(90,31,18,0.35); display: inline-block; padding-right: 10px; }
.page .date p { font-size: inherit; font-weight: inherit; color: inherit; margin: 0; }
.page .ink1 { color: #2a1d14; }
.page .ink2 { color: #1f2733; }
.page .ink2 .date { color: #22324d; border-color: rgba(34,50,77,0.35); }
/* sketches */
.page .sk { position: absolute; background-size: cover; background-position: center; mix-blend-mode: multiply;
  -webkit-mask-image: radial-gradient(closest-side, #000 70%, transparent 100%); mask-image: radial-gradient(closest-side, #000 70%, transparent 100%); }
.page .sk.soft { -webkit-mask-image: radial-gradient(farthest-side, #000 76%, transparent 100%); mask-image: radial-gradient(farthest-side, #000 76%, transparent 100%); }
.page .photo { position: absolute; padding: 6px; background: #f1e6cc; box-shadow: 1px 2px 5px rgba(60,35,10,0.35); }
.page .photo .pi { position: absolute; inset: 6px; background-size: cover; background-position: center; mix-blend-mode: multiply; }
.page .tape { position: absolute; width: 70px; height: 20px; background: rgba(236,226,190,0.78); box-shadow: 0 1px 2px rgba(0,0,0,0.15); }
.page .cap { position: absolute; font-family: 'Caveat', cursive; color: #4a3523; line-height: 1em; }
.page .cap p { font-size: 16px; color: #4a3523; margin: 0; line-height: 1.02em; }
.page .doodle { position: absolute; background-size: contain; background-repeat: no-repeat; opacity: 0.8; }
/* later slip */
.page .slip { position: absolute; padding: 9px 14px 6px; background: #f4ecd9; box-shadow: 2px 3px 8px rgba(60,35,10,0.35);
  background-image: repeating-linear-gradient(transparent 0 20px, rgba(70,90,130,0.18) 20px 21px); }
.page .slip p { font-family: 'Nanum Pen Script', cursive; color: #23324a; font-size: 19px; line-height: 21px; margin: 0; }
.page .slip .date { font-family: 'Nanum Pen Script', cursive; color: #23324a; font-size: 21px; border-color: rgba(35,50,74,0.35); margin-top: 0; }
.page .slip strong { font-weight: 700; }
.page .slip .date:not(:first-child) { margin-top: 8px; }
.page .foot { position: absolute; white-space: nowrap; font-family: 'IM Fell English SC', serif; font-size: 12px; color: #7a6040; letter-spacing: 0.2em; }
.page .foot p { font-family: inherit; font-size: inherit; color: inherit; margin: 0; letter-spacing: inherit; }

.page .d-arrow { background-image: url("data:image/svg+xml;utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 60 60'%3E%3Cg fill='none' stroke='%234a3523' stroke-width='1.8' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M6 44 C 20 20, 38 14, 54 18'/%3E%3Cpath d='M46 12 L 54 18 L 47 25'/%3E%3C/g%3E%3C/svg%3E"); }
.page .d-arrowdn { background-image: url("data:image/svg+xml;utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 60 60'%3E%3Cg fill='none' stroke='%234a3523' stroke-width='1.8' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M30 4 C 18 20, 40 34, 28 54'/%3E%3Cpath d='M22 47 L 28 55 L 35 48'/%3E%3C/g%3E%3C/svg%3E"); }
.page .d-star { background-image: url("data:image/svg+xml;utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 60 60'%3E%3Cg fill='none' stroke='%234a3523' stroke-width='1.8' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M30 6 L 34 26 L 54 30 L 34 34 L 30 54 L 26 34 L 6 30 L 26 26 Z'/%3E%3C/g%3E%3C/svg%3E"); }
.page .d-egg { background-image: url("data:image/svg+xml;utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 60 60'%3E%3Cg fill='none' stroke='%234a3523' stroke-width='1.8' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M30 6 C 14 6, 8 30, 10 40 C 12 52, 22 56, 30 56 C 38 56, 48 52, 50 40 C 52 30, 46 6, 30 6 Z'/%3E%3Cpath d='M22 24 L 28 30 L 24 36 M 34 18 L 38 26' stroke-width='1.2'/%3E%3C/g%3E%3C/svg%3E"); }
.page .d-flame { background-image: url("data:image/svg+xml;utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 60 60'%3E%3Cg fill='none' stroke='%23a3401c' stroke-width='1.8' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M30 56 C 14 56, 12 40, 20 30 C 22 38, 26 38, 26 34 C 24 24, 30 14, 36 6 C 36 18, 50 26, 46 42 C 44 52, 38 56, 30 56 Z'/%3E%3C/g%3E%3C/svg%3E"); }
.page .d-eye { background-image: url("data:image/svg+xml;utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 60 60'%3E%3Cg fill='none' stroke='%234a3523' stroke-width='1.8' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M4 30 C 18 12, 42 12, 56 30 C 42 48, 18 48, 4 30 Z'/%3E%3Ccircle cx='30' cy='30' r='8'/%3E%3Ccircle cx='30' cy='30' r='2.5' fill='%234a3523'/%3E%3C/g%3E%3C/svg%3E"); }
.page .d-clock { background-image: url("data:image/svg+xml;utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 60 60'%3E%3Cg fill='none' stroke='%234a3523' stroke-width='1.8' stroke-linecap='round' stroke-linejoin='round'%3E%3Ccircle cx='30' cy='30' r='24'/%3E%3Ccircle cx='30' cy='30' r='20' stroke-width='0.8'/%3E%3Cpath d='M30 30 L 30 14 M 30 30 L 41 36'/%3E%3Cpath d='M30 8 L30 11 M52 30 L49 30 M30 52 L30 49 M8 30 L11 30' stroke-width='1.2'/%3E%3C/g%3E%3C/svg%3E"); }
.page .d-swirl { background-image: url("data:image/svg+xml;utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 60 60'%3E%3Cg fill='none' stroke='%235b6a8a' stroke-width='1.8' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M30 30 C 30 26, 36 26, 36 31 C 36 38, 25 38, 24 30 C 23 20, 40 18, 42 30 C 44 44, 20 46, 16 32 C 12 16, 34 6, 46 14'/%3E%3C/g%3E%3C/svg%3E"); }
.page .d-rune { background-image: url("data:image/svg+xml;utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 60 60'%3E%3Cg fill='none' stroke='%238b2e1a' stroke-width='1.8' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M30 4 L 30 56 M 18 16 C 24 22, 36 22, 42 16 M 22 40 L 30 32 L 38 40 M 24 50 L 36 50'/%3E%3C/g%3E%3C/svg%3E"); }
.page .d-feather { background-image: url("data:image/svg+xml;utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 60 60'%3E%3Cg fill='none' stroke='%238a6a2c' stroke-width='1.8' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M10 52 C 22 40, 36 20, 52 6 C 50 22, 40 40, 14 50 Z'/%3E%3Cpath d='M10 52 L 40 22' stroke-width='1'/%3E%3C/g%3E%3C/svg%3E"); }
.page .d-claws { background-image: url("data:image/svg+xml;utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 60 60'%3E%3Cg fill='none' stroke='%234a3523' stroke-width='1.8' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M14 40 C 12 34, 14 30, 18 30 M 20 42 C 20 36, 22 32, 26 33 M 26 46 C 28 40, 31 37, 34 39'/%3E%3Cpath d='M34 22 C 32 16, 34 12, 38 12 M 40 24 C 40 18, 42 14, 46 15 M 46 28 C 48 22, 51 19, 54 21'/%3E%3C/g%3E%3C/svg%3E"); }
.page .d-moon { background-image: url("data:image/svg+xml;utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 60 60'%3E%3Cg fill='none' stroke='%235b6a8a' stroke-width='1.8' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M38 8 C 22 10, 14 26, 18 38 C 22 50, 40 56, 50 46 C 36 46, 26 36, 28 24 C 30 16, 34 12, 38 8 Z'/%3E%3C/g%3E%3C/svg%3E"); }
.page .e1-hdr .anno { left: 262px; }
.page .e1-st { left: 600px; top: 30px; transform: rotate(9deg); }
.page .e1-log { left: 52px; top: 168px; width: 404px; }
.page .e1-log p { font-size: 18.5px; }
.page .e1-f1 { left: 466px; top: 166px; width: 300px; height: 205px; background-image: url("https://raw.githubusercontent.com/Omegaoliverid/Public-images/main/genesis-notes/forge-egg.jpg"); transform: rotate(0deg); }
.page .e1-f2 { left: 590px; top: 380px; width: 170px; height: 190px; background-image: url("https://raw.githubusercontent.com/Omegaoliverid/Public-images/main/genesis-notes/kaelthos-big.jpg"); transform: rotate(0deg); }
.page .e1-f3 { left: 476px; top: 420px; width: 108px; height: 108px; transform: rotate(-5deg); }
.page .e1-f3::after { content: ''; position: absolute; inset: 6px; background: url("https://raw.githubusercontent.com/Omegaoliverid/Public-images/main/genesis-notes/kaelthos-shell.jpg") center / cover; mix-blend-mode: multiply; }
.page .e1-f4 { left: 604px; top: 590px; width: 150px; height: 200px; transform: rotate(3deg); }
.page .e1-f4::after { content: ''; position: absolute; inset: 6px; background: url("https://raw.githubusercontent.com/Omegaoliverid/Public-images/main/genesis-notes/kaelthos-portrait.jpg") center / cover; mix-blend-mode: multiply; }
.page .e1-f5 { left: 462px; top: 620px; width: 140px; height: 100px; background-image: url("https://raw.githubusercontent.com/Omegaoliverid/Public-images/main/genesis-notes/kaelthos-hatched.jpg"); transform: rotate(0deg); }
.page .e1-f6 { left: 70px; top: 930px; width: 78px; height: 108px; background-image: url("https://raw.githubusercontent.com/Omegaoliverid/Public-images/main/genesis-notes/kaelthos-early.jpg"); transform: rotate(0deg); }
.page .e1-f7 { left: 170px; top: 924px; width: 86px; height: 114px; background-image: url("https://raw.githubusercontent.com/Omegaoliverid/Public-images/main/genesis-notes/kaelthos-mid.jpg"); transform: rotate(0deg); }
.page .e1-tp0 { left: 498px; top: 412px; width: 64px; transform: rotate(-12deg); }
.page .e1-tp1 { left: 645px; top: 580px; width: 64px; transform: rotate(4deg); }
.page .e1-c0 { left: 476px; top: 366px; width: 280px; transform: rotate(-1deg); }
.page .e1-c1 { left: 470px; top: 536px; width: 130px; transform: rotate(-5deg); }
.page .e1-c2 { left: 618px; top: 562px; width: 150px; transform: rotate(0deg); }
.page .e1-c3 { left: 470px; top: 722px; width: 120px; transform: rotate(-2deg); }
.page .e1-c4 { left: 470px; top: 770px; width: 120px; transform: rotate(-2deg); }
.page .e1-c5 { left: 270px; top: 968px; width: 150px; transform: rotate(-3deg); }
.page .e1-d0 { left: 505px; top: 40px; width: 34px; height: 34px; transform: rotate(-8deg); }
.page .e1-d1 { left: 134px; top: 950px; width: 34px; height: 34px; transform: rotate(0deg); }
.page .e1-r0 { left: 300px; top: 930px; }
.page .e1-slip { left: 462px; top: 806px; width: 304px; transform: rotate(-1.4deg); }
.page .e1-slip p { font-size: 18px; line-height: 20px; }
.page .e1-stp { left: 580px; top: 796px; width: 80px; transform: rotate(4deg); }
.page .e1-ft { left: 60px; top: 1088px; width: 360px; }
.page .e2-hdr .anno { left: 398px; }
.page .e2-st { left: 560px; top: 28px; transform: rotate(-7deg); }
.page .e2-log { left: 322px; top: 168px; width: 420px; }
.page .e2-log p { font-size: 17px; }
.page .e2-f1 { left: 28px; top: 166px; width: 276px; height: 220px; background-image: url("https://raw.githubusercontent.com/Omegaoliverid/Public-images/main/genesis-notes/ashes-altar.jpg"); transform: rotate(0deg); }
.page .e2-f2 { left: 28px; top: 410px; width: 280px; height: 100px; background-image: url("https://raw.githubusercontent.com/Omegaoliverid/Public-images/main/genesis-notes/seraphiel-stages.jpg"); transform: rotate(0deg); }
.page .e2-f3 { left: 64px; top: 530px; width: 190px; height: 140px; background-image: url("https://raw.githubusercontent.com/Omegaoliverid/Public-images/main/Genesis-Eggs/final-2026-10-17/seraphiel-study.jpg"); transform: rotate(0deg); }
.page .e2-c0 { left: 28px; top: 388px; width: 270px; transform: rotate(0deg); }
.page .e2-c1 { left: 34px; top: 508px; width: 260px; transform: rotate(0deg); }
.page .e2-c2 { left: 218px; top: 560px; width: 90px; transform: rotate(-4deg); }
.page .e2-d0 { left: 262px; top: 628px; width: 36px; height: 36px; transform: rotate(10deg); }
.page .e2-d1 { left: 520px; top: 40px; width: 24px; height: 24px; transform: rotate(0deg); }
.page .e2-r0 { left: 560px; top: 880px; }
.page .e2-slip { left: 24px; top: 672px; width: 290px; transform: rotate(1.2deg); }
.page .e2-slip p { font-size: 17px; line-height: 19px; }
.page .e2-stp { left: 144px; top: 662px; width: 80px; transform: rotate(-3deg); }
.page .e2-ft { left: 420px; top: 1090px; width: 360px; }
.page .e3-hdr .anno { left: 436px; }
.page .e3-st { left: 590px; top: 26px; transform: rotate(8deg); }
.page .e3-log { left: 52px; top: 168px; width: 420px; }
.page .e3-log p { font-size: 17px; }
.page .e3-f1 { left: 540px; top: 166px; width: 200px; height: 274px; background-image: url("https://raw.githubusercontent.com/Omegaoliverid/Public-images/main/genesis-notes/mirrith-egg.jpg"); transform: rotate(0deg); }
.page .e3-f2 { left: 486px; top: 330px; width: 130px; height: 96px; transform: rotate(-4deg); }
.page .e3-f2::after { content: ''; position: absolute; inset: 6px; background: url("https://raw.githubusercontent.com/Omegaoliverid/Public-images/main/genesis-notes/mirrith-ruin.jpg") center / cover; mix-blend-mode: multiply; }
.page .e3-f3 { left: 486px; top: 448px; width: 160px; height: 86px; background-image: url("https://raw.githubusercontent.com/Omegaoliverid/Public-images/main/genesis-notes/mirrith-approach.jpg"); transform: rotate(0deg); }
.page .e3-f4 { left: 626px; top: 440px; width: 130px; height: 170px; background-image: url("https://raw.githubusercontent.com/Omegaoliverid/Public-images/main/Genesis-Eggs/final-2026-10-17/mirrith-study.jpg"); transform: rotate(0deg); }
.page .e3-tp0 { left: 510px; top: 322px; width: 60px; transform: rotate(-10deg); }
.page .e3-c0 { left: 486px; top: 170px; width: 80px; transform: rotate(-3deg); }
.page .e3-c1 { left: 490px; top: 534px; width: 130px; transform: rotate(-3deg); }
.page .e3-c2 { left: 640px; top: 590px; width: 130px; transform: rotate(0deg); }
.page .e3-d0 { left: 580px; top: 604px; width: 30px; height: 30px; transform: rotate(0deg); }
.page .e3-r0 { left: 90px; top: 960px; }
.page .e3-slip { left: 480px; top: 626px; width: 290px; transform: rotate(-1deg); }
.page .e3-slip p { font-size: 16.5px; line-height: 18.5px; }
.page .e3-stp { left: 580px; top: 616px; width: 80px; transform: rotate(3deg); }
.page .e3-ft { left: 60px; top: 1090px; width: 360px; }
.page .e4-hdr .anno { left: 330px; }
.page .e4-st { left: 570px; top: 28px; transform: rotate(-6deg); }
.page .e4-log { left: 322px; top: 168px; width: 420px; }
.page .e4-log p { font-size: 17px; }
.page .e4-f1 { left: 44px; top: 166px; width: 220px; height: 250px; background-image: url("https://raw.githubusercontent.com/Omegaoliverid/Public-images/main/genesis-notes/somnius-egg.jpg"); transform: rotate(0deg); }
.page .e4-f2 { left: 28px; top: 420px; width: 280px; height: 150px; background-image: url("https://raw.githubusercontent.com/Omegaoliverid/Public-images/main/genesis-notes/somnius-mist.jpg"); transform: rotate(0deg); }
.page .e4-f3 { left: 54px; top: 556px; width: 200px; height: 150px; background-image: url("https://raw.githubusercontent.com/Omegaoliverid/Public-images/main/genesis-notes/somnius-form.jpg"); transform: rotate(0deg); }
.page .e4-c0 { left: 228px; top: 190px; width: 80px; transform: rotate(-4deg); }
.page .e4-c1 { left: 28px; top: 566px; width: 140px; transform: rotate(0deg); }
.page .e4-c2 { left: 44px; top: 690px; width: 190px; transform: rotate(0deg); }
.page .e4-d0 { left: 520px; top: 40px; width: 30px; height: 30px; transform: rotate(0deg); }
.page .e4-d1 { left: 40px; top: 1000px; width: 40px; height: 40px; transform: rotate(0deg); }
.page .e4-r0 { left: 560px; top: 900px; }
.page .e4-slip { left: 24px; top: 728px; width: 290px; transform: rotate(1.2deg); }
.page .e4-slip p { font-size: 17px; line-height: 19px; }
.page .e4-stp { left: 144px; top: 718px; width: 80px; transform: rotate(-3deg); }
.page .e4-ft { left: 420px; top: 1090px; width: 360px; }
.page .e5-hdr .anno { left: 330px; }
.page .e5-st { left: 596px; top: 30px; transform: rotate(8deg); }
.page .e5-log { left: 52px; top: 168px; width: 432px; }
.page .e5-log p { font-size: 16.5px; }
.page .e5-f1 { left: 556px; top: 166px; width: 190px; height: 222px; background-image: url("https://raw.githubusercontent.com/Omegaoliverid/Public-images/main/genesis-notes/vexigar-egg.jpg"); transform: rotate(0deg); }
.page .e5-f2 { left: 486px; top: 300px; width: 130px; height: 64px; transform: rotate(-6deg); }
.page .e5-f2::after { content: ''; position: absolute; inset: 6px; background: url("https://raw.githubusercontent.com/Omegaoliverid/Public-images/main/genesis-notes/vexigar-runes.jpg") center / cover; mix-blend-mode: multiply; }
.page .e5-f3 { left: 492px; top: 384px; width: 86px; height: 80px; transform: rotate(5deg); }
.page .e5-f3::after { content: ''; position: absolute; inset: 6px; background: url("https://raw.githubusercontent.com/Omegaoliverid/Public-images/main/genesis-notes/contract-seal.jpg") center / cover; mix-blend-mode: multiply; }
.page .e5-f4 { left: 536px; top: 400px; width: 220px; height: 232px; background-image: url("https://raw.githubusercontent.com/Omegaoliverid/Public-images/main/genesis-notes/vexigar-hatchling.jpg"); transform: rotate(0deg); }
.page .e5-tp0 { left: 516px; top: 292px; width: 56px; transform: rotate(-10deg); }
.page .e5-tp1 { left: 506px; top: 376px; width: 46px; transform: rotate(12deg); }
.page .e5-c0 { left: 486px; top: 186px; width: 80px; transform: rotate(-3deg); }
.page .e5-c1 { left: 492px; top: 470px; width: 80px; transform: rotate(4deg); }
.page .e5-c2 { left: 560px; top: 628px; width: 200px; transform: rotate(0deg); }
.page .e5-d0 { left: 520px; top: 40px; width: 26px; height: 26px; transform: rotate(-10deg); }
.page .e5-d1 { left: 494px; top: 520px; width: 36px; height: 36px; transform: rotate(20deg); }
.page .e5-r0 { left: 90px; top: 980px; }
.page .e5-slip { left: 480px; top: 680px; width: 290px; transform: rotate(-1.2deg); }
.page .e5-slip p { font-size: 16.5px; line-height: 18.5px; }
.page .e5-stp { left: 580px; top: 670px; width: 80px; transform: rotate(3deg); }
.page .e5-ft { left: 420px; top: 1092px; width: 360px; }
.page .e6-hdr .anno { left: 424px; }
.page .e6-st { left: 586px; top: 28px; transform: rotate(-8deg); }
.page .e6-log { left: 306px; top: 168px; width: 436px; }
.page .e6-log p { font-size: 16px; }
.page .e6-f1 { left: 44px; top: 166px; width: 130px; height: 214px; background-image: url("https://raw.githubusercontent.com/Omegaoliverid/Public-images/main/genesis-notes/chronis-egg.jpg"); transform: rotate(0deg); }
.page .e6-f2 { left: 160px; top: 180px; width: 140px; height: 170px; background-image: url("https://raw.githubusercontent.com/Omegaoliverid/Public-images/main/genesis-notes/chronis-bird.jpg"); transform: rotate(0deg); }
.page .e6-f3 { left: 28px; top: 392px; width: 276px; height: 82px; background-image: url("https://raw.githubusercontent.com/Omegaoliverid/Public-images/main/genesis-notes/chronis-stages.jpg"); transform: rotate(0deg); }
.page .e6-f4 { left: 194px; top: 320px; width: 100px; height: 70px; transform: rotate(-5deg); }
.page .e6-f4::after { content: ''; position: absolute; inset: 6px; background: url("https://raw.githubusercontent.com/Omegaoliverid/Public-images/main/genesis-notes/chronis-surface.jpg") center / cover; mix-blend-mode: multiply; }
.page .e6-tp0 { left: 224px; top: 312px; width: 50px; transform: rotate(-12deg); }
.page .e6-c0 { left: 42px; top: 378px; width: 120px; transform: rotate(-2deg); }
.page .e6-c1 { left: 34px; top: 474px; width: 260px; transform: rotate(0deg); }
.page .e6-c2 { left: 178px; top: 170px; width: 120px; transform: rotate(-3deg); }
.page .e6-d0 { left: 520px; top: 36px; width: 36px; height: 36px; transform: rotate(0deg); }
.page .e6-d1 { left: 230px; top: 1000px; width: 34px; height: 34px; transform: rotate(0deg); }
.page .e6-r0 { left: 90px; top: 940px; }
.page .e6-slip { left: 24px; top: 512px; width: 280px; transform: rotate(1deg); }
.page .e6-slip p { font-size: 16.5px; line-height: 18.5px; }
.page .e6-stp { left: 144px; top: 502px; width: 80px; transform: rotate(-3deg); }
.page .e6-ft { left: 60px; top: 1090px; width: 360px; }

.page.diary { padding: 62px 60px 66px 76px; background-color: #e9d8b4; }
.page.diary::before { content: ''; position: absolute; left: 58px; top: 0; bottom: 0; width: 3px; border-left: 1px solid rgba(139,46,26,0.28); border-right: 1px solid rgba(139,46,26,0.18); }
.page.diary .columnWrapper { column-count: 1; }
.page.diary p { font-size: 18px; line-height: 1.16em; margin: 0 0 3px; }
.page.diary .ent { margin-bottom: 10px; }
.page.diary .dh { font-family: 'Caveat', cursive; font-weight: 700; font-size: 25px; line-height: 1.1em; margin: 12px 0 4px; padding-left: 30px; position: relative; }
.page.diary .dh p { font-size: inherit; font-weight: inherit; margin: 0; line-height: inherit; }
.page.diary .dh::before { content: ''; position: absolute; left: 0; top: 2px; width: 24px; height: 24px; background-size: contain; background-repeat: no-repeat; opacity: 0.85; }
.page.diary .dh .mo { font-family: 'IM Fell English SC', serif; font-weight: 400; font-size: 15px; letter-spacing: 0.12em; opacity: 0.8; margin-right: 6px; }
.page.diary .iA { color: #2a1d14; } .page.diary .iA .dh { color: #4a1a0e; }
.page.diary .iB { color: #241a14; } .page.diary .iB p { font-size: 18.6px; letter-spacing: 0.1px; } .page.diary .iB .dh { color: #3b1a12; }
.page.diary .iC { color: #33261a; } .page.diary .iC .dh { color: #6b4a1a; }
.page.diary .iD { color: #241c2c; } .page.diary .iD .dh { color: #3d2752; }
.page.diary .iE { color: #1f2a38; } .page.diary .iE .dh { color: #2b4062; }
.page.diary .iF { color: #2e1a16; } .page.diary .iF .dh { color: #7a2414; }
.page.diary .iG { color: #1c2a26; } .page.diary .iG .dh { color: #6b5320; }
.page.diary .iA .dh::before { background-image: url("data:image/svg+xml;utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 60 60'%3E%3Cg fill='none' stroke='%23a3401c' stroke-width='1.8' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M30 56 C 14 56, 12 40, 20 30 C 22 38, 26 38, 26 34 C 24 24, 30 14, 36 6 C 36 18, 50 26, 46 42 C 44 52, 38 56, 30 56 Z'/%3E%3C/g%3E%3C/svg%3E"); }
.page.diary .iB .dh::before { background-image: url("data:image/svg+xml;utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 60 60'%3E%3Cg fill='none' stroke='%234a3523' stroke-width='1.8' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M30 6 C 14 6, 8 30, 10 40 C 12 52, 22 56, 30 56 C 38 56, 48 52, 50 40 C 52 30, 46 6, 30 6 Z'/%3E%3Cpath d='M22 24 L 28 30 L 24 36 M 34 18 L 38 26' stroke-width='1.2'/%3E%3C/g%3E%3C/svg%3E"); }
.page.diary .iC .dh::before { background-image: url("data:image/svg+xml;utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 60 60'%3E%3Cg fill='none' stroke='%238a6a2c' stroke-width='1.8' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M10 52 C 22 40, 36 20, 52 6 C 50 22, 40 40, 14 50 Z'/%3E%3Cpath d='M10 52 L 40 22' stroke-width='1'/%3E%3C/g%3E%3C/svg%3E"); }
.page.diary .iD .dh::before { background-image: url("data:image/svg+xml;utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 60 60'%3E%3Cg fill='none' stroke='%234a3523' stroke-width='1.8' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M4 30 C 18 12, 42 12, 56 30 C 42 48, 18 48, 4 30 Z'/%3E%3Ccircle cx='30' cy='30' r='8'/%3E%3Ccircle cx='30' cy='30' r='2.5' fill='%234a3523'/%3E%3C/g%3E%3C/svg%3E"); }
.page.diary .iE .dh::before { background-image: url("data:image/svg+xml;utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 60 60'%3E%3Cg fill='none' stroke='%235b6a8a' stroke-width='1.8' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M38 8 C 22 10, 14 26, 18 38 C 22 50, 40 56, 50 46 C 36 46, 26 36, 28 24 C 30 16, 34 12, 38 8 Z'/%3E%3C/g%3E%3C/svg%3E"); }
.page.diary .iF .dh::before { background-image: url("data:image/svg+xml;utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 60 60'%3E%3Cg fill='none' stroke='%238b2e1a' stroke-width='1.8' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M30 4 L 30 56 M 18 16 C 24 22, 36 22, 42 16 M 22 40 L 30 32 L 38 40 M 24 50 L 36 50'/%3E%3C/g%3E%3C/svg%3E"); }
.page.diary .iG .dh::before { background-image: url("data:image/svg+xml;utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 60 60'%3E%3Cg fill='none' stroke='%234a3523' stroke-width='1.8' stroke-linecap='round' stroke-linejoin='round'%3E%3Ccircle cx='30' cy='30' r='24'/%3E%3Ccircle cx='30' cy='30' r='20' stroke-width='0.8'/%3E%3Cpath d='M30 30 L 30 14 M 30 30 L 41 36'/%3E%3Cpath d='M30 8 L30 11 M52 30 L49 30 M30 52 L30 49 M8 30 L11 30' stroke-width='1.2'/%3E%3C/g%3E%3C/svg%3E"); }
.page.diary .fig { position: relative; margin: 4px 0 6px 0; mix-blend-mode: multiply; background-size: cover; background-position: center; }
.page.diary .fig.r { float: right; margin-left: 16px; }
.page.diary .fig.l { float: left; margin-right: 16px; }
.page.diary .fig.sk { -webkit-mask-image: radial-gradient(closest-side, #000 70%, transparent 100%); mask-image: radial-gradient(closest-side, #000 70%, transparent 100%); }
.page.diary .fig.soft { -webkit-mask-image: radial-gradient(farthest-side, #000 76%, transparent 100%); mask-image: radial-gradient(farthest-side, #000 76%, transparent 100%); }
.page.diary .fig.photo { mix-blend-mode: normal; border: 6px solid #f1e6cc; box-shadow: 1px 2px 5px rgba(60,35,10,0.35); }
.page.diary .fig.photo::before { content: ''; position: absolute; left: 50%; top: -9px; width: 64px; height: 18px; margin-left: -32px; background: rgba(236,226,190,0.8); box-shadow: 0 1px 2px rgba(0,0,0,0.15); transform: rotate(-4deg); }
.page.diary .yr { text-align: center; margin: 6px 0 14px; }
.page.diary .yr h1 { font-family: 'Caveat', cursive; font-weight: 700; font-size: 54px; color: #22160e; margin: 0; border: none; line-height: 1em; }
.page.diary .yr p { font-family: 'IM Fell English SC', serif; font-size: 16px; letter-spacing: 0.18em; color: #6b5233; margin: 2px 0 0; }
.page.diary .yr::after { content: ''; display: block; height: 12px; margin: 8px auto 0; width: 300px; background: url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='300' height='12' viewBox='0 0 300 12'><path d='M2 8 C 60 2, 120 11, 180 6 S 270 3, 298 7' stroke='%237a2a17' stroke-width='2.2' fill='none' stroke-linecap='round'/></svg>") no-repeat center / 300px 12px; }
.page.diary .rh { position: absolute; left: 76px; right: 60px; top: 26px; display: flex; justify-content: space-between; font-family: 'IM Fell English SC', serif; font-size: 12px; letter-spacing: 0.2em; color: #7a6040; }
.page.diary .rh p { font-family: inherit; font-size: inherit; color: inherit; margin: 0; letter-spacing: inherit; }
.page.diary .pn { position: absolute; left: 0; right: 0; bottom: 26px; text-align: center; font-family: 'Caveat', cursive; font-size: 18px; color: #6b5233; }
.page.diary .pn p { font-size: inherit; color: inherit; margin: 0; }
.page.diary .sig { text-align: right; margin-top: 16px; clear: both; }
.page.diary .sig p { font-size: 26px; font-weight: 700; color: #22160e; margin: 0; }
.page.diary .sig p + p { font-family: 'IM Fell English SC', serif; font-weight: 400; font-size: 14px; letter-spacing: 0.15em; color: #6b5233; }
.page.diary .tp { text-align: center; padding-top: 150px; }
.page.diary .tp h1 { font-family: 'Caveat', cursive; font-weight: 700; font-size: 68px; line-height: 1.05em; color: #22160e; margin: 0; border: none; }
.page.diary .tp p { font-family: 'IM Fell English SC', serif; font-size: 17px; letter-spacing: 0.2em; color: #6b5233; margin: 8px 0 0; }
.page.diary .tp .by { font-family: 'Caveat', cursive; font-size: 26px; letter-spacing: 0; color: #2a1d14; margin-top: 40px; }
.page.diary .tpfig { margin: 46px auto 0; width: 420px; height: 300px; background: url("https://raw.githubusercontent.com/Omegaoliverid/Public-images/main/genesis-notes/forge-egg.jpg") center / cover; mix-blend-mode: multiply;
  -webkit-mask-image: radial-gradient(farthest-side, #000 70%, transparent 100%); mask-image: radial-gradient(farthest-side, #000 70%, transparent 100%); }
.page.diary .tpnote { position: absolute; left: 110px; right: 110px; bottom: 120px; text-align: center; }
.page.diary .tpnote p { font-family: 'Reenie Beanie', cursive; font-size: 24px; color: #8b2e1a; transform: rotate(-1.5deg); }
.page.diary .blot { position: absolute; }

.page.diary .dfig0 { width: 118px; height: 166px; background-image: url("https://raw.githubusercontent.com/Omegaoliverid/Public-images/main/Genesis-Eggs/final-2026-10-17/plain-egg.jpg"); transform: rotate(0deg); }
.page.diary .dfig1 { width: 110px; height: 142px; background-image: url("https://raw.githubusercontent.com/Omegaoliverid/Public-images/main/genesis-notes/kaelthos-mid.jpg"); transform: rotate(0deg); }
.page.diary .dfig2 { width: 150px; height: 168px; background-image: url("https://raw.githubusercontent.com/Omegaoliverid/Public-images/main/genesis-notes/kaelthos-big.jpg"); transform: rotate(0deg); }
.page.diary .dfig3 { width: 165px; height: 220px; background-image: url("https://raw.githubusercontent.com/Omegaoliverid/Public-images/main/genesis-notes/kaelthos-portrait.jpg"); transform: rotate(-3deg); }
.page.diary .dfig4 { width: 230px; height: 164px; background-image: url("https://raw.githubusercontent.com/Omegaoliverid/Public-images/main/genesis-notes/kaelthos-drake.jpg"); transform: rotate(0deg); }
.page.diary .dfig6 { width: 210px; height: 116px; background-image: url("https://raw.githubusercontent.com/Omegaoliverid/Public-images/main/genesis-notes/kaelthos-hatched.jpg"); transform: rotate(0deg); }
.page.diary .dfig7 { width: 150px; height: 190px; background-image: url("https://raw.githubusercontent.com/Omegaoliverid/Public-images/main/genesis-notes/seraphiel-crystal.jpg"); transform: rotate(0deg); }
.page.diary .dfig8 { width: 180px; height: 176px; background-image: url("https://raw.githubusercontent.com/Omegaoliverid/Public-images/main/genesis-notes/ashes-altar.jpg"); transform: rotate(0deg); }
.page.diary .dfig9 { width: 170px; height: 188px; background-image: url("https://raw.githubusercontent.com/Omegaoliverid/Public-images/main/genesis-notes/seraphiel-hatch.jpg"); transform: rotate(0deg); }
.page.diary .dfig10 { width: 200px; height: 232px; background-image: url("https://raw.githubusercontent.com/Omegaoliverid/Public-images/main/Genesis-Eggs/final-2026-10-17/seraphiel-study.jpg"); transform: rotate(0deg); }
.page.diary .dfig11 { width: 110px; height: 150px; background-image: url("https://raw.githubusercontent.com/Omegaoliverid/Public-images/main/genesis-notes/seraphiel-head.jpg"); transform: rotate(4deg); }
.page.diary .dfig12 { width: 150px; height: 206px; background-image: url("https://raw.githubusercontent.com/Omegaoliverid/Public-images/main/genesis-notes/mirrith-egg.jpg"); transform: rotate(0deg); }
.page.diary .dfig13 { width: 190px; height: 134px; background-image: url("https://raw.githubusercontent.com/Omegaoliverid/Public-images/main/genesis-notes/mirrith-eye.jpg"); transform: rotate(0deg); }
.page.diary .dfig14 { width: 170px; height: 224px; background-image: url("https://raw.githubusercontent.com/Omegaoliverid/Public-images/main/Genesis-Eggs/final-2026-10-17/mirrith-study.jpg"); transform: rotate(0deg); }
.page.diary .dfig15 { width: 250px; height: 92px; background-image: url("https://raw.githubusercontent.com/Omegaoliverid/Public-images/main/Genesis-Eggs/final-2026-10-17/temple-ward.jpg"); transform: rotate(0deg); }
.page.diary .dfig16 { width: 250px; height: 186px; background-image: url("https://raw.githubusercontent.com/Omegaoliverid/Public-images/main/genesis-notes/mirrith-ruin.jpg"); transform: rotate(-3deg); }
.page.diary .dfig17 { width: 240px; height: 116px; background-image: url("https://raw.githubusercontent.com/Omegaoliverid/Public-images/main/genesis-notes/somnius-nest.jpg"); transform: rotate(0deg); }
.page.diary .dfig18 { width: 160px; height: 186px; background-image: url("https://raw.githubusercontent.com/Omegaoliverid/Public-images/main/genesis-notes/somnius-egg.jpg"); transform: rotate(0deg); }
.page.diary .dfig19 { width: 250px; height: 170px; background-image: url("https://raw.githubusercontent.com/Omegaoliverid/Public-images/main/genesis-notes/somnius-mist.jpg"); transform: rotate(0deg); }
.page.diary .dfig20 { width: 200px; height: 200px; background-image: url("https://raw.githubusercontent.com/Omegaoliverid/Public-images/main/genesis-notes/somnius-form.jpg"); transform: rotate(0deg); }
.page.diary .dfig21 { width: 190px; height: 126px; background-image: url("https://raw.githubusercontent.com/Omegaoliverid/Public-images/main/Genesis-Eggs/final-2026-10-17/dream-visit.jpg"); transform: rotate(0deg); }
.page.diary .dfig22 { width: 250px; height: 76px; background-image: url("https://raw.githubusercontent.com/Omegaoliverid/Public-images/main/genesis-notes/infernal-glyphs.jpg"); transform: rotate(-2deg); }
.page.diary .dfig23 { width: 150px; height: 176px; background-image: url("https://raw.githubusercontent.com/Omegaoliverid/Public-images/main/genesis-notes/vexigar-egg.jpg"); transform: rotate(0deg); }
.page.diary .dfig24 { width: 200px; height: 212px; background-image: url("https://raw.githubusercontent.com/Omegaoliverid/Public-images/main/genesis-notes/vexigar-hatchling.jpg"); transform: rotate(0deg); }
.page.diary .dfig25 { width: 270px; height: 74px; background-image: url("https://raw.githubusercontent.com/Omegaoliverid/Public-images/main/genesis-notes/vexigar-play.jpg"); transform: rotate(0deg); }
.page.diary .dfig26 { width: 150px; height: 200px; background-image: url("https://raw.githubusercontent.com/Omegaoliverid/Public-images/main/genesis-notes/contract-scroll.jpg"); transform: rotate(3deg); }
.page.diary .dfig28 { width: 130px; height: 212px; background-image: url("https://raw.githubusercontent.com/Omegaoliverid/Public-images/main/genesis-notes/chronis-egg.jpg"); transform: rotate(0deg); }
.page.diary .dfig29 { width: 240px; height: 98px; background-image: url("https://raw.githubusercontent.com/Omegaoliverid/Public-images/main/genesis-notes/chronis-layers.jpg"); transform: rotate(0deg); }
.page.diary .dfig30 { width: 250px; height: 82px; background-image: url("https://raw.githubusercontent.com/Omegaoliverid/Public-images/main/genesis-notes/chronis-stages.jpg"); transform: rotate(0deg); }
.page.diary .dfig31 { width: 170px; height: 186px; background-image: url("https://raw.githubusercontent.com/Omegaoliverid/Public-images/main/genesis-notes/chronis-bird.jpg"); transform: rotate(0deg); }
.page.diary .dfig32 { width: 210px; height: 124px; background-image: url("https://raw.githubusercontent.com/Omegaoliverid/Public-images/main/genesis-notes/vexigar-side.jpg"); transform: rotate(0deg); }
.page.diary .dfig33 { width: 160px; height: 116px; background-image: url("https://raw.githubusercontent.com/Omegaoliverid/Public-images/main/Genesis-Eggs/final-2026-10-17/temple-healing.jpg"); transform: rotate(-4deg); }
.page.diary .dfig34 { width: 110px; height: 146px; background-image: url("https://raw.githubusercontent.com/Omegaoliverid/Public-images/main/Genesis-Eggs/final-2026-10-17/kaelthos-memory.jpg"); transform: rotate(0deg); }
.page.diary .dfig35 { width: 300px; height: 232px; background-image: url("https://raw.githubusercontent.com/Omegaoliverid/Public-images/main/genesis-notes/archive-chest.jpg"); transform: rotate(2deg); }

.page.diary .ent, .page.diary .tp, .page.diary .tpfig, .page.diary .yr, .page.diary .sig, .page.diary .dh { display: block; }
.page.diary .rh { width: 658px; right: auto; }
.page.diary .pn { width: 794px; right: auto; }
.page.diary .tpnote { width: 574px; right: auto; }
.page.diary .ent.cont > p:first-child { margin-top: 0; }
.page.diary .dd { position: absolute; width: 38px; height: 38px; background-size: contain; background-repeat: no-repeat; opacity: 0.75; }
.page.diary .dd p { display: none; }
.page.diary .ring p, .page.diary .blot p { display: none; }
.page.diary .fig p { display: none; }
.page.diary .tpfig p { display: none; }
.page.diary .efig { position: absolute; background-size: cover; background-position: center; mix-blend-mode: multiply; -webkit-mask-image: radial-gradient(farthest-side, #000 72%, transparent 100%); mask-image: radial-gradient(farthest-side, #000 72%, transparent 100%); }
.page.diary .efig p { display: none; }
.page.diary .ecap { position: absolute; text-align: center; }
.page.diary .ecap p { font-family: 'Reenie Beanie', cursive; font-size: 22px; color: #5a4030; margin: 0; }
.page.diary .tp .yrs { font-family: 'Caveat', cursive; font-size: 26px; letter-spacing: 0; color: #2a1d14; margin-top: 30px; }

.page.diary .tpr { left: 520px; top: 80px; }
.page.diary .dp2x0 { left: 560px; top: 860px; }
.page.diary .dp3x0 { left: 742px; top: 300px; }
.page.diary .dp3x1 { left: 742px; top: 700px; }
.page.diary .dp5x0 { left: 690px; top: 1040px; }
.page.diary .dp8x0 { left: 40px; top: 120px; }
.page.diary .dp9x0 { left: 378px; top: 990px; }
.page.diary .dp10x0 { left: 640px; top: 1010px; }
.page.diary .epf10 { left: 177px; top: 790px; width: 440px; height: 196px; background-image: url("https://raw.githubusercontent.com/Omegaoliverid/Public-images/main/Genesis-Eggs/final-2026-10-17/egg-position-study.jpg"); transform: rotate(-1.5deg); }
.page.diary .epc10 { left: 177px; top: 990px; width: 440px; }
.page.diary .dp11x0 { left: 742px; top: 120px; }
.page.diary .dp14x0 { left: 600px; top: 40px; }
.page.diary .dp17x0 { left: 120px; top: 1046px; }
.page.diary .dp20x0 { left: 520px; top: 900px; }
.page.diary .dp24x0 { left: 742px; top: 90px; }
.page.diary .dp24x1 { left: 742px; top: 520px; }
.page.diary .dp24x2 { left: 80px; top: 880px; }

.page.rn .hdr .anno { left: 380px; top: 108px; font-size: 22px; }
/* Restored-art placement corrections: keep silhouettes and captions clear. */
.page.rn .sk, .page.diary .fig.sk, .page.diary .efig { background-size: contain; background-repeat: no-repeat; -webkit-mask-image: radial-gradient(farthest-side, #000 88%, transparent 100%); mask-image: radial-gradient(farthest-side, #000 88%, transparent 100%); }
.page.rn .e1-f6 { top: 974px; height: 88px; }
.page.rn .e1-f7 { top: 970px; height: 94px; }
.page.rn .e1-d1 { top: 992px; }
.page.rn .e1-c5 { top: 1000px; }
.page.rn .e2-f2 { top: 430px; height: 82px; }
.page.rn .e2-c1 { top: 516px; }
.page.rn .e2-f3 { left: 34px; top: 552px; width: 170px; height: 126px; }
.page.rn .e2-c2 { left: 212px; top: 558px; width: 94px; }
.page.rn .e4-f2 { height: 125px; }
.page.rn .e4-c1 { top: 550px; width: 270px; }
.page.rn .e4-f3 { top: 594px; height: 100px; }
.page.rn .e4-c2 { top: 698px; }
.page.rn .e6-f1 { height: 185px; }
.page.rn .e6-c0 { top: 356px; }
.page.rn .e6-f2 { left: 180px; top: 210px; width: 112px; height: 105px; }
</style>

{{blk,ring,e1-r0
}}

{{blk,hdr,e1-hdr
{{ledger HATCHERY LEDGER · SPECIMEN FILE}}
# Egg No. 01
**Initial Classification:** Unknown

{{anno Kaelthos — Obsidian Drake}}

**Alignment:** Fire &nbsp;|&nbsp; **Origin:** College donation
}}

{{blk,stamp,e1-st
FILE CLOSED

234 · IGNISAUR
}}

{{blk,e1-log
{{ink1
{{date Year 234 · Aethelwain — Initial Observation}}

Grey, smooth-shelled specimen. No detectable activity. Donor unable to establish origin. Stored beside laboratory forge pending examination.

{{date Year 234 · Aethelwain — Activation}}

Shell darkening; fine orange fractures developing. Accidental contact caused immediate magical depletion and exhaustion. Forge proximity suspected as elemental influence.

{{date Year 234 · Vaelor — Nurturing}}

Additional heat produced little observable change. Direct magical offerings prompted movement and increased luminosity. Each expenditure required recovery.

Shell responds more strongly to my voice than to ordinary background noise. Repeated descriptions of a draconic form coincide with movement. Cause uncertain.

{{date Year 234 · Vaelor — Hatching}}

Final energy expenditure occurred unexpectedly upon contact. Small obsidian drake emerged. Immediate recognition demonstrated. Designated *Kaelthos*.

Subject appears curious and responsive. Initial behaviour suggests a favourable attachment to researcher.

{{date Year 234 · Sylphren — Development}}

Subject prefers the forge but remains active and healthy during outdoor excursions. Flame emission observed when startled. Increasing independence and protective behaviour.

*Hypothesis: External heat may be necessary for sustained health.* {{anno wrong — see Ignisaur}}

{{date Year 234 · Ignisaur — Correction}}

Subject died following severe injuries sustained defending me against an aquatic creature during coastal reagent collection.

~~External heat essential for survival.~~

**Revised:** No evidence of thermal dependency. Preference mistaken for necessity. Fatality attributable to traumatic injury.

}}
}}

{{sk,soft,e1-f1
}}

{{sk,e1-f2
}}

{{blk,photo,e1-f3
&nbsp;
}}

{{blk,photo,e1-f4
&nbsp;
}}

{{sk,soft,e1-f5
}}

{{sk,e1-f6
}}

{{sk,e1-f7
}}

{{blk,tape,e1-tp0
}}

{{blk,tape,e1-tp1
}}

{{blk,cap,e1-c0
Fig. 1 — Aethelwain. Grey, smooth; left beside the forge.
}}

{{blk,cap,e1-c1
Fig. 2 — shell detail. Contact drains magic.
}}

{{blk,cap,e1-c2
Fig. 3 — Vaelor. Brighter after each offering.
}}

{{blk,cap,e1-c3
Fig. 4 — what remained of the shell.
}}

{{blk,cap,e1-c4
Fig. 5 — Kaelthos.
}}

{{blk,cap,e1-c5
Fig. 6 — grey, then fractured; within the month.
}}

{{blk,doodle,d-flame,e1-d0
}}

{{blk,doodle,d-arrow,e1-d1
}}

{{blk,slip,e1-slip
{{date Year 235 · Zenithar — Retrospective Note}}

Five subsequent specimens have strengthened my belief that personality cannot be adequately predicted from alignment alone.

Kaelthos's protective behaviour was neither taught nor requested.

My first records contain extensive observations of his temperature and almost nothing of his affection.

*An omission I continue to regret.*

}}

{{blk,tape,e1-stp
}}

{{blk,foot,e1-ft
FOLIO 1 · EGG No. 01 · FIRE
}}

\page {rn,fp23}

{{blk,ring,e2-r0
}}

{{blk,hdr,e2-hdr
{{ledger HATCHERY LEDGER · SPECIMEN FILE}}
# Egg No. 02
**Initial Classification:** Unknown — Temple Reliquary

{{anno Seraphiel — The Ashen Saint}}

**Alignment:** Celestial &nbsp;|&nbsp; **Origin:** Temple custodians
}}

{{blk,stamp,e2-st
RESIDENT

TEMPLE INFIRMARY
}}

{{blk,e2-log
{{ink1
{{date Year 234 · Zunith — Initial Observation}}

Pale shell displaying faint internal radiance. Preserved within temple reliquary for an unknown period.

Experiment established in consecrated surroundings. Subject exposed to celestial blessings, personal magical offerings and ashes retained from Egg No. 01.

{{date Year 234 · Zunith — Incubation}}

Golden luminosity increases following offerings. Researcher experiences substantial fatigue; temple blessings do not appear to reduce the personal cost.

Shell remains warm but not dangerously hot.

*Question: Is alignment determined by celestial energy, devotional intention, or their combined influence?*

{{date Year 234 · Verdantis — Hatching}}

Final magical offering completed. Shell dissolved into luminous fragments. Winged, partially radiant organism emerged.

Designated *Seraphiel*. Immediate connection established.

{{date Year 234 · Borealis — Behavioural Observation}}

Subject repeatedly seeks the temple infirmary. Demonstrates apparent restorative abilities and interest in purification.

During examination, subject approached a basin of contaminated water before any visible reaction occurred.

*Possible sensitivity to impurities. Requires confirmation.* {{anno confirmed — temple letters, 235}}

Little interest shown in conventional arcane demonstrations. Strong preference for temple activities.

{{date Year 234 · Kaelum — Separation}}

Subject elected to remain with temple inhabitants. No command to follow issued.

Original magical connection remains perceptible.

*Hypothesis: Prolonged separation may eventually diminish the bond.* {{anno not so — see Obsidian}}

{{date Year 234 · Obsidian — Revision}}

Returned to temple during investigation of Egg No. 03. Immediate recognition by Seraphiel. Magical connection unchanged to my perception.

~~Separation necessarily weakens the bond.~~

Insufficient evidence.

}}
}}

{{sk,soft,e2-f1
}}

{{sk,e2-f2
}}

{{sk,soft,e2-f3
}}

{{blk,cap,e2-c0
Fig. 1 — reliquary egg; Kaelthos's ashes about its base.
}}

{{blk,cap,e2-c1
Fig. 2 — the glow strengthens with each offering.
}}

{{blk,cap,e2-c2
Fig. 3 — Seraphiel, Borealis. Prefers the infirmary.
}}

{{blk,doodle,d-feather,e2-d0
}}

{{blk,doodle,d-star,e2-d1
}}

{{blk,slip,e2-slip
{{date Year 235 · Ignisaur — Correspondence}}

Temple reports continued healing and purification activities. No observed deterioration during prolonged absence.

{{date Year 235 · Zenithar — Further Examination}}

Subject thriving independently. Original connection remains, despite no deliberate release having occurred.

Brief interference perceived while accompanying Egg No. 06. Neither creature exhibited distress.

**Revised conclusion:** Independence does not necessarily terminate a Genesis connection. Whether such persistence complicates subsequent bonding remains unresolved.

*Seraphiel appears to have discovered a calling without requiring my guidance.*

}}

{{blk,tape,e2-stp
}}

{{blk,foot,e2-ft
FOLIO 2 · EGG No. 02 · CELESTIAL
}}

\page {rn,fp24}

{{blk,ring,e3-r0
}}

{{blk,hdr,e3-hdr
{{ledger HATCHERY LEDGER · SPECIMEN FILE}}
# Egg No. 03
**Initial Classification:** Unknown — Provenance Unverified

{{anno Mirrith — The Hollow Reflection}}

**Alignment:** Eldritch (provisional)
}}

{{blk,stamp,e3-st
CONTAINED

PROVISIONALLY
}}

{{blk,e3-log
{{ink1
{{date Year 234 · Umbral — Initial Observation}}

Unidentified egg discovered among recently acquired eldritch manuscripts. No corresponding purchase record.

I have no recollection of its acquisition.

{{date Year 234 · Umbral — Observation I}}

Shell appears black under direct light. Reflections inconsistent with surrounding objects.

My reflected expression changed independently of my own. No witness present.

{{date Year 234 · Umbral — Observation II}}

Specimen discovered outside protective circle. No disturbance to surrounding inscriptions.

Position recorded before retiring. Position different upon return.

Movement not witnessed.

{{date Year 234 · Umbral — Observation III}}

Repeated exhaustion despite no voluntary magical offering.

Apparent development continues.

*Hypothesis: Energy extraction occurring without consent.*

Cannot determine whether expenditure is physical, magical or perceptual.

{{date Year 234 · Obsidian — Observation IV}}

Existing connection with Egg No. 02 intermittently obscured by unfamiliar sensation.

Protective enchantments produce inconsistent results.

A mirror positioned opposite the specimen displayed a reflection of the laboratory with one additional doorway.

The doorway does not exist.

{{date Year 234 · Obsidian — Hatching}}

Egg absent upon entering laboratory. Entity occupying former position. No shell fragments recovered.

Appearance unstable; familiar faces intermittently visible.

Name *Mirrith* recognised without recollection of naming.

{{date Year 234 · Zenithar — Containment}}

Warded mirror chamber constructed with temple assistance. Manifestations substantially diminished.

*Provisional conclusion: Containment successful.* {{anno premature — see 235}}

}}
}}

{{sk,soft,e3-f1
}}

{{blk,photo,e3-f2
&nbsp;
}}

{{sk,e3-f3
}}

{{sk,soft,e3-f4
}}

{{blk,tape,e3-tp0
}}

{{blk,cap,e3-c0
Fig. 1 — black, or a mirror. Never the right reflection.
}}

{{blk,cap,e3-c1
Fig. 2 — glimpsed in the shell. A place I do not know.
}}

{{blk,cap,e3-c2
Fig. 3 — Mirrith. The shape will not hold.
}}

{{blk,doodle,d-eye,e3-d0
}}

{{blk,slip,e3-slip
{{date Year 235 · Aethelwain — Additional Observation}}

Disturbing dreams persist. Mental wards reinforced. Possible residual influence upon subsequent experimental conditions.

{{date Year 235 · Sylphren — Revision}}

Dream wards appear to prevent further encounters.

~~Containment confirmed.~~

Correction: Absence of perception does not establish absence of influence.

{{date Year 235 · Zenithar — Final Inspection}}

Chamber seals intact. No confirmed physical escape.

Occasional reflective anomalies continue.

*I observed my reflection turn away before I did.*

No independent corroboration.

**Status: Contained, provisionally.**

Further direct experimentation inadvisable.

}}

{{blk,tape,e3-stp
}}

{{blk,foot,e3-ft
FOLIO 3 · EGG No. 03 · ELDRITCH (PROVISIONAL)
}}

\page {rn,fp25}

{{blk,ring,e4-r0
}}

{{blk,hdr,e4-hdr
{{ledger HATCHERY LEDGER · SPECIMEN FILE}}
# Egg No. 04
**Initial Classification:** Unaligned

{{anno Somnius — The Veilborn}}

**Alignment:** Dream &nbsp;|&nbsp; **Origin:** Academic correspondence
}}

{{blk,stamp,e4-st
WHEREABOUTS

UNDETERMINED
}}

{{blk,e4-log
{{ink1
{{date Year 235 · Aethelwain — Initial Observation}}

Unaligned egg acquired through verified correspondence. Introduced into laboratory protected by mental and dream-related wards established following Egg No. 03.

Shell developed opalescent characteristics before deliberate aspect infusion.

*Possible unintended exposure to protective enchantments.*

{{date Year 235 · Aethelwain — Perceptual Examination}}

Shell appears to change shape when observation is interrupted.

Two consecutive sketches disagree despite no apparent physical movement.

Unable to determine whether specimen changes or my memory of it does.

{{date Year 235 · Vaelor — Magical Nurturing}}

Offering produced immediate exhaustion and apparent alteration of laboratory dimensions.

Upon recovery, protective inscriptions appeared subtly changed.

Independent examination confirmed inconsistencies in several inscriptions but could not establish their cause.

*Hypothesis: The specimen may influence perception, memory or physical surroundings.*

{{date Year 235 · Vaelor — Additional Observation}}

Dreams increasingly feature unfamiliar locations. Specimen responds to spoken descriptions of these places with internal movement.

Some experimental notes appear unfamiliar in my own handwriting.

All future observations to be recorded immediately.

{{date Year 235 · Sylphren — Hatching}}

Hatching witnessed during sleep. Mist-like organism emerged within apparent dream environment.

Name *Somnius* communicated.

Physical egg absent upon waking. No shell fragments recovered.

Cannot confirm whether hatching occurred materially or within another state of existence.

{{date Year 235 · Ignisaur — Subsequent Contact}}

Subject appears intermittently in dreams. Behaviour suggests curiosity rather than hostility.

No evidence that dream-associated influence removes the usual cost of magical offerings.

}}
}}

{{sk,soft,e4-f1
}}

{{sk,e4-f2
}}

{{sk,soft,e4-f3
}}

{{blk,cap,e4-c0
Fig. 1 — opalescent before any infusion.
}}

{{blk,cap,e4-c1
Fig. 2 — from the dreams. Places I have never been.
}}

{{blk,cap,e4-c2
Fig. 3 — Somnius, as seen asleep.
}}

{{blk,doodle,d-moon,e4-d0
}}

{{blk,doodle,d-swirl,e4-d1
}}

{{blk,slip,e4-slip
{{date Year 235 · Verdantis — Follow-up}}

Brief encounter during sleep. Subject appeared aware of the researcher's recent activities concerning Egg No. 05.

No physical manifestation observed.

{{date Year 235 · Zenithar — Revision}}

Recent dream contained imagery resembling the temporal apparatus employed with Egg No. 06.

Possibly influenced by my own thoughts.

**Conclusion:** Dream-based communication appears possible; the physical nature and location of Somnius remain undetermined.

*I no longer consider my recollection alone sufficient evidence.*

}}

{{blk,tape,e4-stp
}}

{{blk,foot,e4-ft
FOLIO 4 · EGG No. 04 · DREAM
}}

\page {rn,fp26}

{{blk,ring,e5-r0
}}

{{blk,hdr,e5-hdr
{{ledger HATCHERY LEDGER · SPECIMEN FILE}}
# Egg No. 05
**Initial Classification:** Unaligned

{{anno Vexigar — The Hellkin Scamp}}

**Alignment:** Infernal &nbsp;|&nbsp; **Origin:** Arcane collector
}}

{{blk,stamp,e5-st
CONTRACT

CONCLUDED
}}

{{blk,e5-log
{{ink1
{{date Year 235 · Ignisaur — Initial Observation}}

Plain grey egg obtained through documented purchase.

Objective: determine whether inscribed magical glyphs can influence alignment and temperament.

Selected Infernal symbols associated with cunning, binding and reciprocal obligation.

{{date Year 235 · Meridius — First Infusion}}

Final glyph completed. Shell warmed immediately. Reddish illumination appeared beneath surface.

Magical expenditure produced expected exhaustion.

Auditory phenomenon resembling laughter noted. Source uncertain.

{{date Year 235 · Meridius — Nurturing}}

Further offerings accompanied by increased activity and apparent responsiveness to speech.

Minor laboratory objects repeatedly displaced.

No direct evidence establishing specimen as cause.

{{date Year 235 · Meridius — Behavioural Observation}}

Attempted visualisation of a fearsome guardian.

Egg responded with prolonged vibration resembling amusement.

*Question: Does the forming organism interpret the caretaker's expectations or reject them?* {{anno see Zunith!}}

{{date Year 235 · Zunith — Hatching}}

Final infusion completed. Small four-footed infernal organism emerged amid harmless embers.

Immediate speech in Infernal. Declared researcher contractually bound to subject.

Designated *Vexigar*.

Initial temperament: playful, highly inquisitive, independently assertive. Strong apparent attachment despite persistent disobedience.

{{date Year 235 · Verdantis — Development}}

Subject demonstrates sensitivity to researcher's emotional state. Mischief decreases during periods of distress.

Behaviour suggests empathy alongside deliberate provocation.

{{date Year 235 · Borealis — Contract Examination}}

Inscribed glyphs may represent mutual obligations rather than unilateral binding.

Unbinding rite performed with subject's apparent cooperation. Sensation of release experienced.

Subject subsequently departed voluntarily.

}}
}}

{{sk,soft,e5-f1
}}

{{blk,photo,e5-f2
&nbsp;
}}

{{blk,photo,e5-f3
&nbsp;
}}

{{sk,soft,e5-f4
}}

{{blk,tape,e5-tp0
}}

{{blk,tape,e5-tp1
}}

{{blk,cap,e5-c0
Fig. 1 — glyphs: cunning, binding, obligation.
}}

{{blk,cap,e5-c1
Fig. 2 — its seal.
}}

{{blk,cap,e5-c2
Fig. 3 — Vexigar, Zunith. Playful; assertive.
}}

{{blk,doodle,d-rune,e5-d0
}}

{{blk,doodle,d-claws,e5-d1
}}

{{blk,slip,e5-slip
{{date Year 235 · Kaelum — Correction}}

Subject returned without prompting.

~~Loyalty dependent upon contractual enchantment.~~

Unsubstantiated. Continued companionship appears voluntary.

Complete status of underlying Genesis connection remains uncertain.

{{date Year 235 · Obsidian — Further Observation}}

Subject repeatedly attempted to disturb Egg No. 06's surroundings. Following its hatching, several pranks were apparently reversed.

Vexigar's surprise appeared genuine.

{{date Year 235 · Zenithar}}

Regular visits continue.

*The contractual experiment is concluded. The interruptions, regrettably, are not.*

}}

{{blk,tape,e5-stp
}}

{{blk,foot,e5-ft
FOLIO 5 · EGG No. 05 · INFERNAL
}}

\page {rn,fp27}

{{blk,ring,e6-r0
}}

{{blk,hdr,e6-hdr
{{ledger HATCHERY LEDGER · SPECIMEN FILE}}
# Egg No. 06
**Initial Classification:** Unaligned — Clutch Specimen

{{anno Chronis — The Gilded Wing}}

**Alignment:** Chrono &nbsp;|&nbsp; **Origin:** Unidentified bag of holding
}}

{{blk,stamp,e6-st
UNDER

OBSERVATION
}}

{{blk,e6-log
{{ink1
{{date Year 235 · Kaelum — Initial Observation}}

Several unaligned eggs discovered within an unmarked blue bag of holding. Provenance unknown.

One specimen selected for controlled temporal exposure. Remaining specimens secured without incubation.

Experimental apparatus: functioning clocks, stopped timepieces, temporal inscriptions and independent reference instruments.

{{date Year 235 · Kaelum — Initial Infusion}}

Deliberate magical offering initiated. Specimen began producing a faint rhythmic ticking.

Researcher experienced expected fatigue.

Shell subsequently developed fine concentric markings resembling clockwork divisions.

{{date Year 235 · Umbral — Temporal Incident I}}

Magical offering initiated shortly after breakfast.

Momentary disorientation experienced.

Upon recovery: laboratory dark, candles exhausted, hearth cold.

Reference clocks indicate approximately twenty-four hours elapsed.

Severe hunger, thirst, bladder discomfort and magical fatigue evident.

No memory of intervening interval.

*Initial hypothesis: Local acceleration of time.* {{anno no — see Incident II}}

{{date Year 235 · Umbral — Correction}}

Magical reserves remain depleted. No evidence of recovery despite elapsed hours.

Time's passage has not eliminated the expenditure.

*No further infusion until properly rested.*

{{date Year 235 · Umbral — Temporal Incident II}}

Experiment repeated with independent observer.

Researcher perceived momentary interruption. Observer recorded approximately seven minutes of apparent immobility.

Reference clocks support observer's measurement.

**Revised hypothesis:** Altered temporal perception or consciousness more likely than general acceleration of surroundings. Mechanism unresolved.

{{date Year 235 · Obsidian — Hatching}}

Final magical offering completed. Shell unfolded symmetrically rather than fracturing.

Clockwork avian organism emerged. Gilded feathers, rotating dial-like eyes and internal mechanical movement observed.

Designated *Chronis*.

Familiar connection established. Researcher again required recovery.

}}
}}

{{sk,soft,e6-f1
}}

{{sk,soft,e6-f2
}}

{{sk,e6-f3
}}

{{blk,photo,e6-f4
&nbsp;
}}

{{blk,tape,e6-tp0
}}

{{blk,cap,e6-c0
Fig. 1 — concentric markings, like clockwork divisions.
}}

{{blk,cap,e6-c1
Fig. 2 — markings develop, Kaelum to Obsidian.
}}

{{blk,cap,e6-c2
Fig. 3 — Chronis. Gilded; dial-like eyes.
}}

{{blk,doodle,d-clock,e6-d0
}}

{{blk,doodle,d-arrow,e6-d1
}}

{{blk,slip,e6-slip
{{date Year 235 · Obsidian — Post-Hatching}}

Subject demonstrates apparent anticipation or reversal of minor events.

Interactions with Egg No. 05 suggest temporal manipulation, although spatial displacement or illusion cannot be excluded.

{{date Year 235 · Zenithar — Temple Visit}}

Subject encountered Egg No. 02. Brief sensation of interference between existing magical connections.

No observable distress. Significance unknown.

{{date Year 235 · Zenithar — Final Revision}}

~~Time alignment ensures predictability.~~

Unsupported. Chronis favours order, but temporal phenomena remain poorly understood.

**Confirmed:** Apparent passage of time does not reverse sacrifice, restore expended magic or guarantee recovery.

*I wished to understand time. I have instead become considerably more careful about how I spend it.*

}}

{{blk,tape,e6-stp
}}

{{blk,foot,e6-ft
FOLIO 6 · EGG No. 06 · CHRONO
}}

\page {diary,fp28}

{{tp
# The Private Journals of Magister Othrelis Var

Dean Emeritus of Living Thaumaturgy

{{tpfig
&nbsp;
}}

{{yrs Years 234 – 235}}
}}

{{tpnote
Private — not for the College library.
}}

{{ring,tpr
&nbsp;
}}

\page {diary,fp29}

{{rh
Journal of O. Var

Year 234 · Aethelwain
}}

{{yr
# Year 234

Of Discovery, Companionship, Loss and Consequence
}}

{{ent,iA
{{dh
{{mo Aethelwain}} An Unremarkable Donation
}}

{{fig,sk,r,dfig0
&nbsp;
}}

I suspect I have been given a very expensive paperweight.

Among the latest donations to the College was a peculiar egg, grey and unremarkable, with neither markings nor any discernible magical properties. Its previous owner had been unable to establish its origin and apparently considered it of little scholarly value although they called it a Genesis Egg.

Naturally, I claimed it for further study.

For three days it occupied a shelf in my laboratory, situated rather unfortunately beside the forge. I had given the object little consideration beyond recording its dimensions and an approximate weight.

Tonight, whilst reaching for a volume on elemental transmutation, my hand brushed against its surface.

The sensation was extraordinary.

Heat surged through my fingertips, followed by a curious pressure within my chest. For the briefest instant, I felt the unmistakable presence of something reaching towards me.

Then came the exhaustion.

I was forced to sit, unable to account for the sudden weakness in my limbs. My magic felt diminished, though I had cast no spell.

The egg, meanwhile, had become warm.

I have moved it to the centre of my workbench.

I suspect my paperweight may warrant closer examination.

}}

{{ent,iA
{{dh
{{mo Aethelwain}} The Forge's Influence
}}

{{fig,sk,l,dfig1
&nbsp;
}}

I have made an unfortunate discovery.

The shell has begun to change.

What was once smooth and grey is now darkening, its surface developing thin, branching lines resembling cracks in cooling volcanic stone.

At first, I attributed the change to whatever enchantment had awakened when I touched it. This morning, however, I noticed that the wood beneath the egg had begun to blacken.

The forge.

Of course.

I had left an unidentified magical object beside a source of considerable elemental energy for several days, without even considering the possible consequences.

A first-year student would have been reprimanded for such carelessness.

I attempted to reverse the effects by removing the egg from the laboratory's heat. The shell remained dark, and the faint glow within its fractures persisted.

}}

{{pn
— 1 —
}}

\page {diary,fp30}

{{rh
Journal of O. Var

Year 234 · Aethelwain – Vaelor
}}

{{ent,iA,cont
Whatever transformation has begun may already be permanent.

More intriguing still, the egg appears to respond when I approach.

I attempted several elementary spells without measurable success. Only when I placed my hand against the shell and deliberately offered a little of my own magical energy did it respond.

The glow brightened. Something moved inside.

The exhaustion returned.

There is a living thing within this shell.

And I believe I have somehow become responsible for it.

}}

{{ent,iA
{{dh
{{mo Vaelor}} A Voice Without Words
}}

{{fig,sk,r,dfig2
&nbsp;
}}

I have taken to speaking to the egg.

An absurd habit, perhaps, but one that has produced some interesting results.

It responds to my voice, though not consistently. When I read aloud from my books, the shell occasionally trembles. When I speak directly to it, the ember-like veins brighten.

I have begun imagining what might emerge.

A drake, perhaps. Something small, with scales like obsidian and eyes like glowing coals.

This morning, whilst describing such a creature, I felt a distinct movement beneath my palm.

I cannot determine whether my thoughts are influencing its development or whether I am merely imagining connections that do not exist.

My magical offerings continue to leave me fatigued. On two occasions I have been forced to abandon my work for the remainder of the day.

Whatever is growing inside requires considerable energy.

I must be more careful.

Nevertheless, I find myself looking forward to our conversations.

}}

{{ent,iA
{{dh
{{mo Vaelor}} Kaelthos
}}

{{fig,photo,l,dfig3
&nbsp;
}}

I was not prepared.

The egg hatched tonight.

I had been preparing another offering, intending to observe its effects before retiring, when the shell suddenly fractured beneath my hand.

Heat washed across the workbench, scattering papers and setting the corner of an unfortunate manuscript alight.

My strength disappeared almost instantly.

And there, among the broken fragments, sat the most extraordinary little creature I have ever seen.

An obsidian drake.

Hardly larger than a domestic cat, with plates of dark volcanic scales and delicate veins of orange light along its neck and shoulders.

It looked at me.

}}

{{pn
— 2 —
}}

\page {diary,fp31}

{{rh
Journal of O. Var

Year 234 · Vaelor – Ignisaur
}}

{{ent,iA,cont
Not with the bewilderment I might have expected from a newly hatched creature, but with immediate recognition.

It climbed rather unsteadily over the remains of its egg, approached my trembling hand, and pressed its head against my fingers.

I knew its name before I spoke it.

Kaelthos.

He has since fallen asleep beside the forge.

I have spent the better part of an hour simply watching him breathe.

I have brought something into the world.

The magnitude of that statement is only now beginning to trouble me.

}}

{{ent,iA
{{dh
{{mo Sylphren}} An Inconvenient Companion
}}

{{fig,soft,r,dfig4
&nbsp;
}}

Kaelthos has developed a personality.

A considerable one.

He has taken to following me throughout the laboratory, occasionally climbing onto my shoulders when he considers my movements insufficiently interesting.

He is particularly fascinated by the forge, though he has also demonstrated a remarkable appetite for roasted meat and an unfortunate habit of investigating anything left unattended.

Yesterday he overturned an entire container of powdered copper.

I found him sitting proudly in the resulting mess, his black scales glittering orange.

My research has suffered.

I do not particularly mind.

More importantly, he has begun demonstrating abilities that I had not anticipated. A small gout of flame escaped his jaws when a visiting scholar startled him. The scholar was unharmed, although his sleeve required attention.

Kaelthos seemed equally surprised.

I have begun taking him outside the College grounds.

He is curious about everything.

Today he spent nearly an hour pursuing insects through the gardens. When I called him, he returned immediately.

I had not taught him to do so.

I find myself increasingly uncertain whether what connects us is an enchantment, an instinct, or something closer to affection.

Perhaps all three.

}}

{{ent,iB
{{dh
{{mo Ignisaur}} The Tide
}}

There are moments I would give anything to experience differently.

I travelled to the coast this morning to gather reagents exposed by the retreating tide. Kaelthos accompanied me, as he has on nearly every excursion since gaining sufficient strength.

}}

{{ring,dp2x0
&nbsp;
}}

{{pn
— 3 —
}}

\page {diary,fp32}

{{rh
Journal of O. Var

Year 234 · Ignisaur
}}

{{ent,iB,cont
The weather was clear. The tide was unusually low.

Among the rock pools I discovered a promising growth of phosphorescent marine algae, valuable for certain alchemical preparations.

I had barely begun collecting samples when something moved beneath the water.

A great shape rose from the deeper pool beyond the rocks, its hide covered in barnacles and trailing weed. It possessed heavy, jointed limbs and a maw lined with broken, shell-like teeth.

Whether it was disturbed by my work or merely territorial, I cannot say.

It attacked before I could retreat.

I managed to raise a defensive ward, but the creature's first blow shattered it. I fell against the rocks, losing my staff.

Kaelthos struck before I could recover.

He leapt at the thing with a ferocity I had never witnessed, breathing fire across its face and drawing its attention away from me.

I remember shouting his name.

I remember struggling to my feet.

And I remember the creature catching him against the rocks with one of its terrible limbs.

I do not clearly recall what followed. I know I cast spells. I know the beast fell back into the water and did not emerge again.

Kaelthos was lying beside the pool.

His scales were fractured, and the light within them flickered unevenly.

He was alive.

I gathered him into my arms and ran.

There is a temple on the road above the harbour. I had passed it that morning without giving it much thought.

By the time I reached its doors, I could scarcely breathe.

The priests took him from me.

They tried everything within their power.

It was not enough.

He died before sunset.

I remained beside him long after the priests had withdrawn.

My little drake.

My first extraordinary discovery.

He had every opportunity to flee.

Instead, he chose to save me.

I had considered him the product of an experiment.

He considered me worth dying for.

I do not know how to reconcile those two truths.

}}

{{dd,d-swirl,dp3x0
&nbsp;
}}

{{dd,d-swirl,dp3x1
&nbsp;
}}

{{pn
— 4 —
}}

\page {diary,fp33}

{{rh
Journal of O. Var

Year 234 · Meridius – Zunith
}}

{{ent,iB
{{dh
{{mo Meridius}} Ashes
}}

{{fig,soft,l,dfig6
&nbsp;
}}

The temple conducted a small service.

I had expected to find the ceremony uncomfortable, perhaps even unnecessary. Kaelthos was a creature of elemental magic, not a member of their faith.

Yet the priests treated his passing with a dignity I shall never forget.

The eldest among them told me that the manner of a being's creation matters little compared with the choices it makes during its life.

I have spent several nights considering his words.

Kaelthos's ashes now rest in a small vessel upon my desk.

The laboratory is intolerably quiet.

I still glance towards the forge expecting to find him sleeping beside it.

More than once I have caught myself moving an open book to make room for a creature who will never again climb onto my workbench.

My colleagues have encouraged me to resume my studies.

I have tried.

But I find it difficult to look at my original observations without recognising how little I understood.

I measured the changes in his shell. I recorded the expenditure of magical energy. I studied the development of his abilities.

I did not record how he greeted me each morning.

Or how he preferred to sleep with one claw resting upon my sleeve.

There are discoveries for which measurements seem hopelessly inadequate.

}}

{{ent,iC
{{dh
{{mo Zunith}} The Temple's Gift
}}

{{fig,soft,r,dfig7
&nbsp;
}}

I returned to the temple today.

I told myself that I wished to thank the priests properly. In truth, I believe I simply wanted to visit the place where Kaelthos spent his final hours.

The elderly priest recognised me immediately.

We spoke at some length about my experiments and the curious nature of the egg from which Kaelthos had emerged.

He listened without interruption.

Eventually, he led me into the temple's reliquary.

Upon a pedestal lay another egg.

Pale, almost luminous, with a faint radiance deep within its shell.

The priest explained that it had been entrusted to their order generations ago. None had discovered its purpose, and none had successfully awakened it.

He offered me the opportunity to study it.

I hesitated.

The thought of another creature suffering because of my ignorance was almost unbearable.

}}

{{pn
— 5 —
}}

\page {diary,fp34}

{{rh
Journal of O. Var

Year 234 · Zunith – Verdantis
}}

{{ent,iC,cont
Yet I could not ignore the possibility that what I had learned from Kaelthos might allow me to approach this new responsibility with greater care.

I asked whether I might conduct my work within the temple.

He agreed.

I have not taken the egg from its home.

Perhaps, for once, I have made a sensible decision.

}}

{{ent,iC
{{dh
{{mo Zunith}} A Different Offering
}}

{{fig,soft,l,dfig8
&nbsp;
}}

I have begun nurturing the new egg.

This time, nothing has been left entirely to chance.

The priests have permitted me to establish a small working space near the sanctuary. They have assisted with blessings, prayers and rituals through which celestial energy may be directed.

I have also brought a small quantity of Kaelthos's ashes.

I scattered them around the egg before making my first deliberate offering of magical energy.

Whether this gesture carries any genuine influence or merely satisfies my own grief, I cannot determine.

The shell responded with a gentle golden glow.

There was none of the fierce heat I remember from Kaelthos.

Instead, the sensation was one of warmth and extraordinary stillness.

The expenditure left me exhausted, as expected, but the egg remained quiet.

I sat beside it for some time.

For the first time since the coastal incident, I found myself speaking to Kaelthos without immediately feeling the full weight of his absence.

I asked that the new creature might be granted a life of its own.

Not a replacement.

Never that.

Something new.

}}

{{ent,iC
{{dh
{{mo Verdantis}} Seraphiel
}}

{{fig,soft,r,dfig9
&nbsp;
}}

The second egg hatched at dawn.

I had been offering the final measure of magical energy required for its development when the shell began to glow.

The priests gathered as the light intensified.

There was no explosion, no violent breaking.

The surface separated into delicate fragments that dissolved like dust in sunlight.

Within sat a small, extraordinary being, possessing several translucent wings and a body that seemed to exist somewhere between solid matter and radiant light.

}}

{{blot,dp5x0
&nbsp;
}}

{{pn
— 6 —
}}

\page {diary,fp35}

{{rh
Journal of O. Var

Year 234 · Verdantis – Borealis
}}

{{ent,iC,cont
Its feathers shimmered as though formed from fine glass.

It looked upon us all with equal curiosity.

When I reached towards it, I experienced that familiar recognition, the quiet certainty of a connection that had been forming throughout incubation.

Yet this time, there was something different.

Kaelthos had immediately sought my company.

This creature turned towards the temple's inner sanctuary.

As though something there had called to it.

I named it Seraphiel.

Or perhaps, as with Kaelthos, I merely recognised a name that was already its own.

The priests are delighted.

I must confess that I am rather taken with it myself.

}}

{{ent,iC
{{dh
{{mo Borealis}} A Life Beyond My Laboratory
}}

{{fig,soft,l,dfig10
&nbsp;
}}

Seraphiel has proved unlike any creature I had imagined.

Its interest in my experiments is minimal.

Attempts to encourage its curiosity about elemental structures or magical transmutation have generally produced little more than polite indifference.

Healing, however, commands its complete attention.

A few days ago, one of the temple attendants cut her hand while preparing food. Seraphiel approached without prompting and placed a small wing against the wound.

The bleeding diminished, and the attendant's discomfort appeared to ease.

I was astonished.

Since then, Seraphiel has begun accompanying the priests as they care for the sick.

It has also demonstrated an interest in the temple's purification rituals. Yesterday I watched it approach a basin of fouled water and extend its wings over the surface.

Within moments, the unpleasant cloudiness had diminished.

I cannot yet explain how.

The priests believe Seraphiel has been given a sacred purpose.

I remain cautious about such conclusions.

Nevertheless, I cannot deny that the creature appears happiest when engaged in their work.

I have also come to an uncomfortable realisation.

I am poorly qualified to guide it.

My knowledge concerns transmutation, living thaumaturgy and the relationship between magical forces. The disciplines of healing and divine restoration lie far beyond my interests.

Seraphiel has found teachers better suited to its nature.

Perhaps the best thing I can do is allow it to learn from them.

}}

{{pn
— 7 —
}}

\page {diary,fp36}

{{rh
Journal of O. Var

Year 234 · Kaelum – Umbral
}}

{{ent,iC
{{dh
{{mo Kaelum}} The Road Home
}}

{{fig,photo,r,dfig11
&nbsp;
}}

I returned to the College today.

Alone.

Not because Seraphiel has died, or because I have abandoned it, but because it has chosen to remain at the temple.

It seemed content when I prepared to leave, watching from the sanctuary steps as the priests helped load my equipment.

I placed my hand against its feathers before departing.

Our connection was still there.

I made no attempt to sever it.

Nor did I command Seraphiel to follow.

I simply told it that I hoped to return soon.

It rested its head briefly against my hand, then turned back towards the priests.

I felt an unexpected satisfaction.

With Kaelthos, I had feared losing a creature I loved.

With Seraphiel, I am beginning to understand that distance need not be loss.

The journey home was strangely peaceful.

Yet a question has begun troubling me.

If the magical connection between Seraphiel and myself remains, what would happen were I to attempt the nurturing of another egg?

I have no intention of answering that question carelessly.

At least, that is what I told myself this evening.

}}

{{ent,iD
{{dh
{{mo Umbral}} Forbidden Pages
}}

{{fig,soft,l,dfig12
&nbsp;
}}

I have resumed my studies.

Recent correspondence with several colleagues has led me towards an intriguing collection of texts concerning entities from beyond the familiar planes.

Eldritch intelligences, beings whose apparent awareness does not depend upon ordinary physical forms, and accounts of consciousness existing independently of matter.

The implications for Genesis Eggs are considerable.

If the nature of an egg can be influenced by elemental forces or celestial magic, what might happen when exposed to energies that defy conventional classification?

I have spent several evenings considering the question.

Today, while sorting a parcel of books purchased from a distant collection, I discovered an egg among the volumes.

Dark cloth had been wrapped carefully around it.

I have no recollection of ordering such an object.

More troubling still, there is no corresponding entry in my acquisition ledger.

}}

{{pn
— 8 —
}}

\page {diary,fp37}

{{rh
Journal of O. Var

Year 234 · Umbral – Obsidian
}}

{{ent,iD,cont
I questioned the courier, who insisted that the parcel arrived sealed.

The books themselves appear genuine.

The egg does not.

I have placed it inside a protective circle until I can determine its nature.

I cannot escape the uncomfortable feeling that I have seen it before.

}}

{{ent,iD
{{dh
{{mo Umbral}} The Reflection
}}

{{fig,sk,r,dfig13
&nbsp;
}}

Something is wrong.

The egg has changed without any deliberate influence from me.

I cannot adequately describe its surface.

At times it appears perfectly black. At others, it resembles a polished mirror, though the reflection it offers is seldom accurate.

This morning I saw myself standing beside the workbench.

The image was smiling.

I was not.

I withdrew immediately.

The exhaustion began shortly afterwards.

I have given this egg neither life force nor magic.

Yet I recognise the sensation of energy being drawn from me.

Worse still, I occasionally feel the familiar warmth of my connection with Seraphiel, far away at the temple, interrupted by something cold and unfamiliar.

I do not believe these are the same kind of connection.

Nevertheless, their apparent interference is deeply concerning.

I have written to the temple requesting advice.

I have also attempted to isolate the egg.

When I returned from dinner, it was no longer inside the protective circle.

It had moved to the edge of my desk.

I have not touched it again.

}}

{{ent,iD
{{dh
{{mo Obsidian}} Mirrith
}}

{{fig,soft,l,dfig14
&nbsp;
}}

The egg is gone.

I did not witness its hatching.

I entered the laboratory this morning and discovered an entity standing where the egg had rested.

Or rather, I discovered something occupying that space.

It has no consistent shape.

When observed directly, it resembles a figure assembled from shadow and reflections. Its outline changes whenever my attention shifts.

Sometimes I see a face.

Sometimes my own.

}}

{{ring,dp8x0
&nbsp;
}}

{{pn
— 9 —
}}

\page {diary,fp38}

{{rh
Journal of O. Var

Year 234 · Obsidian
}}

{{ent,iD,cont
Sometimes faces I have not thought about in decades.

It does not speak, yet I am certain it understands me.

I have named it Mirrith, though I do not remember deciding upon the name.

The familiar sensation of a Genesis bond is present, but corrupted by something I cannot understand.

Kaelthos's connection had been warm and immediate.

Seraphiel's remains gentle even across great distance.

This is different.

An intrusion.

As though a door has been opened inside my thoughts and something has decided to stand in the doorway.

I am no longer certain whether I invited it.

}}

{{ent,iD
{{dh
{{mo Obsidian}} A Visit to the Temple
}}

{{fig,sk,r,dfig15
&nbsp;
}}

I have returned to the temple.

Not with Mirrith.

I dare not attempt to transport it.

The priests listened to my account with considerable concern. The elderly priest suggested several protective rites, though he cautioned that their effectiveness could not be guaranteed.

Seraphiel approached during our conversation.

I had wondered whether our separation might have weakened its familiarity with me.

I need not have worried.

It came directly to my side, resting one luminous wing against my arm.

For the briefest moment, the unease that has accompanied me since Mirrith's appearance diminished.

The priests prepared a collection of blessed stones and protective inscriptions for my laboratory.

Seraphiel remained nearby throughout the rites.

It has grown more assured since I last saw it.

One young attendant told me that the creature had recently helped cleanse a contaminated well outside the village.

I ought to have felt proud.

Instead, I found myself troubled by the contrast.

One creation brings comfort to the suffering.

Another has left me afraid to enter my own study.

Both have emerged from eggs.

I cannot determine whether the difference lies in the energies that shaped them, my actions during incubation, or something entirely their own.

Perhaps I have been too eager to assume that I am the defining influence in these processes.

}}

{{dd,d-eye,dp9x0
&nbsp;
}}

{{pn
— 10 —
}}

\page {diary,fp39}

{{rh
Journal of O. Var

Year 234 · Zenithar
}}

{{ent,iD
{{dh
{{mo Zenithar}} The Chamber of Mirrors
}}

{{fig,photo,l,dfig16
&nbsp;
}}

Mirrith is contained.

I hesitate to use the word imprisoned, though perhaps that is what I have done.

With assistance from the temple's inscriptions, I constructed a chamber of reinforced glass and warded mirrors. The structure has been placed beneath the laboratory, away from the College's ordinary activities.

The entity entered it under circumstances I cannot entirely explain.

For several moments, my reflections appeared on every surface of the chamber.

Then the wards activated.

The reflections vanished.

Mirrith has not emerged.

I can no longer sense its presence as clearly as before, though certain disturbances remain.

Occasionally a mirror catches my attention for reasons I cannot identify.

At night I dream of corridors that should not exist.

I have begun constructing additional protections around my sleeping quarters.

I know that such precautions may seem excessive.

I have also come to understand that my previous confidence was frequently misplaced.

Seraphiel remains at the temple, and I continue to feel its familiar presence at a distance.

Mirrith remains beneath my workshop, and I cannot establish whether the connection it forced upon me has ended.

Two very different relationships, neither completely explained.

I have spent almost a year studying Genesis Eggs.

I have witnessed courage, compassion and horror.

And for all my accumulated notes, I am beginning to suspect that I understand far less than I believed.

I shall continue my research.

But not without better safeguards.

}}

{{blot,dp10x0
&nbsp;
}}

{{efig,epf10
&nbsp;
}}

{{ecap,epc10
the egg's progress across my desk, as best I recall
}}

{{pn
— 11 —
}}

\page {diary,fp40}

{{rh
Journal of O. Var

Year 235 · Aethelwain
}}

{{yr
# Year 235

Of Dreams, Mischief, Time and Understanding
}}

{{ent,iE
{{dh
{{mo Aethelwain}} The Price of Protection
}}

{{fig,sk,r,dfig17
&nbsp;
}}

I have not slept properly in several weeks.

The wards surrounding my sleeping quarters have been strengthened repeatedly. I have incorporated sigils of mental protection, illusion-dampening enchantments, and several experimental inscriptions intended to prevent unwanted contact during sleep.

They appear effective.

Mirrith has not visited my dreams.

Unfortunately, I can scarcely remember the last occasion upon which I enjoyed an uninterrupted night.

I have begun to wonder whether the protections themselves are disturbing my rest.

A colleague recently sent me another unaligned egg, properly documented and obtained through a reputable academic collection. After my previous experience, I insisted upon personally examining its provenance.

The accompanying records appear satisfactory.

I have placed it within the laboratory, intending to resume my research under carefully controlled conditions.

This time, I shall not permit unknown influences to reach it.

An optimistic assertion, perhaps.

The shell has already begun taking on a faintly opalescent appearance.

I have not yet attempted any deliberate alignment.

I suspect my protective enchantments may be interacting with it.

I should investigate before proceeding.

}}

{{ent,iE
{{dh
{{mo Aethelwain}} Dreams Within the Shell
}}

{{fig,soft,l,dfig18
&nbsp;
}}

The egg has begun behaving most peculiarly.

Its appearance is inconsistent.

When observed directly, it retains a smooth, pale shell. Yet whenever my attention wanders, I find its shape subtly altered.

I have attempted to verify this using mirrors and several elementary observation spells.

The results are inconclusive.

Last night, I dreamt of my laboratory.

Everything appeared perfectly ordinary, save for the position of the doors and windows.

Upon waking, I discovered that I had been speaking aloud.

}}

{{dd,d-moon,dp11x0
&nbsp;
}}

{{pn
— 12 —
}}

\page {diary,fp41}

{{rh
Journal of O. Var

Year 235 · Aethelwain – Sylphren
}}

{{ent,iE,cont
The egg was glowing.

I now suspect that the protective enchantments surrounding my work have influenced its development, particularly those designed to safeguard my sleeping mind.

It is an uncomfortable possibility.

I constructed these wards to prevent Mirrith from entering my thoughts.

I may inadvertently have created an environment in which thought itself has become the dominant shaping influence.

I have resolved to continue the experiment cautiously.

If the egg is already developing an alignment, abandoning it without understanding its condition may be no wiser than proceeding.

Nevertheless, I shall make no further offerings until I have rested.

My previous mistakes have taught me that exhaustion and good judgement are seldom close companions.

}}

{{ent,iE
{{dh
{{mo Vaelor}} The Laboratory That Wasn't
}}

{{fig,sk,r,dfig19
&nbsp;
}}

I attempted an offering of magical energy this afternoon.

The result was deeply unsettling.

The moment my magic entered the shell, the laboratory changed.

The bookshelves stretched towards a ceiling far above the room's normal dimensions. My workbench appeared several feet from its proper position, and the windows opened upon a sky filled with unfamiliar stars.

I saw my quill moving across an open notebook.

I was not holding it.

Then I found myself sitting beside the egg.

The laboratory was normal.

My magic had been expended, and I was exhausted, but I could not determine whether I had physically moved or experienced some form of waking dream.

More disturbing still, the protective inscriptions surrounding the room had changed.

Several symbols were now slightly different from those I had originally written.

I spent the remainder of the afternoon comparing them against my records.

I found no evidence that anyone had entered the laboratory.

The egg remained quiet throughout.

I am beginning to question whether my senses can be trusted during these experiments.

That is an uncomfortable admission for a scholar whose work depends so heavily upon observation.

I have arranged for a colleague to examine the room independently.

I shall not tell him what I believe has happened until he has recorded his own findings.

}}

{{ent,iE
{{dh
{{mo Sylphren}} Somnius
}}

It hatched in my dreams.

I know how absurd that statement appears.

Yet I can offer no more satisfactory explanation.

}}

{{pn
— 13 —
}}

\page {diary,fp42}

{{rh
Journal of O. Var

Year 235 · Sylphren – Ignisaur
}}

{{ent,iE,cont
{{fig,soft,l,dfig20
&nbsp;
}}

Last night, I found myself standing upon the shore of an enormous, perfectly still lake. There was neither wind nor sound, and the sky above reflected stars I did not recognise.

Upon the water rested the egg.

Its shell opened without a sound.

Something rose from within: a delicate, shifting creature composed of mist, translucent veils and fragments of colour that seemed to vanish whenever I attempted to examine them.

It regarded me with unmistakable curiosity.

Then I heard a name.

Somnius.

I awoke immediately.

The egg was gone from my laboratory.

No fragments remained.

I searched the room, examined my wards and questioned the night watch.

Nothing.

Yet whenever I close my eyes, I feel that same gentle curiosity hovering just beyond the edge of conscious thought.

Unlike Mirrith, the sensation is neither threatening nor invasive.

Nevertheless, I cannot identify the precise nature of our connection.

I have brought another creature into existence without understanding where it now resides.

I am becoming distressingly accomplished at this.

}}

{{ent,iE
{{dh
{{mo Ignisaur}} A Visitor in Sleep
}}

{{fig,sk,r,dfig21
&nbsp;
}}

Somnius visited me again.

This time, I found myself wandering through the College library.

The shelves were filled with books I had never read, though their titles seemed strangely familiar.

Somnius moved between them like mist caught in a draught.

I attempted to ask whether it was happy.

An inadequate question, perhaps, but the only one that seemed important.

The creature regarded me for several moments.

Then the library transformed into a hillside beneath a golden evening sky.

I understood, without words, that it wished to explore.

There was no fear in the experience.

Only curiosity.

When I awoke, I felt tired but oddly comforted.

I have decided against attempting to summon Somnius into the waking world.

I cannot establish whether such a thing is possible, and I see little reason to force the question.

If it returns, I shall welcome the visit.

}}

{{pn
— 14 —
}}

\page {diary,fp43}

{{rh
Journal of O. Var

Year 235 · Ignisaur – Meridius
}}

{{ent,iE,cont
If it does not, I hope wherever it has gone offers more pleasant discoveries than those that accompanied its creation.

I have also received a letter from the temple.

Seraphiel continues its work among the priests and has reportedly become rather adept at identifying impurities in their medicinal preparations.

An amusing development.

I spent years studying magical substances before learning half as much about their purification.

My former companion appears to have developed considerably greater practical wisdom than its researcher.

Our connection remains familiar, even at this distance.

It seems that not all bonds demand proximity to endure.

}}

{{ent,iF
{{dh
{{mo Ignisaur}} A Return to Proper Experimentation
}}

{{fig,photo,l,dfig22
&nbsp;
}}

I have resolved to undertake a more disciplined study.

My previous experiments have been influenced by accident, grief, fear and circumstances well beyond my control.

This cannot continue indefinitely.

I recently acquired another unaligned egg from a specialist collector, together with several volumes concerning symbolic enchantment.

My intention is to investigate whether magical glyphs can influence the nature of a developing creature.

The theory is straightforward.

If elemental surroundings may shape an egg, perhaps deliberately selected magical symbols can provide a similar influence.

I have chosen Infernal inscriptions.

Not, I hasten to add, because I wish to create some monstrous instrument of destruction.

My knowledge of Infernal script is simply more extensive than my familiarity with several other symbolic traditions.

I intend to employ signs associated with cunning, obligation and binding.

I have reviewed the relevant translations carefully.

Twice.

Given my recent history, perhaps a third review would be sensible.

}}

{{ent,iF
{{dh
{{mo Meridius}} An Unfortunate Sense of Humour
}}

{{fig,soft,r,dfig23
&nbsp;
}}

The inscriptions have been completed.

The egg responded immediately.

Upon tracing the final symbol, the shell grew warm and a faint reddish glow appeared beneath its surface.

I experienced the expected magical fatigue, though something else accompanied it.

Laughter.

Not from elsewhere in the room.

From the egg.

I am certain of it.

}}

{{ring,dp14x0
&nbsp;
}}

{{pn
— 15 —
}}

\page {diary,fp44}

{{rh
Journal of O. Var

Year 235 · Meridius – Zunith
}}

{{ent,iF,cont
A quiet, mischievous sound, like a child attempting to conceal some particularly entertaining wrongdoing.

I examined the inscriptions again.

None appeared incorrectly formed.

The egg gave another little tremor.

I am beginning to suspect it finds my seriousness amusing.

This morning, I discovered my inkpot on the highest bookshelf.

I distinctly remember leaving it beside my notebook.

No one admits to moving it.

The egg was warm when I retrieved the ink.

I shall attempt to maintain appropriate scientific detachment.

Although I must confess that I laughed.

It has been a long time since I did so.

}}

{{ent,iF
{{dh
{{mo Zunith}} Vexigar
}}

{{fig,soft,l,dfig24
&nbsp;
}}

I have been insulted by something less than an hour old.

The egg hatched this afternoon, scattering harmless embers across my workbench.

From within emerged a small, four-footed creature with dark, layered scales, pointed ears, a curling horn and eyes that glowed like coals.

It surveyed the laboratory with obvious approval.

Then it leapt onto my desk, knocked over a stack of research notes, and climbed directly onto my shoulder.

Before I could speak, it announced in perfectly articulated Infernal:

"Hello, contract-bound! You're mine now!"

I informed it that I had signed no such contract.

It laughed.

I explained that magical bonds were complex phenomena requiring careful examination.

It laughed harder.

I attempted to remove it from my shoulder.

It wrapped itself around my neck and declared that it intended to remain there.

I have named it Vexigar.

Though, as with my previous creations, I suspect the matter of naming may be less entirely my decision than I once believed.

It has already hidden two quills, overturned a bowl of powdered silver and attempted to eat the corner of an ancient manuscript.

I should be furious.

Instead, I find myself smiling.

Kaelthos would have adored him.

I had not expected that thought to bring me comfort.

But it does.

}}

{{pn
— 16 —
}}

\page {diary,fp45}

{{rh
Journal of O. Var

Year 235 · Verdantis – Borealis
}}

{{ent,iF
{{dh
{{mo Verdantis}} The Laboratory Laughs Again
}}

{{fig,soft,r,dfig25
&nbsp;
}}

Vexigar has settled into the College with remarkable confidence.

I cannot say the same for the College.

Several scholars have complained about rearranged books, mysterious laughter and the sudden disappearance of minor personal possessions.

I have apologised repeatedly.

Vexigar has not.

He possesses considerable magical curiosity, though his approach to experimentation differs rather significantly from my own.

For example, he recently discovered that a particular runic inscription causes a small flame to change colour.

I spent an afternoon documenting the interaction.

Vexigar spent the same afternoon attempting to make every candle in the laboratory burn green.

By evening, he had succeeded.

He appeared extraordinarily pleased with himself.

Yet beneath the mischief there is unmistakable affection.

He follows me during my work, watches my experiments and occasionally offers observations that are surprisingly perceptive.

He has also demonstrated a disconcerting awareness of my moods.

On evenings when my thoughts turn towards Kaelthos or the events surrounding Mirrith, his pranks become noticeably less intrusive.

Last night, he simply curled upon the back of my chair while I read.

Neither of us spoke.

I had forgotten how welcome such company could be.

I remain uncertain about the nature of the Infernal connection formed during his incubation, particularly given the lingering bonds and disturbances of my earlier experiments.

It does not resemble Seraphiel's gentle presence.

Nor does it resemble Mirrith's intrusion.

I must resist the temptation to describe all these phenomena as though they were identical.

The differences may prove more significant than the similarities.

}}

{{ent,iF
{{dh
{{mo Borealis}} A Contract Neither of Us Understood
}}

Vexigar and I have reached an arrangement.

Or so I believe.

During a review of the Infernal inscriptions used in his development, I discovered that several symbols could be interpreted as establishing reciprocal obligations rather than simple restrictions.

This would certainly explain his insistence that I belong to him.

I explained my concerns.

He responded by asking whether I intended to dismiss him.

}}

{{pn
— 17 —
}}

\page {diary,fp46}

{{rh
Journal of O. Var

Year 235 · Borealis – Kaelum
}}

{{ent,iF,cont
{{fig,photo,l,dfig26
&nbsp;
}}

I told him that I had no desire to compel his company through magical obligations.

He considered this for a moment.

Then asked whether he might continue visiting the laboratory.

Naturally, I agreed.

We performed a small unbinding rite intended to dissolve whatever contractual hold the glyphs might still exert between us.

The sensation was peculiar: a brief loosening of something I had barely known was present.

Whether every consequence of those inscriptions has been resolved remains uncertain.

Vexigar regarded the completed ritual with considerable scepticism.

Then he stole my quill.

He has since taken to disappearing for days at a time, returning without warning, usually carrying something of dubious provenance.

Yesterday he appeared with a silver spoon.

I have not asked where he found it.

It seems our friendship is no longer dependent upon the peculiar contractual terms of his creation.

I find that reassuring.

There is a pleasure in knowing a creature returns because it wishes to, rather than because it has been instructed to do so.

And, despite myself, I am always glad when I hear that unmistakable laughter coming from the corridor.

}}

{{ent,iF
{{dh
{{mo Kaelum}} The Bag
}}

I have received another mystery.

A bag of holding appeared among my belongings this morning.

It is a simple thing, fashioned from blue cloth faded almost to grey, with no maker's mark or obvious indication of its origin.

I have questioned the College staff.

No one recalls delivering it.

After my experience with Mirrith, I approached the object with considerable caution.

I examined it for hostile enchantments, placed it within a protective circle, and enlisted a colleague to witness the initial inspection.

Nothing untoward occurred.

Within the bag was a clutch of apparently unaligned Genesis Eggs.

Several of them.

Perfectly ordinary in appearance.

I cannot begin to imagine who would have assembled such a collection, much less entrusted it to me without explanation.

I confess the discovery has rekindled a familiar curiosity.

Yet it has also prompted an unfamiliar restraint.

}}

{{blot,dp17x0
&nbsp;
}}

{{pn
— 18 —
}}

\page {diary,fp47}

{{rh
Journal of O. Var

Year 235 · Kaelum – Umbral
}}

{{ent,iF,cont
I have numbered the eggs and placed them in separate protective compartments.

I shall not attempt to nurture them simultaneously.

My previous experiences have demonstrated how difficult it can be to understand even one developing creature, especially when other magical connections remain unresolved.

One egg will suffice.

Perhaps, when I finally understand that single experiment, I shall decide what to do with the others.

}}

{{ent,iG
{{dh
{{mo Kaelum}} The Pursuit of Order
}}

{{fig,soft,r,dfig28
&nbsp;
}}

I have selected an egg.

For several days I considered the possible influences I might employ.

Elemental magic has produced extraordinary results. Celestial energy has revealed unexpected possibilities. Eldritch and dream-aligned experiments have taught me rather more about uncertainty than I wished to learn.

Infernal glyphs, meanwhile, have provided me with a companion who currently appears to be attempting to teach a broom to dance.

I desire something more orderly.

Something measurable.

Something predictable.

Time.

I have constructed a cradle surrounded by clocks, temporal inscriptions and several instruments designed to detect irregularities in the passage of magical energy.

Some of the clocks are functional. Others have been deliberately stopped.

The arrangement is quite beautiful.

Vexigar has already attempted to rearrange it.

I have forbidden him from touching the apparatus.

He smiled when I said this.

I shall reinforce the protective wards.

}}

{{ent,iG
{{dh
{{mo Umbral}} The Missing Day
}}

{{fig,sk,l,dfig29
&nbsp;
}}

I have misplaced an entire day.

I began the latest infusion shortly after breakfast.

The laboratory was brightly lit. Several candles burned beside the workbench, and every clock in the temporal cradle had been carefully synchronised.

I placed my hand upon the egg and began transferring a measured portion of magical energy.

The shell began to tick.

A soft, precise sound.

I felt an unfamiliar pressure behind my eyes.

Then the room went dark.

For several moments I believed the candles had been extinguished by a draught.

I reached for the nearest one.

}}

{{pn
— 19 —
}}

\page {diary,fp48}

{{rh
Journal of O. Var

Year 235 · Umbral
}}

{{ent,iG,cont
There was nothing left but a pool of hardened wax.

Every candle had burned down.

The fire in the hearth was cold.

I looked towards the windows.

Night.

The clocks surrounding the egg indicated that approximately twenty-four hours had passed.

I checked them twice.

Then a third time.

My stomach was painfully empty, my mouth dry, and I experienced a sudden, rather urgent need to visit the privy.

There are indignities to magical research that rarely appear in scholarly publications.

I shall ensure this one remains in my private diary.

After attending to the necessities of existence, I returned to examine the room.

The egg was unchanged, save for the faint ticking within its shell.

My magical energy remained depleted.

I was physically exhausted.

Whatever had occurred, the passage of time had not relieved me of the cost of the offering.

Indeed, I felt as though my body had endured the missing hours while my awareness had simply failed to accompany it.

I cannot determine whether time accelerated around me, whether my perception was interrupted, or whether the egg displaced me through some temporal phenomenon not yet understood.

But one conclusion is unavoidable.

The cost was paid.

I merely failed to witness its passage.

I shall not attempt another infusion until I have properly recovered.

And next time, I shall arrange for someone else to observe the experiment.

Preferably someone who will not permit me to spend an entire day neglecting my bodily requirements.

}}

{{ent,iG
{{dh
{{mo Umbral}} The Witness
}}

{{fig,sk,r,dfig30
&nbsp;
}}

My colleague agreed to observe a subsequent experiment from outside the immediate working circle.

We synchronised several clocks and recorded the condition of the apparatus before beginning.

The result was considerably less dramatic than my previous experience, though no less intriguing.

I felt the familiar pressure behind my eyes.

For an instant, the ticking ceased.

When I looked up, my colleague was staring at me.

He informed me that I had remained motionless for nearly seven minutes.

From my perspective, no more than a heartbeat had elapsed.

The surrounding clocks agreed with his account.

}}

{{pn
— 20 —
}}

\page {diary,fp49}

{{rh
Journal of O. Var

Year 235 · Umbral – Obsidian
}}

{{ent,iG,cont
Once again, I felt the expenditure of magical energy and the accompanying fatigue.

I asked whether he had witnessed anything else unusual.

He hesitated.

Then informed me that, during the interval, I had apparently turned my head towards the egg and smiled.

I have no recollection of doing so.

I find that detail more disturbing than the missing time itself.

The egg continues to develop.

Its shell has begun acquiring delicate lines resembling the mechanisms of a finely crafted clock.

I am cautiously optimistic.

Though I shall refrain from declaring the experiment predictable.

My previous declarations of that nature have rarely survived contact with reality.

}}

{{ent,iG
{{dh
{{mo Obsidian}} Chronis
}}

{{fig,soft,l,dfig31
&nbsp;
}}

The final hatching occurred tonight.

I had prepared the necessary offering and arranged for the experiment to be witnessed.

Vexigar had been firmly instructed to remain outside the working circle.

He complied, though not without complaint.

The egg began ticking steadily as the magic entered it.

For several moments, nothing else occurred.

Then the shell unfolded.

There is no better word.

Its surface separated into delicate, symmetrical sections, opening like the petals of an impossibly intricate mechanical flower.

Within sat a small bird.

Its feathers were fashioned from shimmering gold and darker metallic filaments, while tiny mechanisms turned beneath its surface with astonishing precision.

Its eyes resembled the faces of miniature clocks.

It regarded me calmly.

There was no panic, no confusion.

It extended its wings, rose from the remains of the shell and settled upon my shoulder.

The ticking stopped.

In its place I felt a quiet, rhythmic sensation, almost as though some unseen mechanism had fallen into step with my own heartbeat.

Chronis.

The name arrived with the same peculiar certainty I have encountered before.

Vexigar immediately announced that the creature looked like an expensive clock.

Chronis turned towards him.

The Infernal scamp attempted to flick a small ember at the new arrival.

The ember vanished.

A moment later, it reappeared above Vexigar's head and dropped into his hair.

}}

{{ring,dp20x0
&nbsp;
}}

{{pn
— 21 —
}}

\page {diary,fp50}

{{rh
Journal of O. Var

Year 235 · Obsidian – Zenithar
}}

{{ent,iG,cont
He was not amused.

I laughed until my ribs hurt.

I had forgotten how much joy a successful hatching could bring.

}}

{{ent,iG
{{dh
{{mo Obsidian}} The War of Small Mischiefs
}}

{{fig,soft,r,dfig32
&nbsp;
}}

Chronis and Vexigar have developed a peculiar relationship.

I hesitate to call it a rivalry.

Vexigar delights in disorder. Chronis appears to possess an equally strong inclination towards arrangement, repetition and the correction of minor irregularities.

Yesterday, Vexigar scattered my research papers across the laboratory.

Before the final page touched the floor, they had returned to their original positions.

Vexigar stared at them.

Chronis merely adjusted a feather.

The incident repeated three times.

On the fourth attempt, Vexigar hid the papers beneath a cushion.

The cushion was suddenly beneath the papers.

I have not determined how Chronis accomplished this.

Vexigar accused the bird of cheating.

Chronis remained silent.

Their exchanges have become a source of considerable entertainment.

Yet I am careful not to assume that Chronis's orderly behaviour indicates complete control over its own temporal abilities.

My recent experiences have demonstrated that apparent stability can conceal mechanisms of extraordinary complexity.

I continue to experience fatigue when magical energy is transferred through our connection.

No amount of temporal manipulation has demonstrated an ability to restore energy that was sacrificed.

This, at least, appears consistent.

I am grateful for one reliable observation.

}}

{{ent,iG
{{dh
{{mo Zenithar}} The Temple, Once More
}}

{{fig,photo,l,dfig33
&nbsp;
}}

I returned to the temple this week.

Chronis accompanied me.

The journey was uneventful, though the bird spent a considerable portion of it watching the movement of the sun with what I can only describe as professional interest.

The temple has changed very little.

The old priest greeted me warmly, although he observed that I appeared to have aged somewhat since my first visit.

I informed him that my research had occasionally involved rather more time than I intended.

}}

{{pn
— 22 —
}}

\page {diary,fp51}

{{rh
Journal of O. Var

Year 235 · Zenithar
}}

{{ent,iG,cont
He did not appear to find the remark amusing.

Seraphiel came to meet us in the sanctuary.

It has grown more assured in its movements, its luminous wings now carrying an elegance that was absent when it first emerged from the shell.

It approached without hesitation.

I felt the familiar warmth of our connection before it reached me.

Still there.

Even after our long separation.

Chronis observed Seraphiel quietly from my shoulder.

For a moment, I sensed the peculiar discomfort I have sometimes experienced when the influences of my different experiments appear to overlap.

Then the feeling passed.

Neither creature seemed distressed.

I shall record the incident properly upon my return.

The priests spoke at length of Seraphiel's work.

It has assisted with the treatment of illness, purification of water and the care of travellers seeking shelter.

One young priest remarked that Seraphiel often anticipates the needs of patients before they have expressed them.

I listened with great interest.

Yet I felt no desire to reclaim the creature or redirect its activities.

It has established a life entirely its own.

I once believed that the success of a Genesis Creature could be measured by the degree to which it reflected its caretaker's intentions.

Looking upon Seraphiel, I find that assumption increasingly difficult to defend.

It has become something I could never have taught it to be.

And I am pleased.

}}

{{ent,iG
{{dh
{{mo Zenithar}} Old Friends and Unfinished Questions
}}

{{fig,sk,r,dfig34
&nbsp;
}}

I have begun reviewing my earlier journals.

Two years.

It seems an impossible span of time.

I still remember the first donated egg sitting beside my forge, utterly unremarkable.

I had no conception of what would follow.

Kaelthos.

I cannot write his name without remembering the little creature sleeping beside the fire, nor the desperate journey from the shore to the temple.

His ashes remain part of my collection, though I have never again regarded them merely as a research specimen.

Seraphiel continues its work among the priests. Our connection persists despite the distance between us and the very different paths our lives have taken.

}}

{{pn
— 23 —
}}

\page {diary,fp52}

{{rh
Journal of O. Var

Year 235 · Zenithar
}}

{{ent,iG,cont
Mirrith remains within the warded chamber beneath my laboratory.

At least, I believe it does.

The wards have remained intact, and no further manifestation has been conclusively identified. Nevertheless, I occasionally encounter a reflection that appears to hesitate before following my movements.

Somnius has visited my dreams twice in recent weeks.

On the second occasion, I found myself standing in an unfamiliar meadow beneath a sky filled with slowly moving clocks.

The creature regarded me with its usual curiosity.

I woke feeling strangely reassured.

Vexigar remains an intermittent nuisance.

He has not returned the silver spoon.

Chronis is perched beside me as I write.

Its mechanisms turn quietly, keeping a rhythm I cannot entirely comprehend.

I have spent much of my life believing that understanding a thing meant learning how to control it.

The past two years have provided considerable evidence to the contrary.

I have made mistakes.

Some have been embarrassing.

Others have been costly beyond measure.

Yet I have also witnessed extraordinary kindness, courage, humour and intelligence in beings whose existence I once considered little more than a fascinating branch of magical experimentation.

My research has produced more questions than answers.

I no longer consider that a failure.

}}

{{ent,iG
{{dh
{{mo Zenithar}} The Work Ahead
}}

{{fig,photo,r,dfig35
&nbsp;
}}

I have decided to compile my findings into a formal treatise.

Not merely an account of the creatures themselves, but an examination of the processes through which they came into being.

Looking across the six experiments, I believe I can identify recurring stages of development.

An initial influence upon the egg.

A period of nurturing through magical or physical sacrifice.

The gradual development of awareness and individual form.

And finally, the extraordinary event of hatching.

Yet I must be cautious.

My observations are neither complete nor universally consistent.

Mirrith resisted almost every assumption I had formed. Somnius remains difficult to classify. Chronis has demonstrated effects I can observe but not adequately explain.

}}

{{pn
— 24 —
}}

\page {diary,fp53}

{{rh
Journal of O. Var

Year 235 · Zenithar
}}

{{ent,iG,cont
Even the apparently straightforward experiments contain questions I cannot answer with certainty.

I shall return to my original research notes and revise them wherever subsequent evidence has contradicted my earlier conclusions.

I shall preserve those errors rather than erase them.

A future scholar may learn as much from my mistakes as from my discoveries.

The remaining eggs from the mysterious bag have been secured within the College's protected archives, alongside the original container.

Their origin remains unknown.

I have chosen not to begin another incubation.

Six experiments have provided more than sufficient material for several lifetimes of study.

And, perhaps more importantly, I find that I am content with the company I already keep.

Chronis has settled upon my shoulder.

Somewhere in the laboratory, Vexigar is laughing.

I suspect he has discovered another way to interfere with the clocks.

I should investigate.

But first, one final observation.

When I began this research, I believed a Genesis Egg to be an object awaiting transformation.

I now believe that description is profoundly inadequate.

Something lives within each shell, though the nature of that life remains uncertain until it emerges.

It is influenced by magic, environment and the actions of those who nurture it.

But influence is not ownership.

Connection is not command.

And creation is not the same as understanding.

Kaelthos taught me the cost of responsibility.

Seraphiel taught me the value of independence.

Mirrith taught me to fear my own arrogance.

Somnius taught me that reality may extend beyond what I can perceive.

Vexigar reminded me that affection often arrives without permission.

And Chronis…

Chronis is teaching me that even time cannot make the consequences of our choices disappear.

I began this work hoping to discover what a Genesis Egg might become.

I end these pages wondering what the study has made of me.

}}

{{sig
— Magister Othrelis Var

Dean Emeritus of Living Thaumaturgy
}}

{{dd,d-clock,dp24x0
&nbsp;
}}

{{dd,d-star,dp24x1
&nbsp;
}}

{{ring,dp24x2
&nbsp;
}}

{{pn
— 25 —
}}

\page {production34,fp54}
![](https://raw.githubusercontent.com/Omegaoliverid/Public-images/main/Genesis-Eggs/approved/bramblegut-adult.png){position:absolute,top:0px,left:0px,width:100%,height:100%,object-fit:cover,object-position:center}

{{partcap,top
##### PART THREE
## Example Companions
Four eggs followed from infusion through growth; three include exceptional Ascended examples: Bramblegut, Rynnix, Flubbs and Elysian. Each shows the tracker filled in, then their illustrated growth stages.
}}

{{spellcard
##### SPELLS ORIGINAL TO THIS BOOK
Stir Soil, Stormspark Orb and Haunting Image use their listed spell levels and the companion’s casting limits. Complete definitions, together with the Genesis cantrips Spark Zap, Arc Lance and Force Nudge, appear in the [Original Spells reference](#p56).

Every technique uses the companion’s normal action and existing casting budget.
}}

\page {rules,dense,mechanicsReference}
{{gmtab
GAME MASTER
}}

{{wide
# Creature Spell Reference

A creature’s magical appearance and sounds reflect its anatomy and character. These theatrical details grant no extra effects or castings. Named game spells follow their normal rules except where an entry says otherwise; the bespoke techniques below use their printed mechanics and the companion’s existing casting budget. Agree any unlisted casting requirement with the GM when the technique is learned.

## Practical and Lightning Magic

**Stir Soil** (cantrip). Loosens, shifts or smooths a 5-foot square of soil or mud within 30 feet. Practical only: it deals no damage.

**Stormspark Orb** (1st-level evocation). Casting time: 1 action. Range: 90 feet. Components: V, S. Duration: instantaneous. A crackling orb flies at one creature within range: ranged spell attack, 3d8 lightning damage on a hit.

Both use one creature action. Stormspark Orb consumes one existing level-1 casting; these entries do not grant additional castings.

## Haunting Image

**Haunting Image (2nd-level illusion; one level-2 casting).** One creature action; range 60 feet; one creature the caster can see. The target makes an Intelligence save against the creature’s spell save DC. On failure, it perceives a threatening illusion and takes **1d6 psychic damage at the start of each of its turns** while affected. Concentration, up to 1 minute. It may spend an action to repeat the Intelligence save, ending the effect on success. The effect also ends when concentration ends. It cannot deal additional damage, restrain, frighten, charm, impose free terrain barriers or conjure an attacker. It consumes the listed casting.

## Genesis Cantrips

**Spark Zap** (evocation cantrip). One creature action. Ranged spell attack against one creature within 60 feet (90 feet from Juvenile): **1d8** lightning damage as a Hatchling, **2d8** as a Juvenile and **3d8** as an Adult or Ascended. **Arc Lance** is Rynnix's name for its Adult and Ascended Spark Zap; it is the same cantrip.

**Force Nudge** (evocation cantrip). One creature action. Ranged spell attack against one creature within 60 feet: **1d4** force damage as a Hatchling, **2d4** as a Juvenile and **3d4** as an Adult or Ascended. It doesn't push the target.

Flubbs's Adult level-3 casting uses the SRD spell **Hypnotic Pattern**.

Each new levelled casting requires a fresh player command and consumes its existing casting budget. Normal concentration limits apply.
}}

{{footnote GENESIS EGGS | RULES REFERENCE}}
{{pageNumber,auto}}
\page {casefile,production35,fp55}

{{wide,chapterhead
##### EXAMPLE COMPANION · GENESIS EGG TRACKER
# Bramblegut, the Chitin Guardian
}}

{{wide,caseinfo
| | | | |
|:--|:--|:--|:--|
| Egg Name | “Bramblegut” | Aspect Chosen | Acid |
| PC Name | Thalor Greenbark (Druid) | Campaign/Arc | “Shadow over Silverwood” |
}}

{{wide,trackerGrid
{{stage
#### Stage One – Initial Infusion
- **Trigger:** Egg is bound (1 level of exhaustion taken)
- **Sacrifice Type:** ☑ Hit Die ☐ Spell Slot (Thalor expends one of his own d8 Hit Dice as a Health infusion; the creature’s eventual d10 Hit Die comes from the 3H / 1M total)
- **Infusion Source:** Immersed in moss and acid magic, kept within a giant beetle shell filled with acid, handled with attentive care by Thalor
- **Aspect Chosen:** Acid (theme: defensive barrier)
- **Notes:**
  - Initial reaction: Egg is encased in a shell of organic moss and acid, faintly pulsing with corrosive energy
}}

{{stage
#### Stage Two – Sustained Care
- **Trigger:** Second sacrifice: expend an available resource; gain 1 exhaustion level
- **Sacrifice Type:** ☑ Hit Die ☐ Spell Slot (second Hit Die expended)
- **Care Method Detail:** ☐ Empathy ☐ Dreams ☐ Protective Urge ☑ Whispered Communication ☐ Sings to Egg ☐ Damages Egg ☐ Draws on Egg ☐ Ignores ☐ Other
  > “Thalor stays close, nurturing the egg with vigilant attention, speaking softly and imagining it as a loyal guardian”
- **Care Method Other Detail:** “Uses gentle druidic magic”
- **Care Frequency:** Daily
- **Notes on Physical/Magical Changes:**
  - Shell thickens, and the acid glow becomes more defined, faintly dissolving substances around it
}}

{{stage
#### Stage Three – Visualisation
- **Trigger:** Third sacrifice: expend an available resource; gain 1 exhaustion level
- **Sacrifice Type:** ☑ Hit Die ☐ Spell Slot (third Hit Die expended)
- **PC Visualisation:**
  - **Name:** “Bramblegut” (the name Thalor hopes for the guardian)
  - **Shape/Form Ideas:** Giant insectoid with mossy, acidic hide, exoskeleton with glowing, corrosive reserves, claws and mandibles suited for fighting and defence
  - **Quirks or Emotions:** Loyal, vigilant, driven to protect, with a protective instinct against enemies
- **Care Method Detail:** ☑ Empathy ☐ Dreams ☐ Protective Urge ☑ Whispered Communication ☐ Sings to Egg ☐ Damages Egg ☐ Draws on Egg ☐ Ignores ☐ Other
  > “Thalor narrates stories of defending the grove, imagining Bramblegut as a fierce, acid-dissolving shield”
- **Care Method Other Detail:** “Practices patience, encouraging the egg to develop resilience and defensive magic”
- **Care Frequency:** Every day, during downtime
- **Egg Response:** Gains resilience, begins producing faint acid vapors from shell
- **Notes:**
  - Growing attachment, the egg’s shell shows signs of increased strength and reactive acid subsurface
}}

{{stage
#### Stage Four – Naming & Birth
- **Trigger:** Fourth sacrifice: expend an available resource; gain 1 exhaustion level
- **Sacrifice Type:** ☐ Hit Die ☑ Spell Slot (one spell slot expended; final 3H / 1M ratio gives creature d10 Hit Die)
- **Final Form Name:** **“Bramblegut”**
- **Infusion mix:** 3 Health / 1 Magic (d10); role: Guardian (one minor cantrip; physical protection)
- **Care Score (1–10):** 9 (deep bond, protective instincts)
- **Relationship Notes:** “Thalor’s loyal protector, born from a love of defence and acid magic, designed to dissolve enemy defences and shield allies”
- **Current Creature Hit Die:** ☐ d4 ☐ d6 ☐ d8 ☑ d10 ☐ d12 (d10, grows with player levels)
- **Magical allowance:** 3 Health / 1 Magic (d10): at most **one learned cantrip** at any stage; never levelled spells.
- **Trait Notes:**
  - Acidic exoskeleton, guardian instincts, resilient shell
- **Temperament Notes:**
  - Attentive, loyal, protective, driven by instinct to shield and dissolve threats
- **Visual Characteristic:**
  - Tiny, mossy insectoid
}}
}}

{{footnote GENESIS EGGS | EXAMPLE COMPANION: BRAMBLEGUT}}
{{pageNumber,auto}}

\page {production36,fp56}
{{monster,frame,wide
## Bramblegut — Chitin Guardian
### Hatchling — example bonded player level 3
*Tiny monstrosity (insectoid; acid), neutral good*

**Armor Class** :: 14  
**Hit Points** :: 28 (level-based fixed Hit Die; see Growth, p. 7)  
**Speed** :: 25 ft., climb 15 ft.  

| STR | DEX | CON | INT | WIS | CHA |
|:--:|:--:|:--:|:--:|:--:|:--:|
| 14 (+2) | 12 (+1) | 14 (+2) | 6 (-2) | 12 (+1) | 8 (-1) |

**Saving Throws** :: +4 Constitution  
**Skills** :: Athletics +4  
**Damage Resistances** :: acid, poison  
**Languages** :: Understands simple trained commands  
**Infusions** :: 3 Health / 1 Magic; d10  
**Bond** :: One stable Genesis bond; one creature action; standing orders and GM loyalty apply  
**Proficiency Bonus** :: +2  

**Traits** :: A loyal moss-plated defender; advantage against being knocked prone.

**Actions** :: **Chitin Bash.** Melee weapon attack +4; 1d8 + 2 bludgeoning against one target.

**Other Action** :: **Stand Guard.** May use its action to protect a doorway or adjacent ally instead of attacking.

**Known Magic** :: **Stir Soil** (1 harmless/practical cantrip; spellcasting requires normal command).

**Reaction** :: **Guardian Instinct.** 1/long rest; adjacent perceived ally; prevent up to 1d6 damage from one attack and take the amount prevented. After damage roll, before application; no area damage or wall maintenance. See [Protection Reference](#p60).

*Protection may arise instinctively, even if its bonded player is unconscious.*

}}

{{monster,frame,wide
## Bramblegut — Living Bastion
### Juvenile — example bonded player level 7
*Small monstrosity (insectoid; acid), neutral good*

**Armor Class** :: 17  
**Hit Points** :: 60 (level-based fixed Hit Die; see Growth, p. 7)  
**Speed** :: 30 ft., climb 20 ft.  

| STR | DEX | CON | INT | WIS | CHA |
|:--:|:--:|:--:|:--:|:--:|:--:|
| 16 (+3) | 12 (+1) | 15 (+2) | 6 (-2) | 12 (+1) | 8 (-1) |

**Saving Throws** :: +5 Constitution  
**Skills** :: Athletics +6  
**Damage Resistances** :: acid, poison  
**Languages** :: Understands trained commands  
**Infusions** :: 3 Health / 1 Magic; d10  
**Bond** :: One stable Genesis bond; one creature action; standing orders and GM loyalty apply  
**Proficiency Bonus** :: +3  

**Traits** :: Thick chitin and steady footing; a trained shield for companions.

**Actions** :: **Chitin Slam.** Melee weapon attack +6; 2d8 + 3 bludgeoning to one target.

**Other Action** :: **Guard Position.** Uses its action to protect a position; significant restraint or a control move replaces its damaging attack.

**Known Magic** :: **Stir Soil** (same one known cantrip).

**Reaction** :: **Guardian Interception.** 2/long rest; perceived ally within 10 ft.; prevent up to 2d6 damage from one attack and take the amount prevented. After damage roll, before application; no area damage or wall maintenance. See [Protection Reference](#p60).

*Stronger protection has been earned through story rather than an extra free attack.*

}}


<div class="wide stageGallery" style="height:225px"><img src="https://raw.githubusercontent.com/Omegaoliverid/Public-images/main/Genesis-Eggs/approved/bramblegut-hatchling-juvenile.png" alt="bramblegut hatchling juvenile"></div>

{{footnote GENESIS EGGS | EXAMPLE COMPANION: BRAMBLEGUT}}
{{pageNumber,auto}}

\page {production37,fp57}
{{monster,frame,wide
## Bramblegut — Verdant Guardian
### Adult — example bonded player level 12
*Large monstrosity (insectoid; acid), lawful good*

**Armor Class** :: 19  
**Hit Points** :: 102 (level-based fixed Hit Die; see Growth, p. 7)  
**Speed** :: 30 ft., climb 30 ft., burrow 10 ft.  

| STR | DEX | CON | INT | WIS | CHA |
|:--:|:--:|:--:|:--:|:--:|:--:|
| 18 (+4) | 12 (+1) | 18 (+4) | 6 (-2) | 12 (+1) | 8 (-1) |

**Saving Throws** :: +8 Constitution  
**Skills** :: Athletics +8  
**Damage Resistances** :: acid, poison  
**Languages** :: Understands trained commands  
**Infusions** :: 3 Health / 1 Magic; d10  
**Bond** :: One stable Genesis bond; one creature action; standing orders and GM loyalty apply  
**Proficiency Bonus** :: +4  

**Traits** :: Poisoned-condition immunity; sustained Care 9–10 additionally grants Charmed immunity. No blanket physical weapon resistance.

**Actions** :: **Shell Slam.** Melee weapon attack +8; 2d10 + 4 bludgeoning to one target.

**Other Action** :: **Verdant Shield Wall (2/long rest).** Action to create adjacent opaque 10-by-10-ft. shield (AC 17, 25 HP); next action to maintain, maximum two rounds. Ends at 0 HP, movement, incapacitation or stopped maintenance. Directional total cover only; own AC 22. No movement, attack, casting or interception while maintaining. See [Protection Reference](#p60).

**Known Magic** :: **Stir Soil** (one cantrip only; no levelled spells).

**Reaction** :: **Guardian's Vow.** 2/long rest; perceived ally within 10 ft.; prevent up to 4d6 damage; take half ordinary physical damage prevented (round up), or full magical damage subject to existing resistance. After damage roll, before application; no area damage or wall maintenance. See [Protection Reference](#p60).

*Strong guardian, not a high-damage striker. Its barrier and attacks compete for its creature actions.*

}}

{{evo,wide
#### Final Growth & Learning Progression

**Bramblegut's Development:**

**Suggested GM story milestones:** Ten meaningful interceptions might prompt a Juvenile evolution; surviving a critical sacrifice for another may inspire adulthood. These are examples, never automatic triggers or free HP restoration.
}}

{{art,wide,height:380px,artc,width:100%
![](https://raw.githubusercontent.com/Omegaoliverid/Public-images/main/Genesis-Eggs/approved/bramblegut-adult.png)
}}

{{footnote GENESIS EGGS | EXAMPLE COMPANION: BRAMBLEGUT}}
{{pageNumber,auto}}

\page {rules,dense,mechanicsReference}
{{gmtab
GAME MASTER
}}

{{wide
# Bramblegut — Protection Reference

Bramblegut must be conscious, able to react and within the listed reach. A prevented amount never exceeds the damage the attack would actually deal. Resolve each reaction after damage is rolled but before application. One reaction cannot protect from area damage or be combined with a second reaction. No interception while maintaining Verdant Shield Wall.

**Guardian Instinct (Reaction; 1/long rest).** When an adjacent ally Bramblegut can perceive takes damage from one attack, Bramblegut may use its reaction to prevent up to **1d6** of that damage and take damage equal to the amount prevented. Resolve after damage is rolled but before it is applied; no area attacks or second reaction.

**Guardian Interception (Reaction; 2/long rest).** When an ally within 10 feet that Bramblegut can perceive takes damage from one attack, it may prevent up to **2d6** of the damage and take the same amount itself. Resolve after damage is rolled and before application; no area attacks.

**Guardian’s Vow (Reaction; 2/long rest).** When an ally within 10 feet that Bramblegut can perceive takes damage from one attack, prevent up to **4d6** of that damage. Bramblegut takes half the actual prevented amount (round up) from an ordinary physical attack, or the full amount from magical damage unless an applicable existing resistance genuinely reduces that damage. This cannot be used while maintaining Verdant Shield Wall or against area damage. No double-counting of prevented damage or stacking the same reduction twice.

## Verdant Shield Wall

The barrier is a visible, opaque **10-foot-wide, 10-foot-high, freestanding physical shield** occupying a continuous line directly adjacent to Bramblegut. It does not enclose a creature or create a dome. It has **AC 17, 25 HP**, ends when reduced to 0 HP, lasts at most **2 rounds**, and requires Bramblegut’s action to create and action on the following round to maintain. It ends early if Bramblegut moves, becomes incapacitated, or ceases maintaining it. Only creatures actually behind its line receive total cover from a blocked direction; attacks and effects that can go around the shield still work under ordinary cover rules. Bramblegut’s own AC is 22 only while maintaining; it cannot intercept, move, cast or attack during maintenance. **2 uses per long rest.**
}}

{{footnote GENESIS EGGS | RULES REFERENCE}}
{{pageNumber,auto}}
\page {casefile,production38,fp58}

{{wide,chapterhead
##### EXAMPLE COMPANION · GENESIS EGG TRACKER
# Rynnix, the Arc-Shard
}}

{{wide,caseinfo
| | | | |
|:--|:--|:--|:--|
| Egg Name | “Rynnix” | Aspect Chosen | Lightning |
| PC Name | Aria Painsbain (Cleric) | Campaign/Arc | “Shadow over Silverwood” |
}}

{{wide,trackerGrid
{{stage
#### Stage One – Initial Infusion
- **Trigger:** Egg is infused with lightning energy (1 level of exhaustion taken and one available spell slot expended)
- **Sacrifice Type:** ☐ Hit Die ☑ Spell Slot
- **Infusion Source:** Infused with lightning magic, from a powerful, storm-infused ritual by the caster
- **Aspect Chosen:** Lightning (theme: power)
- **Notes:**
  - Initial reaction: Crackling energy surrounds the egg, faint sparks dance across surface
}}

{{stage
#### Stage Two – Sustained Care
- **Trigger:** Second sacrifice: expend an available resource; gain 1 exhaustion level
- **Sacrifice Type:** ☐ Hit Die ☑ Spell Slot
- **Care Method Detail:** ☐ Empathy ☐ Dreams ☐ Protective Urge ☑ Whispered Communication ☐ Sings to Egg ☐ Damages Egg ☐ Draws on Egg ☐ Ignores ☑ Other
  > “The caster nurtures and speaks softly, channelling lightning using a ring charged with lightning magic to strengthen the hatchling”
- **Care Method Other Detail:** “Focuses on daily contact and shaping the spark of power”
- **Care Frequency:** Daily, during spellcasting routines
- **Notes on Physical/Magical Changes:**
  - Egg pulses with static, sparks lightly dance across surface
}}

{{stage
#### Stage Three – Visualisation
- **Trigger:** Third sacrifice: expend an available resource; gain 1 exhaustion level
- **Sacrifice Type:** ☑ Hit Die ☐ Spell Slot
- **PC Visualisation:**
  - **Name:** “Rynnix” (the name representing the lightning streak)
  - **Shape/Form Ideas:** Tiny elemental fey construct with crackling energy, glowing filament-like Rings, small shimmering with arc lightning
  - **Quirks or Emotions:** Eager to support, fiercely protective, driven by the storm’s power
- **Care Method Detail:** ☑ Empathy ☐ Dreams ☐ Protective Urge ☑ Whispered Communication ☐ Sings to Egg ☐ Damages Egg ☐ Draws on Egg ☐ Ignores ☑ Other
  > “The caster whispers words of power and strength to the egg, envisioning a lightning spirit of Order and support”
- **Care Method Other Detail:** “Practices harnessing static and lightning, eager to evolve”
- **Care Frequency:** Daily
- **Egg Response:** Becomes more volatile, sparks dance more fiercely on surface
- **Notes:**
  - Increasing energy within the egg, ready to blast into a storm
}}

{{stage
#### Stage Four – Naming & Birth
- **Trigger:** Fourth sacrifice: expend an available resource; gain 1 exhaustion level
- **Sacrifice Type:** ☐ Hit Die ☑ Spell Slot (d6 Hit Die; Adult maximum third-level magic)
- **Final Form Name:** **“Arc-Shard”** or **“Rynnix”**
- **Infusion mix:** 1 Health / 3 Magic (d6); role: Magical Striker (lightning spells)
- **Care Score (1–10):** 9 (deep bond, power-focused evolution)
- **Relationship Notes:** “A stormborn protector, born from a desire for power and support, lightning streaks representing her strength”
- **Current Creature Hit Die:** ☐ d4 ☑ d6 ☐ d8 ☐ d10 ☐ d12 (d6 Hit Die)
- **Magical allowance:** 1 Health / 3 Magic (d6): at most **third-level** magic as an Adult under the daily casting limits.
- **Trait Notes:**
  - Crackling, agile, power-infused, lightning resistance; flight develops only under [Flight and Gliding](#p13).
- **Temperament Notes:**
  - Eager, aggressive when supporting allies, lawful neutral
- **Visual Characteristic:**
  - Small, crackling Rings, glowing filament Construct, sparks dancing around it
}}
}}

{{evo,wide
#### Rynnix Evolution System

- **Arc-Shard:** Starting form.

- **Arc-Woven:** Might evolve after a decisive, well-trained lightning rescue.

- **Arc-Fused:** Might mature after learning restraint alongside power.

- **Thunderheart:** An exceptional Ascension needs a significant campaign story and GM approval.
}}

{{footnote GENESIS EGGS | EXAMPLE COMPANION: RYNNIX}}
{{pageNumber,auto}}

\page {production39,fp59}
{{monster,frame,wide
## Rynnix — Arc-Shard
### Hatchling — example bonded player level 3
*Tiny elemental (storm; fey-like), lawful neutral*

**Armor Class** :: 13  
**Hit Points** :: 17 (level-based fixed Hit Die; see Growth, p. 7)  
**Speed** :: 30 ft.; controlled glide only (see [Flight and Gliding](#p13))  

| STR | DEX | CON | INT | WIS | CHA |
|:--:|:--:|:--:|:--:|:--:|:--:|
| 6 (-2) | 14 (+2) | 12 (+1) | 14 (+2) | 10 (+0) | 12 (+1) |

**Saving Throws** :: +4 Dexterity  
**Skills** :: Perception +2  
**Damage Resistances** :: lightning  
**Languages** :: Understands simple words  
**Infusions** :: 1 Health / 3 Magic; d6  
**Bond** :: One stable Genesis bond; one creature action; standing orders and GM loyalty apply  
**Proficiency Bonus** :: +2  

**Traits** :: Harmless static shimmers indicate emotion; cannot fly or hover as a Hatchling.

**Actions** :: **Spark Zap.** Ranged spell attack +4, range 60 ft.; 1d8 lightning damage (one action).

**Known Magic** :: **Spark Zap** (1 learned cantrip; no levelled spells at Hatchling).

*One small magical action, not a second rechargeable attack.*

}}

{{monster,frame,wide
## Rynnix — Arc-Woven
### Juvenile — example bonded player level 7
*Small elemental (storm; fey-like), lawful neutral*

**Armor Class** :: 15  
**Hit Points** :: 37 (level-based fixed Hit Die; see Growth, p. 7)  
**Speed** :: 35 ft.; short flight up to 20 ft. per turn; must land; may glide; no rider (see [Flight and Gliding](#p13))  

| STR | DEX | CON | INT | WIS | CHA |
|:--:|:--:|:--:|:--:|:--:|:--:|
| 6 (-2) | 14 (+2) | 13 (+1) | 16 (+3) | 10 (+0) | 12 (+1) |

**Saving Throws** :: +5 Dexterity  
**Skills** :: Perception +3  
**Damage Resistances** :: lightning  
**Languages** :: Understands trained commands  
**Infusions** :: 1 Health / 3 Magic; d6  
**Bond** :: One stable Genesis bond; one creature action; standing orders and GM loyalty apply  
**Proficiency Bonus** :: +3  

**Traits** :: Can reposition swiftly and uses one action for attacks or spellcasting.

**Actions** :: **Spark Zap.** Ranged spell attack +6, range 90 ft.; 2d8 lightning damage.

**Known Magic** :: Cantrips: **Spark Zap**, **Prestidigitation**. Once per long rest: **Stormspark Orb** (level 1, lightning only), **Shatter** (level 2). Both spells require fresh commands.

*Lightning spells use the same limited budget as any special electrical technique.*

}}




<div class="wide stageGallery" style="height:240px"><img src="https://raw.githubusercontent.com/Omegaoliverid/Public-images/main/Genesis-Eggs/approved/rynnix-hatchling.png" alt="rynnix hatchling"><img src="https://raw.githubusercontent.com/Omegaoliverid/Public-images/main/Genesis-Eggs/approved/rynnix-juvenile.png" alt="rynnix juvenile"></div>

{{footnote GENESIS EGGS | EXAMPLE COMPANION: RYNNIX}}
{{pageNumber,auto}}

\page {production40,fp60}

{{monster,frame,wide
## Rynnix — Arc-Fused
### Adult — example bonded player level 12
*Medium elemental (storm; fey-like), lawful neutral*

**Armor Class** :: 17  
**Hit Points** :: 63 (level-based fixed Hit Die; see Growth, p. 7)  
**Speed** :: 40 ft., fly 50 ft.; cannot carry a rider (see [Flight and Gliding](#p13))  

| STR | DEX | CON | INT | WIS | CHA |
|:--:|:--:|:--:|:--:|:--:|:--:|
| 6 (-2) | 16 (+3) | 14 (+2) | 18 (+4) | 10 (+0) | 12 (+1) |

**Saving Throws** :: +7 Dexterity  
**Skills** :: Perception +4  
**Damage Resistances** :: lightning  
**Languages** :: Understands trained commands  
**Infusions** :: 1 Health / 3 Magic; d6  
**Bond** :: One stable Genesis bond; one creature action; standing orders and GM loyalty apply  
**Proficiency Bonus** :: +4  

**Traits** :: Its attack bonus and save DC follow the bonded player’s proficiency bonus.

**Actions** :: **Arc Lance.** Ranged spell attack +8, range 90 ft.; 3d8 lightning damage, no automatic secondary control.

**Known Magic** :: Cantrips: **Arc Lance**, **Prestidigitation**, **Light**. Per long rest: **2 × Stormspark Orb** (level 1), **1 × Shatter** (level 2), **1 × Lightning Bolt** (level 3). Each levelled spell uses its creature action and a new player command.

*Powerful storms are limited castings, not independent recharge abilities.*

}}

{{monster,frame,wide
## Rynnix — Thunderheart
### Ascended — example bonded player level 17
*Medium elemental (ascended storm; fey-like), lawful neutral*

**Armor Class** :: 18  
**Hit Points** :: 93 (level-based fixed Hit Die; see Growth, p. 7)  
**Speed** :: 50 ft., fly 60 ft.; rider only with GM approval, suitable anatomy, size and capacity (see [Flight and Gliding](#p13))  

| STR | DEX | CON | INT | WIS | CHA |
|:--:|:--:|:--:|:--:|:--:|:--:|
| 6 (-2) | 16 (+3) | 14 (+2) | 18 (+4) | 10 (+0) | 12 (+1) |

**Saving Throws** :: +9 Dexterity  
**Skills** :: Perception +6  
**Damage Resistances** :: lightning  
**Languages** :: Understands trained commands  
**Infusions** :: 1 Health / 3 Magic; d6  
**Bond** :: One stable Genesis bond; one creature action; standing orders and GM loyalty apply  
**Proficiency Bonus** :: +6  

**Traits** :: Exceptional Ascension must be earned by the story; no extra turns, legendary actions or automatic extra ASIs.

**Actions** :: **Arc Lance.** Ranged spell attack +10; 3d8 lightning damage, range 90 ft. as Adult.

**Other Action** :: **Stormlink Nova (one signature use/long rest).** One creature action; up to three visible targets within 60 ft.; DC 18 Dexterity save, 8d6 lightning on failure, half on success. Requires a fresh player command under Ascension rules. No extra stun, chain, reaction damage or additional attack.

**Known Magic** :: Retains Adult cantrips and level-1-to-3 allowance; signature is separate once/long rest.

*Ordinary command is a player action; exceptional mastery might permit a bonus-action command for the signature.*

}}


<div class="wide stageGallery" style="height:240px"><img src="https://raw.githubusercontent.com/Omegaoliverid/Public-images/main/Genesis-Eggs/approved/rynnix-adult.png" alt="rynnix adult"><img src="https://raw.githubusercontent.com/Omegaoliverid/Public-images/main/Genesis-Eggs/approved/rynnix-ascended.png" alt="rynnix ascended"></div>

{{footnote GENESIS EGGS | EXAMPLE COMPANION: RYNNIX}}
{{pageNumber,auto}}

\page {production41,fp61}
![](https://raw.githubusercontent.com/Omegaoliverid/Public-images/main/Genesis-Eggs/final-2026-10-17/rainbow-slime-closeup.jpg){position:absolute,top:95px,left:32px,width:730px,height:730px,object-fit:contain}

{{evo,evocap
#### Flubbs — Slime Evolution

- **Prism-slime:** Shared performances and earned trust may inspire Juvenile evolution.
- **Rainbow-slime:** A defining performance or brave use of illusion may inspire adulthood.
- **Radiant-slime:** Famous or selfless acts may inspire a rare, GM-approved Ascension.

*These are story prompts, not mandatory dice-roll or gold-piece quotas.*
}}

\page {casefile,production42,fp62}

{{wide,chapterhead
##### EXAMPLE COMPANION · GENESIS EGG TRACKER
# Flubbs, the Shimmer-slime
}}

{{wide,caseinfo
| | | | |
|:--|:--|:--|:--|
| Egg Name | “Flubbs” | Aspect Chosen | Illusion |
| PC Name | Jaspian Willowdare (Half-Elf Bard) | Campaign/Arc | “Shadow over Silverwood” |
}}

{{wide,trackerGrid
{{stage
#### Stage One – Initial Infusion
- **Trigger:** Egg is bound (1 level of exhaustion taken)
- **Sacrifice Type:** ☑ Hit Die ☐ Spell Slot (first cost paid in flesh – poetic, Jaspian said)
- **Infusion Source:** Bathed in prismatic stage lights, kissed with bardic glamour and chord resonance during rehearsal
- **Aspect Chosen:** Illusion (theme: colour)
- **Notes:**
  - Initial reaction: Egg jiggles with spectral hues, pulses softly in time with music nearby
  - Environmental influence: Nestled in a satin-lined viola case, absorbing sound and vibration
}}

{{stage
#### Stage Two – Sustained Care
- **Trigger:** Second sacrifice: expend an available resource; gain 1 exhaustion level
- **Sacrifice Type:** ☐ Hit Die ☑ Spell Slot
- **Care Method Detail:** ☑ Empathy ☑ Dreams ☑ Whispered Communication ☑ Sings to Egg ☐ Damages Egg ☐ Draws on Egg ☐ Ignores ☐ Other
  > “Jaspian sings to it every morning before shows, sometimes letting it vibrate on a tuning fork or glide over an enchanted harp”
- **Care Method Other Detail:** “Gently dabbed with colourful pigments during song rituals”
- **Care Frequency:** Daily, at the end of each performance or rehearsal
- **Notes on Physical/Magical Changes:**
  - Egg begins to shimmer iridescently, shifts colours with mood and music pitch
  - Occasionally emits a squeaky hum or repeats musical notes it hears
}}

{{stage
#### Stage Three – Visualisation
- **Trigger:** Third sacrifice: expend an available resource; gain 1 exhaustion level
- **Sacrifice Type:** ☐ Hit Die ☑ Spell Slot
- **PC Visualisation:**
  - **Name:** “Flubbs” (named for the sound it makes when plopping into a room dramatically)
  - **Shape/Form Ideas:** Gelatinous blob with shifting rainbow sheen, eyes like stained glass, tendrils that mimic dance or play instruments
  - **Quirks or Emotions:** Giddy, craves attention, loves being the centre of a crowd, enjoys echoing sounds in comical ways
- **Care Method Detail:** ☑ Empathy ☑ Dreams ☑ Whispered Communication ☑ Sings to Egg ☐ Damages Egg ☐ Draws on Egg ☐ Ignores ☑ Other
  > “Jaspian began rehearsing comedy duets with Flubbs’ projected illusions, testing crowd reactions”
- **Care Method Other Detail:** “Uses it to simulate minor illusions in rehearsals, and let it bounce along drumbeats”
- **Care Frequency:** Every show and downtime moment backstage
- **Egg Response:** Swells slightly with bass tones, reflects intense colour during high applause moments
- **Notes:**
  - Began projecting crude illusions: glowing hearts, musical notes, and mirror images of its bardic partner
}}

{{stage
#### Stage Four – Naming & Birth
- **Trigger:** Fourth sacrifice: expend an available resource; gain 1 exhaustion level
- **Sacrifice Type:** ☐ Hit Die ☑ Spell Slot
- **Final Form Name:** **“Flubbs”**
- **Infusion mix:** 1 Health / 3 Magic (d6); role: Balanced Support/Controller (illusions)
- **Care Score (1–10):** 8 (playful and loyal, sometimes distracted by applause)
- **Relationship Notes:** “Performs beside Jaspian in a lightshow duet, trusted illusion support and comedic partner”
- **Current Creature Hit Die:** ☐ d4 ☑ d6 ☐ d8
- **Magical allowance:** 1 Health / 3 Magic (d6): at most **third-level** magic as an Adult under the daily casting limits.
- **Trait Notes:**
  - Naturally generates minor illusions and distracting lights, can mimic bardic spells
  - Projects light or sound as needed for ambience, theme, or confusion
- **Temperament Notes:**
  - Silly, expressive, melodramatic, but clever with illusions and improvisation
- **Visual Characteristic:**
  - Translucent rainbow ooze, sparkles with internal starlight, can form eyes, a grin, or shapes mid-performance
}}
}}

{{footnote GENESIS EGGS | EXAMPLE COMPANION: FLUBBS}}
{{pageNumber,auto}}

\page {production43,fp63}
{{monster,frame,wide
## Flubbs — Shimmer-slime
### Hatchling — example bonded player level 3
*Small rainbow ooze, playful*

**Armor Class** :: 13  
**Hit Points** :: 20 (level-based fixed Hit Die; see Growth, p. 7)  
**Speed** :: 20 ft., climb 20 ft.  

| STR | DEX | CON | INT | WIS | CHA |
|:--:|:--:|:--:|:--:|:--:|:--:|
| 6 (-2) | 12 (+1) | 14 (+2) | 6 (-2) | 10 (+0) | 14 (+2) |

**Saving Throws** :: +4 Charisma  
**Skills** :: Deception +4  
**Damage Resistances** :: —  
**Languages** :: Understands simple phrases  
**Infusions** :: 1 Health / 3 Magic; d6  
**Bond** :: One stable Genesis bond; one creature action; standing orders and GM loyalty apply  
**Proficiency Bonus** :: +2  

**Traits** :: Amorphous and decorative rainbow light; noncombat performances are free flavour.

**Actions** :: **Slime Slap.** Melee attack +3; 1d6 + 1 bludgeoning.

**Known Magic** :: Cantrip: **Minor Illusion** (1 learned cantrip; no levelled magic).

**Reaction** :: **Distracting Radiance (1/long rest).** When a creature Flubbs can see makes a perceptible melee attack against Flubbs or an ally within 10 ft., spend its reaction before the roll to impose disadvantage on that one roll.

*Needs a meaningful action to create an illusion that changes combat or bypasses an obstacle.*

}}

{{monster,frame,wide
## Flubbs — Prism-slime
### Juvenile — example bonded player level 7
*Small rainbow ooze, playful*

**Armor Class** :: 14  
**Hit Points** :: 44 (level-based fixed Hit Die; see Growth, p. 7)  
**Speed** :: 30 ft., climb 30 ft.  

| STR | DEX | CON | INT | WIS | CHA |
|:--:|:--:|:--:|:--:|:--:|:--:|
| 6 (-2) | 12 (+1) | 14 (+2) | 6 (-2) | 10 (+0) | 17 (+3) |

**Saving Throws** :: +6 Charisma  
**Skills** :: Deception +6  
**Damage Resistances** :: —  
**Languages** :: Understands trained commands  
**Infusions** :: 1 Health / 3 Magic; d6  
**Bond** :: One stable Genesis bond; one creature action; standing orders and GM loyalty apply  
**Proficiency Bonus** :: +3  

**Traits** :: Amorphous form; trained performances may include practical illusions within learned spell limits.

**Actions** :: **Vicious Mockery.** One creature action; one creature within 60 ft. that can hear Flubbs; DC 14 Wisdom save or 2d4 psychic damage and disadvantage on its next attack roll before the end of its next turn. Uses its existing learned cantrip ceiling.

**Known Magic** :: Cantrips: **Minor Illusion**, **Vicious Mockery**. Once/long rest: **Silent Image** (level 1), **Haunting Image** (level 2). New spell command for each casting.

**Reaction** :: **Distracting Mirage (2/long rest).** When a creature Flubbs can see makes a perceptible melee attack against Flubbs or an ally within 10 ft., spend its reaction before the roll to impose disadvantage on that one roll.

*Its illusions cannot automatically create extra concentration or an additional creature action.*

}}


<div class="wide stageGallery" style="height:230px"><img src="https://raw.githubusercontent.com/Omegaoliverid/Public-images/main/Genesis-Eggs/approved/flubbs-hatchling-juvenile.png" alt="flubbs hatchling juvenile"></div>

{{footnote GENESIS EGGS | EXAMPLE COMPANION: FLUBBS}}
{{pageNumber,auto}}

\page {production44,fp64}
{{monster,frame,wide
## Flubbs — Rainbow-slime
### Adult — example bonded player level 12
*Medium rainbow ooze, chaotic good*

**Armor Class** :: 15  
**Hit Points** :: 74 (level-based fixed Hit Die; see Growth, p. 7)  
**Speed** :: 40 ft., climb 40 ft.  

| STR | DEX | CON | INT | WIS | CHA |
|:--:|:--:|:--:|:--:|:--:|:--:|
| 6 (-2) | 14 (+2) | 14 (+2) | 6 (-2) | 10 (+0) | 20 (+5) |

**Saving Throws** :: +9 Charisma  
**Skills** :: Deception +9  
**Damage Resistances** :: —  
**Languages** :: Understands trained commands  
**Infusions** :: 1 Health / 3 Magic; d6  
**Bond** :: One stable Genesis bond; one creature action; standing orders and GM loyalty apply  
**Proficiency Bonus** :: +4  

**Traits** :: Amorphous form. Shapechanging is harmless disguise only unless paid for with an appropriate illusion spell.

**Actions** :: **Vicious Mockery.** One creature action; one creature within 60 ft. that can hear Flubbs; DC 17 Wisdom save or 3d4 psychic damage and disadvantage on its next attack roll before the end of its next turn. Uses its existing learned cantrip ceiling.

**Other Action** :: **Hypnotic Pattern (one level-3 casting).** Action; casts the SRD spell *Hypnotic Pattern* with a DC 17 Wisdom save. Uses its single level-3 casting and needs a fresh command.

**Known Magic** :: Cantrips: **Minor Illusion**, **Vicious Mockery**, **Message**. Two level-1 castings/day (**Silent Image** or **Disguise Self**), one level-2 (**Haunting Image**), one level-3 (**Hypnotic Pattern**, if learned).

**Reaction** :: **Distracting Mirage (3/long rest).** When a creature Flubbs can see makes a perceptible melee attack against Flubbs or an ally within 10 ft., spend its reaction before the roll to impose disadvantage on that one roll.

*This example emphasises distraction and performance, not lethal control.*

}}

{{monster,frame,wide
## Flubbs — Radiant-slime
### Ascended — example bonded player level 17
*Large rainbow ooze, chaotic good*

**Armor Class** :: 17  
**Hit Points** :: 104 (level-based fixed Hit Die; see Growth, p. 7)  
**Speed** :: 50 ft., climb 50 ft.  

| STR | DEX | CON | INT | WIS | CHA |
|:--:|:--:|:--:|:--:|:--:|:--:|
| 6 (-2) | 14 (+2) | 14 (+2) | 6 (-2) | 10 (+0) | 20 (+5) |

**Saving Throws** :: +11 Charisma  
**Skills** :: Deception +11  
**Damage Resistances** :: —  
**Languages** :: Understands trained commands  
**Infusions** :: 1 Health / 3 Magic; d6  
**Bond** :: One stable Genesis bond; one creature action; standing orders and GM loyalty apply  
**Proficiency Bonus** :: +6  

**Traits** :: No legendary actions, double concentration, invulnerability or unconditional extra turns.

**Actions** :: **Vicious Mockery.** One creature action; one creature within 60 ft. that can hear Flubbs; DC 19 Wisdom save or 3d4 psychic damage and disadvantage on its next attack roll before the end of its next turn. Uses its existing learned cantrip ceiling.

**Other Action** :: **Dream of Colour (one signature use/long rest).** Fifth-level-equivalent single-target illusion modelled on *Hold Monster*: one creature within 90 ft., Wisdom save DC 19 or paralysed; concentration up to one minute, repeat the save at each turn's end. It uses one normal creature action.

**Known Magic** :: Retains its Adult three cantrips and level-1-to-3 spell budget.

**Reaction (only if retained from Adult)** :: **Distracting Mirage (3/long rest).** Uses the Adult trigger, 10-ft. range and before-roll timing above; no additional off-turn defence is granted.

*The GM may permit a bonus-action *player command* for the signature only after exceptional mastery.*

}}


<div class="wide stageGallery" style="height:215px"><img src="https://raw.githubusercontent.com/Omegaoliverid/Public-images/main/Genesis-Eggs/approved/flubbs-adult-ascended.png" alt="flubbs adult ascended"></div>

{{footnote GENESIS EGGS | EXAMPLE COMPANION: FLUBBS}}
{{pageNumber,auto}}

\page {casefile,production45,fp65}

{{wide,chapterhead
##### EXAMPLE COMPANION · GENESIS EGG TRACKER
# Elysian, the Runic Hatchling
}}

{{wide,caseinfo
| | | | |
|:--|:--|:--|:--|
| Egg Name | “Elysian” | Aspect Chosen | Arcane |
| PC Name | Vinandi De Mimour (Halfling Wizard) | Campaign/Arc | “Shadow over Silverwood” |
}}

{{wide,trackerGrid
{{stage
#### Stage One – Initial Infusion
- **Trigger:** Egg is bound (1 level of exhaustion taken)
- **Sacrifice Type:** ☑ Hit Die ☐ Spell Slot (one currently available Hit Die expended)
- **Infusion Source:** Contact with Arcane magic, handled with gentle care, magnetic attention from Vinandi
- **Aspect Chosen:** Arcane (theme: force)
- **Notes:**
  - Initial reaction: Egg flickers with tiny sparks, faintly glowing, softly radiating arcane energy
  - Environmental influence: Held carefully by Vinandi in a magical hand, cradled gently in a library workspace
}}

{{stage
#### Stage Two – Sustained Care
- **Trigger:** Second sacrifice: expend an available resource; gain 1 exhaustion level
- **Sacrifice Type:** ☐ Hit Die ☑ Spell Slot (one currently available spell slot expended as bond deepened)
- **Care Method Detail:** ☑ Empathy ☐ Dreams ☑ Protective Urge ☑ Whispered Communication ☐ Sings to Egg ☐ Damages Egg ☐ Draws on Egg ☐ Ignores ☐ Other
  > “Gently reads aloud while eating bacon, with spells prepared, hoping the inside is a dragon, and imagining riding it one day”
- **Care Method Other Detail:** “Reading and nurturing during spell casting, dreams of a future adventure”
- **Care Frequency:** Daily during spell prep, while eating bacon
- **Notes on Physical/Magical Changes:**
  - Egg slightly glows brighter, scales on bonding side begin softening with a faint shimmer
}}

{{stage
#### Stage Three – Visualisation
- **Trigger:** Third sacrifice: expend an available resource; gain 1 exhaustion level
- **Sacrifice Type:** ☐ Hit Die ☑ Spell Slot (one currently available spell slot expended, deepening the bond)
- **PC Visualisation:**
  - **Name:** “Elysian” (the name she hopes for, and the birth name in her mind)
  - **Shape/Form Ideas:** Small rune-winged drakelet with luminous (force-resistive) scales, wings reminiscent of ancient runes, a keen inquisitive gaze
  - **Quirks or Emotions:** Curious, eager to learn, affectionate when read to, playful yet cautious around magic
- **Care Method Detail:** ☑ Empathy ☐ Dreams ☑ Protective Urge ☑ Whispered Communication ☐ Sings to Egg ☐ Damages Egg ☐ Draws on Egg ☐ Ignores ☑ Other
  > “Reads stories as she feeds it bacon, imagining it reading books on its own someday, whispering encouragements”
- **Care Method Other Detail:** “Loves to listen to her voice and watch the egg glow brighter”
- **Care Frequency:** Every day, during spell prep and casual reading time
- **Egg Response:** Glows with increasing intensity as it absorbs knowledge and magical energy
- **Notes:**
  - Growing curiosity and intelligence, beginning to mimic spell gestures or babbled runes
}}

{{stage
#### Stage Four – Naming & Birth
- **Trigger:** Fourth sacrifice: expend an available resource; gain 1 exhaustion level
- **Sacrifice Type:** ☐ Hit Die ☑ Spell Slot (one currently available spell slot expended for maturation)
- **Final Form Name:** **“Elysian”**
- **Infusion mix:** 1 Health / 3 Magic (d6); role: Noncombat/Utility (knowledge and study)
- **Care Score (1–10):** 9 (strong bond, shared learning)
- **Relationship Notes:** “Vinandi’s companion and apprentice, eager to learn and protect, reading books together in secret libraries”
- **Current Creature Hit Die:** ☐ d4 ☑ d6 ☐ d8 (d6 fixed for life)
- **Magical allowance:** 1 Health / 3 Magic (d6): at most **third-level** magic as an Adult under the daily casting limits.
- **Trait Notes:**
  - Curious, book-loving, force-influenced magical abilities, eager to grow and learn
- **Temperament Notes:**
  - Playful, inquisitive, loves bacon and stories, cautious but eager to grow
- **Visual Characteristic:**
  - Tiny rune-winged drakelet with glowing runic wings, shimmering scales with arcane symbols, big expressive eyes
}}
}}

{{footnote GENESIS EGGS | EXAMPLE COMPANION: ELYSIAN}}
{{pageNumber,auto}}

\page {production46,fp66}
{{monster,frame,wide
## Elysian — Runic Hatchling
### Hatchling — example bonded player level 3
*Tiny dragon (rune-winged drakelet), curious*

**Armor Class** :: 13  
**Hit Points** :: 20 (level-based fixed Hit Die; see Growth, p. 7)  
**Speed** :: 20 ft.; controlled glide only (see [Flight and Gliding](#p13))  

| STR | DEX | CON | INT | WIS | CHA |
|:--:|:--:|:--:|:--:|:--:|:--:|
| 6 (-2) | 12 (+1) | 14 (+2) | 14 (+2) | 12 (+1) | 10 (+0) |

**Saving Throws** :: +4 Intelligence  
**Skills** :: Arcana +4, Investigation +4  
**Damage Resistances** :: force  
**Languages** :: Understands Common and Draconic  
**Infusions** :: 1 Health / 3 Magic; d6  
**Bond** :: One stable Genesis bond; one creature action; standing orders and GM loyalty apply  
**Proficiency Bonus** :: +2  

**Traits** :: Loves books and bacon; learned knowledge is permanent.

**Actions** :: **Timid Bite.** Melee attack +3; 1d4 + 1 piercing.

**Known Magic** :: Cantrip: **Mage Hand**. Hatching does not automatically confer extra spells or second damaging cantrip.

*Knowledge and curiosity are strengths even without a strong attack.*

}}

{{monster,frame,wide
## Elysian — Runic Scholar
### Juvenile — example bonded player level 7
*Tiny dragon (rune-winged drakelet), neutral good*

**Armor Class** :: 15  
**Hit Points** :: 44 (level-based fixed Hit Die; see Growth, p. 7)  
**Speed** :: 30 ft.; short flight up to 20 ft. per turn; must land; may glide; no rider (see [Flight and Gliding](#p13))  

| STR | DEX | CON | INT | WIS | CHA |
|:--:|:--:|:--:|:--:|:--:|:--:|
| 6 (-2) | 12 (+1) | 14 (+2) | 17 (+3) | 12 (+1) | 10 (+0) |

**Saving Throws** :: +6 Intelligence  
**Skills** :: Arcana +6, Investigation +6  
**Damage Resistances** :: force  
**Languages** :: Speaks learned languages  
**Infusions** :: 1 Health / 3 Magic; d6  
**Bond** :: One stable Genesis bond; one creature action; standing orders and GM loyalty apply  
**Proficiency Bonus** :: +3  

**Traits** :: Can learn additional languages through meaningful study; this does not create free *Comprehend Languages*.

**Actions** :: **Force Nudge.** Ranged spell attack +6, range 60 ft.; 2d4 force damage, no automatic 10-foot push.

**Known Magic** :: Cantrips: **Mage Hand**, **Force Nudge**. Once/long rest: **Comprehend Languages** (level 1), **Detect Thoughts** (level 2). New command per spell.

*Minor harmless magical flickers are flavour, not automatic checks with advantage.*

}}

<div class="wide stageGallery" style="height:310px"><img src="https://raw.githubusercontent.com/Omegaoliverid/Public-images/main/Genesis-Eggs/approved/elysian-juvenile.png" alt="Elysian juvenile"></div>

{{footnote GENESIS EGGS | EXAMPLE COMPANION: ELYSIAN}}
{{pageNumber,auto}}
\page {production48,fp68}
{{monster,frame,wide
## Elysian — Arcane Archivist
### Adult — example bonded player level 12
*Medium dragon (rune-winged drakelet), neutral good*

**Armor Class** :: 17  
**Hit Points** :: 74 (level-based fixed Hit Die; see Growth, p. 7)  
**Speed** :: 30 ft., fly 50 ft.; cannot carry a rider (see [Flight and Gliding](#p13))  

| STR | DEX | CON | INT | WIS | CHA |
|:--:|:--:|:--:|:--:|:--:|:--:|
| 6 (-2) | 14 (+2) | 14 (+2) | 20 (+5) | 12 (+1) | 10 (+0) |

**Saving Throws** :: +9 Intelligence  
**Skills** :: Arcana +9, Investigation +9  
**Damage Resistances** :: force  
**Languages** :: Speaks languages genuinely learned  
**Infusions** :: 1 Health / 3 Magic; d6  
**Bond** :: One stable Genesis bond; one creature action; standing orders and GM loyalty apply  
**Proficiency Bonus** :: +4  

**Traits** :: Actual learned languages and researched texts remain known. No universal instant translation or blanket research advantage.

**Actions** :: **Force Nudge.** Ranged spell attack +9; 3d4 force damage, range 60 ft. Significant pushing must be a separate ability.

**Other Action** :: **Pocket Archive (one level-3 casting).** Action; 10-ft.-diameter study alcove on empty solid ground within 30 ft.; one hour, dry shelter and reading light for up to four willing Medium or smaller creatures. No combat cover, advantage, recovery, transport/storage, confinement or free casting. See [Arcane Techniques](#p71).

**Known Magic** :: Cantrips: **Mage Hand**, **Force Nudge**, **Prestidigitation**. Two level-1 castings/day (**Comprehend Languages** or **Runic Shield**), one level-2 (**Detect Thoughts**), one level-3 (**Pocket Archive**, if learned).

**Reaction** :: **Runic Shield (one level-1 casting).** Visible ally within 30 ft. hit by an attack: before damage, reaction grants +5 AC against that attack only. Requires a fresh direction to guard that ally, expiring at the start of the player’s next turn; casting spent only if triggered. Full rule: [Arcane Techniques](#p71).

*The archive is a meaningful signature utility choice, not a source of unlimited free casting.*

}}

{{monster,frame,wide
## Elysian — Runebound Archivist
### Ascended — example bonded player level 17
*Medium dragon (rune-winged drakelet), neutral good*

**Armor Class** :: 18  
**Hit Points** :: 104 (level-based fixed Hit Die; see Growth, p. 7)  
**Speed** :: 35 ft., fly 60 ft.; rider only with GM approval, suitable anatomy, size and capacity (see [Flight and Gliding](#p13))  

| STR | DEX | CON | INT | WIS | CHA |
|:--:|:--:|:--:|:--:|:--:|:--:|
| 6 (-2) | 14 (+2) | 14 (+2) | 20 (+5) | 12 (+1) | 10 (+0) |

**Saving Throws** :: +11 Intelligence  
**Skills** :: Arcana +11, Investigation +11  
**Damage Resistances** :: force  
**Languages** :: Speaks languages genuinely learned  
**Infusions** :: 1 Health / 3 Magic; d6  
**Bond** :: One stable Genesis bond; one creature action; standing orders and GM loyalty apply  
**Proficiency Bonus** :: +6  

**Traits** :: An exceptional scholarly Ascension; retains the same ordinary spell allowance and no automatic additional ASI.

**Actions** :: **Force Nudge.** Ranged spell attack +11; 3d4 force damage, range 60 ft. as Adult.

**Other Action** :: **Runebound Sanctuary (1/long rest).** Fifth-level-equivalent signature; action and fresh player command. Flat visible 10-by-10-ft. force barrier on ground within 30 ft.; concentration up to one minute, directional total cover only. No cage, dome, trapping, transport or damage. Ending and counterplay: [Arcane Techniques](#p71).

**Known Magic** :: Retains Adult cantrips, earned knowledge and limited level-1-to-3 castings.

**Reaction** :: **Runic Shield (one level-1 casting).** Visible ally within 30 ft. hit by an attack: before damage, reaction grants +5 AC against that attack only. Requires a fresh direction to guard that ally, expiring at the start of the player’s next turn; casting spent only if triggered. Full rule: [Arcane Techniques](#p71).

*No permanent immortality, automatic teleport from zero HP, or fifth-level repertoire beyond this single signature.*

}}


<div class="wide stageGallery" style="height:225px"><img src="https://raw.githubusercontent.com/Omegaoliverid/Public-images/main/Genesis-Eggs/approved/elysian-adult.png" alt="Elysian adult"></div>

{{footnote GENESIS EGGS | EXAMPLE COMPANION: ELYSIAN}}
{{pageNumber,auto}}

\page {rules,dense,mechanicsReference}
{{gmtab
GAME MASTER
}}

{{wide
# Elysian — Arcane Techniques

## Pocket Archive

**Pocket Archive (Action; one level-3 casting).** Create a visible 10-foot-diameter magical study alcove on unoccupied solid ground within 30 feet. It lasts for 1 hour, provides dry shelter and readable light, and accommodates up to four Medium or smaller willing creatures. It provides **no combat cover, automatic advantage, spell recovery, extradimensional transport/storage, confinement or free casting**. It ends if dispelled or its duration expires. The casting cannot be repeated without another permitted level-3 use.

## Runic Shield

**Runic Shield (Reaction; consumes one level-1 casting).** When an ally Elysian can see within 30 feet is hit by an attack, Elysian can use its reaction before damage to grant that ally **+5 AC against that triggering attack only**, potentially turning the hit into a miss. It does not protect against other attacks or grant a round-long AC increase. The bonded player must have freshly directed Elysian to guard that ally for this potential casting, using the command action/bonus action permitted by training. The direction expires at the start of the bonded player’s next turn whether triggered or not; each casting needs its own instruction. The casting is consumed only if the reaction triggers. Elysian has no extra reaction or level-1 casting beyond its existing budget.

## Runebound Sanctuary

**Runebound Sanctuary (Action; 1/long rest; fifth-level-equivalent Ascended signature).** Create one flat, visible 10-foot-wide by 10-foot-high barrier of magical force on ground within 30 feet for up to 1 minute (concentration). It grants total cover only through its area, cannot be shaped into a sphere/cage/dome, cannot trap or transport creatures, and ends when concentration breaks or it is dispelled. For Counterspell and Dispel Magic, treat this signature as a fifth-level spell: a fifth-level or higher casting succeeds automatically; a lower-level casting requires a DC 15 spellcasting-ability check. Counterspell must interrupt its creation; Dispel Magic targets the existing barrier. It does not deal damage and cannot be used as an attack. A new player command is required; the creature uses its action and its sole Ascended signature use.
}}

{{footnote GENESIS EGGS | RULES REFERENCE}}
{{pageNumber,auto}}
\page {production49,fp69}
{{wide,ascensionTitle
##### ELYSIAN
# The Runebound Archivist
}}

![](https://raw.githubusercontent.com/Omegaoliverid/Public-images/main/Genesis-Eggs/approved/elysian-ascended.png){position:absolute,top:95px,left:20px,width:754px,height:760px,object-fit:contain}

{{evo,evocap
#### Final Growth & Learning Progression

**Elysian's Development Progress:**

**Suggested GM story milestones:** Elysian learns languages through sustained study, practice and meaningful discoveries. Understanding a difficult ancient text may inspire Juvenile growth; a major breakthrough may inspire adulthood. Ascension needs an exceptional story event. Language totals and training points do not trigger evolution automatically.
}}

\page {production50,fp70}
![](https://raw.githubusercontent.com/Omegaoliverid/Public-images/main/Genesis-Eggs/final-2026-10-17/aspect-river.jpg){position:absolute,top:0px,left:0px,width:100%,height:100%,object-fit:cover,object-position:center}

{{partcap
##### PART FOUR
## Aspect Flavour Tables
Quirks, temperaments and possible futures for every Aspect. Flavour first: anything that would be a real power waits for the GM's approval.
}}

\page {aspectPage,rules,production51,fp71}

{{gmtab
GAME MASTER
}}

{{wide,chapterhead
# Aspect Flavour Tables
**GM Rule:** A roll suggests a visual quirk or possible future ability. Harmless details are free; consequential magic, attacks, defence and control must obey the creature's level, training, actions and spell budget. Nothing on this table is awarded automatically. 

These tables are narrative inspiration to help GMs flavour creatures touched by an Aspect; they are not free mechanical unlocks.  
**Roll a d6** or **choose manually** based on the egg’s theme, the player’s vibe, or dramatic story moments.

- **Trait**: A possible GM-approved trait or thematic hook if players haven’t defined one.
- **Temperament**: Personality flavour or roleplay cue.
- **Visual**: A cosmetic quirk or mutation—pure flavour, but great for narrative detail.
}}

{{wide,keyband
**Flavour first.** Roll a d6 or choose. Harmless details are free. Entries marked **◆** describe something that would be a real power: it is a *possible future ability*, never automatic. The GM approves it and charges it to the creature's level, training, actions and spell budget.
}}

{{aspect
#### Fire *(ELEMENTAL)*

| d6 | Trait                         | Temperament           | Visual                            |
|----|-------------------------------|------------------------|------------------------------------|
| 1 | ◆ Controls small flames | Impulsive             | Scorched markings         |
| 2 | ◆ Ignites in bursts when defeated | Competitive           | Glows like coal when angry        |
| 3 | Heats surroundings slightly | Aggressively loyal    | Fire-like flicker in their eyes   |
| 4 | ◆ Resistant to cold | Seeks constant action | Trails smoke when moving fast     |
| 5 | ◆ Can spark fire from nothing | Dramatic              | Hair/tail smolders in rhythm      |
| 6 | ◆ Breathes flammable jets | Hot-headed            | Ember cracks form along limbs     |
}}

{{aspect
#### Water *(ELEMENTAL)*

| d6 | Trait                           | Temperament         | Visual                          |
|----|----------------------------------|----------------------|----------------------------------|
| 1 | Body remains cool and wet | Peaceful            | Eyes shimmer like waves         |
| 2 | Melts into puddles when relaxed | Patient             | Skin ripples subtly             |
| 3 | ◆ Resistant to cold | Melancholic         | Misty form       |
| 4 | ◆ Heals more near water | Mysterious          | Liquid pulse beneath the skin   |
| 5 | Communes with aquatic life | Curious             | Gills open and close when calm  |
| 6 | ◆ Forms water whips when scared | Emotionally fluid   | Fin-like ears or frills         |
}}

{{aspect
#### Earth *(ELEMENTAL)*

| d6 | Trait                       | Temperament     | Visual                               |
|----|-----------------------------|------------------|---------------------------------------|
| 1 | ◆ Naturally armoured (+1 AC) | Steady          | Skin like stone or bark               |
| 2 | ◆ Can cause minor tremors | Stoic           | Pebbles fall from shoulders           |
| 3 | ◆ Resistant to knockback | Protective      | Moss patches or crystal growth        |
| 4 | Grows tougher over time | Grounded        | Cracks with glowing minerals inside   |
| 5 | Merges with soil to sleep | Quiet thinker   | Earthen tattoos shift when focused    |
| 6 | Clings to terrain easily | Determined      | Boulder-like knuckles or hooves       |
}}

{{aspect
#### Air *(ELEMENTAL)*

| d6 | Trait                        | Temperament         | Visual                              |
|----|------------------------------|----------------------|--------------------------------------|
| 1 | ◆ Weightless when focused | Free-spirited       | Hair floats, clothes flutter         |
| 2 | Gusts trail behind movement | Evasive             | Swirling winds follow them           |
| 3 | ◆ Resistant to fall damage | Aloof               | Feathers or wings partially form     |
| 4 | Can ride wind drafts | Energetic           | Constantly in motion                 |
| 5 | Whispers carry unnaturally | Cryptic             | Eyes reflect cloud shapes            |
| 6 | ◆ Controls minor air pulses | Chatty              | Breeze rustles around them indoors   |
}}

{{footnote GENESIS EGGS | ASPECT FLAVOUR TABLES}}
{{pageNumber,auto}}

\page {aspectPage,rules,production52,fp72}

{{gmtab
GAME MASTER
}}

{{wide,keyband
**Flavour first.** Roll a d6 or choose. Harmless details are free. Entries marked **◆** describe something that would be a real power: it is a *possible future ability*, never automatic. The GM approves it and charges it to the creature's level, training, actions and spell budget.
}}

{{aspect
#### Ice *(ELEMENTAL)*

| d6 | Trait                      | Temperament     | Visual                              |
|----|----------------------------|------------------|--------------------------------------|
| 1 | ◆ Randomly adds Cold damage to touch | Detached        | Frost trails along their steps       |
| 2 | ◆ Resistant to fire damage | Calculating     | Crystalline skin patterns            |
| 3 | Preserves objects/food from decay | Slow to act     | Frosted breath even when calm        |
| 4 | ◆ Can freeze surfaces | Quiet           | Icicle-like claws or spikes          |
| 5 | ◆ Shatters things when hit | Harsh when angered | Icy glare, snowflake pupils        |
| 6 | ◆ Forms frost armour (cold resistance) | Proud           | Pale, near-translucent skin    |
}}

{{aspect
#### Lightning *(ELEMENTAL)*

| d6 | Trait                         | Temperament     | Visual                             |
|----|-------------------------------|------------------|-------------------------------------|
| 1 | Sparks leap from body | Hyperactive     | Arcs of electricity crackle on limbs|
| 2 | ◆ Absorbs lightning harmlessly | Erratic         | Veins glow with electric current    |
| 3 | ◆ May develop bursts of speed | Twitchy         | Buzzing noise follows them          |
| 4 | ◆ May learn to dash further | Blunt           | Glowing rune-like lines        |
| 5 | ◆ Emits static field (+1 to Perception) | Reactive        | Fingers trail light as they move    |
| 6 | ◆ Lightning jump short distance | Flashy          | Sparks jump between facial features |
}}

{{aspect
#### Storm *(ELEMENTAL)*

| d6 | Trait                          | Temperament         | Visual                                  |
|----|-------------------------------|----------------------|------------------------------------------|
| 1 | ◆ Thunderous roar (like the Thunderwave spell) | Loud, boisterous     | Cloud-like mane or aura                  |
| 2 | ◆ Resistant to lightning & thunder | Wildly expressive    | Lightning forks beneath their skin       |
| 3 | Rain clings or follows | Melodramatic         | Eyes flicker with stormlight             |
| 4 | ◆ Critical hits boom with thunder | Stormy mood    |Cloud birthmark              |
| 5 | ◆ May develop faster flight | Dramatic             | Wings made of wind              |
| 6 | Body channels raw energy | Fiercely independent | Crackling halo when angry                |
}}

{{aspect
#### Celestial *(PLANAR/SPIRITUAL)*

| d6 | Trait                           | Temperament       | Visual                                 |
|----|----------------------------------|--------------------|-----------------------------------------|
| 1 | Emits calming presence | Gentle            | Halo-glow from crown                    |
| 2 | ◆ Resistant to radiant damage | Hopeful           | Golden feathers or skin shimmer         |
| 3 | ◆ Its light boosts healing on nearby allies | Self-sacrificing  | Glowing tears when hurt                 |
| 4 | Shines brighter in darkness | Protective        | Starburst pattern under eyes            |
| 5 | Truths randomly reveal themselves around them | Righteous         | Light motes orbit their head            |
| 6 | ◆ Breath weapon pulse holy light | Noble             | Skin glows in crescent moon shapes      |
}}

{{aspect
#### Infernal *(PLANAR/SPIRITUAL)*

| d6 | Trait                         | Temperament     | Visual                              |
|----|-------------------------------|------------------|--------------------------------------|
| 1 | ◆ Resistant to fire and charm | Spiteful        | Horn nubs or singed wings            |
| 2 | Emits oppressive heat | Smug            | Faint sulphurous aura                 |
| 3 | Can speak infernal tongues | Deceptive       | Eyes flare like burning coals        |
| 4 | Flames answer its anger | Vengeful        | Branded sigils on limbs              |
| 5 | ◆ Deals extra damage to set prey type | Arrogant        | Tail or tongue forked                |
| 6 | ◆ May learn Vicious Mockery | Snide           | Charred markings glow in darkness    |
}}

{{aspect
#### Fey *(PLANAR/SPIRITUAL)*

| d6 | Trait                            | Temperament    | Visual                                |
|----|-----------------------------------|----------------|----------------------------------------|
| 1 | ◆ Resistant to charm and illusions | Playful        | Flowers bloom where they step          |
| 2 | Communes with beasts or plants | Whimsical      | Butterfly wings or leafy hair          |
| 3 | ◆ Warps space slightly (+1 to Stealth) | Teasing        | Eyes sparkle like gemstones            |
| 4 | ◆ Glimpses between realms (+1 to Insight) | Flighty        | Glow changes with mood                 |
| 5 | ◆ Enchants with voice or music; may learn Calm Emotions | Seductive      | Motes of light swirl around them       |
| 6 | ◆ Teleports short distances | Trickster-ish  | Crown of vines or horns                |
}}

{{footnote GENESIS EGGS | ASPECT FLAVOUR TABLES}}
{{pageNumber,auto}}

\page {aspectPage,rules,production53,fp73}

{{gmtab
GAME MASTER
}}

{{wide,keyband
**Flavour first.** Roll a d6 or choose. Harmless details are free. Entries marked **◆** describe something that would be a real power: it is a *possible future ability*, never automatic. The GM approves it and charges it to the creature's level, training, actions and spell budget.
}}

{{aspect
#### Shadow *(PLANAR/SPIRITUAL)*

| d6 | Trait                       | Temperament     | Visual                               |
|----|-----------------------------|------------------|---------------------------------------|
| 1 | ◆ Resistant to necrotic | Brooding         | Shadows cling unnaturally             |
| 2 | Can dim nearby lights | Mysterious       | Eyes shine like moonlit voids         |
| 3 | ◆ Blends with darkness (+1 to Stealth) | Withdrawn        | Smoke trails when they move           |
| 4 | ◆ Cold presence (+1 cold damage on hits) | Morbidly curious | Constant whisper follows              |
| 5 | ◆ Emits fear in flashes | Quiet menace     | Drips ink-black tears when sad        |
| 6 | ◆ Becomes translucent (+1 to Stealth) | Dour             | Cloak of shadow, semi-permanent       |
}}

{{aspect
#### Undead *(PLANAR/SPIRITUAL)*

| d6 | Trait                         | Temperament     | Visual                               |
|----|-------------------------------|------------------|---------------------------------------|
| 1 | ◆ Resistant to poison/necrotic | Grim             | Bones show through flesh              |
| 2 | ◆ Doesn’t breathe or bleed | Cold             | Eyes glow with undeath                |
| 3 | ◆ Fearless | Unfeeling        | Skin looks waxy               |
| 4 | Communes with undead | Stoic            | Flickers between living/dead visage   |
| 5 | ◆ Clings to life (advantage on death saving throws) | Relentless       | Wisps of ghostlight escape mouth      |
| 6 | ◆ Hungers for Lifeforce | Detached         | Stitches   |
}}

{{aspect
#### Eldritch *(MAGICAL/ETHEREAL)*

| d6 | Trait                         | Temperament     | Visual                                  |
|----|-------------------------------|------------------|------------------------------------------|
| 1 | Sees hidden truths | Detached        | Extra blinking eyes or shifting limbs    |
| 2 | ◆ Resistant to mind magic | Alien           | Faint aura of distortion                 |
| 3 | Speaks random tongues | Obsessive       | Glyphs float behind them when thinking   |
| 4 | ◆ Warps probability slightly | Curious         | Tentacle motifs on skin                 |
| 5 | ◆ Randomly detects thoughts | Coldly logical  | Voice echoes strangely                   |
| 6 | ◆ Memory-leak illusions cast randomly around it | Emotionless     | Shadowed by void fractals                |
}}

{{aspect
#### Arcane *(MAGICAL/ETHEREAL)*

| d6 | Trait                         | Temperament     | Visual                             |
|----|-------------------------------|------------------|-------------------------------------|
| 1 | ◆ May learn two cantrips | Studious        | Runes orbit their body              |
| 2 | ◆ Enhances nearby magic (+1 to its spell attacks) | Inquisitive     | Crackles with raw arcane threads    |
| 3 | ◆ Immune to random magical effects | Focused         | Veins pulse with purple or blue light|
| 4 | ◆ Disrupts weak spells, die roll against hostile cantrips | Blunt           | Arcane lines glow when spell is near|
| 5 | ◆ May learn the Shield spell | Precise         | Cloaked in shimmer like glass       |
| 6 | ◆ Can store minor spells grows with creature | Calculating     | Eyes glow arcane when agitated      |
}}

{{aspect
#### Dream *(MAGICAL/ETHEREAL)*

| d6 | Trait                       | Temperament     | Visual                               |
|----|-----------------------------|------------------|---------------------------------------|
| 1 | Sleeps with eyes open | Imaginative      | Dream-mist trails when they move      |
| 2 | ◆ Invades dreams | Distant          | Eyes flicker like a starfield         |
| 3 | ◆ Resistant to psychic | Serene           | Hair floats like it’s underwater      |
| 4 | Reality flickers near them | Scatterbrained   | Unstable illusion trails              |
| 5 | ◆ Induces vivid hallucinations | Whimsical       | Sparkling dust follows them           |
| 6 | ◆ May learn Color Spray to show emotions | Cryptic          | Antennae or third eye manifests       |
}}

{{fig
![](https://raw.githubusercontent.com/Omegaoliverid/Public-images/main/Genesis-Eggs/final-2026-10-17/aspect-spirit.jpg){width:330px}
}}

{{footnote GENESIS EGGS | ASPECT FLAVOUR TABLES}}
{{pageNumber,auto}}

\page {aspectPage,rules,production54,fp74}

{{gmtab
GAME MASTER
}}

{{wide,keyband
**Flavour first.** Roll a d6 or choose. Harmless details are free. Entries marked **◆** describe something that would be a real power: it is a *possible future ability*, never automatic. The GM approves it and charges it to the creature's level, training, actions and spell budget.
}}

{{aspect
#### Chrono *(MAGICAL/ETHEREAL)*

| d6 | Trait                         | Temperament     | Visual                             |
|----|-------------------------------|------------------|-------------------------------------|
| 1 | ◆ Briefly slows time to react (+1 to Dexterity saves) | Patient         | Eyes tick like clocks               |
| 2 | ◆ Can replay recent moment, inspiring | Reflective      | Chrono sigils hover when active     |
| 3 | ◆ Immune to aging | Distant         | Faint time ripple trails follow     |
| 4 | ◆ Hastens or reverses small things; may learn Mending or Druidcraft | Obsessive       | Wears multiple watches or devices   |
| 5 | ◆ Exists slightly out of sync (+1 to Wisdom saves) | Calm            | Shifts between ghosting frames      |
| 6 | ◆ Speaks like echoing memory (+1 to Persuasion) | Detached        | Ancient hourglass mark on chest     |
}}

{{aspect
#### Illusion *(MAGICAL/ETHEREAL)*

| d6 | Trait                          | Temperament     | Visual                              |
|----|-------------------------------|------------------|--------------------------------------|
| 1 | ◆ Shifting disguises; may learn Disguise Self | Fickle          | Flickers between appearances         |
| 2 | ◆ Makes sound illusions | Jester-like     | Mask grows and changes expression    |
| 3 | ◆ Distorts their size at will | Unpredictable   | Eyes change colour randomly           |
| 4 | ◆ Disappears from memory briefly (+1 to Stealth) | Forgettable     | Skin patterns move like ink blots    |
| 5 | ◆ Inverts visibility (+1 to Stealth) | Secretive       | Cloak of glimmering refraction       |
| 6 | ◆ Mirror illusions split off (+1 AC) | Narcissistic    | Reflects others’ forms faintly       |
}}

{{fig
![](https://raw.githubusercontent.com/Omegaoliverid/Public-images/main/Genesis-Eggs/final-2026-10-17/aspect-seer.jpg){width:300px}
}}

{{aspect
#### Psionic *(MAGICAL/ETHEREAL)*

| d6 | Trait                        | Temperament     | Visual                               |
|----|------------------------------|------------------|---------------------------------------|
| 1 | ◆ Reads surface thoughts | Analytical      | Third eye or crystal in forehead      |
| 2 | ◆ Projects force barrier (+1 AC) | Protective      | Hair lifts when thinking hard         |
| 3 | ◆ Overwhelms weak minds; may learn Charm Person | Intense         | Eyes flare when concentrating         |
| 4 | ◆ Speaks telepathically | Quiet           | Voice reverberates even when silent   |
| 5 | ◆ Resistant to mind effects | Calculating     | Brain-like glow on upper spine        |
| 6 | Dreams influence reality | Weirdly calm    | Floating psychic motes around head    |
}}

{{aspect
#### Divination *(MAGICAL/ETHEREAL)*

| d6 | Trait                        | Temperament     | Visual                              |
|----|------------------------------|------------------|--------------------------------------|
| 1 | Sees glimpses of the future | Cryptic         | Irises shaped like hourglasses       |
| 2 | ◆ Warns of unseen danger | Nervous         | Tarot-style markings on arms         |
| 3 | Echoes alternate timelines | Absent-minded   | Ghost double flickers at times       |
| 4 | Guides others to answers | Cryptically kind| Carries glowing crystal or orb       |
| 5 | Interprets signs in chaos | Riddling        | Scrolls or glyphs swirl around       |
| 6 | ◆ Predicts movement in battle | Calm            | Halo of constellations over head     |
}}

{{aspect
#### Poison *(PHYSICAL/NATURAL)*

| d6 | Trait                          | Temperament    | Visual                                |
|----|-------------------------------|----------------|----------------------------------------|
| 1 | Drips venom when hurt | Grudge-holding | Eyes darken when agitated              |
| 2 | ◆ Resistant to toxins | Sly            | Venom sacs visible            |
| 3 | ◆ Touch causes mild nausea | Sharp-tongued  | Green tint to skin or claws            |
| 4 | ◆ Poisonous aura when angry | Cynical        | Emits toxic mist under pressure        |
| 5 | Craves rare herbs or fungi | Brooding       | Mushroom-like nodules on back          |
| 6 | ◆ Paralytic bite | Cold humour     | Tongue forked          |
}}

{{footnote GENESIS EGGS | ASPECT FLAVOUR TABLES}}
{{pageNumber,auto}}

\page {aspectPage,rules,production55,fp75}

{{gmtab
GAME MASTER
}}

{{wide,keyband
**Flavour first.** Roll a d6 or choose. Harmless details are free. Entries marked **◆** describe something that would be a real power: it is a *possible future ability*, never automatic. The GM approves it and charges it to the creature's level, training, actions and spell budget.
}}

{{aspect
#### Acid *(PHYSICAL/NATURAL)*

| d6 | Trait                         | Temperament     | Visual                                 |
|----|-------------------------------|------------------|-----------------------------------------|
| 1 | Body secretes mild acid | Irritable        | Skin constantly bubbles slightly        |
| 2 | ◆ Resistant to corrosion | Sarcastic        | Slime trails where they walk            |
| 3 | ◆ Acid blood burns attackers | Proud            | Craters on their armour or shell         |
| 4 | Corrodes metals slowly | Precise          | Translucent stomach or outer layer      |
| 5 | ◆ Emits foul acidic breath | Blunt            | Tongue glows acid green                 |
| 6 | Can digest anything | Curious          | Hollowed teeth or dribbling jaws        |
}}

{{aspect
#### Plant *(PHYSICAL/NATURAL)*

| d6 | Trait                          | Temperament     | Visual                              |
|----|-------------------------------|------------------|--------------------------------------|
| 1 | Photosynthesises in sun | Calm            | Leaves grow from hair or arms        |
| 2 | Communicates with flora | Nurturing       | Moss spreads as they rest            |
| 3 | ◆ Can root to heal | Patient         | Eyes glow green in sunlight          |
| 4 | ◆ Thorned in anger (+1 AC) | Gentle until provoked | Bark-like skin patches         |
| 5 | ◆ Releases spores for defence | Wise            | Blossoms open during emotions        |
| 6 | Seasons affect power | Moody           | Vines wrap around gear               |
}}

{{aspect
#### Beast *(PHYSICAL/NATURAL)*

| d6 | Trait                        | Temperament     | Visual                                 |
|----|------------------------------|------------------|-----------------------------------------|
| 1 | ◆ Heightened senses (+1 to Perception) | Instinctual      | Animalistic eyes and claws              |
| 2 | Growls when upset | Loyal            | Fur or scales in patches                |
| 3 | Natural predator reaction | Alpha-minded     | Canine/feline tail or snout             |
| 4 | Hunts best at night | Alert            | Elongated limbs or paws                 |
| 5 | Forms pack bonds | Protective       | Ear shape or call mimics beasts         |
| 6 | Can sniff magic/scent trails | Curious          | Prints glow faintly on certain ground   |
}}

{{aspect
#### Metal *(PHYSICAL/NATURAL)*

| d6 | Trait                          | Temperament     | Visual                                 |
|----|-------------------------------|------------------|-----------------------------------------|
| 1 | ◆ Skin like armour (+1 AC) | Blunt            | Metal plates or joints                  |
| 2 | ◆ Magnetically charged, can shield | Protective       | Floating metal bits orbit their body    |
| 3 | ◆ Resistant to slashing damage | Stubborn         | Joints click with clockwork movement    |
| 4 | Body rings when struck | Diligent         | Engraved with glowing smith marks       |
| 5 | Can reshape metal slightly | Methodical       | Metal claws or nails                    |
| 6 | ◆ Forger’s soul—mends others | Honourable        | Steam vents or smoke-chimney features   |
}}

{{aspect
#### Draconic *(MYTHIC/BLOODLINE)*


| d6 | Trait                                | Temperament     | Visual                                      |
|----|--------------------------------------|------------------|----------------------------------------------|
| 1 | ◆ Breathes elemental energy (faintly) | Proud           | Scaled patches shimmer with iridescence      |
| 2 | ◆ Resistant to fear or elemental magic | Regal           | Eyes are slitted like a true wyrm            |
| 3 | Hoards shiny or arcane objects | Territorial      | Horn nubs, growing fangs or tail             |
| 4 | ◆ Commands lesser creatures instinctively | Dominant    | Crest of bone or fin down their back         |
| 5 | ◆ Roars cause tremors or awe | Fierce           | Heat, mist, or sparks roll off their body    |
| 6 | Can sense magical lineage | Watchful         | Wings sprout briefly during emotion spikes   |
}}

{{gm
**Note for GMs:** These are narrative suggestions meant to inspire and reflect the draconic nature of the creature. Traits may echo ancestry (e.g., red for fire, blue for storm, etc.), and the visual details help highlight the draconic lineage.
}}

{{fig
![](https://raw.githubusercontent.com/Omegaoliverid/Public-images/main/Genesis-Eggs/final-2026-10-17/aspect-thorn.jpg){width:120px}
}}

{{footnote GENESIS EGGS | ASPECT FLAVOUR TABLES}}
{{pageNumber,auto}}

\page {production56,fp76}
![](https://raw.githubusercontent.com/Omegaoliverid/Public-images/main/Genesis-Eggs/final-2026-10-17/owl-companion-woodland.jpg){position:absolute,top:0px,left:0px,width:100%,height:100%,object-fit:cover,object-position:center}

\page {production57,fp77}

![](https://raw.githubusercontent.com/Omegaoliverid/Public-images/main/Genesis-Eggs/final-2026-10-17/first-bond.jpg){position:absolute,top:0,left:0,width:100%,height:100%,object-fit:cover}

{{wide,closing
# Companions That Shape the Story

A Genesis Egg gives the party a companion whose character grows through shared experience. Its form reflects the places it has been, the care it receives and the choices made around it.

The creatures you hatch are *not* pets, nor are they just tools. They are companions—individuals with quirks, instincts, and emergent identities. Some will bond fiercely, becoming loyal unto death. Others may struggle, grow jealous, or question their place beside the party.

As the GM, you are encouraged to give players **autonomy** in shaping these companions. Let them shape the path they hope their egg will follow; you decide when it is ready to evolve. These guides, tables, and examples offer **structure**, but are only that—structure, not limits.

These creatures are **manageable in mechanics**, but **unlimited in spirit**. They may become awakened beings, friends, mounts, or even rivals. One might die saving the party, or turn on them, or outlive them all. And one day, yes—perhaps your **Big Bad** was once a desperate soul who found an egg, and from it, forged a bond no mortal should have made.

**The story doesn’t end when the egg hatches.**  
It grows with the creature—*and your table will remember it.*
}}

{{footnote GENESIS EGGS | AFTERWORD}}
{{pageNumber,auto}}

\page {rules}
{{gmtab
GAME MASTER
}}

{{wide
# Threads from the Notebooks

Magister Var's journals end with questions he never answered. Each one can become an adventure.

## The Bag of Unhatched Eggs *(levels 3–6)*
A bag of holding full of unaligned Genesis Eggs appeared among Var's belongings with no delivery record. It is now sealed in the College archives. Someone sent it, and someone may want it back. Perhaps a rival scholar, or the bag's true owner, hires the party to recover it.

## Mirrith Beneath the Laboratory *(levels 7–10)*
Mirrith lies sealed in a chamber of glass and warded mirrors beneath Var's laboratory. Var once saw his reflection turn away before he did. When the wards begin to crack, the party must decide whether Mirrith is a prisoner, a danger, or both.

## The Places Somnius Shows *(levels 5–9)*
Somnius lives in dreams and has begun showing Var places he has never visited. One of those places turns out to be real. The party travels there to learn why a dream companion knows the way.

## Vexigar's Silver Spoon *(levels 2–5)*
Vexigar's infernal contract was dissolved, or so Var believes. Then the silver spoon Vexigar never returned turns out to belong to someone powerful who wants it back. Was the unbinding truly complete?

## Six Connections, One Scholar *(levels 11–16)*
Var’s six case files leave a tangle of lingering connections, not six stable bonds of the same kind. The strain is starting to show: interference, intrusions and old connections that never closed. The party may be asked to help him, or to stop what those connections are becoming.
}}

{{footnote GENESIS EGGS | THREADS FROM THE NOTEBOOKS}}
{{pageNumber,auto}}

\page {production58,fp78}
![](https://raw.githubusercontent.com/Omegaoliverid/Public-images/main/Genesis-Eggs/final-2026-10-17/training-party.jpg){position:absolute,top:0px,left:0px,width:100%,height:100%,object-fit:cover,object-position:center}
\page
![](https://raw.githubusercontent.com/Omegaoliverid/Public-images/main/Genesis-Eggs/approved/frog-hatchling.png){position:absolute,top:0px,left:0px,width:100%,height:100%,object-fit:cover}


\page {production59,fp79}

![](https://raw.githubusercontent.com/Omegaoliverid/Public-images/main/Genesis-Eggs/approved/kaelthos-colour.png){position:absolute,top:605px,left:85px,width:624px,height:420px,object-fit:contain,mix-blend-mode:multiply}

{{backpanel
# Genesis Eggs: Unlock the Extraordinary!

Four infusions begin the bond. What hatches depends on the egg’s Aspect, its surroundings and the care it receives. Follow Magister Othrelis Var’s notebooks, then use the training rules, worksheets and example companions to bring a new individual into your campaign.

##### Endless Possibilities
Record each infusion, choose a role and teach commands through play. The example companions show how different Aspects and care histories can shape a guardian, a magical striker or a creature that helps beyond combat.

##### The Stages of Creation
- **Initial Infusion:** Bind the egg with a sacrifice of your own strength—a Hit Die or a spell slot—and choose the Aspect that will shape it.
- **Sustained Care:** Provide active nurturing through sacrifice—either health or magical energy. Your bond deepens as you care for your egg.
- **Visualisation:** Imagine the creature’s form and intent. Your desires shape its development and abilities.
- **Naming & Birth:** Perform the final act of devotion and witness your creation as it hatches, beginning a bond shaped by care and shared experience.

Keep the companion’s tracker beside the character sheet. Use the field notes, growth rules and GM references to carry its history from the first infusion into later adventures.
}}

{{backfoot
FOR FIFTH-EDITION-COMPATIBLE GAMES
}}

<style>
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;0,700;1,500;1,600&family=Crimson+Pro:ital,wght@0,400;0,600;0,700;1,400&family=Inter:wght@400;500;600;700&display=swap');
/* GENESIS / IVORY ATLAS — reversible design layer, 21 October 2026 */
.page {color:#202e40;--HB_Color_HeaderText:#14283f;--HB_Color_HeaderUnderline:#a88b52;--HB_Color_HorizontalRule:#a88b52;--HB_Color_Accent:#e7e9e7;--HB_Color_CaptionText:#806b43;}
.page:after {display:none!important;}
.page:not(.rn):not(.diary) {font-family:'Crimson Pro',Georgia,serif;}
.page:not(.rn):not(.diary) h1,.page:not(.rn):not(.diary) h2,.page:not(.rn):not(.diary) h3 {font-family:'Cormorant Garamond',Georgia,serif!important;color:#14283f;font-variant:normal;letter-spacing:0;font-weight:600;}
.page:not(.rn):not(.diary) h1 {font-size:40px;line-height:1.02;border:0;}
.page:not(.rn):not(.diary) h2 {border-bottom:1px solid #b69b654d;}
.page:not(.rn):not(.diary) h4,.page:not(.rn):not(.diary) h5 {font-family:'Inter',sans-serif!important;color:#806b43;font-variant:normal;letter-spacing:.045em;}
.page:not(.rn):not(.diary) p,.page:not(.rn):not(.diary) li,.page:not(.rn):not(.diary) dl,.page:not(.rn):not(.diary) td {font-family:'Crimson Pro',Georgia,serif;}
.page:not(.rn):not(.diary) strong {font-weight:600;}
.page a {color:#244863;text-decoration-color:#a88b52;}
.page table tr:nth-child(odd) {background:#e9e9e2;}
.page table tr:nth-child(even) {background:transparent;}
.page table th {color:#14283f;border-bottom:1px solid #a88b52;}
.page .gm,.page .note {background:#e9eceb;border:0;border-left:2px solid #a88b52;box-shadow:none;}
.page .gm h5 {color:#14283f;}
.page .gmtab {background:#14283f;color:#f7f4eb;border-radius:0;border-bottom:2px solid #a88b52;font-family:'Inter',sans-serif;font-size:8px;letter-spacing:.14em;}
.page .ritual .step {border:0;border-top:2px solid #a88b52;background:#eeeee7;}
.page .ritual h4 {font-size:11px;letter-spacing:0;}
.page .ritual h4 em {font-family:'Inter',sans-serif;font-size:9px;color:#806b43;}
.page .stage {border:1px solid #b69b6560;border-left:2px solid #a88b52;background:#ffffff40;}
.page .stage h4 {font-size:10.5px;letter-spacing:.02em;}
.page .caseinfo td:nth-child(odd) {font-family:'Inter',sans-serif;font-size:9px;letter-spacing:.02em;color:#806b43;}
.page .evo,.page .keyband {background:#14283f;color:#f7f4eb;border-top:1px solid #a88b52;}
.page .evo h4,.page .keyband strong {color:#dbc596;}
.page .evo p,.page .evo li,.page .keyband p {color:#f7f4eb;}
.page .monster.frame.wide {background:#fffdf7;border:1px solid #b69b65;border-top:3px solid #14283f;box-shadow:none;}
.page .monster h2 {font-family:'Cormorant Garamond',serif!important;color:#14283f;border-color:#a88b52;}
.page .monster h3 {border-color:#a88b52;}
.page .monster hr {background:#a88b52;border-color:#a88b52;}
.page .partcap,.page .evo.evocap {background:rgba(15,32,51,.91);border-left:2px solid #c5a76c;}
.page .partcap h2 {color:#faf5e8!important;border:0;}
.page .partcap h5 {color:#d8c18e!important;}
.page .partcap p {color:#f7f4eb;}
.page .spellcard {background:#f7f4ebf2;border-top:3px solid #a88b52;}
.page .spellcard h5 {color:#14283f;}
.page .footnote {font-family:'Inter',sans-serif!important;font-size:7px;letter-spacing:.1em;color:#68707a;border-top:1px solid #b69b6566;padding-top:7px;bottom:24px;}
.page .pageNumber {font-family:'Inter',sans-serif;color:#14283f;font-size:10px;bottom:22px;}
.page .legal {color:#34414e;border-top:1px solid #a88b52;}
.page .toc h1 {font-size:43px;}
.page .toc h3 {font-size:18px;}
.page .toc h4 {font-family:'Crimson Pro',serif!important;font-size:13px;letter-spacing:0;}
.page:has(.frontCover) h1 {font-family:'Cormorant Garamond',serif!important;font-size:64px!important;font-weight:500!important;letter-spacing:.045em!important;color:#fff8e6!important;}
.page:has(.frontCover) h2 {font-family:'Cormorant Garamond',serif!important;font-style:italic;font-size:28px!important;color:#f7ead2!important;border:0;}
.page:has(.frontCover) .banner {font:11px 'Inter',sans-serif!important;letter-spacing:.22em!important;background:#14283f!important;border-top:1px solid #b69b65;border-bottom:1px solid #b69b65;}
.page:has(.frontCover) .footnote {background:rgba(15,32,51,.88)!important;font-family:'Crimson Pro',serif!important;}
.page.rn,.page.diary {color:#293447;}

.page.rn .hdr h1,.page.diary .yr h1,.page.diary .tp h1 {color:#14283f;}
.page.fp20 .notebookTitle h1,.page.fp21 .treatiseTitle h1 {font-family:'Cormorant Garamond',serif!important;color:#14283f;}
.page.fp20 .partcap {background:transparent;border-left:0;}
.page.fp20 .partcap p {color:#26384b;}
.page.fp21 .treatiseLetter {font-family:'Crimson Pro',serif;}
.page .backpanel {background:#14283ff0;border-color:#a88b52;}
.page .backpanel h1 {color:#f7f4eb!important;}
.page .backpanel p,.page .backpanel li {color:#f7f4eb;}
.page .backpanel h5 {color:#d8c18e!important;}
.page#p84 .backpanel h1 {color:#14283f!important;}
.page#p84 .backpanel p,.page#p84 .backpanel li {color:#26384b!important;}
.page#p64 .evo,.page#p72 .evo {background:#14283f!important;}
</style>

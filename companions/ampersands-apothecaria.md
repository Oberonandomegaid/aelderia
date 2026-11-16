<style>
/* =====================================================
   AMPERSAND'S APOTHECARIA — house style (Homebrewery V3, 5ePHB base)
   . A4 pages. Botanical folio: cream, deep plum, bronze, moss.
   ===================================================== */
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@500;700&family=Cormorant+Garamond:ital,wght@0,500;0,600;1,500&display=swap');

/* ---- A4 page size (print: paper A4, margins none, scale 100%, background graphics on) ---- */
.page { width: 210mm; height: 296.8mm; }
.page {
  --HB_Color_HeaderText: #4a1d3f;
  --HB_Color_HeaderUnderline: #9c7a3c;
  --HB_Color_HorizontalRule: #7a4a6b;
  --HB_Color_Accent: #ece4dc;
  --HB_Color_CaptionText: #5c4a2a;
}
.page h1 { font-family: 'Cinzel', serif; font-weight: 700; color: #4a1d3f; font-size: 0.8cm; line-height: 1.08em; margin-bottom: 0.18cm; }
.page h2 { font-family: 'Cinzel', serif; font-weight: 500; color: #5a2a4e; font-size: 0.52cm; line-height: 1.12em; }
.page h3 { color: #5a2a4e; font-size: 0.44cm; }
.page h4, .page h5 { color: #6b5320; }
.page * + h2 { margin-top: 0.34cm; }
.page * + h3 { margin-top: 0.28cm; }
.page h1 + p::first-letter { float: none; padding: 0; margin: 0; font-family: inherit; font-size: inherit; line-height: inherit; color: inherit; background-image: none; -webkit-background-clip: border-box; background-clip: border-box; }
.page h1 + p::first-line { font-variant: normal; }
.page { font-size: 0.355cm; }
.page p, .page ul, .page ol { line-height: 1.33em; }
.page table { width: 100%; font-size: 0.33cm; line-height: 1.28em; }
.page table th, .page table td { padding: 3px 6px; vertical-align: top; }
.page table td:first-child, .page table th { white-space: nowrap; }
.page table th { color: #4a1d3f; }
.page table + * { margin-top: 0.26cm; }
.page .note { border-left: 3px solid #9c7a3c; }
.page blockquote { break-inside: avoid; }

/* ---- Chapter band ---- */
.page .columnWrapper > .chapterhead:not(:first-child) { margin-top: 0.7cm; }
.page .chapterhead { border-bottom: 2px solid #9c7a3c; padding-bottom: 6px; margin-bottom: 12px; }
.page .chapterhead h5 { font-family: 'Cinzel', serif; color: #8a6a2c; letter-spacing: 0.16em; font-size: 0.28cm; margin: 0 0 2px; }
.page .chapterhead p { font-size: 0.37cm; line-height: 1.38em; }

/* ---- GM guidance (purple) — sparingly ---- */
.page .gm { break-inside: avoid; background: #ece3f2; border: 1px solid #bba6cf; border-left: 5px solid #5b3d8a; padding: 7px 12px; margin: 10px 0 12px; }
.page .gm h5 { font-family: 'Cinzel', serif; color: #3f2370; font-size: 0.31cm; letter-spacing: 0.05em; margin: 0 0 3px; }
.page .gm p, .page .gm li { font-size: 0.335cm; line-height: 1.32em; margin: 0; text-indent: 0; }
.page .gm p + p { margin-top: 4px; }

/* ---- Bronze reference panel ---- */
.page .panel { break-inside: avoid; border: 1px solid #c9b07a; border-top: 4px solid #9c7a3c; background: rgba(255,250,238,0.45); padding: 8px 12px 6px; margin: 6px 0 10px; }
.page .panel h3 { margin-top: 0.3cm; }
.page .panel table { font-size: 0.36cm; line-height: 1.45em; }
.page .panel td, .page .panel th { padding: 4px 8px; }
.page .panel p { font-size: 0.37cm; line-height: 1.45em; }
.page .panel h5 { font-family: 'Cinzel', serif; color: #8a6a2c; letter-spacing: 0.14em; font-size: 0.28cm; margin: 0 0 4px; }

/* ---- Two-column panel ---- */
.page .cols2 { column-count: 2; column-gap: 0.8cm; }
.page .cols2 h2 { column-span: all; }

/* ---- Three-card rows (delivery types, potion usage) ---- */
.page .trio { display: grid; grid-template-columns: repeat(3, 1fr); gap: 9px; margin: 6px 0 10px; }
.page .trio .card { background: rgba(255,255,255,0.32); border: 1px solid #cdb68a; border-top: 4px solid #4a1d3f; padding: 6px 9px 7px; break-inside: avoid; }
.page .trio h4 { font-family: 'Cinzel', serif; color: #4a1d3f; font-size: 0.33cm; margin: 0 0 4px; line-height: 1.15em; }
.page .trio p, .page .trio li { font-size: 0.32cm; line-height: 1.3em; margin: 0; }
.page .trio p + p, .page .trio ul + p, .page .trio p + ul { margin-top: 4px; }
.page .trio ul { padding-left: 1em; margin: 0; }

/* ---- Specimen plates ---- */
.page .plate { display: grid; grid-template-columns: 44% 1fr; gap: 14px; align-items: start; margin: 8px 0 6px; break-inside: avoid; }
.page .plate.rev { grid-template-columns: 1fr 44%; }
.page .plate.rev .pimg { order: 2; }
.page .plate .pimg p { margin: 0; }
.page .plate .pimg img { width: 100%; max-height: 400px; object-fit: cover; display: block; border: 1px solid #b9a27a; box-shadow: 0 2px 6px rgba(60,40,20,0.25); }
.page .plate h4 { font-family: 'Cormorant Garamond', serif; font-weight: 600; font-style: italic; color: #4a1d3f; font-size: 0.6cm; line-height: 1.25em; margin: 0 0 4px; }
.page .plate h5 { font-family: 'Cinzel', serif; color: #8a6a2c; letter-spacing: 0.16em; font-size: 0.26cm; margin: 0 0 6px; }
.page .plate p { font-size: 0.355cm; line-height: 1.38em; }
.page .strip { margin: 8px 0 6px; break-inside: avoid; }
.page .strip .pimg img { width: 100%; height: 255px; object-fit: cover; display: block; border: 1px solid #b9a27a; }
.page .strip .pimg p { margin: 0; }
.page .strip.short .pimg img { height: 150px; }
.page .strip.tall .pimg img { height: 400px; }
.page .strip h4 { font-family: 'Cormorant Garamond', serif; font-weight: 600; font-style: italic; color: #4a1d3f; font-size: 0.58cm; line-height: 1.25em; margin: 6px 0 4px; }
.page .strip h5 { font-family: 'Cinzel', serif; color: #8a6a2c; letter-spacing: 0.16em; font-size: 0.26cm; margin: 0 0 4px; }

/* ---- Plant tables ---- */
.page .flora table { font-size: 0.325cm; line-height: 1.26em; }
.page .flora td:first-child { white-space: nowrap; }
.page .flora td:nth-child(2) { white-space: nowrap; color: #5c4a2a; }
.page .tips { break-inside: avoid; border-left: 4px solid #6b7a3a; background: rgba(230,236,214,0.5); padding: 6px 12px; margin: 8px 0; }
.page .tips p, .page .tips li { font-size: 0.33cm; margin: 0; }
.page .tips ul { margin: 2px 0 0; padding-left: 1.1em; }

/* ---- Plant parts grid ---- */
.page .parts ol { columns: 3; column-gap: 26px; margin: 4px 0 8px; padding-left: 2em; }
.page .parts li { break-inside: avoid; font-size: 0.36cm; line-height: 1.35em; margin-bottom: 7px; }

/* ---- Recipe cards ---- */
.page .recipe { break-inside: avoid; border: 1px solid #c9b07a; background: rgba(255,250,238,0.5); margin: 0 0 12px; padding: 0 0 6px; }
.page .recipe h3 { margin: 0 0 6px; padding: 6px 12px; background: #4a1d3f; color: #f4e9d2; font-family: 'Cinzel', serif; font-size: 0.4cm; border: none; }
.page .recipe ul { margin: 0 12px; padding-left: 1.1em; }
.page .recipe li { line-height: 1.36em; }
.page .trio .card.recipe { padding: 0 0 6px; border-top: 1px solid #c9b07a; }
.page .trio .recipe h3 { font-size: 0.34cm; line-height: 1.2em; }
.page .trio .recipe ul { margin: 0 8px; }
.page .trio .recipe li { font-size: 0.31cm; line-height: 1.3em; margin-bottom: 3px; }

/* ---- Item card ---- */
.page .itemcard li { break-inside: auto !important; }
.page .figure { break-inside: avoid; margin: 8px 0; }
.page .figure p { margin: 0; }
.page .figure img { width: 100%; height: 470px; object-fit: cover; object-position: center 40%; display: block; border: 1px solid #b9a27a; box-shadow: 0 2px 6px rgba(60,40,20,0.25); }
.page .figure em { display: block; font-size: 0.3cm; color: #5c4a2a; margin-top: 4px; text-align: center; }
.page .itemcard { display: block; break-inside: auto !important; border: 2px solid #4a1d3f; background: rgba(255,250,238,0.55); padding: 8px 12px; margin: 6px 0 10px; }
.page .itemcard h3 { margin-top: 0; }

/* ---- Index and appendix ---- */
.page .idx table { font-size: 0.32cm; line-height: 1.2em; }
.page .idx td, .page .idx th { padding: 2px 5px; }
.page .idx td:first-child { white-space: normal; }
.page .idx h2 { font-size: 0.4cm; line-height: 1.2em; margin-bottom: 4px; }
.page .idx + .idx { margin-top: 0.3cm; }
.page .d100 table { font-size: 0.33cm; line-height: 1.28em; }
.page .d100 td:first-child, .page .d100 th:first-child { width: 0.9cm; text-align: center; font-family: 'Cinzel', serif; color: #4a1d3f; }

/* ---- Covers, front matter ---- */
.page .imprint { position: absolute; top: 0.9cm; left: 0; right: 0; text-align: center; font-family: 'Cinzel', serif; letter-spacing: 0.3em; font-size: 0.3cm; color: #f4e9d2; text-shadow: 0 0 6px #000, 0 0 3px #000; z-index: 3; }
.page .imprint p { margin: 0; }
.page .banner { background: #4a1d3f; color: #f4e9d2; font-family: 'Cinzel', serif; letter-spacing: 0.12em; }
.page .legal { position: absolute; width: auto !important; left: 1.4cm; right: 1.4cm; bottom: 1.5cm; border-top: 2px solid #9c7a3c; padding-top: 8px; font-size: 0.3cm; line-height: 1.35em; color: #3a2a20; }
.page .legal h5 { font-family: 'Cinzel', serif; color: #4a1d3f; font-size: 0.3cm; letter-spacing: 0.1em; margin: 0 0 4px; }
.page .legal p { margin: 0 0 4px; }
.page .toc li h3 { font-size: 0.5cm; margin-top: 0.3cm; }
.page .toc li h4 { font-size: 0.4cm; line-height: 1.4em; margin-bottom: 0.22cm; }
.page .tagpanel { position: absolute; left: 55px; width: 684px; box-sizing: border-box; bottom: 90px; padding: 14px 22px; background: rgba(30,14,28,0.80); border-left: 5px solid #c9a35a; z-index: 5; }
.page .tagpanel h3 { color: #f4e9d2; border: none; font-family: 'Cormorant Garamond', serif; font-style: italic; font-weight: 600; font-size: 0.62cm; margin: 0; line-height: 1.25em; }
.page .tagpanel h5 { color: #d8bd84; font-family: 'Cinzel', serif; letter-spacing: 0.2em; font-size: 0.28cm; margin: 8px 0 0; }
.page .partcap { position: absolute; left: 55px; bottom: 90px; width: 380px; padding: 14px 20px 13px; background: rgba(30,14,28,0.82); border-left: 5px solid #c9a35a; color: #f1e4c8; z-index: 5; }
.page .partcap h5 { color: #d8bd84; margin: 0; font-family: 'Cinzel', serif; font-size: 0.32cm; letter-spacing: 0.16em; }
.page .partcap h2 { color: #f6ead2; margin: 2px 0 6px; font-size: 0.95cm; border: none; }
.page .partcap p { color: #e8dcc0; font-size: 0.34cm; line-height: 1.35em; margin: 0; }
.page .footnote { bottom: 0.62cm; color: #5c4a2a; width: auto; max-width: 14cm; white-space: nowrap; }
.page .imprint p { display: inline-block; background: rgba(30,14,28,0.78); padding: 5px 16px; }
.page:has(.frontCover) .banner { background: #4a1d3f !important; background-image: none !important; -webkit-mask-image: none !important; mask-image: none !important; color: #f4e9d2 !important; font-size: 0.6cm !important; white-space: nowrap; width: auto !important; padding: 10px 30px 10px 1.6cm !important; border-right: 5px solid #c9a35a; }
.page:has(.frontCover) .banner::before, .page:has(.frontCover) .banner::after { display: none !important; }
.page:has(.frontCover) hr { background-image: none !important; border: none !important; border-top: 3px solid #c9a35a !important; height: 0 !important; -webkit-mask-image: none !important; mask-image: none !important; }

/* Apothecaria art direction — 18 October 2026. Scoped production layout. */
.page {background-color:#f5edda;}
.page h1 {letter-spacing:.015em;}
.page h2 {border-bottom-color:#ad8c54;}
.page table th {background:#4a1d3f;color:#fff4d9;padding:5px 6px;white-space:normal;}
.page table td {padding:4px 6px;}
.page table tr:nth-child(even) td {background:rgba(114,91,46,.055);}
.page .chapterhead {border-bottom:1px solid #9c7a3c;padding-bottom:10px;margin-bottom:15px;}
.page .chapterhead h5 {letter-spacing:.18em;margin-bottom:5px;}
.page .trio .card {border:none;border-top:3px solid #806637;background:rgba(255,251,238,.65);padding:10px;}
.page .trio h4 {font-size:13px;}
.page .gm {background:#efe4ed;border-left-color:#4a1d3f;}
.page .footnote {font-size:8px;letter-spacing:.05em;max-width:650px;bottom:24px;}
.page .pageNumber {bottom:24px;color:#775b29;}
.page .folioArt {column-span:all;margin:15px 0 0;}
.page .folioArt img {width:100%;height:260px;object-fit:contain;mix-blend-mode:multiply;}
.page .folioArt p {margin:0;}
.page:has(.frontCover) .frontCover h1,.page:has(.frontCover) .frontCover h2 {color:#fff3d8;text-shadow:0 2px 6px #170f07;}
.page:has(.frontCover) .frontCover h1 {font-family:'Cinzel',serif;font-size:44px;line-height:1.1;}
.page:has(.frontCover) .frontCover h2 {font-family:'Cormorant Garamond',serif;font-size:24px;letter-spacing:.04em;}
.page:has(.frontCover) .frontCover {z-index:3;}
.page:has(.frontCover) .frontCover .footnote {white-space:normal;max-width:none;left:65px;right:65px;background:#251a16c9;padding:12px;bottom:45px;color:#f9ecd3;font-size:13px;}
.page:has(.frontCover) .banner {left:60px!important;right:60px!important;bottom:135px!important;text-align:center;padding:12px!important;font-size:17px!important;}
.page.ap2 {background-color:#f1e2c3;}
.page.ap2 .advertTitle {position:absolute;top:70px;left:65px;right:65px;text-align:center;z-index:4;}
.page.ap2 .advertTitle h1 {font-size:31px;}
.page.ap2 .advertTitle h5 {letter-spacing:.18em;}
.page.ap2>img,.page.ap2 .columnWrapper>p>img {object-fit:contain!important;}
.page.ap3 .contentsArt {position:absolute;top:490px;left:95px;right:95px;}
.page.ap3 .contentsArt img {width:100%;height:240px;object-fit:cover;object-position:center;mask-image:linear-gradient(transparent,#000 12%,#000 88%,transparent);}
.page.ap3 .toc li h4 {font-size:14px;line-height:1.2;margin-bottom:7px;}
.page.ap3 .toc li h3 {font-size:18px;}
.page.ap4 .figure img {height:470px;object-fit:cover;}
.page.ap5 .harvestArt {position:absolute;right:55px;top:420px;width:315px;}
.page.ap5 .harvestArt img {width:100%;height:470px;object-fit:cover;object-position:40% center;mask-image:linear-gradient(transparent,#000 8%,#000 92%,transparent);}
.page.ap6 .panel table {font-size:13px;line-height:1.35;}
.page.ap7 .parts {border-top:1px solid #ad8c54;border-bottom:1px solid #ad8c54;padding:12px 0;}
.page.ap8 .figure img {height:290px;object-fit:contain;mix-blend-mode:multiply;box-shadow:none;border:none;}
.page.ap8 .itemcard {padding:10px 14px;border-width:1px;}
.page.ap9 table,.page.ap10 table,.page.ap11 table {font-size:12px;}
.page.ap10 .folioArt img {height:275px;}
.page.ap12 .trio .card.recipe h3 {color:#fff4d9;}
.page.ap13 .folioArt img {height:300px;object-fit:cover;mask-image:linear-gradient(transparent,#000 10%,#000 90%,transparent);}
.page.specimen .plate {grid-template-columns:47% 1fr;gap:24px;margin-top:22px;align-items:center;}
.page.specimen .plate.rev {grid-template-columns:1fr 47%;}
.page.specimen .plate .pimg img {height:490px;max-height:none;object-fit:contain;border:none;box-shadow:none;mix-blend-mode:multiply;}
.page.specimen .plate h4 {font-size:29px;border-bottom:1px solid #aa8850;padding-bottom:7px;}
.page.specimen .plate p {font-family:'Cormorant Garamond',serif;font-size:19px;line-height:1.35;}
.page.specimen .strip {display:grid;grid-template-columns:47% 1fr;gap:0 24px;align-items:start;margin-top:22px;}
.page.specimen .strip .pimg {grid-row:1/5;}
.page.specimen .strip .pimg img {height:440px!important;object-fit:contain;border:none;mix-blend-mode:multiply;}
.page.specimen .strip h4 {font-size:29px;margin-top:32px;}
.page.specimen .strip>p {font-family:'Cormorant Garamond',serif;font-size:19px;line-height:1.35;}
.page.plantlist .flora table {font-size:12px;line-height:1.25;}
.page.plantlist .flora td {padding:4px 6px;}
.page.plantlist .strip {display:grid;grid-template-columns:31% 1fr;gap:0 18px;margin-top:14px;align-items:start;}
.page.plantlist .strip .pimg {grid-row:1/5;}
.page.plantlist .strip .pimg img {height:240px!important;object-fit:contain;border:none;mix-blend-mode:multiply;}
.page.plantlist .strip h4 {margin-top:16px;font-size:25px;}
.page.plantlist .strip>p {font-family:'Cormorant Garamond',serif;font-size:16px;line-height:1.3;}
.page.plantlist .plate {grid-template-columns:31% 1fr;gap:18px;align-items:center;}
.page.plantlist .plate img {height:240px!important;object-fit:contain;border:none;mix-blend-mode:multiply;}
.page.plantlist .plate p {font-family:'Cormorant Garamond',serif;font-size:16px;}
.page.idxpage table {font-size:11.5px;line-height:1.18;}
.page.idxpage td {padding:2px 4px;}
.page.ap44 .merchantArt {column-span:all;margin-top:18px;}
.page.ap44 .merchantArt img {width:100%;height:430px;object-fit:cover;object-position:center 55%;mask-image:linear-gradient(transparent,#000 5%,#000 95%,transparent);}
.page.ap49 .mishapArt {position:absolute;right:55px;top:350px;width:315px;}
.page.ap49 .mishapArt img {width:100%;height:590px;object-fit:cover;object-position:center;mask-image:linear-gradient(transparent,#000 8%,#000 92%,transparent);}
.page .d100 table {font-size:12px;line-height:1.25;}
.page .d100 td {padding:3px 5px;}
/* Proof corrections: controlled widths and room for complete text. */
.page:has(.frontCover) h1 {font-family:'Cinzel',serif!important;font-size:44px!important;color:#fff3d8!important;text-shadow:0 2px 7px #130b05;}
.page:has(.frontCover) h2 {font-family:'Cormorant Garamond',serif!important;color:#fff3d8!important;font-size:25px!important;}
.page:has(.frontCover) .footnote {white-space:normal!important;max-width:none!important;left:65px!important;right:65px!important;width:auto!important;bottom:42px!important;padding:12px;background:#251a16d9;color:#fff0d2!important;font:italic 15px/1.4 'Cormorant Garamond',serif!important;}
.page.ap2 .advertTitle,.page.ap3 .contentsArt {width:auto!important;}
.page.ap2 .advertTitle h1 {font-size:29px;line-height:1.2;}
.page.ap8 .brewLayout {display:grid;grid-template-columns:1fr 1fr;gap:24px;align-items:start;}
.page.ap8 .brewLayout .itemcard {margin-top:0;}
.page.ap8 .figure img {height:360px;}
.page.ap10 .folioArt img {height:165px;}
.page.ap13 .folioArt img {height:150px;}
.page.plantlist .flora td {padding:3px 6px;}
.page.plantlist .strip .pimg img,.page.plantlist .plate img {height:210px!important;}
.page.plantlist .strip>p {font-size:15px;line-height:1.25;}
.page.ap44 .merchantArt img {height:290px;}
.page .d100 td {padding:2px 5px;}
.page.ap46 .d100 table {font-size:11.5px;line-height:1.22;}
.page.ap46 .d100 td {padding:1.5px 5px;}

/* Author polish pass: illustration-to-parchment transitions. */
.page.page .pimg img,.page.page .figure img,.page.page .folioArt img,.page.page .contentsArt img,
.page.page .harvestArt img,.page.page .merchantArt img,.page.page .mishapArt img {
 border:none!important;box-shadow:none!important;border-radius:0!important;
 -webkit-mask-image:radial-gradient(ellipse farthest-side at center,#000 76%,rgba(0,0,0,.88) 84%,rgba(0,0,0,.35) 94%,transparent 100%);
 mask-image:radial-gradient(ellipse farthest-side at center,#000 76%,rgba(0,0,0,.88) 84%,rgba(0,0,0,.35) 94%,transparent 100%);
 -webkit-mask-composite:source-over;mask-composite:add;
}
.page.specimen .pimg img {display:block;width:100%!important;height:auto!important;max-height:490px!important;mix-blend-mode:multiply;}
.page.plantlist .pimg img {display:block;width:auto!important;height:210px!important;max-width:100%;margin:auto;mix-blend-mode:multiply;}
.page.ap8 .figure img {display:block;width:100%!important;height:auto!important;max-height:none;}
.page.ap10 .folioArt img {display:block;width:auto!important;height:165px!important;margin:auto;}
.page.ap4 .figure img {mix-blend-mode:multiply;}
.page.ap2 {background-color:#f0e6cd;}
.page.ap2 .advertTitle {top:100px!important;left:92px!important;right:92px!important;}
.page.ap2 .advertTitle h5 {font-size:12px;letter-spacing:.25em;color:#826433;margin-bottom:21px;}
.page.ap2 .advertTitle h1 {font-family:'Cormorant Garamond',serif;font-size:51px!important;line-height:1.04!important;font-weight:600;font-variant:normal;text-transform:none;color:#49283c;}
.page.ap2 .advertTitle:after {content:'✧';display:block;margin:24px auto 0;color:#987339;font-size:25px;}
.page.ap2>img,.page.ap2 .columnWrapper>p>img {
 top:340px!important;left:14px!important;width:766px!important;height:auto!important;object-fit:contain!important;
 mix-blend-mode:multiply;border:none!important;box-shadow:none!important;
 -webkit-mask-image:radial-gradient(ellipse farthest-side at center,#000 76%,rgba(0,0,0,.88) 84%,rgba(0,0,0,.35) 94%,transparent 100%);
 mask-image:radial-gradient(ellipse farthest-side at center,#000 76%,rgba(0,0,0,.88) 84%,rgba(0,0,0,.35) 94%,transparent 100%);
 -webkit-mask-composite:source-over;mask-composite:add;
}
.page.ap2 .tagpanel {left:92px!important;right:92px!important;bottom:90px!important;width:auto!important;background:none!important;color:#49283c!important;box-shadow:none!important;border:0!important;border-top:1px solid #b09360!important;padding:22px 12px 0!important;text-align:center;}
.page.ap2 .tagpanel h3 {font-family:'Cormorant Garamond',serif;font-size:24px;line-height:1.25;font-weight:500;font-style:italic;color:#49283c!important;}
.page.ap2 .tagpanel h5 {font-size:9px;letter-spacing:.13em;color:#846535!important;margin-top:20px;}
/* Quiet finishing rules for reference pages with generous lower margins. */
.page.ap6 .panel {border:1px solid #b49764;background:rgba(255,252,241,.25);padding:15px;}
.page.idxpage:before {content:'';position:absolute;left:280px;right:280px;bottom:130px;height:1px;background:linear-gradient(90deg,transparent,#aa8952,transparent);}


/* Audit layout adjustments, 20 October 2026 */
.page.ap49 .mishapArt {position:relative;top:auto;right:auto;width:100%;column-span:all;margin:15px 0 0;}
.page.ap49 .mishapArt img {height:480px;object-fit:contain;}
.page.ap47 .d100 td,.page.ap48 .d100 td {padding-top:4px;padding-bottom:4px;}

.page.ap8 .figure img {height:230px!important;width:100%!important;object-fit:contain;}
.page.ap8 .itemcard {padding:5px 9px;}
.page.ap8 .itemcard p,.page.ap8 .itemcard ul,.page.ap8 .itemcard li {margin-top:0;margin-bottom:3px;line-height:1.2;}
.page.ap8 .itemcard h3 {margin-bottom:5px;}
.page.ap12 p,.page.ap12 li {margin-top:0;margin-bottom:4px;line-height:1.2;}
.page.ap12 .panel {padding:5px 9px;margin:4px 0;}
.page.ap12 .panel p {line-height:1.2;}
.page.ap12 .chapterhead {padding-bottom:5px;margin-bottom:7px;}
.page.ap12 table td,.page.ap12 table th {padding-top:2px;padding-bottom:2px;}
.page.ap13 .folioArt img {height:90px;object-fit:contain;}
.page.ap13 .folioArt {margin-top:5px;}
.page.ap13 p,.page.ap13 li {margin-top:0;margin-bottom:4px;line-height:1.2;}
.page.ap13 .panel {padding:5px 8px;margin:5px 0;}
.page.ap13 .panel td,.page.ap13 .panel th {padding:2px 5px;}
.page.ap13 .panel table {line-height:1.2;}
.page.ap14 .panel {padding:5px 8px;margin:4px 0;}
.page.ap14 .panel p {margin-bottom:4px;line-height:1.25;}
.page.ap14 .recipe {margin-bottom:5px;}
.page.ap14 .chapterhead {padding-bottom:5px;margin-bottom:8px;}
.page.ap16 .strip .pimg img {height:165px!important;}
.page.ap22 .strip .pimg img {height:120px!important;}
.page.ap22 .flora td {padding-top:2px;padding-bottom:2px;}
.page.ap22 .strip {margin-top:7px;}
.page.ap22 .strip h4 {margin-top:0;}
.page.ap47> .columnWrapper > h2,.page.ap48> .columnWrapper > h2,.page.ap49> .columnWrapper > h2 {column-span:all;}
.page.ap13 .gm {margin:0 0 5px;padding:5px 8px;}
.page.ap13 h2 {margin-top:5px;margin-bottom:5px;}
.page.ap13 ul {margin-bottom:3px;}
.page.ap13 li {margin-bottom:2px;}

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
.page#p66 .tagpanel h3 { font: normal 18px/1.25 'Crimson Pro', serif !important; }
.page#p21 p { text-indent: 0 !important; }
.page#p21 .optional-hopes { margin: 14px 0 !important; }
.page#p64 .evo h4 { color: #dbc596 !important; font-weight: 700 !important; }
.page#p2 .legal { line-height: 1.18 !important; font-size: 9px !important; }
.page#p66 .tagpanel { left: 37% !important; width: 56% !important; bottom: 60px !important; padding: 14px 18px !important; }
.page#p66 .tagpanel h3 { font-size: 16px !important; }
.page#p32 .pimg { clip-path: inset(0 0 2px 0); }
.page .zamp-inline { font: inherit !important; display: inline !important; }

</style>

{{frontCover}}

{{imprint
}}

# Ampersand's Apothecaria

## A Treatise on the Flora Arcana

___

{{banner AN APOTHECARY'S FIELD GUIDE}}

{{footnote
"Within every root, a secret. Within every petal, a power. The wilds speak, if one knows how to listen—and brew."
}}

![](https://raw.githubusercontent.com/Omegaoliverid/Ampersand-s-Apothecary/52ab9f0ae9aedf06de291046c81bc2611d183a48/apo-cover.jpg){position:absolute,top:0px,left:0px,width:100%,height:100%,object-fit:cover,object-position:center}

\page {ap2}
{{wide,advertTitle
##### THE TRAVELLING APOTHECARY
# A workshop, wherever the road leads.
}}

![](https://raw.githubusercontent.com/Omegaoliverid/Ampersand-s-Apothecary/52ab9f0ae9aedf06de291046c81bc2611d183a48/apo-producer.jpg){position:absolute,top:0px,left:0px,width:100%,height:100%,object-fit:contain,object-position:center}

{{tagpanel
### Master the harmony of opposing magic. Distil harm or healing.
### Let your concoctions shape the fate of your journey.
##### AMPERSAND'S PERFECTLY PORTABLE POP-UP POTION PRODUCER™
}}

\page {ap3}
{{toc,wide
# Contents

- ### Techniques
  - #### [{{ Foreword}}{{ 4}}](#p4)
  - #### [{{ The Art of Harvesting}}{{ 5}}](#p5)
  - #### [{{ Plant Parts and Harvesting}}{{ 7}}](#p7)
  - #### [{{ Brewing & Distilling}}{{ 9}}](#p10)
  - #### [{{ Binders & Catalysts}}{{ 10}}](#p11)
  - #### [{{ Complex Brewing and Harmony}}{{ 13}}](#p14)
  - #### [{{ Worked Recipes}}{{ 15}}](#p17)
- ### The Flora Arcana
  - #### [{{ The Fire-Bound Flora}}{{ 17}}](#p19)
  - #### [{{ The Cold-Bound Flora}}{{ 19}}](#p21)
  - #### [{{ The Storm-Touched Flora}}{{ 21}}](#p23)
  - #### [{{ The Deathrooted Flora}}{{ 23}}](#p25)
  - #### [{{ The Luminous Flora}}{{ 25}}](#p27)
  - #### [{{ The Mindwoven Flora}}{{ 27}}](#p29)
  - #### [{{ The Stonebound Flora}}{{ 29}}](#p31)
  - #### [{{ The Tideborn Flora}}{{ 31}}](#p33)
  - #### [{{ The Skyborne Flora}}{{ 33}}](#p35)
  - #### [{{ The Toxin-Touched Flora}}{{ 35}}](#p37)
  - #### [{{ Infernal Flora of the Damned}}{{ 37}}](#p39)
  - #### [{{ Eldritch Flora of the Beyond}}{{ 39}}](#p41)
  - #### [{{ Arcane-Touched Flora}}{{ 41}}](#p43)
- ### Reference
  - #### [{{ Rarity and Habitat Index}}{{ 43}}](#p45)
  - #### [{{ Conditions Glossary}}{{ 45}}](#p49)
  - #### [{{ Merchants, Availability and Price Guide}}{{ 47}}](#p51)
  - #### [{{ GM Quick Reference}}{{ 47}}](#p51)
  - #### [{{ Appendix: Unusual Potion Outcomes}}{{ 49}}](#p53)
  - #### [{{ Zoltan’s Experimental Preparations}}{{ 55}}](#p61)
  - #### [{{ The Field Journal of Zoltan Ambersand}}{{ 57}}](#p63)
}}

{{wide,contentsArt
![](https://raw.githubusercontent.com/Omegaoliverid/Ampersand-s-Apothecary/52ab9f0ae9aedf06de291046c81bc2611d183a48/apo-herbarium.jpg)
}}

{{wide,legal
##### CREDITS & LICENCE
**Ampersand's Apothecaria: A Treatise on the Flora Arcana.** Written and designed by Oberon & Omega. Illustrations: Oberon & Omega.

**Ampersand's Apothecaria** is an independent fifth-edition-compatible supplement.

This work includes material taken from the System Reference Document 5.1 (“SRD 5.1”) by Wizards of the Coast LLC and available at https://dnd.wizards.com/resources/systems-reference-document. The SRD 5.1 is licensed under the Creative Commons Attribution 4.0 International License available at https://creativecommons.org/licenses/by/4.0/legalcode.

Text and illustrations © 2026 Oberon & Omega. All rights reserved, except SRD 5.1 material, which remains under its licence.
}}

\page {ap4}
{{wide,chapterhead
##### AN APOTHECARY'S WELCOME
# Foreword
This tome is a compendium of the rare, volatile, and wondrous flora found across the realms. Designed for herbalists, alchemists, and daring adventurers alike, it offers guidance on harvesting, combining, and crafting potions from elemental and mystical plant parts. Each page is infused with practical knowledge and whispered lore—be it flameleaf gathered near a volcano’s edge or eldritch thorns found in forgotten dreams.
}}

{{wide
Within these pages, readers will find a complete system for harvesting plant material, including distinct parts—roots, stems, petals, spores, and more—each imbued with unique elemental or magical affinities such as fire, cold, poison, radiant or infernal. A clear brewing system governs how plants combine, when opposing magic must be harmonised, and what happens when a brew goes wrong.

Once gathered, ingredients can be used in the creation of a variety of alchemical concoctions, including:

{{trio
{{card
#### Drinkable Potions
Single-use draughts imbued with restorative or transformative effects.
}}
{{card
#### Thrown Potions
Volatile flasks that explode or release magical effects upon impact.
}}
{{card
#### Ointments
Thick alchemical pastes, applied to weapons or armour, granting a limited enhancement.
}}
}}

Whether you are seeking to brew a Dawnsroot draught to mend wounds, craft a volatile Charpod bomb, or coat your blade with Phantom Thorn, this compendium will serve as your guide. The world’s wilds are full of power waiting to be distilled—if you have the skill, the knowledge, and the will to wield it.
}}

{{wide,strip,tall
{{pimg
![](https://raw.githubusercontent.com/Omegaoliverid/Ampersand-s-Apothecary/52ab9f0ae9aedf06de291046c81bc2611d183a48/apo-counter.jpg)
}}
}}

{{footnote AMPERSAND'S APOTHECARIA | FOREWORD}}
{{pageNumber,auto}}

\page {ap5}
{{wide,chapterhead
##### TECHNIQUES · I
# The Art of Harvesting
}}

{{wide,gm
##### The Apothecaria Principle
Clear rules give adventurers something to master, not a cage to restrict their ideas. Let players explore unusual recipes and earn meaningful results. The GM decides what can exist in the world and may bend a rule when the table's story warrants it. Do not erase several sessions of careful effort with an arbitrary, unrewarding outcome.
}}

## Locating Flora: 5d20 Discovery

Search within an appropriate habitat, typically **30–60 minutes per search**. Roll **5d20** as one discovery roll. The player may name an eligible plant they hope to find before rolling; otherwise the GM selects one from that biome. Compare the total to that plant's target. Nature, Survival, tools, character knowledge and spells can guide where to search or what might be present, but do not impose a mandatory second locating roll.

| Suggested rarity | Discovery target |
|---|---:|
| Common | 15 |
| Uncommon | 45 |
| Rare | 60 |
| Ultra Rare | 75 |
| Legendary | 90 |

**Plants found in one search = floor(5d20 total / chosen plant's current discovery target).** Each plant is a distinct specimen; finding it does not automatically yield a handful. If no plant was named, the GM may select one suitable species after seeing the total. A 65 does not grant every rarity that it exceeds; it might reveal four Common plants, one Uncommon plant or one Rare plant, depending on the chosen species.

### Casual foraging

Resolve the whole discovery roll against the target in force at its start. Then increase the target for the **next search of that species in that patch** by **+5 for each specimen found**. Do not raise the target while counting specimens from the same roll. Stop searching the patch when a roll discovers zero plants. For a short campsite forage, the GM may alternatively cap ordinary searching at three attempts. A genuinely new region or new viable patch starts afresh at its normal target.

### Dedicated gathering quest

A deliberate expedition uses the same method but increases the local target by only **+1 per plant found**. Do **not** impose the casual three-search cap: keep searching until the first zero or until the GM judges the patch depleted. **The normal roll is 5d20, including groups of fewer than five. Only a genuinely cooperating six-person gathering party uses 6d20; an appropriate NPC counts only with express GM approval.** Apply the +1 increase after counting the entire discovery roll, before the next search. Story clues, special habitats, quest rewards and multiple patches can make rare objectives achievable; a single Legendary patch is not meant to be a reliable harvest.

{{harvestArt
![](https://raw.githubusercontent.com/Omegaoliverid/Ampersand-s-Apothecary/52ab9f0ae9aedf06de291046c81bc2611d183a48/apo-harvest.jpg)
}}

{{footnote AMPERSAND'S APOTHECARIA | THE ART OF HARVESTING}}
{{pageNumber,auto}}

\page {ap6}
{{wide,panel
##### OPTIONAL GM REFERENCE
## Discovery Benchmarks
These probabilities describe **discoveries before any harvest check**. They are not guarantees or restrictions. Figures model one eligible plant species in one patch and repeated searching until the first zero, without the casual optional three-attempt cap.

### Casual foraging (5d20, +5 target per specimen)

| Rarity | Target | Avg. plants discovered | Chance of at least 2 |
|---|---:|---:|---:|
| Common | 15 | 6.76 | 99.92% |
| Uncommon | 45 | 1.41 | 42.88% |
| Rare | 60 | 0.36 | 5.42% |
| Ultra Rare | 75 | 0.045 | 0.073% |
| Legendary | 90 | 0.0009 | <0.001% |

### Dedicated gathering (target +1 per specimen)

| Rarity | Target | 5d20 average | 6d20 average |
|---|---:|---:|---:|
| Common | 15 | 22.998 | 31.104 |
| Uncommon | 45 | 2.114 | 5.273 |
| Rare | 60 | 0.406 | 1.293 |
| Ultra Rare | 75 | 0.046 | 0.262 |
| Legendary | 90 | 0.001 | 0.030 |

### Probability of completing a discovery goal within one patch

| Quest discovery goal (one patch) | 5d20 party | 6d20 party |
|---|---:|---:|
| 10 Common | 98.029% | 99.792% |
| 3 Uncommon | 34.410% | 70.747% |
| 5 Uncommon | 13.761% | 51.555% |
| 1 Rare | 29.879% | 59.549% |
| 2 Rare | 8.156% | 33.854% |
| 1 Ultra Rare | 4.414% | 21.248% |
| 1 Legendary | 0.094% | 2.968% |
}}

{{wide
*GM note:* A very rare herb may instead be found as quest treasure, purchased from an exceptional specialist, obtained by barter or awarded through play. Rarity describes expected access, not a prohibition. Plant rarity measures how hard an ingredient is to obtain; it is separate from magic item rarity.
}}

{{footnote AMPERSAND'S APOTHECARIA | THE ART OF HARVESTING}}
{{pageNumber,auto}}

\page {ap7}
{{wide,chapterhead
##### TECHNIQUES · II
# Plant Parts and Harvesting
Each flora may yield one or more of the following parts. These parts define how the plant is harvested, what tools are most effective, and what alchemical properties it carries.
}}

{{wide,parts
## Plant Parts Index
1. **Root** – Typically deep within the soil; often stable, grounding, or restorative in nature.
2. **Stem** – The structural carrier of energy and growth; may hold volatile or conductive traits.
3. **Leaf** – Broad absorbers of light and magic; commonly used in salves and healing draughts.
4. **Petal** – Often delicate and potent; usually tied to sensory or emotional effects.
5. **Flower (Whole)** – A composite of several parts; may provide dual effects or more powerful essences.
6. **Seed** – Dormant power; useful for delayed effects, growth potions, or explosive concoctions.
7. **Berry** – Encapsulated effects; often consumed raw or used in ingestible potions.
8. **Bark** – Tough and resilient; used in protective salves or elemental resistance mixtures.
9. **Sap** – Fluid essence; sticky, reactive, and often magical in nature.
10. **Thorn** – Sharp and dangerous; ideal for weapon poisons or harm-based effects.
11. **Vine** – Flexible and connective; can be used for binding, entangling, or longevity effects.
12. **Spores** – Found in fungi; can be hallucinogenic, toxic, or dispersal-based in thrown potions.
13. **Resin** – Hardened sap; slow-forming and stable, often used in enchantments or preservative potions.
14. **Bulb** – A swollen storage organ; rich in nutrients or magic, often used in transformation potions.
15. **Pod** – Protective casing around seeds or spores; may burst, carry defensive magic, or be thrown.
}}

## Identifying and Harvesting

An experienced character automatically recognises plants already known to them. For unfamiliar plants, allow Nature, Arcana, Medicine or suitable tools; on a failed identification check, give a partial clue rather than stopping the game. Raw ingredients usually need brewing and a binder to yield their intended effect; tasting or applying them directly may have a weaker, strange or adverse result at GM discretion.

**Harvest DC = 10 + 1d10**, rolled secretly or openly. Select a specific plant part. A harvesting check may use Nature, Survival or appropriate tools; add proficiency only once, under the rules of the game being played. Every distinct specimen permits one attempt, normally taking 1–5 minutes.

| Harvest check result | Outcome |
|---|---|
| Natural 20 | Always succeeds: two handfuls |
| Meets or beats DC | One handful |
| Fails DC by 1–9 | No usable material |
| Fails DC by 10+ | No usable material; GM applies listed severe-harvest consequence |

Ordinary harvest failure consumes the attempt; do not repeatedly retry the same specimen. The GM may permit an exceptional second attempt or alter difficulty for especially fragile or hazardous plants. **Rarity affects finding the plant, not the basic harvest DC.**

{{wide,gm
##### Known patches and harvest hazards
**Known gathering sites.** If the party has followed reliable directions to a known, reachable patch, the GM may treat discovery as assured. Each specimen still needs its harvest check, and local hazards and guardians remain.

**Missing saves.** Where a severe harvest consequence gives no saving throw, the GM grants a DC 12 save using the ability that fits the effect. Printed saving throws take precedence. The save does not make the failed harvest successful. A natural 1 on a harvest check has no special effect; compare the total to the DC as normal.

**Unlisted recovery.** When a harvest consequence omits a duration, recovery condition or cleansing method, the GM determines it using applicable game rules, the glossary and suggested durations where appropriate. Printed entry-specific rules take priority; do not assume an unstated permanent penalty.
}}

{{footnote AMPERSAND'S APOTHECARIA | PLANT PARTS AND HARVESTING}}
{{pageNumber,auto}}

\page {ap8}
![](https://raw.githubusercontent.com/Omegaoliverid/Ampersand-s-Apothecary/52ab9f0ae9aedf06de291046c81bc2611d183a48/apo-producer.jpg){position:absolute,top:0px,left:0px,width:100%,height:100%,object-fit:cover}

\page
{{wide,chapterhead
##### TECHNIQUES · III
# Brewing & Distilling
## Methods of Brewing

Brewing potions requires a controlled environment, appropriate equipment, and careful measurement of harvested materials. There are two main methods of potion crafting available to adventurers:
}}

{{wide,brewLayout
{{brewLeft
### 1. **Alchemy Labs (Towns & Cities)**

Alchemists and herbalists often maintain workshops with the proper gear for potion creation.

- **Access**: Available in most towns, guild halls, or arcane colleges.
- **Fee**: Determined by the GM (typically 10–50 gp per potion brewed).
- **Containers**: Suitable vials, flasks and jars are included in the fee. Ingredients and binders are not.
- **Capacity**: Brew up to **3 potions** simultaneously with the right workspace.
- **Perks**: Safe, efficient, and supported by local experts or assistants. At the GM's discretion, a well-equipped lab gives advantage on the final brewing check.

{{figure
![](https://raw.githubusercontent.com/Omegaoliverid/Ampersand-s-Apothecary/52ab9f0ae9aedf06de291046c81bc2611d183a48/apo-producer.jpg)

*The Pop-Up Potion Producer, mid-unfurl.*
}}

}}
{{itemcard
### 2. **Ampersand’s Perfectly Portable Pop-Up Potion Producer™**

A rare magical item designed for mobile herbalists and apothecaries on the go.

- **Item Type**: Wondrous Item (Rare), no attunement required
- **Weight**: 5 lb when folded
- **Appearance**: A magical satchel sealed by a mechanism holding a large, gemmed ampersand-shaped clasp.

#### **Activation**
Upon placing the satchel flat and activating the gem:
- The bag unfurls, opens impossibly wide, and from its depths rises a **portable apothecary station**, complete with brewing gear and heating mechanisms. 5ft by 5ft cube.
- Opening the station and folding it away each take one action. It requires a clear 5-foot cube. It cannot fold while a creature occupies it; only its equipment, ingredients and brews are stowed. The station vanishes back into the bag when the clasp is resecured.

#### **Functionality**
- **Base Capacity**: Brew **1 potion** at a time.
- **Upgradeable**:
  - Tier 2: Brew **2 potions** at once.
  - Tier 3: Brew **3 potions** at once.
  - Upgrades may be commissioned from specialist apothecaries or earned through quests, experimentation and arcane tinkering; no compulsory ingredient list. A failed upgrade might waste components, cause a malfunction or reveal something useful, rather than automatically destroying the station.
  - Each brewing slot tracks its own time, so two different recipes can progress simultaneously.
  - The station supplies a suitable vial, flask or jar for each finished brew. It cannot produce empty containers on their own.
  - When folded away, the station’s pocket dimension slows or pauses time: unfinished brews keep their state but normally make no progress until reopened. The GM may grant special upgrades that permit progress while closed.
}}

}}

{{footnote AMPERSAND'S APOTHECARIA | BREWING & DISTILLING}}
{{pageNumber,auto}}

\page {ap9}
{{wide
## Brewing Rules

A recipe uses **1–3 handfuls** of plant ingredients and exactly **1 binder**. One finished brew normally produces **one** potion, throwable flask or ointment container. Three handfuls produce a stronger **single** recipe, not three separate bottles. A natural 20 on the final brewing check may inspire a creative flourish or, exceptionally, allow the GM to divide a concentrate into two finished portions.

| Ingredients + binder | Brewing time | Base brewing DC |
|---|---:|---:|
| 1 handful + 1 binder | 16 hours | 10 |
| 2 of the same plant + 1 binder | 24 hours | 12 |
| 2 different plants + 1 binder | 24 hours | 15 |
| 3 of the same plant + 1 binder | 32 hours | 14 |
| 2 of one, 1 different + 1 binder | 32 hours | 17 |
| 3 different plants + 1 binder | 32 hours | 20 |
}}

Brew time represents downtime and can be paused between stages; continuous hands-on attention is not required. The GM decides when specific steps need active supervision. The ingredients are consumed once brewing begins, whether the final mixture succeeds or fails; exceptional salvage is the GM's choice. Finished potions keep indefinitely if suitably stored, except if their effect is intentionally unstable.

The player describes the intended effect before committing ingredients. The GM helps translate plant properties, binder and investment into a reasonable result. Players may instead deliberately experiment without knowing what they will produce. Increasing one plant's quantity can enhance duration or add a thematic nuance, not automatically multiply every effect. A rare creation may be as potent as a useful spell; scarcity, time and limited quantity—not arbitrary weakening—are the main balancing tools.

For final checks and Harmony, see **Complex Brewing and Harmony** following the binder tables.

*Spring Water, Spirit Resin and Witchhazel Salve are the Common drinkable, throwable and ointment binders in the catalogue below.*

{{wide,chapterhead
##### TECHNIQUES · IV
# Binders & Catalysts
}}

## What Are Binders?

Binders are the alchemical mediums that unify and stabilise potion ingredients. Without a binder, plant matter cannot be distilled into a usable form. Binders determine how a potion is **delivered** (drunk, thrown, applied), influence its **effect stability**, and may **enhance or diminish** the properties of the ingredients used.

Each binder falls into one of three major categories:
- **Drinkable Binders** – Used in potions consumed by the user.
- **Throwable Binders** – Used for potions that are cast like grenades.
- **Ointment Binders** – Used to create salves, oils, and coatings for gear or skin.

## Drinkable Binders (1 use)

These are safe (or mostly safe) to drink and are used in restorative, buffing, or magical effect potions.

{{wide
| Name              | Type         | Traits & Notes                                                                 |
|-------------------|--------------|--------------------------------------------------------------------------------|
| **Spring Water** (C) | Water | Neutral base; stabilises healing and nature-based effects. Common and accessible. |
| **Dwarven Ale** (U) | Alcohol | Boosts physical buffs (STR, CON); causes slight intoxication. |
| **Elven Wine** (U) | Alcohol | Enhances mental/magical buffs (INT, CHA); smooth aftertaste. |
| **Moondew** (U) | Distilled Dew | Enhances lunar, dream, or celestial effects. Only collectable under moonlight. |
| **Tincture of Ash** (U) | Spirit Mix | Stabilises fire and smoke-based ingredients. Bitter and warm. |
| **Twilight Tea** (U) | Herbal Infusion | Enhances stealth, illusion, or shadow-based ingredients. |
| **Sunroot Juice** (U) | Herbal Juice | Amplifies plant-based effects; boosts vitality and photosynthesis magic. |
| **Ironbark Extract** (U) | Sap Tonic | Reinforces defence potions; slightly metallic taste. |
| **Void Milk** (R) | Planar Dairy | Enhances psychic or eldritch effects. Slightly disturbing to consume. |
| **Dragonbone Broth** (R) | Magical Broth | Greatly extends duration of strength and endurance buffs. Hard to obtain. |
| **Rivergold Mead** (R) | Sweet Alcohol | Adds minor regeneration (1 HP at the start of each of the drinker's turns for 1 minute; doses don't stack). Used in minor health potions. |
| **Spectral Cordial** (R) | Spirituous Essence | Used for potions that interact with ghosts, undead, or astral forms. |
}}

{{footnote AMPERSAND'S APOTHECARIA | BINDERS & CATALYSTS}}
{{pageNumber,auto}}

\page {ap10}
## Throwable Binders (1 use)

Highly volatile or reactive, these binders determine the **range**, **spread**, and **impact** of thrown potions. The type of binder affects whether the potion targets a single enemy or explodes into an area-of-effect (AoE).

{{wide
| Name                | Type               | Traits & Notes                                                                 | Effect Radius |
|---------------------|--------------------|--------------------------------------------------------------------------------|----------------|
| **Spirit Resin** (C) | Flammable Oil | Stable and commonly used; carries fire well. Basic explosive spread. | 5 ft radius |
| **Volatile Spirits** (U) | Distilled Alcohol | Boosts flame, thunder, and explosive reactions. Dangerous to store. | 10 ft radius |
| **Troll Spit** (U) | Slime | Sticky, causes lingering effects. Ideal for poison or acid effects. | Single Target |
| **Greenglass Oil** (U) | Alchemical Glass | Shatters into shards; enhances bleed or shrapnel effects. | 5 ft radius |
| **Lightning Varnish** (U) | Reactive Oil | Enhances storm/lightning ingredients. Slight chance to arc randomly. | 5 ft radius |
| **Cindersoot Paste** (U) | Burnt Charcoal Mix | Amplifies smokescreens, blindness, or choking effects. Great for cover. | 10 ft radius |
| **Shimmerdust Flask** (U) | Ethereal Dust | Adds radiant or illusionary burst. Often used to dazzle or reveal hidden foes. | 5 ft radius |
| **Noxfire Oil** (U) | Tainted Oil | Ideal for necrotic or infernal splash effects. Burns violet with sulphurous scent. | 5 ft radius |
| **Rattler Salts** (U) | Sonic Compound | Enhances sound and concussive explosions. Sharp ringing disorients targets. | 10 ft radius |
| **Skyglass Powder** (R) | Arcane Dust | Adds psychic or thunder burst; ethereal particles confuse minds. | 10 ft radius |
| **Blast Honey** (R) | Explosive Sap | Sweet and sticky, ignites on impact. Used in heat or fire effects. | 10 ft radius |
| **Frostfire Gel** (R) | Elemental Slime | Enhances cold/fire dual potions. Volatile but beautiful. | 5 ft radius |
}}

### Effect Radius Guide

- **Single target**: Only the directly struck target is affected.
- **5 ft radius**: Small burst centred on impact; targets inside the measured area may be affected.
- **10 ft radius**: Larger burst measured 10 feet from impact; number of targets varies with positions.
- **Radius boosts**: Add flat increases first, then apply any doubling. Unless the GM approves a special creation, a thrown potion's radius can't exceed 20 feet.

{{gm
##### GM guidance
Measure the listed radius in the tabletop system; creatures caught within it, including allies or the thrower, may be affected unless a deliberately crafted selective effect says otherwise. Terrain and unusual magic are at GM discretion. For throwing, damage and saving throws, use the defaults under **Strength, Saves, Stacking and Time**.
}}

{{wide,panel
## Binder Mechanics Summary

- **Basic Binders:** Widely available, affordable carriers, including Spring Water, Spirit Resin and Witchhazel Salve. Rarity marks (C, U, R, UR, L) represent suggested access, not an additional rolling mechanic.
- **Specialist Binders:** May be scarce, tradeable, or a quest reward. Their own traits and the GM determine any thematic enhancements; they do not replace magical plant ingredients.
- **Matching Affinity:** An aligned binder can gently influence a potion’s theme or a secondary benefit. If a Harmony Test already occurs between conflicting plants, an aligned binder may also provide the optional **+/-1d4 adjustment to one Harmony die**. Binders never trigger a Harmony Test by themselves.
- **Mismatched Binders:** Not automatic failures. A Fire binder with a single Cold plant needs no Harmony Test; the GM might describe steam, smoke or another flavourful side effect. Plants determine the main magic; the binder influences, not dictates, its outcome.
}}

{{wide,folioArt
![](https://raw.githubusercontent.com/Omegaoliverid/Ampersand-s-Apothecary/52ab9f0ae9aedf06de291046c81bc2611d183a48/apo-binders.jpg)
}}

{{footnote AMPERSAND'S APOTHECARIA | BINDERS & CATALYSTS}}
{{pageNumber,auto}}

\page {ap11}
## Ointment Binders (3 applications)

These binders are thick, stable, and designed to be spread on weapons, armour, or skin. Ideal for short-term enchantments or toxic applications. Each binder provides its **listed duration** for which the effect remains active after application, unless a plant states its own duration. Strong harmonised ointments may, at GM discretion and with advance warning when brewing finishes, have a shorter duration if stabilising conflicting magic has consumed some of their staying power.

{{wide
| Name                | Type            | Traits & Notes                                                                                 | Duration |
|---------------------|------------------|-----------------------------------------------------------------------------------------------|----------|
| **Cave Resin** (C) | Sticky Resin | Stable, enhances weapon duration. May slow effect onset. | 5 min |
| **Witchhazel Salve** (C) | Herbal Blend | Neutral base. No enhancements. Gentle, used in healing or resistance salves. | 1 min |
| **Mithbark Oil** (U) | Magical Oil | Enhances elemental coatings (Fire, Cold, etc.). Long-lasting and smooth. | 10 min |
| **Drake Slime** (U) | Alchemical Slime | Boosts potency of flame, acid, and corrosive salves. Glows faintly. | 10 min |
| **Ghost Fat Salve** (U) | Ethereal Fat | Enhances necrotic, ethereal, or cold effects. Used by grave alchemists. | 5 min |
| **Gloam Jelly** (U) | Luminescent Gel | Enhances radiant or light-based enchantments. Glows on contact. | 10 min |
| **Frostcap Wax** (U) | Cold Wax | Boosts cold-based effects. Hardens on contact. | 5 min |
| **Blackroot Balm** (U) | Plant Paste | Used in paralytic and poison salves. Absorbs quickly. | 1 min |
| **Sunsear Grease** (U) | Flame Oil | Enhances fire damage, grants weapon a faint glow. | 5 min |
| **Thornmilk Butter** (U) | Sap/Fat Blend | Used in bleeding or piercing-enhancement salves. | 5 min |
| **Voidpitch Paste** (U) | Shadow Slime | Enhances psychic and fear-inducing applications. Chilling to touch. | 10 min |
| **Stormwax** (U) | Charged Wax | Enhances thunder and lightning weapon coatings. Hair-raising to use. | 10 min |
}}

## Ointment Usage & Duration

Ointments are applied to weapons, armour, or skin to grant temporary magical or alchemical effects.

- **Each ointment container has 3 applications (not 3 attacks).**
- A **"use"** refers to **one application**, not one attack.
- An application provides a **continuous effect for a set duration** (e.g., 1 minute).
  - During this time, all applicable attacks or interactions benefit from the effect.
- When the duration expires, a **new application (re-coating)** is required to regain the benefit.

### Re-Coating in Combat

Whether reapplying an ointment in combat takes an **Action**, **Bonus Action**, or more follows the game and table rules. Use the following as optional examples, depending on:

- The **size and type of the item** (dagger vs. greatsword vs. armour).
- The **binder's texture or viscosity**.
- The **GM’s ruling**, potentially modified by tool proficiencies (e.g., Herbalism Kit).

#### Suggested Rule of Thumb

| Item Type          | Time to Apply    |
|--------------------|------------------|
| Small weapons (daggers, arrows) | **Bonus Action**     |
| Medium weapons (swords, spears) | **Action**           |
| Armour or large shields          | **1 minute** (not in combat) |

\column

### Optional Mechanics

- Players **proficient with Herbalism Kits** or using **enhanced tools** may reapply faster if the GM allows it.
- A hasty application during battle may require a **DC 12 Dexterity check**. Failure might:
  - Waste one application of the ointment.
  - Apply a **shortened effect** (e.g., half duration).

**What can be coated?** Swords, axes, spears, daggers, hammers, staves and other weapons that deliver a physical strike, including magic weapons. One application treats **one weapon**; two wielded weapons need separate applications. Throwing weapons may retain the coating if recovered during the duration. Ranged coatings normally go on **ammunition**, not the bowstring or bow; the GM decides a fair bundle of arrows or bolts per application (ten is a suggested example, not a mandatory limit). Shields count as weapon coatings when used offensively. An item cannot maintain two separately layered active ointments; a deliberate multi-ingredient ointment is brewed as a single recipe. Magical blending experiments can cause an unusual reaction at the GM's discretion.

>  *Ointments shine in tactical play—ideal for prepping before a tough encounter or turning the tide mid-combat. Choosing when to reapply is part of the challenge and fun.*

{{footnote AMPERSAND'S APOTHECARIA | BINDERS & CATALYSTS}}
{{pageNumber,auto}}

\page {ap12}
{{wide,chapterhead
##### TECHNIQUES · V
# Complex Brewing and Harmony
}}

## One Recipe, One Clear Sequence

1. **Propose an outcome.** Identify the plants and choose one binder appropriate to the delivery method. The GM helps frame a plausible primary effect and possible secondary effects.
2. **Check the formula.** Maximum three plant handfuls and one binder; the base DC is 10, plus 2 for each repeat of a plant beyond its first handful, plus 5 for each new distinct plant after the first.
3. **Check for conflict.** Only if **two or more distinct plant ingredients have genuinely conflicting magical properties** does the GM call for a Harmony Test. The binder never triggers one on its own.
4. **Settle magical interactions.** Resolve Harmony per distinct conflicting plant, including permissible tool/binder adjustments. Otherwise skip this step entirely.
5. **Complete the downtime and brewing check.** Make an Intelligence check, adding your proficiency bonus once if you are proficient in Arcana, Nature, Alchemist’s Supplies or Herbalism Kit (or make a Wisdom check if using Medicine). A natural 1 has no special effect. Apply the result bands that follow; every committed ingredient is consumed.
6. **Record one finished item.** Drinkable and throwable potions have one use; ointments provide three applications, each lasting the binder’s stated duration. Action economy follows the gaming system and the GM's table.

### Brewing DC examples

| Recipe | DC | Time |
|---|---:|---:|
| 1 plant | 10 | 16 h |
| 2 same | 12 | 24 h |
| 2 distinct | 15 | 24 h |
| 3 same | 14 | 32 h |
| 2 same + 1 distinct | 17 | 32 h |
| 3 distinct | 20 | 32 h |

{{wide,panel
##### WHEN TO ROLL HARMONY
**Opposed affinities:** Fire–Cold, Fire–Water, Water–Earth, Earth–Air, Earth–Lightning, Radiant–Necrotic, Radiant–Infernal, Psychic–Eldritch, Psychic–Infernal and Arcane–Eldritch. Poison has no default opposite. A Harmony Test is needed only when a brew contains distinct plants from an opposed pair, or another pairing the GM rules genuinely conflicts. Any other plant in the brew adds its effect without rolling.
}}

{{wide
## The Harmony Test: Conflicting Plants Only

Roll **1d20 for each distinct conflicting plant**. Two handfuls of one plant count as a single plant for Harmony. A neutral binder does not roll. A matching binder can tint the finished effect but cannot automatically decide the outcome.

| Final adjusted Harmony die | Result |
|---|---|
| 1–5 | **Lost:** That plant’s magical contribution fails, but remains in the committed brew and still counts towards DC. |
| 6–14 | **Harmonised:** This plant contributes its magical property. |
| 15+ | **Dominant:** This plant strongly influences the outcome, without necessarily erasing everything else. |
}}

If more than one plant is Dominant, the highest **adjusted** result takes precedence as a default. Equal Dominant results can yield an extraordinary synthesis at the GM's discretion; neither plant needs to be erased. Ingredients that lose their effects cannot be removed from the formula to reduce DC. If every plant's contribution is Lost, the brew is a useless mixture (see the Useless Potion table) unless the GM chooses a stranger result.

After rolling the Harmony dice, brewers proficient in Alchemist’s Supplies may distribute their **proficiency bonus** as positive or negative shifts across Harmony dice (total magnitude no more than that bonus). An aligned binder may additionally shift **one** die up or down by **1d4**. These modify the Harmony results, not the basic brewing DC. Binders influence the potion’s thematic character but **do not trigger or dictate Harmony**.

**Harmony reward:** If all conflicting ingredients end on 6–14, the GM **may** grant advantage on the final brewing check. Do not award automatic advantage for a routine one-plant recipe, for three handfuls of the same plant, or for artificially inventing a Harmony conflict. Purchased ingredients are as valid as foraged ones when there is a genuine conflict.

{{footnote AMPERSAND'S APOTHECARIA | COMPLEX BREWING AND HARMONY}}
{{pageNumber,auto}}

\page {ap13}
{{gm
##### A note on reward
The GM should consider what the player has invested in the ingredients, travel, harvesting and brewing. Do not punish excellent play with arbitrary, unrewarding dead ends. Dangerous or bizarre outcomes remain possible, especially on a severe failure. Table conventions, system rules and the GM’s judgement take precedence.
}}

## Strength, Saves, Stacking and Time

- **Strong one-use potions are allowed.** A quest-worthy Fireball-like flask, real invisibility or extraordinary weapon ointment can be an appropriate reward for rare ingredients and arduous brewing. Balance chiefly by access, ingredient rarity, time and finished quantity, not by automatically shrinking successful effects.
- **Suggested effect durations where unspecified:** immediate for damage/healing, 1 minute for battle effects, 10 minutes for defence or exploration, 1 hour for modest utility. Printed plant or binder durations take precedence.
- **Default saving throws:** unless a plant states otherwise, the DC is set by the rarest plant in the brew: Common or Uncommon 12, Rare 14, Ultra Rare or Legendary 16. Use Dexterity against Fire, Lightning, Earth and Air; Constitution against Cold, Poison, Necrotic, Infernal and Radiant; Wisdom against Psychic and Eldritch; Strength against Water that pushes or knocks down. For other Water or Arcane effects, the GM picks the ability that fits.
- **Extra handfuls** may improve duration, reliability or add a thematic nuance, not mechanically multiply a plant's entire effect in every situation. GM-approved exceptions are encouraged when clever brewing deserves them. For example, extra Flameleaf might prolong warmth; extra Wizbloom should not simply restore extra spell slots but might add a surprising magical quirk.
- **No automatic bonus stacking:** when different plants confer closely related magical bonuses, the GM decides what combines. Distinct, fully harmonised effects may all work together as an extraordinary reward. Multiple identical ongoing game buffs follow the game’s own stacking rules, unless the GM rules on a special reaction. AC bonuses from Apothecaria potions and ointments don't stack: a creature uses only the highest.
- **Three ointment applications per container**, all eligible attacks during the binder's stated duration, not once per round by default. At brewing completion the GM may shorten an especially unstable harmonised ointment’s duration if that fits the story; do not add random weapon-dropping or extra stability rolls.
- **One active coating per item** normally. Layering separately prepared oils may instead spark a GM-devised reaction. Weapon coats belong on the striking weapon or ammunition, not automatically on the launcher.
- **Throwing a potion** takes an action, with a range of 20/60 feet. An area flask targets a point within range (no attack roll) and affects every creature within its radius, including allies and the thrower. A single-target flask uses an improvised ranged-weapon attack: roll d20 + Dexterity, adding proficiency only if proficient with improvised weapons. It has disadvantage beyond 20 feet. On a hit, resolve the brew’s printed effect and any saving throw it requires. Use the brew’s damage rather than adding ordinary improvised-weapon impact damage. Brewing-tool proficiency alone does not grant attack proficiency.
- **Default damage:** if a damaging flask has no printed damage, roll once for the whole flask using its rarest plant: Common 1d6, Uncommon 2d6, Rare 4d6, Ultra Rare 6d6, Legendary 8d6. Printed damage always takes priority. On a successful save, a creature takes half damage and suffers no other effect.
- **Drinking a potion**, or giving it to another creature, takes an action.
- **Delayed seeds** trigger at the start of the thrower's next turn unless a plant says otherwise.

{{wide,panel
## The Finished Brew: Result Bands

| Margin against brewing DC | Result |
|---|---|
| Success | Functions as the intended, GM-agreed potion. A natural 20 may bring an optional memorable flourish, sometimes even a yield of two diluted/concentrated portions at GM discretion. |
| Miss by 1–5 | **Flawed but functional:** a weaker duration, compromised potency or interesting minor side effect; it must still do something meaningful. |
| Miss by 6–10 | **Useless mixture:** a mostly harmless, strange outcome; use the d100 Useless Potion table in the Appendix. |
| Miss by 11+ | **Magical mishap:** a dramatic immediate reaction; use the d100 Magical Mishap table in the Appendix. |
}}


{{footnote AMPERSAND'S APOTHECARIA | COMPLEX BREWING AND HARMONY}}
{{pageNumber,auto}}

\page {ap14}
{{wide,chapterhead
##### TECHNIQUES · VI
# Worked Recipes
Worked potions using catalogue ingredients
}}

{{wide
{{trio
{{card,recipe
### Scorched Winter Flask (2 distinct plants, DC 15)

- 1 Charpod (Fire) and 1 Frostpod (Cold).
- 1 Frostfire Gel (throwable binder, 5-ft radius).
- An explosive burst of heat and cold, with the two opposing magical plants requiring Harmony. The GM determines the exact blend and saving throw from the successful rolls. Time: 24 hours, one throwable flask.
}}
{{card,recipe
### Serene Mind Draught (2 distinct plants, DC 15)

- 1 Mindleaf (Psychic) and 1 Snowmoss (Cold).
- 1 Spring Water (drinkable binder).
- A soothing draught that could support resistance to fear or charm and offer modest healing, if the GM judges both effects appropriate. Time: 24 hours, one drinkable potion.
}}
{{card,recipe
### Fire-Ice Stonecoat (3 distinct plants, DC 20)

- 1 Volcanthistle (Fire), 1 Hoarfrost Petal (Cold), 1 Pebblethorn (Earth).
- 1 Mithbark Oil (ointment binder; 10 minutes per application, 3 applications).
- If harmonised and successfully brewed, each successful weapon hit could add 1d4 fire, 1d6 cold and 1d4 piercing + 1d4 force damage. It is an exceptional rare-materials reward, not an inexpensive standard coating. A GM may instead create a different combination when the Harmony results justify it. Time: 32 hours, one ointment container (three applications).
}}
}}
*These recipe examples are demonstrations, not rigid spell formulae. GM discretion and meaningful player reward are central.*
}}

{{wide
## Worked recipe: A simple fire-and-frost synthesis

**Ingredients:** 1 Emberberry (Fire), 1 Rimedust Spores (Cold), 1 Spring Water (neutral drinkable binder). **Brewing DC 15; 24 hours.** The player wants breath that carries heat and an obscuring chill. Two opposing plants require Harmony; Spring Water does not contribute an elemental Harmony roll.

| Harmony outcomes | Example GM interpretation |
|---|---|
| Fire 20, Cold 20 | An exceptionally rare **burning-steam breath**, carrying both heat and a concealing, chilling cloud. The GM rewards the extraordinary tie rather than cancelling one component. |
| Fire 19, Cold 16 | Primarily fiery breath; a trailing veil of frosty vapour offers a modest concealing after-effect. |
| Fire 16, Cold 19 | Primarily freezing, obscuring mist, with scorching embers or warming vapour as a secondary effect. |
| Both 6–14 | Both combine evenly; the GM may permit advantage on the final brewing check. |

No listed illustration is a compulsory new spell; each is a signpost for adjudicating an original recipe.
}}

{{wide,panel,cols2
## Binder Variation: One Pair, Different Character

**Same two plants, same Harmony results:** Emberberry 19, Rimedust Spores 16. They still require Harmony regardless of binder. Their final drinkable potion need not be identical.

**Neutral Spring Water:** The binder adds no new magical affinity. Fire takes precedence on the dice; a fiery breath with cooling vapour is a reasonable interpretation.

**Tincture of Ash (fire-aligned drinkable):** The brewer may apply its optional +/-1d4 Harmony adjustment to one roll (for example +2 to Emberberry, making an adjusted 21 (still Dominant)). The binder also makes smoke, cinders or hot steam a fitting theme. The plants still establish the main properties. The GM could instead adjust Cold towards harmony if appropriate.

**If the GM introduces a frost-aligned drinkable binder:** It might emphasise icy mist even when fire has the stronger Dominant die, while preserving the fire component. Such a binder is an optional addition to the catalogue, not an existing ingredient. **A binder alone never forces another Harmony Test**: one Cold plant and one Fire binder is a normal brew with an interesting possible theme.
}}

{{footnote AMPERSAND'S APOTHECARIA | WORKED RECIPES}}
{{pageNumber,auto}}

\page {ap15,specimen}
![](https://raw.githubusercontent.com/Omegaoliverid/Ampersand-s-Apothecary/52ab9f0ae9aedf06de291046c81bc2611d183a48/apo-counter.jpg){position:absolute,top:0px,left:0px,width:100%,height:100%,object-fit:cover}

\page
{{wide,chapterhead
##### THE FLORA ARCANA · FIRE
# The Fire-Bound Flora
Fire-aligned flora are aggressive, vibrant, and volatile. These plants draw their essence from heat, combustion, and transformation. Found near volcanoes, scorched plains, lava flows, and elemental rifts, they are prized by alchemists and feared by the careless. Each chapter's Potion Usage Guidelines suggest what experimental brews might achieve; the plant tables give the reliable effects.
}}

{{wide
## Potion Usage Guidelines
{{trio
{{card
#### Drinking Potions (Ingested)
Fire plants in potions often grant:

- **Resistance or immunity to fire**
- **Increased aggression or physical damage**
- **Temporary boosts to strength or energy**
- **Internal heating (preventing cold effects or exhaustion)**

Side effects can include:

- Intestinal discomfort
- Random heat auras or skin flushing
- Hallucinations of flame
}}
{{card
#### Throwing Potions (Explosive)
When used in thrown potions, fire plants can:

- **Ignite targets or areas**
- **Create smoke clouds or flashbursts**
- **Cause ongoing burn damage (DoT)**
- **Explode with area effect**

Common interactions include combining with **Volatile Spirits** or **Blast Honey** for wide-radius burns.
}}
{{card
#### Ointments (Coating)
When distilled into ointments, fire plants may:

- **Add fire damage to weapons**
- **Heat armour to burn attackers**
- **Ignite flammable surfaces on contact**

Durations vary with binder quality; improper application can cause burns to the user.
}}
}}
}}

{{wide,plate
{{pimg
![Pyrebark](https://raw.githubusercontent.com/Omegaoliverid/Ampersand-s-Apothecary/52ab9f0ae9aedf06de291046c81bc2611d183a48/apo-15.jpg)
}}
{{ptext
#### Pyrebark
##### SPECIMEN · FIRE
Pyrebark trees are towering, resilient specimens found in scorched forests and charred wastelands. Their thick, dark bark is deeply grooved, with glowing orange veins running beneath the surface like trapped embers. Anchored deep in volcanic soil, their roots withstand intense heat and occasional eruptions, so these trees are often the last flora standing in volcanic regions. In high temperatures the bark pulses with internal heat, casting an ominous glow into the darkness.
}}
}}

{{footnote AMPERSAND'S APOTHECARIA | THE FIRE-BOUND FLORA}}
{{pageNumber,auto}}

\page {ap16,plantlist}
{{wide,flora
## Fire-Aligned Plants

| Plant Name         | Harvestable Part | Alchemical Properties | Severe Harvest Failure |
|--------------------|------------------|-------------------------------------------------------------------|---------------------------------------------------------------|
| **Smoulderseed** (C) | Seed | When brewed into a trap and planted, bursts into flame when disturbed (5 ft radius, 1d6 fire, DC 12 Dex save for half). | Seed ignites prematurely in pouch (burns 1d4 nearby items). |
| **Flameleaf** (U) | Leaf | Grants resistance to cold; can be brewed into warmth draught. | Leaf combusts instantly, burning the harvester (1d4 fire dmg). |
| **Cinderroot** (U) | Root | When brewed into a suitable weapon ointment, adds 1d4 fire damage to each successful melee hit for 1 minute. | Harvester’s hands go numb from internal heat (disadv. on Str checks for 1 hr). |
| **Ashbloom** (U) | Flower (Whole) | Used in throwable blinding-flash potions; creatures in the binder-defined radius make a DC 13 CON save or are blinded until the end of their next turn. | Pollen explodes in face—temporary blindness (1 min). |
| **Emberberry** (U) | Berry | When brewed and drunk, grants one fiery breath: as an action, a 15 ft cone, 1d6 fire (DC 12 Dex save for half). | Berry pops in hand—1 fire dmg and loses the yield. |
| **Ignistalk** (U) | Stem | Boosts adrenaline and strength (advantage on STR checks). | Causes violent shaking and heatstroke (1 level of exhaustion). |
| **Pyrebark** (U) | Bark | Ground bark used in potions for fire resistance. | Bark crumbles to ash—no usable material, coughs violently. |
| **Sparkspore** (U) | Spores | In a thrown potion, ignites in a minor explosion (2d6 fire). | Spores spread into eyes—temporary blindness and coughing. |
| **Charpod** (U) | Pod | Shatters with heat on impact—used in burst fire potions (2d6 fire). | Pod explodes during harvest—harvester takes 1d6 fire dmg. |
| **Molten Sap** (U) | Sap | Sticky, burns over time—great for thrown or coating effects. | Sap clings to skin—burns for 1 minute (1 dmg/round unless removed). |
| **Dragon’s Resin** (U) | Resin | Used to stabilise high-heat potions—adds duration to fire effects. | Resin becomes brittle—crumbles with no yield. |
| **Firesilk Petal** (U) | Petal | Induces passion or rage—used in emotion-based brews. | Skin contact causes intense mood swing (rage or despair). |
| **Scorchvine** (R) | Vine | In a thrown potion, binds and burns: on a failed save, 1d4 fire and restrained for up to 1 minute (escape DC 14). | Vine lashes out and ignites clothing (DC 12 DEX save or take 1d6 fire dmg). |
| **Volcanthistle** (R) | Thorn | Used in weapon poisons to add burning damage (1d4 fire on hit). | Thorn pierces glove, igniting small flame on skin (1d4 dmg). |
| **Hellbulb** (UR) | Bulb | Used for transformation potions—may grant temporary flame form. | Bulb erupts in flash fire (DEX save DC 13 or 2d6 fire dmg). |
}}

{{wide,tips
**Harvesting Tips**:
- Always wear **gloves** and use **snips or trowels** to avoid triggering reactions.
- Harvest at dawn or dusk when internal heat is lowest.
- Plants like **Scorchvine** and **Charpod** may lash out—prepare containment tools.
}}

{{wide,strip,short
{{pimg
![Flameleaf](https://raw.githubusercontent.com/Omegaoliverid/Ampersand-s-Apothecary/52ab9f0ae9aedf06de291046c81bc2611d183a48/apo-16.jpg)
}}
#### Flameleaf
##### SPECIMEN · FIRE
In the wild, Flameleaf grows along the scorched edges of volcanic fissures and across ash-covered ground. Its fiery orange-and-red leaves are thin and almost translucent, flickering like flame. Hardy and heat-loving, it thrives in extreme heat, drawing energy from basaltic soil and geothermal vents and often giving off a faint warmth or glow in the darkness of its rocky home.
}}

{{footnote AMPERSAND'S APOTHECARIA | THE FIRE-BOUND FLORA}}
{{pageNumber,auto}}

\page {ap17,specimen}
{{wide,chapterhead
##### THE FLORA ARCANA · COLD
# The Cold-Bound Flora
The plants aligned with cold and frost thrive in glacial valleys, cursed tundras, or places touched by elemental ice magic. Their effects are often **slowing**, **preserving**, or **numbing**, with some capable of crystallising magic or amplifying cold spells.
}}

{{wide
## Potion Usage Guidelines
{{trio
{{card
#### Drinkable Potions (Internal)
- Slows metabolism (resist poison or necrotic damage)
- Numbs pain (temp HP or reduced effects from critical hits)
- Enhances clarity or focus (cold boosts to concentration)
- Grants temporary cold resistance or "ice armour"
}}
{{card
#### Throwable Potions (External Burst)
- Slow or freeze enemies in a radius
- Chill surfaces (slippery terrain or damage over time)
- Suppress fire effects or melt heat-based enchantments
- Crystallise air into freezing fog (obscurement + cold damage)
}}
{{card
#### Ointments (Weapon/Armour)
- Coat weapons with frostbite damage
- Apply to armour for temporary cold resistance
- Temporarily harden or reinforce surfaces (bonus AC for short time)
}}
}}
}}

{{wide,strip
{{pimg
![Snowmoss](https://raw.githubusercontent.com/Omegaoliverid/Ampersand-s-Apothecary/52ab9f0ae9aedf06de291046c81bc2611d183a48/apo-17.jpg)
}}
#### Snowmoss
##### SPECIMEN · COLD
Snowmoss grows abundantly in the shaded, snow-covered forests of the northern tundra and alpine regions. Its soft, pale-green leaves are dusted with a fine layer of frost, giving it a snow-like appearance. This resilient moss spreads across rocky ground and tree trunks, absorbing the chilling moisture in its environment.
}}

{{footnote AMPERSAND'S APOTHECARIA | THE COLD-BOUND FLORA}}
{{pageNumber,auto}}

\page {ap18,plantlist}
{{wide,flora
## Cold-Aligned Plants

| Plant Name         | Harvestable Part | Alchemical Properties | Severe Harvest Failure |
|--------------------|------------------|-------------------------------------------------------------------|--------------------------------------------------------------|
| **Snowmoss** (C) | Leaf | Used to heal minor wounds; restores 1d4+1 HP when brewed. | The moss releases a freezing puff – the harvester is slowed for 1 minute. |
| **Glacient Root** (U) | Root | Grants cold resistance for 1 hour when brewed. | Causes frostbite damage to harvester's hand (1d6 cold). |
| **Frostbloom** (U) | Flower (Whole) | Minor healing + frost armour (AC +1 for 1 min). | Causes cold shock; DC 13 Con save or gain one level of exhaustion. |
| **Shiverberry** (U) | Berry | Grants resistance to fire for 10 minutes. | Bursts prematurely—cold surge deals 2d6 cold to harvester. |
| **Frostpod** (U) | Pod | Bursts in 5 ft frost nova—ideal for traps. | Explodes during harvest—2d6 cold in 5 ft radius. |
| **Gelid Resin** (U) | Resin | Stabilises and can enhance frost effects in brewing; GM may grant a modest frost-themed improvement. | Binds to tools—reduces harvesting tool efficiency. |
| **Permafrost Bulb** (U) | Bulb | Grants icy skin (cold resistance). | Ruptures—save or be slowed for 1 minute. |
| **Rimedust Spores** (U) | Spores | Creates a fog that lightly obscures the binder's radius for 1 minute—useful for escape. | Cling to harvester—light obscuration (-2 Perception). |
| **Brittle Stem** (U) | Stem | Increases a cold potion's radius by 5 ft, or a cold spell's range by 10 ft. | Snaps noisily—alerts nearby creatures (if stealthing). |
| **Chillseed** (U) | Seed | Delays a cold potion's effect until the start of the thrower's next turn, then adds 2d4 cold damage to its burst. | Backfires—1d4 cold and stunned for 1 round. |
| **Rimevine** (R) | Vine | Entangles creatures in a 5 ft area: DC 14 Str save or restrained for up to 1 minute (escape DC 14). | Vine lashes out violently, causing restrained condition. |
| **Hoarfrost Petal** (R) | Petal | Adds chilling effect to potions or weapons (1d6 cold dmg). | Crumbles to powder, losing potency entirely. |
| **Iceshard Bark** (R) | Bark | Adds bludgeoning resistance; hardens skin like bark. | Bark shatters; harvester takes 1d4 piercing damage. |
| **Winterthorn** (R) | Thorn | Inflicts 1d4 cold + bleed effect when applied to weapons. | Thorn pierces harvester—1d4 cold + 1 bleed/round. |
| **Cryosap** (UR) | Sap | Adds AoE freeze (10 ft) to thrown potions. | Bonds to hand; Strength check required to remove tool. |
}}

{{wide,strip
{{pimg
![Rimevine](https://raw.githubusercontent.com/Omegaoliverid/Ampersand-s-Apothecary/52ab9f0ae9aedf06de291046c81bc2611d183a48/apo-18.jpg)
}}
#### Rimevine
##### SPECIMEN · COLD
Rimevine snakes through the icy crevices of high-altitude tundra and frozen mountain slopes. Its thick, bluish tendrils shimmer with frost and ice crystals, often rimed in a thin layer of frost. Thriving where temperatures hover well below freezing, it clings to rocks and trees, waiting to entangle anything that ventures too close.
}}

{{footnote AMPERSAND'S APOTHECARIA | THE COLD-BOUND FLORA}}
{{pageNumber,auto}}

\page {ap19,specimen}
{{wide,chapterhead
##### THE FLORA ARCANA · LIGHTNING
# The Storm-Touched Flora
Lightning plants surge with electrical energy, found in high-altitude stormlands, shattered plains, and magical regions charged with atmospheric tension. Their effects are often shocking, conductive, or speed-enhancing, with some providing control over kinetic or static energy.
}}

{{wide
## Potion Usage Guidelines
{{trio
{{card
#### Drinkable Potions (Internal)
- Boosts reflexes and reaction time (advantage on Dex saves)
- Enhances movement speed temporarily
- Jump-starts adrenaline (temp HP or bonus action on first turn)
- Charges the body—small lightning shocks on contact (defensive feature)
}}
{{card
#### Throwable Potions (External Burst)
- Discharges electricity in a radius (lightning AoE damage)
- Chains lightning between nearby targets (forked strike)
- Disrupts magical effects or machines
- Electrifies terrain (hazardous zone, speed reduction)
}}
{{card
#### Ointments (Weapon/Armour)
- Adds lightning damage to attacks (1d4 or 1d6)
- Causes shocking retaliation on being struck (1d4 damage)
- Increases initiative or reaction-based bonuses
- Conductive armour—redirects or grounds lightning
}}
}}
}}

{{wide,plate
{{pimg
![Flashthorn](https://raw.githubusercontent.com/Omegaoliverid/Ampersand-s-Apothecary/52ab9f0ae9aedf06de291046c81bc2611d183a48/apo-19.jpg)
}}
{{ptext
#### Flashthorn
##### SPECIMEN · LIGHTNING
Flashthorns dot the arid, rocky regions bordering wild thunderstorm zones, where frequent lightning strikes shape the landscape. These hardy, spiny bushes have jagged thorns that shimmer with faint sparks and static electricity. The plants thrive in nutrient-poor soils, their stiff branches crackling softly during stormy nights.
}}
}}

{{footnote AMPERSAND'S APOTHECARIA | THE STORM-TOUCHED FLORA}}
{{pageNumber,auto}}

\page {ap20,plantlist}
{{wide,flora
## Lightning-Aligned Plants

| Plant Name           | Harvestable Part | Alchemical Properties | Severe Harvest Failure |
|----------------------|------------------|------------------------------------------------------------------------|---------------------------------------------------------------------------|
| **Lumenstem** (C) | Stem | Conducts lightning spells—extends their range by 10 ft. | Snaps explosively—1d8 lightning in a 10 ft line. |
| **Sparkleaf** (U) | Leaf | Adds speed enhancement or 10 ft movement to potion. | Static surge—harvester shocked (1d4) and drops item. |
| **Thunderbloom** (U) | Flower (Whole) | Dual effect: 1d4 healing + thunder burst in 5 ft radius. | Bursts early—1d6 thunder to all within 5 ft. |
| **Boltberry** (U) | Berry | Adds 1d6 lightning damage to thrown or drinkable potion. | Berry explodes—1d6 lightning to harvester and 5 ft splash. |
| **Crackbark** (U) | Bark | In armour ointments, deals 1d4 lightning damage to the attacker on each successful melee hit against the coated armour. | Bark discharges—harvester takes 2d4 lightning. |
| **Flashthorn** (U) | Thorn | Used in weapon salves—adds lightning burst on critical hit. | Thorn surges—harvester’s hand goes numb for 1 hour (no fine tool use). |
| **Joltsap** (U) | Sap | Creates AoE lightning detonation (10 ft, 2d6 lightning). | Bonds to glove—next touch shocks wearer for 1d6 damage. |
| **Stormseed** (U) | Seed | Triggers a delayed lightning burst at the start of the thrower's next turn. | Seed shorts—shocks harvester for 1d6 damage and dazes them for 1 round. |
| **Voltrag Root** (R) | Root | Grants advantage on Dex saves for 1 hour. | Causes minor seizure—DC 12 Con save or lose next action. |
| **Arcvine** (R) | Vine | In a thrown potion, lightning arcs from the main target to one other creature within 10 ft, which takes half the potion's lightning damage on a failed Dex save. | Vine lashes back—deals 1d6 lightning to harvester. |
| **Cracklepod** (R) | Pod | When thrown, bursts in a crackling shockwave: 5 ft radius, lightning damage, and dazed on a failed save. | Pod discharges prematurely—harvester is dazed for 1 round. |
| **Fulgurite Resin** (R) | Resin | Enhances lightning duration and chaining. | Resin electrifies container—equipment malfunctions for 1 hour. |
| **Arcspores** (R) | Spores | Release electrical fog—lightly obscures and zaps within 10 ft. | Spores zap harvester each round until cleaned (1 lightning/round). |
| **Shockpetal** (UR) | Petal | Causes a brief seizure on hit (DC 13 Con save or stunned for 1 round). | Petals spark violently—harvester stunned for 1 round. |
| **Stormbulb** (UR) | Bulb | Boosts reaction speed: for 1 minute, the drinker can take one extra reaction each round, but not to cast a spell. | Overstimulates—harvester is confused for 1 round. |
}}

{{wide,strip
{{pimg
![Thunderbloom](https://raw.githubusercontent.com/Omegaoliverid/Ampersand-s-Apothecary/52ab9f0ae9aedf06de291046c81bc2611d183a48/apo-20.jpg)
}}
#### Thunderbloom
##### SPECIMEN · LIGHTNING
Thunderbloom flourishes on open plains and high-altitude meadows frequently struck by thunderstorms. Its large, luminescent petals are streaked with silver and violet and pulse with soft thunderclaps that seem to resonate from within. During storms it emits a faint crackling aura, harnessing the raw power of lightning.
}}

{{footnote AMPERSAND'S APOTHECARIA | THE STORM-TOUCHED FLORA}}
{{pageNumber,auto}}

\page {ap21,specimen}
{{wide,chapterhead
##### THE FLORA ARCANA · NECROTIC
# The Deathrooted Flora
Necrotic-aligned plants grow in shadow-drenched crypts, cursed battlegrounds, desecrated groves, and lands touched by undeath. Their effects revolve around decay, debilitation, life drain, and manipulation of death energy. Though perilous, they offer immense power to those who dare to harvest them.
}}

{{wide
## Potion Usage Guidelines
{{trio
{{card
#### Drinkable Potions (Internal)
- Grants resistance to necrotic damage
- Provides temporary hit points from nearby deaths
- Suppresses pain and fear (advantage on certain saves)
- Allows communication with the dead or sensing undead
}}
{{card
#### Throwable Potions (External Burst)
- Inflicts decay or rotting effects over time (necrotic DoT)
- Weakens targets’ vitality (reduces healing received)
- Corrupts terrain, making it hazardous or cursed
- Creates zones that repel or harm the living
}}
{{card
#### Ointments (Weapon/Armour)
- Adds necrotic damage on hit (1d4–1d6)
- Coated armour radiates a weakening aura (enemy Str saves at disadvantage)
- Allows weapon to bypass undead resistances
- Temporarily fortifies armour with deathward magic (blocks one fatal blow)
}}
}}
}}

{{wide,plate,rev
{{pimg
![Wanevine](https://raw.githubusercontent.com/Omegaoliverid/Ampersand-s-Apothecary/52ab9f0ae9aedf06de291046c81bc2611d183a48/apo-21.jpg)
}}
{{ptext
#### Wanevine
##### SPECIMEN · NECROTIC
Wanevine coils through shadowy ruins and haunted forests, its thin black tendrils twisting in search of life to drain. Necrotic energy seeps from the vines, and their gnarled stems are studded with small, glowing spores.
}}
}}

{{footnote AMPERSAND'S APOTHECARIA | THE DEATHROOTED FLORA}}
{{pageNumber,auto}}

\page {ap22,plantlist}
{{wide,flora
## Necrotic-Aligned Plants

| Plant Name           | Harvestable Part | Alchemical Properties | Severe Harvest Failure |
|----------------------|------------------|-------------------------------------------------------------------------|---------------------------------------------------------------------------|
| **Deathroot** (U) | Root | Brew grants resistance to necrotic damage for 1 hour. | Root poisons the harvester—DC 14 Con save or take 2d6 necrotic damage. |
| **Ghoulleaf** (U) | Leaf | Used in salves to protect against undead paralysis. | Leaf withers on contact—harvester suffers numbness (-2 to Dex checks). |
| **Gravepetal** (U) | Petal | Induces fear in targets (DC 13 Wis save or frightened until the end of its next turn). | Petals scream softly—harvester gains disadvantage on next Wisdom check. |
| **Mireberry** (U) | Berry | Causes target to rot over time (1d4 necrotic/round for 3 rounds). | Bursts on harvest—deals 2d6 necrotic to harvester in 5 ft splash. |
| **Gravetouch Thorn** (U) | Thorn | Adds necrotic damage and fear on crits (DC 12 Wis). | Thorn embeds in skin—harvester takes 1d4 necrotic/round until removed. |
| **Coffinpod** (U) | Pod | Explodes with necrotic spores (2d6 necrotic in the binder's radius). | Detonates early—1d6 necrotic + frightened on failed Wis save. |
| **Dirgeseed** (U) | Seed | Explodes at the start of the thrower's next turn with a necrotic pulse (2d6 necrotic); great for traps. | Backfires—harvester takes 2d6 necrotic and is dazed for 1 round. |
| **Witherstem** (R) | Stem | When brewed for a weapon coating, adds 1d4 necrotic damage per successful hit and grants temporary hit points equal to the necrotic damage dealt (once per turn); temporary hit points do not stack. | Stem cracks and leaks dark fluid—harvester loses 1d4 max HP temporarily. |
| **Corpsebloom** (R) | Flower (Whole) | Dual effect: heals undead + damages living (2d6 necrotic). | Emits foul stench—harvester must save or be poisoned for 1 hour. |
| **Rotbark** (R) | Bark | Can be brewed into a disease-resistant salve or death aura shield. | Bark splinters and infects tool—harvester risks cursed infection. |
| **Blightsap** (R) | Sap | Creates a 10 ft radius decay zone for 1 minute: a creature that starts its turn there takes 1d6 necrotic (DC 14 Con save for half). | Bonds to skin—harvester becomes sickened (disadvantage on attacks). |
| **Funereal Resin** (R) | Resin | Doubles duration of necrotic effects and dark magic boost. | Resin binds to equipment—harvester’s tools cursed until cleansed. |
| **Rotspores** (R) | Spores | Fills the binder's radius with necrotic mist for 1 minute (lightly obscured): a living creature that starts its turn there takes 1d6 necrotic (DC 14 Con save for half); undead regain 1d6 hit points instead. | Spores infect harvester’s lungs—DC 12 Con save or short-term disease. |
| **Wanevine** (R) | Vine | Entangles and leeches life: 1d4 necrotic and slowed until the end of the target's next turn (DC 14 Con save negates). | Vine bites back—harvester is grappled until freed. |
| **Soulbulb** (UR) | Bulb | Used in elixirs to delay death—grants Death Ward effect (1 use). | Bulb pulses—harvester makes DC 14 Wis save or is stunned by visions. |
}}

{{wide,strip,short
{{pimg
![Gravepetal](https://raw.githubusercontent.com/Omegaoliverid/Ampersand-s-Apothecary/52ab9f0ae9aedf06de291046c81bc2611d183a48/apo-22.jpg)
}}
#### Gravepetal
##### SPECIMEN · NECROTIC
Gravepetals grow in shadowed swamps and cursed moorlands. Their violet petals shiver and scream softly when touched. Disturbing a living Gravepetal releases a spectral aura within 5 feet. Creatures there must make a DC 13 Wisdom save or be frightened of the plant until the end of their next turn. After making the save, a creature is immune to that patch’s aura for 24 hours.
}}

{{footnote AMPERSAND'S APOTHECARIA | THE DEATHROOTED FLORA}}
{{pageNumber,auto}}

\page {ap23,specimen}
{{wide,chapterhead
##### THE FLORA ARCANA · RADIANT
# The Luminous Flora
Radiant-aligned plants grow in hallowed groves, mountaintop shrines, under starlit canopies, or in places bathed in celestial influence. Their effects are purifying, healing, protective, and occasionally blinding. Many are rare, requiring special times (sunrise, solstice, moonlight) or rituals to even appear.
}}

{{wide
## Potion Usage Guidelines
{{trio
{{card
#### Drinkable Potions (Internal)
- Heals HP and removes diseases or poisons
- Grants temporary radiant resistance
- Enhances charisma, clarity, or spell potency
- Allows brief bursts of light or divine presence
}}
{{card
#### Throwable Potions (External Burst)
- Blinds undead or evil creatures
- Radiates cleansing light (removes curses, dispels magical darkness)
- Creates radiant zones of healing or sanctuary
- Deals radiant damage to fiends, undead, or aberrations
}}
{{card
#### Ointments (Weapon/Armour)
- Coats weapons with radiant damage (1d4–1d6)
- Bypasses resistance to non-magical weapons for celestial foes
- Wards armour against necrotic or charm effects
- Emits aura of light (can dispel magical darkness)
}}
}}
}}

{{wide,plate
{{pimg
![Aurastem](https://raw.githubusercontent.com/Omegaoliverid/Ampersand-s-Apothecary/52ab9f0ae9aedf06de291046c81bc2611d183a48/apo-23.jpg)
}}
{{ptext
#### Aurastem
##### SPECIMEN · RADIANT
Aurastem grows tall on sunlit hilltops and clear plains, its slender stems shimmering with a silvery lustre by day. These resilient stalks channel sunlight directly into their core, making them highly effective at amplifying radiant magic. In bright meadows and open forests they stand out, swaying gently in the breeze as their energy pulses softly. When the wind blows over them, it is said, you can hear the goodbyes of the recently departed.
}}
}}

{{footnote AMPERSAND'S APOTHECARIA | THE LUMINOUS FLORA}}
{{pageNumber,auto}}

\page {ap24,plantlist}
{{wide,flora
## Radiant-Aligned Plants

| Plant Name            | Harvestable Part | Alchemical Properties | Severe Harvest Failure |
|-----------------------|------------------|--------------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| **Solleaf** (C) | Leaf | Boosts healing potions (add +1d4 HP). | Leaf burns—harvester takes 1 radiant damage and loses the leaf. |
| **Starberry** (C) | Berry | Enhances charisma or insight temporarily (advantage on 1 social roll). | Berry collapses—harvester suffers emotional surge (GM chooses effect). |
| **Dawnsroot** (U) | Root | Restores 2d4 HP and cures minor ailments when brewed. | Harvester is dazzled—disadvantage on Perception for 10 minutes. |
| **Aurastem** (U) | Stem | When brewed, adds +1 to the saving throw DC of radiant spells for 1 minute. Further amplification from repeated handfuls is GM-guided. | Stem flashes—harvester blinded for 1 round. |
| **Celestbark** (U) | Bark | Wards armour against evil (AC +1 vs undead/fiends for 1 min). | Bark disintegrates—harvester takes 1d6 radiant, tool may be damaged. |
| **Halo Thorn** (U) | Thorn | Adds radiant damage and light burst on crit (1d4 radiant, and dazzled until the end of the target's next turn). | Thorn pierces skin—harvester takes 1 radiant/round until removed. |
| **Seraphsap** (U) | Sap | Creates radiant AoE on throw (10 ft, 2d6 radiant vs undead/fiends). | Bonds to hand—glows for 1 hour, giving away position. |
| **Heavenpod** (U) | Pod | Explodes with calming light; removes frightened condition in 10 ft radius. | Backfires—harvester is calmed (cannot take reactions for 1 minute). |
| **Auric Resin** (U) | Resin | Boosts radiant effects and doubles the duration of a radiant potion (to a maximum of 1 hour). | Resin binds and hums—harvester attracts celestial attention (GM flavour). |
| **Sunbulb** (U) | Bulb | Used in transformative potions; grants “blessed form” (+1 AC, 1 min). | Bursts prematurely—harvester blinded for 1d4 rounds. |
| **Gleamvine** (U) | Vine | Adds light trails or blinding streaks to thrown potions. | Vine binds hand—harvester restrained until freed (DC 12 Str). |
| **Eclipsed Bloom** (R) | Flower (Whole) | Grants resistance to necrotic and radiant damage for 1 hour. | Bloom emits blinding pulse—DC 13 Con save or gain Sunblind (disadv. attacks). |
| **Gloryspores** (R) | Spores | Shines with radiant mist; used in sanctuary potions (enemies avoid area). | Spores react—harvester glows (disadvantage on stealth for 1 hour). |
| **Dawnseed** (R) | Seed | Delays effect, then creates healing pulse (2d6 HP in 5 ft radius). | Seed overloads—harvester takes 1d6 radiant, and the seed is ruined. |
| **Lunapetal** (L) | Petal | Used to brew light-based vision potions (darkvision or true sight). | Petal fades—no material. After a long rest, the harvester may make one additional attempt on this specimen; a second failure exhausts it. |
}}

{{wide,strip,short
{{pimg
![Dawnsroot](https://raw.githubusercontent.com/Omegaoliverid/Ampersand-s-Apothecary/52ab9f0ae9aedf06de291046c81bc2611d183a48/apo-24.jpg)
}}
#### Dawnsroot
##### SPECIMEN · RADIANT
Dawnsroot plants thrive in the first light of dawn, often nestled beneath the soil in fertile grasslands and sun-dappled valleys. Their roots are thick and fibrous, glowing faintly with a soft golden hue as they absorb the morning sun’s energy. These roots are prized for their restorative properties, capable of healing wounds and curing minor ailments when carefully harvested. They are often found near peaceful streams and open fields where the sunrise is most vibrant.
}}

{{footnote AMPERSAND'S APOTHECARIA | THE LUMINOUS FLORA}}
{{pageNumber,auto}}

\page {ap25,specimen}
{{wide,chapterhead
##### THE FLORA ARCANA · PSYCHIC
# The Mindwoven Flora
Psychic flora are attuned to mental energy, thought currents, and emotional resonance. They grow near ancient ley lines, sites of intense emotion, or in realms bordering the Ethereal or Dreamscape. Their effects can bolster mental clarity, disturb thought, or invoke illusion and charm.
}}

{{wide
## Potion Usage Guidelines
{{trio
{{card
#### Drinkable Potions (Internal)
- Grants short-term telepathy or surface-thought reading
- Boosts Intelligence, Wisdom, or Charisma-based checks
- Offers advantage on Insight, Investigation, or saves vs charm/fear
- May trigger vivid dreams or memory recall (used in divination rituals)
}}
{{card
#### Throwable Potions (External Burst)
- Inflicts confusion, disorientation, or psychic damage
- Induces fear or emotional surges in targets
- Creates zones of silence, hallucination, or dreamlike fog
- Disrupts spellcasting by interfering with concentration
}}
{{card
#### Ointments (Weapon/Armour)
- Coats weapons with psychic lash effects (1d4–1d6 psychic damage)
- Bypasses resistance to non-physical attacks
- Applies to armour for mental fortification (resistance vs fear/charm)
- Emits a psychic echo—enemies attacking must make Wis saves or hesitate
}}
}}
}}

{{wide,plate,rev
{{pimg
![Mistspores](https://raw.githubusercontent.com/Omegaoliverid/Ampersand-s-Apothecary/52ab9f0ae9aedf06de291046c81bc2611d183a48/apo-25.jpg)
}}
{{ptext
#### Mistspores
##### SPECIMEN · PSYCHIC
Mistspores flourish in damp, shadowy caverns and secluded, swampy wetlands where mist and fog hang perpetually heavy. Their spores drift like delicate, shimmering clouds, forming an illusory fog that heavily obscures the surroundings. Disturb them and they release a dense, illusion-filled fog that lingers for up to an hour, making reality hard to tell from hallucination.
}}
}}

{{footnote AMPERSAND'S APOTHECARIA | THE MINDWOVEN FLORA}}
{{pageNumber,auto}}

\page {ap26,plantlist}
{{wide,flora
## Psychic-Aligned Plants

| Plant Name            | Harvestable Part | Alchemical Properties | Severe Harvest Failure |
|-----------------------|------------------|--------------------------------------------------------------------------------|--------------------------------------------------------------------------------|
| **Whisperstem** (U) | Stem | Enhances telepathic link potions and Message spells. | Causes auditory hallucinations for 10 minutes (GM flavour). |
| **Mindleaf** (U) | Leaf | Grants advantage on saves vs charm/fear for 1 hour. | Leaf screams briefly—harvester must pass DC 12 Wis save or be frightened. |
| **Wyrmbark** (U) | Bark | Adds psychic resistance when brewed or applied (1 hour). | Bark vibrates painfully—harvester takes 1d6 psychic damage. |
| **Aethershade Resin** (U) | Resin | Boosts duration of psychic effects and enhances dream potions. | Resin glows and hums—attracts astral creatures (GM decision). |
| **Mistspores** (U) | Spores | Creates an illusionary fog in a 15 ft area (heavily obscured) for 1 hour. | Spores attach—harvester sees illusions for 1 hour (DC 12 to disbelieve). |
| **Nervevine** (U) | Vine | Enhances potions that affect movement or control. | Vine coils and shocks—harvester loses movement in one limb for 1 minute. |
| **Reverie Seed** (U) | Seed | Delays potion effect, then triggers psychic shockwave (2d6 psychic). | Backfires—harvester stunned for 1 round and takes 1d4 psychic damage. |
| **Dreamroot** (R) | Root | Used in potions to induce prophetic dreams or remove sleep effects. | Induces involuntary sleep for 1d4 hours if touched barehanded. |
| **Thoughtbloom** (R) | Flower (Whole) | Allows surface thought reading for 10 minutes. | Bloom wilts—harvester hears whispers (disadvantage on Wis saves for 1 hour). |
| **Phantom Thorn** (R) | Thorn | Adds psychic damage and stun on crit (DC 13 Wis or stunned 1 round). | Thorn pierces memory—harvester loses a recent memory (GM discretion). |
| **Dreampod** (R) | Pod | When thrown, induces sleep in 10 ft radius (DC 13 Wis save). | Pod cracks prematurely—harvester falls asleep for 1d4 rounds. |
| **Echopetal** (UR) | Petal | Adds a disorienting echo to thrown potions: targets of the initial blast make the potion’s initial saving throw with disadvantage. | Causes visual doubling—disadvantage on next attack roll. |
| **Soulberry** (UR) | Berry | Restores 1d4 hit points and ends the charmed or frightened condition. | Berry crushes—harvester is dazed (can’t use reactions for 1 round). |
| **Visionsap** (UR) | Sap | Creates an AoE confusion burst (10 ft, DC 14 Int save or confused for 1 minute, repeating the save at the end of each turn). | Sap binds to skin—harvester relives old trauma (roleplay opportunity). |
| **Lucid Bulb** (L) | Bulb | Used in memory restoration or false memory creation potions. | Bulb pulses—harvester confused for 1 minute. |
}}

{{wide,strip,short
{{pimg
![Lucid Bulb](https://raw.githubusercontent.com/Omegaoliverid/Ampersand-s-Apothecary/52ab9f0ae9aedf06de291046c81bc2611d183a48/apo-26.jpg)
}}
#### Lucid Bulb
##### SPECIMEN · PSYCHIC
Lucid Bulbs thrive in quiet, hidden glades and shadowed groves where the veil between dreams and reality is thin. Often buried beneath leaf litter or nestled among ancient stones, their smooth, pale skins pulse faintly with soft blue light against the surrounding dark. They are used in potions that restore memories, or even fabricate false ones.
}}

{{footnote AMPERSAND'S APOTHECARIA | THE MINDWOVEN FLORA}}
{{pageNumber,auto}}

\page {ap27,specimen}
{{wide,chapterhead
##### THE FLORA ARCANA · EARTH
# The Stonebound Flora
Flora of the stone and soil grow in deep valleys, mountainous ridges, caverns, and ancient petrified forests. Earth-aligned plants are hardy and mineral-rich, offering effects tied to protection, physical power, grounding, and endurance.
}}

{{wide
## Potion Usage Guidelines
{{trio
{{card
#### Drinkable Potions (Internal)
- Enhances physical durability (temporary HP or resistance to bludgeoning)
- Grants tremorsense or improved balance/stability
- Increases Constitution checks or Strength-based saves
- Slows movement but provides massive staying power
}}
{{card
#### Throwable Potions (External Burst)
- Causes terrain upheaval (difficult terrain or small stone spikes)
- Buries or knocks prone enemies in small radius
- Petrification or partial hardening effects (temporary immobilisation)
- Suppresses air or flying creatures in the area
}}
{{card
#### Ointments (Weapon/Armour)
- Coats weapons with seismic impact (bonus to bludgeoning damage or knockback)
- Applies to armour to grant temporary AC bonus or resistance to force/bludgeoning
- May grant immunity to prone or movement-based effects for a short time
}}
}}
}}

{{wide,strip
{{pimg
![Stoneleaf](https://raw.githubusercontent.com/Omegaoliverid/Ampersand-s-Apothecary/52ab9f0ae9aedf06de291046c81bc2611d183a48/apo-27.jpg)
}}
#### Stoneleaf
##### SPECIMEN · EARTH
Stoneleaf plants dot the rocky slopes and rugged escarpments of craggy mountains and arid canyons. Their thick, leathery leaves are mottled grey and green, blending seamlessly with stony terrain. These hardy plants thrive in poor, gravelly soil, often clinging to cliff faces or nestled among loose stones.
}}

{{footnote AMPERSAND'S APOTHECARIA | THE STONEBOUND FLORA}}
{{pageNumber,auto}}

\page {ap28,plantlist}
{{wide,flora
## Earth-Aligned Plants

| Plant Name           | Harvestable Part | Alchemical Properties | Severe Harvest Failure |
|----------------------|------------------|-----------------------------------------------------------------------------------|----------------------------------------------------------------------------------|
| **Cragflower** (C) | Petal | Used for creating difficult terrain (5 ft stone growth per use). | Petal turns to dust—useless. |
| **Stoneleaf** (U) | Leaf | Used in fortitude potions (temp HP +2d4). | The leaf releases a cloud of abrasive grit—DC 12 Con save or gain one level of exhaustion. |
| **Terraroot** (U) | Root | Brewed for Constitution save advantage vs poison/disease. | Root seeps clay—harvester stuck, movement halved for 1 minute. |
| **Shardbark** (U) | Bark | Used in armour ointments for deflection: for 1 minute, a creature that hits the coated armour with a melee attack takes 1 piercing damage. | Bark splinters on touch—1d4 slashing damage. |
| **Marblepod** (U) | Pod | When thrown, explodes with stone shrapnel (5 ft, 2d6 bludgeoning). | Pod bursts in hand—takes full damage. |
| **Claydrip Sap** (U) | Sap | Thickens potions or ointments—doubles duration of non-damaging earth effects. | Solidifies instantly—ruins harvesting tool until cleaned. |
| **Basalt Berry** (U) | Berry | Temporarily boosts Strength-based checks (advantage for 1 hour). | Berry hardens and cracks teeth—harvester takes 1d4 force damage. |
| **Earthspore Puff** (U) | Spores | Creates dust cloud—heavily obscures area, 10 ft radius for 1 min. | Spores cling—harvester becomes obvious (disadvantage on Stealth) for 1 hour. |
| **Petraleaf** (U) | Leaf | Grants short-term petrification resistance. | Turns hand stiff—cannot use for fine actions for 10 mins. |
| **Stonecap Fungus** (R) | Spores | Grants resistance to bludgeoning for 1 hour. | Turns brittle—harvester’s next attack roll suffers disadvantage. |
| **Ironvine** (R) | Vine | Used in armour ointments (grants +1 AC for 10 mins). | Vine lashes around limb—restrained until DC 13 Str save succeeds. |
| **Dustbloom** (R) | Flower (Whole) | Throws up choking dust when thrown (10 ft, DC 13 Con save or blinded). | Bloom erupts—harvester blinded for 1 minute. |
| **Gritleaf** (R) | Leaf | Boosts endurance—gives resistance to exhaustion for 1 hour. | Bitter residue—disadvantage on next Con save. |
| **Magnetroot** (R) | Root | Adds magnetic pulse to weapon (attracts metal or disrupts metal armour). | Root triggers local magnetic burst—metal items pulled/stuck for 1d4 rounds. |
| **Pebblethorn** (UR) | Thorn | Coats weapon with stone splinter strike (1d4 piercing + 1d4 force). | Thorn embeds in hand—1d6 damage and painful swelling (disadvantage on attacks). |
}}

{{wide,strip
{{pimg
![Marblepod](https://raw.githubusercontent.com/Omegaoliverid/Ampersand-s-Apothecary/52ab9f0ae9aedf06de291046c81bc2611d183a48/apo-28.jpg)
}}
#### Marblepod
##### SPECIMEN · EARTH
A tough, succulent plant in rocky deserts and cliffs. Its stone-like husk resembles fused mineral rocks, blending with the terrain. When disturbed, it explodes in a burst of jagged stone shrapnel, damaging everything nearby. Its exterior stores water and minerals, making it highly resilient but dangerous to harvest without caution.
}}

{{footnote AMPERSAND'S APOTHECARIA | THE STONEBOUND FLORA}}
{{pageNumber,auto}}

\page {ap29,specimen}
{{wide,chapterhead
##### THE FLORA ARCANA · WATER
# The Tideborn Flora
Flora aligned with water flourish in coastal shallows, deep lakes, swamps, and tidal grottos. These plants embody adaptability, purification, flow, and memory. Their alchemical properties often focus on fluidity, healing, water manipulation, and emotional resonance.
}}

{{wide
## Potion Usage Guidelines
{{trio
{{card
#### Drinkable Potions (Internal)
- Restores vitality or quenches fatigue (healing, remove exhaustion)
- Grants ability to breathe underwater or swim speed
- Enhances memory or insight through "echoes of the tide"
- Removes toxins or diseases through purification
}}
{{card
#### Throwable Potions (External Burst)
- Drenches targets (extinguishing fire, hindering movement)
- Creates slick terrain (10 ft area, creatures must save or fall prone)
- Conjures fog or obscuring mist for stealth or confusion
- Triggers tidal push (small knockback or reposition effect)
}}
{{card
#### Ointments (Weapon/Armour)
- Coats weapons with fluid kinetic energy (bonus to attack rolls, adds splash effect)
- Applies to armour for resistance to fire or elemental damage
- Grants water-walking or slipperiness (advantage on escape attempts)
}}
}}
}}

{{wide,strip
{{pimg
![Lagoon Thorn](https://raw.githubusercontent.com/Omegaoliverid/Ampersand-s-Apothecary/52ab9f0ae9aedf06de291046c81bc2611d183a48/apo-29.jpg)
}}
#### Lagoon Thorn
##### SPECIMEN · WATER
Lagoon Thorns form dense thickets along the edges of tranquil lakes and brackish waters. Their long, sharp thorns glow with a faint bioluminescence and serve to push back intruders or act as natural traps.
}}

{{footnote AMPERSAND'S APOTHECARIA | THE TIDEBORN FLORA}}
{{pageNumber,auto}}

\page {ap30,plantlist}
{{wide,flora
## Water-Aligned Plants

| Plant Name           | Harvestable Part | Alchemical Properties | Severe Harvest Failure |
|----------------------|------------------|-----------------------------------------------------------------------------------|----------------------------------------------------------------------------------|
| **Fogspore** (C) | Spores | Generates obscuring mist when thrown (5 ft fog cloud, 1 min duration). | Spores cling to skin—disadvantage on Stealth for 10 minutes. |
| **Rillstem** (C) | Stem | Boosts healing effects of potion by +2 HP. | Breaks and spoils nearby ingredients (1d4 other materials lost). |
| **Kelproot** (U) | Root | Brew grants a swimming speed of 30 ft for 1 hour; use an existing higher swimming speed instead. | Root tangles tool—harvester restrained for 1 round unless DC 13 Dex save. |
| **Mistleaf** (U) | Leaf | When brewed, creates fog cloud (10 ft radius). | Leaf wilts—no useful effect. |
| **Bubblevine** (U) | Vine | Infused into potions for underwater breathing (1 hour). | Vine bursts—harvester inhales water vapour, begins choking (DC 12 Con save). |
| **Tideblossom** (U) | Flower (Whole) | Grants enhanced memory or recall (advantage on Int checks for 1 hour). | Causes memory lapse—disadvantage on Int-based rolls for 10 minutes. |
| **Riverberry** (U) | Berry | Restores 2d4 HP when consumed. | Spoiled berry—causes nausea (disadvantage on all rolls for 1 minute). |
| **Lagoon Thorn** (U) | Thorn | Adds a push effect on weapon hit (DC 12 Str save or knocked back 5 ft). | Thorn splinters—1d4 damage and disadvantage on next attack roll. |
| **Tidepod** (U) | Pod | When thrown, creates a water burst (10 ft radius knockback, light bludgeoning). | Explodes during harvest—harvester knocked prone and takes 1d6 bludgeoning. |
| **Moonkelp** (R) | Leaf | Used for calm emotions or sleep effects. | Releases drowsy pollen—harvester makes DC 13 Wis save or becomes drowsy. |
| **Driftsap** (R) | Sap | Adds flowing motion to thrown potions (expands 5 ft radius effects by +5 ft). | Sap hardens immediately—destroys the flask it’s stored in. |
| **Mirrorbulb** (R) | Bulb | Used for reflection potions (reaction-based effects like the Shield spell or a parry). | Bulb pulses—harvester is dazzled (disadvantage on Perception for 10 minutes). |
| **Shellfern** (R) | Leaf | Grants temporary armour (AC +1 for 1 hour). | Leaf flakes apart—no effect. |
| **Coralbark** (UR) | Bark | Adds armour resistance to piercing/slashing for 10 minutes. | Sharp fragments cut hand—1d6 piercing damage. |
| **Dewseed** (UR) | Seed | Grants hydration and fatigue removal (removes 1 level of exhaustion). | Seed bursts in pouch—soaks supplies, making 1 item unusable until dried. |
}}

{{wide,strip
{{pimg
![Mistleaf](https://raw.githubusercontent.com/Omegaoliverid/Ampersand-s-Apothecary/52ab9f0ae9aedf06de291046c81bc2611d183a48/apo-30.jpg)
}}
#### Mistleaf
##### SPECIMEN · WATER
Mistleaf flourishes in shady, humid forests near streams or waterfalls. Its broad, delicate leaves shimmer with moisture, often beaded with tiny droplets, and release a faint mist when touched or brewed, forming fog clouds that obscure vision.
}}

{{footnote AMPERSAND'S APOTHECARIA | THE TIDEBORN FLORA}}
{{pageNumber,auto}}

\page {ap31,specimen}
{{wide,chapterhead
##### THE FLORA ARCANA · AIR
# The Skyborne Flora
Plants attuned to air flourish on high peaks, floating isles, windswept plains, and cliffside crags. These flora are defined by mobility, lightness, breath, and sound. Their effects often manipulate wind, silence or amplify sound, aid in movement, or produce concussive force (thunder).
}}

{{wide
## Potion Usage Guidelines
{{trio
{{card
#### Drinkable Potions (Internal)
- Enhances breath control or grants windstep (advantage on Dexterity saves or movement-based checks)
- Grants feather fall or slow descent
- Amplifies voice or hearing (advantage on Persuasion/Perception)
- Removes exhaustion caused by thin air or exertion
}}
{{card
#### Throwable Potions (External Burst)
- Generates shockwaves (thunder damage in a radius, knockback)
- Disperses fog or gas (clears 10 ft radius on impact)
- Disorients with high-frequency sound (deafening or disorienting effects)
- Creates gusts or upward drafts (launches light objects or creatures)
}}
{{card
#### Ointments (Weapon/Armour)
- Adds thunder damage to weapons (1d4 or 1d6 on hit)
- Increases dodge or parry capabilities (brief movement bonuses)
- Buffs armour with reactive air shields (1 use of Shield-like effect)
}}
}}
}}

{{wide,plate
{{pimg
![Windreed Thorn](https://raw.githubusercontent.com/Omegaoliverid/Ampersand-s-Apothecary/52ab9f0ae9aedf06de291046c81bc2611d183a48/apo-31.jpg)
}}
{{ptext
#### Windreed Thorn
##### SPECIMEN · AIR
Windreed Thorns thrive in breezy coastal cliffs and open plains swept by frequent gales. Their long, flexible stems are studded with sharp, dark thorns that shimmer with faint static. These plants sway and bend relentlessly with the wind, collecting atmospheric energy.
}}
}}

{{footnote AMPERSAND'S APOTHECARIA | THE SKYBORNE FLORA}}
{{pageNumber,auto}}

\page {ap32,plantlist}
{{wide,flora
## Air-Aligned Plants

| Plant Name           | Harvestable Part | Alchemical Properties | Severe Harvest Failure |
|----------------------|------------------|----------------------------------------------------------------------------------|----------------------------------------------------------------------------------|
| **Zephyroot** (U) | Root | Grants Feather Fall for 10 minutes when brewed. | Root whips violently—harvester must pass DC 12 Dex save or fall prone. |
| **Whirlvine** (U) | Vine | Used in thrown potions for knockback effects (5–10 ft). | Vines unravel suddenly—harvester loses grip, dropping all tools. |
| **Galeleaf** (U) | Leaf | Adds windstep effect—boosts speed by +10 ft for 1 hour. | Leaf disintegrates into a blinding flurry—temporary blindness for 1 round. |
| **Galebloom** (U) | Flower (Whole) | Bursts with sound—adds 1d6 thunder damage to potions. | Emits deafening pop—DC 13 Con save or deafened for 1 minute. |
| **Driftberry** (U) | Berry | Ingested to gain advantage on Acrobatics and Athletics for 10 minutes. | Makes user dizzy instead—disadvantage on movement checks for 5 minutes. |
| **Windreed Thorn** (U) | Thorn | Adds thunder damage + chance to deafen (DC 12 Con save). | Thorn cracks loudly—deafens harvester for 1 minute. |
| **Burstpod** (U) | Pod | When thrown, emits a sonic blast (2d6 thunder, 10 ft radius). | Explodes while harvesting—2d6 thunder, DC 13 Dex save or drop prone. |
| **Echoseed** (U) | Seed | Imbues potions with reverberating effects (the damage repeats once at the start of the thrower's next turn). | Seeds rattle—alerting nearby creatures (if stealthing). |
| **Driftspores** (U) | Spores | Lighten the air—used in levitation or stealth potions. | Spores cling—disadvantage on Stealth due to glowing cloud. |
| **Breezebulb** (U) | Bulb | Grants air burst to thrown potions (pushes enemies or objects on impact). | Pops prematurely—harvester shoved 5 ft back, must make DC 12 Dex save. |
| **Skywhorl Petal** (R) | Petal | Grants short-term levitation (10 ft hover for 1 minute). | Petals float off—no usable material gained. |
| **Stormbark** (R) | Bark | Enhances armour with wind-buffer (resistance to bludgeoning for 1 minute). | Bark splinters explode—1d4 piercing + push 5 ft from harvest site. |
| **Airsap** (R) | Sap | Expands a thrown potion radius by +5 ft, or by +10 ft instead if combined with thunder plants. | Sap bursts open—harvester deafened for 1d4 minutes. |
| **Tremblestem** (R) | Stem | Boosts thunder spells or thrown potion intensity. | Stem vibrates—harvester must drop it or take 1d4 thunder damage. |
}}

{{wide,strip,short
{{pimg
![Skywhorl Petal](https://raw.githubusercontent.com/Omegaoliverid/Ampersand-s-Apothecary/52ab9f0ae9aedf06de291046c81bc2611d183a48/apo-32.jpg)
}}
#### Skywhorl Petal
##### SPECIMEN · AIR
Skywhorl blossoms in the highest mountain meadows and on floating cloud islands, where the air is thin and currents are strong. Its bright, silvery petals shimmer and rotate gently in the breeze, as if reflecting the sky itself. Prized for levitation spells and effects, the delicate, hovering petals are tricky to gather: mishandle them and they float away, leaving no useful material behind.
}}

{{footnote AMPERSAND'S APOTHECARIA | THE SKYBORNE FLORA}}
{{pageNumber,auto}}

\page {ap33,specimen}
{{wide,chapterhead
##### THE FLORA ARCANA · POISON
# The Toxin-Touched Flora
Poisonous plants are found in swamps, shadowy forests, corrupted glades, and areas of decay or death. Their effects range from paralytics and hallucinogens to necrotic degeneration or mental disruption. While deadly, they offer precise and powerful tools for those skilled enough to wield them.
}}

{{wide
## Potion Usage Guidelines
{{trio
{{card
#### Drinkable Potions (Internal Use)
- Induces immunity or resistance to poison/disease (temporary)
- Produces altered states: trance, hallucinations, sleep, or rage
- Grants venomous bite (for races with natural attacks)
- Used for dark rituals (e.g., speaking with spirits or dreams)
}}
{{card
#### Throwable Potions (Area or Direct Contact)
- Spreads toxic clouds or splashes that cause Con saves or take poison damage
- Induces nausea, paralysis, blindness, or confusion
- Creates lingering zones of corruption or contamination
}}
{{card
#### Ointments (Weapon/Armour Use)
- Coats weapons in venom (adds poison damage or save vs effect)
- Weakens enemy Constitution on hit (DC save)
- Armour applications may harm attackers (e.g., reactive poison on contact)
}}
}}
}}

{{wide,strip
{{pimg
![Nightfang Root](https://raw.githubusercontent.com/Omegaoliverid/Ampersand-s-Apothecary/52ab9f0ae9aedf06de291046c81bc2611d183a48/apo-33.jpg)
}}
#### Nightfang Root
##### SPECIMEN · POISON
Nightfang roots grow deep in shadowy caves and dark, damp forests where no sunlight reaches. Thick, gnarled and black-tinted, they often wear a faint, oily sheen. Beneath their menacing look lie potent toxins that can cause nausea and poisoning if touched—ideal for concocting venom resistance potions.
}}

{{footnote AMPERSAND'S APOTHECARIA | THE TOXIN-TOUCHED FLORA}}
{{pageNumber,auto}}

\page {ap34,plantlist}
{{wide,flora
## Poison-Aligned Plants

| Plant Name           | Harvestable Part | Alchemical Properties | Severe Harvest Failure |
|----------------------|------------------|--------------------------------------------------------------------------------|----------------------------------------------------------------------------------|
| **Nightfang Root** (U) | Root | Brewed into venom resistance potion (1 hour). | Causes nausea on contact—DC 12 Con save or poisoned for 1 hour. |
| **Venomseed** (U) | Seed | Adds delayed poison effect to potions (triggers 1 round later). | Seed releases slowly—harvester suffers 1d4 poison damage every minute for 3 min. |
| **Blackresin** (U) | Resin | Sticky and potent—adds duration to poison effects. | Resin bonds to gloves or tools—harvester must clean gear (10 min delay). |
| **Vilevine** (R) | Vine | In a thrown potion, restrains and poisons: on a failed Con save, 1d4 poison, poisoned until the end of the target's next turn, and restrained for up to 1 minute (escape DC 14). | Vine wraps harvester’s limb—restrained until cut free. |
| **Rotleaf** (R) | Leaf | Applied to weapons to deal 1d4 poison on hit. | Leaf emits foul gas—harvester makes DC 13 Con save or retches for 1 round. |
| **Weepblossom** (R) | Flower (Whole) | Causes sadness and lethargy: DC 14 Wis save or speed reduced by 10 ft for 1 minute (repeat the save at the end of each turn). | Touch induces sorrow—harvester suffers 1 level of exhaustion. |
| **Dreampetal** (R) | Petal | Induces vivid dreams or sleep—used in sleeping draughts or visions. | Harvester must succeed DC 14 Wis save or fall asleep for 1 minute. |
| **Witchberries** (R) | Berry | Used in poisons to cause hallucinations or psychic disruption. | Berries burst—harvester experiences visions (confused for 1d4 rounds). |
| **Blightbark** (R) | Bark | Adds necrotic damage to poison-based attacks. | Bark flakes infect harvester—must save or take 1d6 necrotic over 3 rounds. |
| **Needlethorn** (R) | Thorn | Coats weapons with piercing venom: each hit deals an extra 1d4 poison damage. | Thorn pierces skin—harvester takes 1d6 poison and makes DC 13 Con save. |
| **Fume Pod** (R) | Pod | Bursts into a 10 ft poison cloud: DC 14 Con save or poisoned for 1 minute (repeat the save at the end of each turn). | Pod ruptures on contact—5 ft burst poisons harvester and nearby creatures. |
| **Sporeveil** (R) | Spores | Disperses as a blinding cloud: DC 14 Con save or blinded until the end of the target's next turn. | Spores cling to eyes—harvester is blinded for 1d4 rounds. |
| **Toxsap** (UR) | Sap | Used for paralysis-inducing poison (target loses movement if failed save). | Sap seeps into skin—harvester’s arm numbs (disadvantage on next attack). |
| **Venom Bulb** (UR) | Bulb | Grants temporary venom immunity or transformation into venomous form. | Bulb ruptures—harvester is poisoned and hallucinating for 1d6 minutes. |
}}

{{wide,plate
{{pimg
![Weepblossom](https://raw.githubusercontent.com/Omegaoliverid/Ampersand-s-Apothecary/52ab9f0ae9aedf06de291046c81bc2611d183a48/apo-34.jpg)
}}
{{ptext
#### Weepblossom
##### SPECIMEN · POISON
Weepblossoms flourish in foggy marshes and shadowed woodland glades, their drooping flowers forever dripping thick, dark nectar. The petals give off a faint, sorrowful scent, and their touch can induce melancholy and lethargy in enemies.
}}
}}

{{footnote AMPERSAND'S APOTHECARIA | THE TOXIN-TOUCHED FLORA}}
{{pageNumber,auto}}

\page {ap35,specimen}
{{wide,chapterhead
##### THE FLORA ARCANA · INFERNAL
# Infernal Flora of the Damned
Infernal plants are the spawn of cursed soil and planar bleeding—twisted echoes of nature corrupted by demonic or devilish power. These rare and dangerous flora are imbued with hatred, fear, and domination, often warping those who wield them. Infernal flora may manifest where pacts were made, where infernal creatures walked, or in landscapes cursed by ancient evil.
}}

{{wide
## Potion Usage Guidelines
{{trio
{{card
#### Drinkable Potions (Internal Use)
- Grants temporary fire resistance or immunity (devilish protection)
- Infuses dark charisma or intimidation (bonus to social manipulation)
- Induces berserk fury (rage-like effects)
- Enhances fear-based or domination spells
}}
{{card
#### Throwable Potions (External)
- Causes enemies to become frightened (area of fear)
- Releases bursts of hellfire (fire + necrotic damage)
- Corrupts terrain with infernal energy (difficult terrain, curse zones)
- Summons minor infernal spirits or haunting illusions
}}
{{card
#### Ointments (Weapon/Armour Use)
- Adds necrotic + fire damage on hit
- Causes fear on strike (target must save or be frightened)
- Reflects a portion of damage taken back at attacker (armour)
- Smoulders with infernal heat (may ignite items on contact)
}}
}}
}}

{{wide,plate
{{pimg
![Bloodberry](https://raw.githubusercontent.com/Omegaoliverid/Ampersand-s-Apothecary/52ab9f0ae9aedf06de291046c81bc2611d183a48/apo-35.jpg)
}}
{{ptext
#### Bloodberry
##### SPECIMEN · INFERNAL
Bloodberries grow in cursed, blood-soaked soils within infernal or fiendish domains. Their glossy, deep-red berries pulse with a sinister life force, often dripping with dark ichor. They serve blood magic and healing rituals of fiendish origin, yet touching or harvesting them improperly lets the berries absorb lifeforce, inflicting necrotic damage on the harvester and leaving a dark, lingering mark.
}}
}}

{{footnote AMPERSAND'S APOTHECARIA | INFERNAL FLORA OF THE DAMNED}}
{{pageNumber,auto}}

\page {ap36,plantlist}
{{wide,flora
## Infernal-Aligned Plants

| Plant Name           | Harvestable Part | Alchemical Properties | Severe Harvest Failure |
|----------------------|------------------|----------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|
| **Charleaf** (U) | Leaf | Brewed for intimidation or charisma boosts (+1d4 to Intimidation for 1 hour). | Leaf explodes in smoke—DC 12 Con save or blinded for 1 minute. |
| **Bloodberry** (U) | Berry | Used in blood magic or healing via fiendish means (heals, but leaves a mark). | Berry absorbs lifeforce—harvester takes 1d4 necrotic per berry touched. |
| **Hellsap** (U) | Sap | For 1 minute, +2 damage with melee weapon attacks and −2 AC. Grants no Rage feature or damage resistance. | Sap enrages harvester—must attack nearest creature next turn. |
| **Ashroot** (R) | Root | Grants fire resistance and infernal aura for 1 hour. | Burns harvester's hand—1d6 fire + frightened for 1 round. |
| **Hellbind Vine** (R) | Vine | Used to entangle and cause burning pain—target restrained and takes 1d4 fire. | Vine coils around harvester—must save or be restrained for 1 minute. |
| **Blazebloom** (R) | Flower (Whole) | Explodes with black hellfire—good for thrown potions (2d6 fire, then DC 14 Wis save or frightened until the end of the target's next turn). | Bursts during harvest—harvester takes 2d6 fire and is frightened. |
| **Dreadpetal** (R) | Petal | Adds fear to any potion: DC 14 Wis save or frightened until the end of the target's next turn. | Petal releases a scream—harvester must save or be frightened. |
| **Cinderbark** (R) | Bark | Adds smouldering flame to weapons (1d4 fire damage). | Bark ignites on harvest—burns gear or starts a small fire nearby. |
| **Emberthorn** (R) | Thorn | Inflicts burning wounds (target takes 1d4 fire + 1 bleed per round). | Thorn pierces harvester—same effect as successful hit on self. |
| **Wailpod** (R) | Pod | Bursts into psychic wails: choose when brewing either psychic damage or fear (DC 14 Wis save or frightened until the end of the target's next turn). | Pod ruptures—harvester takes 1d6 psychic and gains Disadvantage on next save. |
| **Fumespores** (R) | Spores | Fills the binder's radius with heavily obscuring smoke for 1 minute; a creature first caught in it makes a DC 14 Wis save or is frightened until the end of its next turn. | Spores invade lungs—harvester makes Con save or suffers poisoned condition. |
| **Pitchresin** (R) | Resin | Burns with black fire—used in throwing potions or traps (persistent fire). | Resin clings—harvester must douse themselves or take 1d6 fire/round. |
| **Infernal Bulb** (R) | Bulb | For 1 minute, advantage on melee attack rolls and vulnerability to radiant damage. | Bulb overloads harvester—must save or gain berserk + attack nearest ally. |
| **Soulseed** (L) | Seed | Used to trap or hold souls (rituals or necrotic potions). | Seed attempts to bind harvester’s soul—DC 15 Cha save or take 1 level exhaustion. |
}}

{{wide,strip
{{pimg
![Hellsap](https://raw.githubusercontent.com/Omegaoliverid/Ampersand-s-Apothecary/52ab9f0ae9aedf06de291046c81bc2611d183a48/apo-36.jpg)
}}
#### Hellsap
##### SPECIMEN · INFERNAL
This ominous glowing sap is extracted from the gnarled, corrupted trees that have been infected with infernal energy. These twisted trees, found deep within dark, cursed groves on the edges of desolate battlegrounds, bleed a viscous, amber-coloured sap when pruned or squeezed. The sap gleams with fiery embers and a dark infernal light, shimmering as it flows freely from jagged wounds in the bark. 
}}

{{footnote AMPERSAND'S APOTHECARIA | INFERNAL FLORA OF THE DAMNED}}
{{pageNumber,auto}}

\page {ap37,specimen}
{{wide,chapterhead
##### THE FLORA ARCANA · ELDRITCH
# Eldritch Flora of the Beyond
Eldritch flora are not native to the Material Plane—they sprout near dimensional rifts, in reality-warped lands, or in proximity to incursions from the Outer Void. These plants pulse with psychic hums, alien geometry, or oozing sap that defies logic. Often unpredictable, they interact with minds, probability, and the boundaries between planes.

They are powerful, mysterious, and sometimes corrupting. Handle with care—or curiosity.
}}

{{wide
## Potion Usage Guidelines
{{trio
{{card
#### Drinkable Potions (Internal Use)
- Opens the mind to hidden truths (Speak with Dead, Comprehend Languages, or Detect Thoughts)
- Grants psychic resistance or telepathy for a short time
- Induces prophetic dreams (or hallucinations)
- Allows brief glimpses into other planes or alternate realities
}}
{{card
#### Throwable Potions (External)
- Causes disorientation or madness in affected targets (Confusion/Disadvantage on Int/Wis saves)
- Rips reality briefly (teleport/banish-style effects)
- Emits waves of psychic energy (psychic damage in 5–10 ft radius)
- Creates zones of silence, fear, or mind-blanking fog
}}
{{card
#### Ointments (Weapon/Armour Use)
- Coated weapons deal additional psychic or chaos damage
- Armour reflects mind-affecting magic or causes backlash to charm/fear effects
- Adds minor defensive "shimmer"—a chance to blink or displace when struck
}}
}}
}}

{{wide,strip
{{pimg
![Umbral Bloom](https://raw.githubusercontent.com/Omegaoliverid/Ampersand-s-Apothecary/52ab9f0ae9aedf06de291046c81bc2611d183a48/apo-37.jpg)
}}
#### Umbral Bloom
##### SPECIMEN · ELDRITCH
Umbral blooms grow in the darkest corners of shadowed groves, where eldritch energies pulse subtly beneath the surface. Their large, ever-shifting black flowers have petals that seem to ripple as if made of shadow. Once brewed, Umbral Bloom cloaks the drinker in a veil of darkness and concealment, making them harder to target.
}}

{{footnote AMPERSAND'S APOTHECARIA | ELDRITCH FLORA OF THE BEYOND}}
{{pageNumber,auto}}

\page {ap38,plantlist}
{{wide,flora
## Eldritch-Aligned Plants

| Plant Name            | Harvestable Part | Alchemical Properties | Severe Harvest Failure |
|-----------------------|------------------|------------------------------------------------------------------------------------|--------------------------------------------------------------------------------|
| **Nullroot** (U) | Root | Grants resistance to psychic damage and silences thoughts (1 hour). | Root emits a psychic scream—DC 14 Int save or stunned for 1 round. |
| **Whisperbark** (U) | Bark | Used in mental shielding salves (advantage vs charm/fear effects). | Bark murmurs secrets—harvester must pass Wis save or reveal a truth aloud. |
| **Ghastroot Bulb** (U) | Bulb | Adds random-effect chance to potions (can create wild magic burst). | Bulb triggers surge—the next spell the harvester casts within 1 minute also triggers a random magical side effect of the GM’s choice. |
| **Skitterleaf** (R) | Leaf | Adds confusion effect to thrown potions (5 ft, 1 round). | Leaf scrambles reality—harvester gains one random condition (GM choice) 1 min. |
| **Mindspike Petal** (R) | Petal | Inflicts psychic damage + chance to stun (1d4 psychic + DC 12 Int save). | Harvester takes 1d6 psychic damage and hears whispers for 1 hour. |
| **Ectoberry** (R) | Berry | Allows communication with spirits/ethereal forms (10 mins). | Berry bursts—harvester must make DC 13 Cha save or become Frightened 1 min. |
| **Oculithorn** (R) | Thorn | Coated weapon strikes cut through illusions: advantage on one attack each turn against a target hidden by an illusion whose location you know. | Thorn pierces deeply—harvester sees overlapping realities (disadvantage Perception). |
| **Whimspores** (R) | Spores | Creates a confusing fog: creatures in the area make a DC 14 Wis save or have disadvantage on their next attack roll before the end of their next turn. | Spores induce mild madness—harvester has -1 to Wis saves for 1 hour. |
| **Thoughtseed** (R) | Seed | Causes insight or future glimpse (1 reroll of any d20 within next hour). | Harvester glimpses something terrible—disadvantage on next Wisdom check. |
| **Warpvine** (UR) | Vine | When brewed, enables short-range teleportation (Blink-like effect). | Vine coils into a paradox loop—harvester loses their action next round. |
| **Umbral Bloom** (UR) | Flower (Whole) | Cloaks drinker in shifting shadows—attack rolls against the drinker have disadvantage (1 min). | Bloom explodes in tendrils—restrains harvester (escape DC 13). |
| **Slipresin** (UR) | Resin | Grants limited invisibility or visual distortion for 1 minute. | Resin coats the harvester—they flicker visibly for 10 minutes (no stealth). |
| **Fracturepod** (UR) | Pod | When thrown, causes a 10 ft psychic burst (2d6 psychic, and confused for 1 round on a failed save). | Pod distorts space—harvester and nearby target switch places. |
| **Seethe Resin** (UR) | Resin | Doubles thrown potion AoE radius but adds instability (roll for mishap on use). | Resin boils—burns harvester for 1d6 force damage. |
}}

{{wide,strip
{{pimg
![Thoughtseed](https://raw.githubusercontent.com/Omegaoliverid/Ampersand-s-Apothecary/52ab9f0ae9aedf06de291046c81bc2611d183a48/apo-38.jpg)
}}
#### Thoughtseed
##### SPECIMEN · ELDRITCH
Thoughtseeds flourish amid the eldritch chaos of warped forests, where the fabric of reality seems thin. The small, dark seeds lie embedded in clumps of twisted, blackened soil, often hidden beneath layers of haunted moss. In the wild they stay dormant, pulsing faintly with mental energy; once planted or disturbed, they can grant glimpses of future events or distant thoughts—valuable but dangerous.
}}

{{footnote AMPERSAND'S APOTHECARIA | ELDRITCH FLORA OF THE BEYOND}}
{{pageNumber,auto}}

\page {ap39,specimen}
{{wide,chapterhead
##### THE FLORA ARCANA · ARCANE
# Arcane-Touched Flora
Arcane flora are plants infused with raw magical essence. Found near ancient ley lines, wizard towers, or dimensional anomalies, these plants react strongly to structured spellcasting and arcane rituals. Their properties amplify, stabilise, or replenish magical energies, making them invaluable to spellcasters.
}}

{{wide
## Potion Usage Guidelines
{{trio
{{card
#### Drinkable Potions (Internal Use)
- Restores a spent spell slot (Level 1, 2, or 3 depending on plant potency)
- Increases arcane focus or concentration (advantage on Constitution saves to maintain spells)
- Temporarily boosts spell attack rolls or DCs
- Grants a brief surge of arcane energy (free casting of cantrip or low-level spell)
- Enhances ritual casting (reduce time or eliminate material cost)
}}
{{card
#### Throwable Potions (External Use)
- Dispel minor enchantments in an area (Dispel Magic-like burst)
- Create wild magic zones or random magical effects
- Create arcane traps or glyph-like temporary sigils
- Interrupt spellcasting with bursts of nullifying force (Counterspell-lite effect)
}}
{{card
#### Ointments (Weapon/Armour Use)
- Coat a weapon to deliver bonus force or arcane damage
- Coat armour for resistance to force/psychic or to suppress magical detection
- Imbue items with temporary enchantment effects (e.g., +1 to hit, magic glow)
}}
}}
}}

{{wide,plate
{{pimg
![Mystvine](https://raw.githubusercontent.com/Omegaoliverid/Ampersand-s-Apothecary/52ab9f0ae9aedf06de291046c81bc2611d183a48/apo-39.jpg)
}}
{{ptext
#### Mystvine
##### SPECIMEN · ARCANE
Mystvines cling to the crumbling stone walls of abandoned arcane sanctuaries and towers. Their thick, snaking vines shimmer with an iridescent sheen, covered in tiny sparkling runes that pulse with raw magic. These vines are sought after for their ability to speed up ritual casting—often twisting around ancient relics or one another in complex patterns.
}}
}}

{{footnote AMPERSAND'S APOTHECARIA | ARCANE-TOUCHED FLORA}}
{{pageNumber,auto}}

\page {ap40,plantlist}
{{wide,flora
## Arcane-Aligned Plants

| Plant Name            | Harvestable Part | Alchemical Properties | Severe Harvest Failure |
|-----------------------|------------------|----------------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| **Mystvine** (U) | Vine | Enhances ritual magic: casting a spell as a ritual takes 5 extra minutes instead of 10. | Vine writhes and lashes—causes 1 turn of spellcasting interruption. |
| **Scrollleaf** (U) | Leaf | Grants a temporary +1 to spell attack rolls for 10 minutes. | Leaf disintegrates, inflicting 1d4 psychic damage to the harvester. |
| **Glimmerpetal** (U) | Petal | Adds shimmering light to potion or spell—functions like Faerie Fire. | Petal flares unexpectedly—harvester is Blinded for 1 round. |
| **Sigilbark** (U) | Bark | Used in armour salves—adds +1 to AC against spell attacks for 1 minute. | Bark etches glyphs into hand—DC 13 save or suffer Minor Curse effect. |
| **Leyresin** (U) | Resin | Infuses a weapon: +1 force damage on every hit for 1 minute. | Resin overloads item—next magic item used fizzles. |
| **Spellroot** (R) | Root | Brewed into a potion that restores one **Level 1 spell slot**. | Root releases raw magic—harvester must make DC 12 Int save or take 1d6 force. |
| **Focus Thorn** (R) | Thorn | Boosts concentration checks for spells (advantage for 10 mins). | Thorn pricks the mind—harvester takes -1 to concentration saves for 1 hour. |
| **Aethersap** (R) | Sap | When brewed and drunk, for 1 hour the drinker can once treat one cantrip damage die as its maximum. | Sap binds to harvester—disadvantage on next spellcasting check. |
| **Crystabulb** (R) | Bulb | Used in crafting wands/staves; brewing grants +1 DC to next spell cast. | Bulb fractures—harvester loses ability to cast 1 spell until short rest. |
| **Wizbloom** (UR) | Flower (Whole) | Brew to regain one **Level 2 spell slot**. | Bloom explodes in arcane force—1d6 force damage in 5 ft. |
| **Manaberry** (UR) | Berry | Restores a **Level 3 spell slot**, but causes 1 level of exhaustion. | Berry corrupts energy—harvester loses lowest-level prepared spell for 1 hour. |
| **Glyphpod** (UR) | Pod | When brewed into a throwable, creates a magical glyph trap in a 5-ft area. The GM determines its strength and stored effect from the recipe and campaign. | Pod misfires—glyph activates during harvest (effect at GM's discretion). |
| **Echo Spores** (L) | Spores | Causes last spell cast to echo—can recast without slot if cast within 1 min. | Spores confuse memory—caster forgets last spell until long rest. |
| **Codex Seed** (L) | Seed | When brewed and drunk, lets the caster cast one spell they don’t know, once, using their own spell slot (the spell must be on their class list and of a level they can cast). | Seed warps the mind—disadvantage on Arcana checks for 1 hour. |
}}

{{wide,tips
*Arcane flora are rarely wild—they bloom with purpose and power. They remember magic, echo intentions, and reshape the threads of magic. Respect them, and they may grant you mastery beyond books and blood.*

**Spell slot potions:** a creature can regain spell slots from only one Apothecaria potion per long rest.
}}

{{wide,strip,short
{{pimg
![Manaberry](https://raw.githubusercontent.com/Omegaoliverid/Ampersand-s-Apothecary/52ab9f0ae9aedf06de291046c81bc2611d183a48/apo-40.jpg)
}}
#### Manaberry
##### SPECIMEN · ARCANE
Manaberries thrive in enchanted groves near ancient arcane pools or nexus points where magical energies concentrate. Their small, luminous berries glow softly with a pulsating light—ranging from deep violet to shimmering blue.
}}

{{footnote AMPERSAND'S APOTHECARIA | ARCANE-TOUCHED FLORA}}
{{pageNumber,auto}}

\page {ap41,idxpage}
{{wide,chapterhead
##### REFERENCE · I
# Rarity and Habitat Index

An at-a-glance index to the 190 plants. Within each tier, entries are alphabetical. Discovery targets are **suggestions** for the species in a suitable habitat; the GM can set finer-grained targets, local exceptions, protected groves or alternate quest access. **Rarity marks:** C = Common, U = Uncommon, R = Rare, UR = Ultra Rare, L = Legendary. Botanical descriptions and art remain in their original affinity chapters.
}}

{{idx
## Common — discovery target 15 (8 plants)

| Plant | Affinity | Typical habitat |
|---|---|---|
| Cragflower | Earth | caves, cliffs, stony slopes |
| Fogspore | Water | rivers, lakes, wetlands |
| Lumenstem | Lightning | storm-struck highlands |
| Rillstem | Water | rivers, lakes, wetlands |
| Smoulderseed | Fire | volcanic fissures, ash fields |
| Snowmoss | Cold | tundra, glaciers, alpine forests |
| Solleaf | Radiant | sunlit meadows, sacred sites |
| Starberry | Radiant | sunlit meadows, sacred sites |
}}

{{idx
## Uncommon — discovery target 45 (89 plants)

| Plant | Affinity | Typical habitat |
|---|---|---|
| Aethershade Resin | Psychic | dream-haunted groves, mind-touched places |
| Ashbloom | Fire | volcanic fissures, ash fields |
| Aurastem | Radiant | sunlit meadows, sacred sites |
| Auric Resin | Radiant | sunlit meadows, sacred sites |
| Basalt Berry | Earth | caves, cliffs, stony slopes |
| Blackresin | Poison | toxic wetlands, fungal forests |
| Bloodberry | Infernal | cursed wastes, infernal sites |
| Boltberry | Lightning | storm-struck highlands |
| Breezebulb | Air | high mountains, wind-swept peaks |
| Brittle Stem | Cold | tundra, glaciers, alpine forests |
| Bubblevine | Water | rivers, lakes, wetlands |
| Burstpod | Air | high mountains, wind-swept peaks |
| Celestbark | Radiant | sunlit meadows, sacred sites |
| Charleaf | Infernal | cursed wastes, infernal sites |
| Charpod | Fire | volcanic fissures, ash fields |
| Chillseed | Cold | tundra, glaciers, alpine forests |
| Cinderroot | Fire | volcanic fissures, ash fields |
| Claydrip Sap | Earth | caves, cliffs, stony slopes |
| Coffinpod | Necrotic | graveyards, blighted ground |
| Crackbark | Lightning | storm-struck highlands |
| Dawnsroot | Radiant | sunlit meadows, sacred sites |
| Deathroot | Necrotic | graveyards, blighted ground |
| Dirgeseed | Necrotic | graveyards, blighted ground |
| Dragon’s Resin | Fire | volcanic fissures, ash fields |
| Driftberry | Air | high mountains, wind-swept peaks |
}}

\column

{{idx
## Uncommon — discovery target 45 (89 plants) (continued)

| Plant | Affinity | Typical habitat |
|---|---|---|
| Driftspores | Air | high mountains, wind-swept peaks |
| Earthspore Puff | Earth | caves, cliffs, stony slopes |
| Echoseed | Air | high mountains, wind-swept peaks |
| Emberberry | Fire | volcanic fissures, ash fields |
| Firesilk Petal | Fire | volcanic fissures, ash fields |
| Flameleaf | Fire | volcanic fissures, ash fields |
| Flashthorn | Lightning | storm-struck highlands |
| Frostbloom | Cold | tundra, glaciers, alpine forests |
| Frostpod | Cold | tundra, glaciers, alpine forests |
| Galebloom | Air | high mountains, wind-swept peaks |
| Galeleaf | Air | high mountains, wind-swept peaks |
| Gelid Resin | Cold | tundra, glaciers, alpine forests |
| Ghastroot Bulb | Eldritch | warped forests, planar rifts |
| Ghoulleaf | Necrotic | graveyards, blighted ground |
| Glacient Root | Cold | tundra, glaciers, alpine forests |
| Gleamvine | Radiant | sunlit meadows, sacred sites |
| Glimmerpetal | Arcane | ley lines, magical ruins |
| Gravepetal | Necrotic | graveyards, blighted ground |
| Gravetouch Thorn | Necrotic | graveyards, blighted ground |
| Halo Thorn | Radiant | sunlit meadows, sacred sites |
| Heavenpod | Radiant | sunlit meadows, sacred sites |
| Hellsap | Infernal | cursed wastes, infernal sites |
| Ignistalk | Fire | volcanic fissures, ash fields |
| Joltsap | Lightning | storm-struck highlands |
| Kelproot | Water | rivers, lakes, wetlands |
| Lagoon Thorn | Water | rivers, lakes, wetlands |
| Leyresin | Arcane | ley lines, magical ruins |
| Marblepod | Earth | caves, cliffs, stony slopes |
| Mindleaf | Psychic | dream-haunted groves, mind-touched places |
| Mireberry | Necrotic | graveyards, blighted ground |
| Mistleaf | Water | rivers, lakes, wetlands |
| Mistspores | Psychic | dream-haunted groves, mind-touched places |
| Molten Sap | Fire | volcanic fissures, ash fields |
| Mystvine | Arcane | ley lines, magical ruins |
| Nervevine | Psychic | dream-haunted groves, mind-touched places |
}}

{{footnote AMPERSAND'S APOTHECARIA | RARITY AND HABITAT INDEX}}
{{pageNumber,auto}}

\page {ap42,idxpage}
{{idx
## Uncommon — discovery target 45 (89 plants) (continued)

| Plant | Affinity | Typical habitat |
|---|---|---|
| Nightfang Root | Poison | toxic wetlands, fungal forests |
| Nullroot | Eldritch | warped forests, planar rifts |
| Permafrost Bulb | Cold | tundra, glaciers, alpine forests |
| Petraleaf | Earth | caves, cliffs, stony slopes |
| Pyrebark | Fire | volcanic fissures, ash fields |
| Reverie Seed | Psychic | dream-haunted groves, mind-touched places |
| Rimedust Spores | Cold | tundra, glaciers, alpine forests |
| Riverberry | Water | rivers, lakes, wetlands |
| Scrollleaf | Arcane | ley lines, magical ruins |
| Seraphsap | Radiant | sunlit meadows, sacred sites |
| Shardbark | Earth | caves, cliffs, stony slopes |
| Shiverberry | Cold | tundra, glaciers, alpine forests |
| Sigilbark | Arcane | ley lines, magical ruins |
| Sparkleaf | Lightning | storm-struck highlands |
| Sparkspore | Fire | volcanic fissures, ash fields |
| Stoneleaf | Earth | caves, cliffs, stony slopes |
| Stormseed | Lightning | storm-struck highlands |
| Sunbulb | Radiant | sunlit meadows, sacred sites |
| Terraroot | Earth | caves, cliffs, stony slopes |
| Thunderbloom | Lightning | storm-struck highlands |
| Tideblossom | Water | rivers, lakes, wetlands |
| Tidepod | Water | rivers, lakes, wetlands |
| Venomseed | Poison | toxic wetlands, fungal forests |
| Whirlvine | Air | high mountains, wind-swept peaks |
| Whisperbark | Eldritch | warped forests, planar rifts |
| Whisperstem | Psychic | dream-haunted groves, mind-touched places |
| Windreed Thorn | Air | high mountains, wind-swept peaks |
| Wyrmbark | Psychic | dream-haunted groves, mind-touched places |
| Zephyroot | Air | high mountains, wind-swept peaks |
}}

{{idx
## Rare — discovery target 60 (67 plants)

| Plant | Affinity | Typical habitat |
|---|---|---|
| Aethersap | Arcane | ley lines, magical ruins |
| Airsap | Air | high mountains, wind-swept peaks |
| Arcspores | Lightning | storm-struck highlands |
| Arcvine | Lightning | storm-struck highlands |
| Ashroot | Infernal | cursed wastes, infernal sites |
| Blazebloom | Infernal | cursed wastes, infernal sites |
| Blightbark | Poison | toxic wetlands, fungal forests |
}}

\column

{{idx
## Rare — discovery target 60 (67 plants) (continued)

| Plant | Affinity | Typical habitat |
|---|---|---|
| Blightsap | Necrotic | graveyards, blighted ground |
| Cinderbark | Infernal | cursed wastes, infernal sites |
| Corpsebloom | Necrotic | graveyards, blighted ground |
| Cracklepod | Lightning | storm-struck highlands |
| Crystabulb | Arcane | ley lines, magical ruins |
| Dawnseed | Radiant | sunlit meadows, sacred sites |
| Dreadpetal | Infernal | cursed wastes, infernal sites |
| Dreampetal | Poison | toxic wetlands, fungal forests |
| Dreampod | Psychic | dream-haunted groves, mind-touched places |
| Dreamroot | Psychic | dream-haunted groves, mind-touched places |
| Driftsap | Water | rivers, lakes, wetlands |
| Dustbloom | Earth | caves, cliffs, stony slopes |
| Eclipsed Bloom | Radiant | sunlit meadows, sacred sites |
| Ectoberry | Eldritch | warped forests, planar rifts |
| Emberthorn | Infernal | cursed wastes, infernal sites |
| Focus Thorn | Arcane | ley lines, magical ruins |
| Fulgurite Resin | Lightning | storm-struck highlands |
| Fume Pod | Poison | toxic wetlands, fungal forests |
| Fumespores | Infernal | cursed wastes, infernal sites |
| Funereal Resin | Necrotic | graveyards, blighted ground |
| Gloryspores | Radiant | sunlit meadows, sacred sites |
| Gritleaf | Earth | caves, cliffs, stony slopes |
| Hellbind Vine | Infernal | cursed wastes, infernal sites |
| Hoarfrost Petal | Cold | tundra, glaciers, alpine forests |
| Iceshard Bark | Cold | tundra, glaciers, alpine forests |
| Infernal Bulb | Infernal | cursed wastes, infernal sites |
| Ironvine | Earth | caves, cliffs, stony slopes |
| Magnetroot | Earth | caves, cliffs, stony slopes |
| Mindspike Petal | Eldritch | warped forests, planar rifts |
| Mirrorbulb | Water | rivers, lakes, wetlands |
| Moonkelp | Water | rivers, lakes, wetlands |
| Needlethorn | Poison | toxic wetlands, fungal forests |
| Oculithorn | Eldritch | warped forests, planar rifts |
| Phantom Thorn | Psychic | dream-haunted groves, mind-touched places |
| Pitchresin | Infernal | cursed wastes, infernal sites |
| Rimevine | Cold | tundra, glaciers, alpine forests |
| Rotbark | Necrotic | graveyards, blighted ground |
| Rotleaf | Poison | toxic wetlands, fungal forests |
| Rotspores | Necrotic | graveyards, blighted ground |
| Scorchvine | Fire | volcanic fissures, ash fields |
}}

{{footnote AMPERSAND'S APOTHECARIA | RARITY AND HABITAT INDEX}}
{{pageNumber,auto}}

\page {ap43,idxpage}
{{idx
## Rare — discovery target 60 (67 plants) (continued)

| Plant | Affinity | Typical habitat |
|---|---|---|
| Shellfern | Water | rivers, lakes, wetlands |
| Skitterleaf | Eldritch | warped forests, planar rifts |
| Skywhorl Petal | Air | high mountains, wind-swept peaks |
| Spellroot | Arcane | ley lines, magical ruins |
| Sporeveil | Poison | toxic wetlands, fungal forests |
| Stonecap Fungus | Earth | caves, cliffs, stony slopes |
| Stormbark | Air | high mountains, wind-swept peaks |
| Thoughtbloom | Psychic | dream-haunted groves, mind-touched places |
| Thoughtseed | Eldritch | warped forests, planar rifts |
| Tremblestem | Air | high mountains, wind-swept peaks |
| Vilevine | Poison | toxic wetlands, fungal forests |
| Volcanthistle | Fire | volcanic fissures, ash fields |
| Voltrag Root | Lightning | storm-struck highlands |
| Wailpod | Infernal | cursed wastes, infernal sites |
| Wanevine | Necrotic | graveyards, blighted ground |
| Weepblossom | Poison | toxic wetlands, fungal forests |
| Whimspores | Eldritch | warped forests, planar rifts |
| Winterthorn | Cold | tundra, glaciers, alpine forests |
| Witchberries | Poison | toxic wetlands, fungal forests |
| Witherstem | Necrotic | graveyards, blighted ground |
}}

\column

{{idx
## Ultra Rare — discovery target 75 (21 plants)

| Plant | Affinity | Typical habitat |
|---|---|---|
| Coralbark | Water | rivers, lakes, wetlands |
| Cryosap | Cold | tundra, glaciers, alpine forests |
| Dewseed | Water | rivers, lakes, wetlands |
| Echopetal | Psychic | dream-haunted groves, mind-touched places |
| Fracturepod | Eldritch | warped forests, planar rifts |
| Glyphpod | Arcane | ley lines, magical ruins |
| Hellbulb | Fire | volcanic fissures, ash fields |
| Manaberry | Arcane | ley lines, magical ruins |
| Pebblethorn | Earth | caves, cliffs, stony slopes |
| Seethe Resin | Eldritch | warped forests, planar rifts |
| Shockpetal | Lightning | storm-struck highlands |
| Slipresin | Eldritch | warped forests, planar rifts |
| Soulberry | Psychic | dream-haunted groves, mind-touched places |
| Soulbulb | Necrotic | graveyards, blighted ground |
| Stormbulb | Lightning | storm-struck highlands |
| Toxsap | Poison | toxic wetlands, fungal forests |
| Umbral Bloom | Eldritch | warped forests, planar rifts |
| Venom Bulb | Poison | toxic wetlands, fungal forests |
| Visionsap | Psychic | dream-haunted groves, mind-touched places |
| Warpvine | Eldritch | warped forests, planar rifts |
| Wizbloom | Arcane | ley lines, magical ruins |
}}

{{idx
## Legendary — discovery target 90 (5 plants)

| Plant | Affinity | Typical habitat |
|---|---|---|
| Codex Seed | Arcane | ley lines, magical ruins |
| Echo Spores | Arcane | ley lines, magical ruins |
| Lucid Bulb | Psychic | dream-haunted groves, mind-touched places |
| Lunapetal | Radiant | sunlit meadows, sacred sites |
| Soulseed | Infernal | cursed wastes, infernal sites |
}}

{{wide,gm
##### Conditions Glossary
Standard conditions (blinded, charmed, frightened, poisoned, restrained, stunned and so on) follow the game's normal rules. These shorter terms mean:

- **Dazed:** can't take reactions until the end of its next turn.
- **Dazzled:** disadvantage on Wisdom (Perception) checks that rely on sight, for the stated time.
- **Slowed:** speed halved for the stated time, or until the end of its next turn.
- **Sickened:** disadvantage on attack rolls for the stated time.
- **Bleed:** takes the listed damage at the start of each of its turns until it regains any hit points or a creature uses an action to pass a DC 10 Wisdom (Medicine) check on it.
- **Sunblind:** disadvantage on attack rolls and on Wisdom (Perception) checks that rely on sight, for 1 minute.
- **Drowsy:** disadvantage on Wisdom (Perception) checks and initiative rolls for 1 hour.
- **Calmed:** can't take reactions for the stated time.
- **Berserk:** on its next turn, must use its action to attack the nearest creature.
- **Confused:** at the start of each of its turns, roll a d4: 1, it moves in a random direction; 2, it does nothing; 3, it attacks the nearest creature; 4, it acts normally.
- **Minor curse:** disadvantage on one kind of ability check (GM's choice) until it finishes a long rest or the curse is removed by magic.
}}

{{footnote AMPERSAND'S APOTHECARIA | RARITY AND HABITAT INDEX}}
{{pageNumber,auto}}

\page {ap44}
![](https://raw.githubusercontent.com/Omegaoliverid/Ampersand-s-Apothecary/52ab9f0ae9aedf06de291046c81bc2611d183a48/apo-15.jpg){position:absolute,top:0px,left:0px,width:100%,height:100%,object-fit:cover}

\page
{{wide,chapterhead
##### REFERENCE · II
# Merchants, Availability and Price Guide

Shopping should support stories, not replace travel. These prices describe **one handful** of plant material, not the price of a finished enchanted item. Suggested 5x merchant markup is a convenience, not a universal economy rule.
}}

| Rarity | Shop buys | Shop sells |
|---|---:|---:|
| Common | 2 cp | 1 sp |
| Uncommon | 2 sp | 1 gp |
| Rare | 2 gp | 10 gp |
| Ultra Rare | 10 gp | 50 gp |
| Legendary | 100 gp | 500 gp |

### Optional d100 Shop Availability

Roll once for the chance that a plausible shop carries **at least one handful**, only if the GM wants a random market. Location, specialist contacts and the story take priority. The GM decides actual stock quantities. As a guide, a binder costs the same as one handful of a plant of the same rarity.

| Rarity | Village herbalist | Town shop | Magical apothecary |
|---|---:|---:|---:|
| Common | 80% | 95% | 100% |
| Uncommon | 25% | 60% | 90% |
| Rare | 2% | 20% | 55% |
| Ultra Rare | — | 5% | 20% |
| Legendary | — | — | 2% |

**Optional bargaining:** Buyer and seller (GM) each roll d20. The higher roll wins; the winner's Charisma modifier may shift the price in their favour using a denomination and magnitude appropriate to the sale. Ties leave the price unchanged. Speciality binders may cost more or be unavailable despite the underlying species' tier.

\column

{{gm
##### GM Quick Reference

- **Find:** 5d20 versus target; local +5 casual / +1 quest per specimen found, then one harvest check per specimen.
- **Harvest:** 10 + 1d10; natural 20 yields two handfuls, success one, miss by 1–9 none, miss by 10+ adverse consequence.
- **Brew:** up to 3 handfuls + 1 binder; 16/24/32h; DC 10 / +2 repeat / +5 new species; one item.
- **Harmony:** only genuinely conflicting plants, one d20 per distinct conflicting species; 1–5 lost, 6–14 harmonised, 15+ dominant. Alchemist's Supplies proficiency distribution, matching binder +/-1d4. Perfect harmony may earn advantage.
- **Outcome:** success full; miss 1–5 flawed but useful; miss 6–10 useless; miss 11+ magical mishap.
- **Delivery:** drinkable and throwable single-use; ointment 3 applications of its listed binder duration.
- **Throw:** action, 20/60 ft; missing damage by rarest plant 1d6/2d6/4d6/6d6/8d6; save DC 12/14/16; half damage on a save.
}}

{{wide,merchantArt
![](https://raw.githubusercontent.com/Omegaoliverid/Ampersand-s-Apothecary/52ab9f0ae9aedf06de291046c81bc2611d183a48/apo-shop.jpg)
}}

{{footnote AMPERSAND'S APOTHECARIA | MERCHANTS AND PRICES}}
{{pageNumber,auto}}

\page {ap45}
![](https://raw.githubusercontent.com/Omegaoliverid/Ampersand-s-Apothecary/52ab9f0ae9aedf06de291046c81bc2611d183a48/apo-18.jpg){position:absolute,top:0px,left:0px,width:100%,height:100%,object-fit:cover}

\page
{{wide,chapterhead
##### REFERENCE · III
# Appendix: Unusual Potion Outcomes
**Useless Potion d100:** harmless, whimsical, odd, occasionally unexpectedly beneficial effects; a miss by 6–10 generally ruins intended utility while offering entertaining colour.

**Magical Mishap d100:** wild, dramatic, strange, funny and occasionally hazardous immediate effects; a miss by 11+ calls for a mishap under the GM’s judgement. The GM can always choose an outcome more fitting to the plants, the setting and the players’ earlier efforts. For a failed throwable, a creature-directed result affects the creature splashed, not the thrower. Otherwise, “the drinker” means whoever drinks the potion. A mishap during brewing affects the brewer. Follow each entry’s stated trigger; an obvious change to the mixture or flask is apparent when it occurs.
}}

## Useless Potion (d100)

{{d100
| d100 | Outcome |
|:-:|:--|
| 1 | The brew tastes exactly like rainwater left in a boot. It does nothing else. |
| 2 | The drinker's voice drops an octave for 1 hour. Singing is now strongly discouraged. |
| 3 | The liquid turns clear the moment it is uncorked and smells faintly of disappointment. |
| 4 | For 10 minutes, the drinker hiccups small, harmless soap bubbles. |
| 5 | The flask hums a three-note tune whenever shaken. It never stops doing this. |
| 6 | The drinker's hair turns the colour of the main plant ingredient for 1 day. |
| 7 | All nearby candles lean politely towards the drinker for 1 hour. |
| 8 | The mixture sets into a firm jelly that wobbles reproachfully when anyone mentions brewing. |
| 9 | The drinker smells strongly of fresh bread for 8 hours. Dogs follow hopefully. |
| 10 | Tiny flowers sprout from the drinker's footprints for 1 minute, then wilt. |
| 11 | The potion is perfectly drinkable and perfectly ordinary herbal tea. |
| 12 | The drinker sneezes glitter once per minute for 10 minutes. |
| 13 | For 1 hour the drinker can only whisper; shouting comes out as a polite murmur. |
| 14 | The flask becomes pleasantly warm and stays warm forever. It makes a fine hand-warmer. |
| 15 | The drinker's shadow lags half a second behind them for 1 hour. |
| 16 | The brew turns into a fine grey sand. Ampersand insists this is "still technically a result". |
| 17 | The drinker's sweat smells of Snowmoss and leaves a faint frost on their collar for 1 hour. |
| 18 | Every coin the drinker touches in the next hour briefly turns green, then back. |
| 19 | The drinker gains a strong, temporary conviction that they have left something boiling at home. |
| 20 | The liquid separates into neat coloured layers that refuse to mix again, no matter how hard it is shaken. |
| 21 | For 1 minute, the drinker's footsteps squeak like a damp mouse. |
}}

\column

{{d100
| d100 | Outcome |
|:-:|:--|
| 22 | The drinker can taste colours for 10 minutes. Red tastes of copper; blue of cold stone. |
| 23 | The potion smells wonderful and tastes of nothing whatsoever. |
| 24 | The cork shoots out with a loud pop and is never found again. The potion is otherwise water. |
| 25 | The drinker's fingernails glow softly in the dark for one night. Useful for reading, briefly. |
| 26 | Small birds find the drinker fascinating for 1 hour and follow at a respectful distance. |
| 27 | The drinker's ears turn pointed for 1 hour, or round if they were already pointed. |
| 28 | The brew foams up over the rim, leaving a sticky ring on whatever it stands on. |
| 29 | The drinker forgets the name of one ordinary vegetable for 1 day. |
| 30 | For 10 minutes, everything the drinker says rhymes, whether they intend it to or not. |
| 31 | The flask grows a fine layer of moss overnight. The potion inside is now mostly moss. |
| 32 | The drinker becomes convinced their left boot is slightly heavier than their right. It is not. |
| 33 | A faint, pleasant wind chime sound follows the drinker for 1 hour. |
| 34 | The brew is so bitter that the drinker's eyes water for 1 minute. It has no other effect. |
| 35 | The drinker's reflection winks at them once. Nothing else happens. Probably. |
| 36 | Any milk within 10 feet of the drinker curdles over the next hour. |
| 37 | The liquid crystallises into a pretty, worthless sugar-glass bead. |
| 38 | The drinker gains the ability to identify any cheese by smell for 1 day. |
| 39 | The potion bubbles cheerfully but goes flat within a minute, like stale ale. |
| 40 | For 1 hour the drinker's breath is visible, even in warm rooms. |
| 41 | The drinker's eyebrows grow 1 inch longer over the course of the evening. |
| 42 | The flask label (if any) rewrites itself to read "Try Again". |
}}

{{footnote AMPERSAND'S APOTHECARIA | APPENDIX}}
{{pageNumber,auto}}

\page {ap46}
## Useless Potion (d100), continued

{{d100
| d100 | Outcome |
|:-:|:--|
| 43 | Small sparks crackle harmlessly from the drinker's hair when brushed for 1 day. |
| 44 | The drinker feels intensely, briefly nostalgic for a place they have never been. |
| 45 | The brew tastes of Emberberry but provides only a mild, pleasant warmth in the stomach. |
| 46 | Every door the drinker opens in the next hour creaks dramatically. |
| 47 | The drinker's cheeks flush bright pink for 10 minutes, as if caught telling a lie. |
| 48 | The potion turns solid in the flask. Shaking it produces a satisfying rattle. |
| 49 | For 1 hour, the drinker always knows which way is north, and it is rarely helpful. |
| 50 | A single petal grows behind the drinker's ear and stays until plucked. |
| 51 | The drinker's sneezes smell of cinnamon for 1 day. |
| 52 | The potion makes the drinker extremely confident about one bad idea. The GM chooses which. |
| 53 | The drinker's handwriting becomes elegant calligraphy for 1 hour, then reverts mid-word. |
| 54 | The flask cools to freezing and frosts over, but the liquid is merely cold water. |
| 55 | Insects politely avoid the drinker for 1 hour, then return with renewed interest. |
| 56 | The drinker hears faint applause whenever they finish a sentence for 10 minutes. |
| 57 | The brew is a startlingly good dye. Fingers, lips and teeth turn purple for 1 day. |
| 58 | The drinker's pockets fill with dry leaves at dawn the next morning. |
| 59 | The potion tastes of whatever the drinker least wanted it to taste of. |
| 60 | For 1 minute, the drinker floats one inch above the ground and cannot control it at all. |
| 61 | A small rain cloud forms over the flask, rains once on the brewer, and dissolves. |
| 62 | The drinker feels rested, as if they had a short nap. Nothing mechanical; just pleasant. |
| 63 | The drinker's laugh becomes a goose-like honk for 1 hour. |
| 64 | The liquid spells the brewer's name in bubbles before going still and inert. |
| 65 | The drinker attracts a single persistent moth for the rest of the day. |
| 66 | For 10 minutes, the drinker can only walk backwards comfortably. |
| 67 | The brew coats the drinker's tongue in a sparkly film. It washes off with a mouthful of Spring Water. |
| 68 | The drinker's shoes become slightly too large for 1 hour. |
| 69 | The mixture smells so strongly of herbs that rations within 5 feet taste of thyme for a week. |
| 70 | The drinker is followed for 1 hour by the faint scent of the plant they most recently harvested. |
| 71 | The flask becomes extremely slippery and is dropped at the least convenient moment today. |
}}

\column

{{d100
| d100 | Outcome |
|:-:|:--|
| 72 | The drinker knows the exact number of hairs on their own head for 1 minute, then forgets. |
| 73 | The brew glows faintly for 1 hour, making a modest candle-substitute, then dims to mud. |
| 74 | The drinker's freckles rearrange into a little constellation, returning to normal at dusk. |
| 75 | For 1 hour, the drinker's yawns are contagious to everyone within 30 feet. |
| 76 | The potion produces a beautiful smoke ring when uncorked. That is the whole effect. |
| 77 | The drinker feels an overwhelming urge to tidy something. Resisting is entirely possible. |
| 78 | The liquid is now salty seawater. A tiny shell rattles at the bottom. |
| 79 | The drinker's hands smell of the binder used, and soap does not help for 1 day. |
| 80 | For 1 hour, any music the drinker hears seems slightly out of tune to them alone. |
| 81 | The brew causes the drinker's hat (or hair) to stand straight up for 10 minutes. |
| 82 | The drinker briefly remembers a dream from three years ago in vivid, pointless detail. |
| 83 | Small leaves sprout from the cork and must be trimmed weekly. The potion is inert. |
| 84 | The drinker speaks with the accent of the last person they spoke to for 1 hour. |
| 85 | The potion is fizzy and refreshing. Several days of thirst are no closer to being quenched. |
| 86 | For 10 minutes, the drinker's eyes change colour every time they blink. |
| 87 | A faint outline of the intended effect shimmers around the drinker for a moment, then fades. |
| 88 | The drinker's bootlaces tie themselves together once, at a harmless moment. |
| 89 | The liquid is warm, sweet and smells of honey. It is otherwise useless but popular at parties. |
| 90 | For 1 hour, the drinker's footsteps leave faintly glowing prints that fade after a minute. |
| 91 | The drinker becomes unusually good at whistling for 1 day, and unusually keen to show it. |
| 92 | The brew solidifies into a rubbery ball that bounces surprisingly high. |
| 93 | The drinker's coins all land on the same face for 1 hour. This proves nothing useful. |
| 94 | A tiny, harmless spark of lightning jumps between the drinker's fingers when they snap them for 1 hour. |
| 95 | The drinker can understand the cooing of pigeons for 10 minutes. Pigeons say very little. |
| 96 | The flask's glass turns smoky and opaque. The potion inside is now dusty water. |
| 97 | The drinker's skin takes on a faint shimmer that is only visible in moonlight, for one night. |
| 98 | For 1 hour the drinker cannot stop humming the last tune they heard. |
| 99 | The potion tastes faintly of victory but does absolutely nothing. |
| 100 | Roll twice and combine both results. The GM may decide one cancels the other into tea. |
}}

{{footnote AMPERSAND'S APOTHECARIA | APPENDIX}}
{{pageNumber,auto}}

\page {ap47}
## Magical Mishap (d100)

{{d100
| d100 | Outcome |
|:-:|:--|
| 1 | The flask explodes in a burst of coloured smoke. Everyone within 10 feet is lightly obscured for 1 minute. |
| 2 | The brewer is splashed: DC 13 Constitution save or take 2d6 damage of the main plant's affinity type. |
| 3 | A thunderous bang deafens everyone within 15 feet for 1 minute (DC 12 Constitution save negates). |
| 4 | The brew boils over and sets the brewing equipment alight. Extinguishing it takes an action. |
| 5 | The drinker's skin turns to rough bark for 1 hour: −10 feet speed, but +1 AC. |
| 6 | The mixture releases a choking cloud in a 10-foot radius. DC 13 Constitution save or poisoned for 1 minute. |
| 7 | Vines burst from the flask and restrain the holder (escape DC 13) for 1 minute. |
| 8 | The drinker floats uncontrollably upward 20 feet over 1 round, then drifts down gently after 1 minute. |
| 9 | Every metal object within 10 feet becomes magnetised to the drinker for 1 minute. |
| 10 | The brew screams. Creatures within 30 feet who can hear it must succeed on a DC 12 Wisdom save or be frightened until the end of their next turn. |
| 11 | The drinker grows a second shadow that acts independently and mischievously for 1 hour. |
| 12 | Frost erupts from the flask. Ground in a 10-foot radius becomes difficult terrain for 10 minutes. |
| 13 | The drinker swaps voices with the nearest creature for 1 hour. |
| 14 | A burst of blinding light: creatures within 10 feet make a DC 13 Constitution save or are blinded until the end of their next turn. |
| 15 | The potion animates into a small, angry ooze (use rat statistics) and flees with 1 handful of unused ingredients. |
| 16 | The drinker shrinks to Small size (or Tiny if already Small) for 10 minutes. Equipment does not shrink. |
| 17 | The drinker grows to one size larger for 1 minute and cannot fit comfortably through ordinary doors. |
| 18 | Every empty flask and bottle within 10 feet shatters with a musical crash. Sealed potions survive. |
| 19 | Static builds on the drinker: the next creature they touch within 1 minute takes 1d8 lightning damage, as does the drinker. |
| 20 | The brew teleports the drinker 30 feet in a random direction to an unoccupied space. |
}}

\column

{{d100
| d100 | Outcome |
|:-:|:--|
| 21 | The drinker becomes invisible for 1 minute, but so do all their clothes and none of their equipment. |
| 22 | The drinker's hair catches harmless green fire for 1 minute, shedding bright light in a 10-foot radius. |
| 23 | Spores burst outward. Creatures within 10 feet are sneezing helplessly: disadvantage on attack rolls for 1 round. |
| 24 | The drinker's limbs become rubbery for 10 minutes: advantage on escaping grapples, disadvantage on Strength checks. |
| 25 | A rift of whispering darkness opens for 1 round. DC 13 Wisdom save or 1d6 psychic damage to all within 10 feet. |
| 26 | The drinker speaks only in Infernal for 1 hour, whether they know the language or not. |
| 27 | Gravity reverses on the drinker for 1 round. They fall to the ceiling, then back to the floor at the start of their next turn. |
| 28 | The drinker gains vulnerability to the main plant's damage type for 1 hour. |
| 29 | The brew becomes sentient for a few seconds, insults the brewer's technique, and evaporates. |
| 30 | A gust of wind blasts out from the flask. Creatures within 10 feet make a DC 13 Strength save or are pushed 10 feet. |
| 31 | The drinker sweats sticky resin for 10 minutes. Anything they put down sticks; anything they pick up is hard to release. |
| 32 | The drinker's eyes glow brightly for 1 hour, making stealth checks in darkness impossible. |
| 33 | The potion detonates in a small fireball: 2d6 fire damage to creatures within 5 feet (DC 13 Dexterity save for half). |
| 34 | The brewer's tools fuse together into a single beautiful, useless sculpture. |
| 35 | The drinker becomes magically convinced they are a plant for 10 minutes and tries to stand in sunlight. |
| 36 | The drinker ages one year in appearance overnight. This fades over the next month. |
| 37 | Roots erupt from the floor in a 15-foot radius. The area becomes difficult terrain until cleared. |
| 38 | The drinker's weight halves for 1 hour. Strong winds become a genuine concern. |
| 39 | A cold mist chills everyone within 10 feet: DC 12 Constitution save or 1d6 cold damage and speed halved until the end of their next turn. |
| 40 | The drinker hears every thought within 10 feet for 1 minute, all at once. DC 13 Wisdom save or stunned for 1 round. |
}}

{{footnote AMPERSAND'S APOTHECARIA | APPENDIX}}
{{pageNumber,auto}}

\page {ap48}
## Magical Mishap (d100), continued

{{d100
| d100 | Outcome |
|:-:|:--|
| 41 | The flask grows legs and runs away. It can be recaptured with a DC 13 Dexterity check. |
| 42 | The drinker's hands glow and cannot hold anything for 1 minute; objects slide out of their grip. |
| 43 | The drinker is charmed by the first creature they see for 1 minute (DC 13 Wisdom save negates). |
| 44 | The mixture eats through its container and the table beneath. Repairs may be required. |
| 45 | A surge of necrotic chill: the drinker's hit point maximum is reduced by 1d6 until their next long rest. |
| 46 | The drinker becomes buoyant and cannot sink in water for 1 day, nor easily dive. |
| 47 | Butterflies burst from the flask in a dazzling cloud that lightly obscures a 15-foot radius for 1 minute. |
| 48 | The drinker sees everything upside down for 10 minutes: disadvantage on ranged attack rolls. |
| 49 | Every plant within 30 feet grows a foot in a single breath, cracking pots and floorboards. |
| 50 | The drinker gains one level of exhaustion as the brew draws on their vitality. |
| 51 | The potion becomes a swarm of glowing motes that orbit the drinker for 1 hour, making them easy to spot. |
| 52 | The drinker's skin becomes translucent for 1 hour. It is unsettling but harmless. |
| 53 | A tremor shakes the area. Creatures within 15 feet make a DC 12 Dexterity save or fall prone. |
| 54 | The drinker can only move in straight lines for 1 minute and must stop to change direction. |
| 55 | The drinker is struck silent for 1 minute; spells with verbal components cannot be cast. |
| 56 | Rain falls from nowhere in a 20-foot radius for 10 minutes, extinguishing small flames. |
| 57 | The drinker's weapon or focus becomes wrapped in thorny vines. Freeing it takes an action. |
| 58 | The brew sends the drinker into a deep, peaceful sleep for 1 minute, unless they take damage. |
| 59 | Light bends strangely: the drinker appears 5 feet from where they actually are for 1 minute. |
| 60 | A flash of time slip: the drinker loses their next turn as everyone else briefly moves faster. |
}}

\column

{{d100
| d100 | Outcome |
|:-:|:--|
| 61 | Radiant sparks scorch the drinker: 1d8 radiant damage, and they shed dim light for 1 hour. |
| 62 | The drinker's footsteps boom like thunder for 1 hour. Stealth is out of the question. |
| 63 | The potion freezes the drinker's feet to the ground for 1 round (DC 13 Strength check to break free early). |
| 64 | The drinker sprouts small, useless wings that flap anxiously for 1 day. |
| 65 | A memory is lost: the drinker forgets the last 10 minutes entirely. |
| 66 | Ink-black tears stream from the drinker's eyes for 1 minute: disadvantage on Perception checks that rely on sight. |
| 67 | The drinker is surrounded by a 10-foot aura of calm. No creature inside can willingly start a fight for 1 round. |
| 68 | The flask erupts with sticky foam. Creatures within 5 feet are restrained until the end of their next turn (DC 12 Dexterity save negates). |
| 69 | The drinker's body becomes intensely magnetic to lightning: they have disadvantage on saves against lightning for 1 hour. |
| 70 | The potion hatches a tiny, very short-lived elemental of the main affinity that panics for 1 round, then fizzles out. |
| 71 | Everyone within 10 feet swaps places randomly with one another. |
| 72 | The drinker's luck curdles: the next d20 they roll within 1 hour is rolled with disadvantage. |
| 73 | A wave of nausea: the drinker is poisoned for 1 minute (DC 13 Constitution save negates). |
| 74 | The drinker becomes briefly ethereal and drops through 5 feet of floor before solidifying. |
| 75 | Glittering acid spatters the brewer: 1d6 acid damage, and one piece of non-magical equipment is pitted. |
| 76 | The drinker is followed for 1 day by a loud, invisible drumbeat matching their heartbeat. |
| 77 | Plants within 30 feet turn towards the drinker and whisper their name for 1 hour. |
| 78 | The drinker's temperature soars: they must drink twice as much water today or gain a level of exhaustion. |
| 79 | A small storm cloud forms over the drinker's head and drizzles on them for 1 hour. |
| 80 | The drinker gains the intended effect, but only for 1 round, and in the most inconvenient way possible. |
}}

{{footnote AMPERSAND'S APOTHECARIA | APPENDIX}}
{{pageNumber,auto}}

\page {ap49}
## Magical Mishap (d100), continued

{{d100
| d100 | Outcome |
|:-:|:--|
| 81 | The drinker turns a vivid shade of blue for 1 week. No mechanical effect. Considerable social effect. |
| 82 | The potion's magic leaps to the nearest hostile creature instead. The GM decides how it is affected. |
| 83 | The drinker's hands become weapons of the main affinity for 1 minute (1d4 damage) but they cannot hold anything. |
| 84 | Mirrors within 30 feet crack, and the drinker briefly sees someone else in each reflection. |
| 85 | The drinker becomes heavy as stone for 1 minute: speed 0, but they cannot be moved against their will. |
| 86 | A hungry rumble: the drinker must eat a full meal within the hour or gain one level of exhaustion. |
| 87 | Light drains from a 20-foot radius, creating magical darkness for 1 round. |
| 88 | The drinker's senses swap: they hear colours and see sounds for 1 minute (disadvantage on Perception checks). |
| 89 | The flask becomes a tiny portal for 1 round. Something small comes through. The GM decides what. |
| 90 | The drinker sheds their skin like a snake over the next hour. It is painless and deeply unpleasant. |
}}

\column

{{d100
| d100 | Outcome |
|:-:|:--|
| 91 | One unused handful in the brewer's pack is consumed by the reaction. The GM chooses which. |
| 92 | The drinker becomes the target of every insect within 100 feet for 10 minutes. |
| 93 | A harmonic chime rings out: any open, unstoppered potion within 10 feet goes flat and loses its magic. |
| 94 | The drinker briefly becomes a small plant of the main ingredient's species for 1 minute, then reverts. |
| 95 | A chain reaction: the nearest other flask also suffers a roll on this table. |
| 96 | The brew's magic sinks into the brewer's bones: they cannot benefit from potions for 1 hour. |
| 97 | The drinker's reflection steps out of the nearest mirror or puddle, copies their every move for 1 minute, then collapses into harmless glass dust. |
| 98 | A flash of all elements at once: 1d4 fire, 1d4 cold and 1d4 lightning damage to the drinker. |
| 99 | The drinker gains the intended effect at double strength and duration, then suffers one other roll on this table. |
| 100 | The GM's choice. The worst outcome should still make a good story, never a dead end. |
}}

{{wide,mishapArt
![](https://raw.githubusercontent.com/Omegaoliverid/Ampersand-s-Apothecary/52ab9f0ae9aedf06de291046c81bc2611d183a48/apo-mishap.jpg)
}}

{{footnote AMPERSAND'S APOTHECARIA | APPENDIX}}
{{pageNumber,auto}}

\page {ap50}
![](https://raw.githubusercontent.com/Omegaoliverid/Ampersand-s-Apothecary/52ab9f0ae9aedf06de291046c81bc2611d183a48/apo-21.jpg){position:absolute,top:0px,left:0px,width:100%,height:100%,object-fit:cover}

\page

{{wide,chapterhead
##### GAME MASTER · SIGNATURE PREPARATIONS
# Zoltan’s Experimental Preparations
Rules for the signature potions described in Zoltan’s journal. Share a preparation’s effects when it is discovered; the journal remains an account of his experiments.
}}

{{wide
## Slumber’s Relief

A pale-blue draught with a soft floral scent and a slight shimmer. After drinking it, the subject sleeps deeply for **four hours** and gains the benefits of **one long rest**. The sleeper cannot be woken during this sleep.

Apply the campaign’s normal long-rest recovery for hit points, spell resources, Hit Dice and exhaustion. The potion supplies one long rest’s benefits, subject to the normal limit of one qualifying long rest in 24 hours. It does not separately remove all exhaustion. The journal’s warnings about drinking in combat or while standing remain apt.

## Potion of Ghost Poos

The potion produces a **very messy deposit**. The drinker’s senses leave their body and hover just above the **largest surviving piece of that deposit**, wherever it is moved. The projection can **see and hear**, but cannot touch, attack, cast or interact with anything. It cannot serve as a casting origin or provide sight for spell targeting. As an **action**, the drinker may focus sight and hearing on either their body or the deposit; only one viewpoint functions at a time. The body remains awake and under their control, but while projecting they cannot see or hear its surroundings. Other senses remain available; apply the normal consequences of missing perception, not paralysis or unconsciousness.

The projection lasts **seven days or until the drinker next drinks a Potion of Ghost Poos**, whichever occurs first. A moved sample carries the viewpoint with it; the privy is not the anchor. Switching focus does not reset the duration. If no part of the deposit survives, the projected viewpoint ends and the senses return to the body.

A little movement is possible. Moving farther creates an increasing pulling sensation, and continued attempts can cause the embarrassing accident described in the journal. The GM judges permissible movement and the escalating pull in context. The effect does not grant a clean-deposit or permanent cleaning benefit.

## Recipe and provenance

These are signature experimental preparations, not automatic outcomes of the ordinary worked recipes. The GM controls their recipes, crafting rarity and sale prices; a matching theme alone does not make them an ordinary catalogue recipe.

The journal also mentions healing and clarity preparations without complete agreed game entries. Those references remain narrative discoveries unless the GM gives them a complete game entry.
}}

{{footnote AMPERSAND'S APOTHECARIA | GM SIGNATURE PREPARATIONS}}
{{pageNumber,auto}}


\page {zjournal,zstage1,ztitle}
![](https://raw.githubusercontent.com/Omegaoliverid/Ampersand-s-Apothecary/52ab9f0ae9aedf06de291046c81bc2611d183a48/apo-24.jpg){position:absolute,top:0px,left:0px,width:100%,height:100%,object-fit:cover}

\page

{{zbody
# The Field Journal of Zoltan Ambersand

<div class="zsignatures" aria-label="Ampersand signature experiments"><span>Z. &amp;</span><span>Zoltan &amp;</span><span>&amp; &amp; &amp;!</span></div>

*Alchemist, Inventor, Distinguished Researcher and Occasional Victim of His Own Brilliance.*

{{zeditor
*The journal is bound in dark green leather, stained with substances of several colours. Its brass clasp has been replaced twice. The pages smell faintly of lavender, sulphur and something considerably less pleasant. The handwriting begins in neat columns with immaculate measurements. It does not stay that way.*
}}

## Inside the Front Cover

{{zbookplate
<span class="zcaps">PROPERTY OF ZOLTAN AMBERSAND</span>. Master Alchemist. Inventor of Several Things Not Yet Properly Appreciated.
}}

<span class="zcaps">DO NOT TOUCH</span>. Unless you are an alchemist. Or an adventurer. Or have something interesting. *Especially* something interesting.

<span class="zcaps">IMPORTANT</span>: If any page begins to smoke, close the book.

No no. Not that page. The <span class="zcaps">OTHER</span> page.
}}

{{footnote AMPERSAND'S APOTHECARIA | THE FIELD JOURNAL}}
{{pageNumber,auto}}

\page {zjournal,zstage1}

{{zbody
## A Most Fortunate Beginning

Ambersand has been given a laboratory! A proper one. Benches, burners, distillation coils and a very fine cabinet for dangerous ingredients. The family has been most generous.

The Ambersand name is known throughout the city. Our apothecary has supplied the finest households for generations: respectable remedies, reliable tinctures, medicines that do precisely what the label says.

How terribly *predictable*.

Why should a potion do only <span class="zcaps">ONE</span> thing? A healing draught is excellent for wounds, yes yes. But what if it also restored the colour to one's hair? Or let one breathe underwater? Or made one irresistible to butterflies?

Not all at once, naturally.

Although…

*Note: try all at once.*

*Second note: do not tell Father.*

## On the Proper Study of Ingredients

Reading about an ingredient is <span class="zcaps">NOT</span> the same as knowing it. A book may say a root makes you tingle. But <span class="zcaps">WHERE?</span> The tongue? The toes? Behind the ears? When heated? When combined with this? Or that?

This and that! Yes yes! Or perhaps that and this. The order is important. *Very* important.

This morning's trials:

- **Silvercap fungus.** First taste: cooling. Second taste: left ear turned blue. Third taste: ear returned to normal. Excellent! Reversible!
- **Whisperleaf.** Distant sounds grow clearer. Spent twenty minutes listening to the gardener discuss turnips. Very informative.
- **Unidentified purple berry.** Delicious. Fingernails glowed for two hours. Must identify berry. Must obtain more. Must remember where I found it…

<span class="zcaps">NOTE TO SELF</span>: <span class="zcaps">THIS IS WHY WE KEEP JOURNALS</span>.
}}

{{footnote AMPERSAND'S APOTHECARIA | THE FIELD JOURNAL}}
{{pageNumber,auto}}

\page {zjournal,zstage2,zdense}

{{zbody
## Adventurers Make Excellent Research Partners

Adventurers came to the apothecary today. Wonderful people! Scratched, bruised, curious, and willing to drink almost anything for a small discount. They are walking laboratories!

One brought a pouch of pale dust from an ancient crypt. We mixed a little with spring water. Green, then yellow, then clear. When he drank it, his shadow stayed standing while he walked away.

For six seconds. <span class="zcaps">SIX SECONDS!</span> Could a shadow carry things? Could it do the household chores?

The gentleman was less enthusiastic. He insisted his shadow tried to strangle him. Ambersand saw no such thing.

Although he was facing the other way at the time.

*Research note: never promise an adventurer a potion is completely harmless. Say* reasonably *harmless. Much more accurate.*

## The Potion of Ghost Poos

Overheard two adventurers at the counter this morning. One boasted he had done a "ghost poo" before breakfast. The other was most impressed.

A ghost poo, it seems, is one so clean that it needs no wiping at all.

Extraordinary!

Everyone does it. Every single day. And nobody has ever thought to improve it with a <span class="zcaps">POTION?</span>

Yes yes. Ambersand shall make it happen on purpose.

**Trial one.** Drank the draught. Waited. Performed the experiment.

It was not a ghost poo.

It was the opposite of a ghost poo. A most *messy* affair. Wiping was required. A great deal of wiping.

Failure. Disappointing.

And then, while sitting quietly and reflecting on my failure, my senses floated clean out of my body.

I was hovering above the privy! Above my own… result. Could see. Could hear the birds. Could not touch a thing.

Naturally, I tried to move. A little movement was fine. More produced a pulling sensation. Not in the head. Not in the stomach.

Somewhat lower.

Tried again. Stronger tug.

Tried once more, for science.

…

<span class="zcaps">RESEARCH INTERRUPTED</span>. Change of trousers required.

**Later.** The connection follows the *deposit*, not the privy. An assistant moved a sample (he was paid extra) and my senses went with it, floating just above the largest piece. It lasts about a week, or until the next dose.

Think of it! A spy in an enemy fortress. Beneath a meeting table. Inside a locked vault!

No no. One would need to get into the vault first.

Unless…

*Must consider delivery methods.*

*<span class="zcaps">IMPORTANT</span>: do not explain this to customers while they are eating.*

## Slumber's Relief

Pale blue. Soft floral smell. A little shimmer in the light. Why sleep eight hours when a potion can do it in four?

Trial one: slept eleven minutes. Trial two: dreamed of a very large cabbage. Trial three: <span class="zcaps">SUCCESS!</span> Four hours of deep sleep, and a whole long rest's worth of recovery!

One small difficulty. The sleeper cannot be woken. Not by shouting. Not by shaking. Not, my assistant reports, by a bucket of cold water.

*Warning: do not drink in combat. Do not drink while standing. Stop testing it on the good carpet. Mother has complained. Again.*
}}

{{footnote AMPERSAND'S APOTHECARIA | THE FIELD JOURNAL}}
{{pageNumber,auto}}

\page {zjournal,zstage2,zchemical}

{{zbody
## Words and Potions

Some potions work better when the drinker *declares* it. Does the magic listen? Or is a potion simply more effective when shouted at?

"<span class="zcaps">REPEAT AFTER ME!</span> I <span class="zcaps">AM HEALED</span>, I <span class="zcaps">AM WHOLE</span>, I <span class="zcaps">AM RENEWED!</span>"

A customer asked if the shouting was necessary. Ambersand explained that proper experiments need consistency. The customer said the shouting was embarrassing.

Embarrassing? Would the great wizards of old have discovered magic if they were embarrassed by their own voices?

<span class="zcaps">NO NO!</span>

Well. Probably not.

*Note: do not let Father hear me shouting at the patients again.*

## A Most Unreasonable Complaint

Father visited the laboratory today. He says the family apothecary is a place of healing, not a testing ground for nonsense.

He pointed at the green stain on the ceiling. A perfectly ordinary by-product.

He pointed at the small hole in the wall. Energetic crystallisation.

He pointed at the door. A customer had left yesterday with feathers growing from his elbows. Only temporarily! And he was delighted, waving his arms and laughing all the way down the street.

Father says he was screaming.

A matter of interpretation.

What is a ruined carpet compared to a new understanding of the world? Father did not answer. He merely looked at the carpet.

## This and That, or That and This

Most alchemists consider only <span class="zcaps">WHAT</span> is combined. But perhaps the secret is <span class="zcaps">WHEN</span>.

A into B: pale yellow. B into A: violet. Same quantities, same heat, same glass. Different results! Seven trials. Seven times the same.

<span class="zcaps">YES YES!</span>

Tomorrow, a third ingredient. Then a fourth. And heat. A little heat. Not too much.

*Important: the third ingredient must be added <span class="zcaps">AFTER</span> the violet has settled, or the mixture becomes unstable. <span class="zdouble">Possibly* dangerously *unstable.</span>*

…

Why is that sentence underlined?

Ah well. Tomorrow!
}}

{{footnote AMPERSAND'S APOTHECARIA | THE FIELD JOURNAL}}
{{pageNumber,auto}}

\page {zjournal,zstage3,zburnt}

{{zbody
## The Most Extraordinary Discovery

I <span class="zcaps">HAVE FOUND IT!</span>

Three ingredients. A precise order. A moment of heat. And then: *light*. Light that moves against its own source. Tiny glowing shapes hanging in the liquid. The whole flask trembling without touching the glass.

This is no potion. This is a <span class="zcaps">NEW PRINCIPLE</span>.

The first flask cracked. The second melted its stand. The third held for eleven seconds.

<span class="zcaps">ELEVEN SECONDS!</span>

The Guild will be astonished. The whole city will speak of Zoltan Ambersand!

Tomorrow: a larger vessel. Greater quantities. More heat?

No no, not more heat. A stronger binder. Or *two* binders.

Yes yes! This and that! And that and this!

Tomorrow shall be <span class="zcaps">MAGNIFICENT!</span>

{{zeditor
*The bottom of the page is scorched. The next three pages are missing.*
}}
}}

{{footnote AMPERSAND'S APOTHECARIA | THE FIELD JOURNAL}}
{{pageNumber,auto}}

\page {zjournal,zafter}

{{zbody
## After

{{zeditor
*The handwriting resumes on cheaper paper. The ink is faint.*
}}

The apothecary is gone.

Not damaged. Not in need of repair. Gone. The laboratory, the cabinets, the family sign. There is a hole where the workshop stood.

Quite a large hole.

The family says I was warned. Correct. They say I should have listened. Also correct. They say intelligence without caution is a danger to everyone near it.

I do not care for that. But I cannot entirely dispute it.

The measurements were right. The timing was right. It should have held. I still do not understand what went wrong, and that troubles me more than anything.

Not knowing.

## A Change of Circumstances

The family has decided. I am to leave the city. They have disowned me, and Father has forbidden me the family name.

Ambersand. Generations of respectable apothecaries. A name I was meant to bring honour to.

Father asked whether I understood what I had destroyed. I said yes. He asked whether I would ever try the experiment again.

…

I should have said no. It was the sensible answer. The answer he wanted.

But I still believe it could work. With different quantities. With more care. Much more care. I cannot promise never to try.

So I am sent to a place called Silverwood. Small. Quiet. Far away. It is thought such a place will cure me of ambitious experiments.

An interesting theory.

I suspect it is incorrect.
}}

{{footnote AMPERSAND'S APOTHECARIA | THE FIELD JOURNAL}}
{{pageNumber,auto}}

\page {zjournal,zstage4,ztravel,ztwocol}

{{zbody
## On the Road to Silverwood

Travel is dreadful. No laboratory. No shelving. No calibrated anything. How is an alchemist supposed to <span class="zcaps">WORK?</span>

Tried a cooking pot. Unacceptable. Tried a waterskin. Worse. Tried hanging a flask over the campfire on a wire. Promising! Flask broke.

Found a root by the road. Tasted it. Warm tongue, then an overwhelming craving for pickled onions. Tasted more to confirm. Craving considerably stronger.

Bought three jars of pickled onions. Very expensive. Research requires sacrifice.

## A Curious Difficulty with My Name

The adventurers sharing the road are very friendly. Very <span class="zcaps">LOUD</span>. One asked my name while I was measuring powder into a flask.

"Zoltan Ambersand!"

"Ampersand?"

"No no! Amber—"

But the liquid had just turned <span class="zcaps">PURPLE</span>. It was supposed to be <span class="zcaps">GREEN!</span> Naturally, I had more important matters to attend to.

The next morning: "Master Ampersand! Is this mushroom poisonous?"

"Did you eat it?"

"No."

"<span class="zcaps">MARVELLOUS!</span> Then we have time to find out!"

At the next village, a merchant called me Master Ampersand. At the next camp, I was introduced as Zoltan Ampersand, expert in all things bubbling. I tried to correct him, but someone had found a fungus that smelled of cinnamon.

The name could wait. The fungus could not.

Somewhere along the road, I stopped correcting them.

Father has forbidden the old name. But a *new* name?

Hmm. Must investigate.

Later. The cinnamon fungus is doing something peculiar.

## A Laboratory That Travels

A <span class="zcaps">MOST EXCELLENT THOUGHT</span>.

Why must a laboratory stay in one place? A laboratory is not a building. It is the equipment, the ingredients and the mind of the alchemist. All of those can be made portable.

The mind is already portable. Usually.

A workshop that unfolds from a bag! Burners, glassware, storage, somewhere safe for the volatile ingredients. It must protect everything on the road and fold away again.

An extraordinarily difficult proposition.

<span class="zcaps">AMBERSAND LOVES DIFFICULT PROPOSITIONS</span>.

{{zeditor
*Several pages of hinges, nested drawers and increasingly improbable folding diagrams follow.*
}}

- **Prototype one.** The table unfolded. The shelving did not. A small fire followed. Progress!
- **Prototype two.** Unfolded beautifully. Refused to fold up again. Spent two hours arguing with the lock. It won.
- **Prototype three.** <span class="zcaps">IT FOLDS AWAY!</span> Usually. The left shelf sticks, one drawer opens upside down, and when folded it hums alarmingly. Possibly harmless. But I brewed a real potion inside it, by the side of a muddy road!

A passing adventurer shouted, "Well done, Ampersand!"

Ambersand was too busy dancing to correct him.
}}

{{footnote AMPERSAND'S APOTHECARIA | THE FIELD JOURNAL}}
{{pageNumber,auto}}

\page {zjournal,zstage4,zsignpage,ztwocol}

{{zbody
## Silverwood

I have arrived. Quiet streets, green woods, little shops, and all around them forests, streams and ruins full of plants that are in none of my books.

One smells of honey when crushed. One changes colour in moonlight. One made my nose go numb for eleven minutes.

Must collect more.

The people ask a great many questions. "Where are you from?" "What happened to your old shop?" "Is that smoke supposed to be coming out of your bag?"

Questions, questions! An alchemist has work to do!

I have found a small shop. A counter, a few shelves. Nothing like the family establishment. It will do.

No no. It will be <span class="zcaps">MARVELLOUS</span>.

## The Matter of the Sign

A sign painter came today and asked what name should go above the door.

"Zoltan Ambersand, Alchemist," I told him, while studying the underside of a most unusual leaf.

One of the adventurers from the road was passing and kindly offered to help with the spelling.

The sign arrived this afternoon. Beautiful lettering. It reads:

{{zsign
**<span class="zcaps">AMPERSAND</span>’S <span class="zcaps">APOTHECARIA</span>**
}}

Again!

I was about to complain when I saw the little golden squiggle painted beneath the name. <span class="zamp-inline">&amp;</span>

Clerks use it between words. It means <span class="zcaps">AND</span>. This *and* that. Two things brought together.

Why, that is the very heart of alchemy!

And then I remembered Father's words. The family name is no longer mine.

But this one? This *Ampersand*? It belongs to no one but me.

Well. Me and the sign painter. And the adventurers who invented it by accident.

Nevertheless! <span class="zcaps">ZOLTAN AMPERSAND!</span> Alchemist! Inventor! Master of This <span class="zcaps">AND</span> That!

I shall keep it.

No no. I <span class="zcaps">KNOW</span> I shall keep it.

And the sign is already paid for.

## The Final Adjustment

A level floor and a proper bench at last! The travelling laboratory has had its final improvements. The shelf unfolds. The burners light first time. The drawers stay upright. The humming has stopped.

Mostly.

It needs a name. Something grand. Something memorable.

{{zproducer
**<span class="zcaps">AMPERSAND</span>’S <span class="zcaps">PERFECTLY PORTABLE POP-UP POTION PRODUCER!</span>**
}}

Too many words? No no. Not enough!

A brass plate on the clasp, with the name engraved, and beneath it the little squiggle. <span class="zamp">&amp;</span> A perfect symbol for joining things that perhaps ought not to be joined.

And occasionally become something <span class="zcaps">WONDERFUL</span>.

## The Honesty Box

The people of Silverwood enjoy talking. Very friendly. Very time-consuming. So: a sign with prices, potions on the shelves, a small box by the door. Customers take what they need and leave the coin.

No fuss. No knocking while I am concentrating.

Naturally, I shall still speak to anyone carrying an interesting ingredient. Or showing an unusual symptom.

Or willing to test a new preparation.
}}

{{footnote AMPERSAND'S APOTHECARIA | THE FIELD JOURNAL}}
{{pageNumber,auto}}

\page {zjournal,zstage4,zfinal}

{{zbody
## The First Evening

The shop is quiet. The shelves are full. The honesty box sits by the door, and the Producer is folded away for tomorrow.

For the first time since the explosion, everything is where it should be. Not where it used to be. Where it should be *now*.

The family thought Silverwood would end my experiments. Instead they have sent me to the greatest laboratory imaginable. Forests! Creatures! Plants no city merchant has ever seen! All of them waiting to be combined.

This and that. Or that and this.

I still wish I knew what went wrong that night. One day, perhaps, I shall understand it.

And here they know me as Ampersand. Not Ambersand.

Perhaps that is a good thing. Perhaps I shall make this new name mean something wonderful. Something of my own.

Yes yes. That would be nice.

{{zeditor
*Below this entry is a careful sketch of the new shop, with a particularly elaborate ampersand painted beneath the sign.*
}}

## A Final Note Before Tomorrow

Must prepare:

- Fresh glassware.
- Three replacement burners.
- Labels for the ordinary potions.
- *Different* labels for the experimental potions.
- A bigger honesty box.
- A second sign: <span class="zcaps">POTIONS!</span> <span class="zcaps">REMEDIES!</span> <span class="zcaps">RARE INGREDIENTS!</span> <span class="zcaps">VOLUNTEERS WANTED!</span>

No no. Might frighten the customers.

{{zeditor
*The next several lines are crossed out.*
}}
<div class="zscribble" aria-hidden="true"></div>

<span class="zcaps">YES YES!</span>

{{zeditor
*At the bottom of the page, in tiny, immaculate handwriting:*
}}

{{zmotto
*A failed experiment is only a failure if you learn nothing from it.*
}}

{{zeditor
*And beneath that, in much larger letters:*
}}

{{zshout
<span class="zcaps">ALSO REMEMBER TO TEST THE SAND BUCKET</span>.
}}

---

{{zeditor
*Inside the back cover is a pressed blue flower, a list of unidentified ingredients and a small handwritten notice:*
}}

> If you find something strange, bring it to Ampersand.
>
> If you taste something strange, tell Ampersand.
>
> If something strange happens <span class="zcaps">AFTER</span> you taste it…
>
> <span class="zcaps">COME QUICKLY!</span> Ampersand wishes to observe.
}}

{{footnote AMPERSAND'S APOTHECARIA | THE FIELD JOURNAL}}
{{pageNumber,auto}}

\page {ap50}
![](https://raw.githubusercontent.com/Omegaoliverid/Ampersand-s-Apothecary/52ab9f0ae9aedf06de291046c81bc2611d183a48/apo-shop.jpg){position:absolute,top:0px,left:0px,width:100%,height:100%,object-fit:cover,object-position:bottom}

{{tagpanel
### A field guide to 190 magical plants across 13 affinities. Identify and harvest useful parts, combine their properties through Harmony, and turn hard-won ingredients into potions, ointments and thrown preparations. Includes harvesting and brewing references, unusual outcomes, and Zoltan’s field journal.
##### FOR FIFTH-EDITION-COMPATIBLE GAMES
}}
<style>
/* TYPOGRAPHY ONLY — 21 October 2026; original colours and artwork retained. */
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;0,700;1,500;1,600&family=Crimson+Pro:ital,wght@0,400;0,600;0,700;1,400&family=Inter:wght@400;500;600;700&display=swap');
.page {font-family:'Crimson Pro',serif;}
.page p,.page li,.page td,.page dd,.page dt {font-family:'Crimson Pro',serif!important;}
.page h1,.page h2,.page h3,#p1 h1,#p1 h2,#p2 h1,#p2 h2,.page:has(.frontCover) h1,.page:has(.frontCover) h2 {font-family:'Cormorant Garamond',serif!important;}
.page h4,.page h5,.page th,.page .footnote,.page .pageNumber,.page .banner,.page .forge h5,.page .partcap h5,#p49 .columnWrapper h5 {font-family:'Inter',sans-serif!important;}
</style>

<style>
@import url('https://fonts.googleapis.com/css2?family=IM+Fell+English:ital@0;1&family=Caveat:wght@400;600;700&family=Nanum+Pen+Script&display=swap');
/* Zoltan's journal: all treatments are scoped to inserted pages. */
.page.zjournal {padding:17mm 18mm 17mm 20mm;column-count:1;position:relative;background-color:#e9dcae;background-image:repeating-linear-gradient(0deg,transparent 0px,transparent 23px,#8b745817 24px,transparent 25px),radial-gradient(ellipse at 100% 20%,#8d63344d,transparent 40%),linear-gradient(110deg,#d1bb82,#f2e7c6 15%,#ede0b9 85%,#c7ac73);box-shadow:inset 0 0 38px #61432388;--zhand:'IM Fell English';--zink:#34291f;}
.page.zjournal::before {content:'';position:absolute;inset:7mm 6mm;pointer-events:none;border-left:1px solid #785b3b35;border-right:2px solid #785b3b25;}
.page.zjournal .columnWrapper {column-count:1;}
.page.zjournal .zbody {position:relative;z-index:1;color:var(--zink);font-family:var(--zhand),cursive!important;font-size:17px;line-height:1.24;}
.page.zjournal .zbody p,.page.zjournal .zbody li {font-family:var(--zhand),cursive!important;font-size:inherit;line-height:inherit;color:inherit;margin:0 0 7px;text-indent:0;}
.page.zjournal .zbody h1,.page.zjournal .zbody h2 {font-family:var(--zhand),cursive!important;color:var(--zink);font-variant:normal;text-transform:none;letter-spacing:0;border:0;line-height:1.06;margin:16px 0 10px;break-after:avoid;}
.page.zjournal .zbody h1 {font-size:40px;}
.page.zjournal .zbody h2 {font-size:27px;}
.page.zjournal .zbody ul {padding-left:20px;margin:6px 0 10px;}
.page.zjournal .zbody strong {font-weight:700;}
.page.zjournal .zbody .zeditor,.page.zjournal .zbody .zeditor p {font-family:'Crimson Pro',serif!important;font-size:11px;line-height:1.28;color:#514a3e;font-style:normal;margin:8px 0;}
.page.zjournal .zeditor em {font-style:normal;}
.page.zjournal .footnote {font-size:9px;bottom:22px;color:#53432e;}
.page.zjournal .pageNumber {color:#53432e;}
.page.zjournal .zbookplate {background:#f5edd5;border:1px solid #63513a;outline:1px solid #63513a;outline-offset:4px;padding:16px;margin:24px 10px;transform:rotate(-1.2deg);box-shadow:2px 3px 3px #33251133;}
.page.zjournal .zbookplate p {font-family:'IM Fell English',serif!important;font-size:18px;text-align:center;}
.page.zjournal.ztitle .zbody {padding:24px 20px;}
.page.zjournal.ztitle h1 {font-size:48px;margin:30px 0;}
.page.zjournal.ztitle .zmetadata {margin-bottom:25px;}
.page.zjournal.zstage1::after {content:'';position:absolute;right:20px;bottom:85px;width:120px;height:120px;border:7px double #92744133;border-radius:50%;transform:scaleY(.7) rotate(12deg);box-shadow:0 0 8px #76532622;}
.page.zjournal.zstage2 {--zhand:'Caveat';--zink:#30281e;}
.page.zjournal.zstage2 .zbody {font-size:19px;line-height:1.12;}
.page.zjournal.zdense .zbody {column-count:2;column-gap:24px;font-size:19px;line-height:1.06;}
.page.zjournal.zdense h2 {font-size:24px;}
.page.zjournal.zstage2 .zbody>p:nth-of-type(3n) {transform:rotate(-.35deg);}
.page.zjournal.zstage2 .zbody>p:nth-of-type(4n) {transform:rotate(.4deg);}
.page.zjournal.zstage2::after {content:'';position:absolute;inset:30px 8px 55px auto;width:35px;background:radial-gradient(ellipse at 20% 15%,#302921 0 4px,transparent 5px),radial-gradient(circle at 70% 17%,#302921 0 2px,transparent 3px),radial-gradient(circle at 40% 61%,#302921 0 6px,transparent 7px),radial-gradient(ellipse at 65% 63%,#302921 0 2px,transparent 3px);}
.page.zjournal.zchemical {background-image:radial-gradient(ellipse at 98% 48%,#49612b66,transparent 19%),repeating-linear-gradient(0deg,transparent 0px,transparent 23px,#8b745817 24px,transparent 25px),linear-gradient(110deg,#d1bb82,#f2e7c6 15%,#ede0b9 85%,#c7ac73);}
.page.zjournal.zchemical .zbody::after {content:'';display:block;width:70px;height:32px;margin:25px 0 0 auto;border-radius:50%;background:repeating-radial-gradient(ellipse,#463b2933 0 1px,transparent 2px 4px);transform:rotate(-28deg);}
.page.zjournal .zdouble {text-decoration:underline double;text-underline-offset:3px;text-decoration-thickness:1px;}
.page.zjournal.zburnt {--zhand:'Caveat';--zink:#302219;}
.page.zjournal.zburnt .zbody {font-size:26px;line-height:1.2;max-width:610px;transform:rotate(-1deg);}
.page.zjournal.zburnt .zbody h2 {font-size:39px;}
.page.zjournal.zburnt .zbody>p:nth-of-type(3n) {transform:rotate(1.4deg);}
.page.zjournal.zburnt::after {content:'';position:absolute;bottom:0;left:0;right:0;height:200px;background:linear-gradient(to top,#17130f 0%,#422b17 17%,#976032b0 36%,#a3763c40 65%,transparent);clip-path:polygon(0 19%,4% 28%,8% 17%,13% 32%,18% 24%,23% 35%,29% 18%,35% 26%,43% 34%,51% 18%,56% 31%,63% 21%,70% 28%,77% 17%,83% 30%,89% 20%,95% 32%,100% 22%,100% 100%,0 100%);}
.page.zjournal.zburnt .footnote,.page.zjournal.zburnt .pageNumber {z-index:3;color:#f1e4c9;}
.page.zjournal.zafter {background:#d9d7ca;background-image:linear-gradient(95deg,#9d9b8d44,transparent 15%,#efeee533 55%,#92918433);--zink:#66645c;box-shadow:inset 0 0 22px #55534444;}
.page.zjournal.zafter .zbody {font-size:17px;line-height:1.3;}
.page.zjournal.zafter::before {inset:0 auto 0 8px;width:17px;border:0;background:#77736855;clip-path:polygon(0 0,90% 0,43% 4%,100% 9%,30% 14%,90% 20%,40% 28%,100% 36%,30% 44%,90% 53%,40% 61%,100% 70%,30% 79%,90% 88%,40% 95%,100% 100%,0 100%);}
.page.zjournal.zstage4 {--zhand:'Nanum Pen Script';--zink:#38291e;}
.page.zjournal.zstage4 .zbody {font-size:22px;line-height:1.02;}
.page.zjournal.zstage4 .zbody h2 {font-size:29px;}
.page.zjournal.ztwocol .zbody {column-count:2;column-gap:24px;font-size:20px;line-height:1.04;}
.page.zjournal.ztwocol h2 {font-size:25px;}
.page.zjournal.ztravel::after {content:'';position:absolute;bottom:55px;right:14px;width:34px;height:95px;border-radius:50% 40% 25% 25%;transform:rotate(-22deg);background:repeating-linear-gradient(0deg,#69533344 0 5px,transparent 5px 8px);box-shadow:0 0 12px #66513233;}
.page.zjournal.ztravel .zbody ul {border-right:2px dotted #78513255;padding-right:10px;}
.page.zjournal.ztravel .zbody ul::after {content:'';display:block;width:26px;height:22px;margin:8px 0 0 auto;border-radius:40% 60% 32% 55%;background:#3d291a;box-shadow:0 0 0 3px #8e6034,0 0 8px 5px #ad865955;}
.page.zjournal .zsign {border:2px solid #a58a44;outline:1px solid #a58a4477;outline-offset:3px;padding:10px 4px;margin:16px 5px;transform:rotate(-1deg);text-align:center;color:#806020;}
.page.zjournal .zsign p {font-size:24px!important;}
.page.zjournal .zproducer {font-size:28px;line-height:.95;transform:rotate(-1deg);margin:15px 0;letter-spacing:-.8px;}
.page.zjournal .zmotto {margin:15px 0 5px;}
.page.zjournal .zmotto p {font-family:'IM Fell English',serif!important;font-size:13px;}
.page.zjournal .zshout {font-size:35px;line-height:.95;transform:rotate(-1.3deg);margin:12px 0 22px;}
.page.zjournal blockquote {font-family:var(--zhand),cursive!important;background:#f5e9bc;border:0;padding:15px 18px;margin:15px 0 0 90px;box-shadow:2px 4px 6px #38271744;transform:rotate(1deg);position:relative;}
.page.zjournal blockquote::before {content:'';position:absolute;top:5px;left:48%;width:8px;height:8px;background:#775440;border-radius:50%;box-shadow:1px 2px 2px #0008;}
.page.zjournal blockquote::after {content:'';position:absolute;width:65px;height:85px;left:-75px;top:10px;background:radial-gradient(ellipse at 38% 25%,#527796 0 9px,transparent 10px),radial-gradient(ellipse at 62% 25%,#486b90 0 9px,transparent 10px),radial-gradient(ellipse at 30% 43%,#7696b0 0 9px,transparent 10px),radial-gradient(ellipse at 67% 43%,#567b9b 0 9px,transparent 10px),radial-gradient(circle at 49% 37%,#b7a56a 0 5px,transparent 6px),linear-gradient(87deg,transparent 48%,#6b754c 49% 51%,transparent 52%);transform:rotate(-13deg);}
.page.zjournal.zfinal hr {border:0;border-top:1px dashed #77664c;margin:15px 0;}
@media print {.page.zjournal {-webkit-print-color-adjust:exact;print-color-adjust:exact;}}
</style>

<style>
.page.zjournal.zdense .zbody {column-count:2;column-gap:24px;font-size:19px;line-height:1.04;}
.page.zjournal.zdense .zbody p {margin-bottom:4px;}
.page.zjournal.ztwocol {padding-left:17mm;padding-right:16mm;}
.page.zjournal.ztwocol .zbody {font-size:20px;line-height:1;}
.page.zjournal.ztwocol .zbody p,.page.zjournal.ztwocol .zbody li {margin-bottom:4px;}
.page.zjournal.ztwocol .zbody h2 {margin:10px 0 7px;font-size:25px;}
.page.zjournal.zfinal .zbody {font-size:20px;line-height:1;}
.page.zjournal.zfinal .zbody p,.page.zjournal.zfinal .zbody li {margin-bottom:4px;}
.page.zjournal.zfinal .zbody h2 {margin:12px 0 8px;}
.page.zjournal.zfinal .zbody .zshout p {font-size:32px;line-height:.95;}
.page.zjournal.zfinal blockquote p {font-size:19px;}
.page.zjournal.zburnt .footnote,.page.zjournal.zburnt .pageNumber {position:absolute;z-index:5!important;}
.page.zjournal .zamp {font-size:52px;color:#9b7826;line-height:.8;display:inline-block;transform:rotate(-7deg);}
.page.zjournal .zscribble {height:12px;width:150px;margin:5px 0;background:repeating-linear-gradient(175deg,transparent 0 3px,#3c3020 4px,transparent 5px 7px);transform:rotate(-2deg);}
.page.zjournal.zsignpage::after {content:'';position:absolute;right:10px;top:13px;width:95px;height:30px;border:5px double #95752c44;border-radius:50%;transform:rotate(15deg);}
.page.zjournal.ztitle .zbody>p:first-of-type,.page.zjournal.zstage1 .zbody {font-style:italic;}
</style>

<style>
.page.zjournal.zfinal .zbody {column-count:2;column-gap:27px;font-size:21px;line-height:1.02;}
.page.zjournal.zfinal .zbody h2 {font-size:26px;}
.page.zjournal.zfinal blockquote {margin:22px 0 0 26px;padding:14px 12px;break-inside:avoid;}
.page.zjournal.zfinal blockquote::after {left:-38px;width:34px;height:65px;}
.page.zjournal.zfinal .zshout {break-inside:avoid;}
.page.zjournal.zburnt .footnote,.page.zjournal.zburnt .pageNumber {color:#f6ead5!important;opacity:1!important;}
</style>

<style>
.page.zjournal .zcaps {font-weight:700;text-shadow:.25px 0 currentColor;}
.page.zjournal.zfinal blockquote::after {width:50px;left:-55px;}
</style>

<style>
.page.zjournal.zburnt {isolation:isolate;}
.page.zjournal.zburnt::after {z-index:-1;}
</style>

<style>
.page.zjournal.ztitle .zoldname {position:relative;display:inline-block;text-decoration:line-through;text-decoration-thickness:2px;text-decoration-color:#59432d;}
.page.zjournal.ztitle .zoldname::after {content:'';position:absolute;left:-3px;right:-5px;top:55%;border-top:2px solid #59432d;transform:rotate(-6deg);}
.page.zjournal.ztitle .znewname {display:block;font-family:'Caveat',cursive!important;font-size:62px;font-weight:700;line-height:.9;transform:rotate(-7deg);margin:9px 0 0 40px;letter-spacing:-2px;}
.page.zjournal.ztitle .zsignatures {display:flex;gap:27px;align-items:center;margin:25px 0 22px 10px;color:#69512b;font-family:'Caveat',cursive;font-size:29px;}
.page.zjournal.ztitle .zsignatures span:nth-child(1) {transform:rotate(5deg);text-decoration:line-through;}
.page.zjournal.ztitle .zsignatures span:nth-child(2) {transform:rotate(-5deg);border-bottom:1px solid #69512b;}
.page.zjournal.ztitle .zsignatures span:nth-child(3) {font-family:'Nanum Pen Script',cursive;font-size:43px;transform:rotate(6deg);}
</style>

<style>
.page.zjournal.zburnt .footnote,.page.zjournal.zburnt .pageNumber {bottom:210px!important;color:#53432e!important;}
</style>

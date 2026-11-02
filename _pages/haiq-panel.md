---
title: HAI-Q Panel
layout: sub
permalink: /haiq-panel/
---

<style>
  :root { --haiq-navy: #123a61; --haiq-blue: #176b9c; --haiq-cyan: #23b7cf; --haiq-pale: #eef9fc; --haiq-ink: #263f53; }
  .haiq-page { color: var(--haiq-ink); }
  .haiq-page hr { margin: 2rem 0; border: 0; border-top: 1px solid #d6e6ee; }
  .haiq-page > h2 { margin-bottom: 1.1rem; color: var(--haiq-navy); font-size: 1.65rem; }
  .haiq-hero { position: relative; min-height: 500px; margin: .35rem 0 2.5rem; overflow: hidden; border-radius: .35rem; background: radial-gradient(circle at 78% 42%, rgba(16,143,210,.3), transparent 25%), radial-gradient(circle at 86% 84%, rgba(0,210,238,.2), transparent 24%), linear-gradient(118deg, #041a35 0%, #062a50 53%, #041e3d 100%); isolation: isolate; }
  .haiq-hero::before { content: ""; position: absolute; inset: 0; z-index: -1; background-image: linear-gradient(rgba(65,193,232,.04) 1px, transparent 1px), linear-gradient(90deg, rgba(65,193,232,.04) 1px, transparent 1px); background-size: 36px 36px; mask-image: linear-gradient(90deg, transparent 32%, #000 65%); }
  .haiq-hero::after { content: ""; position: absolute; left: 0; right: 0; bottom: 0; z-index: 5; height: 2px; background: linear-gradient(90deg, var(--haiq-cyan), rgba(255,255,255,.75), transparent); animation: haiq-flow 5s ease-in-out infinite alternate; }
  .haiq-hero-copy { position: relative; z-index: 4; width: min(55%, 630px); padding: 2.65rem 2.4rem; color: #fff; animation: haiq-rise .8s ease-out both; }
  .haiq-hero-scene { position: absolute; top: 0; right: 0; bottom: 0; z-index: 1; width: 58%; overflow: hidden; pointer-events: none; perspective: 900px; }
  .haiq-hero-canvas, .haiq-flow-lines { position: absolute; inset: 0; width: 100%; height: 100%; }
  .haiq-flow-lines { opacity: .72; filter: drop-shadow(0 0 7px rgba(48,211,246,.55)); }
  .haiq-flow-lines path { fill: none; stroke: rgba(71,211,246,.65); stroke-width: 1.2; stroke-dasharray: 7 12; animation: haiq-dash 7s linear infinite; }
  .haiq-question-cloud { position: absolute; top: 8%; left: 7%; width: 55%; height: 42%; transform-style: preserve-3d; }
  .haiq-question-card { position: absolute; top: 22%; left: 25%; display: grid; width: 42px; height: 32px; place-items: center; border: 1px solid rgba(119,227,255,.7); border-radius: 5px; background: linear-gradient(145deg, rgba(34,154,219,.5), rgba(10,65,120,.18)); box-shadow: inset 0 0 12px rgba(132,235,255,.18), 0 0 10px rgba(41,200,241,.2); color: rgba(224,250,255,.9); font-size: 1.05rem; font-weight: 700; opacity: 0; transform: translate3d(var(--x), var(--y), var(--z)) scale(var(--s)); animation: haiq-card-stream 14s ease-in-out infinite; animation-delay: var(--delay); }
  .haiq-source-badge, .haiq-top-badge { position: absolute; padding: .42rem .7rem; border: 1px solid rgba(112,225,255,.7); border-radius: 4px; background: rgba(4,44,85,.58); box-shadow: inset 0 0 12px rgba(55,191,234,.15), 0 0 18px rgba(47,199,240,.2); color: #dffaff; text-align: center; text-transform: uppercase; }
  .haiq-source-badge { top: 7%; right: 8%; animation: haiq-glow 3.8s ease-in-out infinite; }
  .haiq-source-badge strong, .haiq-top-badge strong { display: block; color: #fff; font-size: 1.05rem; line-height: 1; }
  .haiq-source-badge span, .haiq-top-badge span { font-size: .56rem; letter-spacing: .09em; }
  .haiq-processor { position: absolute; top: 39%; left: 55%; width: 150px; height: 150px; transform: translate(-50%, -50%); }
  .haiq-ring { position: absolute; inset: 12%; border: 1px solid rgba(85,220,250,.72); border-radius: 50%; box-shadow: 0 0 15px rgba(34,187,228,.25), inset 0 0 13px rgba(34,187,228,.18); animation: haiq-spin 12s linear infinite; }
  .haiq-ring::before, .haiq-ring::after { content: ""; position: absolute; width: 7px; height: 7px; border-radius: 50%; background: #9ff5ff; box-shadow: 0 0 10px #45dff7; }
  .haiq-ring::before { top: -4px; left: 48%; } .haiq-ring::after { right: 4px; bottom: 18%; }
  .haiq-ring--two { inset: 2%; border-style: dashed; opacity: .65; animation-name: haiq-spin-tilted; animation-duration: 18s; animation-direction: reverse; transform: rotateX(63deg); }
  .haiq-ring--three { inset: 24%; opacity: .8; animation-duration: 8s; }
  .haiq-chip { position: absolute; inset: 34%; display: grid; place-items: center; border: 1px solid #83efff; border-radius: 6px; background: linear-gradient(145deg, #157cc5, #063e77); box-shadow: 0 0 22px rgba(45,211,246,.75), inset 0 0 12px rgba(193,248,255,.28); color: #fff; font-size: 1rem; font-weight: 800; transform: rotate(-8deg); animation: haiq-chip-breathe 3.5s ease-in-out infinite; }
  .haiq-process-tags { position: absolute; top: 23%; right: 2%; display: grid; gap: .42rem; }
  .haiq-process-tags span { min-width: 104px; padding: .33rem .55rem; border-left: 2px solid #45d9f2; border-radius: 0 9px 9px 0; background: linear-gradient(90deg, rgba(11,77,133,.76), rgba(7,45,87,.36)); color: #dffaff; font-size: .59rem; font-weight: 700; letter-spacing: .05em; opacity: .45; animation: haiq-tag-cycle 14s ease-in-out infinite; }
  .haiq-process-tags span:nth-child(2) { animation-delay: 1.2s; } .haiq-process-tags span:nth-child(3) { animation-delay: 2.4s; } .haiq-process-tags span:nth-child(4) { animation-delay: 3.6s; }
  .haiq-platform { position: absolute; right: 12%; bottom: 6%; width: 245px; height: 74px; border: 1px solid rgba(84,219,249,.65); border-radius: 50%; background: radial-gradient(ellipse, rgba(40,195,231,.25), rgba(4,39,76,.12) 63%, transparent 65%); box-shadow: 0 0 28px rgba(30,188,227,.35), inset 0 0 18px rgba(118,235,255,.24); animation: haiq-scan 4.5s ease-in-out infinite; }
  .haiq-top-cards { position: absolute; left: 50%; bottom: 42%; display: flex; gap: 5px; transform: translateX(-50%); }
  .haiq-top-cards span { display: grid; width: 35px; height: 48px; place-items: center; border: 1px solid #86eeff; border-radius: 4px; background: linear-gradient(160deg, rgba(38,150,212,.9), rgba(5,50,94,.9)); box-shadow: 0 0 12px rgba(63,214,246,.45); color: #fff; font-weight: 800; opacity: 0; transform: translateY(38px); animation: haiq-top-rise 14s ease-in-out infinite; }
  .haiq-top-cards span:nth-child(2) { animation-delay: .25s; } .haiq-top-cards span:nth-child(3) { animation-delay: .5s; width: 42px; height: 57px; } .haiq-top-cards span:nth-child(4) { animation-delay: .75s; } .haiq-top-cards span:nth-child(5) { animation-delay: 1s; }
  .haiq-top-badge { right: -1%; bottom: 8%; opacity: .8; animation: haiq-glow 3.8s ease-in-out infinite 1.4s; }
  .haiq-hero.is-paused *, .haiq-hero.is-paused *::before, .haiq-hero.is-paused *::after { animation-play-state: paused !important; }
  .haiq-logo { display: block; width: 190px; max-width: 46%; height: auto; margin-bottom: 1.1rem; padding: .35rem .45rem; border-radius: .2rem; background: rgba(255,255,255,.92); }
  .haiq-label { margin: 0 0 .45rem; color: #9feeff; font-size: .88rem; font-weight: 700; letter-spacing: .1em; text-transform: uppercase; }
  .haiq-title { margin: 0 0 .7rem; color: #fff; font-size: clamp(2rem, 4vw, 3.15rem); line-height: 1.08; text-shadow: 0 2px 22px rgba(0,0,0,.2); }
  .haiq-subtitle { max-width: 590px; margin: 0; color: #e9f8fc; font-size: 1.06rem; line-height: 1.55; }
  .haiq-session { margin: 1.25rem 0 0; padding-top: .85rem; border-top: 1px solid rgba(178,232,247,.55); color: #fff; font-size: .92rem; line-height: 1.5; }
  .haiq-split { display: grid; grid-template-columns: minmax(0, 1.05fr) minmax(300px, .95fr); align-items: center; gap: 2.2rem; }
  .haiq-split--reverse .haiq-visual { order: -1; }
  .haiq-copy p:last-child { margin-bottom: 0; }
  .haiq-visual { position: relative; margin: 0; overflow: hidden; border-radius: .25rem; background: var(--haiq-pale); box-shadow: 0 6px 18px rgba(25,84,122,.1); }
  .haiq-visual img { display: block; width: 100%; height: 100%; aspect-ratio: 2 / 1; object-fit: cover; transition: transform .6s ease; }
  .haiq-visual:hover img { transform: scale(1.02); }
  .haiq-about { max-width: 920px; margin: 0; line-height: 1.65; }
  .haiq-process { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); align-items: stretch; gap: 1.35rem; margin: 1.15rem 0 .2rem; }
  .haiq-step { display: flex; min-width: 0; overflow: hidden; border-radius: .75rem; background: #fff; box-shadow: 0 8px 22px rgba(20,77,112,.13); opacity: 0; animation: haiq-card-in .55s ease-out forwards; transition: transform .25s ease, box-shadow .25s ease; }
  .haiq-step:nth-child(2) { animation-delay: .12s; }
  .haiq-step:nth-child(3) { animation-delay: .24s; }
  .haiq-step:hover { transform: translateY(-4px); box-shadow: 0 12px 28px rgba(20,77,112,.18); }
  .haiq-step-inner { display: flex; width: 100%; flex-direction: column; }
  .haiq-step-image { display: block; width: min(72%, 220px); height: auto; margin: 1rem auto; border-radius: .4rem; transition: transform .35s ease; }
  .haiq-step:hover .haiq-step-image { transform: scale(1.035); }
  .haiq-step-body { display: flex; flex: 1; flex-direction: column; padding: 1.15rem 1.1rem 1.25rem; border-top: 3px solid #36c2d8; }
  .haiq-step-heading { margin-bottom: .65rem; }
  .haiq-step-number { display: block; margin-bottom: .25rem; color: #1685bd; font-size: 1.3rem; font-weight: 800; line-height: 1; letter-spacing: .03em; }
  .haiq-step-number::after { content: ""; display: block; width: 2.25rem; height: 2px; margin-top: .45rem; background: #40c4d8; }
  .haiq-step h5 { min-height: 3.55rem; margin: 0; color: #163f67; font-size: 1rem; line-height: 1.4; }
  .haiq-step p { margin: auto 0 0; color: #40586a; font-size: .9rem; line-height: 1.55; }
  .haiq-voting { display: grid; grid-template-columns: minmax(0, 1fr) 195px; align-items: center; gap: 1.8rem; margin: 1rem 0 1.6rem; padding: 1.5rem; border-left: 4px solid var(--haiq-cyan); border-radius: .2rem; background: #eef8fb; }
  .haiq-voting-copy h4 { margin-top: 0; color: var(--haiq-navy); font-size: 1.3rem; }
  .haiq-voting-copy p { margin: 0 0 .75rem; }
  .haiq-deadline { display: inline-block; margin: .15rem 0 .9rem !important; padding: .48rem .75rem; border-left: 3px solid var(--haiq-cyan); background: #fff; color: var(--haiq-navy); }
  .haiq-vote-button { display: inline-block; margin: .2rem 0 0; padding: .72rem 1.45rem; border-radius: 2rem; background: linear-gradient(100deg, var(--haiq-blue), #139bb8); box-shadow: 0 7px 16px rgba(16,112,151,.22); color: #fff !important; font-weight: 700; text-decoration: none !important; transition: transform .2s ease, box-shadow .2s ease; }
  .haiq-vote-button:hover, .haiq-vote-button:focus { transform: translateY(-2px); box-shadow: 0 10px 20px rgba(16,112,151,.3); }
  .haiq-voting-qr { text-align: center; }
  .haiq-qr { display: block; width: 180px; max-width: 100%; height: auto; margin: 0 auto .45rem; padding: .45rem; border-radius: .2rem; background: #fff; box-shadow: 0 5px 14px rgba(12,66,98,.1); }
  .haiq-scan-label { color: var(--haiq-blue); font-size: .9rem; }
  .haiq-discussion-visual img { aspect-ratio: 16 / 9; }
  .haiq-people-sections { display: grid; grid-template-columns: 1fr 1fr; gap: 2rem; }
  .haiq-people-section { padding-left: 1rem; border-left: 3px solid #8ed8e6; }
  .haiq-people-section h2 { margin: 0 0 .85rem; color: var(--haiq-navy); font-size: 1.45rem; }
  .haiq-people { margin: 0; color: #334f64; }
  .haiq-person { margin: 0 0 .4rem; line-height: 1.5; }
  .haiq-person:last-child { margin-bottom: 0; }
  .haiq-contact-grid { display: flex; flex-wrap: wrap; gap: .7rem 2rem; margin-top: .8rem; }
  .haiq-contact-grid p { margin: 0; }
  .haiq-ethics-line { font-size: .92rem; }
  @keyframes haiq-flow { from { background-position: 0 0; } to { background-position: 100% 0; } }
  @keyframes haiq-rise { from { opacity: 0; transform: translateY(12px); } to { opacity: 1; transform: translateY(0); } }
  @keyframes haiq-card-in { from { opacity: 0; transform: translateY(14px); } to { opacity: 1; transform: translateY(0); } }
  @keyframes haiq-dash { to { stroke-dashoffset: -76; } }
  @keyframes haiq-spin { to { transform: rotate(360deg); } }
  @keyframes haiq-spin-tilted { to { transform: rotateX(63deg) rotate(360deg); } }
  @keyframes haiq-chip-breathe { 0%,100% { filter: brightness(.9); transform: rotate(-8deg) scale(.96); } 50% { filter: brightness(1.25); transform: rotate(-8deg) scale(1.04); } }
  @keyframes haiq-glow { 0%,100% { opacity: .62; filter: brightness(.85); } 50% { opacity: 1; filter: brightness(1.2); } }
  @keyframes haiq-tag-cycle { 0%,18%,100% { opacity: .36; transform: translateX(7px); } 28%,62% { opacity: 1; transform: translateX(0); } 72% { opacity: .48; } }
  @keyframes haiq-scan { 0%,100% { transform: scale(.96); box-shadow: 0 0 18px rgba(30,188,227,.25), inset 0 0 12px rgba(118,235,255,.2); } 50% { transform: scale(1.03); box-shadow: 0 0 34px rgba(30,188,227,.48), inset 0 0 24px rgba(118,235,255,.32); } }
  @keyframes haiq-top-rise { 0%,45% { opacity: 0; transform: translateY(38px) scale(.86); } 58%,88% { opacity: .95; transform: translateY(0) scale(1); } 100% { opacity: 0; transform: translateY(-8px) scale(.96); } }
  @keyframes haiq-card-stream { 0%,8% { opacity: 0; transform: translate3d(var(--x), var(--y), var(--z)) scale(var(--s)); } 18%,40% { opacity: .68; } 58% { opacity: .85; transform: translate3d(145px, 112px, 0) scale(.62); } 68%,100% { opacity: 0; transform: translate3d(210px, 190px, -80px) scale(.28); } }
  @media (min-width: 1200px) {
    .haiq-ethics-line { white-space: nowrap; }
  }
  @media (max-width: 767.98px) {
    .haiq-hero { min-height: 650px; }
    .haiq-hero-copy { width: 100%; padding: 2rem 1.5rem 300px; }
    .haiq-hero-scene { top: auto; width: 100%; height: 330px; opacity: .94; }
    .haiq-process-tags { right: 1%; }
    .haiq-split { grid-template-columns: 1fr; gap: 1.2rem; }
    .haiq-split--reverse .haiq-visual { order: 0; }
    .haiq-process { grid-template-columns: 1fr; gap: 1.2rem; }
    .haiq-step h5 { min-height: 0; }
    .haiq-voting { grid-template-columns: minmax(0, 1fr) 180px; padding: 1.3rem; }
  }
  @media (max-width: 575.98px) {
    .haiq-page hr { margin: 1.8rem 0; }
    .haiq-hero { min-height: 690px; }
    .haiq-hero-copy { width: 100%; padding: 1.5rem 1.2rem 310px; }
    .haiq-hero-scene { height: 310px; transform: scale(.96); transform-origin: bottom center; }
    .haiq-source-badge { right: 3%; }
    .haiq-process-tags { display: none; }
    .haiq-processor { left: 56%; }
    .haiq-platform { right: 4%; }
    .haiq-logo { width: 155px; max-width: 52%; }
    .haiq-title { font-size: 1.8rem; }
    .haiq-label { font-size: .85rem; }
    .haiq-session { font-size: .9rem; }
    .haiq-visual img { aspect-ratio: 4 / 3; }
    .haiq-voting { grid-template-columns: 1fr; gap: 1.25rem; padding: 1.15rem; }
    .haiq-qr { width: 165px; }
    .haiq-people-sections { grid-template-columns: 1fr; gap: 1.5rem; }
    .haiq-contact-grid { display: block; }
    .haiq-contact-grid p + p { margin-top: .7rem; }
  }
  @media (prefers-reduced-motion: reduce) {
    .haiq-hero::after, .haiq-hero-copy, .haiq-hero-scene *, .haiq-hero-scene *::before, .haiq-hero-scene *::after { animation: none !important; }
    .haiq-question-card { opacity: .62; }
    .haiq-top-cards span { opacity: .92; transform: translateY(0); }
    .haiq-process-tags span, .haiq-source-badge, .haiq-top-badge { opacity: .82; transform: none; }
    .haiq-step { opacity: 1; animation: none; }
    .haiq-step, .haiq-step-image, .haiq-visual img, .haiq-vote-button { transition: none; }
  }
</style>

<div class="haiq-page" markdown="1">

<div class="haiq-hero" role="img" aria-label="Future AI question space visualized as a luminous semantic knowledge network">
  <div class="haiq-hero-scene" aria-hidden="true">
    <canvas class="haiq-hero-canvas"></canvas>
    <svg class="haiq-flow-lines" viewBox="0 0 700 500" preserveAspectRatio="none">
      <path d="M80 75 C250 70 250 180 390 205 S500 250 455 430"></path>
      <path d="M125 145 C270 120 300 180 390 205 S420 340 455 430"></path>
      <path d="M210 40 C300 95 320 160 390 205 C450 245 430 360 455 430"></path>
    </svg>
    <div class="haiq-question-cloud">
      <span class="haiq-question-card" style="--x:-115px;--y:-35px;--z:-80px;--s:.62;--delay:-1s">?</span>
      <span class="haiq-question-card" style="--x:-60px;--y:5px;--z:20px;--s:1;--delay:-3s">?</span>
      <span class="haiq-question-card" style="--x:20px;--y:-25px;--z:55px;--s:1.2;--delay:-5s">?</span>
      <span class="haiq-question-card" style="--x:95px;--y:12px;--z:-10px;--s:.86;--delay:-7s">?</span>
      <span class="haiq-question-card" style="--x:-90px;--y:70px;--z:40px;--s:.9;--delay:-9s">?</span>
      <span class="haiq-question-card" style="--x:-10px;--y:82px;--z:-20px;--s:.72;--delay:-11s">?</span>
      <span class="haiq-question-card" style="--x:82px;--y:88px;--z:70px;--s:1.1;--delay:-13s">?</span>
      <span class="haiq-question-card" style="--x:145px;--y:55px;--z:-50px;--s:.58;--delay:-2s">?</span>
      <span class="haiq-question-card" style="--x:-135px;--y:120px;--z:-30px;--s:.5;--delay:-4s">?</span>
      <span class="haiq-question-card" style="--x:42px;--y:135px;--z:30px;--s:.78;--delay:-6s">?</span>
      <span class="haiq-question-card" style="--x:128px;--y:130px;--z:10px;--s:.66;--delay:-8s">?</span>
      <span class="haiq-question-card" style="--x:178px;--y:96px;--z:-65px;--s:.48;--delay:-10s">?</span>
    </div>
    <div class="haiq-source-badge"><strong>1000</strong><span>Original Questions</span></div>
    <div class="haiq-processor">
      <span class="haiq-ring"></span><span class="haiq-ring haiq-ring--two"></span><span class="haiq-ring haiq-ring--three"></span>
      <span class="haiq-chip">AI</span>
    </div>
    <div class="haiq-process-tags"><span>FILTERING</span><span>AGGREGATION</span><span>SELECTION</span><span>RANKING</span></div>
    <div class="haiq-platform"><div class="haiq-top-cards"><span>?</span><span>?</span><span>?</span><span>?</span><span>?</span></div></div>
    <div class="haiq-top-badge"><strong>TOP</strong><span>Top Questions</span></div>
  </div>
  <div class="haiq-hero-copy">
    <img class="haiq-logo" src="{{ '/assets/images/haiq/haiq-logo-from-poster.png' | relative_url }}" alt="HAI-Q: Hyper/Super AI Questions Initiative logo">
    <p class="haiq-label">Panel-Q | HAI-Q</p>
    <h1 class="haiq-title">Questions of a Thousand Questions for Future AI</h1>
    <p class="haiq-subtitle">Methods, Rationale, and Reflections on Large-Scale Open Question Selection</p>
    <p class="haiq-session"><strong>November 12, 2026</strong> &nbsp;|&nbsp; 10:50 AM &ndash; 12:20 PM AEDT &nbsp;|&nbsp; Melbourne, Australia</p>
  </div>
</div>

<script>
(() => {
  const hero = document.querySelector('.haiq-hero');
  const canvas = hero && hero.querySelector('.haiq-hero-canvas');
  if (!hero || !canvas) return;

  const context = canvas.getContext('2d', { alpha: true });
  const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
  const particles = Array.from({ length: 44 }, (_, index) => ({
    t: (index / 44 + Math.random() * .12) % 1,
    speed: .00006 + Math.random() * .000025,
    size: .7 + Math.random() * 1.8,
    drift: (Math.random() - .5) * 18
  }));
  let width = 0;
  let height = 0;
  let visible = true;
  let frame = 0;
  let previousTime = 0;

  const resize = () => {
    const rect = canvas.getBoundingClientRect();
    const ratio = Math.min(window.devicePixelRatio || 1, 1.5);
    width = Math.max(1, rect.width);
    height = Math.max(1, rect.height);
    canvas.width = Math.round(width * ratio);
    canvas.height = Math.round(height * ratio);
    context.setTransform(ratio, 0, 0, ratio, 0, 0);
  };

  const bezier = (a, b, c, t) => {
    const inverse = 1 - t;
    return inverse * inverse * a + 2 * inverse * t * b + t * t * c;
  };

  const position = particle => {
    if (particle.t < .58) {
      const t = particle.t / .58;
      return {
        x: bezier(width * .08, width * .38, width * .56, t),
        y: bezier(height * (.1 + particle.drift / 200), height * .18, height * .42, t)
      };
    }
    const t = (particle.t - .58) / .42;
    return {
      x: bezier(width * .56, width * .62, width * .68, t),
      y: bezier(height * .42, height * .58, height * .84, t)
    };
  };

  const render = time => {
    context.clearRect(0, 0, width, height);
    const delta = Math.min(40, time - previousTime || 16);
    previousTime = time;
    particles.forEach((particle, index) => {
      if (!reduceMotion.matches) particle.t = (particle.t + particle.speed * delta) % 1;
      const point = position(particle);
      const pulse = .55 + Math.sin(time * .0016 + index) * .25;
      context.beginPath();
      context.fillStyle = `rgba(111, 230, 255, ${Math.max(.18, pulse)})`;
      context.shadowColor = 'rgba(45, 207, 245, .85)';
      context.shadowBlur = 8;
      context.arc(point.x, point.y + particle.drift, particle.size, 0, Math.PI * 2);
      context.fill();
    });
    context.shadowBlur = 0;
  };

  const animate = time => {
    render(time);
    if (visible && !document.hidden && !reduceMotion.matches) frame = requestAnimationFrame(animate);
  };

  const sync = () => {
    const paused = !visible || document.hidden || reduceMotion.matches;
    hero.classList.toggle('is-paused', paused);
    cancelAnimationFrame(frame);
    if (paused) render(performance.now());
    else frame = requestAnimationFrame(animate);
  };

  new ResizeObserver(() => { resize(); render(performance.now()); }).observe(canvas);
  new IntersectionObserver(entries => {
    visible = entries[0].isIntersecting;
    sync();
  }, { threshold: .08 }).observe(hero);
  document.addEventListener('visibilitychange', sync);
  reduceMotion.addEventListener('change', sync);
  resize();
  sync();
})();
</script>

<hr>

## About HAI-Q

<p class="haiq-about">HAI-Q brings together global perspectives on the future of Hyper/Super AI. Through public participation, AI-assisted analysis, and human review, it identifies key questions for voting and panel discussion.</p>

<hr>

## The HAI-Q Process

<div class="haiq-process">
  <section class="haiq-step">
    <div class="haiq-step-inner">
      <img class="haiq-step-image" src="{{ '/assets/images/haiq/step01_question_collection.webp' | relative_url }}" alt="A connected globe representing worldwide question collection" loading="lazy" width="502" height="411">
      <div class="haiq-step-body">
        <div class="haiq-step-heading">
          <span class="haiq-step-number">01</span>
          <h5><strong>Ask:</strong> Question Collection</h5>
        </div>
        <p>Questions about Hyper/Super AI were collected from participants worldwide.</p>
      </div>
    </div>
  </section>
  <section class="haiq-step">
    <div class="haiq-step-inner">
      <img class="haiq-step-image" src="{{ '/assets/images/haiq/step02_ai_analysis.webp' | relative_url }}" alt="AI-assisted analysis organizing and ranking related questions" loading="lazy" width="498" height="411">
      <div class="haiq-step-body">
        <div class="haiq-step-heading">
          <span class="haiq-step-number">02</span>
          <h5><strong>Organize:</strong> AI-Assisted Question Analysis and Ranking</h5>
        </div>
        <p>Use LLMs and human review to consolidate related questions and identify recurring themes.</p>
      </div>
    </div>
  </section>
  <section class="haiq-step">
    <div class="haiq-step-inner">
      <img class="haiq-step-image" src="{{ '/assets/images/haiq/step03_panel_discussion.webp' | relative_url }}" alt="A panel discussing top questions and future directions" loading="lazy" width="500" height="411">
      <div class="haiq-step-body">
        <div class="haiq-step-heading">
          <span class="haiq-step-number">03</span>
          <h5><strong>Explore:</strong> Question Discussion and Future Directions</h5>
        </div>
        <p>Vote on 30 candidate questions. The top 10 will be presented and discussed at the HAI-Q Panel.</p>
      </div>
    </div>
  </section>
</div>

<hr>

## Public Voting

<div class="haiq-voting">
  <div class="haiq-voting-copy">
    <h4>What Questions Matter Most for the Future of AI?</h4>
    <p>Review 30 candidate questions and select up to 10 that you consider most important and worth exploring.</p>
    <p class="haiq-deadline"><strong>Voting Deadline: November 10, 2026</strong></p>
    <p>Voting results will be used to rank the candidate questions. The top ten questions will be presented and discussed at the HAI-Q panel on November 12, 2026.</p>
    <a class="haiq-vote-button" href="https://forms.gle/d6FXhrLuiSFn5gAC9" target="_blank" rel="noopener noreferrer">Vote Now</a>
  </div>
  <div class="haiq-voting-qr">
    <a href="https://forms.gle/d6FXhrLuiSFn5gAC9" target="_blank" rel="noopener noreferrer" aria-label="Open the HAI-Q voting form">
      <img class="haiq-qr" src="{{ '/assets/images/haiq/haiq-voting-qr-final.png' | relative_url }}" alt="QR code for the HAI-Q public voting form">
    </a>
    <strong class="haiq-scan-label">Scan to Vote</strong>
  </div>
</div>

<hr>

## Panel Discussion

<div class="haiq-split haiq-split--reverse">
  <div class="haiq-copy">
    <p style="text-align: justify;">The HAI-Q panel will present the top ten questions emerging from the public voting process and examine the methods and rationale behind their selection.</p>
    <p style="text-align: justify;">The discussion will reflect on the challenges of large-scale question collection and AI-assisted analysis, and explore the implications of the selected questions for future Hyper/Super AI research.</p>
    <p><strong>Date:</strong> November 12, 2026<br><strong>Time:</strong> 10:50 AM &ndash; 12:20 PM AEDT</p>
  </div>
  <figure class="haiq-visual haiq-discussion-visual">
    <img src="{{ '/assets/images/haiq/haiq-future-panel-discussion.jpg' | relative_url }}" alt="Conceptual future AI research roundtable connected by a shared knowledge network" loading="lazy" width="1400" height="787">
  </figure>
</div>

<hr>

<div class="haiq-people-sections">
  <section class="haiq-people-section">
    <h2>Panel Chairs</h2>
    <div class="haiq-people">
      <p class="haiq-person"><strong>Jianhua Ma</strong>, Hosei University, Japan</p>
      <p class="haiq-person"><strong>Qun Jin</strong>, Waseda University, Japan</p>
    </div>
  </section>
  <section class="haiq-people-section">
    <h2>Panelists</h2>
    <div class="haiq-people">
      <p class="haiq-person"><strong>Nicolas Tsapatsoulis</strong>, Cyprus University of Technology, Cyprus</p>
      <p class="haiq-person"><strong>Hongji Yang</strong>, University of Leicester, United Kingdom</p>
    </div>
  </section>
</div>

<hr>

## Ethics and Contact

<p><strong>Ethics Approval:</strong><br><span class="haiq-ethics-line">This study was reviewed and approved by the Ethics Review Committee on Research with Human Subjects at Waseda University, Japan (Approval No. 2026-350).</span></p>

<div class="haiq-contact-grid">
  <p><strong>Contact:</strong> <a href="mailto:haiq.init@gmail.com"><u>haiq.init@gmail.com</u></a></p>
  <p><strong>Official HAI-Q Website:</strong> <a href="https://gai-hyperi.github.io/haiq/" target="_blank" rel="noopener noreferrer"><u>https://gai-hyperi.github.io/haiq/</u></a></p>
</div>

</div>

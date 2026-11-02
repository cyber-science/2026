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
  .haiq-hero-media { position: absolute; top: 0; right: 0; bottom: 0; z-index: 1; width: 54%; overflow: hidden; pointer-events: none; -webkit-mask-image: linear-gradient(90deg, transparent 0%, rgba(0,0,0,.2) 8%, #000 29%); mask-image: linear-gradient(90deg, transparent 0%, rgba(0,0,0,.2) 8%, #000 29%); }
  .haiq-hero-video { display: block; width: 100%; height: 100%; object-fit: cover; object-position: center center; }
  .haiq-logo { display: block; width: 210px; max-width: 48%; height: auto; margin-bottom: 1.1rem; }
  .haiq-label { margin: 0 0 .45rem; color: #9feeff; font-size: .88rem; font-weight: 700; letter-spacing: .1em; text-transform: uppercase; }
  .haiq-title { margin: 0 0 .7rem; color: #fff; font-size: clamp(2rem, 4vw, 3.15rem); line-height: 1.08; text-shadow: 0 2px 22px rgba(0,0,0,.2); }
  .haiq-subtitle { margin: 0; color: #e9f8fc; font-size: clamp(.9rem, 1.25vw, 1.02rem); line-height: 1.55; }
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
  @media (min-width: 1200px) {
    .haiq-subtitle { white-space: nowrap; }
    .haiq-ethics-line { white-space: nowrap; }
  }
  @media (max-width: 767.98px) {
    .haiq-hero { min-height: 650px; }
    .haiq-hero-copy { width: 100%; padding: 2rem 1.5rem 300px; }
    .haiq-hero-media { top: auto; width: 100%; height: 330px; opacity: .92; -webkit-mask-image: linear-gradient(180deg, transparent 0%, rgba(0,0,0,.72) 22%, #000 43%); mask-image: linear-gradient(180deg, transparent 0%, rgba(0,0,0,.72) 22%, #000 43%); }
    .haiq-hero-video { object-position: center 46%; }
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
    .haiq-hero-media { height: 310px; }
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
    .haiq-hero::after, .haiq-hero-copy { animation: none !important; }
    .haiq-step { opacity: 1; animation: none; }
    .haiq-step, .haiq-step-image, .haiq-visual img, .haiq-vote-button { transition: none; }
  }
</style>

<div class="haiq-page" markdown="1">

<div class="haiq-hero" role="img" aria-label="Future AI question space visualized as a luminous semantic knowledge network">
  <div class="haiq-hero-media" aria-hidden="true">
    <video class="haiq-hero-video" autoplay muted loop playsinline preload="metadata" poster="{{ '/assets/images/haiq/haiq-hero-right-poster.png' | relative_url }}">
      <source src="{{ '/assets/videos/haiq/HAIQ_right_background.mp4' | relative_url }}" type="video/mp4">
    </video>
  </div>
  <div class="haiq-hero-copy">
    <svg class="haiq-logo" viewBox="0 0 452 160" role="img" aria-labelledby="haiq-logo-title">
      <title id="haiq-logo-title">HAI-Q: Hyper/Super AI Questions Initiative logo</title>
      <defs>
        <filter id="haiq-white-logo" color-interpolation-filters="sRGB">
          <feColorMatrix values="0 0 0 0 1  0 0 0 0 1  0 0 0 0 1  -0.333 -0.333 -0.333 0 1"></feColorMatrix>
          <feComponentTransfer><feFuncA type="discrete" tableValues="0 0 1 1 1"></feFuncA></feComponentTransfer>
        </filter>
      </defs>
      <image href="{{ '/assets/images/haiq/haiq-logo-from-poster.png' | relative_url }}" width="452" height="160" filter="url(#haiq-white-logo)"></image>
    </svg>
    <p class="haiq-label">Panel-Q | HAI-Q</p>
    <h1 class="haiq-title">Questions of a Thousand Questions for Future AI</h1>
    <p class="haiq-subtitle">Methods, Rationale, and Reflections on Large-Scale Open Question Selection</p>
    <p class="haiq-session"><strong>November 12, 2026</strong> &nbsp;|&nbsp; 10:50 AM &ndash; 12:20 PM AEDT &nbsp;|&nbsp; Melbourne, Australia</p>
  </div>
</div>

<script>
(() => {
  const video = document.querySelector('.haiq-hero-video');
  if (!video) return;
  const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
  const syncPlayback = () => {
    if (reducedMotion.matches || document.hidden) video.pause();
    else video.play().catch(() => {});
  };
  reducedMotion.addEventListener('change', syncPlayback);
  document.addEventListener('visibilitychange', syncPlayback);
  syncPlayback();
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

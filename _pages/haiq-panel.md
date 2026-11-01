---
title: HAI-Q Panel
layout: sub
permalink: /haiq-panel/
---

<style>
  :root { --haiq-navy: #123a61; --haiq-blue: #176b9c; --haiq-cyan: #23b7cf; --haiq-pale: #eef9fc; --haiq-ink: #263f53; }
  .haiq-page { color: var(--haiq-ink); }
  .haiq-page hr { margin: 2.4rem 0; border: 0; border-top: 1px solid #d6e6ee; }
  .haiq-page > h2 { margin-bottom: 1.1rem; color: var(--haiq-navy); font-size: 1.65rem; }
  .haiq-hero { position: relative; min-height: 430px; margin: .35rem 0 2.5rem; overflow: hidden; border-radius: .35rem; background: #0e4778 url("{{ '/assets/images/haiq/haiq-ai-question-space.jpg' | relative_url }}") center/cover no-repeat; isolation: isolate; }
  .haiq-hero::before { content: ""; position: absolute; inset: 0; z-index: -1; background: linear-gradient(90deg, rgba(8,38,70,.94) 0%, rgba(9,55,94,.82) 43%, rgba(11,75,119,.18) 75%); }
  .haiq-hero::after { content: ""; position: absolute; left: 0; right: 0; bottom: 0; height: 3px; background: linear-gradient(90deg, var(--haiq-cyan), rgba(255,255,255,.8), transparent); animation: haiq-flow 5s ease-in-out infinite alternate; }
  .haiq-hero-copy { width: min(60%, 650px); padding: 2.8rem 2.5rem; color: #fff; animation: haiq-rise .8s ease-out both; }
  .haiq-logo { display: block; width: 190px; max-width: 46%; height: auto; margin-bottom: 1.1rem; padding: .35rem .45rem; border-radius: .2rem; background: rgba(255,255,255,.92); }
  .haiq-label { margin: 0 0 .45rem; color: #9feeff; font-size: .88rem; font-weight: 700; letter-spacing: .1em; text-transform: uppercase; }
  .haiq-title { margin: 0 0 .7rem; color: #fff; font-size: clamp(2rem, 4vw, 3.15rem); line-height: 1.08; text-shadow: 0 2px 22px rgba(0,0,0,.2); }
  .haiq-subtitle { max-width: 590px; margin: 0; color: #e9f8fc; font-size: 1.06rem; line-height: 1.55; }
  .haiq-session { margin: 1.25rem 0 0; padding-top: .85rem; border-top: 1px solid rgba(178,232,247,.55); color: #fff; font-size: .92rem; line-height: 1.5; }
  .haiq-split { display: grid; grid-template-columns: minmax(0, 1.05fr) minmax(300px, .95fr); align-items: center; gap: 2.2rem; }
  .haiq-split--reverse .haiq-visual { order: -1; }
  .haiq-copy p:last-child { margin-bottom: 0; }
  .haiq-visual { position: relative; margin: 0; overflow: hidden; border-radius: .3rem; background: var(--haiq-pale); box-shadow: 0 12px 30px rgba(25,84,122,.14); }
  .haiq-visual::after { content: ""; position: absolute; inset: 0; pointer-events: none; border: 1px solid rgba(83,188,215,.25); }
  .haiq-visual img { display: block; width: 100%; height: 100%; aspect-ratio: 2 / 1; object-fit: cover; transition: transform .6s ease; }
  .haiq-visual:hover img { transform: scale(1.02); }
  .haiq-process { position: relative; display: grid; grid-template-columns: repeat(3, 1fr); gap: 1.35rem; margin: 1.5rem 0 .35rem; }
  .haiq-process::before { content: ""; position: absolute; top: 1.7rem; left: 16%; right: 16%; height: 2px; background: linear-gradient(90deg, #89d7e6, var(--haiq-cyan), #89d7e6); background-size: 200% 100%; animation: haiq-flow 4s linear infinite; }
  .haiq-step { position: relative; z-index: 1; padding: 0 .55rem; text-align: center; }
  .haiq-step-heading { display: block; margin-bottom: .65rem; }
  .haiq-step-icon { display: inline-flex; align-items: center; justify-content: center; width: 3.5rem; height: 3.5rem; margin-bottom: .65rem; border: 4px solid #fff; border-radius: 50%; background: linear-gradient(135deg, #dff7fb, #fff); color: var(--haiq-blue); box-shadow: 0 0 0 1px #9edce8, 0 7px 18px rgba(31,130,166,.15); }
  .haiq-step-icon svg { width: 1.45rem; height: 1.45rem; fill: none; stroke: currentColor; stroke-width: 1.8; stroke-linecap: round; stroke-linejoin: round; }
  .haiq-step-number { display: block; margin-bottom: .12rem; color: #5e798a; font-size: .72rem; font-weight: 700; letter-spacing: .08em; text-transform: uppercase; }
  .haiq-step h5 { margin: 0; color: var(--haiq-blue); font-size: 1rem; }
  .haiq-step p { margin: 0; font-size: .9rem; line-height: 1.5; }
  .haiq-voting { display: grid; grid-template-columns: minmax(0, 1fr) 210px; align-items: center; gap: 2.2rem; margin: 1rem 0 1.6rem; padding: 2rem; border: 1px solid #b9e2ec; border-left: 5px solid var(--haiq-cyan); border-radius: .3rem; background: radial-gradient(circle at 88% 18%, rgba(76,202,224,.18), transparent 30%), linear-gradient(135deg, #f7fcfe, #eaf7fb); box-shadow: 0 12px 28px rgba(24,92,130,.1); }
  .haiq-voting-copy h4 { margin-top: 0; color: var(--haiq-navy); font-size: 1.3rem; }
  .haiq-voting-copy p { margin: 0 0 .75rem; }
  .haiq-deadline { display: inline-block; margin: .15rem 0 .9rem !important; padding: .48rem .75rem; border-left: 3px solid var(--haiq-cyan); background: #fff; color: var(--haiq-navy); }
  .haiq-vote-button { display: inline-block; margin: .2rem 0 0; padding: .72rem 1.45rem; border-radius: 2rem; background: linear-gradient(100deg, var(--haiq-blue), #139bb8); box-shadow: 0 7px 16px rgba(16,112,151,.22); color: #fff !important; font-weight: 700; text-decoration: none !important; transition: transform .2s ease, box-shadow .2s ease; }
  .haiq-vote-button:hover, .haiq-vote-button:focus { transform: translateY(-2px); box-shadow: 0 10px 20px rgba(16,112,151,.3); }
  .haiq-voting-qr { text-align: center; }
  .haiq-qr { display: block; width: 185px; max-width: 100%; height: auto; margin: 0 auto .45rem; padding: .5rem; border-radius: .25rem; background: #fff; box-shadow: 0 8px 24px rgba(12,66,98,.15); }
  .haiq-scan-label { color: var(--haiq-blue); font-size: .9rem; }
  .haiq-video-section { margin: 1.6rem 0 .35rem; text-align: center; }
  .haiq-video-section h4 { margin-bottom: .8rem; color: var(--haiq-navy); }
  .haiq-video-frame { display: block; width: 100%; max-width: 820px; aspect-ratio: 16 / 9; height: auto; margin: auto; border: 1px solid #b9d6e3; border-radius: .3rem; background: #0d1f2d; box-shadow: 0 12px 28px rgba(20,72,103,.13); }
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
  @media (min-width: 1200px) {
    .haiq-ethics-line { white-space: nowrap; }
  }
  @media (max-width: 767.98px) {
    .haiq-hero { min-height: 390px; background-position: 62% center; }
    .haiq-hero-copy { width: 75%; padding: 2rem 1.5rem; }
    .haiq-split { grid-template-columns: 1fr; gap: 1.2rem; }
    .haiq-split--reverse .haiq-visual { order: 0; }
    .haiq-process { grid-template-columns: 1fr; gap: 1.2rem; }
    .haiq-process::before { top: 1.8rem; bottom: 1.8rem; left: 1.75rem; right: auto; width: 2px; height: auto; background: linear-gradient(#89d7e6, var(--haiq-cyan), #89d7e6); }
    .haiq-step { display: grid; grid-template-columns: 4rem 1fr; padding: 0; text-align: left; }
    .haiq-step-heading { display: contents; }
    .haiq-step-icon { grid-row: 1 / span 2; margin: 0; }
    .haiq-step-heading > div { align-self: end; }
    .haiq-step p { grid-column: 2; align-self: start; }
    .haiq-voting { grid-template-columns: 1fr 180px; padding: 1.4rem; }
  }
  @media (max-width: 575.98px) {
    .haiq-page hr { margin: 1.8rem 0; }
    .haiq-hero { min-height: 470px; background-position: 67% center; }
    .haiq-hero::before { background: linear-gradient(90deg, rgba(8,38,70,.95), rgba(9,55,94,.82) 68%, rgba(11,75,119,.28)); }
    .haiq-hero-copy { width: 100%; padding: 1.5rem 1.2rem; }
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
    .haiq-hero::after, .haiq-hero-copy, .haiq-process::before { animation: none; }
    .haiq-visual img, .haiq-vote-button { transition: none; }
  }
</style>

<div class="haiq-page" markdown="1">

<div class="haiq-hero" role="img" aria-label="Future AI question space visualized as a luminous semantic knowledge network">
  <div class="haiq-hero-copy">
    <img class="haiq-logo" src="{{ '/assets/images/haiq/haiq-logo-from-poster.png' | relative_url }}" alt="HAI-Q: Hyper/Super AI Questions Initiative logo">
    <p class="haiq-label">Panel-Q | HAI-Q</p>
    <h1 class="haiq-title">Questions of a Thousand Questions for Future AI</h1>
    <p class="haiq-subtitle">Methods, Rationale, and Reflections on Large-Scale Open Question Selection</p>
    <p class="haiq-session"><strong>November 12, 2026</strong> &nbsp;|&nbsp; 10:50 AM &ndash; 12:20 PM AEDT &nbsp;|&nbsp; Melbourne, Australia</p>
  </div>
</div>

<hr>

## About HAI-Q

<div class="haiq-split">
  <div class="haiq-copy">
    <p style="text-align: justify;">The Hyper/Super AI Questions Initiative (HAI-Q) is an open event of GAI-HyperI 2026 that brings together global perspectives on fundamental questions about the future of Hyper/Super AI. Building on earlier initiatives such as <a href="https://wi-consortium.org/blog/top10qi/" target="_blank" rel="noopener noreferrer">Top10Qi</a> and <a href="https://doi.org/10.1109/ACCESS.2015.2504123" target="_blank" rel="noopener noreferrer">Top10Cs</a>, HAI-Q combines public participation, AI-assisted analysis, and human review to identify questions that may shape future research and discussion.</p>
  </div>
  <figure class="haiq-visual">
    <img src="{{ '/assets/images/haiq/haiq-global-knowledge-network.jpg' | relative_url }}" alt="Abstract visualization of global questions connected through an AI knowledge network" loading="lazy" width="1400" height="700">
  </figure>
</div>

<hr>

## The HAI-Q Process

<div class="haiq-process">
  <section class="haiq-step">
    <div class="haiq-step-heading">
      <span class="haiq-step-icon" aria-hidden="true"><svg viewBox="0 0 24 24"><path d="M5 5h14v10H9l-4 4V5Z"></path><path d="M9 9h6M9 12h4"></path></svg></span>
      <div><span class="haiq-step-number">01</span><h5><strong>Ask:</strong> Question Collection</h5></div>
    </div>
    <p>Fundamental questions about Hyper/Super AI were collected from participants worldwide.</p>
  </section>
  <section class="haiq-step">
    <div class="haiq-step-heading">
      <span class="haiq-step-icon" aria-hidden="true"><svg viewBox="0 0 24 24"><circle cx="6" cy="6" r="2"></circle><circle cx="18" cy="6" r="2"></circle><circle cx="12" cy="18" r="2"></circle><path d="m8 7 3 9M16 7l-3 9M8 6h8"></path></svg></span>
      <div><span class="haiq-step-number">02</span><h5><strong>Organize:</strong> AI-Assisted Question Analysis</h5></div>
    </div>
    <p>AI-assisted methods and human review were used to identify semantic similarities, consolidate related questions, and organize recurring themes.</p>
  </section>
  <section class="haiq-step">
    <div class="haiq-step-heading">
      <span class="haiq-step-icon" aria-hidden="true"><svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="8"></circle><path d="m9 12 2 2 4-5"></path></svg></span>
      <div><span class="haiq-step-number">03</span><h5><strong>Explore:</strong> Public Voting and Panel Discussion</h5></div>
    </div>
    <p>Thirty candidate questions are open for public voting. The top ten will be presented and discussed at the HAI-Q panel.</p>
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

<div class="haiq-video-section">
  <h4>How to Vote</h4>
  <video class="haiq-video-frame" controls playsinline preload="metadata">
    <source src="{{ '/assets/videos/haiq/haiq-how-to-vote-nov10.mp4' | relative_url }}" type="video/mp4">
    Your browser does not support the HTML5 video element.
  </video>
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

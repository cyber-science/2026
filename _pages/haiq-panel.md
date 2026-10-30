---
title: HAI-Q Panel
layout: sub
permalink: /haiq-panel/
---

<style>
  .haiq-hero { display: flex; align-items: center; gap: 2rem; padding: .35rem 0 1.1rem; }
  .haiq-logo { width: 210px; max-width: 28%; height: auto; flex: 0 0 auto; }
  .haiq-hero-copy { flex: 1 1 auto; min-width: 0; }
  .haiq-label { margin: 0 0 .3rem; color: #176b9c; font-size: .95rem; font-weight: 700; letter-spacing: .04em; text-transform: uppercase; }
  .haiq-title { margin: 0 0 .35rem; color: #1b365d; font-size: 2rem; line-height: 1.2; }
  .haiq-subtitle { margin: 0; font-size: 1.05rem; line-height: 1.45; }
  .haiq-session { margin: .8rem 0 0; padding-top: .65rem; border-top: 1px solid #b7c8d8; color: #334f64; font-size: .95rem; line-height: 1.45; }
  .haiq-process { display: flex; align-items: stretch; margin: 1rem 0 .35rem; }
  .haiq-step { position: relative; flex: 1 1 0; padding: .2rem 1.8rem .2rem .9rem; border-left: 3px solid #78b8d8; }
  .haiq-step:last-child { padding-right: .3rem; }
  .haiq-step:not(:last-child)::after { content: ""; position: absolute; top: 1.45rem; right: .45rem; width: .7rem; height: .7rem; border-top: 2px solid #78b8d8; border-right: 2px solid #78b8d8; transform: rotate(45deg); }
  .haiq-step-heading { display: flex; align-items: center; gap: .55rem; margin-bottom: .45rem; }
  .haiq-step-icon { display: inline-flex; align-items: center; justify-content: center; width: 2.25rem; height: 2.25rem; flex: 0 0 2.25rem; border-radius: 50%; background: #e4f2f9; color: #176b9c; }
  .haiq-step-icon svg { width: 1.2rem; height: 1.2rem; fill: none; stroke: currentColor; stroke-width: 1.8; stroke-linecap: round; stroke-linejoin: round; }
  .haiq-step-number { display: block; color: #607887; font-size: .72rem; font-weight: 700; letter-spacing: .05em; text-transform: uppercase; }
  .haiq-step h5 { margin: 0; color: #155f89; font-size: 1rem; }
  .haiq-step p { margin: 0; font-size: .9rem; line-height: 1.45; }
  .haiq-voting { display: flex; align-items: center; gap: 2rem; margin: 1rem 0 .35rem; padding: 1.5rem 1.75rem; border-left: 4px solid #176b9c; background: #eef7fb; }
  .haiq-voting-copy { flex: 1 1 65%; }
  .haiq-voting-copy h4 { margin-top: 0; color: #1b365d; }
  .haiq-voting-copy p { margin: 0 0 .7rem; }
  .haiq-deadline { display: inline-block; margin: .15rem 0 .8rem !important; padding: .45rem .7rem; border-left: 3px solid #78b8d8; background: #fff; }
  .haiq-vote-button { display: inline-block; margin: .15rem 0 0; padding: .65rem 1.25rem; border-radius: .2rem; background: #176b9c; color: #fff !important; font-weight: 700; text-decoration: none !important; }
  .haiq-vote-button:hover, .haiq-vote-button:focus { background: #114f74; }
  .haiq-voting-qr { flex: 0 0 190px; text-align: center; }
  .haiq-qr { display: block; width: 165px; max-width: 100%; height: auto; margin: 0 auto .35rem; padding: .35rem; background: #fff; }
  .haiq-scan-label { color: #155f89; font-size: .88rem; }
  .haiq-chairs { margin: .15rem 0 .35rem; color: #334f64; }
  .haiq-contact-grid { display: flex; flex-wrap: wrap; gap: .7rem 2rem; margin-top: .8rem; }
  .haiq-contact-grid p { margin: 0; }
  .haiq-ethics-line { font-size: .92rem; }
  @media (min-width: 1200px) {
    .haiq-ethics-line { white-space: nowrap; }
  }
  @media (max-width: 575.98px) {
    .haiq-hero { display: block; padding-top: 0; text-align: center; }
    .haiq-logo { width: 180px; max-width: 65%; margin-bottom: .85rem; }
    .haiq-title { font-size: 1.55rem; }
    .haiq-label { font-size: .85rem; }
    .haiq-session { font-size: .9rem; }
    .haiq-process { display: block; }
    .haiq-step { padding: .25rem 0 1rem .85rem; border-left-width: 2px; }
    .haiq-step:last-child { padding: .25rem 0 .2rem .85rem; }
    .haiq-step:not(:last-child)::after { top: auto; right: auto; bottom: .25rem; left: -.28rem; width: .55rem; height: .55rem; transform: rotate(135deg); background: #fff; }
    .haiq-voting { display: block; padding: 1.15rem; }
    .haiq-voting-qr { margin: 1.2rem auto 0; }
    .haiq-qr { width: 150px; }
    .haiq-contact-grid { display: block; }
    .haiq-contact-grid p + p { margin-top: .7rem; }
  }
</style>

<div class="haiq-hero">
  <img class="haiq-logo" src="{{ '/assets/images/haiq/haiq-logo-from-poster.png' | relative_url }}" alt="HAI-Q: Hyper/Super AI Questions Initiative logo">
  <div class="haiq-hero-copy">
    <p class="haiq-label">Panel-Q | HAI-Q</p>
    <h1 class="haiq-title">Questions of a Thousand Questions for Future AI</h1>
    <p class="haiq-subtitle">Methods, Rationale, and Reflections on Large-Scale Open Question Selection</p>
    <p class="haiq-session"><strong>November 12, 2026</strong> &nbsp;|&nbsp; 10:50 AM &ndash; 12:20 PM AEDT &nbsp;|&nbsp; Melbourne, Australia</p>
  </div>
</div>

<hr>

## About HAI-Q

<p style="text-align: justify;">The Hyper/Super AI Questions Initiative (HAI-Q) is an open event of GAI-HyperI 2026 that invites the global community to identify fundamental, forward-looking questions about the future of Hyper/Super AI.</p>

<p style="text-align: justify;">Inspired by earlier initiatives such as Top10Qi and Top10Cs, HAI-Q explores how collective questioning, AI-assisted analysis, and public participation can help identify questions that may shape the next era of intelligence.</p>

<hr>

## Why HAI-Q?

<p style="text-align: justify;">Questions shape the evolution of science and technology. From &ldquo;Can machines think?&rdquo; to emerging questions about Hyper AI and Super AI, fundamental questions can open new directions for scientific inquiry.</p>

<p style="text-align: justify;">HAI-Q brings together perspectives from the global community to examine which questions deserve further exploration and how they can be organized, evaluated, and discussed.</p>

<hr>

## The HAI-Q Process

<div class="haiq-process">
  <section class="haiq-step">
    <div class="haiq-step-heading">
      <span class="haiq-step-icon" aria-hidden="true"><svg viewBox="0 0 24 24"><path d="M5 5h14v10H9l-4 4V5Z"></path><path d="M9 9h6M9 12h4"></path></svg></span>
      <div><span class="haiq-step-number">Stage 01</span><h5><strong>Ask</strong> &mdash; Question Collection</h5></div>
    </div>
    <p>Fundamental questions about Hyper/Super AI were collected through an open international call for questions.</p>
  </section>
  <section class="haiq-step">
    <div class="haiq-step-heading">
      <span class="haiq-step-icon" aria-hidden="true"><svg viewBox="0 0 24 24"><circle cx="6" cy="6" r="2"></circle><circle cx="18" cy="6" r="2"></circle><circle cx="12" cy="18" r="2"></circle><path d="m8 7 3 9M16 7l-3 9M8 6h8"></path></svg></span>
      <div><span class="haiq-step-number">Stage 02</span><h5><strong>Organize</strong> &mdash; AI-Assisted Question Analysis</h5></div>
    </div>
    <p>Submitted questions are analyzed using AI-assisted methods and human review to identify semantic similarities, consolidate related questions, and organize emerging themes.</p>
  </section>
  <section class="haiq-step">
    <div class="haiq-step-heading">
      <span class="haiq-step-icon" aria-hidden="true"><svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="8"></circle><path d="m9 12 2 2 4-5"></path></svg></span>
      <div><span class="haiq-step-number">Stage 03</span><h5><strong>Explore</strong> &mdash; Public Voting and Panel Discussion</h5></div>
    </div>
    <p>Thirty candidate questions are presented for public voting. Participants may select up to ten questions that they consider most important. The top ten questions will be presented and discussed at the HAI-Q panel.</p>
  </section>
</div>

<hr>

## Public Voting

<div class="haiq-voting">
  <div class="haiq-voting-copy">
    <h4>What Questions Matter Most for the Future of AI?</h4>
    <p>Review 30 candidate questions and select up to 10 that you consider most important and worth exploring.</p>
    <p class="haiq-deadline"><strong>Voting Deadline: November 10, 2026</strong></p>
    <p>The selected top ten questions will be presented and discussed at the HAI-Q panel on November 12, 2026.</p>
    <a class="haiq-vote-button" href="https://forms.gle/BUTBxczwCphUGTfq5" target="_blank" rel="noopener noreferrer">Vote for the Questions</a>
  </div>
  <div class="haiq-voting-qr">
    <a href="https://forms.gle/BUTBxczwCphUGTfq5" target="_blank" rel="noopener noreferrer" aria-label="Open the HAI-Q voting form">
      <img class="haiq-qr" src="{{ '/assets/images/haiq/haiq-voting-qr-from-poster.png' | relative_url }}" alt="QR code for the HAI-Q public voting form">
    </a>
    <strong class="haiq-scan-label">Scan to Vote</strong>
  </div>
</div>

<hr>

## Panel Discussion

<p style="text-align: justify;">The HAI-Q panel will present and discuss the top-ranked questions emerging from the initiative, together with the methods, rationale, and reflections involved in large-scale open question selection.</p>

<p style="text-align: justify;">The discussion will explore the significance of these questions and their implications for future research on Hyper/Super AI.</p>

<p><strong>Date:</strong> November 12, 2026<br><strong>Time:</strong> 10:50 AM &ndash; 12:20 PM AEDT</p>

<hr>

## Forum Chairs

<p class="haiq-chairs"><strong>To Be Announced</strong></p>

<hr>

## Ethics and Contact

<p><strong>Ethics Approval:</strong><br><span class="haiq-ethics-line">This study was reviewed and approved by the Ethics Review Committee on Research with Human Subjects at Waseda University, Japan (Approval No. 2026-350).</span></p>

<div class="haiq-contact-grid">
  <p><strong>Contact:</strong> <a href="mailto:haiq.init@gmail.com"><u>haiq.init@gmail.com</u></a></p>
  <p><strong>Official HAI-Q Website:</strong> <a href="https://gai-hyperi.github.io/haiq/" target="_blank" rel="noopener noreferrer"><u>https://gai-hyperi.github.io/haiq/</u></a></p>
</div>

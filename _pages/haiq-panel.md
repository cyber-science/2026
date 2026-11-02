---
title: HAI-Q Panel
layout: sub-haiq
permalink: /haiq-panel/
---

<style>
  .haiq-page {
    position: relative;
    left: 50%;
    width: 100vw;
    margin: 0 0 -3rem -50vw;
    overflow: hidden;
    padding-bottom: 3rem;
    background: #09284a;
  }
  .haiq-stage {
    position: relative;
    width: min(100%, 2560px);
    margin: 0 auto;
    overflow: hidden;
    aspect-ratio: 2560 / 1282;
    background: #0c3b68;
  }
  .haiq-stage-video {
    display: block;
    width: 100%;
    height: 100%;
    object-fit: contain;
    object-position: center;
  }
  .haiq-meta {
    position: relative;
    z-index: 2;
    width: min(100%, 1500px);
    margin: -42px auto 0;
    padding: 72px clamp(1.5rem, 4vw, 4rem) 2rem;
    color: #fff;
  }
  .haiq-meta::before {
    content: "";
    position: absolute;
    top: 0;
    right: calc(50% - 50vw);
    left: calc(50% - 50vw);
    z-index: -1;
    height: 100%;
    background: linear-gradient(180deg, rgba(9,40,74,0) 0, rgba(9,40,74,.9) 38px, #09284a 72px, #09284a 100%);
  }
  .haiq-people { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 3rem; }
  .haiq-people-group { min-width: 0; }
  .haiq-meta-label { display: block; margin-bottom: 15px; color: #70d9f5; font-size: 16px; font-weight: 600; line-height: 1.25; letter-spacing: .07em; text-transform: uppercase; }
  .haiq-meta-person { display: block; margin-top: 14px; line-height: 1.5; }
  .haiq-meta-person:first-of-type { margin-top: 0; }
  .haiq-person-name { color: #fff; font-size: 21px; font-weight: 600; }
  .haiq-person-affiliation { color: #c1d7e9; font-size: 18px; font-weight: 400; }
  @media (min-width: 1440px) {
    .haiq-meta { padding-top: 78px; padding-bottom: 38px; }
    .haiq-meta-label { margin-bottom: 16px; font-size: 18px; font-weight: 600; }
    .haiq-meta-person { margin-top: 15px; line-height: 1.5; }
    .haiq-person-name { font-size: 24px; font-weight: 600; }
    .haiq-person-affiliation { font-size: 20px; font-weight: 400; }
  }
  @media (max-width: 767.98px) {
    .haiq-meta { padding: 68px 1.4rem 2rem; }
    .haiq-people { grid-template-columns: 1fr; gap: 1.25rem; }
    .haiq-meta-label { font-size: 15px; }
    .haiq-person-name { font-size: 20px; }
    .haiq-person-affiliation { font-size: 17px; }
  }
  @media (max-width: 699.98px) {
    .haiq-page { display: grid; min-height: calc(100svh - 1px); place-items: start center; }
    .haiq-stage { width: 100%; margin-top: clamp(0px, 8vh, 72px); }
    .haiq-meta { width: 100%; }
  }
</style>

<div class="haiq-page">
  <section class="haiq-stage" aria-label="HAI-Q Panel: Questions of a Thousand Questions for Future Hyper/Super AI, November 12, 2026, Melbourne, Australia">
    <video class="haiq-stage-video" autoplay muted loop playsinline preload="metadata" poster="{{ '/assets/images/haiq/haiq-hero-full-poster.png' | relative_url }}">
      <source src="{{ '/assets/videos/haiq/haiq-hero-full.mp4' | relative_url }}" type="video/mp4">
    </video>
  </section>
  <section class="haiq-meta" aria-label="HAI-Q panel chairs and panelists">
    <div class="haiq-people">
      <div class="haiq-people-group">
        <span class="haiq-meta-label">Panel Chairs</span>
        <span class="haiq-meta-person"><strong class="haiq-person-name">Jianhua Ma</strong><span class="haiq-person-affiliation">, Hosei University, Japan</span></span>
        <span class="haiq-meta-person"><strong class="haiq-person-name">Qun Jin</strong><span class="haiq-person-affiliation">, Waseda University, Japan</span></span>
      </div>
      <div class="haiq-people-group">
        <span class="haiq-meta-label">Panelists</span>
        <span class="haiq-meta-person"><strong class="haiq-person-name">Hongji Yang</strong><span class="haiq-person-affiliation">, University of Leicester, United Kingdom</span></span>
        <span class="haiq-meta-person"><strong class="haiq-person-name">Nicolas Tsapatsoulis</strong><span class="haiq-person-affiliation">, Cyprus University of Tech., Cyprus</span></span>
      </div>
    </div>
  </section>
</div>

<script>
(() => {
  const video = document.querySelector('.haiq-stage-video');
  if (!video) return;
  const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
  let visible = true;

  const syncPlayback = () => {
    const paused = reducedMotion.matches || document.hidden || !visible;
    if (paused) video.pause();
    else video.play().catch(() => {});
  };

  new IntersectionObserver(entries => {
    visible = entries[0].isIntersecting;
    syncPlayback();
  }, { threshold: .05 }).observe(video);
  reducedMotion.addEventListener('change', syncPlayback);
  document.addEventListener('visibilitychange', syncPlayback);
  syncPlayback();
})();
</script>

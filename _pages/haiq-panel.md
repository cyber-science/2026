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
    aspect-ratio: 2 / 1;
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
    padding: 58px clamp(1.5rem, 4vw, 4rem) 2rem;
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
  .haiq-access { display: flex; align-items: center; gap: 1.5rem; }
  .haiq-access-copy { min-width: 0; }
  .haiq-access-links { display: flex; gap: 1.1rem; margin: 0; }
  .haiq-access-links a { color: #70d9f5 !important; font-size: 20px; font-weight: 600; text-decoration: underline; text-underline-offset: .2em; }
  .haiq-access-links a:hover, .haiq-access-links a:focus { color: #b8f3ff !important; }
  .haiq-people { display: grid; grid-template-columns: minmax(0, 3fr) minmax(0, 7fr); gap: clamp(2.5rem, 5vw, 5rem); margin-top: 20px; }
  .haiq-people-group { min-width: 0; }
  .haiq-person-list { display: grid; min-width: 0; gap: 14px; }
  .haiq-panelists-list { grid-template-columns: repeat(2, minmax(0, 1fr)); column-gap: clamp(1.5rem, 3vw, 3rem); }
  .haiq-meta-label { display: block; margin-bottom: 18px; color: #70d9f5; font-size: 19px; font-weight: 600; line-height: 1.25; letter-spacing: .07em; text-transform: uppercase; }
  .haiq-meta-person { display: block; min-width: 0; line-height: 1.5; }
  .haiq-person-name { color: #fff; font-size: 23px; font-weight: 600; }
  .haiq-person-affiliation { color: #c1d7e9; font-size: 18px; font-weight: 400; }
  @media (min-width: 1200px) {
    .haiq-meta-person { white-space: nowrap; }
  }
  @media (min-width: 1440px) {
    .haiq-meta { padding-top: 60px; padding-bottom: 38px; }
    .haiq-meta-label { margin-bottom: 22px; font-size: 22px; font-weight: 600; }
    .haiq-person-list { gap: 16px; }
    .haiq-meta-person { line-height: 1.5; }
    .haiq-person-name { font-size: 24px; font-weight: 600; }
    .haiq-person-affiliation { font-size: 19px; font-weight: 400; }
    .haiq-access-links a { font-size: 22px; }
  }
  @media (max-width: 767.98px) {
    .haiq-page { display: block; min-height: 0; padding-top: 10px; }
    .haiq-stage { width: 100%; height: auto; min-height: 0; margin-top: 0; }
    .haiq-meta { padding: 58px 1.4rem 2rem; }
    .haiq-access { align-items: flex-start; }
    .haiq-access-links a { font-size: 18px; }
    .haiq-people { grid-template-columns: 1fr; gap: 1.25rem; }
    .haiq-panelists-list { grid-template-columns: 1fr; }
    .haiq-meta-label { font-size: 17px; }
    .haiq-person-name { font-size: 22px; }
    .haiq-person-affiliation { font-size: 18px; }
  }
</style>

<div class="haiq-page">
  <section class="haiq-stage" aria-label="HAI-Q Panel: Questions of a Thousand Questions for Future Hyper/Super AI, November 12, 2026, Melbourne, Australia">
    <video class="haiq-stage-video" autoplay muted loop playsinline webkit-playsinline x5-playsinline x5-video-player-type="h5-page" x5-video-player-fullscreen="false" x-webkit-airplay="allow" preload="metadata" poster="{{ '/assets/images/haiq/haiq-hero-full-poster.png' | relative_url }}">
      <source src="{{ '/assets/videos/haiq/haiq-hero-full.mp4' | relative_url }}" type="video/mp4">
    </video>
  </section>
  <section class="haiq-meta" aria-label="HAI-Q panel chairs and panelists">
    <div class="haiq-access">
      <div class="haiq-access-copy">
        <p class="haiq-access-links"><a href="https://gai-hyperi.github.io/haiq/" target="_blank" rel="noopener noreferrer">HAI-Q Website</a><a href="https://list-waseda-jp.zoom.us/j/96196767132?pwd=9ekrS16hnNOUaucHpvQK6XQMwjr1cn.1" target="_blank" rel="noopener noreferrer">Panel Zoom</a></p>
      </div>
    </div>
    <div class="haiq-people">
      <div class="haiq-people-group">
        <span class="haiq-meta-label">Panel Chairs</span>
        <div class="haiq-person-list">
          <span class="haiq-meta-person"><strong class="haiq-person-name">Jianhua Ma</strong><span class="haiq-person-affiliation">, Hosei Univ., Japan</span></span>
          <span class="haiq-meta-person"><strong class="haiq-person-name">Qun Jin</strong><span class="haiq-person-affiliation">, Waseda Univ., Japan</span></span>
        </div>
      </div>
      <div class="haiq-people-group">
        <span class="haiq-meta-label">Panelists</span>
        <div class="haiq-person-list haiq-panelists-list">
          <span class="haiq-meta-person"><strong class="haiq-person-name">Stephen S. Yau</strong><span class="haiq-person-affiliation">, ASU, USA</span></span>
          <span class="haiq-meta-person"><strong class="haiq-person-name">Hongji Yang</strong><span class="haiq-person-affiliation">, Univ. of Leicester, UK</span></span>
          <span class="haiq-meta-person"><strong class="haiq-person-name">Nicolas Tsapatsoulis</strong><span class="haiq-person-affiliation">, CUT, Cyprus</span></span>
        </div>
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

  video.muted = true;
  video.defaultMuted = true;
  video.setAttribute('muted', '');

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
  document.addEventListener('WeixinJSBridgeReady', syncPlayback, false);
  document.addEventListener('DOMContentLoaded', syncPlayback, { once: true });
  document.addEventListener('touchstart', syncPlayback, { once: true, passive: true });
  syncPlayback();
})();
</script>

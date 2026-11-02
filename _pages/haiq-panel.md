---
title: HAI-Q Panel
layout: sub
permalink: /haiq-panel/
---

<style>
  .haiq-page {
    position: relative;
    left: 50%;
    width: 100vw;
    margin: 0 0 -3rem -50vw;
    overflow: hidden;
    background: #0c3b68;
  }
  .haiq-stage {
    position: relative;
    width: min(100%, 1774px);
    margin: 0 auto;
    overflow: hidden;
    aspect-ratio: 1774 / 888;
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
    display: grid;
    grid-template-columns: 1.05fr 1fr 1.25fr .85fr;
    width: min(100%, 1774px);
    margin: 0 auto;
    padding: 1.65rem clamp(1.35rem, 3vw, 3.25rem) 1.75rem;
    background: linear-gradient(100deg, #0b3158, #124f7b 58%, #176792);
    color: #ecfaff;
    box-shadow: inset 0 1px rgba(113,224,244,.32);
  }
  .haiq-meta-block { min-width: 0; padding: 0 1.5rem; border-left: 1px solid rgba(126,224,242,.3); }
  .haiq-meta-block:first-child { padding-left: 0; border-left: 0; }
  .haiq-meta-label { display: block; margin-bottom: .55rem; color: #9cecf7; font-size: 16px; font-weight: 600; line-height: 1.25; letter-spacing: .045em; text-transform: uppercase; }
  .haiq-meta h2 { margin: 0; color: #fff; font-size: 22px; font-weight: 600; line-height: 1.3; }
  .haiq-meta h3 { margin: 0; color: #fff; font-size: 19px; font-weight: 600; line-height: 1.35; }
  .haiq-meta p { margin: .42rem 0 0; color: #edfaff; font-size: 17px; line-height: 1.5; }
  .haiq-meta-person { display: block; margin-top: .34rem; }
  .haiq-meta-person:first-child { margin-top: 0; }
  .haiq-person-name { color: #fff; font-size: 19px; font-weight: 600; }
  .haiq-person-affiliation { color: #e8f7fb; font-size: 17px; font-weight: 400; }
  .haiq-vote-link { display: inline-block; margin-top: .75rem; padding: .7rem 1.4rem; border-radius: 2rem; background: #2bbbd2; box-shadow: 0 6px 16px rgba(6,38,65,.22); color: #fff !important; font-size: 18px; font-weight: 700; line-height: 1.2; text-decoration: none !important; transition: background .2s ease, transform .2s ease, box-shadow .2s ease; }
  .haiq-vote-link:hover, .haiq-vote-link:focus { background: #35cbe1; transform: translateY(-1px); }
  @media (max-width: 1499.98px) {
    .haiq-meta { grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 1.5rem 0; }
    .haiq-meta-block:nth-child(3) { padding-left: 0; border-left: 0; }
  }
  @media (max-width: 699.98px) {
    .haiq-page { display: grid; min-height: calc(100svh - 1px); place-items: start center; }
    .haiq-stage { width: 100%; margin-top: clamp(0px, 8vh, 72px); }
    .haiq-meta { grid-template-columns: 1fr; gap: 0; padding: 1.5rem 1.25rem 1.75rem; }
    .haiq-meta-block { padding: 1.15rem 0 0; border-top: 1px solid rgba(126,224,242,.24); border-left: 0; }
    .haiq-meta-block:first-child { padding-top: 0; border-top: 0; }
    .haiq-meta-block:nth-child(3) { padding-left: 0; }
  }
</style>

<div class="haiq-page">
  <section class="haiq-stage" aria-label="HAI-Q Panel: Questions of a Thousand Questions for Future Hyper/Super AI, November 12, 2026, Melbourne, Australia">
    <video class="haiq-stage-video" autoplay muted loop playsinline preload="metadata" poster="{{ '/assets/images/haiq/haiq-hero-full-poster.png' | relative_url }}">
      <source src="{{ '/assets/videos/haiq/haiq-hero-full.mp4' | relative_url }}" type="video/mp4">
    </video>
  </section>
  <section class="haiq-meta" aria-label="HAI-Q panel details and voting information">
    <div class="haiq-meta-block">
      <span class="haiq-meta-label">Conference Session</span>
      <h2>CyberSciTech 2026 &middot; Panel Q</h2>
      <p>RMIT University, Building 80</p>
    </div>
    <div class="haiq-meta-block">
      <span class="haiq-meta-label">Panel Chairs</span>
      <p><span class="haiq-meta-person"><strong class="haiq-person-name">Jianhua Ma</strong><span class="haiq-person-affiliation">, Hosei University, Japan</span></span><span class="haiq-meta-person"><strong class="haiq-person-name">Qun Jin</strong><span class="haiq-person-affiliation">, Waseda University, Japan</span></span></p>
    </div>
    <div class="haiq-meta-block">
      <span class="haiq-meta-label">Panelists</span>
      <p><span class="haiq-meta-person"><strong class="haiq-person-name">Nicolas Tsapatsoulis</strong><span class="haiq-person-affiliation">, Cyprus University of Technology, Cyprus</span></span><span class="haiq-meta-person"><strong class="haiq-person-name">Hongji Yang</strong><span class="haiq-person-affiliation">, University of Leicester, United Kingdom</span></span></p>
    </div>
    <div class="haiq-meta-block">
      <span class="haiq-meta-label">Public Voting</span>
      <h3>Deadline: November 10, 2026</h3>
      <a class="haiq-vote-link" href="https://forms.gle/d6FXhrLuiSFn5gAC9" target="_blank" rel="noopener noreferrer">Vote Now</a>
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

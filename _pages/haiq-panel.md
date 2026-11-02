---
title: HAI-Q Panel
layout: sub
permalink: /haiq-panel/
---

<style>
  :root { --haiq-deep: #0b3158; --haiq-mid: #145986; --haiq-cyan: #45dcf4; }
  .haiq-page { position: relative; left: 50%; width: 100vw; margin: 0 0 -3rem -50vw; overflow: hidden; background: var(--haiq-deep); }
  .haiq-stage { position: relative; width: 100%; aspect-ratio: 16 / 9; min-height: 620px; overflow: hidden; background: radial-gradient(circle at 72% 42%, rgba(53,204,239,.2), transparent 28%), linear-gradient(120deg, #123b63, #18507d 52%, #2570a3); isolation: isolate; }
  .haiq-stage::after { content: ""; position: absolute; inset: 0; z-index: 3; pointer-events: none; background: linear-gradient(90deg, rgba(15,52,87,1) 0%, rgba(18,59,99,.99) 37%, rgba(18,66,105,.92) 45%, rgba(18,73,112,.55) 54%, transparent 66%); }
  .haiq-stage-video { position: absolute; inset: 0; z-index: 1; width: 100%; height: 100%; object-fit: cover; object-position: 54% center; }
  .haiq-particle-layer, .haiq-native-fx { position: absolute; inset: 0; z-index: 4; width: 100%; height: 100%; pointer-events: none; }
  .haiq-native-fx { overflow: visible; filter: drop-shadow(0 0 7px rgba(63,218,249,.45)); }
  .haiq-question-tile rect { fill: url(#haiq-card-fill); stroke: rgba(133,238,255,.9); stroke-width: 2; }
  .haiq-question-tile text { fill: #effdff; font: 700 30px Arial, sans-serif; text-anchor: middle; }
  .haiq-orbit { fill: none; stroke: url(#haiq-orbit-stroke); stroke-width: 3; stroke-linecap: round; stroke-dasharray: 18 15; transform-origin: 975px 414px; animation: haiq-orbit-spin 12.5s linear infinite; }
  .haiq-orbit--two { animation-direction: reverse; animation-duration: 8.5s; opacity: .72; }
  .haiq-core-pulse { fill: none; stroke: #74eafa; stroke-width: 3; opacity: .2; transform-origin: 975px 414px; animation: haiq-core-pulse 3.2s ease-in-out infinite; }
  .haiq-funnel-stream { fill: none; stroke: rgba(120,236,255,.85); stroke-width: 3; stroke-linecap: round; stroke-dasharray: 4 16; animation: haiq-stream 2.6s linear infinite; }
  .haiq-bottom-glow { fill: #eafcff; opacity: .15; animation: haiq-card-glow 12.5s ease-in-out infinite; }
  .haiq-bottom-glow:nth-of-type(2) { animation-delay: 1s; }
  .haiq-bottom-glow:nth-of-type(3) { animation-delay: 2s; }
  .haiq-bottom-glow:nth-of-type(4) { animation-delay: 3s; }
  .haiq-top-scan { fill: url(#haiq-scan-gradient); opacity: 0; animation: haiq-top-scan 4.2s ease-in-out infinite; }
  .haiq-copy { position: absolute; top: 17%; left: max(4.5vw, calc((100vw - 1500px) / 2)); z-index: 6; width: min(47vw, 760px); color: #fff; text-shadow: 0 2px 16px rgba(0,21,48,.42); }
  .haiq-logo { display: block; width: clamp(210px, 18vw, 300px); height: auto; margin: 0 0 1.1rem; }
  .haiq-title { margin: 0; color: #fff; font-size: clamp(2.8rem, 4.25vw, 5rem); font-weight: 700; line-height: 1.06; letter-spacing: -.025em; }
  .haiq-title span { display: block; }
  .haiq-title em { color: #50e0f1; font-style: normal; }
  .haiq-subtitle { max-width: 760px; margin: 1rem 0 0; color: #eefbff; font-size: clamp(.88rem, 1.25vw, 1.25rem); line-height: 1.45; }
  .haiq-session { margin: .85rem 0 0; color: #fff; font-size: clamp(.8rem, 1.12vw, 1.08rem); font-weight: 600; line-height: 1.45; }
  @keyframes haiq-orbit-spin { to { transform: rotate(360deg); } }
  @keyframes haiq-core-pulse { 0%,100% { opacity: .18; transform: scale(.86); } 50% { opacity: .75; transform: scale(1.12); } }
  @keyframes haiq-stream { to { stroke-dashoffset: -80; } }
  @keyframes haiq-card-glow { 0%,40%,100% { opacity: .12; } 48%,66% { opacity: .9; } 76% { opacity: .26; } }
  @keyframes haiq-top-scan { 0%,22%,100% { opacity: 0; transform: translateX(-190px); } 36% { opacity: .85; } 65% { opacity: .2; transform: translateX(260px); } }
  @media (max-width: 991.98px) {
    .haiq-stage { min-height: 100svh; aspect-ratio: auto; padding-top: 50vw; }
    .haiq-stage-video { bottom: auto; height: auto; aspect-ratio: 2 / 1; object-fit: contain; object-position: center top; }
    .haiq-stage::after { background: linear-gradient(180deg, rgba(13,49,84,.18) 0, rgba(13,49,84,.38) 35vw, rgba(13,49,84,.98) 51vw, #123b63 70vw); }
    .haiq-particle-layer, .haiq-native-fx { height: 50vw; }
    .haiq-copy { top: 48vw; left: 7vw; width: 86vw; padding-bottom: 3rem; }
    .haiq-logo { width: clamp(170px, 34vw, 245px); margin-bottom: .8rem; }
    .haiq-title { font-size: clamp(2.35rem, 7.7vw, 4.25rem); }
    .haiq-subtitle { max-width: 680px; font-size: clamp(.92rem, 2.45vw, 1.15rem); }
    .haiq-session { max-width: 680px; font-size: clamp(.83rem, 2.2vw, 1rem); }
  }
  @media (max-width: 575.98px) {
    .haiq-stage { min-height: 760px; padding-top: 55vw; }
    .haiq-stage::after { background: linear-gradient(180deg, rgba(13,49,84,.08) 0, rgba(13,49,84,.3) 35vw, rgba(13,49,84,.98) 54vw, #123b63 74vw); }
    .haiq-particle-layer, .haiq-native-fx { display: none; }
    .haiq-copy { top: 54vw; left: 6vw; width: 88vw; }
    .haiq-logo { width: 165px; }
    .haiq-title { font-size: clamp(2rem, 10.3vw, 2.65rem); line-height: 1.07; }
    .haiq-subtitle { margin-top: .8rem; font-size: .92rem; }
    .haiq-session { margin-top: .7rem; font-size: .84rem; }
  }
  @media (prefers-reduced-motion: reduce) {
    .haiq-native-fx * { animation: none !important; }
  }
</style>

<div class="haiq-page">
  <section class="haiq-stage" aria-labelledby="haiq-title">
    <video class="haiq-stage-video" autoplay muted loop playsinline preload="metadata" poster="{{ '/assets/images/haiq/haiq-hero-full-poster.png' | relative_url }}" aria-hidden="true">
      <source src="{{ '/assets/videos/haiq/haiq-hero-full.mp4' | relative_url }}" type="video/mp4">
    </video>
    <canvas class="haiq-particle-layer" aria-hidden="true"></canvas>
    <svg class="haiq-native-fx" viewBox="0 0 1774 998" preserveAspectRatio="xMidYMid slice" aria-hidden="true">
      <defs>
        <linearGradient id="haiq-card-fill" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#42d9f3" stop-opacity=".62"/><stop offset="1" stop-color="#174f9d" stop-opacity=".28"/></linearGradient>
        <linearGradient id="haiq-orbit-stroke"><stop stop-color="#64ecff"/><stop offset=".5" stop-color="#6f7fff"/><stop offset="1" stop-color="#f0c85d"/></linearGradient>
        <linearGradient id="haiq-scan-gradient"><stop stop-color="#fff" stop-opacity="0"/><stop offset=".5" stop-color="#fff" stop-opacity=".85"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient>
        <filter id="haiq-soft-glow"><feGaussianBlur stdDeviation="5" result="blur"/><feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
        <g id="haiq-card" class="haiq-question-tile"><rect x="-27" y="-20" width="54" height="40" rx="6"/><text y="11">?</text></g>
      </defs>
      <g opacity=".82">
        <g><use href="#haiq-card"/><animateMotion dur="12.5s" begin="-1s" repeatCount="indefinite" path="M520 105 C720 80 810 240 960 390"/></g>
        <g transform="scale(.75)"><use href="#haiq-card"/><animateMotion dur="12.5s" begin="-3.2s" repeatCount="indefinite" path="M650 62 C790 130 860 250 968 394"/></g>
        <g transform="scale(1.18)"><use href="#haiq-card"/><animateMotion dur="12.5s" begin="-5.4s" repeatCount="indefinite" path="M575 215 C745 175 835 280 968 397"/></g>
        <g transform="scale(.62)"><use href="#haiq-card"/><animateMotion dur="12.5s" begin="-7.6s" repeatCount="indefinite" path="M755 108 C835 180 895 300 972 402"/></g>
        <g transform="scale(.9)"><use href="#haiq-card"/><animateMotion dur="12.5s" begin="-9.8s" repeatCount="indefinite" path="M680 280 C810 265 880 335 970 405"/></g>
      </g>
      <ellipse class="haiq-orbit" cx="975" cy="414" rx="236" ry="92"/>
      <ellipse class="haiq-orbit haiq-orbit--two" cx="975" cy="414" rx="185" ry="68"/>
      <circle class="haiq-core-pulse" cx="975" cy="414" r="72" filter="url(#haiq-soft-glow)"/>
      <path class="haiq-funnel-stream" d="M974 440 C972 522 950 575 932 657"/>
      <path class="haiq-funnel-stream" d="M1000 444 C990 535 974 590 958 665" style="animation-delay:-1.1s"/>
      <g filter="url(#haiq-soft-glow)">
        <rect class="haiq-bottom-glow" x="812" y="650" width="72" height="88" rx="8"/>
        <rect class="haiq-bottom-glow" x="895" y="630" width="78" height="102" rx="8"/>
        <rect class="haiq-bottom-glow" x="985" y="637" width="76" height="96" rx="8"/>
        <rect class="haiq-bottom-glow" x="1073" y="656" width="68" height="82" rx="8"/>
      </g>
      <rect class="haiq-top-scan" x="1210" y="510" width="68" height="145" rx="18" transform="skewX(-12)"/>
    </svg>
    <div class="haiq-copy">
      <img class="haiq-logo" src="{{ '/assets/images/haiq/haiq-logo-transparent.png' | relative_url }}" width="452" height="160" alt="HAI-Q: Hyper/Super AI Questions Initiative">
      <h1 class="haiq-title" id="haiq-title"><span>Questions of a</span><span>Thousand Questions</span><span>for Future <em>Hyper/Super AI</em></span></h1>
      <p class="haiq-subtitle">Methods, Rationale, and Reflections on Large-Scale Open Question Selection</p>
      <p class="haiq-session">November 12, 2026 &nbsp;|&nbsp; 10:50 AM &ndash; 12:20 PM AEDT &nbsp;|&nbsp; Melbourne, Australia</p>
    </div>
  </section>
</div>

<script>
(() => {
  const stage = document.querySelector('.haiq-stage');
  const video = stage && stage.querySelector('.haiq-stage-video');
  const canvas = stage && stage.querySelector('.haiq-particle-layer');
  const svg = stage && stage.querySelector('.haiq-native-fx');
  if (!stage || !video || !canvas) return;
  const context = canvas.getContext('2d', { alpha: true });
  const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
  let width = 0, height = 0, visible = true, frame = 0, previous = 0;
  const particles = Array.from({ length: 54 }, (_, index) => ({ t: (index / 54 + Math.random() * .08) % 1, speed: .00007 + Math.random() * .000018, size: .7 + Math.random() * 1.7, offset: (Math.random() - .5) * .11 }));
  const resize = () => { const rect = canvas.getBoundingClientRect(); const ratio = Math.min(window.devicePixelRatio || 1, 1.5); width = Math.max(1, rect.width); height = Math.max(1, rect.height); canvas.width = Math.round(width * ratio); canvas.height = Math.round(height * ratio); context.setTransform(ratio, 0, 0, ratio, 0, 0); };
  const curve = (a, b, c, t) => (1 - t) * (1 - t) * a + 2 * (1 - t) * t * b + t * t * c;
  const locate = particle => { if (particle.t < .64) { const t = particle.t / .64; return { x: curve(width * (.38 + particle.offset), width * .54, width * .57, t), y: curve(height * .12, height * .18, height * .42, t) }; } const t = (particle.t - .64) / .36; return { x: curve(width * .57, width * .56, width * .54, t), y: curve(height * .42, height * .58, height * .72, t) }; };
  const render = time => { context.clearRect(0, 0, width, height); const delta = Math.min(40, time - previous || 16); previous = time; particles.forEach((particle, index) => { if (!reducedMotion.matches) particle.t = (particle.t + particle.speed * delta) % 1; const point = locate(particle); const alpha = .28 + .42 * Math.sin(Math.PI * particle.t); context.beginPath(); context.fillStyle = `rgba(126, 237, 255, ${alpha})`; context.shadowColor = index % 7 ? '#38d8f4' : '#e8c766'; context.shadowBlur = 8; context.arc(point.x, point.y, particle.size, 0, Math.PI * 2); context.fill(); }); context.shadowBlur = 0; };
  const animate = time => { render(time); if (visible && !document.hidden && !reducedMotion.matches) frame = requestAnimationFrame(animate); };
  const sync = () => { const paused = reducedMotion.matches || document.hidden || !visible; cancelAnimationFrame(frame); if (paused) { video.pause(); if (svg && svg.pauseAnimations) svg.pauseAnimations(); render(performance.now()); } else { video.playbackRate = .8; video.play().catch(() => {}); if (svg && svg.unpauseAnimations) svg.unpauseAnimations(); frame = requestAnimationFrame(animate); } };
  new ResizeObserver(() => { resize(); render(performance.now()); }).observe(canvas);
  new IntersectionObserver(entries => { visible = entries[0].isIntersecting; sync(); }, { threshold: .05 }).observe(stage);
  reducedMotion.addEventListener('change', sync);
  document.addEventListener('visibilitychange', sync);
  resize();
  sync();
})();
</script>

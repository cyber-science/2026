---
title: Program Outline
layout: sub
permalink: /outline/
---

<style>
/* --- Draft Program at a Glance (scoped under .draft-program) --- */
.draft-program {
  --dp-keynote:   #dbe9f9;  --dp-keynote-b: #2c6cb0;
  --dp-panel:     #e8def5;  --dp-panel-b:   #7a4fb5;
  --dp-session:   #dff0e2;  --dp-session-b: #2e8b57;
  --dp-workshop:  #fdf3d7;  --dp-workshop-b:#c9931a;
  --dp-break:     #f2f2f2;  --dp-break-b:   #9a9a9a;
  --dp-social:    #fbe3e0;  --dp-social-b:  #c94f3d;
  --dp-ceremony:  #e0f0f5;  --dp-ceremony-b:#2a8ba8;
  --dp-ink: #1d2733;
  color: var(--dp-ink);
  font-family: "Segoe UI", "Helvetica Neue", Arial, sans-serif;
  max-width: 1280px;
  margin: 0 auto;
}
.draft-program * { box-sizing: border-box; }

.draft-program .dp-header { text-align: center; margin-bottom: 6px; }
.draft-program .dp-header h1 { font-size: 1.5rem; margin: 0 0 4px; color: #16324f; }
.draft-program .dp-header h2 { font-size: 1.05rem; margin: 0 0 2px; font-weight: 600; color: #2c6cb0; }
.draft-program .dp-header p  { margin: 2px 0; font-size: .92rem; color: #4a5866; }
.draft-program .draft-badge {
  display: inline-block; margin-top: 6px; padding: 2px 12px;
  border: 1px solid #c94f3d; color: #c94f3d; border-radius: 12px;
  font-size: .78rem; font-weight: 600; letter-spacing: .04em;
}

.draft-program .grid {
  display: grid; grid-template-columns: repeat(5, 1fr);
  gap: 10px; margin-top: 18px; align-items: start;
}
.draft-program .day { background: #fff; border: 1px solid #dde3e9; border-radius: 8px; overflow: hidden; }
.draft-program .day-head { background: #16324f; color: #fff; text-align: center; padding: 8px 4px; }
.draft-program .day-head .dnum { font-size: .75rem; letter-spacing: .08em; text-transform: uppercase; opacity: .8; }
.draft-program .day-head .dname { font-size: .95rem; font-weight: 700; }
.draft-program .day-head.main { background: #2c6cb0; }

.draft-program .slot {
  margin: 6px; padding: 6px 8px; border-radius: 5px;
  border-left: 4px solid var(--dp-break-b); background: var(--dp-break);
  font-size: .8rem; line-height: 1.3;
}
.draft-program .slot .time { font-weight: 700; font-size: .74rem; color: #333; display: block; }
.draft-program .slot .what { font-weight: 600; }
.draft-program .slot .note { display: block; font-size: .72rem; color: #55606b; font-weight: 400; }
.draft-program .keynote  { background: var(--dp-keynote);  border-color: var(--dp-keynote-b); }
.draft-program .panel    { background: var(--dp-panel);    border-color: var(--dp-panel-b); }
.draft-program .session  { background: var(--dp-session);  border-color: var(--dp-session-b); }
.draft-program .workshop { background: var(--dp-workshop); border-color: var(--dp-workshop-b); }
.draft-program .social   { background: var(--dp-social);   border-color: var(--dp-social-b); }
.draft-program .ceremony { background: var(--dp-ceremony); border-color: var(--dp-ceremony-b); }

.draft-program .legend {
  display: flex; flex-wrap: wrap; gap: 10px; justify-content: center;
  margin-top: 18px; font-size: .78rem;
}
.draft-program .legend span { display: inline-flex; align-items: center; gap: 5px; }
.draft-program .chip { width: 14px; height: 14px; border-radius: 3px; display: inline-block; border-left: 4px solid; }
.draft-program .dp-footer { margin-top: 16px; text-align: center; font-size: .75rem; color: #6a7684; }

@media (max-width: 900px) { .draft-program .grid { grid-template-columns: 1fr; } }
</style>

<div class="draft-program">
  <div class="dp-header">
    <h1>2026 IEEE CyberSciTech / DASC / PICom / CBDCom Co-located Conferences</h1>
    <h2>(Hybrid: On-site/Online)</h2>
    <p>9–13 November 2026 · Melbourne, Australia · All times AEDT (UTC+11)</p>
    <p><strong>Program at a Glance</strong></p>
    <span class="draft-badge">DRAFT — subject to change</span>
  </div>

  <div class="grid">

    <!-- DAY 1 -->
    <div class="day">
      <div class="day-head">
        <div class="dnum">Day 1</div>
        <div class="dname">Mon, 9 Nov</div>
      </div>
      <div class="slot"><span class="time">08:00 –</span><span class="what">Registration opens</span></div>
      <div class="slot workshop"><span class="time">09:00 – 10:30</span><span class="what">Workshop &amp; Tutorial</span></div>
      <div class="slot"><span class="time">10:30 – 11:00</span><span class="what">Morning Tea</span></div>
      <div class="slot workshop"><span class="time">11:00 – 12:30</span><span class="what">Workshop &amp; Tutorial</span></div>
      <div class="slot"><span class="time">12:30 – 13:30</span><span class="what">Lunch</span></div>
      <div class="slot workshop"><span class="time">13:30 – 15:00</span><span class="what">Workshop &amp; Tutorial</span></div>
      <div class="slot"><span class="time">15:00 – 15:30</span><span class="what">Afternoon Tea</span></div>
      <div class="slot workshop"><span class="time">15:30 – 17:00</span><span class="what">Birds-of-a-Feather (BoF)</span></div>
      <div class="slot social"><span class="time">18:00 – 20:00</span><span class="what">Welcome Reception</span></div>
    </div>

    <!-- DAY 2 -->
    <div class="day">
      <div class="day-head main">
        <div class="dnum">Day 2</div>
        <div class="dname">Tue, 10 Nov</div>
      </div>
      <div class="slot"><span class="time">08:30 –</span><span class="what">Registration</span></div>
      <div class="slot ceremony"><span class="time">09:00 – 09:40</span><span class="what">Opening Ceremony</span></div>
      <div class="slot keynote"><span class="time">09:40 – 10:20</span><span class="what">Keynote</span></div>
      <div class="slot"><span class="time">10:20 – 10:50</span><span class="what">Morning Tea</span></div>
      <div class="slot panel"><span class="time">10:50 – 12:20</span><span class="what">Panel Discussion</span></div>
      <div class="slot"><span class="time">12:30 – 13:30</span><span class="what">Lunch</span></div>
      <div class="slot session"><span class="time">13:30 – 15:00</span><span class="what">Parallel Session</span></div>
      <div class="slot"><span class="time">15:00 – 15:30</span><span class="what">Afternoon Tea</span></div>
      <div class="slot session"><span class="time">15:30 – 17:00</span><span class="what">Parallel Session</span></div>
    </div>

    <!-- DAY 3 -->
    <div class="day">
      <div class="day-head main">
        <div class="dnum">Day 3</div>
        <div class="dname">Wed, 11 Nov</div>
      </div>
      <div class="slot"><span class="time">08:30 –</span><span class="what">Registration</span></div>
      <div class="slot keynote"><span class="time">09:00 – 09:40</span><span class="what">Keynote</span></div>
      <div class="slot keynote"><span class="time">09:40 – 10:20</span><span class="what">Keynote</span></div>
      <div class="slot"><span class="time">10:20 – 10:50</span><span class="what">Morning Tea</span></div>
      <div class="slot panel"><span class="time">10:50 – 12:20</span><span class="what">Panel Discussion</span></div>
      <div class="slot"><span class="time">12:30 – 13:30</span><span class="what">Lunch</span></div>
      <div class="slot session"><span class="time">13:30 – 15:00</span><span class="what">Parallel Session</span></div>
      <div class="slot"><span class="time">15:00 – 15:30</span><span class="what">Afternoon Tea</span></div>
      <div class="slot session"><span class="time">15:30 – 17:00</span><span class="what">Parallel Session</span></div>
      <div class="slot social"><span class="time">18:30 – 21:30</span><span class="what">Conference Banquet</span><span class="note">Awards presentation</span></div>
    </div>

    <!-- DAY 4 -->
    <div class="day">
      <div class="day-head main">
        <div class="dnum">Day 4</div>
        <div class="dname">Thu, 12 Nov</div>
      </div>
      <div class="slot"><span class="time">08:30 –</span><span class="what">Registration</span></div>
      <div class="slot keynote"><span class="time">09:00 – 09:40</span><span class="what">Keynote</span></div>
      <div class="slot keynote"><span class="time">09:40 – 10:20</span><span class="what">Keynote</span></div>
      <div class="slot"><span class="time">10:20 – 10:50</span><span class="what">Morning Tea</span></div>
      <div class="slot panel"><span class="time">10:50 – 12:20</span><span class="what">Panel Discussion</span></div>
      <div class="slot"><span class="time">12:30 – 13:30</span><span class="what">Lunch</span></div>
      <div class="slot session"><span class="time">13:30 – 15:00</span><span class="what">Parallel Session</span></div>
      <div class="slot"><span class="time">15:00 – 15:30</span><span class="what">Afternoon Tea</span></div>
      <div class="slot session"><span class="time">15:30 – 17:00</span><span class="what">Parallel Session</span></div>
    </div>

    <!-- DAY 5 -->
    <div class="day">
      <div class="day-head">
        <div class="dnum">Day 5</div>
        <div class="dname">Fri, 13 Nov</div>
      </div>
      <div class="slot"><span class="time">08:30 –</span><span class="what">Registration</span></div>
      <div class="slot session"><span class="time">09:00 – 10:20</span><span class="what">Parallel Session</span></div>
      <div class="slot"><span class="time">10:20 – 10:50</span><span class="what">Morning Tea</span></div>
      <div class="slot session"><span class="time">10:50 – 12:30</span><span class="what">Parallel Session</span></div>
      <div class="slot ceremony"><span class="time">12:30 – 13:30</span><span class="what">Closing &amp; Lunch</span></div>
      <div class="slot social"><span class="time">13:30 – 15:30</span><span class="what">Visit RMIT AIDA Hub and Campus Tour</span></div>
      <div class="slot"><span class="time">15:30 – 16:00</span><span class="what">Afternoon Tea</span></div>
      <div class="slot ceremony"><span class="time">16:00 – 17:00</span><span class="what">Committee Meeting</span></div>
    </div>

  </div>

  <div class="legend">
    <span><span class="chip" style="background:var(--dp-keynote); border-color:var(--dp-keynote-b)"></span>Keynote</span>
    <span><span class="chip" style="background:var(--dp-panel); border-color:var(--dp-panel-b)"></span>Panel</span>
    <span><span class="chip" style="background:var(--dp-session); border-color:var(--dp-session-b)"></span>Parallel sessions</span>
    <span><span class="chip" style="background:var(--dp-workshop); border-color:var(--dp-workshop-b)"></span>Workshops / Tutorials / BoF</span>
    <span><span class="chip" style="background:var(--dp-ceremony); border-color:var(--dp-ceremony-b)"></span>Ceremonies / Meetings</span>
    <span><span class="chip" style="background:var(--dp-social); border-color:var(--dp-social-b)"></span>Social events</span>
    <span><span class="chip" style="background:var(--dp-break); border-color:var(--dp-break-b)"></span>Breaks / Registration</span>
  </div>

  <div class="dp-footer">
    IEEE CyberSciTech / DASC / PICom / CBDCom 2026 · cyber-science.org/2026 · Draft program subject to change
  </div>
</div>

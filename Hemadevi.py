 <!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>Smart Hospital Robotics Simulation — Project Report</title>
<style>
  @import url('https://fonts.cdnfonts.com/css/glacial-indifference');

  :root {
    --bg: #ede8f5;
    --surface: #f8f5ff;
    --surface2: #e8dff7;
    --accent: #5b21b6;
    --accent2: #9333ea;
    --accent3: #059669;
    --text: #0f0a1e;
    --muted: #4a3a6e;
    --border: #cbbff0;
    --f: 'Glacial Indifference', sans-serif;
  }

  *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
  html { scroll-behavior: smooth; }

  body {
    background: var(--bg);
    color: var(--text);
    font-family: var(--f);
    font-size: 15px;
    line-height: 1.75;
    min-height: 100vh;
  }

  body::before {
    content: '';
    position: fixed; inset: 0;
    background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noise'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noise)' opacity='0.03'/%3E%3C/svg%3E");
    pointer-events: none; z-index: 9999; opacity: 0.4;
  }

  header {
    position: relative;
    padding: 80px 0 60px;
    overflow: hidden;
    border-bottom: 1px solid var(--border);
  }

  header::after {
    content: '';
    position: absolute;
    top: -120px; left: 50%; transform: translateX(-50%);
    width: 800px; height: 400px;
    background: radial-gradient(ellipse, rgba(124,58,237,0.13) 0%, transparent 70%);
    pointer-events: none;
  }

  .grid-bg {
    position: absolute; inset: 0;
    background-image:
      linear-gradient(rgba(124,58,237,0.07) 1px, transparent 1px),
      linear-gradient(90deg, rgba(124,58,237,0.07) 1px, transparent 1px);
    background-size: 40px 40px;
  }

  .container { max-width: 900px; margin: 0 auto; padding: 0 36px; position: relative; }

  .tag {
    display: inline-block;
    font-family: var(--f);
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    color: var(--accent);
    border: 1px solid rgba(124,58,237,0.35);
    padding: 4px 12px;
    border-radius: 2px;
    margin-bottom: 20px;
    background: rgba(124,58,237,0.07);
  }

  h1 {
    font-family: var(--f);
    font-size: clamp(36px, 5vw, 58px);
    font-weight: 700;
    line-height: 1.1;
    color: #0f0a1e;
    margin-bottom: 18px;
    letter-spacing: 0.01em;
  }

  h1 span { color: var(--accent); }

  .subtitle {
    font-size: 14px;
    color: #4a3a6e;
    font-family: var(--f);
    letter-spacing: 0.06em;
    margin-bottom: 36px;
  }

  .meta-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(160px, 1fr));
    gap: 12px;
    margin-top: 40px;
  }

  .meta-card {
    background: var(--surface);
    border: 1px solid var(--border);
    padding: 14px 18px;
    border-radius: 4px;
  }

  .meta-card .label {
    font-family: var(--f);
    font-size: 9px;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    color: #4a3a6e;
    margin-bottom: 4px;
    font-weight: 700;
  }

  .meta-card .value { font-size: 13px; font-weight: 600; color: #0f0a1e; }

  .toc {
    background: var(--surface);
    border: 1px solid var(--border);
    border-left: 3px solid var(--accent);
    padding: 28px 32px;
    border-radius: 4px;
    margin: 48px 0;
  }

  .toc-title {
    font-family: var(--f);
    font-size: 10px;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    color: var(--accent);
    margin-bottom: 16px;
    font-weight: 700;
  }

  .toc ol { list-style: none; counter-reset: toc; }

  .toc li {
    counter-increment: toc;
    padding: 5px 0;
    border-bottom: 1px solid rgba(91,33,182,0.10);
  }

  .toc li:last-child { border-bottom: none; }

  .toc a {
    color: var(--text);
    text-decoration: none;
    font-size: 14px;
    display: flex;
    align-items: center;
    gap: 12px;
    transition: color 0.2s;
    font-family: var(--f);
  }

  .toc a::before {
    content: counter(toc, decimal-leading-zero);
    font-family: var(--f);
    font-size: 11px;
    color: var(--accent);
    min-width: 24px;
    font-weight: 700;
  }

  .toc a:hover { color: var(--accent); }

  .section { padding: 60px 0; border-bottom: 1px solid var(--border); }

  .section-header { display: flex; align-items: flex-start; gap: 20px; margin-bottom: 32px; }

  .section-num {
    font-family: var(--f);
    font-size: 11px;
    color: var(--accent);
    padding-top: 8px;
    letter-spacing: 0.1em;
    min-width: 28px;
    font-weight: 700;
  }

  h2 {
    font-family: var(--f);
    font-size: clamp(22px, 3vw, 30px);
    font-weight: 700;
    color: #0f0a1e;
    line-height: 1.2;
    letter-spacing: 0.02em;
  }

  h3 {
    font-family: var(--f);
    font-size: 11px;
    font-weight: 700;
    color: var(--accent);
    margin: 28px 0 12px;
    text-transform: uppercase;
    letter-spacing: 0.18em;
  }

  p { color: #2a1a4a; margin-bottom: 16px; font-size: 15px; font-family: var(--f); }

  .highlight {
    background: linear-gradient(135deg, rgba(91,33,182,0.08), rgba(91,33,182,0.03));
    border: 1px solid rgba(91,33,182,0.25);
    padding: 20px 24px;
    border-radius: 4px;
    margin: 20px 0;
  }

  .highlight p { margin: 0; color: var(--text); }

  .component-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(240px, 1fr));
    gap: 16px;
    margin: 24px 0;
  }

  .component-card {
    background: var(--surface2);
    border: 1px solid var(--border);
    padding: 20px;
    border-radius: 4px;
    transition: border-color 0.25s, transform 0.25s;
    position: relative;
    overflow: hidden;
  }

  .component-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 2px;
    background: var(--accent);
    transform: scaleX(0);
    transform-origin: left;
    transition: transform 0.25s;
  }

  .component-card:hover::before { transform: scaleX(1); }
  .component-card:hover { border-color: rgba(91,33,182,0.45); transform: translateY(-2px); }
  .component-card .card-icon { font-size: 22px; margin-bottom: 10px; display: block; }
  .component-card .card-title { font-size: 13px; font-weight: 700; color: #0f0a1e; margin-bottom: 6px; font-family: var(--f); }
  .component-card .card-desc { font-size: 12px; color: #3d2a60; line-height: 1.5; font-family: var(--f); }

  .code-block {
    background: #f7f3ff;
    border: 1px solid var(--border);
    border-radius: 4px;
    margin: 20px 0;
    overflow: hidden;
  }

  .code-header {
    background: #ede5ff;
    padding: 8px 16px;
    font-family: var(--f);
    font-size: 11px;
    color: var(--muted);
    border-bottom: 1px solid var(--border);
    display: flex;
    align-items: center;
    gap: 8px;
    letter-spacing: 0.08em;
  }

  .code-dot { width: 8px; height: 8px; border-radius: 50%; }

  pre {
    padding: 20px;
    font-family: 'Courier New', monospace;
    font-size: 12px;
    line-height: 1.7;
    color: #3b1f6e;
    overflow-x: auto;
  }

  .kw { color: #be185d; }
  .fn { color: #7c3aed; }
  .st { color: #047857; }
  .cm { color: #a78dbf; font-style: italic; }
  .nm { color: #b45309; }

  table { width: 100%; border-collapse: collapse; margin: 20px 0; font-size: 13px; font-family: var(--f); }

  th {
    background: var(--surface2);
    padding: 10px 16px;
    text-align: left;
    font-family: var(--f);
    font-size: 10px;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    color: var(--accent);
    border-bottom: 2px solid var(--border);
    font-weight: 700;
  }

  td { padding: 10px 16px; border-bottom: 1px solid var(--border); color: #2a1a4a; }
  tr:hover td { background: rgba(91,33,182,0.04); }

  .flow { margin: 24px 0; position: relative; }

  .flow-step {
    display: flex;
    gap: 20px;
    padding: 16px 0;
    position: relative;
  }

  .flow-step::before {
    content: '';
    position: absolute;
    left: 20px; top: 52px; bottom: -16px;
    width: 1px;
    background: linear-gradient(var(--border), transparent);
  }

  .flow-step:last-child::before { display: none; }

  .flow-num {
    min-width: 40px; height: 40px;
    background: var(--surface2);
    border: 1px solid var(--accent);
    border-radius: 50%;
    display: flex; align-items: center; justify-content: center;
    font-family: var(--f);
    font-size: 12px;
    font-weight: 700;
    color: var(--accent);
    flex-shrink: 0;
  }

  .flow-content .flow-title { font-size: 14px; font-weight: 700; color: #0f0a1e; margin-bottom: 4px; font-family: var(--f); }
  .flow-content p { margin: 0; font-size: 13px; color: #3d2a60; }

  .outcome-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
    gap: 16px;
    margin: 24px 0;
  }

  .outcome-card {
    background: var(--surface2);
    border: 1px solid var(--border);
    padding: 20px;
    border-radius: 4px;
    text-align: center;
  }

  .outcome-num {
    font-family: var(--f);
    font-size: 40px;
    font-weight: 700;
    color: var(--accent);
    line-height: 1;
    margin-bottom: 6px;
    letter-spacing: -0.02em;
  }

  .outcome-label { font-size: 12px; color: #3d2a60; letter-spacing: 0.05em; font-family: var(--f); }

  .challenge-item {
    display: flex;
    gap: 16px;
    padding: 16px 0;
    border-bottom: 1px solid var(--border);
  }

  .challenge-item:last-child { border-bottom: none; }

  .challenge-marker {
    min-width: 6px; height: 6px;
    background: var(--accent2);
    border-radius: 50%;
    margin-top: 8px;
    flex-shrink: 0;
  }

  .challenge-title { font-size: 14px; font-weight: 700; color: #0f0a1e; margin-bottom: 4px; font-family: var(--f); }
  .challenge-desc { font-size: 13px; color: #3d2a60; font-family: var(--f); }

  .future-list { list-style: none; margin: 16px 0; }

  .future-list li {
    padding: 10px 0;
    border-bottom: 1px solid var(--border);
    font-size: 14px;
    color: #2a1a4a;
    display: flex;
    align-items: center;
    gap: 12px;
    font-family: var(--f);
  }

  .future-list li::before {
    content: '→';
    font-family: var(--f);
    color: var(--accent3);
    font-size: 13px;
  }

  .conclusion-box {
    background: linear-gradient(135deg, rgba(124,58,237,0.07), rgba(192,38,211,0.04));
    border: 1px solid rgba(124,58,237,0.22);
    padding: 36px;
    border-radius: 4px;
    margin: 32px 0;
  }

  footer { padding: 48px 0; text-align: center; }

  footer p {
    font-family: var(--f);
    font-size: 11px;
    color: #4a3a6e;
    letter-spacing: 0.1em;
    margin: 0;
  }

  .reveal { opacity: 0; transform: translateY(24px); transition: opacity 0.6s ease, transform 0.6s ease; }
  .reveal.visible { opacity: 1; transform: translateY(0); }

  .ref-list { margin: 24px 0; }

  .ref-item {
    display: flex;
    gap: 16px;
    padding: 14px 0;
    border-bottom: 1px solid var(--border);
    align-items: flex-start;
  }

  .ref-item:last-child { border-bottom: none; }

  .ref-num {
    font-family: var(--f);
    font-size: 11px;
    font-weight: 700;
    color: var(--accent);
    min-width: 32px;
    padding-top: 2px;
    letter-spacing: 0.05em;
  }

  .ref-body { font-size: 13px; line-height: 1.65; color: #3d2a60; font-family: var(--f); }
  .ref-authors { font-weight: 700; color: #0f0a1e; margin-right: 4px; }
  .ref-year { margin-right: 4px; color: #3d2a60; }
  .ref-title { font-style: italic; color: #5b21b6; margin-right: 4px; }
  .ref-source { margin-right: 6px; color: #3d2a60; }

  .ref-link {
    color: var(--accent);
    text-decoration: none;
    font-family: var(--f);
    font-size: 11px;
    word-break: break-all;
  }

  .ref-link:hover { text-decoration: underline; }

  /* SOLO AUTHOR BLOCK */
  .author-block {
    margin: 28px 0 36px;
    padding: 22px 28px;
    background: rgba(91,33,182,0.07);
    border: 1px solid rgba(91,33,182,0.22);
    border-left: 4px solid var(--accent);
    border-radius: 6px;
    display: inline-block;
    width: 100%;
  }

  .author-label {
    font-family: var(--f);
    font-size: 9px;
    letter-spacing: 0.22em;
    text-transform: uppercase;
    color: var(--accent);
    margin-bottom: 8px;
    font-weight: 700;
  }

  .author-name {
    font-family: var(--f);
    font-size: 22px;
    font-weight: 700;
    color: #0f0a1e;
    letter-spacing: 0.04em;
  }

  @media (max-width: 600px) {
    .container { padding: 0 20px; }
    h1 { font-size: 30px; }
    .meta-grid { grid-template-columns: 1fr 1fr; }
    .author-name { font-size: 18px; }
  }
</style>
</head>
<body>

<header>
  <div class="grid-bg"></div>
  <div class="container">
    <div class="tag">Project Report · Robotics Simulation</div>
    <h1>Smart Hospital<br/><span>Robotics Simulation</span><br/>Environment</h1>
    <p class="subtitle">// Intelligent Multi-Robot Healthcare Automation using BrowserBotics &amp; PyBullet Physics</p>

    <div class="author-block">
      <div class="author-label">Author</div>
      <div class="author-name">Gautam Vijay K K</div>
    </div>

    <div class="meta-grid">
      <div class="meta-card"><div class="label">Domain</div><div class="value">Healthcare Robotics</div></div>
      <div class="meta-card"><div class="label">Platform</div><div class="value">BrowserBotics (bb)</div></div>
      <div class="meta-card"><div class="label">Physics Engine</div><div class="value">PyBullet / Bullet3</div></div>
      <div class="meta-card"><div class="label">Simulation Rate</div><div class="value">240 Hz (DT = 1/240 s)</div></div>
      <div class="meta-card"><div class="label">Robot Models</div><div class="value">Franka Panda URDF</div></div>
      <div class="meta-card"><div class="label">Language</div><div class="value">Python 3</div></div>
    </div>
  </div>
</header>

<main>
  <div class="container">

    <div class="toc reveal">
      <div class="toc-title">// Table of Contents</div>
      <ol>
        <li><a href="#abstract">Abstract</a></li>
        <li><a href="#problem">Problem Statement</a></li>
        <li><a href="#objectives">Objectives</a></li>
        <li><a href="#environment">Environment Design</a></li>
        <li><a href="#methodology">Methodology &amp; Architecture</a></li>
        <li><a href="#implementation">Implementation Details</a></li>
        <li><a href="#outcomes">Results &amp; Outcomes</a></li>
        <li><a href="#challenges">Challenges &amp; Solutions</a></li>
        <li><a href="#future">Future Work</a></li>
        <li><a href="#conclusion">Conclusion</a></li>
        <li><a href="#references">References</a></li>
      </ol>
    </div>

    <section class="section reveal" id="abstract">
      <div class="section-header"><span class="section-num">01</span><h2>Abstract</h2></div>
      <div class="highlight">
        <p>This project presents a comprehensive <strong>physics-based simulation of a fully equipped smart hospital room</strong> featuring multiple collaborative autonomous robots. Built on the BrowserBotics (bb) framework atop PyBullet rigid-body physics, the simulation integrates a Franka Panda 7-DOF robotic arm for medication pick-and-place operations, a Da Vinci-inspired surgical robot with animated multi-arm kinematics, a Lokomat rehabilitation exoskeleton performing gait assistance, and an autonomous vacuum robot performing continuous floor cleaning. The environment models realistic hospital equipment — beds, IV stands, vital-sign monitors, crash carts, surgical lighting, and workstations — all repositionable at runtime via interactive debug sliders.</p>
      </div>
      <p>The simulation serves as a proof-of-concept testbed for human-robot collaboration protocols in clinical settings, demonstrating path planning, inverse kinematics, and multi-agent coordination within a shared physical workspace.</p>
    </section>

    <section class="section reveal" id="problem">
      <div class="section-header"><span class="section-num">02</span><h2>Problem Statement</h2></div>
      <p>Modern hospitals increasingly explore robotic automation to reduce staff workload, minimize infection vectors from human contact, and improve precision in surgical and rehabilitation workflows. However, testing real robotic systems in live clinical environments is:</p>
      <div class="flow">
        <div class="flow-step">
          <div class="flow-num">!</div>
          <div class="flow-content"><div class="flow-title">Prohibitively expensive</div><p>Physical robot procurement, facility modification, and insurance overhead creates barriers to iterative prototyping.</p></div>
        </div>
        <div class="flow-step">
          <div class="flow-num">!</div>
          <div class="flow-content"><div class="flow-title">Safety-critical</div><p>Bugs in motion planning or collision avoidance cannot be tolerated near patients or fragile equipment.</p></div>
        </div>
        <div class="flow-step">
          <div class="flow-num">!</div>
          <div class="flow-content"><div class="flow-title">Multi-system complexity</div><p>Coordinating heterogeneous robots (surgical, rehabilitative, logistics) in the same space requires simulation before deployment.</p></div>
        </div>
      </div>
      <p>This project addresses these barriers by providing a <strong>low-cost, high-fidelity simulation environment</strong> where robotic algorithms can be developed, tested, and visualized before any physical hardware is involved.</p>
    </section>

    <section class="section reveal" id="objectives">
      <div class="section-header"><span class="section-num">03</span><h2>Objectives</h2></div>
      <ul class="future-list">
        <li>Design a geometrically detailed 10×8×4 m hospital room using primitive collision bodies</li>
        <li>Implement a Franka Panda arm with full 7-DOF IK-based pick-and-place for medication delivery</li>
        <li>Simulate a Da Vinci surgical robot with three animated arms performing table-top maneuvers</li>
        <li>Animate a Lokomat rehabilitation exoskeleton executing periodic gait cycles</li>
        <li>Deploy an autonomous vacuum robot executing a room-wide coverage path</li>
        <li>Enable runtime repositioning of all major furniture and equipment via debug UI sliders</li>
        <li>Provide a gripper control interface (manual + automatic pick-and-drop sequences)</li>
        <li>Simulate dynamic objects (medication cube) subject to rigid-body physics</li>
      </ul>
    </section>

    <section class="section reveal" id="environment">
      <div class="section-header"><span class="section-num">04</span><h2>Environment Design</h2></div>
      <p>The hospital room is constructed entirely from axis-aligned box primitives via <code>bb.createBody(shape="box", ...)</code>. This approach allows real-time physics simulation with precise collision geometry. The room dimensions are <strong>10 m (L) × 8 m (W) × 4 m (H)</strong>.</p>

      <h3>Static Elements</h3>
      <div class="component-grid">
        <div class="component-card"><span class="card-icon">🏥</span><div class="card-title">Room Shell</div><div class="card-desc">Floor with tile grid, 3 solid walls, front wall with double-door entry and hospital cross signage</div></div>
        <div class="component-card"><span class="card-icon">💡</span><div class="card-title">Overhead Surgical Light</div><div class="card-desc">Dual-arm ceiling light above the bed zone with 6 recessed panel lights</div></div>
        <div class="component-card"><span class="card-icon">🪟</span><div class="card-title">Windows</div><div class="card-desc">Two framed windows with horizontal blind slats on both side walls</div></div>
        <div class="component-card"><span class="card-icon">🚿</span><div class="card-title">Sink &amp; Mirror</div><div class="card-desc">Hand-wash station with faucet, basin, soap dispenser, and wall mirror</div></div>
        <div class="component-card"><span class="card-icon">💊</span><div class="card-title">Medicine Cabinet</div><div class="card-desc">Wall-mounted locked cabinet with red cross, three shelves with vials</div></div>
        <div class="component-card"><span class="card-icon">📋</span><div class="card-title">Whiteboard</div><div class="card-desc">Patient info board with color-coded marker lines and tray</div></div>
        <div class="component-card"><span class="card-icon">🖥️</span><div class="card-title">Nurse Workstation</div><div class="card-desc">Full L-shaped desk with dual monitors, keyboard, mouse, tower PC, and operator chair</div></div>
        <div class="component-card"><span class="card-icon">🗑️</span><div class="card-title">Waste Bins</div><div class="card-desc">Color-coded biohazard (red), sharps (yellow), and general bins</div></div>
        <div class="component-card"><span class="card-icon">🔌</span><div class="card-title">Network Rack</div><div class="card-desc">19" rack unit with 8 patch panels and status LEDs</div></div>
        <div class="component-card"><span class="card-icon">🚨</span><div class="card-title">Emergency Call Panel</div><div class="card-desc">Wall-mounted panel beside door with red alert and green clear buttons</div></div>
        <div class="component-card"><span class="card-icon">⏱️</span><div class="card-title">Wall Clock</div><div class="card-desc">Round clock with hour and minute hands above door</div></div>
        <div class="component-card"><span class="card-icon">💉</span><div class="card-title">Medication Counter</div><div class="card-desc">Prep counter with vials, syringes, and drawer set</div></div>
      </div>

      <h3>Moveable Groups</h3>
      <p>Six equipment groups are repositionable at runtime using <strong>XY debug sliders</strong>. Each group is defined as a list of <code>(body_id, original_position)</code> tuples; displacement is applied as a delta transform:</p>
      <table>
        <thead><tr><th>Group</th><th>Default Position</th><th>Slider Range</th><th>Components</th></tr></thead>
        <tbody>
          <tr><td>Hospital Bed</td><td>(0, 0)</td><td>±3 m</td><td>Frame, mattress, rails, IV bar, pillow, coverlet</td></tr>
          <tr><td>Panda Robot + Tray</td><td>(0, −1)</td><td>X: ±3, Y: −3..1</td><td>Base platform, wheels, tray table, tool items</td></tr>
          <tr><td>IV Stand</td><td>(−0.9, 0.9)</td><td>±3.5 m</td><td>Pole, base cross, bag, drip tube, pump</td></tr>
          <tr><td>Crash Cart</td><td>(3.8, 2.5)</td><td>±4.5 m</td><td>Red body, drawers with pulls, wheels, AED paddle</td></tr>
          <tr><td>Oxygen Tank</td><td>(−1.4, 0.9)</td><td>±4 m</td><td>Green cylinder, valve, regulator head</td></tr>
          <tr><td>Vital Signs Monitor</td><td>(−1.7, −0.9)</td><td>±4 m</td><td>Pole stand, screen, waveform bars, cable</td></tr>
        </tbody>
      </table>
    </section>

    <section class="section reveal" id="methodology">
      <div class="section-header"><span class="section-num">05</span><h2>Methodology &amp; Architecture</h2></div>
      <h3>System Architecture</h3>
      <div class="flow">
        <div class="flow-step"><div class="flow-num">1</div><div class="flow-content"><div class="flow-title">Scene Initialization</div><p>All static bodies, moveable groups, robot models, and animated objects created once before the main loop.</p></div></div>
        <div class="flow-step"><div class="flow-num">2</div><div class="flow-content"><div class="flow-title">Physics Step</div><p><code>bb.stepSimulation(DT)</code> advances rigid-body dynamics at 240 Hz. Dynamic mass is assigned only to the medication cube.</p></div></div>
        <div class="flow-step"><div class="flow-num">3</div><div class="flow-content"><div class="flow-title">Autonomous Robot Updates</div><p>Vacuum robot waypoint navigation, Da Vinci surgical arm parametric animation, Lokomat gait kinematics — all updated per frame using elapsed simulation time.</p></div></div>
        <div class="flow-step"><div class="flow-num">4</div><div class="flow-content"><div class="flow-title">User Input Processing</div><p>Debug sliders polled for object positions; debug buttons checked for state transitions (PickAndDrop, ResetCube, MoveArm, GripOpen, GripClose).</p></div></div>
        <div class="flow-step"><div class="flow-num">5</div><div class="flow-content"><div class="flow-title">Panda Arm Sequencer</div><p>Finite-state pick-and-place sequence executes IK-guided motion steps with configurable hold durations per phase.</p></div></div>
      </div>
      <h3>Simulation Philosophy</h3>
      <p>The simulation deliberately uses <strong>kinematic override</strong> for all animated robots (Da Vinci, Lokomat, vacuum, visual gripper fingers) rather than PD torque control. This provides visually smooth motion without requiring tuned gains, which is appropriate for a visualization-first prototype. Only the Franka Panda uses PyBullet's joint motor PD control via <code>setJointMotorControl</code> to demonstrate realistic servo-driven behavior.</p>
    </section>

    <section class="section reveal" id="implementation">
      <div class="section-header"><span class="section-num">06</span><h2>Implementation Details</h2></div>
      <h3>Franka Panda — Pick-and-Place</h3>
      <p>The Panda arm is loaded from URDF with <code>fixedBase=True</code> oriented 90° about Z. Inverse kinematics targets are computed via:</p>
      <div class="code-block">
        <div class="code-header"><div class="code-dot" style="background:#ff5f57"></div><div class="code-dot" style="background:#febc2e"></div><div class="code-dot" style="background:#28c840"></div>&nbsp;panda_ik.py</div>
        <pre><span class="cm"># Compute IK for end-effector position + fixed downward orientation</span>
<span class="kw">def</span> <span class="fn">ik_move</span>(px, py, pz):
    jp = bb.<span class="fn">calculateInverseKinematics</span>(
        robot, ee_link,
        [px, py, pz], DQ   <span class="cm"># DQ = euler(π, 0, 0) → gripper faces down</span>
    )
    <span class="kw">for</span> i <span class="kw">in</span> <span class="fn">range</span>(<span class="fn">min</span>(<span class="nm">7</span>, <span class="fn">len</span>(jp))):
        bb.<span class="fn">setJointMotorControl</span>(robot, i, targetPosition=jp[i])</pre>
      </div>

      <p>The pick-and-place sequence is defined as a list of <strong>(label, action_fn, hold_frames)</strong> tuples. Twelve discrete phases are executed:</p>
      <table>
        <thead><tr><th>Phase</th><th>Action</th><th>Hold (frames)</th></tr></thead>
        <tbody>
          <tr><td>HOME</td><td>Return to home joint configuration</td><td>160</td></tr>
          <tr><td>OPEN</td><td>Open gripper fingers</td><td>80</td></tr>
          <tr><td>ABOVE_PICK</td><td>Move to +16 cm above pick point</td><td>300</td></tr>
          <tr><td>TO_PICK</td><td>Descend to cube surface</td><td>300</td></tr>
          <tr><td>GRIP</td><td>Close fingers around cube</td><td>160</td></tr>
          <tr><td>LIFT</td><td>Raise to carry height</td><td>300</td></tr>
          <tr><td>TRANSIT</td><td>Arc through midpoint at +5 cm carry height</td><td>300</td></tr>
          <tr><td>ABOV_DROP</td><td>Descend above drop zone</td><td>300</td></tr>
          <tr><td>TO_DROP</td><td>Lower to drop surface</td><td>300</td></tr>
          <tr><td>RELEASE</td><td>Open gripper to deposit cube</td><td>160</td></tr>
          <tr><td>RETREAT</td><td>Lift back above drop zone</td><td>300</td></tr>
          <tr><td>HOME_END</td><td>Return home</td><td>160</td></tr>
        </tbody>
      </table>

      <h3>Cube Carry (Kinematic Attachment)</h3>
      <div class="code-block">
        <div class="code-header"><div class="code-dot" style="background:#ff5f57"></div><div class="code-dot" style="background:#febc2e"></div><div class="code-dot" style="background:#28c840"></div>&nbsp;carry_logic.py</div>
        <pre><span class="kw">if</span> gripped:
    ep, eo = bb.<span class="fn">getLinkPose</span>(robot, ee_link)
    bb.<span class="fn">resetBasePose</span>(cube,
        [ep[<span class="nm">0</span>], ep[<span class="nm">1</span>], ep[<span class="nm">2</span>] - CARRY],  <span class="cm"># 5.5 cm below EE</span>
        eo)</pre>
      </div>

      <h3>Da Vinci Surgical Robot</h3>
      <div class="code-block">
        <div class="code-header"><div class="code-dot" style="background:#ff5f57"></div><div class="code-dot" style="background:#febc2e"></div><div class="code-dot" style="background:#28c840"></div>&nbsp;surgical_anim.py</div>
        <pre><span class="kw">def</span> <span class="fn">animate_surgical_robot</span>(t):
    a1 = t * <span class="nm">0.6</span>
    tip1_x = SRX + math.<span class="fn">sin</span>(a1)*<span class="nm">0.12</span> - <span class="nm">0.08</span>
    tip1_y = SRY + math.<span class="fn">cos</span>(a1*<span class="nm">0.7</span>)*<span class="nm">0.08</span>
    tip1_z = table_z + <span class="nm">0.02</span>
    mid1 = [(<span class="fn">sh1</span>[<span class="nm">0</span>]+tip1_x)/<span class="nm">2</span>, ..., ... + <span class="nm">0.15</span>]
    g = <span class="nm">0.012</span> + <span class="nm">0.008</span>*math.<span class="fn">sin</span>(t*<span class="nm">2.5</span>)</pre>
      </div>

      <h3>Lokomat Gait Animation</h3>
      <div class="code-block">
        <div class="code-header"><div class="code-dot" style="background:#ff5f57"></div><div class="code-dot" style="background:#febc2e"></div><div class="code-dot" style="background:#28c840"></div>&nbsp;lokomat_gait.py</div>
        <pre><span class="cm"># Hip and knee angles from phase offset</span>
ph = t * LK_GAIT_SPEED + (<span class="nm">0.0</span> <span class="kw">if</span> side==<span class="st">"L"</span> <span class="kw">else</span> math.pi)
hip_a  = LK_HIP_AMP  * math.<span class="fn">sin</span>(ph)
knee_b = LK_KNEE_AMP * <span class="fn">max</span>(<span class="nm">0</span>, math.<span class="fn">sin</span>(ph - <span class="nm">0.5</span>))
knee_x = LKX + LK_THIGH_LEN * math.<span class="fn">sin</span>(hip_a)
knee_z = hip_z - LK_THIGH_LEN * math.<span class="fn">cos</span>(hip_a)</pre>
      </div>

      <h3>Vacuum Robot Navigation</h3>
      <div class="code-block">
        <div class="code-header"><div class="code-dot" style="background:#ff5f57"></div><div class="code-dot" style="background:#febc2e"></div><div class="code-dot" style="background:#28c840"></div>&nbsp;vacuum_nav.py</div>
        <pre>tgt = vac_path[vac_wp]
dvx = tgt[<span class="nm">0</span>]-vac_x;  dvy = tgt[<span class="nm">1</span>]-vac_y
d   = math.<span class="fn">sqrt</span>(dvx*dvx + dvy*dvy)
<span class="kw">if</span> d &lt; <span class="nm">0.15</span>:
    vac_wp = (vac_wp+<span class="nm">1</span>) % <span class="fn">len</span>(vac_path)
<span class="kw">else</span>:
    vac_x += (dvx/d)*vac_spd
    ang = math.<span class="fn">atan2</span>(dvy, dvx)</pre>
      </div>
    </section>

    <section class="section reveal" id="outcomes">
      <div class="section-header"><span class="section-num">07</span><h2>Results &amp; Outcomes</h2></div>
      <div class="outcome-grid">
        <div class="outcome-card"><div class="outcome-num">4</div><div class="outcome-label">Distinct Robot Systems</div></div>
        <div class="outcome-card"><div class="outcome-num">240</div><div class="outcome-label">Hz Physics Rate</div></div>
        <div class="outcome-card"><div class="outcome-num">12</div><div class="outcome-label">Pick-and-Place Phases</div></div>
        <div class="outcome-card"><div class="outcome-num">6</div><div class="outcome-label">Repositionable Equipment Groups</div></div>
        <div class="outcome-card"><div class="outcome-num">13</div><div class="outcome-label">Vacuum Coverage Waypoints</div></div>
        <div class="outcome-card"><div class="outcome-num">300+</div><div class="outcome-label">Scene Primitive Bodies</div></div>
      </div>
      <h3>Key Achievements</h3>
      <ul class="future-list">
        <li>Fully automated medication delivery cycle: tray → bed and bed → tray, both directions</li>
        <li>All robot positions update correctly when equipment is repositioned via sliders at runtime</li>
        <li>Da Vinci arm animation produces realistic instrument sweep over a simulated patient table</li>
        <li>Lokomat gait cycle shows physiologically plausible bilateral alternating leg swing with treadmill belt motion</li>
        <li>Vacuum robot completes full room coverage without manual intervention</li>
        <li>Visual gripper finger bodies track end-effector orientation in real-time using quaternion rotation</li>
        <li>Status overlay text dynamically reports active motion phase to operator</li>
      </ul>
    </section>

    <section class="section reveal" id="challenges">
      <div class="section-header"><span class="section-num">08</span><h2>Challenges &amp; Solutions</h2></div>
      <div class="challenge-item"><div class="challenge-marker"></div><div><div class="challenge-title">Cube Slipping Under High-Speed Motion</div><div class="challenge-desc">Fast IK transitions caused the dynamic cube to lag behind the gripper. Solved by using <code>resetBasePose</code> kinematic attachment on every frame during the CARRY_STEPS phases, completely overriding physics for the carried object.</div></div></div>
      <div class="challenge-item"><div class="challenge-marker"></div><div><div class="challenge-title">Group Repositioning of Multi-Body Objects</div><div class="challenge-desc">Updating dozens of body positions atomically per slider change was expensive. Solved by tracking previous slider values and only triggering <code>reposition_group</code> when delta exceeds 1 mm threshold.</div></div></div>
      <div class="challenge-item"><div class="challenge-marker"></div><div><div class="challenge-title">IK Failing Near Arm Singularities</div><div class="challenge-desc">Some target positions caused URDF IK to return fewer than 7 joint values. Mitigated by clamping loop to <code>min(7, len(jp))</code> and defining home configuration offsets that bias the arm away from known singularity regions.</div></div></div>
      <div class="challenge-item"><div class="challenge-marker"></div><div><div class="challenge-title">Visual Finger Orientation Drift</div><div class="challenge-desc">Gripper finger visualization needed to match end-effector orientation dynamically. Solved by implementing <code>quat_rotate</code> to project finger offsets into EE frame, then placing them using <code>resetBasePose</code> each frame.</div></div></div>
      <div class="challenge-item"><div class="challenge-marker"></div><div><div class="challenge-title">Coordinate Offsets on Repositioned Sequences</div><div class="challenge-desc">When the robot base is moved via slider, the pick/drop target coordinates must be adjusted. Solved by computing <code>base_dx/dy</code> and <code>bed_dx/dy</code> deltas at the moment PickAndDrop is pressed, then constructing the sequence with offset-corrected positions.</div></div></div>
    </section>

    <section class="section reveal" id="future">
      <div class="section-header"><span class="section-num">09</span><h2>Future Work</h2></div>
      <ul class="future-list">
        <li>Replace hardcoded Lokomat gait with a patient-adaptive model driven by EMG signal data</li>
        <li>Implement full ROS2 integration to allow real Panda hardware control from the same codebase</li>
        <li>Add collision detection-based obstacle avoidance for the vacuum robot path planner</li>
        <li>Introduce a second robotic nurse assistant capable of drawing curtains and operating door handles</li>
        <li>Replace debug sliders with a 2D touchscreen floor-plan interface for drag-and-drop furniture layout</li>
        <li>Add occupancy grid mapping from simulated LIDAR on the robot base platform</li>
        <li>Simulate fluid dynamics for IV drip bag volume decrease over time</li>
        <li>Implement multi-robot collision avoidance using a shared workspace reservation system</li>
      </ul>
    </section>

    <section class="section reveal" id="conclusion">
      <div class="section-header"><span class="section-num">10</span><h2>Conclusion</h2></div>
      <div class="conclusion-box">
        <p style="color: #2a1a4a; font-size: 15px; margin: 0;">
          This project successfully demonstrates a <strong>multi-robot smart hospital simulation</strong> that is both visually accurate and physically grounded. By combining a Franka Panda arm executing IK-guided pick-and-place with a Da Vinci surgical robot, a Lokomat exoskeleton, and an autonomous vacuum agent — all sharing the same physics world — the system provides a meaningful testbed for studying human-robot collaboration protocols, spatial layout planning, and motion algorithm development in healthcare environments.
          <br/><br/>
          The architecture's clean separation of static scene construction, moveable group management, animation callbacks, and user input processing makes it highly extensible. The simulation validates that physics-based virtual environments can replicate the complexity of real hospital workflows at negligible cost and zero patient risk — making it a compelling first step toward simulation-to-real transfer for clinical robotics.
        </p>
      </div>
      <h3>Technology Stack Summary</h3>
      <table>
        <thead><tr><th>Component</th><th>Technology</th><th>Purpose</th></tr></thead>
        <tbody>
          <tr><td>Physics Engine</td><td>PyBullet / Bullet3</td><td>Rigid-body dynamics, IK solver, URDF loading</td></tr>
          <tr><td>Simulation API</td><td>BrowserBotics (bb)</td><td>Scene construction, debug UI, joint control</td></tr>
          <tr><td>Robot Model</td><td>panda.urdf (Franka)</td><td>7-DOF arm kinematics and link definitions</td></tr>
          <tr><td>Language</td><td>Python 3</td><td>Control logic, animation, sequencing</td></tr>
          <tr><td>Math</td><td>Python math module</td><td>Trig for gait, quaternion ops, path geometry</td></tr>
          <tr><td>Timing</td><td>time.sleep(DT)</td><td>Real-time pacing at 240 Hz</td></tr>
        </tbody>
      </table>
    </section>

    <section class="section reveal" id="references">
      <div class="section-header"><span class="section-num">11</span><h2>References</h2></div>
      <div class="ref-list">
        <div class="ref-item"><div class="ref-num">[1]</div><div class="ref-body"><span class="ref-authors">Coumans, E., &amp; Bai, Y.</span> <span class="ref-year">(2016–2021).</span> <span class="ref-title">PyBullet, a Python module for physics simulation for games, robotics and machine learning.</span> <span class="ref-source">GitHub Repository.</span> <a class="ref-link" href="http://pybullet.org" target="_blank">http://pybullet.org</a></div></div>
        <div class="ref-item"><div class="ref-num">[2]</div><div class="ref-body"><span class="ref-authors">Haddadin, S., et al.</span> <span class="ref-year">(2022).</span> <span class="ref-title">The Franka Emika Robot: A Reference Platform for Robotics Research and Education.</span> <span class="ref-source">IEEE Robotics &amp; Automation Magazine, 29(2), 46–64.</span></div></div>
        <div class="ref-item"><div class="ref-num">[3]</div><div class="ref-body"><span class="ref-authors">Guthart, G. S., &amp; Salisbury, J. K.</span> <span class="ref-year">(2000).</span> <span class="ref-title">The Intuitive™ telesurgery system: Overview and application.</span> <span class="ref-source">Proceedings ICRA, 618–621.</span></div></div>
        <div class="ref-item"><div class="ref-num">[4]</div><div class="ref-body"><span class="ref-authors">Jezernik, S., et al.</span> <span class="ref-year">(2003).</span> <span class="ref-title">Robotic orthosis Lokomat: A rehabilitation and research tool.</span> <span class="ref-source">Neuromodulation, 6(2), 108–115.</span></div></div>
        <div class="ref-item"><div class="ref-num">[5]</div><div class="ref-body"><span class="ref-authors">Siciliano, B., et al.</span> <span class="ref-year">(2009).</span> <span class="ref-title">Robotics: Modelling, Planning and Control.</span> <span class="ref-source">Springer.</span></div></div>
        <div class="ref-item"><div class="ref-num">[6]</div><div class="ref-body"><span class="ref-authors">Meng, L., et al.</span> <span class="ref-year">(2021).</span> <span class="ref-title">Autonomous robot for hospital logistics.</span> <span class="ref-source">Robotics and Autonomous Systems, 136, 103724.</span></div></div>
        <div class="ref-item"><div class="ref-num">[7]</div><div class="ref-body"><span class="ref-authors">Quigley, M., et al.</span> <span class="ref-year">(2009).</span> <span class="ref-title">ROS: An open-source Robot Operating System.</span> <span class="ref-source">ICRA Workshop on Open Source Software.</span></div></div>
        <div class="ref-item"><div class="ref-num">[8]</div><div class="ref-body"><span class="ref-authors">Craig, J. J.</span> <span class="ref-year">(2005).</span> <span class="ref-title">Introduction to Robotics: Mechanics and Control (3rd ed.).</span> <span class="ref-source">Pearson Prentice Hall.</span></div></div>
        <div class="ref-item"><div class="ref-num">[9]</div><div class="ref-body"><span class="ref-authors">Correll, N., et al.</span> <span class="ref-year">(2016).</span> <span class="ref-title">Analysis and Observations from the First Amazon Picking Challenge.</span> <span class="ref-source">IEEE TASE, 15(1), 172–188.</span></div></div>
        <div class="ref-item"><div class="ref-num">[10]</div><div class="ref-body"><span class="ref-authors">Bharti, T., &amp; Turlapati, S. H.</span> <span class="ref-year">(2020).</span> <span class="ref-title">Simulation environments for robot learning: A comparative review.</span> <span class="ref-source">IJRRD, 10(1), 1–12.</span></div></div>
        <div class="ref-item"><div class="ref-num">[11]</div><div class="ref-body"><span class="ref-authors">BrowserBotics Documentation.</span> <span class="ref-year">(2024).</span> <span class="ref-title">BrowserBotics API Reference.</span> <span class="ref-source">Internal Technical Documentation.</span></div></div>
        <div class="ref-item"><div class="ref-num">[12]</div><div class="ref-body"><span class="ref-authors">Franka Robotics GmbH.</span> <span class="ref-year">(2023).</span> <span class="ref-title">Franka Emika Panda URDF and Dynamic Parameters.</span> <a class="ref-link" href="https://frankaemika.github.io/docs" target="_blank">https://frankaemika.github.io/docs</a></div></div>
      </div>
    </section>

  </div>
</main>

<footer>
  <div class="container">
    <p>Smart Hospital Robotics Simulation &nbsp;·&nbsp; BrowserBotics + PyBullet &nbsp;·&nbsp; Gautam Vijay K K</p>
  </div>
</footer>

<script>
  const reveals = document.querySelectorAll('.reveal');
  const obs = new IntersectionObserver(entries => {
    entries.forEach(e => { if (e.isIntersecting) { e.target.classList.add('visible'); obs.unobserve(e.target); } });
  }, { threshold: 0.08 });
  reveals.forEach(r => obs.observe(r));
</script>

</body>
</html>

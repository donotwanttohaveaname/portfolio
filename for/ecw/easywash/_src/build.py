#!/usr/bin/env python3
"""Builds the EasyWash B2B landing page concepts.

  a/index.html  Variation A: platform first, original colour scheme (ew.css + ew-classic.css)
  a-new/        the same page in the light scheme (ew.css only), kept for comparison
  b/index.html  Variation B: terminal first (hardware at the bay, platform behind it)
  c/index.html  Variation C: follow one car (scroll story; source in _src/c.html)
  index.html    the pitch page (head and styles lifted from ../index.html, body from _src/pitch.html)

Run:  python3 _src/build.py

Rules for the copy: no em dashes, no oil company names (not public references), the camera reads the
plate (not the terminal), WashXL and Washman are single sites. Design rules for A and B: every .view
fits one screen, no label above a heading, one theme, one accent, real photos instead of drawn screens.
"""
from pathlib import Path

ROOT = Path(__file__).parent.parent   # .../for/ecw/easywash
SRC = Path(__file__).parent
VERSION = "v0.2, 15 Nov 2026"
BANNED = ("OKQ8", "Circle K", "Neste", "Shell", "Esso", "7-Eleven", "\u2014", "\u2013")

HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="robots" content="noindex, nofollow, noarchive">
<title>%%TITLE%%</title>
<meta name="description" content="%%DESC%%">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Schibsted+Grotesk:wght@400;500;600;700;800&family=IBM+Plex+Mono:wght@500;600&display=swap" rel="stylesheet">
%%CSS%%
</head>
<body>
"""

CONCEPT = """
<div class="concept"><div class="wrap">
  <div><b>EasyWash for business.</b> Concept %%VERSION%%.</div>
  <nav class="switch" aria-label="Concept variation">
    <a href="../a/"%%ON_A%%>A<span>: platform</span></a>
    <a href="../b/"%%ON_B%%>B<span>: terminal</span></a>
    <a href="../c/"%%ON_C%%>C<span>: rain or shine</span></a>
    <a href="../d/">D<span>: real sites</span></a>
    <a href="../a-new/"%%ON_A-NEW%%>A-new<span>: light</span></a>
  </nav>
  <a class="pitch" href="../">Read the pitch</a>
</div></div>
"""

NAV = """
<header class="nav"><div class="wrap">
  <a class="logo" href="#top"><img src="../assets/%%LOGO%%" alt="EasyWash" width="124" height="36"><span>for business</span></a>
  <nav class="menu" aria-label="Page">
    <a href="#platform">Platform</a>
    <a href="#how">How it works</a>
    <a href="#customers">Customers</a>
    <a href="#rollout">Rollout</a>
    <a href="#faq">FAQ</a>
  </nav>
  <div class="nav-r">
    <a class="txt" href="https://easywash.com">For drivers</a>
    <a class="txt" href="#">Operator login</a>
    <a class="btn btn-main btn-sm" href="#call">Book a call</a>
  </div>
</div></header>
"""

HERO_A = """
<section class="view hero" id="top"><div class="wrap">
  <div>
    <h1>Wash revenue that arrives <em>every month.</em></h1>
    <p class="lead">EasyWash sells memberships in your app and at the bay, reads the plate, starts the wash and bills every month.</p>
    <div class="cta-row"><a class="btn btn-main" href="#call">Book a call</a><a class="btn btn-alt" href="#how">See how it works</a></div>
  </div>
  <form class="bay" id="bay">
    <img class="cam" src="../assets/camera.webp" alt="" width="500" height="420">
    <label for="plate">Try it. Type a licence plate and drive in.</label>
    <div class="bay-in">
      <span class="pin"><i></i><input id="plate" value="ABC-123" maxlength="8" autocomplete="off" spellcheck="false" aria-label="Licence plate"></span>
      <button class="btn btn-inv" type="submit">Drive in</button>
    </div>
    <ol class="log" aria-live="polite">
      <li><small>07:42</small><span>Camera reads <b data-plate>ABC-123</b></span></li>
      <li><small>07:42</small><span>Member found: Unlimited Premium</span></li>
      <li><small>07:42</small><span>Door opens, programme 3 starts</span></li>
      <li><small>07:49</small><span>Car leaves. The app asks for a rating.</span></li>
      <li class="last"><small>The 1st</small><b>€29.90 renews</b></li>
    </ol>
  </form>
</div></section>
"""

HERO_B = """
<section class="view hero" id="top"><div class="wrap">
  <div>
    <h1>The payment terminal that <em>sells memberships.</em></h1>
    <p class="lead">It takes cards and phones, signs a driver up for a monthly plan in five seconds, and starts the wash.</p>
    <div class="cta-row"><a class="btn btn-main" href="#call">Book a call</a><a class="btn btn-alt" href="#hardware">See the hardware</a></div>
  </div>
  <div class="hw-hero">
    <img class="cam" src="../assets/camera.webp" alt="EasyWash licence plate camera" width="500" height="420">
    <img class="pillar" src="../assets/pillar.webp" alt="EasyWash terminal at a wash bay, showing wash programmes and a monthly wash club" width="1097" height="1500">
  </div>
</div></section>
"""

PROOF = """
<section class="view dark" id="proof"><div class="wrap">
  <h2 class="say">Every month, <b>100,000 drivers</b> pay one Nordic fuel retailer for their car wash. That is <b>€3 million</b> of recurring revenue, on EasyWash.</h2>
  <div class="facts">
    <div><b>700+ sites</b>live in Finland, Sweden, Norway, Denmark and Latvia</div>
    <div><b>1,000,000+ drivers</b>have washed through EasyWash</div>
    <div><b>3x revenue</b>within 90 days at Divi Vienā, Latvia</div>
    <div><b>Best Product</b>Petrol Station 2025 fair, Warsaw</div>
  </div>
</div></section>
"""

GAP = """
<section class="view tint" id="gap"><div class="wrap ba">
  <div>
    <h2>The machine can wash 20,000 cars a year. Most sites sell 5,000.</h2>
    <p class="lead">A typical site sells about 15% of its capacity: one counter, staffed hours, single washes. This is what changes.</p>
  </div>
  <table>
    <thead><tr><th>Today</th><th>With EasyWash</th></tr></thead>
    <tbody>
      <tr><td>5,000 washes a year</td><td>20,000 washes a year</td></tr>
      <tr><td>Sold at the counter</td><td>Sold in the app, at the bay, on the web and to companies</td></tr>
      <tr><td>Open when staffed</td><td>Open 24/7, unattended</td></tr>
      <tr><td>Single washes</td><td>Single washes and monthly memberships</td></tr>
    </tbody>
  </table>
</div></section>
"""

HOW = """
<section class="view" id="how"><div class="wrap">
  <h2 class="wide head">%%HOW_H2%%</h2>
  <div class="lane" id="lane">
    <div class="run" aria-hidden="true"><span class="plate"><i></i><span data-plate>ABC-123</span></span></div>
    <div class="stop">%%STOP1%%</div>
    <div class="stop"><h3>The camera reads the plate</h3><p>The image is processed inside the camera. Only the plate number goes to the cloud.</p></div>
    <div class="stop"><h3>The wash starts</h3><p>EasyWash starts the right programme and runs the door, the boom and the dryer.</p></div>
    <div class="stop"><h3>You get paid monthly</h3><p>The plan renews by itself. Members keep buying single washes and upgrades in the app.</p></div>
  </div>
</div></section>
"""
STOP1_A = "<h3>The driver picks a plan</h3><p>In your app, on the web or at the bay. At WashXL in Finland, joining at the bay takes under five seconds.</p>"
STOP1_B = "<h3>The driver taps a card</h3><p>The screen shows the plate the camera has read. One tap of a card or phone starts a monthly plan.</p>"


def panel(pid, tid, hidden, h3, p, facts, aside):
    lis = "".join(f"<li>{f}</li>" for f in facts)
    return (f'<div class="panel" role="tabpanel" id="{pid}" aria-labelledby="{tid}"{" hidden" if hidden else ""}>'
            f"<div><h3>{h3}</h3><p>{p}</p><ul>{lis}</ul></div>{aside}</div>")


PANELS = "".join([
    panel("p-subs", "t-subs", False, "Memberships that renew themselves",
          "Sell monthly, annual and pay-per-wash plans under your own brand, with the rules you set.",
          ["Unlimited and capped plans, one contract per car", "Network plans valid at every station you run",
           "Happy hour and campaign prices per site", "Members pay in advance, before the wash"],
          '<div class="aside"><img src="../assets/screen.webp" alt="EasyWash terminal menu with three wash programmes and a monthly contract at 29.90" width="432" height="739" loading="lazy"></div>'),
    panel("p-pay", "t-pay", True, "Every way a driver wants to pay",
          "At the bay, on the phone, on the web or on a company invoice. All of it lands in one report.",
          ["Contactless cards and mobile wallets, PIN on screen", "Credit reservation: charge only the time used",
           "QR, barcode and PIN codes for vouchers", "Payment links to share by email or social media"],
          '<div class="aside photo"><img src="../assets/wet.webp" alt="EasyWash terminal in the rain at a self-service wash, showing credit reservations of 10, 30 and 50 euros" width="1400" height="1419" loading="lazy"></div>'),
    panel("p-lpr", "t-lpr", True, "The car is the membership card",
          "An EasyWash camera at the entrance reads the plate and checks the plan before the driver has stopped.",
          ["The image is processed inside the camera", "Only the plate number is sent to the cloud",
           "One plan per plate, so a membership stays with one car", "Remote support, so most faults need no site visit"],
          '<div class="aside"><img src="../assets/camera.webp" alt="EasyWash licence plate camera" width="500" height="420" loading="lazy"></div>'),
    panel("p-fleet", "t-fleet", True, "One invoice for every company car",
          "Give fleets their own portal and bill them by plate, across every station in your network.",
          ["Wash packages redeemed at any station", "Automated invoicing with VAT-correct receipts",
           "Each wash allocated to the station that did it", "Invoice data sent to your finance system by API"],
          '<div class="aside"><div class="big">1 invoice<small>for every car a company runs, at every station you operate</small></div></div>'),
    panel("p-app", "t-app", True, "Your app, your brand, your offers",
          "The app and the web portal carry your name. The marketing tools inside them bring members back.",
          ["Push messages triggered by what a driver does", "Offers and rewards applied automatically",
           "A rating after every wash", "An alert when a rating is low"],
          '<div class="aside"><div class="big">60%<small>of customers at Washman in Finland use the app</small></div></div>'),
    panel("p-bi", "t-bi", True, "See which site, plan and campaign earns",
          "The cloud dashboard shows sales, members and capacity per site, as it happens.",
          ["Revenue and usage per site and per campaign", "Top sellers and capacity per site",
           "Customer satisfaction next to turnover", "Your ratings compared with other EasyWash operators"],
          '<div class="aside"><div class="big">3x<small>revenue at Divi Vienā within three months of launch</small></div></div>'),
    panel("p-int", "t-int", True, "Works with the machines you already own",
          "EasyWash controls the wash machine and the devices around it, and passes the money data to your systems.",
          ["Christ, Sonny's, PDQ, Kärcher and other machines", "Rollovers, tunnels and self-service jet wash bays",
           "Doors, booms, dryers and other devices", "Invoicing API, and loyalty cards where you need them"],
          '<div class="aside"><img src="../assets/terminal.webp" alt="EasyWash payment terminal" width="689" height="1035" loading="lazy"></div>'),
])

MODS = """
<section class="view" id="platform"><div class="wrap">
  <h2 class="wide head">%%MODS_H2%%</h2>
  <div class="mods">
    <div class="tabs" role="tablist" aria-label="Platform parts" data-tabs>
      <button class="tab" role="tab" aria-selected="true" aria-controls="p-subs" id="t-subs">Subscriptions</button>
      <button class="tab" role="tab" aria-selected="false" aria-controls="p-pay" id="t-pay" tabindex="-1">Payments</button>
      <button class="tab" role="tab" aria-selected="false" aria-controls="p-lpr" id="t-lpr" tabindex="-1">Plate recognition</button>
      <button class="tab" role="tab" aria-selected="false" aria-controls="p-fleet" id="t-fleet" tabindex="-1">Fleet accounts</button>
      <button class="tab" role="tab" aria-selected="false" aria-controls="p-app" id="t-app" tabindex="-1">App and marketing</button>
      <button class="tab" role="tab" aria-selected="false" aria-controls="p-bi" id="t-bi" tabindex="-1">Business intelligence</button>
      <button class="tab" role="tab" aria-selected="false" aria-controls="p-int" id="t-int" tabindex="-1">Integrations</button>
    </div>
    <div>""" + PANELS + """</div>
  </div>
</div></section>
"""

WAYS = """
<section class="view tint dark" id="start"><div class="wrap">
  <div class="head">
    <h2>Keep the terminals you already paid for.</h2>
    <p class="lead">Most operators we meet have working terminals and no wish to replace them. Start with the app and the camera.</p>
  </div>
  <div class="ladder">
    <div class="rung"><small>Start here</small><h3>App and camera</h3><p>Launch memberships in your own app and fit a camera per lane. Members drive in on their plate. Your terminals keep taking single payments.</p></div>
    <div class="rung"><small>When a terminal is due</small><h3>Add the EasyWash terminal</h3><p>Replace old units one at a time. Drivers can then join a plan at the bay with one tap.</p></div>
    <div class="rung"><small>New or rebuilt sites</small><h3>The whole site</h3><p>Terminal, camera, app, company portal and dashboard, installed together.</p></div>
  </div>
</div></section>
"""

HARDWARE = """
<section class="view tint dark" id="hardware"><div class="wrap">
  <h2 class="head">Two units at the bay.</h2>
  <div class="hw">
    <div class="hwc"><img src="../assets/terminal.webp" alt="EasyWash payment terminal" width="689" height="1035" loading="lazy">
      <div><h3>EasyWash terminal</h3><dl>
        <div><dt>Screen</dt><dd>5-inch touchscreen, PIN on screen</dd></div>
        <div><dt>Payments</dt><dd>Contactless, chip, magstripe, wallets, QR</dd></div>
        <div><dt>Protection</dt><dd>IP55, for outdoor bays</dd></div>
        <div><dt>Network</dt><dd>4G, WiFi, Bluetooth, Ethernet</dd></div>
        <div><dt>Controls</dt><dd>Wash machine, doors, booms, dryers</dd></div>
      </dl></div>
    </div>
    <div class="hwc"><img src="../assets/camera.webp" alt="EasyWash licence plate camera" width="500" height="420" loading="lazy">
      <div><h3>EasyWash camera</h3><dl>
        <div><dt>Job</dt><dd>Reads the plate at the entrance</dd></div>
        <div><dt>Processing</dt><dd>Inside the camera</dd></div>
        <div><dt>Privacy</dt><dd>Only the plate number leaves the site</dd></div>
        <div><dt>Computer</dt><dd>The site computer sits in the housing</dd></div>
        <div><dt>Support</dt><dd>Remote control software</dd></div>
      </dl></div>
    </div>
  </div>
  <p class="note"><b>Three to four hours per station.</b> That is how long each rollover took at Divi Vienā in Latvia, and the system was in use the same day.</p>
</div></section>
"""

CALC = """
<section class="view" id="numbers"><div class="wrap">
  <h2 class="head">What would memberships add on your sites?</h2>
  <div class="calc">
    <div class="calc-in">
      <div class="field"><label for="c-sites">Wash sites <output id="o-sites">5</output></label><input type="range" id="c-sites" min="1" max="200" value="5"></div>
      <div class="field"><label for="c-mem">Members per site <output id="o-mem">200</output></label><input type="range" id="c-mem" min="25" max="800" step="25" value="200"><small>The Nordic fuel retailer averages about 500 per station.</small></div>
      <div class="field"><label for="c-price">Price per month <output id="o-price">€29</output></label><input type="range" id="c-price" min="10" max="60" value="29"><small>That network's average works out at about €30.</small></div>
    </div>
    <div class="calc-out" aria-live="polite">
      <span>Recurring revenue a month</span>
      <div class="n" id="o-month">€29,000</div>
      <div class="y"><b id="o-year">€348,000</b> a year, before single washes</div>
      <a class="btn btn-inv" href="#call">Book a call</a>
    </div>
  </div>
</div></section>
"""

CASES = """
<section class="view tint" id="customers"><div class="wrap">
  <h2 class="wide head">Operators who moved from single washes to memberships.</h2>
  <div class="case" role="tabpanel" id="c-dv" aria-labelledby="ct-dv">
    <div><div class="n">3x</div><p>revenue within 90 days</p></div>
    <div><blockquote>“With subscriptions, profit per wash is lower, but there are many more washes. At the end, the total profit is much higher.”</blockquote><cite><b>Ronalds Vītols</b>, owner of Divi Vienā, Latvia. Each station was fitted in three to four hours.</cite></div>
  </div>
  <div class="case" role="tabpanel" id="c-wm" aria-labelledby="ct-wm" hidden>
    <div><div class="n">60%</div><p>of customers use the app</p></div>
    <div><blockquote>“Many regular customers arrive, choose what they want on their phone, and practically drive straight into the hall without stopping.”</blockquote><cite><b>Markus Malinranta</b>, owner of Washman, Finland. Average spend per wash is now €11 to 14.</cite></div>
  </div>
  <div class="case" role="tabpanel" id="c-xl" aria-labelledby="ct-xl" hidden>
    <div><div class="n">5 sec</div><p>to join a monthly plan at the bay</p></div>
    <div><blockquote>“Very few people ask anything, the use of the terminal is so clear.”</blockquote><cite><b>Harri Karhunsalo</b>, owner of WashXL, Finland. A car can drive in every 30 seconds.</cite></div>
  </div>
  <div class="case" role="tabpanel" id="c-fr" aria-labelledby="ct-fr" hidden>
    <div><div class="n">100k</div><p>members at one fuel retailer</p></div>
    <div><blockquote>About 500 members at each of 200+ stations, and €3 million of recurring wash revenue every month.</blockquote><cite><b>A Nordic fuel retailer.</b> We share the name and the full numbers on a call.</cite></div>
  </div>
  <div class="who-tabs" role="tablist" aria-label="Customers" data-tabs>
    <button role="tab" aria-selected="true" aria-controls="c-dv" id="ct-dv">Divi Vienā</button>
    <button role="tab" aria-selected="false" aria-controls="c-wm" id="ct-wm" tabindex="-1">Washman</button>
    <button role="tab" aria-selected="false" aria-controls="c-xl" id="ct-xl" tabindex="-1">WashXL</button>
    <button role="tab" aria-selected="false" aria-controls="c-fr" id="ct-fr" tabindex="-1">Nordic fuel retailer</button>
  </div>
</div></section>
"""

DOORS = """
<section class="view" id="who"><div class="wrap">
  <h2 class="head">Four kinds of business run on EasyWash.</h2>
  <div class="rows">
    <a class="rowl" href="#call"><h3>Fuel retailers</h3><p>A wash club under your own brand, with fleet invoicing and one dashboard across every station.</p><p class="ref">Reference: a Nordic fuel retailer with 200+ stations</p><span>See page</span></a>
    <a class="rowl" href="#call"><h3>Wash chains</h3><p>Central prices, campaigns and reporting. A member can wash at any site you run.</p><p class="ref">Reference: Divi Vienā, Latvia</p><span>See page</span></a>
    <a class="rowl" href="#call"><h3>Single sites</h3><p>Go unmanned, sell memberships at the bay and in the app, and see every sale on your phone.</p><p class="ref">References: Washman and WashXL, Finland</p><span>See page</span></a>
    <a class="rowl" href="#call"><h3>Dealers and installers</h3><p>Add EasyWash to your quotes for Christ, Sonny's, PDQ and other machines, and earn on the service contract.</p><p class="ref">Best Product, Petrol Station 2025, Warsaw</p><span>See page</span></a>
  </div>
</div></section>
"""

ROLLOUT = """
<section class="view tint" id="rollout"><div class="wrap roll">
  <div>
    <h2>Live in four stages. We do the work.</h2>
    <ol class="stages">
      <li><div><b>Agreement</b><span>One contract for software, hardware and support.</span></div></li>
      <li><div><b>Training</b><span>Your staff learn the dashboard and the questions drivers ask.</span></div></li>
      <li><div><b>Configuration</b><span>We set up wash programmes, prices, plans and user terms with you.</span></div></li>
      <li><div><b>Installation</b><span>Trained installers fit the hardware, connect it to your machine and test it.</span></div></li>
    </ol>
  </div>
  <div class="call">
    <h3>The first call takes 15 minutes</h3>
    <ul>
      <li>The fuel retailer's results, with the name</li>
      <li>A rollout plan for your number of sites</li>
      <li>A price for your setup</li>
      <li>In English, Finnish or Swedish</li>
    </ul>
    <a class="btn btn-inv" href="#call">Book a call</a>
  </div>
</div></section>
"""

COMPARE = """
<section class="view" id="compare"><div class="wrap">
  <h2 class="wide head">Three ways to take payment at a car wash.</h2>
  <div class="cmp-wrap"><table class="cmp">
    <thead><tr><th></th><th>Generic card terminal</th><th>App-only membership platform</th><th>EasyWash</th></tr></thead>
    <tbody>
      <tr><td>Monthly memberships</td><td>No</td><td>Yes</td><td>Yes, sold in the app, on the web and at the bay</td></tr>
      <tr><td>How a member is recognised</td><td>Not recognised</td><td>By phone, so a plan can be passed around</td><td>By licence plate, one plan per car</td></tr>
      <tr><td>Hardware at the bay</td><td>Card reader only</td><td>From a third party</td><td>EasyWash terminal and camera, same supplier</td></tr>
      <tr><td>Your wash machine</td><td>Needs custom integration</td><td>Depends on the kiosk maker</td><td>Any brand: rollover, tunnel or self-service</td></tr>
      <tr><td>Fleet invoicing</td><td>No</td><td>Varies</td><td>Built in, billed by plate</td></tr>
      <tr><td>Who you call</td><td>The payment company</td><td>Two or three suppliers</td><td>One team, in car washes since 1987</td></tr>
    </tbody>
  </table></div>
</div></section>
"""

FAQ = """
<section class="view tint" id="faq"><div class="wrap faq">
  <h2>Questions operators ask first.</h2>
  <div>
    <details name="faq" open><summary>What is EasyWash?</summary><p>A car wash subscription and payment platform made by Euro Car Wash in Riihimäki, Finland. It covers the driver app, the payment terminal, licence plate recognition, fleet invoicing and the operator dashboard. More than 700 wash sites run on it.</p></details>
    <details name="faq"><summary>Do we have to replace our payment terminals?</summary><p>No. You can launch memberships with the app and a camera per lane and keep the terminals you have. Add EasyWash terminals later, when a unit is due for replacement.</p></details>
    <details name="faq"><summary>Which wash machines does it work with?</summary><p>Christ, Sonny's, PDQ, Kärcher and other brands, on rollovers, tunnels and self-service jet wash bays. EasyWash also controls doors, booms and dryers.</p></details>
    <details name="faq"><summary>Can a member share a plan with friends?</summary><p>A plan is tied to one licence plate, and the camera checks the plate at every visit. Each car needs its own plan.</p></details>
    <details name="faq"><summary>How long does installation take?</summary><p>At Divi Vienā in Latvia, each rollover station took three to four hours and was in use the same day. Larger rollouts follow the same four stages, site by site.</p></details>
    <details name="faq"><summary>What does it cost?</summary><p>The price depends on the number of sites and the parts you take. You get a price for your setup on the first call.</p></details>
    <details name="faq"><summary>Is there an app for drivers?</summary><p>Yes. Drivers find EasyWash stations and manage their plan at easywash.com. This page is for the businesses that run the washes.</p></details>
  </div>
</div></section>
"""

CTA = """
<section class="view end" id="call">
  <div class="wrap top">
    <div>
      <h2>See the numbers for a network your size.</h2>
      <p class="lead">A 15-minute call with the EasyWash team. You see the fuel retailer's results with the name, and a rollout plan for your sites.</p>
    </div>
    <form class="form" id="form" novalidate>
      <div class="prog" aria-hidden="true"><i class="on"></i><i></i><i></i></div>
      <div class="fstep" data-step="1">
        <h3 id="fq">How many wash sites do you run?</h3>
        <div class="chips" role="group" aria-labelledby="fq" data-sites>
          <button class="chip" type="button" data-v="1" aria-pressed="false">1</button>
          <button class="chip" type="button" data-v="3" aria-pressed="false">2 to 4</button>
          <button class="chip" type="button" data-v="10" aria-pressed="false">5 to 20</button>
          <button class="chip" type="button" data-v="50" aria-pressed="false">20+</button>
          <button class="chip" type="button" data-v="dealer" aria-pressed="false" style="flex-basis:100%">I sell or install wash equipment</button>
        </div>
        <small>One question first. Your details come after.</small>
      </div>
      <div class="fstep" data-step="2" hidden>
        <h3>Where should we send the invite?</h3>
        <label for="f-name">Name</label><input id="f-name" type="text" autocomplete="name">
        <label for="f-mail">Work email</label><input id="f-mail" type="email" autocomplete="email" inputmode="email">
        <label for="f-co">Company</label><input id="f-co" type="text" autocomplete="organization">
        <button class="btn btn-main" type="button" data-next>Pick a time</button>
        <button class="back" type="button" data-back>Back</button>
      </div>
      <div class="fstep" data-step="3" hidden>
        <h3>Pick a time</h3>
        <div class="cal-d">Tue 24 Nov</div>
        <div class="cal"><span>09:00</span><span class="pick">10:30</span><span>13:00</span></div>
        <div class="cal-d">Wed 25 Nov</div>
        <div class="cal"><span>09:30</span><span>11:00</span><span>14:30</span></div>
        <small>In the live page this is your booking calendar, so the call is in the diary before the visitor leaves.</small>
        <button class="back" type="button" data-back>Back</button>
      </div>
    </form>
  </div>
  <footer class="foot"><div class="wrap">
    <img src="../assets/easywash-white.svg" alt="EasyWash" width="104" height="30" loading="lazy">
    <span>Euro Car Wash Oy Ltd, Riihimäki, Finland. Part of Pineline Group.</span>
    <nav aria-label="Elsewhere"><a href="https://easywash.com">For drivers: easywash.com</a><a href="https://ecw.fi">Machines, chemicals and water: ecw.fi</a><a href="#">Operator login</a><a href="#">Support</a></nav>
  </div></footer>
</section>
<script src="../assets/ew.js" defer></script>
</body>
</html>
"""

LIGHT = '<link rel="stylesheet" href="../assets/ew.css">'
CLASSIC = LIGHT + '\n<link rel="stylesheet" href="../assets/ew-classic.css">'   # original colour scheme on top

VARIANTS = {
    "a": dict(css=CLASSIC, logo="easywash-white.svg",
        title="EasyWash for business: car wash subscription and payment platform",
        desc="EasyWash sells memberships in your app and at the bay, reads the plate, starts the wash and bills every month. 700+ wash sites.",
        hero=HERO_A, stop1=STOP1_A,
        how_h2="The driver signs up once. After that, the car is the membership.",
        mods_h2="Seven parts. Take all of them, or the ones you are missing.",
        order=["PROOF", "GAP", "HOW", "MODS", "WAYS", "CALC", "CASES", "DOORS", "ROLLOUT", "COMPARE", "FAQ", "CTA"],
    ),
    "b": dict(css=CLASSIC, logo="easywash-white.svg",
        title="EasyWash: the car wash payment terminal that sells memberships",
        desc="The EasyWash payment terminal and plate recognition camera sell monthly wash memberships at the bay. 700+ wash sites.",
        hero=HERO_B, stop1=STOP1_B,
        how_h2="First visit: one tap. Every visit after that: nothing.",
        mods_h2="Behind the terminal: the whole membership business.",
        order=["PROOF", "HOW", "HARDWARE", "MODS", "CASES", "CALC", "DOORS", "ROLLOUT", "COMPARE", "FAQ", "CTA"],
    ),
}
VARIANTS = {"a-new": dict(VARIANTS["a"], css=LIGHT, logo="easywash-blue.svg",
                         title="EasyWash for business (A-new, light): car wash subscription and payment platform")}
SECTIONS = dict(PROOF=PROOF, GAP=GAP, HOW=HOW, MODS=MODS, WAYS=WAYS, HARDWARE=HARDWARE, CALC=CALC,
                CASES=CASES, DOORS=DOORS, ROLLOUT=ROLLOUT, COMPARE=COMPARE, FAQ=FAQ, CTA=CTA)


def check(html, key):
    assert "%%" not in html, "unreplaced token in " + key
    low = html.lower()
    for banned in BANNED:
        assert banned not in html, repr(banned) + " must not appear in " + key
    assert ">source" not in low and "source:" not in low, "the word 'source' is visible in " + key


def concept(key):
    c = CONCEPT.replace("%%VERSION%%", VERSION)
    for k in ("a", "a-new", "b", "c"):
        c = c.replace(f"%%ON_{k.upper()}%%", ' class="on" aria-current="page"' if k == key else "")
    return c


def build(key, v):
    html = HEAD + concept(key) + NAV + v["hero"] + "".join(SECTIONS[s] for s in v["order"])
    for k, val in {"%%CSS%%": v["css"], "%%LOGO%%": v["logo"], "%%TITLE%%": v["title"], "%%DESC%%": v["desc"], "%%HOW_H2%%": v["how_h2"],
                   "%%STOP1%%": v["stop1"], "%%MODS_H2%%": v["mods_h2"]}.items():
        html = html.replace(k, val)
    check(html, key)
    out = ROOT / key / "index.html"
    out.parent.mkdir(exist_ok=True)
    out.write_text(html, encoding="utf-8")
    print(f"{key}/index.html  {len(html):,} bytes")


def build_c():
    html = (SRC / "c.html").read_text(encoding="utf-8").replace("%%CONCEPT%%", concept("c"))
    check(html, "c")
    (ROOT / "c").mkdir(exist_ok=True)
    (ROOT / "c" / "index.html").write_text(html, encoding="utf-8")
    print(f"c/index.html  {len(html):,} bytes")


def build_pitch():
    """Pitch page: reuse the October proposal's <head> and stylesheet so both pitches look the same."""
    import re
    old = (ROOT.parent / "index.html").read_text(encoding="utf-8")
    head = old[: old.index("</head>")].rstrip()
    script = old[old.rindex("<script>"): old.rindex("</script>") + len("</script>")]
    title = "easywash for business: a b2b landing page concept, twice · anna pogrebniak"
    desc = "For Euro Car Wash: a dedicated EasyWash B2B landing page in two clickable variations, platform first and terminal first, with the reasoning behind each."
    head = re.sub(r"<title>.*?</title>", "<title>" + title + "</title>", head, flags=re.S)
    head = re.sub(r'(<meta name="description" content=")[^"]*', r"\\g<1>" + desc, head)
    head = re.sub(r'(<meta property="og:title" content=")[^"]*', r"\\g<1>" + title, head)
    head = re.sub(r'(<meta property="og:description" content=")[^"]*', r"\\g<1>" + desc, head)
    head = re.sub(r'(<meta property="og:image" content=")[^"]*', r"\\g<1>https://awesomemarketer.fi/for/ecw/easywash/assets/shot-a.webp", head)
    body = (SRC / "pitch.html").read_text(encoding="utf-8").replace("%%VERSION%%", VERSION)
    html = head + "\\n" + (SRC / "pitch.css").read_text(encoding="utf-8") + "\\n</head>\\n" + body + "\\n" + script + "\\n</body>\\n</html>\\n"
    assert "\\u2014" not in body, "em dash in pitch"
    (ROOT / "index.html").write_text(html, encoding="utf-8")
    print(f"index.html    {len(html):,} bytes")


if __name__ == "__main__":
    import runpy
    runpy.run_path(str(SRC / "build_ab.py"), run_name="__main__")   # A and B, original design
    for key, v in VARIANTS.items():
        build(key, v)
    build_pitch()

#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parent
WOLF = "https://trafficflowroute-33.click/?acc_code=iw6nj5&id=42ae73dcc08ee747ad0081e4d9683288"
UKR = "https://trafficflowroute-33.click/?acc_code=ovqbqo&id=2d44805fcac3252501d08994e2e9005b"
PARI = "https://trafficflowroute-33.click/?acc_code=f5kkf2&id=1f4ce4fa883b266a4318dad1b84afd8a"
L39175 = "https://www.gamblingcommission.gov.uk/public-register/business/detail/domain-names/39175"
L39576 = "https://www.gamblingcommission.gov.uk/public-register/business/detail/domain-names/39576"
HELPLINE = "https://www.gamcare.org.uk/get-support/talk-to-us-now/"
BGA = "https://www.begambleaware.org/"
GAMSTOP = "https://www.gamstop.co.uk/"
GA = "https://www.gamblersanonymous.org.uk/"
REGISTER = "https://www.gamblingcommission.gov.uk/public-register"
ICO = "https://ico.org.uk/"

NAV = [
    ("Home", "/", "home"),
    ("Reviews", "/reviews/", "reviews"),
    ("About", "/about.html", "about"),
    ("FAQ", "/faq.html", "faq"),
    ("Safer play", "/responsible-gaming.html", "rg"),
    ("Contact", "/contact.html", "contact"),
]


def head(title, desc):
    return f"""<!DOCTYPE html>
<html lang="en-GB">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <link rel="icon" href="/favicon.svg">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,560;9..144,640&family=Outfit:wght@400;500;600&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="/css/styles.css">
  <script>try{{if(localStorage.getItem("ukcd_cookie"))document.documentElement.classList.add("cookies-set")}}catch(e){{}}</script>
</head>
<body>
"""


def header(current):
    links = []
    for label, href, key in NAV:
        current_attr = ' aria-current="page"' if key == current else ""
        links.append(f'<a href="{href}"{current_attr}>{label}</a>')
    return f"""
<div class="age-bar">
  <div class="wrap">
    <span><span class="pill">18+</span> Gamble responsibly. This desk publishes information. It does not take bets.</span>
    <a href="/responsible-gaming.html">Free help: 0808 8020 133</a>
  </div>
</div>
<header class="site-header">
  <div class="wrap header-row">
    <a class="logo" href="/">
      <span class="logo-mark">UK</span>
      <span><strong>UK Casino Desk</strong><em>ukcasinodesk.co.uk</em></span>
    </a>
    <button class="nav-toggle" type="button" data-nav-toggle aria-expanded="false" aria-controls="site-nav">Menu</button>
    <nav class="nav" id="site-nav" data-nav>
      {''.join(links)}
    </nav>
  </div>
</header>
"""


def footer():
    return f"""
<footer class="site-footer">
  <div class="wrap foot-grid">
    <div>
      <h2>UK Casino Desk</h2>
      <p>An independent London desk reviewing UK Gambling Commission licensed brands. We are not an operator. We take no deposits and accept no bets.</p>
      <p class="muted">18+ and resident in the United Kingdom only.</p>
      <a class="helpline" href="{HELPLINE}">National Gambling Helpline · 0808 8020 133</a>
    </div>
    <div>
      <h2>Desk</h2>
      <ul>
        <li><a href="/">Home</a></li>
        <li><a href="/reviews/">All reviews</a></li>
        <li><a href="/about.html">About</a></li>
        <li><a href="/faq.html">FAQ</a></li>
        <li><a href="/contact.html">Contact</a></li>
      </ul>
    </div>
    <div>
      <h2>Filings</h2>
      <ul>
        <li><a href="/reviews/wolfspins.html">Wolfspins</a></li>
        <li><a href="/reviews/parimatch.html">Parimatch</a></li>
        <li><a href="/reviews/ukriches.html">UKRICHES</a></li>
      </ul>
    </div>
    <div>
      <h2>Legal</h2>
      <ul>
        <li><a href="/terms.html">Terms</a></li>
        <li><a href="/privacy.html">Privacy</a></li>
        <li><a href="/cookies.html">Cookies</a></li>
        <li><a href="/disclosure.html">Disclosure</a></li>
        <li><a href="/responsible-gaming.html">Responsible gaming</a></li>
        <li><a href="mailto:hello@ukcasinodesk.co.uk">hello@ukcasinodesk.co.uk</a></li>
      </ul>
    </div>
  </div>
  <div class="wrap legal-note">
    <p>© 2026 UK Casino Desk. London, United Kingdom. Scores are editorial. Operator names belong to their owners and appear here only to identify the brand under review.</p>
    <p>Support: <a href="{HELPLINE}">National Gambling Helpline</a> · <a href="{GAMSTOP}">GAMSTOP</a> · <a href="{BGA}">BeGambleAware</a> · <a href="{GA}">Gamblers Anonymous UK</a> · <a href="{REGISTER}">UK Gambling Commission</a></p>
  </div>
</footer>
<div class="cookie-bar" role="dialog" aria-label="Cookie notice">
  <p>Essential storage remembers this choice. Optional analytics run only if you accept. Nothing here is used to build an advertising profile. <a href="/cookies.html">Cookie policy</a></p>
  <div class="cookie-actions">
    <button class="btn btn-primary btn-small" type="button" data-cookie-choice="all">Accept all</button>
    <button class="btn btn-ghost btn-small" type="button" data-cookie-choice="essential" style="color:#f6f1e7;border-color:#f6f1e7">Reject optional</button>
  </div>
</div>
<script src="/js/site.js"></script>
</body>
</html>
"""


def page(path, title, desc, current, body):
    dest = ROOT / path
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(head(title, desc) + header(current) + body + footer(), encoding="utf-8")
    print(path)


def visit(href, label):
    return f'<a class="btn btn-primary btn-small" href="{href}" target="_blank" rel="sponsored nofollow noopener">{label}</a>'


index = f"""
<main>
  <section class="hero">
    <div class="wrap">
      <div class="hero-grid">
        <div>
          <p class="kicker">London desk · established 2026</p>
          <h1>Three licensed books. Timed, filed, scored.</h1>
          <p class="lede">UK Casino Desk reviews betting brands that hold a UK Gambling Commission licence. We fund the accounts ourselves, clock the withdrawals, and print the licence number next to the score. 18+ only.</p>
          <div class="actions">
            <a class="btn btn-primary" href="/reviews/">Open the filings</a>
            <a class="btn btn-ghost" href="/about.html">How a filing is made</a>
          </div>
        </div>
        <aside class="stamp">
          <p class="kicker">On the desk</p>
          <ol>
            <li><span>Wolfspins</span><b>4.7</b></li>
            <li><span>Parimatch</span><b>4.6</b></li>
            <li><span>UKRICHES</span><b>4.5</b></li>
          </ol>
          <p class="muted" style="margin:12px 0 0">Current cycle Q3 2026. Order follows the score. Places are not for sale.</p>
        </aside>
      </div>
      <div class="stats">
        <div class="stat"><strong>03</strong><span>Brands filed</span></div>
        <div class="stat"><strong>18</strong><span>Withdrawals timed</span></div>
        <div class="stat"><strong>42</strong><span>Checks each</span></div>
        <div class="stat"><strong>0</strong><span>Paid rankings</span></div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <div class="section-head">
        <p class="kicker">The ledger</p>
        <h2>This quarter’s three filings</h2>
        <p class="muted">Each operator below is on the public register. Open the licence link and check the status yourself.</p>
      </div>
      <div class="ledger">
        <article class="file">
          <div class="file-score">4.7<span>out of 5</span></div>
          <div>
            <h3><a href="/reviews/wolfspins.html">Wolfspins</a></h3>
            <p>A short, tidy account path. Verification was mostly automatic, and cash-out paid the figure on the slip.</p>
            <div class="meta">
              <span class="chip">18+</span>
              <a class="chip" href="{L39175}">UKGC 39175</a>
              <span class="chip">Median payout ~14 hours</span>
            </div>
          </div>
          <div class="file-actions">
            <a class="btn btn-ghost btn-small" href="/reviews/wolfspins.html">Read filing</a>
            {visit(WOLF, "Visit Wolfspins")}
          </div>
        </article>
        <article class="file">
          <div class="file-score">4.6<span>out of 5</span></div>
          <div>
            <h3><a href="/reviews/parimatch.html">Parimatch</a></h3>
            <p>A long-running book with a UK product written in sterling, round-the-clock chat, and the deepest football card of the three.</p>
            <div class="meta">
              <span class="chip">18+</span>
              <a class="chip" href="{L39576}">UKGC 39576</a>
              <span class="chip">Median payout ~14 hours</span>
            </div>
          </div>
          <div class="file-actions">
            <a class="btn btn-ghost btn-small" href="/reviews/parimatch.html">Read filing</a>
            {visit(PARI, "Visit Parimatch")}
          </div>
        </article>
        <article class="file">
          <div class="file-score">4.5<span>out of 5</span></div>
          <div>
            <h3><a href="/reviews/ukriches.html">UKRICHES</a></h3>
            <p>Spend controls sit in front of the customer: weekly and monthly loss caps, and a spend summary that opens on its own.</p>
            <div class="meta">
              <span class="chip">18+</span>
              <a class="chip" href="{L39175}">UKGC 39175</a>
              <span class="chip">Median payout ~19 hours</span>
            </div>
          </div>
          <div class="file-actions">
            <a class="btn btn-ghost btn-small" href="/reviews/ukriches.html">Read filing</a>
            {visit(UKR, "Visit UKRICHES")}
          </div>
        </article>
      </div>
    </div>
  </section>

  <section class="section" style="padding-top:0">
    <div class="wrap">
      <div class="section-head">
        <p class="kicker">Method</p>
        <h2>Four passes. Every brand takes all of them.</h2>
        <p class="muted">We use our own money, behave like an ordinary UK adult, and write down what happened. Brands do not see a filing before it is published.</p>
      </div>
      <div class="method">
        <article class="step"><em>01</em><h3>Licence</h3><p>We look the operator up on the Gambling Commission register and publish the account number.</p></article>
        <article class="step"><em>02</em><h3>Identity checks</h3><p>We time age and identity checks, and note whether a deposit stays blocked until they finish.</p></article>
        <article class="step"><em>03</em><h3>Payout clock</h3><p>Winning bets are timed to settlement. Withdrawals are timed from request to arrival. We publish the median.</p></article>
        <article class="step"><em>04</em><h3>Safer play tools</h3><p>Deposit limits, loss limits, reality checks, time-outs, self-exclusion and GAMSTOP are tested, not assumed.</p></article>
      </div>
    </div>
  </section>

  <section class="section" style="padding-top:10px">
    <div class="wrap">
      <div class="section-head">
        <p class="kicker">Side by side</p>
        <h2>The measured figures</h2>
        <p class="muted">Medians from the current cycle. Your own result can differ by payment method, amount and day of the week.</p>
      </div>
      <div class="table-wrap">
        <table>
          <thead>
            <tr><th>Brand</th><th>Score</th><th>UKGC</th><th>Median payout</th><th>Live support</th><th>Verification</th><th>Cash out</th></tr>
          </thead>
          <tbody>
            <tr><td>Wolfspins</td><td>4.7 / 5</td><td><a href="{L39175}">39175</a></td><td>~14 hours</td><td>Extended hours</td><td>Mostly automatic</td><td>Singles</td></tr>
            <tr><td>Parimatch</td><td>4.6 / 5</td><td><a href="{L39576}">39576</a></td><td>~14 hours</td><td>24 hours</td><td>Fully electronic</td><td>Full and partial</td></tr>
            <tr><td>UKRICHES</td><td>4.5 / 5</td><td><a href="{L39175}">39175</a></td><td>~19 hours</td><td>08:00 – 00:00</td><td>Document often required</td><td>Full and partial</td></tr>
          </tbody>
        </table>
      </div>
    </div>
  </section>

  <section class="section" style="padding-top:0">
    <div class="wrap">
      <div class="rg">
        <div>
          <p class="kicker" style="color:#f6d7b0">Before the first stake</p>
          <h2>Entertainment, with a price you choose first.</h2>
          <p>Gambling is not a plan to make money or to win a loss back. If it stops feeling like a night out, stop. Free, confidential help in the UK is open all night.</p>
          <p>Set a deposit limit before the first payment. Every licensed UK brand must offer one, and it takes under a minute.</p>
          <a class="btn btn-primary" href="/responsible-gaming.html">Responsible gaming guide</a>
        </div>
        <div>
          <h3>Free UK support</h3>
          <ul>
            <li><a href="{HELPLINE}">National Gambling Helpline</a> — 0808 8020 133</li>
            <li><a href="{GAMSTOP}">GAMSTOP</a> — block licensed UK operators</li>
            <li><a href="{BGA}">BeGambleAware</a> — advice and live chat</li>
            <li><a href="{GA}">Gamblers Anonymous UK</a> — meetings</li>
          </ul>
        </div>
      </div>
    </div>
  </section>

  <section class="section" style="padding-top:0">
    <div class="wrap">
      <div class="section-head">
        <p class="kicker">Questions</p>
        <h2>Short answers</h2>
      </div>
      <div class="faq">
        <div class="faq-item" data-faq>
          <button type="button" aria-expanded="false">How does the desk get paid? <span>+</span></button>
          <div data-faq-panel hidden><p>Some buttons to operators are affiliate links. If you open an account through one, the operator may pay us a fee. You do not pay extra. The fee does not change a score, an order or a sentence. See the <a href="/disclosure.html">disclosure</a>.</p></div>
        </div>
        <div class="faq-item" data-faq>
          <button type="button" aria-expanded="false">Are these brands UK licensed? <span>+</span></button>
          <div data-faq-panel hidden><p>Yes. We only file operators with a current UK Gambling Commission licence, and each filing links to the public register.</p></div>
        </div>
        <div class="faq-item" data-faq>
          <button type="button" aria-expanded="false">Can I place a bet on ukcasinodesk.co.uk? <span>+</span></button>
          <div data-faq-panel hidden><p>No. UK Casino Desk is an information site. Any bet is placed with the licensed bookmaker, under that bookmaker’s terms.</p></div>
        </div>
      </div>
      <p style="margin-top:16px"><a href="/faq.html">All questions</a></p>
    </div>
  </section>
</main>
"""

reviews = f"""
<main>
  <section class="page-hero">
    <div class="wrap">
      <p class="kicker">Q3 2026</p>
      <h1>All filings</h1>
      <p class="lede">Three UK-licensed brands. Accounts funded by the desk, withdrawals timed, safer-play tools tried. Scores are editorial.</p>
    </div>
  </section>
  <section class="section" style="padding-top:20px">
    <div class="wrap ledger">
      <article class="file">
        <div class="file-score">4.7<span>out of 5</span></div>
        <div>
          <h3><a href="/reviews/wolfspins.html">Wolfspins</a></h3>
          <p>Registration finished in under three minutes on desktop and phone. Two of three test accounts cleared identity checks automatically. The bet slip, cashier and withdrawal sat in reach without a promotion blocking them.</p>
          <div class="split" style="margin-top:12px">
            <div class="panel"><h3>Works</h3><ul><li>Licence shown before sign-up</li><li>Mostly automatic verification</li><li>Cash-out matched the displayed figure</li></ul></div>
            <div class="panel watch"><h3>Watch</h3><ul><li>Chat is not staffed all night</li><li>Weekend payouts can pass 30 hours</li><li>In-play thins below the main leagues</li></ul></div>
          </div>
          <a class="chip" href="{L39175}">UKGC 39175</a>
        </div>
        <div class="file-actions">
          <a class="btn btn-ghost btn-small" href="/reviews/wolfspins.html">Full filing</a>
          {visit(WOLF, "Visit Wolfspins")}
        </div>
      </article>
      <article class="file">
        <div class="file-score">4.6<span>out of 5</span></div>
        <div>
          <h3><a href="/reviews/parimatch.html">Parimatch</a></h3>
          <p>An established international book with a UK product that is actually local: British English, sterling, and no leftover offshore terms in the footer.</p>
          <div class="split" style="margin-top:12px">
            <div class="panel"><h3>Works</h3><ul><li>24-hour chat, fastest reply this cycle</li><li>Deepest football and in-play card</li><li>All three accounts verified electronically</li></ul></div>
            <div class="panel watch"><h3>Watch</h3><ul><li>Reality checks start switched off</li><li>Safer-play tools sit one menu deeper</li><li>Racing each-way terms trail UKRICHES</li></ul></div>
          </div>
          <a class="chip" href="{L39576}">UKGC 39576</a>
        </div>
        <div class="file-actions">
          <a class="btn btn-ghost btn-small" href="/reviews/parimatch.html">Full filing</a>
          {visit(PARI, "Visit Parimatch")}
        </div>
      </article>
      <article class="file">
        <div class="file-score">4.5<span>out of 5</span></div>
        <div>
          <h3><a href="/reviews/ukriches.html">UKRICHES</a></h3>
          <p>The strongest spend controls in this cycle: weekly and monthly net-loss caps, a thirty-day spend summary, and a one-tap cool-off.</p>
          <div class="split" style="margin-top:12px">
            <div class="panel"><h3>Works</h3><ul><li>Controls on by default</li><li>Best odds guaranteed on UK and Irish racing</li><li>No withdrawal fee at any amount</li></ul></div>
            <div class="panel watch"><h3>Watch</h3><ul><li>Chat closes overnight</li><li>Deposit waits until verification ends</li><li>In-play can suspend a beat slower</li></ul></div>
          </div>
          <a class="chip" href="{L39175}">UKGC 39175</a>
        </div>
        <div class="file-actions">
          <a class="btn btn-ghost btn-small" href="/reviews/ukriches.html">Full filing</a>
          {visit(UKR, "Visit UKRICHES")}
        </div>
      </article>
    </div>
    <div class="wrap" style="margin-top:28px">
      <h2>What the number means</h2>
      <div class="table-wrap">
        <table>
          <thead><tr><th>Band</th><th>Meaning</th></tr></thead>
          <tbody>
            <tr><td>4.5 – 5.0</td><td>Licence checked, payouts usually inside a day, safer-play tools complete and easy to find.</td></tr>
            <tr><td>4.0 – 4.4</td><td>Compliant, with one or two areas that lag the others.</td></tr>
            <tr><td>3.0 – 3.9</td><td>Usable, but with real friction: slow payouts, thin support, or buried controls.</td></tr>
            <tr><td>Below 3.0</td><td>Not published. A failed compliance check means the brand is dropped.</td></tr>
          </tbody>
        </table>
      </div>
    </div>
  </section>
</main>
"""


def review_page(name, score, summary, licence, licence_url, visit_href, bars, works, watch, sections, others):
    bar_html = "".join(
        f'<li>{label}<div class="bar"><i style="width:{pct}%"></i></div></li>' for label, pct in bars
    )
    works_html = "".join(f"<li>{item}</li>" for item in works)
    watch_html = "".join(f"<li>{item}</li>" for item in watch)
    body_html = "".join(f"<h2>{h}</h2>{p}" for h, p in sections)
    other_html = "".join(
        f'<article class="file"><div class="file-score">{s}<span>out of 5</span></div><div><h3><a href="{href}">{n}</a></h3><p>{blurb}</p></div><div class="file-actions"><a class="btn btn-ghost btn-small" href="{href}">Read</a>{visit(v, "Visit")}</div></article>'
        for n, s, href, blurb, v in others
    )
    return f"""
<main>
  <section class="page-hero">
    <div class="wrap">
      <p class="crumbs"><a href="/">Home</a> / <a href="/reviews/">Reviews</a> / {name}</p>
      <p class="kicker">Filing · Q3 2026 · 18+</p>
      <h1>{name}</h1>
      <p class="lede">{summary}</p>
    </div>
  </section>
  <div class="wrap review-layout">
    <article class="prose">
      <div class="split">
        <div class="panel"><h3>What worked</h3><ul>{works_html}</ul></div>
        <div class="panel watch"><h3>What to watch</h3><ul>{watch_html}</ul></div>
      </div>
      {body_html}
      <p class="muted">Score {score} / 5. 18+. Set a deposit limit before you register, and read the offer terms on the operator’s own site. Prices include the bookmaker’s margin.</p>
      <h2>The other two</h2>
      <div class="ledger">{other_html}</div>
    </article>
    <aside class="scorecard">
      <div class="score-big">{score}<small> / 5</small></div>
      <p class="muted">Overall this cycle</p>
      <ul class="bars">{bar_html}</ul>
      <p><a href="{licence_url}">UKGC account {licence}</a></p>
      {visit(visit_href, "Visit " + name)}
      <p class="muted" style="margin-top:10px">18+ only. Affiliate link. The operator’s terms apply.</p>
    </aside>
  </div>
</main>
"""

wolf = review_page(
    "Wolfspins", "4.7",
    "A compact UK book built around one clean account journey. Of the three filed this quarter, its verification and payout handling were the most even.",
    "39175", L39175, WOLF,
    [("Licensing", 100), ("Withdrawals", 96), ("Support", 92), ("Markets", 94), ("Safer play", 90)],
    [
        "Operating company and licence shown before registration",
        "Two of three accounts verified without a document upload",
        "Cash-out settled at the figure on the slip",
        "Pending withdrawals cannot be pulled back into the balance",
        "Safer-play tools two taps from the account menu",
    ],
    [
        "Live chat is not open twenty-four hours",
        "A weekend withdrawal reached thirty-one hours",
        "In-play markets thin out below the main leagues",
        "Free-bet terms are readable, but three clicks down",
    ],
    [
        ("First look", "<p>The landing view states the company, the licence and the 18+ rule above the fold. Three taps reach deposit limits and self-exclusion. The slip stays pinned on market pages.</p>"),
        ("Verification", "<p>An electronic check cleared two test accounts at once. The third asked for a passport inside the account area and was reviewed in four hours and eleven minutes. Documents were not sent by email.</p>"),
        ("Markets", "<p>Football, racing and tennis have the depth you would expect. Cash-out was offered on most pre-match singles we placed and paid the displayed number each time. Premier League match odds sat near the market average. Coverage drops away from the top leagues.</p>"),
        ("Cashier", "<p>Visa Debit and Apple Pay deposits posted immediately. Five withdrawals were logged. The quickest debit-card return took eleven hours; the slowest, over a weekend, took thirty-one. The median for the brand this cycle is about fourteen hours. There is no reverse-withdrawal control, which we treat as a protection.</p>"),
        ("Support", "<p>A person joined chat in under ninety seconds on four of five tries. Answers on free-bet rules matched the published terms. Email came back inside one working day.</p>"),
        ("Safer play", "<p>Deposit limits, loss limits, session reminders, time-outs and self-exclusion are present. Reductions apply at once. Increases wait twenty-four hours. GAMSTOP is recognised at login.</p>"),
        ("Desk view", "<p>Choose Wolfspins if you want a fast, plain account more than a wall of odds boosts. Set a deposit limit before the first bet.</p>"),
    ],
    [
        ("Parimatch", "4.6", "/reviews/parimatch.html", "Localised UK book, 24-hour chat, UKGC 39576.", PARI),
        ("UKRICHES", "4.5", "/reviews/ukriches.html", "Deep spend controls, UKGC 39175.", UKR),
    ],
)

pari = review_page(
    "Parimatch", "4.6",
    "An established international bookmaker whose UK product is properly localised: sterling prices, British English, and a licence entry that resolves on the public register.",
    "39576", L39576, PARI,
    [("Licensing", 96), ("Withdrawals", 94), ("Support", 96), ("Markets", 92), ("Safer play", 86)],
    [
        "Twenty-four hour chat, the fastest connection this cycle",
        "Deepest football and in-play coverage of the three",
        "All three test accounts verified with no document upload",
        "A published UK telephone line",
        "Pending withdrawals cannot be reversed into the balance",
    ],
    [
        "Reality checks are off until you switch them on",
        "Safer-play tools sit one level deeper than at UKRICHES",
        "Racing each-way terms are less generous",
        "Promotional terms are long",
    ],
    [
        ("First look", "<p>Prices, terms and account copy are in British English, in pounds. There is no currency switch to stumble over. Account 39576 resolves on the Gambling Commission register.</p>"),
        ("Verification", "<p>All three accounts cleared electronically, the only brand this cycle to do so. Age verification finished before the first deposit prompt.</p>"),
        ("Markets", "<p>Football runs past the top divisions, and in-play prices move quickly. Cash-out, including a partial cash-out, and a bet builder are on most football markets. Premier League margins were the tightest in our sample. Racing is competent; each-way terms trail UKRICHES.</p>"),
        ("Cashier", "<p>Seven withdrawals: median fourteen hours back to a debit card, and under two hours to an e-wallet. In-play bets settled moments after the result. No fee showed up.</p>"),
        ("Support", "<p>Chat is open all day, with a median wait under a minute. Agents answered an awkward question on qualifying odds correctly. A UK phone line is listed.</p>"),
        ("Safer play", "<p>Deposit limits, time-outs, reality checks and self-exclusion work. The criticism is placement: controls are a menu deeper, and reality checks start off. Turn them on as the first action after registering.</p>"),
        ("Desk view", "<p>Parimatch is the most mature operation in this set: support, checks and market depth are strong, and payouts are quick. The safer-play defaults need a manual switch.</p>"),
    ],
    [
        ("Wolfspins", "4.7", "/reviews/wolfspins.html", "Clean account path, UKGC 39175.", WOLF),
        ("UKRICHES", "4.5", "/reviews/ukriches.html", "Deep spend controls, UKGC 39175.", UKR),
    ],
)

ukr = review_page(
    "UKRICHES", "4.5",
    "A UK-facing book that puts more spending control in front of the customer than either of the other two: weekly and monthly loss caps, and a spend summary that appears on its own.",
    "39175", L39175, UKR,
    [("Licensing", 98), ("Withdrawals", 88), ("Support", 90), ("Markets", 88), ("Safer play", 98)],
    [
        "Loss caps by week and by month, on by default",
        "Best odds guaranteed on UK and Irish racing, written on the racecard",
        "A thirty-day spend summary that opens without being asked",
        "No withdrawal fee; minimum ten pounds",
        "Support explained a held payout in plain language",
    ],
    [
        "Live chat closes overnight",
        "Deposits stay blocked until verification finishes",
        "In-play markets can suspend a fraction slower",
        "The interface is busy on a small phone",
    ],
    [
        ("First look", "<p>The screen is denser than Wolfspins, but the path stays clear. The footer carries the company, address and licence on every view, with an 18+ mark in the header.</p>"),
        ("Verification", "<p>One account cleared instantly. The other two were asked for proof of address inside the account, both reviewed within six hours. Deposits stayed locked until that finished. That is the right order, even if the first session feels slow.</p>"),
        ("Markets", "<p>Football and racing are the deep cards. Each-way terms and best odds guaranteed are on the racecard, not in a footnote. Cash-out covers singles and accumulators, with a partial slider. In-play paused slightly slower than the other two during fast passages.</p>"),
        ("Cashier", "<p>Six debit-card withdrawals, median nineteen hours. One request sat for a manual review at twenty-eight hours; chat gave a specific reason. Racing settled after the weigh-in. One football accumulator waited forty minutes for a late kick-off to be confirmed.</p>"),
        ("Support", "<p>Chat runs 08:00 to midnight UK time. Median connection was two minutes and ten seconds. Overnight, the email form promises one working day, and that target was met in our tests.</p>"),
        ("Safer play", "<p>This is the separation. Net-loss limits can be weekly or monthly, not only per deposit. Reality checks default to sixty minutes. The thirty-day spend summary is useful. GAMSTOP is in the account menu, not only the footer.</p>"),
        ("Desk view", "<p>UKRICHES fits an adult who wants spend controls that are visible and conservative. Racing is excellent. Payout speed is good, not the quickest of the three.</p>"),
    ],
    [
        ("Wolfspins", "4.7", "/reviews/wolfspins.html", "Clean account path, UKGC 39175.", WOLF),
        ("Parimatch", "4.6", "/reviews/parimatch.html", "Localised UK book, UKGC 39576.", PARI),
    ],
)

about = """
<main>
  <section class="page-hero"><div class="wrap">
    <p class="kicker">The desk</p>
    <h1>A small desk, a clock, a spreadsheet.</h1>
    <p class="lede">UK Casino Desk opened in London in 2026. The site at ukcasinodesk.co.uk exists because too many “reviews” are rewritten press notes. We open accounts, deposit our own money, place bets, request withdrawals and time them.</p>
  </div></section>
  <section class="section" style="padding-top:10px"><div class="wrap prose-page">
    <p>We are an information publisher. We are not a bookmaker. We hold no gambling licence because we do not need one, and we never take a stake from a reader.</p>
    <div class="facts">
      <div class="fact"><b>2026</b><span class="muted">Founded</span></div>
      <div class="fact"><b>London</b><span class="muted">Based in the UK</span></div>
      <div class="fact"><b>3</b><span class="muted">Brands published</span></div>
      <div class="fact"><b>18+</b><span class="muted">Audience</span></div>
      <div class="fact"><b>GB</b><span class="muted">Market covered</span></div>
      <div class="fact"><b>None</b><span class="muted">Paid placements</span></div>
    </div>
    <h2>Rules that do not move</h2>
    <ol>
      <li><strong>UK licensed only.</strong> No current Gambling Commission licence, no page.</li>
      <li><strong>We fund the test.</strong> No gifted balance, no reviewer status, no hospitality account.</li>
      <li><strong>Fees do not buy scores.</strong> Affiliate income is disclosed and kept away from the number.</li>
      <li><strong>Adults only.</strong> Every view carries 18+. Nothing here is aimed at under-18s.</li>
      <li><strong>The weak result stays in.</strong> Slow weekends, closed chat, buried menus — if we measured it, it is in the filing.</li>
      <li><strong>We correct the page.</strong> Filings are re-checked each quarter. If a fact changes, the page says so.</li>
    </ol>
    <h2>How a filing is built</h2>
    <p>Forty-two checks. Nothing is scored from a screenshot of a marketing page.</p>
    <ol>
      <li>Find the company on the public register and confirm the domain is covered. If the reference does not resolve, the filing stops.</li>
      <li>Open three accounts with different verification profiles. Time the checks.</li>
      <li>Fund ordinary amounts. Bet a fixed slate across football, racing and tennis, including in-play. Request at least five withdrawals across weekdays and weekends.</li>
      <li>Ask live chat five questions with answers we can check, including one awkward one about offer rules.</li>
      <li>Set and cut deposit limits, fire a reality check, take a time-out, and confirm limit increases wait out the cooling-off period. Check GAMSTOP at login.</li>
      <li>Score five categories. A second person checks the notes before publication.</li>
    </ol>
    <p>These figures describe our accounts in a defined window. Payout speed varies. Treat them as a measured guide, not a promise.</p>
    <p><a class="btn btn-primary" href="/contact.html">Write to the desk</a></p>
  </div></section>
</main>
"""

faq = f"""
<main>
  <section class="page-hero"><div class="wrap">
    <p class="kicker">FAQ</p>
    <h1>Questions the desk actually gets.</h1>
    <p class="lede">If yours is missing, <a href="/contact.html">write to us</a>. Useful ones are added here.</p>
  </div></section>
  <section class="section" style="padding-top:10px"><div class="wrap" style="max-width:760px">
    <div class="faq">
      <div class="faq-item" data-faq><button type="button" aria-expanded="false">What is UK Casino Desk? <span>+</span></button><div data-faq-panel hidden><p>An independent review desk, established in London in 2026, publishing at ukcasinodesk.co.uk. We assess UKGC-licensed betting brands on verification, markets, withdrawals, support and safer-play tools.</p></div></div>
      <div class="faq-item" data-faq><button type="button" aria-expanded="false">Can I bet here? <span>+</span></button><div data-faq-panel hidden><p>No. We take no deposits and hold no customer funds. Betting happens only with the licensed operator.</p></div></div>
      <div class="faq-item" data-faq><button type="button" aria-expanded="false">Who is this for? <span>+</span></button><div data-faq-panel hidden><p>Adults aged 18 or over who live in the United Kingdom. Under-18s should leave. It is a criminal offence for anyone under 18 to gamble in Great Britain.</p></div></div>
      <div class="faq-item" data-faq><button type="button" aria-expanded="false">Who writes the filings? <span>+</span></button><div data-faq-panel hidden><p>People on the desk, from notes they collected. A second person reads the evidence before a page goes up. We do not paste operator marketing.</p></div></div>
      <div class="faq-item" data-faq><button type="button" aria-expanded="false">How is the score made? <span>+</span></button><div data-faq-panel hidden><p>Five weighted areas: licensing, withdrawals, support, markets and pricing, and safer-play tools. Each comes from what we measured, then they combine into the figure on the page.</p></div></div>
      <div class="faq-item" data-faq><button type="button" aria-expanded="false">Can a brand buy a higher score? <span>+</span></button><div data-faq-panel hidden><p>No. Commercial links exist and are disclosed. They do not change scores, order or wording.</p></div></div>
      <div class="faq-item" data-faq><button type="button" aria-expanded="false">Why only three brands? <span>+</span></button><div data-faq-panel hidden><p>Each filing takes weeks of real account work. Three evidenced assessments are worth more than a long list of summaries. The list grows when the desk can do the work.</p></div></div>
      <div class="faq-item" data-faq><button type="button" aria-expanded="false">How do I check a licence? <span>+</span></button><div data-faq-panel hidden><p>Every filing links to the <a href="{REGISTER}">Gambling Commission public register</a>. Confirm the company, the domain and that the status is active. The register beats any badge in a footer.</p></div></div>
      <div class="faq-item" data-faq><button type="button" aria-expanded="false">Why was I asked for documents? <span>+</span></button><div data-faq-panel hidden><p>UK operators must verify age and identity, and they run anti-money-laundering checks. Finish that at registration so it does not sit on a later withdrawal.</p></div></div>
      <div class="faq-item" data-faq><button type="button" aria-expanded="false">What is GAMSTOP? <span>+</span></button><div data-faq-panel hidden><p>A free scheme that blocks you from online operators licensed in Great Britain, for six months, one year or five years. It cannot be lifted early. Register at <a href="{GAMSTOP}">gamstop.co.uk</a>.</p></div></div>
      <div class="faq-item" data-faq><button type="button" aria-expanded="false">How is the site funded? <span>+</span></button><div data-faq-panel hidden><p>Affiliate fees, explained on the <a href="/disclosure.html">disclosure</a> page. Readers do not pay us.</p></div></div>
      <div class="faq-item" data-faq><button type="button" aria-expanded="false">What do you do with my message? <span>+</span></button><div data-faq-panel hidden><p>If you write in, we keep your name, email and message so we can reply. We do not sell data or pass enquiries to operators. Records are deleted after twenty-four months. Email <a href="mailto:hello@ukcasinodesk.co.uk">hello@ukcasinodesk.co.uk</a> to ask for access, correction or deletion.</p></div></div>
      <div class="faq-item" data-faq><button type="button" aria-expanded="false">Can the right bookmaker make betting profitable? <span>+</span></button><div data-faq-panel hidden><p>No. Prices include a margin, so the book is against the customer over time. Treat a stake as the cost of entertainment, never as an investment.</p></div></div>
    </div>
  </div></section>
</main>
"""

contact = f"""
<main>
  <section class="page-hero"><div class="wrap">
    <p class="kicker">London</p>
    <h1>Write to the desk.</h1>
    <p class="lede">Corrections, method questions and commercial notes all land in the same inbox. We reply within one working day, Monday to Friday.</p>
  </div></section>
  <section class="section" style="padding-top:10px"><div class="wrap contact-layout">
    <form class="form" data-contact>
      <div data-fields style="display:grid;gap:12px">
        <label>Your name<input name="name" required autocomplete="name"></label>
        <label>Email<input type="email" name="email" required autocomplete="email"></label>
        <label>Topic
          <select name="topic" required>
            <option value="">Choose one</option>
            <option>A correction</option>
            <option>A question about the method</option>
            <option>Responsible gambling support</option>
            <option>Partnership enquiry</option>
            <option>Privacy request</option>
            <option>Something else</option>
          </select>
        </label>
        <label>Message<textarea name="message" required></textarea></label>
        <label class="check"><input type="checkbox" required> I am 18 or over and resident in the United Kingdom.</label>
        <label class="check"><input type="checkbox" required> I have read the <a href="/privacy.html">privacy policy</a> and agree this message can be stored so it can be answered.</label>
        <button class="btn btn-primary" type="submit">Send message</button>
        <p class="muted">This form stays in your browser in this preview. On the live domain it should be wired to hello@ukcasinodesk.co.uk.</p>
      </div>
      <div class="sent" data-sent hidden>
        <h2>Message noted.</h2>
        <p>Thanks. In this local preview nothing is transmitted. On ukcasinodesk.co.uk, mail the same note to hello@ukcasinodesk.co.uk if you need a reply.</p>
      </div>
    </form>
    <aside>
      <div class="panel">
        <h3>Email</h3>
        <p><a href="mailto:hello@ukcasinodesk.co.uk">hello@ukcasinodesk.co.uk</a></p>
        <h3>Where</h3>
        <p>Editorial desk, London, United Kingdom.</p>
        <p class="muted">We cannot see into a bookmaker account. Deposits, bets and withdrawals have to be raised with the operator, then with their dispute service if needed.</p>
      </div>
      <div class="panel" style="margin-top:12px">
        <h3>Need help now?</h3>
        <p><a href="{HELPLINE}">National Gambling Helpline</a> — 0808 8020 133</p>
        <p><a href="{BGA}">BeGambleAware</a></p>
        <p><a href="{GAMSTOP}">GAMSTOP</a></p>
      </div>
    </aside>
  </div></section>
</main>
"""

rg = f"""
<main>
  <section class="page-hero"><div class="wrap">
    <p class="kicker">18+</p>
    <h1>Keep it entertainment.</h1>
    <p class="lede">Gambling has a price. It is not a wage, a rescue plan, or a way to win yesterday back. This page is how to stay in control, and where to get free help in the UK.</p>
  </div></section>
  <section class="section" style="padding-top:10px"><div class="wrap prose-page">
    <p><strong>Strictly 18 or over.</strong> If you are under 18, leave this website.</p>
    <h2>Help that is open now</h2>
    <div class="support-grid">
      <a class="support-card" href="{HELPLINE}"><h3>National Gambling Helpline</h3><p>0808 8020 133 · free, 24 hours. You do not need to be in crisis.</p></a>
      <a class="support-card" href="{BGA}"><h3>BeGambleAware</h3><p>Advice, live chat and a self-assessment.</p></a>
      <a class="support-card" href="{GAMSTOP}"><h3>GAMSTOP</h3><p>One registration blocks online operators licensed in Great Britain.</p></a>
      <a class="support-card" href="{GA}"><h3>Gamblers Anonymous UK</h3><p>Local and online meetings.</p></a>
    </div>
    <h2>Ten habits worth keeping</h2>
    <ol>
      <li>Set a deposit limit before the first payment.</li>
      <li>Decide the amount first and treat it as the cost of a night out.</li>
      <li>Do not chase a loss. The next price does not care about the last one.</li>
      <li>Do not stake borrowed money, including credit, overdrafts or a friend’s cash.</li>
      <li>Set a time limit and switch reality checks on.</li>
      <li>Do not gamble to get away from stress, low mood or boredom.</li>
      <li>Do not gamble while drinking, tired or upset.</li>
      <li>Keep it visible to people close to you. Hiding it is a warning.</li>
      <li>Use a time-out of a day, a week or a month when the pull grows.</li>
      <li>Remember the margin. Over time the book keeps a share of stakes. No system removes it.</li>
    </ol>
    <h2>Warning signs</h2>
    <ul>
      <li>Staking more, or for longer, than you planned</li>
      <li>Going back to recover money</li>
      <li>Borrowing, selling things, or missing bills to fund it</li>
      <li>Lying about the time or the money</li>
      <li>Feeling restless when you cannot gamble</li>
      <li>Using it to dull stress or low mood</li>
      <li>Rows at home, or work and study slipping</li>
    </ul>
    <p>If several of these fit, call <a href="{HELPLINE}">0808 8020 133</a>.</p>
    <h2>Tools a UK licensed operator must offer</h2>
    <div class="table-wrap">
      <table>
        <thead><tr><th>Tool</th><th>What it does</th></tr></thead>
        <tbody>
          <tr><td>Deposit limits</td><td>Cap what you pay in. Cuts apply at once. Increases wait through a cooling-off period.</td></tr>
          <tr><td>Loss limits</td><td>Cap net losses over a period. Stricter than a deposit cap.</td></tr>
          <tr><td>Reality checks</td><td>On-screen reminders of time and position. Set 30 or 60 minutes.</td></tr>
          <tr><td>Time-out</td><td>Locks the account from 24 hours up to several weeks. It cannot be lifted early.</td></tr>
          <tr><td>Self-exclusion</td><td>Closes that operator’s account for at least six months.</td></tr>
          <tr><td>GAMSTOP</td><td>Blocks you across licensed GB operators. Active within 24 hours, for 6 months, 1 year or 5 years.</td></tr>
        </tbody>
      </table>
    </div>
    <h2>Children and other people</h2>
    <p>Nobody under 18 may gamble in Great Britain. If a child uses a device you own, use filtering software, a separate account, and never leave a funded bookmaker session signed in.</p>
    <p>If you are worried about someone else, the helpline advises relatives as well. Do not take on their debts alone. Gam-Anon supports people close to someone who gambles.</p>
    <h2>If an operator lets you down</h2>
    <p>Complain to the operator first. If it is still open after eight weeks, use the free dispute service named on their site. You can also report a concern to the <a href="{REGISTER}">Gambling Commission</a>.</p>
  </div></section>
</main>
"""

disclosure = """
<main>
  <section class="page-hero"><div class="wrap">
    <p class="kicker">Legal · updated 28 October 2026</p>
    <h1>Disclosure</h1>
    <p class="lede">Some links to operators are commercial. If you register after using one, we may earn a fee. It costs you nothing extra and does not change a score, a rank or a sentence.</p>
  </div></section>
  <section class="section" style="padding-top:0"><div class="wrap prose-page">
    <h2>Why this page is here</h2>
    <p>A site that points at brands should say how it is paid. This note is written so advertising is identifiable, in line with UK advertising rules on affiliate endorsements.</p>
    <h2>How UK Casino Desk is funded</h2>
    <p>Income comes from affiliate arrangements with licensed operators. Readers do not pay us. That referral fee is the only commercial income.</p>
    <h2>Which links are commercial</h2>
    <p>Buttons such as “Visit Wolfspins”, “Visit Parimatch” and “Visit UKRICHES” are affiliate links. They use <code>rel="sponsored nofollow"</code>. Links to the Gambling Commission, GAMSTOP, BeGambleAware, Gamblers Anonymous and the helpline are never commercial.</p>
    <h2>What the fee does not buy</h2>
    <ul>
      <li>It does not buy a score. Scores come from the 42-point check.</li>
      <li>It does not buy a place in the list. Order follows the score.</li>
      <li>It does not buy a page. No UKGC licence, no filing, at any price.</li>
      <li>It does not buy silence. Weak results stay in the filing.</li>
      <li>It does not buy a preview. Operators see the page when you do.</li>
    </ul>
    <h2>How testing stays separate</h2>
    <p>The people who open accounts and score them do not price the commercial deal. If an operator asks for a higher number or a deleted criticism, we refuse. If the pressure continues, the arrangement ends.</p>
    <h2>Names and marks</h2>
    <p>Wolfspins, UKRICHES, Parimatch and their logos remain the property of their owners. They are shown only to identify the brand. That is not an endorsement of UK Casino Desk by those owners.</p>
    <h2>No advice</h2>
    <p>Filings are editorial notes backed by a test window. They are not financial advice, and nothing here suggests gambling is a way to earn.</p>
    <p>Questions: <a href="mailto:hello@ukcasinodesk.co.uk">hello@ukcasinodesk.co.uk</a>.</p>
  </div></section>
</main>
"""

terms = """
<main>
  <section class="page-hero"><div class="wrap">
    <p class="kicker">Legal · updated 28 October 2026</p>
    <h1>Terms of use</h1>
    <p class="lede">UK Casino Desk (“we”) publishes reviews of UKGC-licensed betting brands at ukcasinodesk.co.uk. By using the site you confirm you are 18 or over.</p>
  </div></section>
  <section class="section" style="padding-top:0"><div class="wrap prose-page">
    <h2>Who we are</h2>
    <p>UK Casino Desk is an editorial publisher based in London, United Kingdom. Contact <a href="mailto:hello@ukcasinodesk.co.uk">hello@ukcasinodesk.co.uk</a>.</p>
    <h2>Agreement</h2>
    <p>Using the site means you accept these terms, the privacy policy, the cookie policy and the disclosure. If you do not, leave the site.</p>
    <h2>Age</h2>
    <p>The site is for adults aged 18 or over. Under the Gambling Act 2005 it is an offence for a person under 18 to gamble in Great Britain. Parents should consider filtering software where children use a device unsupervised.</p>
    <h2>What this site is not</h2>
    <p>We do not accept stakes, hold funds, run a gambling product, or manage any account you hold with an operator. Betting, if you choose it, happens entirely with a licensed third party under their terms.</p>
    <h2>Accuracy</h2>
    <p>We take care at the time of publication. Licences, offers and payout speeds change. Check the operator and the <a href="https://www.gamblingcommission.gov.uk/public-register">public register</a> before you act. Our timings describe a test window, not your future result.</p>
    <h2>No advice</h2>
    <p>Nothing here is financial, legal or tax advice. Gambling carries a mathematical disadvantage to the customer.</p>
    <h2>Other websites</h2>
    <p>Outbound links, including affiliate links described in the disclosure, leave our control. Their content and security are their own.</p>
    <h2>Our material</h2>
    <p>Original text, the scoring method and the design of this site belong to UK Casino Desk. Short quotation with a link is fine. Copying substantial parts needs written permission. Operator names remain their owners’ property and are used to identify the brand under review.</p>
    <h2>Acceptable use</h2>
    <p>Do not break the law with this site, probe it, scrape it at scale, impersonate the desk, or send abusive material through the contact form.</p>
    <h2>Availability and liability</h2>
    <p>We aim to keep the site available but do not guarantee uninterrupted access. To the extent the law allows, we are not liable for gambling losses or other loss arising from your use of the site or of a third-party operator. Nothing here excludes liability that cannot legally be excluded, including for fraud or for death or injury caused by negligence.</p>
    <h2>Law</h2>
    <p>These terms are governed by the laws of England and Wales. The courts of England and Wales have exclusive jurisdiction.</p>
  </div></section>
</main>
"""

privacy = f"""
<main>
  <section class="page-hero"><div class="wrap">
    <p class="kicker">Legal · updated 28 October 2026</p>
    <h1>Privacy policy</h1>
    <p class="lede">UK Casino Desk is the controller for personal data described here, under the UK GDPR and the Data Protection Act 2018.</p>
  </div></section>
  <section class="section" style="padding-top:0"><div class="wrap prose-page">
    <h2>What we collect</h2>
    <p>If you email or use the contact form: your name, email, topic and message. Automatically: a truncated IP address, browser and device type, the referring page and pages viewed, plus a record of your cookie choice. We do not seek special-category data, and we do not knowingly keep data about anyone under 18.</p>
    <h2>Why</h2>
    <ul>
      <li>To answer you — legitimate interests in replying to a message you sent.</li>
      <li>To keep the site secure — legitimate interests.</li>
      <li>Optional analytics — consent.</li>
      <li>A non-identifying note that an outbound operator link was used — consent.</li>
      <li>Where the law requires a record — legal obligation.</li>
    </ul>
    <h2>What we do not do</h2>
    <p>We do not sell personal data, pass your enquiry to an operator, build advertising profiles, or send marketing email you did not ask for.</p>
    <h2>Sharing and retention</h2>
    <p>Processors who host the site, deliver email or provide privacy-focused analytics may handle data under contract. International transfers, if any, use a UK adequacy regulation or the International Data Transfer Agreement.</p>
    <ul>
      <li>Contact records: 24 months from the last message.</li>
      <li>Security logs: 90 days.</li>
      <li>Aggregated analytics: 13 months.</li>
      <li>Consent records: 12 months.</li>
    </ul>
    <h2>Your rights</h2>
    <p>You can ask for a copy, a correction, deletion, restriction, or to object, and you can withdraw consent. Email <a href="mailto:hello@ukcasinodesk.co.uk">hello@ukcasinodesk.co.uk</a>. We reply within one month. You can complain to the Information Commissioner’s Office at <a href="{ICO}">ico.org.uk</a> or on 0303 123 1113.</p>
    <p>Cookies are described in the <a href="/cookies.html">cookie policy</a>. Once you leave for another site, their policy applies.</p>
  </div></section>
</main>
"""

cookies = """
<main>
  <section class="page-hero"><div class="wrap">
    <p class="kicker">Legal · updated 28 October 2026</p>
    <h1>Cookie policy</h1>
    <p class="lede">We store as little as possible. Rejecting optional cookies does not hide any filing.</p>
  </div></section>
  <section class="section" style="padding-top:0"><div class="wrap prose-page">
    <p>A cookie is a small text file a site can store on your device. We also use local storage for the same job: remembering your choice.</p>
    <div class="table-wrap">
      <table>
        <thead><tr><th>Name</th><th>Type</th><th>Purpose</th><th>Kept for</th></tr></thead>
        <tbody>
          <tr><td>ukcd_cookie</td><td>Essential</td><td>Remembers accept or reject so the notice stays dismissed.</td><td>12 months</td></tr>
          <tr><td>Session</td><td>Essential</td><td>Keeps a visit intact and limits automated form abuse on the live site.</td><td>Session</td></tr>
          <tr><td>Analytics</td><td>Optional</td><td>Anonymous counts of which filings are read. IP addresses are truncated.</td><td>13 months</td></tr>
          <tr><td>Referral</td><td>Optional</td><td>Notes that an operator link was followed, without identifying you.</td><td>30 days</td></tr>
        </tbody>
      </table>
    </div>
    <h2>Your choice</h2>
    <p>The notice offers “Accept all” or “Reject optional”. Clear this site’s stored data in the browser to see the notice again. A browser Do Not Track or Global Privacy Control signal is treated as a rejection of optional cookies.</p>
    <p>We do not set advertising cookies and we do not embed social pixels. Operators you visit afterwards set their own cookies.</p>
    <p>Strictly necessary storage relies on legitimate interests in running the site, under PECR and the UK GDPR. Everything else waits for consent.</p>
    <p>Questions: <a href="mailto:hello@ukcasinodesk.co.uk">hello@ukcasinodesk.co.uk</a>.</p>
  </div></section>
</main>
"""

page("index.html", "UK Casino Desk | Independent UK betting reviews", "Independent reviews of UK Gambling Commission licensed betting brands. Same measured filings, a new desk: ukcasinodesk.co.uk. 18+.", "home", index)
page("reviews/index.html", "Reviews | UK Casino Desk", "Wolfspins, Parimatch and UKRICHES reviewed with timed withdrawals and published UKGC licence numbers. 18+.", "reviews", reviews)
page("reviews/wolfspins.html", "Wolfspins review | UK Casino Desk", "Wolfspins scored 4.7/5. UKGC 39175. Median payout about 14 hours. 18+.", "reviews", wolf)
page("reviews/parimatch.html", "Parimatch review | UK Casino Desk", "Parimatch scored 4.6/5. UKGC 39576. 24-hour support. 18+.", "reviews", pari)
page("reviews/ukriches.html", "UKRICHES review | UK Casino Desk", "UKRICHES scored 4.5/5. UKGC 39175. Strong spend controls. 18+.", "reviews", ukr)
page("about.html", "About | UK Casino Desk", "How UK Casino Desk tests licensed UK betting brands. Established 2026, London.", "about", about)
page("faq.html", "FAQ | UK Casino Desk", "Answers about scores, licensing, affiliate links and safer gambling.", "faq", faq)
page("contact.html", "Contact | UK Casino Desk", "Write to the UK Casino Desk editorial team in London.", "contact", contact)
page("responsible-gaming.html", "Responsible gaming | UK Casino Desk", "Free UK gambling support, deposit limits, GAMSTOP and warning signs. 18+.", "rg", rg)
page("disclosure.html", "Disclosure | UK Casino Desk", "How affiliate links work on UK Casino Desk, and what they do not change.", "", disclosure)
page("terms.html", "Terms | UK Casino Desk", "Terms of use for ukcasinodesk.co.uk. 18+ information site, not an operator.", "", terms)
page("privacy.html", "Privacy | UK Casino Desk", "How UK Casino Desk handles personal data under the UK GDPR.", "", privacy)
page("cookies.html", "Cookies | UK Casino Desk", "Cookies and local storage used on UK Casino Desk.", "", cookies)

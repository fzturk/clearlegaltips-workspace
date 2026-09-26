#!/usr/bin/env python3
"""Build workspace/plans/editorial-calendar-2026-2027.csv from the approved hub plan.

One row per publish slot (Mon-Fri, one post per day). Re-running regenerates the
file from the definitions below but keeps any status/post_id already filled in.

Usage: python3 workspace/tools/build_calendar.py
"""
import csv
import datetime as dt
import os

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OUT = os.path.join(ROOT, "workspace", "plans", "editorial-calendar-2026-2027.csv")

STATES = {
    "AL": "alabama", "AZ": "arizona", "CA": "california", "CO": "colorado",
    "FL": "florida", "GA": "georgia", "IL": "illinois", "IN": "indiana",
    "MA": "massachusetts", "MD": "maryland", "MI": "michigan", "MN": "minnesota",
    "MO": "missouri", "NC": "north-carolina", "NJ": "new-jersey", "NY": "new-york",
    "OH": "ohio", "OK": "oklahoma", "OR": "oregon", "PA": "pennsylvania",
    "TN": "tennessee", "TX": "texas", "UT": "utah", "VA": "virginia",
    "WA": "washington", "WY": "wyoming",
}


def title_state(code):
    return STATES[code].replace("-", " ").title()


# Category IDs on the live site
CAT = {"templates": 1, "calculators": 6, "estate": 7, "filing": 8}

# (week number, monday date, hub key, [5 slots])
# slot = (type, slug, working title, category, focus keyword)
PLAN = []


def spoke(slug_tpl, title_tpl, cat, kw_tpl, codes):
    out = []
    for c in codes:
        s, t = STATES[c], title_state(c)
        out.append(("spoke", slug_tpl.format(s=s), title_tpl.format(t=t), cat, kw_tpl.format(t=t.lower())))
    return out


def weeks(start_week, monday, hub, slots):
    """Split a flat slot list into consecutive 5-day weeks."""
    d = monday
    w = start_week
    for i in range(0, len(slots), 5):
        PLAN.append((w, d, hub, slots[i:i + 5]))
        w += 1
        d += dt.timedelta(days=7)


D = dt.date

# ---- Hub 2: Small Estate (W01-W04) ----
se = [("hub", "small-estate-affidavit-limits-by-state", "Small Estate Affidavit Limits by State (2026)", CAT["estate"], "small estate affidavit limits by state")]
se += spoke("{s}-small-estate-affidavit", "{t} Small Estate Affidavit (2026): Limit, Rules & Form", CAT["estate"], "{t} small estate affidavit",
            ["TX", "CA", "FL", "IL", "NY", "PA", "OH", "MI", "VA", "IN", "GA", "NC", "AZ", "WA", "NJ", "TN", "MO", "MD", "CO"])
weeks(1, D(2026, 10, 5), "H2-small-estate", se)

# ---- Hub 1: Small Claims (W05-W08) ----
sc = [("hub-upgrade", "small-claims-court-filing-limits-and-fees", "Small Claims Court Limits & Fees by State (2026)", CAT["filing"], "small claims court limits by state")]
sc += spoke("{s}-small-claims-court", "{t} Small Claims Court (2026): Limit, Fees & How to File", CAT["filing"], "{t} small claims court",
            ["CA", "TX", "FL", "NY", "OH", "MI", "PA", "IL", "GA", "NC", "VA", "AZ", "CO", "WA", "NJ", "TN", "MA", "MD", "UT"])
weeks(5, D(2026, 11, 2), "H1-small-claims", sc)

# ---- Hub 3: Divorce (W09-W12) ----
dv = [("hub", "divorce-requirements-by-state", "Divorce Requirements by State (2027): Fees, Residency, Waiting", CAT["estate"], "divorce requirements by state")]
dv += spoke("how-to-file-for-divorce-in-{s}", "How to File for Divorce in {t} (2027): Fees & Steps", CAT["filing"], "how to file for divorce in {t}",
            ["TX", "CA", "FL", "NY", "PA", "IL", "OH", "GA", "NC", "MI", "NJ", "VA", "WA", "AZ", "TN", "CO", "IN", "MO", "MA"])
weeks(9, D(2026, 11, 30), "H3-divorce", dv)

# W13 buffer: 28 Dec 2026 - 1 Jan 2027, no posts.

# ---- Hub 4: Judgment & Garnishment (W14-W17) ----
jg = [("hub", "judgment-interest-rates-by-state", "Judgment Interest Rates by State (2027) + Calculator", CAT["calculators"], "judgment interest rates by state"),
      ("hub", "wage-garnishment-laws-by-state", "Wage Garnishment Laws by State (2027): How Much Is Protected", CAT["filing"], "wage garnishment laws by state")]
jg += spoke("{s}-wage-garnishment-laws", "{t} Wage Garnishment Laws (2027): Limits & Exemptions", CAT["filing"], "{t} wage garnishment laws",
            ["TX", "CA", "FL", "NY", "PA", "IL", "OH", "GA", "NC"])
jg += spoke("how-to-collect-a-small-claims-judgment-in-{s}", "How to Collect a Small Claims Judgment in {t} (2027)", CAT["filing"], "collect small claims judgment {t}",
            ["CA", "TX", "FL", "NY", "OH", "MI", "PA", "IL", "GA"])
weeks(14, D(2027, 1, 4), "H4-judgment", jg)

# ---- Hub 11: US company for non-residents (W18-W21) ----
nr = [
    ("hub", "us-company-for-non-residents", "How to Start a US Company as a Non-Resident (2027)", CAT["filing"], "us company for non residents"),
    ("spoke", "form-5472-guide-foreign-owned-llc", "Form 5472 for Foreign-Owned LLCs (2027): Avoid the $25K Penalty", CAT["filing"], "form 5472"),
    ("spoke", "ein-for-non-us-residents", "How to Get an EIN as a Non-US Resident (No SSN) 2027", CAT["filing"], "ein for non us residents"),
    ("spoke", "us-llc-taxes-for-non-residents", "US LLC Taxes for Non-Residents (2027): ECI, FDAP, 1040-NR", CAT["filing"], "us llc taxes for non residents"),
    ("spoke", "us-business-bank-account-non-resident", "US Business Bank Account for Non-Residents (2027)", CAT["filing"], "us business bank account non resident"),
    ("spoke", "llc-vs-c-corp-for-non-residents", "LLC vs C-Corp for Non-Residents (2027): Tax Compared", CAT["filing"], "llc vs c corp for non residents"),
    ("spoke", "best-state-for-llc-non-residents", "Best State for an LLC as a Non-Resident (2027)", CAT["filing"], "best state for llc non residents"),
    ("spoke", "foreign-partner-us-partnership-1446-withholding", "Foreign Partners in a US Partnership: 1446 Withholding (2027)", CAT["filing"], "foreign partner us partnership"),
    ("spoke", "foreign-owned-llc-operating-agreement-template", "Foreign-Owned LLC Operating Agreement Template (2027)", CAT["templates"], "foreign owned llc operating agreement"),
    ("spoke", "boi-reporting-2026-non-residents", "BOI Reporting After FinCEN's 2026 Final Rule: Non-Residents", CAT["filing"], "boi reporting non residents"),
    ("spoke", "itin-vs-ein-non-residents", "ITIN vs EIN for Non-Residents (2027): Which Do You Need?", CAT["filing"], "itin vs ein non resident"),
    ("spoke", "w-8ben-e-us-llc-payments-stripe-paypal", "W-8BEN vs W-8BEN-E for a US LLC: Stripe & PayPal (2027)", CAT["filing"], "w-8ben-e us llc"),
    ("spoke", "foreign-owned-llc-annual-compliance-calendar", "Foreign-Owned LLC Compliance Calendar (2027)", CAT["filing"], "foreign owned llc compliance"),
    ("spoke", "e-2-visa-business-requirements", "E-2 Visa Business Requirements (2027): Treaty Countries", CAT["filing"], "e-2 visa business requirements"),
    ("spoke", "how-to-open-a-us-llc-from-turkey", "How to Open a US LLC from Turkey (2027)", CAT["filing"], "us llc from turkey"),
    ("spoke", "how-to-open-a-us-llc-from-india", "How to Open a US LLC from India (2027)", CAT["filing"], "us llc from india"),
    ("spoke", "how-to-open-a-us-llc-from-pakistan", "How to Open a US LLC from Pakistan (2027)", CAT["filing"], "us llc from pakistan"),
    ("spoke", "how-to-open-a-us-llc-from-bangladesh", "How to Open a US LLC from Bangladesh (2027)", CAT["filing"], "us llc from bangladesh"),
    ("spoke", "how-to-open-a-us-llc-from-canada", "How to Open a US LLC from Canada (2027): Tax Trap", CAT["filing"], "us llc from canada"),
    ("spoke", "how-to-open-a-us-llc-from-the-uk", "How to Open a US LLC from the UK (2027)", CAT["filing"], "us llc from uk"),
]
weeks(18, D(2027, 2, 1), "H11-non-resident", nr)

# ---- Hub 8: Contractor license & liens (W22-W24) ----
ct = [("hub", "contractor-license-requirements-by-state", "Contractor License Requirements by State (2027)", CAT["filing"], "contractor license requirements by state"),
      ("hub", "mechanics-lien-deadlines-by-state", "Mechanics Lien Deadlines by State (2027) + Calculator", CAT["filing"], "mechanics lien deadlines by state")]
ct += spoke("{s}-contractor-license-requirements", "{t} Contractor License Requirements (2027)", CAT["filing"], "{t} contractor license requirements",
            ["CA", "TX", "FL", "NY", "AZ", "NC", "GA"])
ct += spoke("{s}-mechanics-lien-deadlines", "{t} Mechanics Lien Deadlines (2027)", CAT["filing"], "{t} mechanics lien deadlines",
            ["CA", "TX", "FL", "NY", "PA", "IL"])
weeks(22, D(2027, 3, 1), "H8-contractor", ct)

# ---- Hub 6: Eviction & squatters (W25-W27) ----
ev = [("hub", "eviction-timeline-by-state", "Eviction Timeline by State (2027): How Long It Takes", CAT["filing"], "eviction timeline by state"),
      ("hub", "squatters-rights-by-state", "Squatters' Rights by State (2027): New Removal Laws", CAT["filing"], "squatters rights by state")]
ev += spoke("eviction-process-in-{s}", "Eviction Process in {t} (2027): Timeline & Costs", CAT["filing"], "eviction process in {t}",
            ["TX", "CA", "FL", "NY", "GA", "NC", "OH", "MI", "AZ"])
ev += spoke("squatters-rights-{s}", "{t} Squatters' Rights (2027): How to Remove Squatters", CAT["filing"], "{t} squatters rights",
            ["FL", "GA", "AL", "TN"])
weeks(25, D(2027, 3, 22), "H6-eviction", ev)

# ---- Hub 7: Rent rules (W28-W30) ----
rr = [("hub", "late-fee-laws-by-state", "Rent Late Fee Laws by State (2027) + Checker", CAT["filing"], "late fee laws by state"),
      ("hub", "rent-increase-laws-by-state", "Rent Increase Laws by State (2027): Notice & Caps", CAT["filing"], "rent increase laws by state")]
rr += spoke("{s}-rent-increase-laws", "{t} Rent Increase Laws (2027): Notice & Limits", CAT["filing"], "{t} rent increase laws",
            ["WA", "CA", "OR", "NY", "NJ", "FL", "TX", "IL", "MA", "CO"])
rr += spoke("{s}-rent-late-fee-laws", "{t} Rent Late Fee Laws (2027): Max Fee & Grace Period", CAT["filing"], "{t} rent late fee laws",
            ["TX", "FL", "CA"])
weeks(28, D(2027, 4, 12), "H7-rent-rules", rr)

# ---- Hub 5: Wills (W31-W33) ----
wl = [("hub", "will-requirements-by-state", "Will Requirements by State (2027): Witnesses & Notary", CAT["estate"], "will requirements by state"),
      ("hub", "electronic-wills-by-state", "Electronic Wills by State (2027): Where E-Wills Are Legal", CAT["estate"], "electronic wills by state")]
wl += spoke("how-to-make-a-will-in-{s}", "How to Make a Will in {t} (2027): Legal Requirements", CAT["estate"], "how to make a will in {t}",
            ["CA", "TX", "FL", "NY", "PA", "IL", "OH", "GA", "NC", "MI", "NJ", "VA"])
wl += [("spoke", "holographic-wills-by-state", "Holographic (Handwritten) Wills by State (2027)", CAT["estate"], "holographic wills by state")]
weeks(31, D(2027, 5, 3), "H5-wills", wl)

# W34 buffer: 24-28 May 2027, measurement, no posts.

# ---- Hub 9: Non-compete (W35-W37) ----
nc = [("hub", "non-compete-laws-by-state", "Non-Compete Laws by State (2027): Bans & Limits", CAT["filing"], "non compete laws by state")]
nc += spoke("{s}-non-compete-laws", "{t} Non-Compete Laws (2027): Are They Enforceable?", CAT["filing"], "{t} non compete laws",
            ["CA", "TX", "FL", "NY", "VA", "WY", "MN", "IL", "WA", "CO", "MA", "GA", "OK"])
nc += [("spoke", "non-compete-vs-non-solicitation", "Non-Compete vs Non-Solicitation Agreements (2027)", CAT["filing"], "non compete vs non solicitation")]
weeks(35, D(2027, 5, 31), "H9-non-compete", nc)

# ---- Hub 10: Employer compliance (W38-W40) ----
em = [("hub", "final-paycheck-laws-by-state", "Final Paycheck Laws by State (2027) + Deadline Checker", CAT["filing"], "final paycheck laws by state"),
      ("hub", "paid-sick-leave-laws-by-state", "Paid Sick Leave Laws by State (2027)", CAT["filing"], "paid sick leave laws by state")]
em += spoke("{s}-final-paycheck-law", "{t} Final Paycheck Law (2027): Deadlines & Penalties", CAT["filing"], "{t} final paycheck law",
            ["CA", "TX", "FL", "NY", "IL", "PA", "OH", "GA", "NC", "MI", "WA"])
em += [("spoke", "pto-payout-laws-by-state", "PTO Payout Laws by State (2027)", CAT["filing"], "pto payout laws by state"),
       ("spoke", "employer-wont-pay-final-paycheck-what-to-do", "Employer Won't Pay Your Final Paycheck? What to Do (2027)", CAT["filing"], "employer won't pay final paycheck")]
weeks(38, D(2027, 6, 21), "H10-employer", em)

DAYS = ["Mon", "Tue", "Wed", "Thu", "Fri"]
PHASE_A = {"H2-small-estate", "H1-small-claims", "H3-divorce", "H4-judgment"}
FIELDS = ["date", "day", "week", "phase", "hub", "type", "slug", "working_title",
          "category_id", "focus_keyword", "draft_path", "status", "post_id"]


def main():
    existing = {}
    if os.path.exists(OUT):
        with open(OUT, newline="", encoding="utf-8") as f:
            for r in csv.DictReader(f):
                existing[r["slug"]] = r

    rows = []
    for week, monday, hub, slots in PLAN:
        for i, (typ, slug, title, cat, kw) in enumerate(slots):
            day = monday + dt.timedelta(days=i)
            prev = existing.get(slug, {})
            rows.append({
                "date": day.isoformat(),
                "day": DAYS[i],
                "week": f"W{week:02d}",
                "phase": "A" if hub in PHASE_A else "B",
                "hub": hub,
                "type": typ,
                "slug": slug,
                "working_title": title,
                "category_id": cat,
                "focus_keyword": kw,
                "draft_path": f"workspace/drafts/{hub}/{slug}.html",
                "status": prev.get("status") or "planned",
                "post_id": prev.get("post_id", ""),
            })

    slugs = [r["slug"] for r in rows]
    dupes = {s for s in slugs if slugs.count(s) > 1}
    assert not dupes, f"duplicate slugs: {dupes}"

    with open(OUT, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS)
        w.writeheader()
        w.writerows(rows)
    a = sum(r["phase"] == "A" for r in rows)
    print(f"{len(rows)} rows ({a} phase A, {len(rows) - a} phase B) -> {os.path.relpath(OUT, ROOT)}")


if __name__ == "__main__":
    main()

# Open items for the research team

Items found after the fact checks (09, 09b, 09c). None of these is in the page data yet. The data
rules still apply: a fact goes into `build/data/` only after it is in a team file (01 to 08) and
has passed a fact check.

## 1. No record for medical equipment through Medicare

Found 29 Oct 2026 during a Medicare coverage check of the equipment and home health records.

**The gap.** The data says SSDI and Childhood Disability Benefits lead to Medicare after 24 months
(records `ssdi`, `cdb`, `medicare-savings`). But the only equipment record, `mo-healthnet-dme`,
covers MO HealthNet. No record tells a family how to get a wheelchair or other equipment through
Medicare. For a person with both Medicare and MO HealthNet, Medicare usually pays first for
equipment, so these families are missing a step. Confirm this order of payment before it goes in
the data.

**What the CMS Medicare Coverage Database showed (checked 29 Oct 2026).** These are Medicare
rules only. They do not confirm any MO HealthNet rule.

- NCD 280.3, Mobility Assistive Equipment (effective 5 May 2005). Medicare covers canes, crutches,
  walkers, manual wheelchairs, power wheelchairs, and scooters when a mobility limit stops the
  person from doing daily tasks at home (toileting, feeding, dressing, grooming, bathing). The
  review goes step by step: cane or walker first, then manual chair, then scooter, then power
  chair. A caregiver who can push a manual chair counts in the decision.
  https://www.cms.gov/medicare-coverage-database/view/ncd.aspx?ncdid=219&ncdver=2
- NCD 280.16, Seat Elevation Equipment (Power Operated) on Power Wheelchairs (effective
  16 May 2023). Covered for people who use complex rehab power chairs, after a specialty
  evaluation by a trained PT, OT, or similar practitioner, and when the person transfers in and
  out of the chair at home or reaches from the chair for daily tasks.
  https://www.cms.gov/medicare-coverage-database/view/ncd.aspx?ncdid=376&ncdver=1
- LCD L33788, Manual Wheelchair Bases, version 19, effective 1 Oct 2026. Issued by the DME
  Medicare contractors (CGS Administrators and Noridian Healthcare Solutions).
  https://www.cms.gov/medicare-coverage-database/view/lcd.aspx?lcdid=33788&ver=19
- Related LCDs not yet read: L33792, Wheelchair Options/Accessories; L33312, Wheelchair Seating.

**Questions to answer.**

1. Which DME Medicare contractor serves Missouri? The CMS tool does not map states to
   contractors.
2. For a person with Medicare and MO HealthNet, does Medicare pay first for equipment, and how
   does the MO HealthNet prior authorization work after a Medicare denial?
3. What does a family need for a Medicare wheelchair: the prescription, the face-to-face visit,
   the home check, and the supplier rules? Which suppliers in Southwest Missouri take Medicare
   for complex rehab chairs?
4. Does Missouri's power wheelchair seat elevation criteria (MO HealthNet bulletin dated
   23 Sep 2026, marked "not reviewed" in `mo-healthnet-dme`) match Medicare NCD 280.16?

**Suggested owners.** Agent 03 (physician: equipment and clinical letters), agent 06 (benefits:
Medicare timing for SSDI and CDB), and agent 08 (community living: equipment supply).

## 2. Medicare facts the coverage database cannot check

The CMS tool covers Medicare coverage rules only. These Medicare facts in the data need their own
sources at the next fact check:

- `medicare-savings`: Part B premium for 2026 ($202.90 a month) and the 2027 premium, which was
  not out on 26 Oct 2026.
- `home-health`: the face-to-face visit window (90 days before or 30 days after care starts)
  cites the Medicaid rule, 42 CFR 440.70. This is in federal regulations, not in the coverage
  database.

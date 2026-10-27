# Social scientist (02) findings
Checked: 2026-10-26. Area covered: the 23 counties of the DMH Division of Developmental Disabilities (DD) Springfield Regional Office and its Joplin Satellite Office.

- Springfield Regional Office (12 counties): Christian, Dallas, Douglas, Greene, Hickory, Laclede, Ozark, Polk, Stone, Taney, Webster, Wright. Address on the DMH page: 1515 E. Pythian, Springfield, MO 65801. Phone on the DMH page: 417-895-7400.
- Joplin Satellite Office (11 counties): Barry, Barton, Cedar, Dade, Henry, Jasper, Lawrence, McDonald, Newton, St. Clair, Vernon. Address on the DMH page: 3600 E. Newman Rd., Joplin, MO 64802. Phone on the DMH page: 417-629-3020.
- Source: [DMH Springfield Regional Office page](https://dmh.mo.gov/dev-disabilities/regional-offices/springfield), checked 2026-10-26. (The page spells Stone County as "Stoney". This is a typo on the DMH page.) Confidence: High.
- Note: the Southwest Missouri Autism Project also says it serves "23 counties" through the Joplin and Springfield regional offices, which agrees with this list. [DMH Southwest Missouri Autism Project](https://dmh.mo.gov/dev-disabilities/autism/southwest).

Role note: program cards (section 1) are optional for my role. I give no program cards. Sections 2 to 5 of the brief format are at the end of this file, after my role sections (A to E).

---

## A. Population data

### A1. Method (read this first)

- Data: U.S. Census Bureau, American Community Survey (ACS) 2020–2024 5-year estimates. This is the newest 5-year release on data.census.gov on 2026-10-26. Pulled with the data.census.gov table API on 2026-10-26.
- Note on access: the api.census.gov endpoint now redirects requests with no key to a "missing key" page (checked 2026-10-26). I used the data.census.gov table API instead. It returns the same published tables.
- ACS "any disability" means one or more of six difficulties: hearing, vision, cognitive, ambulatory, self-care, independent living. This is the exact set in our scope.
- ACS counts only the civilian noninstitutionalized population. People who live in nursing homes, ICF/IID facilities, prisons, and some group homes are not in these counts. So these numbers are a floor for the adult disability population.
- The 16+ problem: the published table with an "age 16 and over" row (S1811) is suppressed for 18 of the 23 counties in the 5-year file (only Christian, Greene, Jasper, Newton, and Taney have values). So I used S1810 (all counties) for adults 18+, and I estimated ages 16–17.
- 16–17 estimate: I multiplied each county's count of disabled children ages 5–17 by 0.1874. That is the Missouri share of disabled 5–17 year olds who are 16–17 (Missouri S1811 16+ count 848,326 minus Missouri S1810 18+ count 835,442 = 12,884; divided by 68,749 Missouri children ages 5–17 with a disability in S1810 = 0.1874). Check: for the 5 counties that have a published S1811 value, my 16+ estimate is within 2% of the published number (Greene 42,530 versus 42,486 published; Jasper 19,728 versus 19,698; Christian 10,497 versus 10,622; Taney 8,619 versus 8,675; Newton 8,378 versus 8,552). The 16–17 column is an estimate. The 18+ column is a published number.
- Margins of error (MOE) are 90% MOE from the Census Bureau. Subtotal MOEs are approximate (square root of the sum of squares).
- Scripts and raw downloads: /tmp/claude-0/-home-user-Snoozetown/898057f6-f868-5a37-83ee-038867ed6b7b/scratchpad/scripts/ and /tmp/claude-0/-home-user-Snoozetown/898057f6-f868-5a37-83ee-038867ed6b7b/scratchpad/census/

Sources (all checked 2026-10-26):
- [ACS 2020–2024 5-year S1810, Disability Characteristics, Missouri counties](https://data.census.gov/table/ACSST5Y2024.S1810?g=040XX00US29$0500000)
- [ACS 2020–2024 5-year S1811, Economic Characteristics by Disability Status](https://data.census.gov/table/ACSST5Y2024.S1811?g=040XX00US29$0500000)
- [ACS 2020–2024 5-year C18130, Age by Disability Status by Poverty Status](https://data.census.gov/table/ACSDT5Y2024.C18130?g=040XX00US29$0500000)
- [ACS 2020–2024 5-year S1701, Poverty Status](https://data.census.gov/table/ACSST5Y2024.S1701?g=040XX00US29$0500000)
- [ACS 2020–2024 5-year S0101, Age and Sex](https://data.census.gov/table/ACSST5Y2024.S0101?g=040XX00US29$0500000)
- [ACS 2020–2024 5-year S2801, Computers and Internet Subscriptions](https://data.census.gov/table/ACSST5Y2024.S2801?g=040XX00US29$0500000)
- [ACS 2020–2024 5-year S1601, Language Spoken at Home](https://data.census.gov/table/ACSST5Y2024.S1601?g=040XX00US29$0500000)
- [2020 Decennial Census DHC P2, Urban and Rural](https://data.census.gov/table/DECENNIALDHC2020.P2?g=040XX00US29$0500000)
- Confidence: High for published numbers. Medium for the 16–17 estimate.

### A2. Table 1: People ages 16+ with a disability, poverty, and rural share, by county

| County | DD office | Total pop. | Adults 18+ with any disability (MOE) | % of adults 18+ | Est. ages 16–17 with a disability | Est. total ages 16+ | Check: published 16+ (S1811) | Disabled adults 18+ below poverty % | All-ages poverty % | Rural % (2020) |
|---|---|---|---|---|---|---|---|---|---|---|
| Christian | Springfield RO | 92,915 | 10,241 (±815) | 14.8 | 256 | 10,497 | 10,622 | 14.8 | 8.2 | 42.2 |
| Dallas | Springfield RO | 17,551 | 3,231 (±433) | 24.5 | 106 | 3,337 | n/a | 24.8 | 20.5 | 100.0 |
| Douglas | Springfield RO | 11,965 | 2,155 (±279) | 23.7 | 20 | 2,175 | n/a | 29.4 | 17.5 | 100.0 |
| Greene | Springfield RO | 303,375 | 41,930 (±1,458) | 17.7 | 600 | 42,530 | 42,486 | 22.6 | 13.6 | 14.1 |
| Hickory | Springfield RO | 8,585 | 2,036 (±259) | 29.4 | 13 | 2,049 | n/a | 31.3 | 19.8 | 100.0 |
| Laclede | Springfield RO | 36,390 | 6,271 (±467) | 23.1 | 143 | 6,414 | n/a | 22.4 | 18.2 | 59.2 |
| Ozark | Springfield RO | 8,873 | 2,065 (±232) | 28.9 | 15 | 2,080 | n/a | 37.2 | 21.5 | 100.0 |
| Polk | Springfield RO | 32,444 | 4,607 (±406) | 18.8 | 115 | 4,722 | n/a | 27.0 | 16.3 | 67.2 |
| Stone | Springfield RO | 32,048 | 5,981 (±492) | 22.6 | 50 | 6,031 | n/a | 16.0 | 13.9 | 82.9 |
| Taney | Springfield RO | 56,529 | 8,486 (±631) | 19.2 | 133 | 8,619 | 8,675 | 20.1 | 15.6 | 37.2 |
| Webster | Springfield RO | 40,500 | 4,926 (±506) | 17.4 | 51 | 4,977 | n/a | 23.1 | 15.2 | 80.7 |
| Wright | Springfield RO | 18,965 | 3,238 (±336) | 23.3 | 22 | 3,260 | n/a | 31.6 | 18.7 | 77.6 |
| Barry | Joplin satellite | 35,033 | 5,101 (±436) | 19.0 | 85 | 5,186 | n/a | 25.8 | 15.2 | 82.5 |
| Barton | Joplin satellite | 11,690 | 2,190 (±260) | 24.7 | 37 | 2,227 | n/a | 32.3 | 20.2 | 100.0 |
| Cedar | Joplin satellite | 14,615 | 2,576 (±328) | 23.6 | 26 | 2,602 | n/a | 25.0 | 17.0 | 100.0 |
| Dade | Joplin satellite | 7,641 | 1,310 (±145) | 22.2 | 15 | 1,325 | n/a | 18.2 | 12.6 | 100.0 |
| Henry | Joplin satellite | 22,328 | 3,784 (±354) | 22.0 | 60 | 3,844 | n/a | 20.0 | 14.3 | 59.6 |
| Jasper | Joplin satellite | 124,357 | 19,398 (±974) | 20.9 | 330 | 19,728 | 19,698 | 24.6 | 17.0 | 23.5 |
| Lawrence | Joplin satellite | 38,593 | 5,289 (±476) | 18.8 | 109 | 5,398 | n/a | 20.7 | 14.5 | 71.5 |
| McDonald | Joplin satellite | 23,701 | 3,435 (±356) | 19.6 | 30 | 3,465 | n/a | 24.5 | 16.8 | 99.9 |
| Newton | Joplin satellite | 60,118 | 8,262 (±584) | 18.3 | 116 | 8,378 | 8,552 | 23.0 | 13.5 | 63.2 |
| St. Clair | Joplin satellite | 9,587 | 1,854 (±197) | 25.2 | 19 | 1,873 | n/a | 29.7 | 14.7 | 100.0 |
| Vernon | Joplin satellite | 19,687 | 3,535 (±352) | 24.2 | 29 | 3,564 | n/a | 33.9 | 18.8 | 56.7 |
| **Subtotal: Springfield RO area (12 counties)** |  | 660,140 | 95,167 (±2,138) | 18.8 | 1,522 | 96,689 | n/a | 22.4 | n/a | 40.3 |
| **Subtotal: Joplin satellite area (11 counties)** |  | 367,350 | 56,734 (±1,522) | 20.6 | 857 | 57,591 | n/a | 24.7 | n/a | 58.6 |
| **Total: 23 counties** |  | 1,027,490 | 151,901 (±2,624) | 19.4 | 2,379 | 154,280 | n/a | 23.2 | n/a | 46.9 |
| Missouri |  | 6,191,814 | 835,442 (±6,662) | 17.7 | 12,884 | 848,326 | 848,326 | 21.5 | 12.6 | 30.5 |
| United States |  | 334,922,499 | 40,291,676 (±82,821) | 15.7 | 646,392 | 40,938,068 | 40,916,779 | 20.1 | 12.5 | n/a |

Notes: "Rural %" is the 2020 Census share of residents in rural areas (DHC table P2). "Disabled adults 18+ below poverty %" is from C18130 (18–64 plus 65+). For Missouri and the U.S., the 16–17 column is the actual difference between S1811 and S1810, not an estimate.

### A3. Table 2: Adults 18+ by type of difficulty (a person can have more than one type)

| County | Cognitive 18+ | Ambulatory 18+ | Self-care 18+ | Independent living 18+ | Hearing 18+ | Vision 18+ | Any disability 18–34 | Cognitive 18–34 |
|---|---|---|---|---|---|---|---|---|
| Christian | 3,188 | 4,505 | 1,221 | 3,325 | 3,421 | 1,841 | 1,282 | 901 |
| Dallas | 1,361 | 1,570 | 607 | 1,316 | 982 | 677 | 344 | 259 |
| Douglas | 723 | 1,038 | 451 | 797 | 748 | 352 | 76 | 72 |
| Greene | 16,601 | 19,483 | 6,408 | 14,640 | 12,600 | 8,171 | 8,188 | 5,704 |
| Hickory | 856 | 1,104 | 496 | 648 | 797 | 443 | 213 | 176 |
| Laclede | 2,252 | 3,336 | 1,038 | 2,443 | 2,036 | 957 | 790 | 542 |
| Ozark | 641 | 1,242 | 356 | 942 | 733 | 499 | 146 | 69 |
| Polk | 1,625 | 2,255 | 756 | 1,632 | 1,834 | 825 | 612 | 349 |
| Stone | 1,769 | 2,793 | 993 | 1,790 | 2,382 | 1,192 | 534 | 320 |
| Taney | 2,798 | 4,432 | 1,033 | 2,748 | 2,272 | 1,432 | 1,002 | 644 |
| Webster | 1,775 | 2,537 | 848 | 1,883 | 1,654 | 799 | 384 | 278 |
| Wright | 1,315 | 1,984 | 682 | 1,459 | 1,050 | 565 | 349 | 286 |
| Barry | 1,533 | 2,769 | 769 | 1,552 | 1,710 | 1,013 | 287 | 158 |
| Barton | 566 | 1,269 | 410 | 745 | 828 | 430 | 244 | 205 |
| Cedar | 881 | 1,616 | 627 | 1,048 | 973 | 486 | 218 | 129 |
| Dade | 429 | 677 | 177 | 454 | 394 | 267 | 151 | 108 |
| Henry | 1,180 | 2,200 | 647 | 1,577 | 1,192 | 360 | 381 | 299 |
| Jasper | 7,311 | 9,981 | 2,869 | 6,735 | 5,068 | 3,854 | 2,911 | 1,880 |
| Lawrence | 1,736 | 2,608 | 887 | 2,012 | 2,005 | 1,063 | 681 | 492 |
| McDonald | 1,130 | 1,898 | 583 | 1,422 | 929 | 874 | 429 | 227 |
| Newton | 3,214 | 4,367 | 1,389 | 3,028 | 2,694 | 1,560 | 1,186 | 850 |
| St. Clair | 621 | 963 | 236 | 592 | 626 | 208 | 142 | 111 |
| Vernon | 1,331 | 1,993 | 499 | 1,202 | 946 | 623 | 369 | 299 |
| **Subtotal: Springfield RO area** | 34,904 | 46,279 | 14,889 | 33,623 | 30,509 | 17,753 | 13,920 | 9,600 |
| **Subtotal: Joplin satellite area** | 19,932 | 30,341 | 9,093 | 20,367 | 17,365 | 10,738 | 6,999 | 4,758 |
| **Total: 23 counties** | 54,836 | 76,620 | 23,982 | 53,990 | 47,874 | 28,491 | 20,919 | 14,358 |
| Missouri | 309,832 | 423,697 | 141,387 | 304,789 | 247,826 | 150,429 | 124,111 | 85,567 |
| United States | 14,718,158 | 20,410,559 | 7,356,973 | 15,219,479 | 11,529,553 | 7,571,371 | 6,058,471 | 4,056,714 |

Source: S1810 (2020–2024 ACS 5-year). Each type sums the "18 to 64" and "65 and over" rows. Small-county type counts have large relative MOE; use them for planning size, not for ranking counties.

Caution: "cognitive difficulty" in ACS is much broader than IDD. It includes dementia, brain injury, and serious mental illness. Do not read the cognitive column as an IDD count.

### A4. Table 3: Age, internet access, and language, by county

| County | Median age | % age 65+ | Households | % with broadband (any type) | % with no internet subscription | % with no computer | % smartphone is the only device | % cellular data plan is the only internet | Persons 5+ who speak English less than "very well" (n, %) | of whom Spanish speakers (n) |
|---|---|---|---|---|---|---|---|---|---|---|
| Christian | 39.2 | 16.7 | 35,142 | 91.6 | 8.0 | 3.0 | 9.5 | 16.3 | 1,139 (1.3%) | 468 |
| Dallas | 41.7 | 21.0 | 6,768 | 81.9 | 18.1 | 8.5 | 14.8 | 22.6 | 281 (1.7%) | 9 |
| Douglas | 45.5 | 24.9 | 4,654 | 81.4 | 18.5 | 8.7 | 18.3 | 21.9 | 35 (0.3%) | 9 |
| Greene | 36.4 | 17.2 | 130,951 | 86.7 | 13.2 | 3.9 | 11.1 | 14.3 | 4,442 (1.5%) | 1,522 |
| Hickory | 55.2 | 32.3 | 3,601 | 71.7 | 28.0 | 14.2 | 20.0 | 23.9 | 23 (0.3%) | 19 |
| Laclede | 39.2 | 18.3 | 14,558 | 77.2 | 22.6 | 7.9 | 19.3 | 18.6 | 235 (0.7%) | 61 |
| Ozark | 51.4 | 29.3 | 3,709 | 78.7 | 21.2 | 10.2 | 16.7 | 25.8 | 20 (0.2%) | 3 |
| Polk | 38.1 | 18.3 | 12,059 | 82.4 | 17.6 | 6.7 | 15.3 | 21.3 | 204 (0.7%) | 82 |
| Stone | 54.6 | 32.0 | 13,530 | 88.6 | 10.8 | 5.3 | 13.1 | 22.1 | 194 (0.6%) | 141 |
| Taney | 42.6 | 22.8 | 22,788 | 89.1 | 10.8 | 4.3 | 11.6 | 18.3 | 1,370 (2.6%) | 963 |
| Webster | 37.0 | 15.8 | 13,964 | 82.1 | 17.7 | 10.4 | 11.8 | 20.6 | 1,549 (4.1%) | 53 |
| Wright | 41.1 | 19.7 | 7,187 | 79.7 | 18.4 | 8.2 | 21.2 | 25.5 | 192 (1.1%) | 33 |
| Barry | 43.4 | 22.0 | 13,336 | 84.5 | 15.2 | 7.9 | 17.8 | 19.2 | 1,264 (3.8%) | 839 |
| Barton | 41.1 | 21.4 | 4,454 | 82.7 | 16.7 | 9.0 | 19.6 | 24.9 | 38 (0.3%) | 27 |
| Cedar | 43.0 | 23.1 | 5,773 | 82.4 | 17.6 | 9.7 | 15.5 | 19.1 | 49 (0.4%) | 19 |
| Dade | 47.0 | 24.6 | 3,057 | 82.3 | 17.5 | 10.2 | 19.5 | 26.5 | 64 (0.9%) | 16 |
| Henry | 43.7 | 22.4 | 9,217 | 84.7 | 15.0 | 7.3 | 15.0 | 19.4 | 202 (1.0%) | 148 |
| Jasper | 36.8 | 16.1 | 49,489 | 88.9 | 11.1 | 4.9 | 15.2 | 19.7 | 3,034 (2.6%) | 2,549 |
| Lawrence | 38.8 | 18.1 | 14,602 | 85.1 | 14.7 | 7.0 | 18.5 | 22.6 | 856 (2.4%) | 584 |
| McDonald | 38.2 | 15.6 | 8,558 | 78.9 | 19.1 | 10.0 | 25.7 | 27.4 | 1,813 (8.2%) | 1,097 |
| Newton | 40.2 | 18.8 | 22,129 | 88.0 | 11.6 | 5.1 | 16.3 | 24.1 | 1,983 (3.5%) | 1,065 |
| St. Clair | 46.1 | 25.6 | 4,071 | 82.4 | 16.9 | 9.4 | 19.2 | 31.2 | 45 (0.5%) | 20 |
| Vernon | 41.9 | 20.6 | 7,754 | 84.3 | 15.7 | 9.4 | 17.0 | 21.4 | 398 (2.2%) | 103 |
| **Subtotal: Springfield RO area** | n/a | 19.0 | 268,911 | 86.0 | 13.8 | 5.1 | 12.4 | 17.1 | 9,684 (1.6%) | 3,363 |
| **Subtotal: Joplin satellite area** | n/a | 18.8 | 142,440 | 86.1 | 13.7 | 6.7 | 17.0 | 21.8 | 9,746 (2.8%) | 6,467 |
| **Total: 23 counties** | n/a | 18.9 | 411,351 | 86.0 | 13.8 | 5.7 | 14.0 | 18.7 | 19,430 (2.0%) | 9,830 |
| Missouri | 39.0 | 17.9 | 2,508,227 | 89.3 | 10.6 | 5.2 | 11.4 | 13.0 | 135,025 (2.3%) | 60,199 |
| United States | 38.9 | 17.2 | 129,227,496 | 91.0 | 8.9 | 4.5 | 9.5 | 11.5 | 27,139,643 (8.6%) | 17,218,782 |

Sources: S0101, S2801, S1601 (2020–2024 ACS 5-year). These internet and language figures are for all households or all persons, not only disabled people. ACS does not publish internet access by disability status at county level.

Language detail (S1601, persons who speak English less than "very well"): in Webster County, 1,458 of 1,549 speak "other Indo-European languages" (the table does not name the language). In Greene County, 1,571 speak Asian and Pacific Island languages and 995 speak other Indo-European languages. McDonald County (8.2%) has 1,097 Spanish speakers, 421 Asian and Pacific Island language speakers, and 280 "other languages" speakers.

### A5. What the population data means for the products

1. Size: about 152,000 adults (18+) in the 23 counties report at least one disability (2020–2024 ACS), plus an estimated 2,400 youth ages 16–17. That is about 154,000 people ages 16+. About 97,000 live in the 12 counties of the Springfield Regional Office area.
2. Rurality: 47% of the region's people lived in rural areas in 2020, versus 30.5% for Missouri. Eight counties are 100% rural (Dallas, Douglas, Hickory, Ozark, Barton, Cedar, Dade, St. Clair), and McDonald is 99.9% rural.
3. Poverty: 23.2% of disabled adults in the region are below the poverty line, versus 21.5% statewide. Rates reach 30% to 37% in Ozark, Vernon, Barton, Wright, Hickory, and St. Clair counties.
4. Higher disability rates in rural, older counties: 24% to 29% of adults in Hickory, Ozark, St. Clair, Barton, Dallas, and Vernon report a disability, versus 17.7% statewide. These counties are also older (median age 41 to 55) and have the fewest local providers (see section B and C).
5. Digital access: 13.8% of households in the region have no internet subscription (Missouri 10.6%; U.S. 8.9%). In Hickory County it is 28.0%; in Laclede 22.6%; in Ozark 21.2%. 14.0% of households have a smartphone as their only computing device; in McDonald it is 25.7%. A screener must work on a phone, on a slow cellular connection, and must have a print or phone path for families with no internet.
6. Language: limited English is low overall (2.0%), but it is concentrated: McDonald 8.2%, Webster 4.1%, Barry 3.8%, Newton 3.5%. Spanish is about half of the limited English group. Asian and Pacific Island languages are the second group (Greene, Newton, McDonald, Barry). A Spanish version of the screener is the first priority; the second needs local confirmation of which languages (see Open questions).
7. The transition-age group: about 20,900 adults ages 18–34 in the region report a disability; about 14,400 of them report a cognitive difficulty (ACS, 2020–2024). This is the group most exposed to the "services cliff" in section C.

---

## B. System size

### B1. NEW: Missouri DD waiver wait lists started 15 October 2026

- Fact: "Effective October 15, 2026, the Division of Developmental Disabilities (DDD) implemented wait lists for new enrollments into PfH, CSW, and Comp waiver programs." Reason given: "current budget limitations." "Currently, there is no estimated end date for the wait lists."
- Who is not affected: people already in any waiver continue. New participants whose costs are covered by Inter-Divisional Agreements, and those "whose participation is mandated by federal rule," keep access. The MOCDD (children's) waiver "will continue to be managed as usual."
- How the list is ordered: priority of need (PON) 1 to 5, then date added. PON 1 to 4 comes from the Missouri Adaptive Ability Scale (MAAS) score. PON 5 means the person meets a crisis criterion in 9 CSR 45-2.017(1)(E). Higher PON goes first.
- DMH page names two monthly reports ("Monthly DDD HCBS Waiver Processing List" and "Monthly DDD HCBS Wait List Report") but, on 2026-10-26, the page had no links or numbers for them.
- History: DDD also placed qualifying people on a wait list from 1 July 2024 until a supplemental budget signed 17 March 2025 let DDD enroll people from it (secondary: news reports and a DMH page; see sources).
- Sources: [DMH DD Waiting List page](https://dmh.mo.gov/dev-disabilities/waiting-list), checked 2026-10-26; [DDD Wait List Memo, 15 Oct 2026](https://dmh.mo.gov/sites/g/files/zuston541/files/media/pdf/2026/10/wait%20list%20memo%202026.pdf), checked 2026-10-26; [9 CSR 45-2](https://www.sos.mo.gov/cmsimages/adrules/csr/current/9csr/9c45-2.pdf); [News Tribune, 8 Sep 2024, "Adults with disabilities left waiting on"](https://www.newstribune.com/news/2024/sep/08/adults-with-disabilities-left-waiting-on/) (secondary).
- Confidence: High (primary memo read today). Legal detail of PON and appeal rights belongs to 04 legal and 01 advocate.
- Meaning for the products: the screener and guide must say plainly that DD eligibility does not mean a funded waiver slot now. Families should still apply for DD eligibility, because the wait list is ordered by need and then by date added.

### B2. Missouri DD system counts (DMH, state fiscal years)

| Measure | FY 2022 | FY 2023 | FY 2024 | FY 2025 | FY 2026 projected |
|---|---|---|---|---|---|
| Total individuals served by Division of DD (regional offices and state facilities) | 40,895 | 41,582 | 43,095 | 43,922 | n/a |
| Comprehensive Waiver participants | 8,645 | 8,789 | 9,027 | 9,019 | 9,473 |
| Community Support Waiver participants | 4,702 | 5,549 | 6,509 | 6,439 | 6,939 |
| MOCDD (children) Waiver participants | 305 | 312 | 309 | 310 | 360 |
| Partnership for Hope Waiver participants | 2,077 | 1,903 | 1,435 | 1,053 | 1,253 |
| All four DD waivers | 15,729 | 16,553 | 17,280 | 16,821 | 18,025 |
| Caseload: residential | n/a | 7,738 | 7,908 | 7,980 | 8,434 |
| Caseload: in-home | n/a | 16,928 | 17,693 | 17,783 | 18,516 |
| Caseload: case management only | n/a | 16,661 | 17,230 | 17,912 | 17,912 |

Other FY 2025 facts from the same source:
- Of 9,019 Comprehensive Waiver participants, 7,413 received residential services; 1,606 lived on their own or with family. "Currently, only individuals with the highest prioritization of need for residential services are enrolled in this waiver."
- Community Support Waiver cost cap: $42,000 per year "except in special circumstances."
- Partnership for Hope: cap $12,362 per year, or $15,000 with an exception. State match is split 50/50 with the county, and the waiver exists only in counties with an SB40 board that has agreed to take part.
- 32% of residential consumers are over age 55 (chart, FY 2023 to FY 2025).
- Self-directed services: 4,257 participants in FY 2025, 24.2% of waiver participants.
- Average annual cost per person, FY 2025: residential services $48,534 (group home, shared living, and Individualized Supported Living); self-directed services $28,662.
- Residential provider rates were funded to support "a $17.02/hour wage for direct support professionals."
- DDD oversees 1,092 contracted community provider sites.
- Southwest Missouri Autism Project served 2,213 people in FY 2025 (Central 2,217; East 1,382; Northwest 1,160; Southeast 706).
- NCI Adult Family Survey: 240 Missouri family members responded in FY 2024.

Plain reading: in FY 2025, about 17,900 of the roughly 43,700 people on the DD caseload (41%) received case management only, with no funded in-home or residential service. Partnership for Hope, the low-cost entry waiver tied to SB40 boards, fell by half from 2,077 (FY 2022) to 1,053 (FY 2025).

- Source: [Missouri Office of Administration, FY 2027 DMH Program Descriptions Book](https://oa.mo.gov/sites/default/files/FY27%20DMH%20Program%20Descriptions%20Book.pdf), pages 75 to 104, checked 2026-10-26.
- Confidence: High for FY 2022 to FY 2025 actuals (primary budget document). The FY 2026 projections were made before the 15 Oct 2026 wait list and are now likely too high.
- Waiver participant caps: CMS approved amendments on 14 Jan 2025 (effective 1 July 2024) that raised the Comprehensive Waiver unduplicated count from 9,847 to 10,095, the Community Support Waiver count from 7,317 to 7,357, and the Community Support cost cap from $40,000 to $42,000. Source: [DMH blast, waiver amendments approved, 17 Jan 2025](https://dmh.mo.gov/sites/dmh/files/media/pdf/2025/01/blastwaiveramendmentsapproved011725.pdf) (seen in search summary; Medium until the PDF is read).

### B3. National wait list context (KFF)

| KFF survey year | Missouri total people on HCBS waiting or interest lists | U.S. total |
|---|---|---|
| 2022 | 833 | 516,037 |
| 2023 | 680 | 514,176 |
| 2024 | 76 | 533,444 |
| 2025 | 1,272 | 606,895 |
| 2026 | 1,835 | 649,905 |

- KFF 2026 survey (states answered April to August 2026; brief published 5 Oct 2026): people with I/DD are 72% of people on waiver waiting lists nationally; average wait for I/DD waivers is 38 months; over 80% of people on home care waiting lists are eligible for personal care or other state plan services. KFF notes waiting lists "are not necessarily comparable across states or over time."
- The Missouri 2026 figure (1,835) was collected before the new 15 Oct 2026 wait list. It is likely to grow.
- Sources: [KFF state indicator, number of people waiting for HCBS, Missouri](https://www.kff.org/medicaid/state-indicator/number-of-people-waiting-for-hcbs-by-target-population-and-whether-states-screen-for-eligibility/?state=mo), checked 2026-10-26; [KFF, A Look at Waiting Lists for Medicaid HCBS from 2016 to 2026](https://www.kff.org/medicaid/a-look-at-waiting-lists-for-medicaid-home-and-community-based-services-from-2016-to-2026/), checked 2026-10-26.
- Confidence: Medium. The KFF table text I extracted did not show which column (I/DD or other) held Missouri's count; the totals are clear.

### B4. Spending: Missouri compared with the U.S. (State of the States in IDD, FY 2023, in 2023 dollars)

| Measure (FY 2023) | Missouri | United States |
|---|---|---|
| Total public IDD spending | $2.31 billion | $105 billion (chart also shows $104.6B) |
| Federal-state Medicaid share of IDD spending | 84.8% | 83.1% |
| Medicaid HCBS spending | $1.77 billion | $67 billion |
| Fiscal effort (IDD spending per $1,000 of state personal income) | $6.26 | $4.66 |
| Adjusted HCBS waiver cost per participant | $107,500 | $70,500 |
| Family support spending (share of IDD spending) | $17.5 million (0.8%) | $11.1 billion (10.6%) |
| Supported employment spending (share) | $15.4 million (0.7%) | $1.1 billion (1%) |
| Supported living spending (share) | $1,246.3 million (53.9%) | $18.1 billion (17.3%) |
| Estimated IDD caregiving families | 102,300 | 5,498,900 |
| Share of caregiving families that get state IDD agency family support | 6% | 11% |
| Estimated people with IDD living with a family caregiver | 102,300 (73%) | n/a in profile text |
| Living alone or with a roommate | 25,900 (18%) | n/a |
| Supervised residential setting | 12,800 (9%) | n/a |
| Family support participants | 6,245 | n/a |
| Supported employment participants | 609 (of 6,506 day and work participants, 9%) | n/a |

Plain reading:
- Missouri spends more per person enrolled than the U.S. average ($107,500 versus $70,500 per waiver participant) and more relative to state income ($6.26 versus $4.66 per $1,000). Most of it buys 24-hour supported living for a small group.
- Missouri spends very little on families who care at home: 0.8% of IDD dollars go to family support, versus 10.6% nationally. Only about 6% of Missouri IDD caregiving families get state family support, versus 11% nationally.
- This is a "deep but narrow" system: high cost per person served, low reach to the 73% of people with IDD who live with family. That is the group our navigator and screener serve.
- Source: [Tanis, E.S., et al. (2025). The State of the States in IDD, Missouri State Profile](https://stateofthestates.ku.edu/sites/stateofthestates/files/2025-08/MO_8pg_accessible.pdf) and [U.S. Profile](https://stateofthestates.ku.edu/sites/stateofthestates/files/images/2026/US_8pg_accessible.pdf), checked 2026-10-26. Values read from the chart labels (charts are images in the PDF).
- Confidence: Medium. Primary research source, but FY 2023 data and read from chart images. "Supported living" definitions differ by state, so the Missouri versus U.S. supported living cost comparison ($121,500 versus $46,600 per person) is not a like-for-like comparison.

### B5. Direct support professional (DSP) workforce, Missouri, calendar year 2024

| Measure (NCI-IDD State of the Workforce, 2024) | Missouri | NCI-IDD states |
|---|---|---|
| Provider agencies responding | 236 | 3,936 total |
| DSPs on payroll at responding agencies | 16,694 | n/a |
| DSP turnover ratio (mean) | 46.5% (median 37.5%) | weighted mean 37.1%; state range 16.7% to 53.7% |
| DSPs who left during 2024 (separations) | 8,420 | n/a |
| Share of separated DSPs who left in under 6 months | 43.9% | n/a |
| Full-time vacancy rate | 6.6% | 9.7% average |
| Part-time vacancy rate | 10.9% | 13.2% average |
| Agencies that turned away or stopped accepting new referrals because of DSP staffing | 28.0% | 26.6% |
| Average DSP hourly wage | $18.07 (median $18.00) | $18.49 average (median $18.39) |
| State minimum wage used in report | $12.30 | federal $7.25 |
| "Living wage" used in report | $20.87 | n/a |

- Plain reading: in 2024, more than one in four Missouri provider agencies turned away new referrals because they lacked staff. Missouri DSP wages are below the living wage figure used by NCI. A family who gets a waiver slot can still wait for a provider who has staff.
- DMH also reports DMH's own staff turnover above 30% each year 2023 to 2025 (FY27 DMH Program Descriptions Book, "DMH Turnover 2023-2025" chart).
- Sources: [NCI-IDD 2024 State of the Workforce Survey Report](https://idd.nationalcoreindicators.org/wp-content/uploads/2025/12/2024-NCI-IDD-SoTW_Final-Tagged.pdf), Tables 13, 15, 16, 17, 21, 22, checked 2026-10-26; [FY27 DMH Program Descriptions Book](https://oa.mo.gov/sites/default/files/FY27%20DMH%20Program%20Descriptions%20Book.pdf).
- Confidence: High (primary report, 2024 data). Data are statewide; there is no regional (Southwest Missouri) breakdown in the report.

### B6. Caregiver age (aging caregivers)

| Estimated caregivers of people with IDD, by caregiver age, FY 2023 | Missouri | United States |
|---|---|---|
| Age 60 and older | 25,900 (25%) | 1,334,600 (24%) |
| Age 41 to 59 | 35,900 (35%) | 1,929,000 (35%) |
| Under age 41 | 40,500 (40%) | 2,235,300 (41%) |

- Plain reading: about 1 in 4 Missouri families caring for a person with IDD at home has a caregiver age 60 or older. That is about 25,900 households statewide. These are estimates (the project applies prevalence rates to population data), not counts of known people.
- DMH reports that 32% of people in DD residential services are over age 55 (FY 2023 to FY 2025).
- Rough regional share (my estimate, not a published number): the 23-county region holds about 16.6% of Missouri's people (1,027,490 of 6,191,814, ACS 2020–2024). If caregiving follows population, that is about 4,300 caregivers age 60+ in the region. Treat this as an order-of-magnitude figure only.
- Sources: [State of the States, Missouri profile, page 8](https://stateofthestates.ku.edu/sites/stateofthestates/files/2025-08/MO_8pg_accessible.pdf); [U.S. profile, page 8](https://stateofthestates.ku.edu/sites/stateofthestates/files/images/2026/US_8pg_accessible.pdf), checked 2026-10-26.
- Confidence: Medium (modeled estimates).

### B7. Regional DD counts

- I could not find a public count of DD eligible people, waiver participants, or wait list members for the Springfield Regional Office or its counties. DMH publishes statewide counts only (see Open questions).

---

## C. Why families get stuck: administrative burden analysis

### C1. The framework

- Administrative burden is the cost a person pays to deal with a public program. It has three parts (Moynihan, Herd and Harvey 2015):
  - **Learning costs:** finding out that a program exists, whether you may qualify, and how to apply.
  - **Compliance costs:** forms, documents, appointments, assessments, renewals, and reporting.
  - **Psychological costs:** stress, stigma, loss of control, frustration, and fear.
- Burden is not neutral. It is a policy choice ("policymaking by other means"), and it can ration a program as surely as a budget cut can.
- Burden falls hardest on people with fewer resources. Christensen, Aarøe, Baekgaard, Herd and Moynihan (2020) show that burdens interact with cognitive resources, especially executive function. Stress and scarcity reduce those same resources. This is a "burden trap": the families with the most need have the least capacity to get through the process. For our population, the person with IDD and an exhausted or aging caregiver are both in this trap.
- Sources: [Moynihan, Herd and Harvey 2015, JPART 25(1):43–69, author PDF](https://digitalgovernmenthub.org/wp-content/uploads/2022/07/muu009.pdf); [Christensen et al. 2020, Public Administration Review 80(1):127–136, record](https://www.vive.dk/en/publications/human-capital-and-administrative-burden-the-role-of-cognitive-resources-in-citizen-state-interactions-ozon7lvn/). Checked 2026-10-26. Confidence: High (peer-reviewed; bibliographic details confirmed).

I add a fourth category that is not administrative burden but looks the same to a family: **supply rationing** (wait lists, no provider with staff, no slot). Navigation cannot fix supply rationing. It can only make sure the family is in line, at the right priority, and using what is available while they wait.

### C2. Failure points, classified

| # | Failure point in Southwest Missouri | Burden type | Evidence | Who is hit hardest |
|---|---|---|---|---|
| 1 | Family does not know DD eligibility, MO HealthNet, SSI, VR, and SB40 boards are separate systems with separate front doors. | Learning | Advocate (01) and benefits (06) files map the many entry points. Finkelstein and Notowidigdo (2019): among likely eligible older adults not enrolled in SNAP, only 6% enrolled in 9 months with no contact; a letter telling them they were likely eligible raised this to 11%. Lack of information alone holds people out. | Rural, low-literacy, limited English, new to area |
| 2 | Services stop when school ends ("services cliff"). Adult services are eligibility-based, not entitlements. | Learning, then supply | Shattuck et al. (2011): 39.1% of young adults with autism received no services after high school. Roux et al. (2015): about 26% received no services in their early 20s; 37% were "disconnected" from work and school, versus under 8% of young adults with other disabilities. Lee et al. (2022): being out of high school was associated with fewer services (β = −0.26). | Transition age 16–25; families without an advocate |
| 3 | DD eligibility needs evidence of onset before age 22 and a functional assessment. Old school or medical records may be missing. | Compliance | DMH eligibility rules (see 01 and 04). Records loss grows with age; aging caregivers often hold the only records. | Adults assessed late; aging caregivers |
| 4 | DD eligibility does not give a waiver slot. New wait lists for Comp, CSW, and PfH from 15 Oct 2026, ordered by priority of need, then date. | Supply rationing (and psychological) | DDD memo, 15 Oct 2026. In FY 2025, 17,912 of the DD caseload had case management only (B2). KFF 2026: average I/DD waiver wait 38 months nationally. | Everyone without a crisis (PON 5) |
| 5 | Medicaid application and renewal: income and asset tests, spend-down, documents, mail, deadlines. | Compliance | National: 69% of people disenrolled during the 2023–2024 Medicaid unwinding lost coverage for procedural reasons (KFF, data to 12 Sep 2024). Medicaid forms tested at grade 11 to 18 (signature pages, mean grade 15.5) in a 50-state study (Wilson, Wallace and DeVoe 2009). | Low-literacy; people who move; people with no reliable mail |
| 6 | SSI and SSDI applications need many documents and in-person or phone contact with SSA. | Compliance, learning | Deshpande and Li (2019): closing an SSA field office cut disability applications in nearby areas by about 10% and new recipients by 16%; the largest drops were among applicants with low education and low earnings. Distance and congestion screen out eligible people. | Rural; low-income; people without transport |
| 7 | Partnership for Hope exists only in counties whose SB40 board pays half of the state match. | Supply rationing by geography | FY27 DMH book: PfH available only where an SB40 board agreed to take part; PfH enrollment fell from 2,077 (FY 2022) to 1,053 (FY 2025). | Families in counties without PfH (see Open questions) |
| 8 | A waiver slot does not mean a worker. Providers cannot staff hours. | Supply rationing | NCI 2024: 28.0% of Missouri agencies turned away new referrals because of DSP staffing; DSP turnover 46.5%; 43.9% of DSPs who left had worked under 6 months (B5). | Rural counties; people with high support needs |
| 9 | Guardianship versus supported decision-making decision is made under time pressure at age 18. | Learning, psychological | Belongs to 04 legal and 07 transition. Burden note: a court process is a large compliance cost; families often choose the default they hear about first. | Families told "you must get guardianship" |
| 10 | Each office asks for the same history again. No shared record across DMH, FSD, SSA, VR, school. | Compliance, psychological | Common finding in service integration literature; Missouri has no single application across these programs (see 01). | Caregivers with low time; multiple-program families |
| 11 | Stress, stigma, fear of losing benefits by working or saving, and distrust of government. | Psychological | Marsack-Topolewski and Church (2019): among 320 parents age 50+ of adults with autism, developmental and financial burden predicted lower quality of life. Urban Institute (2019): 13.7% of adults in immigrant families (20.7% of low-income ones) said they or a family member avoided a public benefit in 2018 for fear of green card problems. | Aging caregivers; immigrant and mixed-status families |
| 12 | Information is not accessible: print only, phone only, no ASL, inaccessible websites and PDFs. | Learning, compliance | McKee et al. (2015): 48% of Deaf ASL users had inadequate health literacy; odds 6.9 times those of hearing adults (this reflects access to English print, not intelligence). WebAIM Million 2026: 95.9% of the top 1 million home pages had detected WCAG 2 failures; 51% had missing form input labels. | Deaf, blind, low vision, people with IDD |

Sources for the table (all checked 2026-10-26): [Finkelstein and Notowidigdo, QJE 2019, MIT record](https://dspace.mit.edu/handle/1721.1/123496) and [NBER working paper w24652](https://www.nber.org/system/files/working_papers/w24652/w24652.pdf); [Shattuck et al. 2011, Arch Pediatr Adolesc Med 165(2):141–146, SRI record](https://www.sri.com/publication/education-learning-pubs/post-high-school-service-use-among-young-adults-with-an-autism-spectrum-disorder/); [Drexel A.J. Drexel Autism Institute, National Autism Indicators Report 2015, news release](https://drexel.edu/autisminstitute/news-events/news/2015/April/Autism-Indicators-Young-Adult-Transition/); [Lee, Burke, DaWalt, Li and Taylor 2022, Autism 26(4):1001–1006](https://pmc.ncbi.nlm.nih.gov/articles/PMC9010347); [DDD Wait List Memo](https://dmh.mo.gov/sites/g/files/zuston541/files/media/pdf/2026/10/wait%20list%20memo%202026.pdf); [KFF HCBS waiting lists 2016 to 2026](https://www.kff.org/medicaid/a-look-at-waiting-lists-for-medicaid-home-and-community-based-services-from-2016-to-2026/); [KFF Medicaid Enrollment and Unwinding Tracker](https://www.kff.org/medicaid/issue-brief/medicaid-enrollment-and-unwinding-tracker/); [Wilson, Wallace and DeVoe 2009, "Are state Medicaid application enrollment forms readable?", OHSU record](https://ohsu.elsevierpure.com/en/publications/are-state-medicaid-application-enrollment-forms-readable-2); [Deshpande and Li 2019, AEJ: Economic Policy 11(4):213–248, NBER page](https://nber.org/papers/w23472) and [BFI summary](https://bfi.uchicago.edu/insight/research-summary/who-is-screened-out-application-costs-and-the-targeting-of-disability-programs/); [FY27 DMH Program Descriptions Book](https://oa.mo.gov/sites/default/files/FY27%20DMH%20Program%20Descriptions%20Book.pdf); [NCI-IDD 2024 State of the Workforce](https://idd.nationalcoreindicators.org/wp-content/uploads/2025/12/2024-NCI-IDD-SoTW_Final-Tagged.pdf); [Marsack-Topolewski and Church 2019, AJIDD 124(2):145–156, EMU record](https://commons.emich.edu/fac_sch2019/163); [Urban Institute 2019 via CHCF](https://www.chcf.org/resource/2019/07/09/one-in-seven-adults-in-immigrant-families-reported-avoiding-public-benefit-programs-in-2018/) (secondary listing of the Urban brief); [McKee et al. 2015, J Health Commun 20(sup2):92–100](https://pmc.ncbi.nlm.nih.gov/articles/PMC4714330); [WebAIM Million 2026](https://webaim.org/projects/million/).
Confidence: High for the peer-reviewed and agency figures as quoted. Medium where I relied on an abstract or summary (Deshpande and Li published figures; Wilson et al. 2009; Urban Institute 2018 figure via CHCF).

### C3. Who gets stuck most, and why (equity lens)

- **Rural families (47% of the region lives in rural areas; 8 counties are 100% rural).** Distance raises compliance cost (office visits, assessments, court for guardianship) and narrows supply (fewer providers and DSPs). Evidence that distance and office congestion screen out eligible disability applicants: Deshpande and Li (2019). Evidence on rural reach: RTC:Rural reports that over 3.6 million U.S. households with a disabled member are more than 65 miles from a Center for Independent Living, most of them rural ([RTC:Rural, Rural Institute, University of Montana](https://mtdh.ruralinstitute.umt.edu/?p=696), secondary summary, Medium). Regional fact: no-internet rates of 18% to 28% in Dallas, Douglas, Hickory, Laclede, Ozark, and Wright counties (Table 3).
- **Low-income families (23.2% of disabled adults in the region are below poverty; over 30% in six counties).** Less slack time, less ability to pay for copies, travel, or a private attorney. Scarcity reduces executive function (Christensen et al. 2020). Asset limits create a fear of saving and working (see 06 benefits planner).
- **Low-literacy families.** In the 2023 PIAAC, 28% of U.S. adults ages 16–65 scored at Level 1 or below in literacy, up from 19% in 2017; 34% were at Level 1 or below in numeracy (up from 29%). Medicaid forms have been measured far above the 6th to 8th grade target. People with IDD who apply for themselves face this barrier directly. Source: [NCES press release, 10 Dec 2024](https://ies.ed.gov/learn/press-release/u-s-adults-score-par-international-average-literacy-skills-below-international-average-numeracy-and), checked 2026-10-26. Confidence: High. County literacy estimates exist (PIAAC Skills Map) but I did not pull them (Open questions).
- **Limited-English families (2.0% of the region; 8.2% in McDonald County).** Spanish is about half; Asian and Pacific Island languages and "other Indo-European" languages are the rest (Table 3). Fear of immigration consequences adds psychological cost (Urban Institute 2019). Interpreter rights belong to 04 legal.
- **Deaf and hard of hearing (about 47,900 adults in the region report a hearing difficulty; most are older adults).** Phone-based systems (SSA, FSD call centers, DD intake) are the main barrier for signing Deaf people; relay calls are slow and often dropped. Written English may be a second language for ASL users (McKee et al. 2015). Need: ASL video, text and chat options, captioned video, and plain written English.
- **Blind and low vision (about 28,500 adults in the region report a vision difficulty).** Barriers are inaccessible PDFs, scanned forms, CAPTCHA, image-only text, and unlabeled form fields. WebAIM 2026 shows these failures are near universal on the web. A screener must pass WCAG 2.1 or 2.2 AA in real testing with a screen reader, not only an automated checker. (Legal duties of public entities under ADA Title II web rules belong to 04 legal.)
- **Aging caregivers (about 25,900 Missouri IDD caregivers are 60+; rough regional estimate 4,300).** Highest risk of crisis when the caregiver gets sick or dies, which is often the moment a family first contacts DD. Under the new wait list, crisis (PON 5) is the fastest route to a slot, which rewards late contact. Future planning research: Heller and Caldwell (2006) tested a peer-support future planning program for aging caregivers; a later quote from Heller says fewer than half of families make future plans (secondary, Medium). Source: [Heller and Caldwell 2006, Mental Retardation 44(3):189–202, summary via search](https://ahs.uic.edu/academics/disability-and-human-development/virtual-future-planning-v-fin) (Medium).
- **The person with the disability.** Many adults with IDD, brain injury, or serious cognitive difficulty cannot complete a process alone. A system that assumes a capable, available family member fails adults whose family is gone or estranged.


---

## D. Evidence on solutions

### D1. Navigation: what the research shows

| Model | Best evidence | Effect | Cost or cost note | Confidence |
|---|---|---|---|---|
| Proactive outreach letter to likely eligible people (information only) | Finkelstein and Notowidigdo, RCT, about 30,000 older adults likely eligible for SNAP (QJE 2019) | Enrollment in 9 months: 6% control, 11% information only | Very low cost per contact | High |
| Outreach plus hands-on application help | Same RCT | 18% enrolled with information plus assistance (12 points above control, 3 times the control rate) | Higher cost than letters; authors judged both arms cost-effective as redistribution | High |
| Family navigation by bilingual community health workers (manualized, 11 core components, at least 3 visits) | Feinberg et al., RCT, 249 families of toddlers with positive autism screens, 11 urban primary care sites (JAMA Pediatrics 2021) | Diagnostic follow-through in 1 year: 85.7% navigation versus 76.4% usual care management; hazard ratio 1.39 (95% CI 1.05–1.84). Hispanic families: 90.9% versus 53.3% (HR 2.81) | Mean 19.6 contacts per family: 2.6 in person, 9.2 calls, 6.9 texts, 2.7 emails. Navigators had cell phones and a car service subscription | High (strong trial; child diagnosis, not adult services, so transfer is by analogy) |
| Patient navigation (mostly cancer screening) | Meta-analysis of 13 RCTs (Ali-Faisal et al., J Oncol Navig Surviv 2017) | Odds of completing screening 2.47 times usual care (95% CI 1.91–3.20) | n/a | Medium (summary seen, not full text) |
| Community health worker program for Medicaid or uninsured adults (IMPaCT) | RCT, 302 patients, with return on investment analysis (Kangovi et al., Health Affairs 2020;39(2):207–213) | Fewer hospital days and better outcomes (trial) | $2.47 returned to Medicaid for each $1 spent, within one fiscal year (sensitivity range $1.84 to $3.09) | Medium (abstract and press summaries) |
| Parent advocacy training for transition (VAP-T, then ASSIST, 12 weeks) | Pilot RCT, 41 parents (Taylor et al., JADD 2017); larger RCT, 185 parents in IL, TN, WI | Pilot: more knowledge of adult services, more advocacy skill, more empowerment than controls. Baseline ASSIST data: parent advocacy was strongly associated with number of services (β = 0.33) | About 24 hours of group training per parent | High for knowledge and advocacy; service access outcome trial (Burke, DaWalt and Taylor 2025) seen only in a secondary summary, so Low for service outcomes |
| Aging and Disability Resource Centers and "No Wrong Door" options counseling | State process evaluations (for example Iowa ADRC pilot 2009) | I found no rigorous outcome trial | n/a | Low (evidence gap) |
| Peer-support future planning for aging caregivers | Heller and Caldwell 2006 (29 intervention and 19 control families) | Design confirmed; outcome detail not read | n/a | Medium-low |

Sources (checked 2026-10-26): [Finkelstein and Notowidigdo (NBER w24652)](https://www.nber.org/system/files/working_papers/w24652/w24652.pdf); [Feinberg et al. 2021, JAMA Pediatr 175(3):243–250, PMC full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC7802008); [Ali-Faisal et al. 2017, JONS](https://www.jons-online.com/issues/2017/july-2017-vol-8-no-7/patient-navigation-effectiveness); [Penn Medicine news release on Kangovi et al. 2020](https://pennmedicine.org/news/news-releases/2020/february/penns-community-health-worker-program-yields-247-for-every-1-invested-annually-by-medicaid) (secondary to the Health Affairs paper); [Taylor et al. 2017 VAP-T pilot, PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC6070423); [Lee et al. 2022 (ASSIST baseline), PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC9010347); [Iowa ADRC pilot evaluation listing, ADvancing States](https://advancingstates.org/hcbs/article/iowa-aging-and-disability-resource-center-pilot-sites-evaluation-report); [UIC V-FIN future planning project](https://ahs.uic.edu/academics/disability-and-human-development/virtual-future-planning-v-fin).

What the evidence says for a Southwest Missouri navigator service:
1. **Help, not only information.** Information alone roughly doubles take-up from a low base; information plus hands-on help triples it (Finkelstein and Notowidigdo). The navigator should fill forms with the family, gather documents, and book the next appointment.
2. **Go to the family.** Outreach to people who are likely eligible works better than waiting for them to call. Good outreach lists: students in their last 2 years of school who have an IEP (through schools, with consent), SSI child recipients near age 18 (redetermination; see 06), families on the DD "case management only" caseload, and caregivers age 60+.
3. **Target the highest burden.** Outreach pulls in the least needy first unless it is aimed (Finkelstein and Notowidigdo found the marginal enrollees were less needy). Aim outreach at rural, poor, limited-English, Deaf, and aging-caregiver households. The effect of navigation was largest for the group with the most barriers (Hispanic families, HR 2.81, in Feinberg et al.).
4. **Matched, local navigators.** The successful family navigation model used bilingual, bicultural community members, trained and supervised centrally.
5. **Text first, with some in-person visits.** In the navigation trial, texts and calls were most of the contact; about 2 to 3 in-person visits per family. In rural counties, add transport help or video visits.
6. **Train parents to advocate.** Parent advocacy is strongly tied to the number of adult services received (Lee et al. 2022). A group course (VAP-T or ASSIST style) multiplies one navigator's reach.
7. **Pay for it with existing streams where possible.** DMH states that SB40 boards that provide DD support coordination can bill MO HealthNet through DD Targeted Case Management (FY27 DMH book, p. 104). That covers people already DD-eligible and on Medicaid. The navigator role before eligibility (screening, first application, school exit) has no Medicaid billing route that I found. County SB40 levies, United Way, or foundation funds are the likely payers (see 05).
8. **Do not promise what supply cannot deliver.** Under the 15 Oct 2026 wait list and DSP shortage, a navigator's success measure must include "on the right list at the right priority, using state plan services while waiting" and not only "got a waiver."

### D2. Designing the eligibility screener: evidence and rules

**Reading level and wording**
- Target grade 6 for all screener text; never above grade 8. Medicaid forms have tested at grade 11 to 18 (Wilson, Wallace and DeVoe 2009), and the CHCF Medi-Cal review cites a 6th to 8th grade ideal. 28% of U.S. adults are at Level 1 or below in literacy (PIAAC 2023).
- For people with IDD, the 2026 systematic review of Easy Read found limited evidence that Easy Read alone improves understanding; many "Easy Read" materials were written at a reading age of 13 to 14, above the roughly 8-year level that recent research suggests. People valued a supporter who reads with them. Rules: check reading level with a formula AND test with real users; co-produce with self-advocates (for example People First Missouri, see 01); design for a helper to sit beside the person.
- Sources: [Wilson, Irvine, Alexander and Mengoni 2026, J Appl Res Intellect Disabil 39(1):e70195](https://pmc.ncbi.nlm.nih.gov/articles/PMC12893875/); [Chinn and Homeyard 2017, Health Expectations 20(6):1189–1200](https://pmc.ncbi.nlm.nih.gov/articles/PMC5689240); [CHCF, Making Medi-Cal Communications Clear](https://www.chcf.org/wp-content/uploads/2024/04/MakingMedicaidCommsClear.pdf); checked 2026-10-26. Confidence: High for the reviews; Medium for the CHCF grade target (secondary summary).

**Number of questions and flow**
- Length lowers starts and completion. In a web survey experiment, 75% started when told it took 10 minutes, versus 65% for 20 minutes and 62% for 30 minutes (Galesic and Bosnjak 2009, Public Opinion Quarterly 73(2):349–360). Later questions got faster, lower-quality answers.
- Rules: say "about 5 minutes" only if true; aim for 10 to 15 core questions, one per screen, with branching so most users see fewer. Ask gate questions first (age, county, disability type, has MO HealthNet or SSI, in school or not). Offer "I am not sure" on every question, and route "not sure" to "ask a navigator" rather than to "not eligible." Use income ranges tied to the program limit, not exact dollars, where the rule allows (benefit limits come from 06).
- Error rule: a false "not eligible" is the most harmful error, because it stops a family from applying. When in doubt, show the program as "may qualify, check with..." Results must say "This is not a decision. Only the agency can decide."
- Source: [Galesic and Bosnjak 2009, summary via Survey Research Methods](https://ojs.ub.uni-konstanz.de/srm/article/view/8348/7667), checked 2026-10-26. Confidence: Medium (findings seen through later citing article).

**Trust and privacy**
- Fear stops eligible people from seeking help: in 2018, 13.7% of adults in immigrant families (20.7% of low-income ones) said they or a family member avoided a noncash benefit because of green card fears (Urban Institute, via CHCF). Psychological cost is a burden in its own right.
- Rules: state at the top, in plain words, "Nothing you type leaves this device. We do not save or send your answers." Make it true: no analytics scripts, no cookies, no third-party fonts or trackers, no form submission. Do not ask for name, birth date, Social Security number, address, or immigration status. Give a "clear my answers" button. Let users print or save results locally.

**Mobile, slow connections, and no internet**
- In the 23 counties, 14.0% of households have a smartphone as their only computing device (25.7% in McDonald), 18.7% rely on a cellular data plan as their only internet, and 13.8% have no internet subscription (28.0% in Hickory) (Table 3, ACS 2020–2024). Nationally, 16% of adults are "smartphone-only" internet users (Pew, 2025 survey).
- Rules: one column; large tap targets; works on a small, old phone; total page weight small (no framework, no large images) so it loads on a weak signal; works offline once loaded. Make a printable paper version of the same questions and results, and a phone script for navigators, 211, libraries, schools, and SB40 boards to use with families who have no internet.
- Source: [Pew Research Center, Mobile Fact Sheet](https://pewresearch.org/internet/fact-sheet/mobile/), checked 2026-10-26 (Medium: figure from search summary of the live page).

**Blind and low-vision users**
- 95.9% of the top 1 million home pages had detected WCAG 2 failures in 2026; the most common were low-contrast text (83.9%), missing image alternative text (53.1%), and missing form input labels (51%) (WebAIM Million 2026).
- Rules: meet WCAG 2.2 AA; use native HTML form controls with visible labels; no CAPTCHA; no time limits; logical heading order; results as a text list, not an image or a PDF; support 200% zoom and high contrast. Test by hand with NVDA or JAWS on Windows, VoiceOver on iPhone, and TalkBack on Android, with blind testers. An automated checker alone is not enough.

**Deaf and hard of hearing users**
- 48% of Deaf ASL users in one study had inadequate health literacy in English-based testing; odds 6.9 times hearing adults (McKee et al. 2015).
- Rules: no step should require a voice phone call. For every "next step," list text, email, video phone, or in-person options where they exist. Short ASL videos for the introduction and key terms help ASL users (optional, captioned). Keep English short and concrete.

**Limited-English users**
- Spanish first (about half of limited-English residents in the region). Use professional translation with community review. Before adding other languages, confirm which ones with local data (see Open questions).

**People with IDD using it themselves**
- Offer "I am answering for myself" and "I am answering for someone else" at the start, and change pronouns to match. Avoid deficit language. One idea per sentence. Allow the browser's read-aloud feature to work (real text, not images of text).

---

## E. How to measure success without collecting private data

### E1. Rules for all measures
1. Count events, not people. Never record name, birth date, address, SSN, Medicaid ID, diagnosis, or immigration status.
2. Report only totals by month and by county or county group. Do not publish any count under 11; combine small counties (for example "Hickory, Dallas, Polk") if needed. (The threshold of 11 is my recommendation, not a cited standard.)
3. If a navigator needs to follow a family over time, use a random case code that only the navigator holds, kept apart from the tally sheet, and delete the code key when the case closes.
4. The screener sends nothing by default. Any count from it must be a single anonymous event with no answers attached.

### E2. Screener measures

| Measure | How to get it without private data | Target or use |
|---|---|---|
| Page loads and result views | Static host request counts (no IP storage), or no counting at all | Trend only |
| Opt-in one-tap feedback at the end: "Do you know your next step?" yes/no | Sends one value; no answers attached | 80% or more "yes" (my proposed target) |
| Accuracy audit | Each quarter, navigators enter 20 to 30 closed real cases (no identifiers, answers only) and compare screener output with the actual agency decision | Report false "not eligible" rate; aim for near zero |
| Reading level | Run all screener text through a readability formula | Grade 6 target, never above 8 |
| Accessibility | Automated checker plus manual tests with screen readers and blind testers | Zero WCAG 2.2 AA failures found |
| Usability | Small moderated tests (5 to 8 people per group): rural older caregivers, Spanish speakers, Deaf ASL users, blind users, self-advocates with IDD | Task completion, minutes to finish, points of confusion |
| Load on a weak connection | Test on an old phone with network throttling | Usable in under 10 seconds on a slow mobile connection (my proposed target) |

### E3. Navigator service measures (aggregate tallies)

| Measure | Why it matters | Data source |
|---|---|---|
| Contacts per month by county, channel (phone, text, in person, video, ASL), and language | Reach and access | Tally sheet |
| Contacts per 1,000 people ages 16+ with a disability, by county | Shows rural reach gaps; denominator is Table 1 | Tally sheet plus ACS |
| Share of contacts from rural counties, from limited-English, Deaf, and blind families, and from caregivers age 60+, compared with their share of the population | Equity check | Tally sheet plus ACS and B6 |
| Milestones reached (count): DD intake requested; DD eligibility decided; PON and service plan submitted; placed on wait list; MO HealthNet application filed; SSI application filed; VR referral; transition plan includes adult services; future plan started | Shows movement through the system | Navigator closing checklist |
| Median days from first contact to each milestone | Measures compliance burden and agency delay | Case code with dates only |
| Denials by reason type: procedural (missing paper, missed deadline) versus substantive (not eligible) | Procedural denials are pure administrative burden and are fixable | Family report at follow-up |
| Unmet need tally by reason: wait list, no provider staff, no transport, cost, language, other | Feeds the policy report; separates supply rationing from burden | Navigator closing checklist |
| Family-reported burden, 3 items, 1 to 5 scale, anonymous, at first contact and at close: "I know my next step" (learning); "I have the papers I need" (compliance); "I feel less stressed about this" (psychological) | Direct measure of the three burden types | Anonymous card or one-tap form |
| Next step completed at 90 days (yes or no) | Outcome that matters to families | Follow-up call tally |

### E4. System indicators to track each year (public data only)
- ACS: disabled adults below poverty, by county (Table 1), and households with no internet (Table 3).
- DMH: total DD caseload; waiver counts; "case management only" count; wait list counts if DMH publishes them (FY27 DMH book and later editions).
- KFF: Missouri total on HCBS waiting lists (B3).
- NCI State of the Workforce: Missouri DSP turnover, vacancy, wage, and share of agencies turning away referrals (B5).
- State of the States: Missouri share of IDD spending on family support (B4).

---

## 2. Order and dependencies (social science view; details belong to 01, 04, 06)

1. DD eligibility through the Regional Office comes first. Then the MAAS and priority of need (PON). Since 15 Oct 2026, a person then goes on the wait list for Comp, CSW, or PfH (ordered by PON, then date added). Applying early matters because date added breaks ties within a PON level. (Source: DMH waiting list page and memo, B1.)
2. A DD waiver also needs MO HealthNet eligibility and an ICF/IID level of care determination before waiver services start (FY27 DMH book, DD Support Coordination section).
3. Partnership for Hope is possible only if the person's county SB40 board takes part (FY27 DMH book).
4. Start adult-system steps before school exit. Service use drops after high school (Shattuck 2011; Roux 2015; Lee 2022).
5. A waiver slot comes before a provider; a provider with staff comes before services. Staffing is a separate gate (NCI 2024).
6. VR: other agents report that Missouri VR closed Priority Categories II and III on 9 Dec 2024. My searches did not confirm this from a primary source. I leave it to 07.

## 3. Gaps and failure points (summary)

1. **New wait list, no public count.** DD waiver enrollment for adults is wait-listed from 15 Oct 2026 with no end date. DMH publishes no wait list numbers yet. (B1)
2. **Large "case management only" group.** In FY 2025, 17,912 people on the DD caseload had case management only (41% of the caseload). (B2)
3. **Deep but narrow spending.** Missouri spends $107,500 per waiver participant (U.S. $70,500) but only 0.8% of IDD dollars on family support (U.S. 10.6%). Only about 6% of IDD caregiving families get state family support (U.S. 11%). 73% of Missourians with IDD live with family. (B4)
4. **Workforce gate.** 28.0% of Missouri provider agencies turned away referrals in 2024 for lack of staff; DSP turnover 46.5%; average wage $18.07 against a $20.87 living wage benchmark. (B5)
5. **Aging caregivers.** About 25,900 Missouri IDD caregivers are age 60+; crisis is the fastest path to a slot, so the system rewards late contact. (B6, C3)
6. **Services cliff at school exit.** Strong national evidence; no Missouri or regional measure found. (C2)
7. **Rural and digital gaps.** 47% of the region is rural; 13.8% of households have no internet (up to 28.0%); disabled-adult poverty above 30% in six counties. (A)
8. **Burden falls on those least able to bear it.** Low literacy (28% of U.S. adults at Level 1 or below), complex forms (grade 11 to 18), phone-only systems that exclude Deaf users, and inaccessible web forms. (C2, C3)
9. **PfH depends on county choice.** PfH enrollment fell by half from FY 2022 to FY 2025; access depends on whether the county SB40 board takes part. (B2)
10. **Data gaps.** No public regional or county DD counts; no Missouri-specific procedural denial data found; NCI family survey results for Missouri not public in a form I could find. (B7, Open questions)

## 4. Recommendations from my field

| # | Recommendation | Evidence | Who can make the change |
|---|---|---|---|
| 1 | Publish monthly wait list counts by waiver, PON level, and Regional Office, plus median time on list. The page sections already exist. | B1; KFF notes lists are hard to compare without definitions | State agency (DMH DD) |
| 2 | Publish annual DD counts by Regional Office and county: eligible, case management only, each waiver, wait list. | B7 | State agency (DMH DD) |
| 3 | Fund a regional navigator service that does hands-on application help, uses bilingual and local staff, contacts families by text first, and reaches out to likely eligible families (school exit cohort, SSI youth near 18, case management only, caregivers 60+). | Finkelstein and Notowidigdo; Feinberg et al. | County SB40 boards, nonprofits, United Way; DMH for DD-eligible Medicaid members through Targeted Case Management |
| 4 | Run a parent advocacy course for transition-age families each year in Springfield and Joplin, with a video option for rural counties. | Taylor et al. 2017; Lee et al. 2022 | Providers and nonprofits (for example Parent Training and Information Center, see 01); county boards to fund |
| 5 | Add a future-planning program for caregivers age 60+ and ask DMH to treat caregiver age and health as a planned-transition factor, not only as a crisis. | B6; Heller and Caldwell 2006 | Providers (program); state agency and legislature (PON policy; see 04 and 05) |
| 6 | Shift some IDD dollars toward family support (respite, flexible family funds). Missouri spends 0.8% versus 10.6% nationally. | B4 | Legislature; state agency |
| 7 | Fund DSP wages toward the $20.87 living wage benchmark and track the share of agencies turning away referrals. | B5 | Legislature; state agency |
| 8 | Adopt a plain language (grade 6 to 8) and accessibility (WCAG 2.2 AA, no voice-only steps) standard for every DD, FSD, and county board form and web page; test with users with IDD, Deaf, and blind users. | C2; D2 | State agencies (DMH, DSS/FSD); county boards; providers |
| 9 | Build the screener to the D2 rules: short, branching, "not sure" option, no false "not eligible," no data saved, mobile-first, printable, Spanish first. | D2 | Product team (lead) |
| 10 | Bring services to rural counties: scheduled outreach days at libraries and county offices, video intake and assessment where allowed, and transport help for required in-person steps. | Deshpande and Li 2019; Table 1 and 3 | State agency (DMH, FSD, SSA local offices); county boards |
| 11 | Track the E2 and E3 measures from day one, and report unmet need by reason so supply rationing and burden are shown separately. | E | Navigator service; county boards |

## 5. Open questions

1. Regional DD numbers for the Springfield Regional Office and Joplin Satellite Office: number eligible, on each waiver, case management only, on the new wait list. Not public. (DMH data request would be needed; we are not to contact anyone.)
2. Size of the new (15 Oct 2026) wait list: no published count yet.
3. Which SW Missouri county SB40 boards take part in Partnership for Hope (01 or 08 may have this).
4. KFF 2026 Missouri count (1,835): the extracted table did not show which population column it is in.
5. DMH notice of the Jan 2025 waiver cap increases: the PDF URL returned 404; figures (10,095 Comp; 7,357 CSW; $42,000 cap) seen only in a search summary. The $42,000 CSW cap is confirmed in the FY27 DMH book.
6. Missouri-specific share of Medicaid unwinding disenrollments that were procedural (national figure 69%).
7. NCI Adult Family Survey results for Missouri (for example, "family has enough information"). DMH says 240 Missouri families responded in FY 2024; results not found.
8. County-level adult literacy (PIAAC Skills Map) for the 23 counties.
9. Which languages are behind "other Indo-European languages" in Webster County (1,458 limited-English speakers) and "Asian and Pacific Island languages" in Greene, Newton, McDonald, and Barry. ACS detailed table B16001 was not available at county level through the data.census.gov API.
10. Missouri VR order of selection: other agents report Priority Categories II and III closed on 9 Dec 2024. I could not confirm this from a primary source.
11. Cost of a navigator position in the region (salary and benefits) for a budget; not researched.
12. Service-access results of the ASSIST trial (Burke, DaWalt and Taylor 2025) seen only in a secondary summary.
13. ACS undercounts: people in group homes and ICF/IID facilities are excluded from Table 1. A regional count of people in DD residential settings would close this gap.

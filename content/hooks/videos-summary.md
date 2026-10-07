# Video index summary (Google Drive, mimeType video/*)

Scanned 2 pages x 100 results = 200 rows, 162 unique files (38 duplicate ids across pages). Page 3 failed twice with "Operation is not implemented" from the Drive connector, so the index may be incomplete beyond 200 rows. Classification is from the file title only; no video was opened.

## Counts per folder

| Folder (parentId) | Files |
|---|---|
| Ads export A (`1C1gBLlR-cVqyGEOt_oDZfhw6QdykYWNM`) | 104 |
| Ads export B (LP-named) (`1qF6kVTBfral_lO5AzDs3UBk_wVYsAZdw`) | 57 |
| Loose upload (`157hjuJT7K0te9uesJJnjRMJBhzQWAINj`) | 1 |

## Counts per category

| Category | Files |
|---|---|
| ad-final | 79 |
| ugc | 41 |
| product-demo | 23 |
| other | 14 |
| egg-test | 5 |

## Category per folder

| Folder | ugc | ad-final | product-demo | egg-test | other |
|---|---|---|---|---|---|
| Loose upload | 1 | 0 | 0 | 0 | 0 |
| Ads export A | 22 | 54 | 18 | 4 | 6 |
| Ads export B (LP-named) | 18 | 25 | 5 | 1 | 8 |

## GIF candidates

Every file is under 100 MB (largest 56.7 MB), so all 162 are technically GIF candidates; `gif_candidate` is "yes" for every row. The `gif_hint` column marks the ones whose title promises a usable visual beat: pouring / cooking 12, hammered close-up 11, scratch / side-by-side comparison 11, egg release 5, cleaning (one-pass wipe) 5.

### Top 10 for email GIFs (ffmpeg later)

| # | Drive id | Beat | Why | Title |
|---|---|---|---|---|
| 1 | `1pddPJvl9Ie0szCivehVjvf3Bj-s3kOIl` | egg release | 0.7 MB, organic egg flip, shortest clip, ideal first GIF test | 107 - Video - organic egg flip - Hammered Pan - PP - 201025.mp4 |
| 2 | `1fF_7HHgbhmuA_45iWTajibxcYDyS-XIu` | egg release | before/after egg scroll UGC, 3.9 MB | 069 - [S] - TOF_115V1C-VID-SYDNEY_BEFORE_AFTER_EGG_SCROLL-UGC-BOTH-PAN |
| 3 | `1dSRJam17nEAM4TEfSxHta6_Uw7rmX4Ew` | egg release | PFAS villain egg slide proof, kinetic type, 8.7 MB (use the egg beat only) | 106 - SAR-PA-PFASVILLAIN-EGGSLIDEPROOF-LIFETIMEGUARANTEE-KINETICTYPE-V |
| 4 | `1WCr_8xqsuY44n64f5_P1vh-n7yuJ-IDe` | cleaning (one-pass wipe) | real-time wipe after salmon, no offer, 9.2 MB; the strongest cleaning proof (ad spend 70k) | 157 - Vid - AME-MA-CLEANUPDOUBT-WATCHTHISHOOK-REALTIMEWIPE-NOOFFER-CIN |
| 5 | `12h3_0ZMORKeZcRRUOOBqoyxptxoVX6BG` | hammered close-up | ASMR sensory glide cine, 6.8 MB | 061 - SAR-SA-EFFORTLESS-ASMR-SENSORYGLIDECINE-V1 Hook 1.mp4 |
| 6 | `1jQd5NfZP_jYOPM6XTQAgXiRsed2Tu3xw` | hammered close-up | asmr 4x5, 2.7 MB | 150 - Video - asmr 4x5.mov- Hammered Pan Pro PDP.mp4 |
| 7 | `1qp8MJPWyRM11iQFlJ3Ek-RHAQRvprEBp` | hammered close-up | toxic coating ASMR hook 1, 9.1 MB | 002 - CLAUDEXMANUS -SAR-PA-TOXICCOATING-ASMR-LIFETIMEGUARANTEE-HAMMERE |
| 8 | `1nlzfCIswJnOr1IKIigkNAiB09T_oCn1T` | scratch / side-by-side comparison | hexclad comparison UGC 9x16, 9.5 MB (ROAS 1.55 on 62k spend) | 004 - sk_hexclad comparisation 9x16__Competitor_vid_Pan_UGC_PDP.mp4 |
| 9 | `1rRFjuuj6XVV4v-XeubNE14-hDQlsO1Pu` | pouring / cooking | steak concept hook 4, 9.6 MB (sear shot) | 166 - hexcladinspo_steak_concept Hook 4.mp4 |
| 10 | `1vXqzjDdkCY6LZpp-pdCIFSqPdMh9YApd` | pouring / cooking | First Crepe Win V3, 18.3 MB (batter pour + flip) | 041 - SV - Titanium Cookware - First Crepe Win _V3.mp4 |

Recipe when ffmpeg is available: trim to the 2 to 4 second beat, 600 px wide, 12 fps, palettegen/paletteuse, target under 1.5 MB for hero use and under 600 KB for inline. Egg release and one-pass wipe are the two beats that read without sound and without a caption; the hammered close-up needs a one-line caption ("Zero coatings. Titanium cooking surface.").

## Notes
- Folder A holds the Adnova-era exports (Creative #15 Hook 2, Johnny Creative #9, the 22-year chef rating ads, AME cleanup wipe). Folder B holds the older LP-named exports (Sarah/Steven/Amelia VSLs, TikTok comment formats, Black Friday banners from 2025).
- No water test or pouring-only b-roll exists under those words in titles; the closest are the salmon wipe and the crepe/steak cooking shots. If a water test clip is needed it must be shot or cut from the "Titanium vs Everything" demo.
- "other" holds concept files (Cortisol concept, merge Carree, Labour day video 9) that need a look before use.

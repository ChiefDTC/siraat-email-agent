# 15 · Livewacht v5-flows

Live sinds 8 oktober 2026, 22:29 UTC (9 oktober 00:29 Amsterdam). Bewaker: Claude (alleen lezen via Klaviyo-API). Eén controleronde per 20 minuten: instroom tegenover triggers, opens (menselijk, machine_open false) en kliks (geen bot) per mail, bounces, spam, uitschrijvingen, overgeslagen sends, codes, dubbele mails en flowstatus. Alarmen gaan direct naar Slack #claude-mail; verder stil, behalve één "Stand v5" rond 08:00 Amsterdam.

Drempels: draaiboek `03-golive-draaiboek.md` sectie 6. Baseline: oude flows (12 maanden, `research/history/flow-messages-all.csv`) en de T01-controle-arm "Old · ..." binnen dezelfde v5-flow.

Leeswijzer logregel: `Chec:a/b` = a profielen met rijpe trigger (wachttijd + 15 min verstreken), b profielen die de eerste mail kregen (v5 plus Old-arm). hopen = menselijke opens, hklik = kliks zonder bot.

## VERBETERVOORSTELLEN (niet uitgevoerd)

_Nog geen._

## Logboek (één regel per ronde, UTC)

- 10-08 22:38 · +0.2u · v5-mails 0 · QUBUQV:0/0 TZG9Mx:0/0 WdRz5k:0/0 T4a5Mk:0/0 X3ySuU:0/0 VLGhbR:0/0 VQ93sx:-/0 TbYQmX:-/0 Wzz6xC:-/0 VPixnJ:-/0 UyFc78:-/0 VTkxFL:-/0 XbYT7T:-/0 · skipped 0 · codes 0 · geen alarm
- 10-08 22:58 · +0.5u · v5-mails 0 · QUBUQV:0/0 TZG9Mx:0/0 WdRz5k:0/0 T4a5Mk:0/0 X3ySuU:0/0 VLGhbR:0/0 VQ93sx:-/0 TbYQmX:-/0 Wzz6xC:-/0 VPixnJ:-/0 UyFc78:-/0 VTkxFL:-/0 XbYT7T:-/0 · skipped 0 · codes 0 · geen alarm
- 10-08 23:18 · +0.8u · v5-mails 0 · QUBUQV:0/0 TZG9Mx:0/0 WdRz5k:0/0 T4a5Mk:7/0 X3ySuU:0/0 VLGhbR:0/0 VQ93sx:-/0 TbYQmX:-/0 Wzz6xC:-/0 VPixnJ:-/0 UyFc78:-/0 VTkxFL:-/0 XbYT7T:-/0 · skipped 0 · codes 0 · geen alarm

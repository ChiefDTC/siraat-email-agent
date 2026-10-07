#!/bin/bash
# Rendert elke dynamische mail met Django (zelfde syntax als Klaviyo) op echte, geanonimiseerde voorbeeld-events en controleert de uitkomst.
# Eenmalig: pip install --target research/tailoring/test/pylib django==4.2
cd "$(dirname "$0")"; R=../../../klaviyo/templates; mkdir -p out; fail=0
t(){ f=$1; s=$2; shift 2; n=$(basename $f)
  python3 expand.py $R/v3/$f.html $R/v3/$(dirname $f)/assets /dev/null out/$n.exp.html || { echo "FOUT expand $f"; fail=1; return; }
  python3 render.py out/$n.exp.html samples/$s.json out/${n}_$s.html $R/v3/$(dirname $f)/assets $R/partials/shared >/dev/null || { echo "FOUT render $f $s"; fail=1; return; }
  for k in "$@"; do want=1; [ "${k:0:1}" = "!" ] && { want=0; k=${k:1}; }
    python3 -c "import re,sys,html;t=html.unescape(re.sub(r'<[^>]+>','|',open('out/${n}_$s.html').read()));sys.exit(0 if sys.argv[1] in t else 1)" "$k"; got=$((1-$?))
    [ $got = $want ] && echo "ok   $f $s: $( [ $want = 1 ] && echo bevat || echo mist ) '$k'" || { echo "FOUT $f $s: '$k'"; fail=1; }
  done; }
t checkout/c1 co_apron '!One pan. Nothing'; t checkout/c1 co_pan 'One pan. Nothing'; t checkout/c1 co_set6 'One pan. Nothing'
t checkout/c2-acc co_apron 'Heavy 16-oz canvas' '!Pure titanium, non-porous'; t checkout/c2-acc co_board 'Pure titanium, non-porous' '!16-oz'; t checkout/c2-acc co_giftcard 'Sent by email'
t checkout/c3-acc co_apron 'An apron does want'; t checkout/c3-acc co_mill '!An apron does want'
t checkout/c4 co_apron '!12-piece set' '!Duties paid'; t checkout/c4 co_pizza '12-piece set' 'YOUR CODE RUNS OUT' '!{{'; t checkout/c4 co_pan_eur '!12-piece set' 'Duties paid' 'NO IMPORT'
t checkout/c4-nocode co_pan '12-piece set' '!Duties paid' '!YOUR CODE RUNS OUT'; t checkout/c4-nocode co_pan_eur '!12-piece set' 'duties paid'
t cart/k1 atc_lid_eur '!$39.00'; t cart/k1 atc_pan '$134.00'
t cart/k1-acc atc_apron 'Heavy 16-oz canvas' '$49.00'; t cart/k1-acc atc_lid_eur '304 stainless' '!$39'
t browse/b1 vp_set6 'Get 10% off this set' 'THE SET YOU VIEWED'; t browse/b1 vp_pan 'Get 10% off this pan'
t browse/b1-acc vp_mill '12 numbered grind settings'; t browse/b1-acc vp_apron '16-oz canvas, adjustable'
t browse/b2-clicked vp_lid '!Pure titanium cooking surface' '!One pan.'; t browse/b2-clicked vp_pan 'Pure titanium cooking surface' 'One pan.'
t post-purchase/p1-first po_apron_us '!first egg' 'your door' '!chef tells' 'Thank you for ordering from us'; t post-purchase/p1-first po_pan_us 'first egg' 'chef tells'
t post-purchase/p3-pan po_deep_us 'same diameter as your pan'
t post-purchase/p3-next po_panlid_us 'YOU HAVE THE LID' '$62.10' 'A second Pan Pro'; t post-purchase/p3-next po_deep 'MATCHED TO YOUR PAN' '!$53.10'
t post-purchase/p3-apron po_apron_us '$120.60'
t winback/r1-pan po_panlid_us '!Stainless Steel Lid'; t winback/r1-pan po_pan_us 'Stainless Steel Lid'
t winback/r1-acc po_board_us '$120.60'; t winback/r1-acc po_board '!$120.60'
# Strenger op tags (QA-poort 2026-10-07): kltags.py mag alleen Klaviyo-tags kennen, en alle 61 mails moeten de allowlist,
# de Django-render op alle varianten en de ruwe-HTML-structuur halen (scripts/qa_render.py --static, zonder browser).
python3 -c "import re,sys;sys.path.insert(0,'../../../scripts');t=set(re.findall(r'def (\w+)\(',open('kltags.py').read()))-{'lookup','days_later','format_date_string'};A={'today','coupon_code','unsubscribe','unsubscribe_link','manage_preferences','manage_preferences_link','web_view','web_view_link'};sys.exit(0 if t==A else 1)" && echo "ok   kltags.py = Klaviyo-allowlist" || { echo "FOUT kltags.py wijkt af van de Klaviyo-allowlist"; fail=1; }
python3 -I -c "import sys;sys.argv=['q'];sys.path.insert(0,'$PWD/../../../scripts');import qa_render as q;f=q.tags_filters('{% manage_preferences_url %}{% unsubscribe_url %}{{ x|bogus }}')[0];sys.exit(0 if len(f)==3 else 1)" && echo "ok   allowlist weigert manage_preferences_url, unsubscribe_url, |bogus" || { echo "FOUT allowlist laat foute tags door"; fail=1; }
(cd /tmp && python3 -I "$OLDPWD/../../../scripts/qa_render.py" --static >/dev/null) && echo "ok   qa_render.py --static: alle mails groen" || { echo "FOUT qa_render.py --static (zie exports/qa/render-report.md)"; fail=1; }
exit $fail

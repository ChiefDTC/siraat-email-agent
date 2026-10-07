#!/bin/bash
# Bouwt en rendert alle flow-mails in klaviyo/templates/v3 (of alleen de opgegeven flowmappen).
# Gebruik: bash scripts/build_all.sh [checkout cart ...]
R=$(cd "$(dirname "$0")/.." && pwd)
FLOWS=${@:-checkout cart browse welcome post-purchase winback}
for f in $FLOWS; do d=$R/klaviyo/templates/v3/$f
  for s in $d/*.html; do case $s in *-preview*.html|*.klaviyo.html|*-preview-*.html) continue;; esac
    n=$(basename $s .html); python3 -I $R/scripts/build_template.py $s $d/assets $d/assets/klaviyo-urls.txt >/dev/null || { echo "FOUT $f/$n"; continue; }
    (cd $d && node $R/scripts/render_preview.js $n-preview.html previews/$n >/dev/null) && echo "ok $f/$n"
  done; done

"""Gedeelde helper (6 nov): wikkelt elk beeld zonder link in de link van de eerstvolgende link."""
def link_all(v):
    """6 nov (Homestead-review): elk beeld zonder link krijgt de link van de eerstvolgende link in de mail."""
    import re as _re
    out, pos, depth = [], 0, 0
    for m in _re.finditer(r'<a\b[^>]*>|</a>|<img\b[^>]*>', v):
        out.append(v[pos:m.start()]); tag = m.group(0); pos = m.end()
        if tag.startswith('<a'): depth += 1; out.append(tag); continue
        if tag == '</a>': depth = max(0, depth - 1); out.append(tag); continue
        if depth == 0 and 'width="1"' not in tag:
            ok = lambda x: x and 'unsubscribe' not in x and 'preferences' not in x and '-ft-' not in x and 'utm_content' in x
            nxt = _re.search(r'<a\b[^>]*href="([^"]+)"', v[m.end():])
            href = nxt.group(1) if nxt and ok(nxt.group(1)) else None
            if not href:
                prev = [h for h in _re.findall(r'<a\b[^>]*href="([^"]+)"', v[:m.start()]) if ok(h)]
                href = prev[-1] if prev else None
            if href:
                out.append('<a href="%s" style="text-decoration:none;">%s</a>' % (href, tag)); continue
        out.append(tag)
    out.append(v[pos:]); return ''.join(out)

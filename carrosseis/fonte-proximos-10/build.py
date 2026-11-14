import base64, os, json
from content import C, CTA_EB, AV
eb = base64.b64encode(open('ebook.png','rb').read()).decode()
CSS = open('base.css').read() + """
.item.term .n{font-size:38px;min-width:250px;padding-top:2px}
.note{margin-top:34px;font-family:LoraV;font-style:italic;font-size:36px;line-height:1.4;color:#E4DED0}
.note b{font-style:normal;color:#F3E2B8}
td{font-size:36px} th{font-size:26px}
"""
def page(i, n, body):
    return f"<!doctype html><html><head><meta charset='utf-8'><style>{CSS}</style></head><body>{body}<div class='foot'><span>FÁBRICA DE INVESTIDOR</span><span>{i}/{n}</span></div></body></html>"
def slide(s):
    t = s['t']; head = f"<div class='kick'>{s['kick']}</div><div class='rule'></div>"
    if t == 'cover':
        return f"<div class='wrap' id='w'>{head}<h1>{s['h']}</h1><div class='sub'>{s['sub']}</div></div><div class='coin'>R$</div><div class='swipe'>ARRASTA PRO LADO →</div>"
    if t == 'list':
        cls = 'item term' if s.get('terms') else 'item'
        it = ''.join(f"<div class='{cls}'><div class='n'>{a}</div><div class='t'>{b}</div></div>" for a, b in s['items'])
        note = f"<div class='note'>{s['note']}</div>" if s.get('note') else ''
        return f"<div class='wrap' id='w'>{head}<h2>{s['h']}</h2>{it}{note}</div>"
    if t == 'text':
        ps = ''.join(f"<p class='b'>{p}</p>" for p in s['ps'])
        return f"<div class='wrap' id='w'>{head}<h2>{s['h']}</h2>{ps}</div>"
    if t == 'table':
        th = ''.join(f"<th>{h}</th>" for h in s['head'])
        rows = ''.join('<tr>' + ''.join((f"<td class='k'>{c}</td>" if j == 0 else f"<td>{c}</td>") for j, c in enumerate(r)) + '</tr>' for r in s['rows'])
        note = f"<div class='note' style='font-size:30px'>{s['note']}</div>" if s.get('note') else ''
        return f"<div class='wrap' id='w'>{head}<table><tr>{th}</tr>{rows}</table>{note}</div>"
    if t == 'cta':
        ps = ''.join(f"<p class='b'>{p}</p>" for p in s['ps'])
        return (f"<div class='wrap' id='w'>{head}<h2>{s['h']}</h2>{ps}<p class='b'>Segue a @afabricadeinvestidor pra receber o próximo.</p>"
                f"<div class='btn'>O Método Tostão · link na bio</div></div><img class='ebook' src='data:image/png;base64,{eb}'>"
                f"<div class='src' style='bottom:130px'>Conteúdo educativo, não é recomendação de investimento.</div>")
man = []
for c in C:
    d = f"{c['date']}-{c['slug']}"; os.makedirs(d, exist_ok=True)
    n = len(c['slides'])
    for i, s in enumerate(c['slides'], 1): open(f'{d}/slide{i}.html', 'w').write(page(i, n, slide(s)))
    man.append(dict(dir=d, n=n, date=c['date'], text=c['caption'] + "\n" + CTA_EB + "\n" + AV, comment=c['comment']))
json.dump(man, open('manifest.json', 'w'), ensure_ascii=False, indent=1)
print(len(man))

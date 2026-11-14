import base64, json
eb = base64.b64encode(open('ebook.png','rb').read()).decode()
CSS = """
@font-face{font-family:LoraV;src:url('file:///usr/share/fonts/truetype/google-fonts/Lora-Variable.ttf');font-weight:400 700}
@font-face{font-family:LoraV;font-style:italic;src:url('file:///usr/share/fonts/truetype/google-fonts/Lora-Italic-Variable.ttf');font-weight:400 700}
*{margin:0;padding:0;box-sizing:border-box}
body{width:1080px;height:1350px;overflow:hidden;font-family:Inter,sans-serif;color:#ECE8DD;
 background:radial-gradient(ellipse 75% 60% at 40% 52%,#26372c 0%,#18231e 55%,#0f1513 100%);position:relative}
.wrap{position:absolute;left:96px;right:96px;top:110px}
.kick{font:600 26px Inter;letter-spacing:.32em;color:#D9B26A;text-transform:uppercase}
.rule{width:110px;height:2px;background:#B8914E;margin:26px 0 40px}
h1{font-family:LoraV;font-weight:700;font-size:96px;line-height:1.06;color:#F3E2B8}
h1 em{font-style:normal;color:#D9AE5E}
h2{font-family:LoraV;font-weight:700;font-size:74px;line-height:1.1;color:#F3E2B8}
h2 em{font-style:normal;color:#D9AE5E}
.sub{font-family:LoraV;font-style:italic;font-size:42px;line-height:1.4;color:#E4DED0;margin-top:34px}
p.b{font-size:38px;line-height:1.5;color:#E4DED0;margin-top:26px}
.item{display:flex;gap:30px;align-items:flex-start;padding:30px 0;border-bottom:1px solid rgba(217,178,106,.18)}
.n{font-family:LoraV;font-weight:700;font-size:46px;color:#D9AE5E;min-width:56px;line-height:1.1}
.t{font-size:38px;line-height:1.42}
.t b{color:#F3E2B8;font-weight:600}
table{width:100%;border-collapse:collapse;margin-top:10px}
th{font:600 26px Inter;letter-spacing:.2em;color:#D9B26A;text-align:left;padding:0 0 22px}
td{font-size:31px;line-height:1.38;padding:24px 18px 24px 0;border-top:1px solid rgba(217,178,106,.18);vertical-align:top}
td.k{font-family:LoraV;font-weight:700;color:#F3E2B8;font-size:32px;width:240px}
.big{font-family:LoraV;font-weight:700;font-size:200px;color:#D9AE5E;line-height:1}
.foot{position:absolute;left:96px;right:96px;bottom:70px;display:flex;justify-content:space-between;font:600 22px Inter;letter-spacing:.3em;color:#8F8A78}
.swipe{position:absolute;left:96px;bottom:150px;font:600 30px Inter;letter-spacing:.14em;color:#D9B26A}
.src{position:absolute;left:96px;right:96px;bottom:140px;font-family:LoraV;font-style:italic;font-size:24px;color:#9C9686;line-height:1.45}
.coin{position:absolute;right:-70px;top:760px;width:380px;height:380px;border-radius:50%;
 background:radial-gradient(circle at 38% 34%,#f6dc95 0%,#d7a94e 45%,#a87a2c 80%,#7c561c 100%);
 box-shadow:0 30px 70px rgba(0,0,0,.55), inset 0 0 0 14px rgba(255,236,170,.25), inset 0 0 0 30px rgba(120,80,20,.25);
 display:flex;align-items:center;justify-content:center;font-family:LoraV;font-weight:700;font-size:150px;color:#7a5418;text-shadow:0 2px 0 rgba(255,230,160,.5)}
.btn{display:inline-block;margin-top:46px;padding:26px 44px;border-radius:60px;background:linear-gradient(180deg,#ecc77d,#d4a656);color:#1a1a12;font:700 34px Inter}
.ebook{position:absolute;left:640px;top:760px;width:380px}
.pill{display:inline-block;padding:10px 26px;border:2px solid #B8914E;border-radius:40px;font:600 26px Inter;letter-spacing:.12em;color:#D9B26A;margin-bottom:26px}
"""
N = 7
def page(i, body, extra=''):
    return f"<!doctype html><html><head><meta charset='utf-8'><style>{CSS}</style></head><body>{body}{extra}<div class='foot'><span>FÁBRICA DE INVESTIDOR</span><span>{i}/{N}</span></div></body></html>"
S = []
S.append(page(1, """<div class='wrap'><div class='kick'>Ação x ETF</div><div class='rule'></div>
<h1>Escolher <em>uma</em> empresa ou levar a <em>cesta</em> inteira?</h1>
<div class='sub'>A diferença entre ação e ETF, sem complicação. Salva pra consultar depois.</div></div>
<div class='coin'>R$</div><div class='swipe'>ARRASTA PRO LADO →</div>"""))
S.append(page(2, """<div class='wrap'><div class='kick'>Ação · você escolhe</div><div class='rule'></div>
<h2>Um pedacinho de <em>uma</em> empresa.</h2>
<div class='item'><div class='n'>1</div><div class='t'>Comprou uma ação, virou <b>sócio</b> daquela empresa. Ex.: PETR4, da Petrobras.</div></div>
<div class='item'><div class='n'>2</div><div class='t'><b>Você decide</b> qual comprar, quanto e quando vender.</div></div>
<div class='item'><div class='n'>3</div><div class='t'>Se a empresa vai mal, <b>você sente sozinho</b> o tombo dela.</div></div></div>"""))
S.append(page(3, """<div class='wrap'><div class='kick'>ETF · você leva a cesta</div><div class='rule'></div>
<h2>Um fundo que <em>copia</em> um índice.</h2>
<div class='item'><div class='n'>1</div><div class='t'>É negociado na Bolsa <b>como uma ação</b>, com código e cotação.</div></div>
<div class='item'><div class='n'>2</div><div class='t'>Ex.: o <b>BOVA11</b> copia o Ibovespa, que tem <b>76 ações</b> na carteira de set. a dez./2026.</div></div>
<div class='item'><div class='n'>3</div><div class='t'>Com uma cota, você leva <b>um pedacinho de cada</b> empresa do índice.</div></div></div>"""))
S.append(page(4, """<div class='wrap'><div class='kick'>Lado a lado</div><div class='rule'></div>
<table><tr><th></th><th>AÇÃO</th><th>ETF</th></tr>
<tr><td class='k'>Diversificação</td><td>Você monta, empresa por empresa</td><td>Já vem com várias empresas</td></tr>
<tr><td class='k'>Quem escolhe</td><td>Você analisa cada empresa</td><td>O índice define a carteira</td></tr>
<tr><td class='k'>Custo</td><td>Sem taxa de administração</td><td>Tem taxa (BOVA11: 0,10% ao ano)</td></tr>
<tr><td class='k'>Imposto</td><td>15% no lucro; isento se vender até R$ 20 mil no mês</td><td>15% no lucro, sem a isenção de R$ 20 mil</td></tr>
</table></div>
<div class='src'>Fontes: BlackRock (página do BOVA11, out/2026); B3 Bora Investir (IR de ETFs, 2026); Contábeis (isenção de R$ 20 mil, art. 35 do RIR).</div>"""))
S.append(page(5, """<div class='wrap'><div class='kick'>Mas atenção</div><div class='rule'></div>
<h2>Cesta não é <em>escudo.</em></h2>
<p class='b'>O ETF sobe e desce junto com o índice. Se a Bolsa inteira cai, ele cai também.</p>
<p class='b'>Diversificar diminui o peso de uma empresa ruim, mas <b style='color:#F3E2B8'>não elimina o risco</b> de perder dinheiro.</p>
<p class='b'>E tanto ação quanto ETF de ações são renda variável: o preço muda todo dia.</p></div>"""))
S.append(page(6, """<div class='wrap'><div class='kick'>O dado</div><div class='rule'></div>
<div class='big'>929 mil</div>
<h2 style='font-size:60px;margin-top:20px'>investidores em ETFs na B3 em <em>agosto de 2026.</em></h2>
<p class='b'>Uma alta de 39% em 12 meses. Hoje a B3 tem 219 ETFs emitidos no Brasil.</p></div>
<div class='src'>Fonte: B3 · Bora Investir, "Mercado de ETFs tem crescimento exponencial e se aproxima de 1 milhão de investidores", 17/09/2026.</div>"""))
S.append(page(7, f"""<div class='wrap'><div class='kick'>Salva este post</div><div class='rule'></div>
<h2>Não é sobre qual é <em>melhor.</em></h2>
<p class='b'>É sobre entender o que você está comprando. Uns preferem escolher empresa por empresa; outros, levar a cesta.</p>
<p class='b'>Segunda, 12h, tem vídeo do Tostão explicando o ETF. Segue a @afabricadeinvestidor.</p>
<div class='btn'>O Método Tostão · link na bio</div></div>
<img class='ebook' src='data:image/png;base64,{eb}'>
<div class='src' style='bottom:130px'>Conteúdo educativo, não é recomendação de investimento.</div>"""))
for i, s in enumerate(S, 1): open(f'slide{i}.html', 'w').write(s)

# 10 carrosséis (15/11 a 24/11/2026). Tipos de slide: cover, list, text, big, table, cta
C = []
def add(slug, date, slides, caption, comment): C.append(dict(slug=slug, date=date, slides=slides, caption=caption, comment=comment))
CTA_EB = "📘 O passo a passo completo está no ebook O Método Tostão. Link na bio."
AV = "⚠️ Conteúdo educativo, não é recomendação de investimento."

add('glossario-do-investidor', '2026-11-15', [
 dict(t='cover', kick='Glossário', h="7 palavras que <em>todo</em> investidor precisa entender", sub='Sem economês. Salva e consulta sempre que travar numa delas.'),
 dict(t='list', kick='Parte 1', h='O <em>básico</em> do básico.', items=[('Rentabilidade', 'quanto o investimento rendeu num período, em %.'), ('Liquidez', 'a rapidez pra transformar o investimento em dinheiro na conta.'), ('Risco', 'a chance de o resultado ser diferente do esperado, inclusive de perder.')], terms=True),
 dict(t='list', kick='Parte 2', h='As <em>siglas</em> do jornal.', items=[('Selic', 'a taxa básica de juros do Brasil, definida pelo Copom.'), ('CDI', 'a taxa que os bancos usam entre si; anda colada na Selic.'), ('IPCA', 'o índice oficial da inflação: mede quanto os preços subiram.')], terms=True),
 dict(t='list', kick='Parte 3', h='A <em>estratégia</em>.', items=[('Diversificação', 'espalhar o dinheiro em vários investimentos pra um tombo não derrubar tudo.')], terms=True,
      note='Bônus: <b>aporte</b> é o dinheiro novo que você coloca todo mês.'),
 dict(t='text', kick='Mas atenção', h='Entender a palavra <em>não</em> é entender o produto.', ps=['Antes de investir, leia a lâmina ou o documento do produto e pergunte: quanto rende, quanto custa, quando eu resgato e qual é o risco?']),
 dict(t='cta', kick='Salva este post', h='Palavra difícil <em>não</em> é desculpa.', ps=['Qual termo de investimento ainda te confunde? Comenta que ele pode virar o próximo post.']),
], "7 palavras que todo investidor precisa entender. 📖\n\nRentabilidade, liquidez, risco, Selic, CDI, IPCA e diversificação, explicados sem economês.\nSalva e consulta sempre que uma delas aparecer.\n\nQual termo ainda te confunde? Comenta 👇", "Qual palavra de investimento você queria que alguém te explicasse? 👇")

add('5-perguntas-antes-de-investir', '2026-11-16', [
 dict(t='cover', kick='Antes de investir', h="5 perguntas que <em>salvam</em> o seu dinheiro", sub='Vale pra qualquer produto: do CDB à criptomoeda. Arrasta.'),
 dict(t='list', kick='Perguntas 1 e 2', h='Rende e <em>custa</em> quanto?', items=[('1', '<b>Quanto rende?</b> Em % ao ano, e atrelado a quê (CDI, IPCA, prefixado).'), ('2', '<b>Quanto custa?</b> Taxa de administração, de custódia, de performance, imposto.')]),
 dict(t='list', kick='Perguntas 3 e 4', h='Quando e <em>quem</em>?', items=[('3', '<b>Quando posso resgatar?</b> Na hora, em alguns dias ou só no vencimento?'), ('4', '<b>Quem garante?</b> O governo, o FGC, a empresa… ou ninguém?')]),
 dict(t='list', kick='Pergunta 5', h='E se der <em>errado</em>?', items=[('5', '<b>Qual é o risco?</b> Quanto eu posso perder no pior cenário, e eu aguento isso?')], note='Se ninguém consegue responder as 5 com clareza, é sinal de alerta.'),
 dict(t='text', kick='Mas atenção', h='Promessa de lucro <em>garantido</em> e alto é alerta vermelho.', ps=['Rendimento muito acima do mercado, pressa pra você decidir e "só hoje" são sinais clássicos de golpe.']),
 dict(t='cta', kick='Salva este post', h='Pergunta <em>não</em> custa nada.', ps=['Manda pra alguém que vive recebendo "oportunidade imperdível" no WhatsApp.']),
], "5 perguntas que salvam o seu dinheiro antes de investir em qualquer coisa. 🔎\n\nQuanto rende? Quanto custa? Quando resgato? Quem garante? Qual o risco?\nSe ninguém responde as 5 com clareza, desconfia.\n\nManda pra quem vive recebendo \"oportunidade imperdível\" 👇", "Qual dessas perguntas você nunca tinha feito? 👇")

add('diversificacao-por-objetivo', '2026-11-17', [
 dict(t='cover', kick='Diversificação', h="Não coloque todos os <em>ovos</em> na mesma cesta", sub='Um jeito simples de dividir: pelo prazo de cada objetivo.'),
 dict(t='text', kick='A ideia', h='Cada objetivo tem um <em>prazo</em>.', ps=['Dinheiro que você vai usar logo não pode ficar onde o preço sobe e desce todo dia.', 'Dinheiro pra daqui a 10 anos aguenta mais oscilação no caminho.']),
 dict(t='list', kick='Na prática', h='Três <em>gavetas</em>.', items=[('Curto', '<b>até 1 ano</b>: reserva e contas. Busca segurança e liquidez diária.'), ('Médio', '<b>1 a 5 anos</b>: viagem, carro, entrada. Renda fixa com prazo compatível.'), ('Longo', '<b>5+ anos</b>: aposentadoria. Pode ter uma parte em renda variável.')], terms=True),
 dict(t='text', kick='Dentro de cada gaveta', h='Também <em>espalhe</em>.', ps=['Mais de um emissor, mais de um tipo de título, mais de uma empresa.', 'Um ETF, por exemplo, já é uma cesta com várias ações.']),
 dict(t='text', kick='Mas atenção', h='Diversificar <em>reduz</em> o risco, não zera.', ps=['E diversificar demais, sem entender o que comprou, também atrapalha. Menos produtos bem entendidos valem mais que muitos no escuro.']),
 dict(t='cta', kick='Salva este post', h='Uma cesta por <em>objetivo.</em>', ps=['Quais são as suas três gavetas hoje? Comenta o seu principal objetivo.']),
], "Não coloque todos os ovos na mesma cesta. 🥚🧺\n\nUm jeito simples de diversificar: separar o dinheiro em gavetas pelo prazo de cada objetivo (curto, médio e longo) e espalhar dentro de cada uma.\nSalva pra montar as suas.\n\nQual é o seu principal objetivo hoje? Comenta 👇", "Seu objetivo principal é de curto, médio ou longo prazo? 👇")

add('liquidez-d0-d1-d30', '2026-11-18', [
 dict(t='cover', kick='Liquidez', h="D+0, D+1, D+30: quando o dinheiro <em>volta</em>?", sub='O detalhe que mais pega iniciante de surpresa. Arrasta.'),
 dict(t='text', kick='O que é', h='Liquidez é <em>velocidade</em>.', ps=['É quanto tempo leva entre você pedir o resgate e o dinheiro cair na conta.', 'O "D" é o dia do pedido. O número é quantos dias depois o dinheiro chega (úteis ou corridos, conforme a regra do produto).']),
 dict(t='list', kick='Exemplos', h='Lendo o <em>código</em>.', items=[('D+0', 'cai no mesmo dia do pedido.'), ('D+1', 'cai no dia útil seguinte.'), ('D+30', 'cai cerca de 30 dias depois do pedido.')], terms=True),
 dict(t='text', kick='Pegadinha', h='Liquidez <em>no vencimento</em>.', ps=['Alguns produtos só devolvem o dinheiro na data final. Antes disso, ou não dá pra sacar, ou dá vendendo a preço de mercado, que pode ser menor.']),
 dict(t='text', kick='Regra de ouro', h='Reserva de emergência pede liquidez <em>diária</em>.', ps=['Emergência não espera 30 dias. Deixe a reserva onde dá pra resgatar rápido e com baixo risco.']),
 dict(t='cta', kick='Salva este post', h='Olha o <em>D+</em> antes de investir.', ps=['Você já precisou do dinheiro e descobriu que ele demorava pra voltar? Conta aqui.']),
], "D+0, D+1, D+30: quando o seu dinheiro volta pra conta? ⏳\n\nLiquidez é a velocidade do resgate. O número depois do D é quantos dias úteis o dinheiro leva pra cair.\nE cuidado com a liquidez só no vencimento.\n\nJá passou aperto por causa disso? Conta 👇", "Você sabe a liquidez de onde está o seu dinheiro hoje? 👇")

add('regra-do-72', '2026-11-19', [
 dict(t='cover', kick='Regra do 72', h="Em quanto tempo o seu dinheiro <em>dobra</em>?", sub='Uma conta de cabeça que todo investidor deveria saber.'),
 dict(t='text', kick='A conta', h='72 ÷ taxa ao ano = anos pra <em>dobrar</em>.', ps=['É uma aproximação dos juros compostos. Funciona bem para taxas entre 4% e 15% ao ano.']),
 dict(t='table', kick='Exemplos', head=['Taxa ao ano', 'Dobra em'], rows=[['6%', '≈ 12 anos'], ['8%', '≈ 9 anos'], ['9%', '≈ 8 anos'], ['12%', '≈ 6 anos']], note='Taxas ilustrativas, sem considerar imposto e inflação.'),
 dict(t='text', kick='Ao contrário', h='Funciona pra <em>dívida</em> também.', ps=['Uma dívida que cresce 12% ao ano dobra em cerca de 6 anos. Se os juros são ao mês, a conta fica assustadora rápido.']),
 dict(t='text', kick='Mas atenção', h='Dobrar <em>no papel</em> não é dobrar o poder de compra.', ps=['Desconte a inflação e o imposto pra saber o ganho real. Por isso compare sempre a taxa com o IPCA.']),
 dict(t='cta', kick='Salva este post', h='72 dividido pela <em>taxa.</em>', ps=['Faz a conta com o seu investimento e comenta em quantos anos ele dobra.']),
], "Em quanto tempo o seu dinheiro dobra? ✖️2\n\nRegra do 72: divida 72 pela taxa ao ano. A 6% ao ano, cerca de 12 anos; a 12%, cerca de 6.\nE a mesma conta vale pras dívidas.\n\nFaz a conta com o seu e comenta 👇", "Fez a conta? Em quantos anos o seu dinheiro dobra? 👇")

add('perfil-de-investidor', '2026-11-20', [
 dict(t='cover', kick='Perfil de investidor', h="Conservador, moderado ou <em>arrojado</em>?", sub='O teste que a corretora te pede tem um motivo. Arrasta.'),
 dict(t='text', kick='O que é', h='Suitability = <em>adequação</em>.', ps=['Pela regra da CVM (Resolução 30), bancos e corretoras precisam conhecer o seu perfil antes de recomendar produtos.', 'O questionário olha seus objetivos, prazo, renda e quanto risco você aguenta.']),
 dict(t='list', kick='Os três perfis', h='Qual é o <em>seu</em>?', items=[('Conservador', 'prioriza segurança e liquidez; aceita pouca oscilação.'), ('Moderado', 'aceita alguma oscilação em parte do dinheiro pra buscar mais retorno.'), ('Arrojado', 'aceita mais oscilação e perdas no curto prazo pensando no longo.')], terms=True),
 dict(t='text', kick='Dica', h='Responda com <em>sinceridade.</em>', ps=['Marcar "arrojado" só pra liberar produto é perigoso. O perfil serve pra te proteger, não pra te barrar.']),
 dict(t='text', kick='Mas atenção', h='Perfil <em>muda</em> com a vida.', ps=['Casou, teve filho, mudou de emprego, chegou perto de um objetivo? Refaça o questionário.']),
 dict(t='cta', kick='Salva este post', h='Conheça seu perfil <em>antes</em> do produto.', ps=['Qual deu o seu? Comenta conservador, moderado ou arrojado.']),
], "Conservador, moderado ou arrojado? 🧭\n\nO questionário de perfil (suitability) é exigido pela CVM pra que bancos e corretoras te ofereçam produtos adequados.\nResponda com sinceridade e refaça quando a vida mudar.\n\nQual deu o seu? Comenta 👇", "Qual é o seu perfil: conservador, moderado ou arrojado? 👇")

add('renda-fixa-x-renda-variavel', '2026-11-21', [
 dict(t='cover', kick='O básico', h="Renda fixa x renda <em>variável</em>", sub='A primeira divisão do mundo dos investimentos. Arrasta.'),
 dict(t='text', kick='Renda fixa', h='Você <em>empresta</em> dinheiro.', ps=['Para o governo, um banco ou uma empresa. Em troca, recebe juros numa regra combinada antes: prefixado, atrelado ao CDI ou à inflação.', 'Ex.: Tesouro Direto, CDB, LCI, LCA.']),
 dict(t='text', kick='Renda variável', h='Você vira <em>dono</em> de um pedaço.', ps=['De uma empresa (ações), de imóveis (fundos imobiliários) ou de uma cesta (ETFs).', 'O retorno não é combinado: depende do preço e dos resultados.']),
 dict(t='table', kick='Lado a lado', head=['', 'Renda fixa', 'Renda variável'], rows=[['Retorno', 'regra conhecida', 'imprevisível'], ['Oscilação', 'menor', 'maior'], ['Bom pra', 'reserva e prazos curtos', 'objetivos longos']]),
 dict(t='text', kick='Mas atenção', h='"Fixa" não quer dizer <em>sem risco</em>.', ps=['Se você vender antes do vencimento, o preço pode estar menor. E o emissor pode ter problemas. Leia sempre quem garante.']),
 dict(t='cta', kick='Salva este post', h='Emprestar ou ser <em>sócio</em>?', ps=['A maioria das carteiras tem um pouco dos dois. Hoje o seu dinheiro está em qual?']),
], "Renda fixa x renda variável: emprestar ou ser sócio? ⚖️\n\nNa renda fixa você empresta e recebe juros numa regra combinada. Na variável você vira dono de um pedaço e o retorno depende do preço.\n\nHoje seu dinheiro está em qual? Comenta 👇", "Seu dinheiro hoje está mais na renda fixa ou na variável? 👇")

add('6-erros-de-iniciante', '2026-11-22', [
 dict(t='cover', kick='Começando a investir', h="6 erros que quase <em>todo</em> iniciante comete", sub='Se identificou com algum? Normal. O importante é corrigir.'),
 dict(t='list', kick='Erros 1 a 3', h='Antes de <em>começar</em>.', items=[('1', 'Investir antes de montar a <b>reserva de emergência</b>.'), ('2', 'Investir com <b>dívida cara</b> aberta, como cartão e cheque especial.'), ('3', 'Comprar o que <b>não entende</b> porque alguém disse que rende muito.')]),
 dict(t='list', kick='Erros 4 a 6', h='Depois que <em>começa</em>.', items=[('4', 'Olhar o saldo <b>todo dia</b> e vender no primeiro susto.'), ('5', '<b>Ignorar os custos</b>: taxas e imposto comem o rendimento.'), ('6', 'Esperar o <b>"momento certo"</b> e nunca começar.')]),
 dict(t='text', kick='O antídoto', h='Constância vence <em>pressa.</em>', ps=['Aporte todo mês, mesmo pouco, num investimento que você entende. Revise a carteira de tempos em tempos, não de hora em hora.']),
 dict(t='text', kick='Mas atenção', h='Errar <em>pequeno</em> faz parte.', ps=['Começar com pouco serve pra isso: aprender sem colocar em risco o dinheiro que você não pode perder.']),
 dict(t='cta', kick='Salva este post', h='Qual desses foi o <em>seu</em>?', ps=['Comenta o número do erro que você já cometeu. Sem julgamento.']),
], "6 erros que quase todo iniciante comete. 🚧\n\nInvestir sem reserva, com dívida cara, sem entender o produto, vender no primeiro susto, ignorar custos e esperar o momento certo.\n\nQual foi o seu? Comenta o número 👇", "Comenta o número do erro que você já cometeu 👇")

add('cet-antes-do-emprestimo', '2026-11-23', [
 dict(t='cover', kick='Empréstimo', h="Olhe o <em>CET</em> antes de assinar", sub='A taxa de juros não conta a história toda. Arrasta.'),
 dict(t='text', kick='O que é', h='CET = Custo Efetivo <em>Total</em>.', ps=['É o custo de verdade do crédito: juros + tarifas + seguros + impostos (como o IOF) + outras despesas.', 'Pela regra do Conselho Monetário Nacional (Resolução 3.517/2007), o banco deve informar o CET antes da contratação.']),
 dict(t='text', kick='Por que importa', h='Juros <em>parecidos</em>, custos diferentes.', ps=['Dois empréstimos com a mesma taxa de juros podem ter CETs bem diferentes por causa de tarifas e seguros embutidos.']),
 dict(t='list', kick='Checklist', h='Antes de <em>assinar</em>.', items=[('1', 'Peça o <b>CET ao ano</b> por escrito.'), ('2', 'Compare o CET de <b>pelo menos 3</b> instituições.'), ('3', 'Veja se há <b>seguro embutido</b>: você pode recusar o que não quer.'), ('4', 'Confira se a <b>parcela cabe</b> no orçamento sem aperto.')]),
 dict(t='text', kick='Mas atenção', h='O melhor empréstimo é o que você <em>não precisa</em> pegar.', ps=['Se for pra consumo, vale esperar e juntar. Se for pra trocar dívida cara por uma mais barata, aí pode fazer sentido.']),
 dict(t='cta', kick='Salva este post', h='Compare o CET, não a <em>propaganda.</em>', ps=['Manda pra quem está pensando em pegar um empréstimo.']),
], "Vai pegar empréstimo? Olhe o CET antes de assinar. 🧾\n\nO Custo Efetivo Total soma juros, tarifas, seguros e impostos. O banco deve informar antes da contratação.\nCompare o CET de pelo menos 3 lugares.\n\nManda pra quem está pensando em pegar crédito 👇", "Você já comparou o CET antes de pegar um empréstimo? 👇")

add('dinheiro-a-dois', '2026-11-24', [
 dict(t='cover', kick='Dinheiro a dois', h="5 combinados pra dinheiro não virar <em>briga</em>", sub='Vale pra casal, família ou quem divide a casa.'),
 dict(t='list', kick='Combinados 1 a 3', h='Abrir o <em>jogo</em>.', items=[('1', '<b>Conversa marcada</b>, uma vez por mês, sem ser no meio da briga.'), ('2', '<b>Números na mesa</b>: renda, contas fixas e dívidas de cada um.'), ('3', '<b>Regra de divisão</b> das contas: meio a meio ou proporcional à renda.')]),
 dict(t='list', kick='Combinados 4 e 5', h='Espaço e <em>sonho</em>.', items=[('4', 'Um <b>valor livre</b> pra cada um gastar sem dar satisfação.'), ('5', 'Um <b>objetivo em comum</b> com valor e prazo: viagem, casa, reserva.')]),
 dict(t='text', kick='Dica', h='Combine um <em>limite</em> de consulta.', ps=['Ex.: compras acima de um valor combinado, só depois de conversar. Evita surpresa na fatura.']),
 dict(t='text', kick='Mas atenção', h='Dinheiro não pode virar <em>controle.</em>', ps=['Os dois precisam ter acesso às informações e voz nas decisões. Transparência vale pros dois lados.']),
 dict(t='cta', kick='Salva este post', h='Marca quem <em>divide</em> as contas com você.', ps=['Qual desses combinados vocês já têm? Comenta.']),
], "5 combinados pra dinheiro não virar briga. 🤝\n\nConversa marcada, números na mesa, regra de divisão, valor livre pra cada um e um objetivo em comum.\n\nMarca quem divide as contas com você 👇", "Qual desses combinados vocês já têm em casa? 👇")

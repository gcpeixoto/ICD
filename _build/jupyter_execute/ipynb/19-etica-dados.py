#!/usr/bin/env python
# coding: utf-8

# # Ciência de dados e ética

# _Ética_ é uma área de estudo da Filosofia que se preocupa em resolver questões da moralidade humana. Tendo suas origens nos pensadores gregos mais antigos, a ética se preocupa em delimitar as fronteiras de conceitos tomados como antagônicos, tais como  certo e errado, bom e mau, justo e injusto.
# 
# No âmbito profissional, um dos atos mais solenes que se conhece é o [juramento de Hipócrates](https://cremers.org.br/juramento-de-hipocrates/), que embasa o compromisso dos médicos para com seus pacientes. Desde o século V a.C., o texto original sofreu modificações até que, em 2017, a Associação Médica Mundial estabeleceu o _Compromisso do Médico_. Alguns recortes destacáveis são: 
# 
# - _"guardarei o máximo respeito pela vida humana"_;
# - _"respeitarei os segredos que me forem confiados_";
# - _"não usarei os meus conhecimentos (...) para violar direitos humanos e liberdades civis, mesmo sob ameaça."_
# 
# O juramento médico inspira um comportamento de "fazer as coisas corretamente" e "não causar danos" a seus pacientes. Na profissão de cientista de dados, cuidar dos dados é também uma atitude que perpassa os campos da ética e da moralidade. Ao lidar com dados, cruzamos as tênues fronteiras da privacidade, do viés, da orientação e do acesso à informação privilegiada. Então, uma maneira de superar dilemas éticos no mundo dos dados é estabelecer critérios de governança e seguir as melhores práticas de conformidade e legalidade.
# 
# 
# Neste capítulo, faremos uma introdução ao tema da _ética em dados_, recomendando materiais para que você adquira uma formação ampliada neste tema de grande importância nos tempos atuais. Grande parte do texto são excertos de publicações sobre o tema.
# 

# ## Ética em dados
# 
# De acordo com [Floridi e Taddeo](https://royalsocietypublishing.org/doi/pdf/10.1098/rsta.2016.0360), a _ética dos dados_ é um novo ramo da ética que estuda e avalia problemas morais em diferentes domínios a fim de formular soluções moralmente boas, tais como condutas e valores corretos. A ética dos dados abrange
# 
# - dados, em si, (geração, gravação, curadoria, processamento, dissemniação, compartilhamento e uso);
# - algoritmos (inteligência artificial, agentes artificiais, aprendizagem de máquina e robótica) e 
# - práticas (inovação responsável, programação, _hacking_ e códigos profissionais).
# 
# Segundo os autores, 
# 
# > _"A ciência de dados, como a última fase da revolução da informação, está agora levando a uma mudança adicional no nível de abstração [das inquirições éticas], no qual nossa análise ética pode ser desenvolvida da maneira mais proveitosa. Em poucas décadas, passamos a compreender que não se trata de uma tecnologia específica (computadores, tablets, telefones celulares, plataformas online, computação em nuvem e assim por diante), mas o que qualquer tecnologia digital manipula que representa o foco correto de nossas estratégias éticas. A mudança da ética da informação para a ética dos dados é provavelmente mais semântica do que conceitual, mas destaca a necessidade de nos concentrarmos no que está sendo tratado como a verdadeira invariante de nossas preocupações._"
# 
# A mudança no nível de abstração deu surgimento a três eixos de pesquisa: i) ética dos dados; ii) ética dos algoritmos; e iii) ética das práticas.
# 
# ### Ética dos dados
# 
# A ética dos dados se concentra em problemas éticos impostos pela coleta e análise de grandes conjuntos de dados e em questões que vão desde o uso dos grandes dados (_big data_) em pesquisas biomédicas e ciências sociais até a criação de perfis, publicidade, filantropia de dados e dados abertos. Tópicos estudados neste eixo estudam:
# 
# - identificação de indivíduos por meio de mineração de dados;
# - vinculação, fusão e reutilização de grandes conjuntos de dados;
# - riscos de privacidade, confiança e transparência;
# 
# ### Ética dos algoritmos
# 
# A ética dos algoritmos aborda as questões relacionados à complexidade e autonomia dos algoritmos, especialmente os que envolvem inteligência artificial, agentes artificiais e bots da internet, bem como aprendizado de máquina. Os desafios neste eixo estudam:
# 
# - responsabilidade moral (de designers e de cientistas de dados)
# - projeto ético e auditoria dos requisitos dos algoritmos 
# - avaliação de resultados potenciais indesejáveis (discriminação, promoção de conteúdo anti-social)
# 
# ### Ética das práticas
# 
# A ética das práticas (incluindo a ética profissional) aborda as questões relativas às responsabilidades das pessoas e organizações responsáveis por processos, estratégias e políticas de dados, incluindo cientistas de dados, com o objetivo de definir uma estrutura ética para moldar códigos profissionais sobre inovação, desenvolvimento e utilização responsáveis, que podem garantir práticas éticas que favoreçam o progresso da ciência de dados e a proteção dos direitos de indivíduos e grupos. As questões centrais nesta linha de análise são: 
# 
# - consentimento
# - privacidade do usuário e 
# - uso secundário.

# ## A Lei Geral de Proteção de Dados Pessoais (LGPD)
# 
# O texto a seguir é composto de excertos do [Guia LGPD](https://www.lgpdbrasil.com.br/ebooks/), produzido por Paulo Vinícius Carvalho Soares.
# 
# A _Lei Geral de Proteção de Dados Pessoais (LGPD)_ [(Lei 13709/2018)](http://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/Lei/L13709.htm), alterada pela Lei 13853/2019, tem o objetivo de proteger os direitos fundamentais de liberdade e de privacidade e o livre desenvolvimento da personalidade da pessoa natural. A LGPD segue uma tendência global adotada em mais de 120 países para proteção de dados pessoais contra o uso indevido deles, especialmente por empresas. A LGPD tem os seguintes fundamentos:
# 
# - proteção à privacidade;
# - autodeterminação informativa;
# - liberdade de expressão, informação, comunicação e opinião;
# - inviolabilidade da intimidade, honra e da imagem;
# - desenvolvimento econômico, tecnológico e inovação;
# - livre iniciativa, livre concorrência e a defesa do consumidor;
# - direitos humanos, livre desenvolvimento da personalidade, dignidade e exercício da cidadania.
# 
# 
# A LGPD se aplica:
# 
# - aos dados pessoais de indivíduos localizados no Brasil;
# - quando o tratamento se dá no Brasil;
# - quando houver oferta de bens e serviços para indivíduos no Brasil.
# 
# E não se aplica:
# 
# - para dados provenientes e destinados a outros países, que apenas transitem pelo território nacional;
# - para uso pessoal ou não comercial;
# - para fins jornalísticos, acadêmicos ou de segurança pública.

# ## Referências para aprofundamento
# 
# - [Portal LGPD Brasil](https://www.lgpdbrasil.com.br)
# - [Hand, D. J., Aspects of Data Ethics in a Changing World: Where Are We Now?](https://www.liebertpub.com/doi/pdfplus/10.1089/big.2018.0083)
# - [Floridi, L., Soft Ethics and the Governance of the Digital](https://link.springer.com/content/pdf/10.1007/s13347-018-0303-9.pdf)
# - [Richterich, A., The Big Data Agenda: Data Ethics and Critical Data Studies](https://library.oapen.org/bitstream/handle/20.500.12657/30155/649695.pdf?sequence=1)
# - [Floridi, L., Soft Ethics and the Governance of the Digital](https://link.springer.com/content/pdf/10.1007/s13347-018-0303-9.pdf)
# - [Hasselbalch, G., Making sense of data ethics. The powers behind the data ethics debate in European policymaking](https://www.econstor.eu/bitstream/10419/214073/1/IntPolRev-2019-2-1401.pdf)
# - [Floridi, L., Translating Principles into Practices of Digital Ethics: Five Risks of Being Unethical](https://link.springer.com/content/pdf/10.1007/s13347-019-00354-x.pdf)
# - [Oxford Internet Institute](https://digitalethicslab.oii.ox.ac.uk)

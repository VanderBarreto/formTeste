from django import forms



class ContactForm(forms.Form):
       
    
    descri_dcdescriptionabstract = "Descreva o escopo, foco ou objetivo da revista de maneira sucinta"
    dcdescriptionabstract = forms.CharField(widget=forms.Textarea,label='Descrição', help_text = descri_dcdescriptionabstract ,required=True)
    descri_dctitle = "O campo Título deve ser preenchido da mesma forma que o campo Key title, presente no registro da revista na rede ISSN. Essa inforFmação pode ser verificada no link: https://portal.issn.org/" 
    dctitle = forms.CharField(max_length=200, label='Título', help_text=descri_dctitle, required=True)
    descri_dctitleabbreviated = "O campo Título abreviado deve ser preenchido da mesma forma que o campo Abbreviated key title, presente no registro da revista na rede ISSN. Em alguns casos, essa informação pode ser verificada no link: https://portal.issn.org/"
    dctitleabbreviated = forms.CharField(max_length=100, label='Título abreviado', help_text=descri_dctitleabbreviated, required=False)
    descri_dctitleproper = "O campo Título próprio deve ser preenchido da mesma forma que o campo Title proper, presente no registro da revista na rede ISSN. Em alguns casos, essa informação pode ser verificada no link: https://portal.issn.org/"
    dctitleproper = forms.CharField(max_length=100, help_text=descri_dctitleproper, label='Título próprio',required=False)
    descri_dctitleother = "O campo Outros títulos pode ser preenchido da mesma forma que os campos Other title ou Variant title, presentes no registro da revista na rede ISSN. Em alguns casos, essas informações podem ser verificadas no link: https://portal.issn.org/"
    dctitleother = forms.CharField(max_length=100, help_text = descri_dctitleother, label='Outros Títulos',required=False)
    descri_dctitleprevious = "Caso a revista tenha descendido de outro título, indique-o,  de acordo com o campo Key title, presente no registro da revista na rede ISSN. O ISSN do título anterior deve ser colocado neste campo, ao final, entre colchetes. Em alguns casos, essa informação pode ser verificada no link: https://portal.issn.org/"
    dctitleprevious = forms.CharField(max_length=100, help_text = descri_dctitleprevious, label='Título anterior',required=False)
    descri_dctitlelater = "Caso a revista deixe de ser publicada com o título original, mas continue sendo com outro título, indique-o, de acordo com o campo \"Key title\", presente no registro da revista na rede ISSN.  O ISSN do título posterior deve ser colocado neste campo, ao final, entre colchetes. Em alguns casos, essa informação pode ser verificada no link: https://portal.issn.org/"
    dctitlelater = forms.CharField(max_length=100, help_text=descri_dctitlelater, label='Título posterior',required=False)
    descri_dcidentifierissn = "Informe o número de ISSN conforme consta no registro da revista na rede ISSN. Essa informação pode ser verificada no link: https://portal.issn.org/"
    dcidentifierissn = forms.CharField(max_length=100, label='ISSN', help_text = descri_dcidentifierissn, required=True)
    descri_dcidentifierissnl = "Informe o número de ISSN- L conforme consta no registro da revista na rede ISSN. Essa informação pode ser verificada no link: https://portal.issn.org/"
    dcidentifierissnl = forms.CharField(max_length=100, label='ISSN-L', help_text=descri_dcidentifierissnl, required=True)
    op_dcdescriptionsituation = [("", ""),("Vigente","Vigente"),("Descontinuada (deixou de ser publicada)","Descontinuada (deixou de ser publicada)")]
    descri_situation="Indique se a revista se encontra vigente ou se deixou de ser publicada."
    dcdescriptionsituation = forms.ChoiceField(choices=op_dcdescriptionsituation,label='Situação',help_text=descri_situation, required=True)
    descri_startyear="Informe o ano de início da publicação de acordo com o campo \"Dates of publication\", conforme consta no registro da revista na rede ISSN. Em alguns casos, essa informação pode ser verificada no link:https://portal.issn.org/"
    dcdatestartyear = forms.CharField(label = 'Ano de início de publicação',help_text=descri_startyear,required=True)
    desci_endyear="Caso a revista tenha deixado de ser publicada, informe o ano de publicação do último número, fascículo ou artigo."
    dcdateendyear = forms.CharField(label = 'Ano de finalização de publicação',help_text=desci_endyear,required=False)
    descri_url="Informe a URL da página inicial do site oficial de publicação."
    dcidentifierurl = forms.CharField(max_length=100, label='URL',help_text= descri_url, required=True)
   
    descri_interoperabilityprotocol="Indique a URL do protocolo de interoperabilidade utilizado pela revista para coleta dos seus documentos por outros sistemas de distribuição. Caso a revista utilize o software OJS, o protocolo de interoperabilidade padrão é o OAI-PMH. Para obtê-lo, basta digitar, ao final da URL, a expressão \"oai\". Caso a revista não seja editada em OJS, não esteja com o OAI-PMH habilitado ou utilize outro protocolo de interoperabilidade, sugerimos entrar em contato com o suporte técnico da revista. Por fim, caso a revista não utilize nenhum protocolo de interoperabilidade, deixe a questão em branco."
    dcidentifierinteroperabilityprotocol = forms.CharField(max_length=100, label='Protocolo de interoperabilidade',help_text=descri_interoperabilityprotocol, required=False)
    descri_persistentidentifier="Indique o link do identificador persistente atribuído à revista. Caso a revista não utilize nenhum identificador persistente, deixe a questão em branco. Identificador persistente é um identificador único de longa duração de um recurso na Internet que se mantém válido mesmo que a tecnologia de acesso ou a localização física do recurso identificado se modifique no tempo. Exemplos: DOI (Digital Object Identifier), Handle, URN, PURL, ARK."
    dcidentifierpersistentidentifier = forms.CharField(max_length=100, label='Identificador persistente',help_text =descri_persistentidentifier,required=False)
    descri_language="Selecione o (s) idioma (s) aceito (s) pela revista para submissão de documentos. Indique a resposta de acordo com as opções descritas na aba Opções de resposta. Caso as opções listadas não se adequem à realidade da revista, indique a resposta manualmente na caixa de texto."
    dclanguage = forms.CharField(max_length=100,label='Idioma de publicação',help_text = descri_language , required=True)    

    # Pagina dois
    
    descri_cnpq="Selecione as principais áreas do conhecimento em que a revista publica seus conteúdos, de acordo com a tabela de áreas do CNPq. Indique a resposta de acordo com as opções descritas na aba Opções de resposta. Solicita-se que sejam selecionadas somente as áreas de conhecimento em que a revista dá mais ênfase em suas publicações, não sendo aconselhável adicionar mais do que cinco entradas."
    dcsubjectcnpq = forms.CharField(max_length=200, label='Áreas do conhecimento',help_text=descri_cnpq,required=True)
    descri_name="Informe o nome completo e por extenso da instituição responsável pela edição da revista . A responsabilidade pela edição da revista deverá levar em consideração o nível hierárquico mais alto de afiliação. Por exemplo, uma universidade, e não seus departamentos, faculdades ou institutos. Todos esses organismos subordinados podem ser descritos no campo Organismo subordinado. Caso a revista não possua instituição responsável pela edição, indique “Publicação independente”. Exemplo de preenchimento:Universidade de Brasília (UnB).  "
    dcpublishername = forms.CharField(max_length=100, label='Instituição editora',help_text = descri_name,required=True)
    descri_subordinate="Informe o nome completo e por extenso do organismo subordinado à instituição editora que atua diretamente na publicação da revista. Considere como organismos subordinados: departamentos, faculdades, coordenações, institutos etc. Exemplo de preenchimento: Programa de Pós-Graduação em História (PPGHIS)."
    dcpublishersubordinate = forms.CharField(max_length=100, label='Organismo subordinado',help_text =descri_subordinate, required=False)
    descri_publisher="Indique a URL do cadastro da instituição editora em plataformas que geram um identificador único para instituição, como as plataformas GRID, ISNI e CADI por exemplo. Os endereços das plataformas GRID, ISNI e CADI são respectivamente: https://www.grid.ac/, http://www.grid.ac/, http://www.isni.org/, https://www.isni.org/ e http://di.cnpq.br/di/cadi/consultaInst.do , http://di.cnpq.br/di/cadi/consultaInst.do"
    dcidentifierpublisher = forms.CharField(max_length=100, label='Identificador da instituição editora',help_text= descri_publisher, required=False)
    op_dcpublisherlegalnature = [("",""),("Instituição privada","Instituição privada"),\
                                 ("Instituição pública","Instituição pública"),\
                                 ("Organização não governamental (ONG)","Organização não governamental (ONG)"),\
                                 ("Publicação independente","Publicação independente"),\
                                 ("Sociedade civil organizada (sindicatos, associações, cooperativas etc.)","Sociedade civil organizada (sindicatos, associações, cooperativas etc.)")]
    descri_legalnature="Indique a natureza jurídica da instituição editora da revista."
    dcpublisherlegalnature = forms.ChoiceField(choices=op_dcpublisherlegalnature, label='Natureza jurídica da instituição editora',help_text= descri_legalnature,required=True)
    descri_contributor="Informe, por extenso, o nome do principal editor responsável pela revista. O nome do editor responsável deve ser preenchido, preferencialmente, da mesma forma que o campo Nome do curriculo Lattes."
    dccontributoreditor = forms.CharField(max_length=100, label='Editor responsável',help_text = descri_contributor,required=True)
    descri_editor="Indique o código identificador do editor responsável em plataformas que geram um identificador único, como o currículo Lattes e ORCid.Os endereços das plataformas Lattes  e ORCid são, respectivamente: http://lattes.cnpq.br/ e https://orcid.org/" 
    dcidentifiereditor = forms.CharField(max_length=100, label='Identificador do editor responsável',help_text=descri_editor,required=True)
    descri_email="Informe o endereço de e-mail utilizado pela revista. Deve ser indicado o endereço de e-mail próprio da revista, evitando, portanto, e-mails pessoais, já que a mudança de editor pode acarretar perda do contato."
    dcidentifieremail = forms.EmailField(max_length=100, label='E-mail',help_text = descri_email, required=True) 
    descri_cep="Informe o código postal do local de contato da revista. Preenchimento: 99999-999."
    dcdescriptioncep = forms.CharField(max_length=100, label='Código Postal (CEP)',help_text=descri_cep,required=True)
    op_dcdescriptionstate = [("", ""),("Acre (AC)","Acre (AC)"),\
                             ("Alagoas (AL)","Alagoas (AL)"),\
                             ("Amapá  (AP)","Amapá (AP)"),\
                             ("Amazonas (AM)","Amazonas (AM)"),\
                             ("Bahia (BA)","Bahia (BA)"),\
                             ("Ceará (CE)","Ceará (CE)"),\
                             ("Distrito Federal (DF)","Distrito Federal (DF)"),\
                             ("Espírito Santo (ES)","Espírito Santo (ES)"),\
                             ("Goiás (GO)","Goiás (GO)"),\
                             ("Maranhão (MA)","Maranhão (MA)"),\
                             ("Mato Grosso (MT)","Mato Grosso (MT)"),\
                             ("Mato Grosso do Sul (MS)","Mato Grosso do Sul (MS)"),\
                             ("Minas Gerais (MG)","Minas Gerais (MG)"),\
                             ("Pará (PA)","Pará (PA)"),\
                             ("Paraíba (PB)","Paraíba (PB)"),\
                             ("Paraná (PR)","Paraná (PR)"),\
                             ("Pernambuco (PE)","Pernambuco (PE)"),\
                             ("Piauí (PI)","Piauí (PI)"),\
                             ("Rio de Janeiro (RJ)","Rio de Janeiro (RJ)"),\
                             ("Rio Grande do Norte (RN)","Rio Grande do Norte (RN)"),\
                             ("Rio Grande do Sul (RS)","Rio Grande do Sul (RS)"),\
                             ("Rondônia (RO)","Rondônia (RO)"),\
                             ("Roraima (RR)","Roraima (RR)"),\
                             ("Santa Catarina (SC)","Santa Catarina (SC)"),\
                             ("São Paulo (SP)","São Paulo (SP)"),\
                             ("Sergipe (SE)","Sergipe (SE)"),\
                             ("Tocantins (TO)","Tocantins (TO)")]
    descri_state="Informe o estado de acordo com o código postal."
    dcdescriptionstate = forms.ChoiceField(choices=op_dcdescriptionstate, label='Estado (UF)',help_text=descri_state, required=True)
    descri_city="Informe a cidade de acordo com o código postal."
    dcdescriptioncity = forms.CharField(max_length=100, label='Cidade',help_text=descri_city, required=True)
    descri_neighborhood="Informe bairro de acordo com o código postal."
    dcdescriptionneighborhood = forms.CharField(max_length=100, label='Bairro',help_text=descri_neighborhood, required=True)
    descri_street="Informe a rua, quadra ou similar de acordo com código postal."
    dcdescriptionstreet = forms.CharField(max_length=100, label='Rua/Quadra ou similar',help_text= descri_street, required=False)
    descri_building="Informe casa, prédio, sala ou similar de acordo com o código postal."
    dcdescriptionbuilding = forms.CharField(max_length=100, label='Casa/Prédio/Sala ou similar',help_text=descri_building, required=False)
    descri_phone="Informe o telefone de contato da revista. Deve ser indicado telefone próprio da revista, evitando, portanto, telefones pessoais, já que a mudança de editor pode acarretar perda do contato. Preenchimento: (99) 99999-9999."
    dcdescriptionphone = forms.CharField(max_length=100, label='Telefone',help_text =descri_phone, required=False)
    op_dcdescriptionmodalityofpublication = [("", ""),("Tradicional","Tradicional"),("Ahead of print","Ahead of print"),("Fluxo contínuo","Fluxo contínuo")]
    descri_modalityofpublication ="Indique a modalidade de publicação adotada pela revista.Tradicional:o editor espera a data final de publicação do fascículo para publicá-lo por completo, com todos os artigos. Ahead of print:os artigos são publicados à medida que passam pelo processo de avaliação, fechando-se o fascículo quando se atinge a data final de publicação.Fluxo contínuo:os artigos são publicados à medida que passam pelo processo de avaliação, o fluxo contínuo não prevê uma periodicidade, de modo que não se exige uma data final para para o fechamento ou publicação do fascículo."
    dcdescriptionmodalityofpublication = forms.ChoiceField(choices=op_dcdescriptionmodalityofpublication, label='Modalidades de publicação',help_text=descri_modalityofpublication, required=True)
    
    #Pagina Tres
    
    
    op_dcdescriptionperiodicity = [("", ""),("Publicação contínua","Publicação contínua"),("Anual","Anual"),("Bianual","Bianual"),("Bimestral","Bimestral"),("Diária","Diária"),("Mensal","Mensal"),("Quadrienal","Quadrienal"),("Quadrienal","Quadrienal"),("Quadrimestral","Quadrimestral"),("Quinzenal","Quinzenal"),("Semanal","Semanal"),("Semestral","Semestral"),("Trianual","Trianual"),("Trimestral","Trimestral")]
    descri_periodicity="Indique a periodicidade de publicação dos fascículos. Caso a revista publique na modalidade Fluxo contínuo esta deve indicar que publica de forma contínua."
    dcdescriptionperiodicity = forms.ChoiceField(choices=op_dcdescriptionperiodicity, label='Periodicidade do fascículo',help_text=descri_periodicity, required=True)
    op_dcdatemonthofpublication = [("", ""),("Publicação contínua","Publicação contínua"),("Janeiro","Janeiro"),("Fevereiro","Fevereiro"),("Março","Março"),("Abril","Abril"),("Maio","Maio"),("Junho","Junho"),("Julho","Julho"),("Agosto","Agosto"),("Setembro","Setembro"),("Outubro","Outubro"),("Novembro","Novembro"),("Dezembro","Dezembro")]
    descri_monthofpublication = "Indique o (s) mês (es) em que o (s) fascículo (s) é (são) publicado (s). Caso a revista publique na modalidade Fluxo contínuo esta deve indicar que publica de forma contínua. Para marcar mais de uma opção mantenha pressionada a tecla “Control” (Ctrl) e selecione as opções desejadas."
    dcdatemonthofpublication = forms.ChoiceField(choices=op_dcdatemonthofpublication, label='Mês de publicação do fascículo',help_text=descri_monthofpublication , required=True)
    op_period_exp = [("", ""),("Em branco","Em branco"),("Anual","Anual"),("Bianual","Bianual"),("Bimestral","Bimestral"),("Diária","Diária"),("Mensal","Mensal"),("Quadrienal","Quadrienal"),("Quadrienal","Quadrienal"),("Quadrimestral","Quadrimestral"),("Quinzenal","Quinzenal"),("Semanal","Semanal"),("Semestral","Semestral"),("Trianual","Trianual"),("Trimestral","Trimestral")]
    descri_editorialboardperiodicity="Caso a revista publique na modalidade Fluxo contínuo indique a periodicidade de publicação do expediente da revista. A publicação periódica do expediente, para publicações que atuam sob essa modalidade se faz essencial, pois, este indica quem são os responsáveis pelo processo de publicação dos artigos em determinado período. Caso a revista não publique em Fluxo continuo indique a resposta  “Em branco”."
    dcdescriptioneditorialboardperiodicity = forms.ChoiceField(choices=op_period_exp, label='Periodicidade de publicação do expediente',help_text= descri_editorialboardperiodicity,  required=False)
    op_mes_exp = [("", ""),("Janeiro","Janeiro"),("Fevereiro","Fevereiro"),("Março","Março"),("Abril","Abril"),("Maio","Maio"),("Junho","Junho"),("Julho","Julho"),("Agosto","Agosto"),("Setembro","Setembro"),("Outubro","Outubro"),("Novembro","Novembro"),("Dezembro","Dezembro")]
    descri_editorialboardmonthofpublication="Caso a revista publique modalidade Fluxo contínuo indique o (s) mês (es) em que é (são) publicado (s) o expediente. Para marcar mais de uma opção mantenha pressionada a tecla “Control” (Ctrl) e selecione as opções desejadas. Para desmarcar as opções mantenha pressionada a tecla “Control” (Ctrl) e selecione as opções que deseja desmarcar. Caso a revista não publique em Fluxo continuo deixe a questão em branco."
    dcdateeditorialboardmonthofpublication = forms.ChoiceField(choices=op_mes_exp, label='Mês de publicação do expediente',help_text= descri_editorialboardmonthofpublication, required=False)
    #dcdateeditorialboardmonthofpublication.widget.attrs.update(size='2')
    op_mod_pub_pares = [("", ""),("Avaliação aberta","Avaliação aberta"),("Avaliação duplo-cego","Avaliação duplo-cego"),("Avaliação simples-cega","Avaliação simples-cega")]
    #descri_peerreview="Informe o modelo de revisão por pares adotado pela revista.Avaliação aberta:as identidades dos autores e dos avaliadores são reveladas para ambos durante o processo de avaliação.Avaliação duplo-cega:as identidades dos autores e dos avaliadores não são reveladas para ambos durante o processo de avaliação. Avaliação simples-cega: as identidades dos autores são reveladas para os avaliadores, mas as dos avaliadores são mantidas em sigilo para os autores durante o processo de avaliação. "
    descri_peerreview="Informe o modelo de revisão por pares adotado pela revista."
    dcdescriptionpeerreview = forms.ChoiceField(choices=op_mod_pub_pares, label='Modalidade de avaliação por pares',help_text=descri_peerreview , required=True)
    op_dcdescriptionreviewerspublication= [("", ""),('A revista publica o nome de avaliadores dos documentos que foram aprovados na avaliação por pares','A revista publica o nome de avaliadores dos documentos que foram aprovados na avaliação por pares'),\
                                           ('A revista publica o nome de todos os avaliadores que participaram da avaliação de documentos por determinado período','A revista publica o nome de todos os avaliadores que participaram da avaliação de documentos por determinado período'),\
                                           ('A revista somente publica avaliadores que concordam com a publicação do seu nome','A revista somente publica avaliadores que concordam com a publicação do seu nome'),\
                                           ('A revista não publica o nome dos avaliadores, mas disponibiliza a lista de pesquisadores cadastrados como possíveis avaliadores','A revista não publica o nome dos avaliadores, mas disponibiliza a lista de pesquisadores cadastrados como possíveis avaliadores'),\
                                           ('A revista não publica, nem revela o nome dos avaliadores','A revista não publica, nem revela o nome dos avaliadores')] 
    descri_reviewerspublication="Indique em que situação o nome dos avaliadores podem ser publicados."
    dcdescriptionreviewerspublication = forms.ChoiceField(choices=op_dcdescriptionreviewerspublication, label='Publicação dos avaliadores',help_text= descri_reviewerspublication, required=True)
    op_dcdescriptionreviewerstypeofpublication= [("", ""),('A revista publica, no expediente, a listagem dos avaliadores que realizaram avaliações','A revista publica, no expediente, a listagem dos avaliadores que realizaram avaliações'),\
                                           ('A revista publica, no corpo do documento aprovado na avaliação por pares, o nome dos avaliadores responsáveis','A revista publica, no corpo do documento aprovado na avaliação por pares, o nome dos avaliadores responsáveis'),\
                                           ('A revista publica os pareceres resultantes das avaliações realizadas com o nome dos avaliadores','A revista publica os pareceres resultantes das avaliações realizadas com o nome dos avaliadores'),\
                                           ('A revista não publica o nome dos avaliadores, mas disponibiliza a lista de pesquisadores cadastrados como possíveis avaliadores','A revista não publica o nome dos avaliadores, mas disponibiliza a lista de pesquisadores cadastrados como possíveis avaliadores'),\
                                           ('A revista não publica, nem revela o nome dos avaliadores','A revista não publica, nem revela o nome dos avaliadores')] 
    descri_reviewerstypeofpublication="Indique a forma que se publica ou disponibiliza o nome dos avaliadores responsáveis pela revisão dos artigos submetidos à revista. Para marcar mais de uma opção mantenha pressionada a tecla “Control” (Ctrl) e selecione as opções desejadas."
    dcdescriptionreviewerstypeofpublication = forms.ChoiceField(choices=op_dcdescriptionreviewerstypeofpublication, label='Forma de publicação do nome dos avaliadores',help_text = descri_reviewerstypeofpublication,  required=True)
    op_dcdescriptionreviewersperiodicityofpublication = [("", ""),("Em branco","Em branco"),("Anual","Anual"),("Bianual","Bianual"),("Bimestral","Bimestral"),("Diária","Diária"),("Mensal","Mensal"),("Quadrienal","Quadrienal"),("Quadrienal","Quadrienal"),("Quadrimestral","Quadrimestral"),("Quinzenal","Quinzenal"),("Semanal","Semanal"),("Semestral","Semestral"),("Trianual","Trianual"),("Trimestral","Trimestral")]
    descri_reviewersperiodicityofpublication="Caso a revista publique os avaliadores via expediente, indique a periodicidade de publicação da lista de avaliadores que atuaram na revista. A periodicidade de publicação dos avaliadores não precisa, necessariamente, ser igual à periodicidade dos fascículos ou dos expedientes. A revista pode, por exemplo, publicar seus fascículos semestralmente e publicar os avaliadores via expediente a cada 2, 3 ou 4 fascículos. Caso a revista não publique seus avaliadores indique a resposta “Em branco”."
    dcdescriptionreviewersperiodicityofpublication = forms.ChoiceField(choices=op_dcdescriptionreviewersperiodicityofpublication, label='Periodicidade de publicação dos avaliadores', help_text = descri_reviewersperiodicityofpublication, required=False)
    op_dcdescriptionpeerreviewexternality =[("", ""),("A avaliação por pares é realizada, exclusivamente, por pesquisadores da instituição que edita a revista","A avaliação por pares é realizada, exclusivamente, por pesquisadores da instituição que edita a revista"),\
                                            ("A avaliação por pares é realizada por pesquisadores da instituiçao que edita a revista e por pesquisadores que são externos à instituição que edita a revista","A avaliação por pares é realizada por pesquisadores da instituiçao que edita a revista e por pesquisadores que são externos à instituição que edita a revista"),\
                                            ("A avaliação por pares é realizada, exclusivamente, por pesquisadores que são externos à instituição que edita a revista","A avaliação por pares é realizada, exclusivamente, por pesquisadores que são externos à instituição que edita a revista")]
    descri_peerreviewexternality="Indique se a avaliação por pares adotada pela revista considera agentes externos, internos ou ambos. Opções de resposta: 1. A avaliação por pares é realizada, exclusivamente, por pesquisadores da instituição que edita a revista. 2. A avaliação por pares é realizada por pesquisadores da instituiçao que edita a revista e por pesquisadores que são externos à instituição que edita a revista. 3. A avaliação por pares é realizada, exclusivamente, por pesquisadores que são externos à instituição que edita a revista."
    dcdescriptionpeerreviewexternality = forms.ChoiceField(choices=op_dcdescriptionpeerreviewexternality, label='Externalidade da avaliação por pares',help_text = descri_peerreviewexternality, required=True)
    descri_peerreviewdocuments="Indique as seções ou tipos de documentos publicados pela revista que passam pela avaliação por pares. Exemplos: Artigo original, Artigo de revisão,  Dados de pesquisa, Resenha, Dossiê, Tradução, Relato de experiência. Indique a resposta de acordo com as opções descritas na aba Opções de resposta. Caso as opções listadas não se adequem à realidade da revista, indique a resposta manualmente na caixa de texto."
    dcdescriptionpeerreviewdocuments = forms.CharField(widget=forms.Textarea, label='Documentos avaliados',help_text= descri_peerreviewdocuments,required=True)
    descri_publishingresponsable="Indique a instância responsável pela decisão final de publicar ou não o (s) documento (s) depois que passam pelo processo de avaliação por pares. Exemplos: Avaliador (es), Editor responsável, Editor de seção, Editor executivo. Indique a resposta de acordo com as opções descritas na aba Opções de resposta. Caso as opções listadas não se adequem à realidade da revista, indique a resposta manualmente na caixa de texto."
    dccontributorpublishingresponsable = forms.CharField(max_length=100, label='Responsável pela decisão de publicação',help_text= descri_publishingresponsable, required=True)
    op_dcrightspreprintsubmission = [("", ""),("A revista aceita a submissão de preprints que já se encontra armazenado em outras plataformas","A revista aceita a submissão de preprints que já se encontra armazenado em outras plataformas"),\
                                     ("A revista não aceita a submissão de preprints que já se encontra armazenado em outras plataformas.","A revista não aceita a submissão de preprints que já se encontra armazenado em outras plataformas")]
    descri_preprintsubmission="Informe se a revista aceita ou não a submissão de preprints que já se encontrem armazenados em plataformas de preprint. Preprint é a versão do documento (artigo original,artigo de revisão, tradução etc) que não passou por avaliação por pares e que, neste caso, foi previamente depositada em outras plataformas, antes mesmo de ser submetida à revista."
    dcrightspreprintsubmission = forms.ChoiceField(choices=op_dcrightspreprintsubmission, label='Permissão de submissão de preprint',help_text=descri_preprintsubmission ,required=True)
    op_dcrightspreprint = [("", ""),("A revista permite o armazenamento e acesso, em repositórios institucionais/digitais, da versão preprint do documento submetido para avaliação.","A revista permite o armazenamento e acesso, em repositórios institucionais/digitais, da versão preprint do documento submetido para avaliação."),\
                           ("A revista não permite o armazenamento e acesso, em repositórios institucionais/digitais, da versão preprint do documento submetido para avaliação.","A revista não permite o armazenamento e acesso, em repositórios institucionais/digitais, da versão preprint do documento submetido para avaliação.")]
    descri_rightspreprint="Informe se a revista permite ou não o armazenamento e acesso a versão preprint do documento submetido a revista em repositórios institucionais/digitais. Diferentemente da questão anterior nesta questão deve-se indicar se a revista permite ou não que a versão preprint de um documento aceito pela revista possa ser armazenado e acessado em repositórios institucionais/digitais."
    dcrightspreprint = forms.ChoiceField(choices=op_dcrightspreprint, label='Permissão de armazenamento e acesso à versão preprint',help_text =descri_rightspreprint ,required=True)
    op_dcrightsauthorpostprint = [("A revista permite o armazenamento e acesso, em repositórios institucionais/digitais, da versão pós-print do autor","A revista permite o armazenamento e acesso, em repositórios institucionais/digitais, da versão pós-print do autor"),\
                           ("A revista não permite o armazenamento e acesso, em repositórios institucionais/digitais, da versão pós-print do autor.","A revista não permite o armazenamento e acesso, em repositórios institucionais/digitais, da versão pós-print do autor.")]
    descri_authorpostprint="Informe se a revista permite ou não o armazenamento e acesso à versão pós-print do autor em repositórios institucionais/digitais. Entende-se por pós-print do autor a versão do documento (artigo original, Artigo de revisão, dados de pesquisa, tradução etc) que já foi avaliada e aceita pela revista e corrigida pelo autor, mas que ainda não foi publicada."
    dcrightsauthorpostprint = forms.ChoiceField(choices=op_dcrightsauthorpostprint, label='Permissão de armazenamento e acesso à versão pós-print do autor',help_text = descri_authorpostprint, required=True)
    op_dcrightsjournalpostprint = [("A revista permite o armazenamento e acesso, em repositórios institucionais/digitais, da versão pós-print da revista","A revista permite o armazenamento e acesso, em repositórios institucionais/digitais, da versão pós-print da revista"),\
                                   ("A revista não permite o armazenamento e acesso, em repositórios institucionais/digitais, da versão pós-print da revista","A revista não permite o armazenamento e acesso, em repositórios institucionais/digitais, da versão pós-print da revista")]
    descri_journalpostprint="Informe se a revista permite ou não armazenamento e acesso à versão pós-print da revista em repositórios institucionais/digitais. Entende-se por pós-print da revista a versão do documento (artigo original, artigo de revisão, dados de pesquisa, tradução etc) que já foi avaliada, aceita e publicada pela revista. Diz respeito, portanto, à versão final do documento."
    dcrightsjournalpostprint = forms.ChoiceField(choices=op_dcrightsjournalpostprint, label='Permissão de armazenamento e acesso à versão pós-prints da revista',help_text= descri_journalpostprint, required=True)
    
    #Pagina quatro
    
    op_dcrightssealcolor = [("Amarela: permite o armazenamento e acesso das versões pré-print dos documentos em repositórios institucionais/digitais","Amarela: permite o armazenamento e acesso das versões pré-print dos documentos em repositórios institucionais/digitais"),\
                            ("Azul: permite o armazenamento e acesso das versões pós-print dos documentos em repositórios institucionais/digitais","Azul: permite o armazenamento e acesso das versões pós-print dos documentos em repositórios institucionais/digitais"),\
                            ("Branca: apresenta restrições para o armazenamento e acesso das versões pré-print e pós-print dos documentos em repositórios institucionais/digitais","Branca: apresenta restrições para o armazenamento e acesso das versões pré-print e pós-print dos documentos em repositórios institucionais/digitais"),\
                            ("Verde: permite o armazenamento e acesso das versões pré-print e pós-print dos documentos em repositórios institucionais/digitais","Verde: permite o armazenamento e acesso das versões pré-print e pós-print dos documentos em repositórios institucionais/digitais")]
    descri_sealcolor="De acordo com as respostas dadas nas quatro últimas questões acerca das permissões estabelecidas para as diferentes versões dos documentos para armazenamento e acesso em repositórios institucionais/digitais, atribua um selo/cor que resuma a política da revista.Opções de resposta:1.permite o armazenamento e acesso das versões pré-print dos documentos em repositórios institucionais/digitais.2.permite o armazenamento e acesso das versões pós-print dos documentos em repositórios institucionais/digitais.3.apresenta restrições para o armazenamento e acesso das versões pré-print e pós-print dos documentos em repositórios institucionais/digitais.4.permite o armazenamento e acesso das versões pré-print e pós-print dos documentos em repositórios institucionais/digitais."
    dcrightssealcolor = forms.ChoiceField(choices=op_dcrightssealcolor, label='Selo de armazenamento e acesso',help_text = descri_sealcolor, required=True)
    op_dcrightstime = [("Imediatamente após a aceitação do documento","Imediatamente após a aceitação do documento"),\
                       ("Imediatamente após a publicação do documento","Imediatamente após a publicação do documento"),\
                       ("Após finalizado o período de embargo","Após finalizado o período de embargo"),\
                       ("Não permite o armazenamento","Não permite o armazenamento")]
    descri_rightstime="Informe quando os documentos poderão ser disponibilizados em acesso aberto em repositórios institucionais/digitais."
    dcrightstime = forms.ChoiceField(choices=op_dcrightstime, label='Prazo para disponibilização de documentos',help_text= descri_rightstime, required=True)
    op_dcrightsaccess = [("Acesso aberto imediato","Acesso aberto imediato"),\
                         ("Acesso aberto após período de embargo","Acesso aberto após período de embargo"),\
                         ("Acesso restrito","Acesso restrito"),\
                         ("Acesso híbrido","Acesso híbrido")]
    descri_access="Selecione o tipo de acesso permitido por sua instituição editora aos documentos da revista. A opção Acesso híbrido se refere a permissão de armazenamento e acesso somente a parte dos documentos da revista."
    dcrightsaccess = forms.ChoiceField(choices=op_dcrightsaccess, label='Tipo de acesso',help_text = descri_access ,required=True)
    descri_rightsembargedtime="Caso tenha marcado a opção “Acesso aberto após período de embargo”, informe, em meses, o tempo que os documentos não estarão disponíveis para acesso. Exemplo: 12 meses."
    dcrightsembargedtime = forms.CharField(max_length=100, label='Período de embargo',help_text = descri_rightsembargedtime, required=False)
    op_dcrightscreativecommons = [("Permite distribuição, remixagem, adaptação e criação a partir da obra, mesmo para fins comerciais, desde que seja atribuído o crédito ao autor da obra original (CC BY)","Permite distribuição, remixagem, adaptação e criação a partir da obra, mesmo para fins comerciais,\n desde que seja atribuído o crédito ao autor da obra original (CC BY)"),\
                                  ("Permite distribuição, remixagem, adaptação e criação a partir da obra, mesmo para fins comerciais, desde que seja atribuído o crédito ao autor da obra original e que as novas criações utilizem a mesma licença da obra original (CC BY-SA)","Permite distribuição, remixagem, adaptação e criação a partir da obra, mesmo para fins comerciais,\n desde que seja atribuído o crédito ao autor da obra original e que as novas criações utilizem a mesma licença da obra original (CC BY-SA)"),\
                                  ("Permite redistribuição, comercial ou não comercial, desde que a obra não seja modificada e que seja atribuído o crédito ao autor (CC BY-ND)","Permite redistribuição, comercial ou não comercial, desde que a obra não seja modificada e que seja atribuído o crédito ao autor (CC BY-ND)"),\
                                  ("Permite remixagem, adaptação e criação a partir da obra, desde que seja atribuído o crédito ao autor e que a nova criação não seja usada para fins comerciais (CC BY-NC)","Permite remixagem, adaptação e criação a partir da obra, desde que seja atribuído\n o crédito ao autor e que a nova criação não seja usada para fins comerciais (CC BY-NC)"),\
                                  ("Permite remixagem, adaptação e criação a partir da obra, para fins não comerciais, desde que seja atribuído o crédito ao autor da obra original e que as novas criações utilizem a mesma licença da obra original (CC BY-NC-SA)","Permite remixagem, adaptação e criação a partir da obra\n, para fins não comerciais, desde que seja atribuído o crédito ao autor da obra original e que as novas criações utilizem a mesma licença da obra original (CC BY-NC-SA)"),\
                                  ("Permite redistribuição não comercial, desde que seja atribuído o crédito ao autor e que a obra não seja alterada de nenhuma forma (CC BY-NC-ND)","Permite redistribuição não comercial, desde que seja atribuído o crédito ao autor\n e que a obra não seja alterada de nenhuma forma (CC BY-NC-ND)")]
    #descri_rightscreativecommons="Selecione, entre as licenças Licenças Creative Commons, aquela que define as condições estabelecidas pela revista para uso, adaptação e redistribuição dos conteúdos publicados. O conteúdo completo das Licenças Creative Commons pode ser acessado pelo link https://br.creativecommons.org/licencas/ , https://br.creativecommons.org/licencas/ , Opções de resposta:1.Permite distribuição, remixagem, adaptação e criação a partir da obra, mesmo para fins comerciais, desde que seja atribuído o crédito ao autor da obra original (CC BY).2.Permite distribuição, remixagem, adaptação e criação a partir da obra, mesmo para fins comerciais, desde que seja atribuído o crédito ao autor da obra original e que as novas criações utilizem a mesma licença da obra original (CC BY-SA)3.Permite redistribuição, comercial ou não comercial, desde que a obra não seja modificada e que seja atribuído o crédito ao autor (CC BY-ND)4.Permite remixagem, adaptação e criação a partir da obra, desde que seja atribuído o crédito ao autor e que a nova criação não seja usada para fins comerciais (CC BY-NC)5.Permite remixagem, adaptação e criação a partir da obra, para fins não comerciais, desde que seja atribuído o crédito ao autor da obra original e que as novas criações utilizem a mesma licença da obra original (CC BY-NC-SA)6.Permite redistribuição não comercial, desde que seja atribuído o crédito ao autor e que a obra não seja alterada de nenhuma forma (CC BY-NC-ND)."
    descri_rightscreativecommons="Selecione, entre as licenças Licenças Creative Commons, aquela que define as condições estabelecidas pela revista para uso, adaptação e redistribuição dos conteúdos publicados. O conteúdo completo das Licenças Creative Commons pode ser acessado pelo link https://br.creativecommons.org/licencas/ , https://br.creativecommons.org/licencas/."
    dcrightscreativecommons = forms.ChoiceField(choices=op_dcrightscreativecommons, label='Licença Creative Commons',help_text = descri_rightscreativecommons, required=True, widget=forms.RadioSelect)
    #dcrightscreativecommons.widget.attrs.update(size='2')
    op_dcdescriptionpublicationfees = [("", ""),("A revista cobra taxa de submissão de artigos","A revista cobra taxa de submissão de artigos"),\
                                       ("A revista cobra taxa de processamento de artigos (APC)","A revista cobra taxa de processamento de artigos (APC)"),\
                                       ("A revista cobra taxa de submissão e de processamento de artigos","A revista cobra taxa de submissão e de processamento de artigos"),\
                                       ("A revista não cobra nenhuma taxa de publicação","A revista não cobra nenhuma taxa de publicação")]
    descri_publicationfees ="Informe se a revista cobra algum tipo de taxa para publicação de artigos. Por taxas de publicação entende-se tanto taxa de submissão quanto taxa de processamento (APC)."
    dcdescriptionpublicationfees = forms.ChoiceField(choices=op_dcdescriptionpublicationfees, label='Taxas de publicação',help_text = descri_publicationfees, required=True)
    descri_submissionfees="Informe, em reais, o valor da Taxa de submissão de artigos. Entende-se por Taxa de submissão de artigos o valor cobrado dos autores para que os trabalhos submetidos à revista possam ser avaliados. O pagamento da taxa não é e nem deve ser um condicionante para a aprovação do artigo. Caso a revista cobre a taxa em outra moeda que não o real, solicita-se que o valor seja convertido para o real. Caso a revista não cobre a taxa, indique o valor 0 BRL. Exemplo depreenchimento: 20 BRL."
    dcdescriptionsubmissionfees = forms.CharField(max_length=100, label='Taxa de submissão de artigos',help_text = descri_submissionfees, required=True)
    descri_apc ="Informe, em reais, o valor da Taxa de Processamento de Artigo (APC), do inglês Article Processing Charges (APC). Entende-se por Taxa de Processamento de Artigo (APC) o valor cobrado dos autores para a publicação de um artigo que já foi aprovado no processo de avaliação por pares. Caso a revista cobre a taxa em outra moeda que não o real, solicita-se que o valor seja convertido para o real para preenchimento do campo. Caso a revista não cobre a taxa indique o valor 0 BRL. Exemplo de preenchimento: 50 BRL."
    dcdescriptionapc = forms.CharField(max_length=100, label='Taxa de processamento de artigos (APC)',help_text = descri_apc , required=True)
    descri_codeofethics="Informe a qual (is) Código (s) de ética ou recomendações internacionais a revista faz adesão. Indique a resposta de acordo com as opções descritas na aba Opções de resposta. Caso as opções listadas não se adequem à realidade da revista, indique a resposta manualmente na caixa de texto. Exemplos: COPE, ICJME, BOAI etc."
    dcdescriptioncodeofethics = forms.CharField(max_length=100, label='Código de ética', help_text = descri_codeofethics, required=False)
    descri_referenceguidelines="Indique o padrão de normalização bibliográfica adotado pela revista. Indique a resposta de acordo com as opções descritas na aba Opções de resposta. Caso as opções listadas não se adequem à realidade da revista, indique a resposta manualmente na caixa de texto. Caso a revista adote um Padrão de normalização bibliográfica próprio deixe a questão em branco."
    dcdescriptionreferenceguidelines = forms.CharField(max_length=100, label='Padrão de normalização bibliográfica',help_text = descri_referenceguidelines, required=False)
    descri_descriptionplagiarismdetection ="Indique a resposta de acordo com as opções descritas na aba Opções de resposta. Caso as opções listadas não se adequem à realidade da revista, indique a resposta manualmente na caixa de texto. Exemplos de softwares : Copia e Cola, Ephorus, Farejador de Plágio, Glatt, iThenticate, Plagiarism.org, Plagius, Turnitin, WriteCheck, Similarity check."
    dcdescriptionplagiarismdetection = forms.CharField(max_length=100, label='Plataforma de detecção de plágio', help_text= descri_descriptionplagiarismdetection, required=False)
    descri_descriptiondigitalpreservation="Indique a estratégia de preservação digital adotada pela revista. Indique a resposta de acordo com as opções descritas na aba Opções de resposta. Caso as opções listadas não se adequem à realidade da revista, indique a resposta manualmente na caixa de texto. Exemplos: Lockss, CLockss, Pórtico, Archivematica."
    dcdescriptiondigitalpreservation = forms.CharField(max_length=100, label='Estratégia de preservação digital', help_text = descri_descriptiondigitalpreservation , required=True)
    op_dcrightsresearchdata = [("", ""),("A revista exige que os autores publiquem os dados que deram origem à pesquisa em repositórios e/ou revistas de dados","A revista exige que os autores publiquem os dados que deram origem à pesquisa em repositórios e/ou revistas de dados"),\
                               ("A revista publica os dados que deram origem à pesquisa na própriarevista","A revista publica os dados que deram origem à pesquisa na própria revista"),\
                               ("A revista não exige que os autores publiquem os dados que deram origem à pesquisa","A revista não exige que os autores publiquem os dados que deram origem à pesquisa")]
    descri_rightsresearchdata="Informe se a revista exige que os autores disponibilizem os dados que deram origem à pesquisa publicada."
    dcrightsresearchdata = forms.ChoiceField(choices=op_dcrightsresearchdata, label='Exigência de disponibilização de dados de pesquisa',help_text = descri_rightsresearchdata, required=True)
    op_dcdescriptionqualisarea = [("", ""),("Revista não avaliada","Revista não avaliada"),\
                                  ("Administração pública e de empresas, Ciências contábeis e Turismo","Administração pública e de empresas, Ciências contábeis e Turismo"),\
                                  ("Antropologia / Arqueologia","Antropologia / Arqueologia"),\
                                  ("Arquitetura, urbanismo e design","Arquitetura, urbanismo e design"),\
                                  ("Artes","Artes"),\
                                  ("Astronomia / Física","Astronomia / Física"),\
                                  ("Biodiversidade","Biodiversidade"),\
                                  ("Biotecnologia","Biotecnologia"),\
                                  ("Ciência da computação","Ciência da computação"),\
                                  ("Ciência de alimentos","Ciência de alimentos"),\
                                  ("Ciência política e Relações internacionais","Ciência política e Relações internacionais"),\
                                  ("Ciências agrárias I","Ciências agrárias I"),\
                                  ("Ciências ambientais","Ciências ambientais"),\
                                  ("Ciências biológicas I","Ciências biológicas I"),\
                                  ("Ciências biológicas II","Ciências biológicas II"),\
                                  ("Ciências biológicas III","Ciências biológicas III"),\
                                  ("Ciências da religião e Teologia","Ciências da religião e Teologia"),\
                                  ("Comunicação e informação","Comunicação e informação"),\
                                  ("Direito","Direito"),\
                                  ("Economia","Economia"),\
                                  ("Educação","Educação"),\
                                  ("Educação física","Educação física"),\
                                  ("Enfermagem","Enfermagem"),\
                                  ("Engenharias I","Engenharias I"),\
                                  ("Engenharias II","Engenharias II"),\
                                  ("Engenharias III","Engenharias III"),\
                                  ("Engenharias IV","Engenharias IV"),\
                                  ("Ensino","Ensino"),\
                                  ("Farmácia","Farmácia"),\
                                  ("Filosofia","Filosofia"),\
                                  ("Geociências","Geociências"),\
                                  ("Geografia","Geografia"),\
                                  ("História","História"),\
                                  ("Interdisciplinar","Interdisciplinar"),\
                                  ("Linguística e literatura","Linguística e literatura"),\
                                  ("Matemática / Probabilidade e estatística","Matemática / Probabilidade e estatística"),\
                                  ("Materiais","Materiais"),\
                                  ("Medicina I","Medicina I"),\
                                  ("Medicina II","Medicina II"),\
                                  ("Medicina III","Medicina III"),\
                                  ("Medicina veterinária","Medicina veterinária"),\
                                  ("Nutrição","Nutrição"),\
                                  ("Odontologia","Odontologia"),\
                                  ("Planejamento urbano e regional / Demografia","Planejamento urbano e regional / Demografia"),\
                                  ("Psicologia","Psicologia"),\
                                  ("Química","Química"),\
                                  ("Saúde coletiva","Saúde coletiva"),\
                                  ("Serviço social","Serviço social"),\
                                  ("Sociologia","Sociologia"),\
                                  ("Zootecnia / Recursos pesqueiros","Zootecnia / Recursos pesqueiros")]
    descri_descriptionqualisarea="Indique a área-mãe de avaliação da revista no estrato Qualis-Periódicos, de acordo com a classificação mais recente da revista. Caso a revista ainda não tenha sido avaliada, indique Revista não avaliada. Essa informação pode ser verificada pela busca por número de ISSN da revista no link: https://sucupira.capes.gov.br/sucupira/public/consultas/coleta/veiculoPublicacaoQualis/listaConsultaGeralPeriodicos.jsf "
    dcdescriptionqualisarea = forms.ChoiceField(choices=op_dcdescriptionqualisarea, label='Área de avaliação Qualis-Periódicos',help_text = descri_descriptionqualisarea, required=True)
    op_dcdescriptionqualisclassification = [("", ""),("Revista não avaliada","Revista não avaliada"),\
                                            ("A1","A1"),\
                                            ("A2","A2"),\
                                            ("A3","A3"),\
                                            ("A4","A4"),\
                                            ("B1","B1"),\
                                            ("B2","B2"),\
                                            ("B3","B3"),\
                                            ("B4","B4"),\
                                            ("C","C")]
    descri_descripstionqualisclassification = "Indique a classificação mais recente da revista no estrato Qualis-Periódicos para a área-mãe indicada no campo acima. Caso a revista ainda não tenha sido avaliada, indique Revista não avaliada. Essa informação pode ser verificada pela busca do ISSN da revista no link:https://sucupira.capes.gov.br/sucupira/public/consultas/coleta/veiculoPublicacaoQualis/listaConsultaGeralPeriodicos.jsf"
    dcdescriptionqualisclassification = forms.ChoiceField(choices=op_dcdescriptionqualisclassification, label='Classificação Qualis-Periódicos', help_text = descri_descripstionqualisclassification, required=True)
    descri_descriptionsocialnetwork ="A revista deve indicar o nome da(s) rede(s) social(is) em que está presente. Indique a resposta de acordo com as opções descritas na aba Opções de resposta. Caso as opções listadas não se adequem à realidade da revista, indique a resposta manualmente na caixa de texto."
    dcdescriptionsocialnetworks = forms.CharField(max_length=100, label='Redes Sociais',help_text = descri_descriptionsocialnetwork, required=False)
    descri_relationinformationservices="A revista deve indicar os serviços de informação em que está presente. Como serviços de informação consideram-se bases de dados, índices, indexadores, diretórios e etc. Indique a resposta de acordo com as opções descritas na aba Opções de resposta. Caso as opções listadas não se adequem à realidade da revista, indique a resposta manualmente na caixa de texto. Caso a revista não faça parte de nenhum serviço de informação indique apenas o Miguilim (Diretório de Revistas Científicas Eletrônicas Brasileiras). Exemplos: Oasisbr, SciELO, Redalyc, Latindex, Diadorim, Web of Science, Scopus, Sumários.org etc."
    dcrelationinformationservices = forms.CharField(max_length=100, label='Serviços de informação', help_text = descri_relationinformationservices, required=True)
    descri_identifierjournalsportaluri ="Indique o título do portal de periódicos que hospeda a revista. Portal de periódicos é o portal institucional em que o site oficial da revista se encontra hospedado. Exemplos: Portal de Periódicos UFSC, Portal de Periódicos Eletrônicos Científicos da UNICAMP."
    dcidentifierjournalsportaluri = forms.CharField(max_length=100, label='Portal de periódicos',help_text = descri_identifierjournalsportaluri, required=False)
    #descri_relationoasisbr ="Indique a URL da busca do ISSN da revista no Portal oasisbr."
    #dcrelationoasisbr = forms.CharField(max_length=100, label='Artigos da revista no Portal oasisbr',help_text= descri_relationoasisbr, required=False)
    
    



        
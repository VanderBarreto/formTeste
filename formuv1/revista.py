"""
@author: Vanderlino Coelho Barreto Neto
"""
from django.forms.models import inlineformset_factory
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .autenticacao import Logar
from .dados import Dados
from .forms import ContactForm
from .enviodeemail import EnviodoEmail

g_link=""
g_token=""
end_dspace = "http:/192.168.10.17:8080"
#end_dspace = "http://172.25.0.73:8080"

class Revistas:
            
    
    def revista(self, request):
        
        global g_link
        global g_token
        global end_dspace
        nomerevista = ""
        submitted = False
        
            
        if request.method == 'POST':
            
            form = ContactForm(request.POST)
            
            if form.is_valid():
                
                token = g_token
                end_dspace_metadata = end_dspace+g_link+"/metadata"
                
                nome_revista=str(request.POST.get('dctitle'))
                print(nome_revista)
                metadata ='[{"key":"dc.description.abstract","value":"'+str(request.POST.get('dcdescriptionabstract'))+'","language":"pt_BR"},\
                {"key":"dc.title","value":"'+str(request.POST.get('dctitle'))+'","language":"pt_BR"},\
                {"key":"dc.title.abbreviated","value":"'+str(request.POST.get('dctitleabbreviated'))+'","language":"pt_BR"},\
                {"key":"dc.title.proper","value":"'+str(request.POST.get('dctitleproper'))+'","language":"pt_BR"},\
                {"key":"dc.title.other","value":"'+str(request.POST.get('dctitleother'))+'","language":"pt_BR"},\
                {"key":"dc.title.previous","value":"'+str(request.POST.get('dctitleprevious'))+'","language":"pt_BR"},\
                {"key":"dc.title.later","value":"'+str(request.POST.get('dctitlelater'))+'","language":"pt_BR"},\
                {"key":"dc.identifier.issn","value":"'+str(request.POST.get('dcidentifierissn'))+'","language":"pt_BR"},\
                {"key":"dc.identifier.issnl","value":"'+str(request.POST.get('dcidentifierissnl'))+'","language":"pt_BR"},\
                {"key":"dc.description.situation","value":"'+str(request.POST.get('dcdescriptionsituation'))+'","language":"pt_BR"},\
                {"key":"dc.date.startyear","value":"'+str(request.POST.get('dcdatestartyear'))+'","language":"pt_BR"},\
                {"key":"dc.date.endyear","value":"'+str(request.POST.get('dcdateendyear'))+'","language":"pt_BR"},\
                {"key":"dc.identifier.url","value":"'+str(request.POST.get('dcidentifierurl'))+'","language":"pt_BR"},\
                {"key":"dc.identifier.interoperabilityprotocol","value":"'+str(request.POST.get('dcidentifierinteroperabilityprotocol'))+'","language":"pt_BR"},\
                {"key":"dc.identifier.persistentidentifier","value":"'+str(request.POST.get('dcidentifierpersistentidentifier'))+'","language":"pt_BR"},\
                {"key":"dc.language","value":"'+str(request.POST.get('dclanguage'))+'","language":"pt_BR"},\
                {"key":"dc.subject.cnpq","value":"'+str(request.POST.get('dcsubjectcnpq'))+'","language":"pt_BR"},\
                {"key":"dc.publisher.name","value":"'+str(request.POST.get('dcpublishername'))+'","language":"pt_BR"},\
                {"key":"dc.publisher.subordinate","value":"'+str(request.POST.get('dc.publisher.subordinate'))+'","language":"pt_BR"},\
                {"key":"dc.identifier.publisher","value":"'+str(request.POST.get('dcidentifierpublisher'))+'","language":"pt_BR"},\
                {"key":"dc.publisher.legalnature","value":"'+str(request.POST.get('dcpublisherlegalnature'))+'","language":"pt_BR"},\
                {"key":"dc.contributor.editor","value":"'+str(request.POST.get('dccontributoreditor'))+'","language":"pt_BR"},\
                {"key":"dc.identifier.editor","value":"'+str(request.POST.get('dcidentifiereditor'))+'","language":"pt_BR"},\
                {"key":"dc.identifier.email","value":"'+str(request.POST.get('dcidentifieremail'))+'","language":"pt_BR"},\
                {"key":"dc.description.cep","value":"'+str(request.POST.get('dcdescriptioncep'))+'"},\
                {"key":"dc.description.state","value":"'+str(request.POST.get('dcdescriptionstate'))+'","language":"pt_BR"},\
                {"key":"dc.description.city","value":"'+str(request.POST.get('dcdescriptioncity'))+'","language":"pt_BR"},\
                {"key":"dc.description.neighborhood","value":"'+str(request.POST.get('dcdescriptionneighborhood'))+'"},\
                {"key":"dc.description.street","value":"'+str(request.POST.get('dcdescriptionstreet'))+'","language":"pt_BR"},\
                {"key":"dc.description.building","value":"'+str(request.POST.get('dcdescriptionbuilding'))+'","language":"pt_BR"},\
                {"key":"dc.description.phone","value":"'+str(request.POST.get('dcdescriptionphone'))+'"},\
                {"key":"dc.description.modalityofpublication","value":"'+str(request.POST.get('dcdescriptionmodalityofpublication'))+'","language":"pt_BR"},\
                {"key":"dc.description.periodicity","value":"'+str(request.POST.get('dcdescriptionperiodicity'))+'","language":"pt_BR"},\
                {"key":"dc.date.monthofpublication","value":"'+str(request.POST.get('dcdatemonthofpublication'))+'"},\
                {"key":"dc.description.editorialboardperiodicity","value":"'+str(request.POST.get('dcdescriptioneditorialboardperiodicity'))+'"},\
                {"key":"dc.date.editorialboardmonthofpublication","value":"'+str(request.POST.get('dcdateeditorialboardmonthofpublication'))+'","language":"pt_BR"},\
                {"key":"dc.description.peerreview","value":"'+str(request.POST.get('dcdescriptionpeerreview'))+'","language":"pt_BR"},\
                {"key":"dc.description.reviewerspublication","value":"'+str(request.POST.get('dcdescriptionreviewerspublication'))+'","language":"pt_BR"},\
                {"key":"dc.description.reviewerstypeofpublication","value":"'+str(request.POST.get('dcdescriptionreviewerstypeofpublication'))+'","language":"pt_BR"},\
                {"key":"dc.description.reviewersperiodicityofpublication","value":"'+str(request.POST.get('dcdescriptionreviewersperiodicityofpublication'))+'","language":"pt_BR"},\
                {"key":"dc.description.peerreviewexternality","value":"'+str(request.POST.get('dcdescriptionpeerreviewexternality'))+'","language":"pt_BR"},\
                {"key":"dc.description.peerreviewdocuments","value":"'+str(request.POST.get('dcdescriptionpeerreviewdocuments'))+'","language":"pt_BR"},\
                {"key":"dc.contributor.publishingresponsable","value":"'+str(request.POST.get('dccontributorpublishingresponsable'))+'","language":"pt_BR"},\
                {"key":"dc.rights.preprintsubmission","value":"'+str(request.POST.get('dcrightspreprintsubmission'))+'","language":"pt_BR"},\
                {"key":"dc.rights.preprint","value":"'+str(request.POST.get('dcrightspreprint'))+'","language":"pt_BR"},\
                {"key":"dc.rights.authorpostprint","value":"'+str(request.POST.get('dcrightsauthorpostprint'))+'","language":"pt_BR"},\
                {"key":"dc.rights.journalpostprint","value":"'+str(request.POST.get('dcrightsjournalpostprint'))+'","language":"pt_BR"},\
                {"key":"dc.rights.sealcolor","value":"'+str(request.POST.get('dcrightssealcolor'))+'","language":"pt_BR"},\
                {"key":"dc.rights.time","value":"'+str(request.POST.get('dcrightstime'))+'","language":"pt_BR"},\
                {"key":"dc.rights.access","value":"'+str(request.POST.get('dcrightsaccess'))+'","language":"pt_BR"},\
                {"key":"dc.rights.embargedtime","value":"'+str(request.POST.get('dcrightsembargedtime'))+'","language":"pt_BR"},\
                {"key":"dc.rights.creativecommons","value":"'+str(request.POST.get('dcrightscreativecommons'))+'"},\
                {"key":"dc.description.publicationfees","value":"'+str(request.POST.get('dcdescriptionpublicationfees'))+'","language":"pt_BR"},\
                {"key":"dc.description.submissionfees","value":"'+str(request.POST.get('dcdescriptionsubmissionfees'))+'","language":"pt_BR"},\
                {"key":"dc.description.apc","value":"'+str(request.POST.get('dcdescriptionapc'))+'","language":"pt_BR"},\
                {"key":"dc.description.codeofethics","value":"'+str(request.POST.get('dcdescriptioncodeofethics'))+'","language":"pt_BR"},\
                {"key":"dc.description.referenceguidelines","value":"'+str(request.POST.get('dcdescriptionreferenceguidelines'))+'","language":"pt_BR"},\
                {"key":"dc.description.plagiarismdetection","value":"'+str(request.POST.get('dcdescriptionplagiarismdetection'))+'","language":"pt_BR"},\
                {"key":"dc.description.digitalpreservation","value":"'+str(request.POST.get('dcdescriptiondigitalpreservation'))+'","language":"pt_BR"},\
                {"key":"dc.rights.researchdata","value":"'+str(request.POST.get('dcrightsresearchdata'))+'","language":"pt_BR"},\
                {"key":"dc.description.qualisarea","value":"'+str(request.POST.get('dcdescriptionqualisarea'))+'","language":"pt_BR"},\
                {"key":"dc.description.qualisclassification","value":"'+str(request.POST.get('dcdescriptionqualisclassification'))+'","language":"pt_BR"},\
                {"key":"dc.description.socialnetworks","value":"'+str(request.POST.get('dcdescriptionsocialnetworks'))+'","language":"pt_BR"},\
                {"key":"dc.relation.informationservices","value":"'+str(request.POST.get('dcrelationinformationservices'))+'","language":"pt_BR"},\
                {"key":"dc.identifier.journalsportaluri","value":"'+str(request.POST.get('dcidentifierjournalsportaluri'))+'","language":"pt_BR"}]'
                
                
                #print(metadata)
                ComandoURL = 'curl --cookie "JSESSIONID='+token+'" -H "accept: application/json" -H "Content-Type: application/json" -X PUT '+end_dspace_metadata+" -d '"+metadata+"'"
                
                print(ComandoURL)
                
                #os.system(ComandoURL)
                
                #enviaremail = EnviodoEmail
                #enviado = enviaremail.envio(nome_revista)
                #print(enviado)
                metadata=""
                token=""
                
                return HttpResponseRedirect('/revista?submitted=True')
                       
        else:
            
            if g_token=="":
                
                mensagem = ""

                return HttpResponseRedirect('/login')    
            
            else:
                
                dados_iniciais = Dados()
                dados_iniciais.buscar(g_link,end_dspace)
                nomerevista=dados_iniciais.retorno('dc.title')
                info_entrada = {"dcdescriptionabstract": dados_iniciais.retorno('dc.description.abstract'),\
                        "dctitle": dados_iniciais.retorno('dc.title'),\
                        "dctitleabbreviated": dados_iniciais.retorno('dc.title.abbreviated'),\
                        "dctitleproper": dados_iniciais.retorno('dc.title.proper'),\
                        "dctitleother": dados_iniciais.retorno('dc.title.other'),\
                        "dctitleprevious": dados_iniciais.retorno('dc.title.previous'),\
                        "dctitlelater": dados_iniciais.retorno('dc.title.later'),\
                        "dcidentifierissn": dados_iniciais.retorno('dc.identifier.issn'),\
                        "dcidentifierissnl": dados_iniciais.retorno('dc.identifier.issnl'),\
                        "dcdescriptionsituation": dados_iniciais.retorno('dc.description.situation'),\
                        "dcdatestartyear": dados_iniciais.retorno('dc.date.startyear'),\
                        "dcdateendyear": dados_iniciais.retorno('dc.date.endyear'),\
                        "dcidentifierurl": dados_iniciais.retorno('dc.identifier.url'),\
                        "dcidentifierinteroperabilityprotocol": dados_iniciais.retorno('dc.identifier.interoperabilityprotocol'),\
                        "dcidentifierpersistentidentifier": dados_iniciais.retorno('dc.identifier.persistentidentifier'),\
                        "dclanguage": dados_iniciais.retorno('dc.language'),\
                        "dcsubjectcnpq": dados_iniciais.retorno('dc.subject.cnpq'),\
                        "dcpublishername": dados_iniciais.retorno('dc.publisher.name'),\
                        "dcpublishersubordinate": dados_iniciais.retorno('dc.publisher.subordinate'),\
                        "dcidentifierpublisher": dados_iniciais.retorno('dc.identifier.publisher'),\
                        "dcpublisherlegalnature": dados_iniciais.retorno('dc.publisher.legalnature'),\
                        "dccontributoreditor": dados_iniciais.retorno('dc.contributor.editor'),\
                        "dcidentifiereditor": dados_iniciais.retorno('dc.identifier.editor'),\
                        "dcidentifieremail": dados_iniciais.retorno('dc.identifier.email'),\
                        "dcdescriptioncep":  dados_iniciais.retorno('dc.description.cep'),\
                        "dcdescriptionstate":  dados_iniciais.retorno('dc.description.state'),\
                        "dcdescriptioncity": dados_iniciais.retorno('dc.description.city'),\
                        "dcdescriptionneighborhood": dados_iniciais.retorno('dc.description.neighborhood'),\
                        "dcdescriptionstreet": dados_iniciais.retorno('dc.description.street'),\
                        "dcdescriptionbuilding": dados_iniciais.retorno('dc.description.building'),\
                        "dcdescriptionphone": dados_iniciais.retorno('dc.description.phone'),\
                        "dcdescriptionmodalityofpublication": dados_iniciais.retorno('dc.description.modalityofpublication'),\
                        "dcdescriptionperiodicity": dados_iniciais.retorno('dc.description.periodicity'),\
                        "dcdatemonthofpublication": dados_iniciais.retorno('dc.date.monthofpublication'),\
                        "dcdescriptioneditorialboardperiodicity": dados_iniciais.retorno('dc.description.editorialboardperiodicity'),\
                        "dcdateeditorialboardmonthofpublication": dados_iniciais.retorno('dc.date.editorialboardmonthofpublication'),\
                        "dcdescriptionpeerreview": dados_iniciais.retorno('dc.description.peerreview'),\
                        "dcdescriptionreviewerspublication": dados_iniciais.retorno('dc.description.reviewerspublication'),\
                        "dcdescriptionreviewerstypeofpublication": dados_iniciais.retorno('dc.description.reviewerstypeofpublication'),\
                        "dcdescriptionreviewersperiodicityofpublication": dados_iniciais.retorno('dc.description.reviewersperiodicityofpublication'),\
                        "dcdescriptionpeerreviewexternality": dados_iniciais.retorno('dc.description.peerreviewexternality'),\
                        "dcdescriptionpeerreviewdocuments": dados_iniciais.retorno('dc.description.peerreviewdocuments'),\
                        "dccontributorpublishingresponsable": dados_iniciais.retorno('dc.contributor.publishingresponsable'),\
                        "dcrightspreprintsubmission": dados_iniciais.retorno('dc.rights.preprintsubmission'),\
                        "dcrightspreprint": dados_iniciais.retorno('dc.rights.preprint'),\
                        "dcrightsauthorpostprint": dados_iniciais.retorno('dc.rights.authorpostprint'),\
                        "dcrightsjournalpostprint": dados_iniciais.retorno('dc.rights.journalpostprint'),\
                        "dcrightssealcolor": dados_iniciais.retorno('dc.rights.sealcolor'),\
                        "dcrightstime": dados_iniciais.retorno('dc.rights.time'),\
                        "dcrightsaccess": dados_iniciais.retorno('dc.rights.access'),\
                        "dcrightsembargedtime": dados_iniciais.retorno('dc.rights.embargedtime'),\
                        "dcrightscreativecommons": dados_iniciais.retorno('dc.rights.creativecommons'),\
                        "dcdescriptionpublicationfees": dados_iniciais.retorno('dc.description.publicationfees'),\
                        "dcdescriptionsubmissionfees": dados_iniciais.retorno('dc.description.submissionfees'),\
                        "dcdescriptionapc": dados_iniciais.retorno('dc.description.apc'),\
                        "dcdescriptioncodeofethics": dados_iniciais.retorno('dc.description.codeofethics'),\
                        "dcdescriptionreferenceguidelines": dados_iniciais.retorno('dc.description.referenceguidelines'),\
                        "dcdescriptionplagiarismdetection": dados_iniciais.retorno('dc.description.plagiarismdetection'),\
                        "dcdescriptiondigitalpreservation": dados_iniciais.retorno('dc.description.digitalpreservation'),\
                        "dcrightsresearchdata": dados_iniciais.retorno('dc.rights.researchdata'),\
                        "dcdescriptionqualisarea": dados_iniciais.retorno('dc.description.qualisarea'),\
                        "dcdescriptionqualisclassification": dados_iniciais.retorno('dc.description.qualisclassification'),\
                        "dcdescriptionsocialnetworks": dados_iniciais.retorno('dc.description.socialnetworks"'),\
                        "dcrelationinformationservices": dados_iniciais.retorno('dc.relation.informationservices'),\
                        "dcidentifierjournalsportaluri": dados_iniciais.retorno('dc.identifier.journalsportaluri')}
                #print(info_entrada)
                form = ContactForm(info_entrada) # as informações são carredas nesse momento
                info_entrada=None
                print(form)
                
                if 'submitted' in request.GET:
                    submitted = True
        
    
        return render(request, 'revista/revista.html', {'nomerevista': nomerevista, 'forms': form, 'submitted': submitted})

        
class Login:
    
    
    def user_login(self, request):
        
        global g_link
        global g_token 
        global end_dspace
        self.user_global= ""
        self.senha_global= ""
        self.revista_global= ""
        self.link_global= ""
        self.token_global=""
        g_link = ""
        g_token = ""
        Autentica=Logar()
        mensagem = "Atualize sua revista"
        
        
        
        if request.method == 'POST':
            
            self.user_global= request.POST.get('email')
            self.senha_global= request.POST.get('senha')
            self.revista_global= request.POST.get('revista')
            
            
            
            if self.user_global != "" and self.senha_global != "" and self.revista_global != "" :
                
                self.link_global = Autentica.procuraissn(self.revista_global,end_dspace)
                g_link = Autentica.procuraissn(self.revista_global,end_dspace)
                print("\nlink = "+g_link)
                (cod, token) = Autentica.autenticar(self.user_global,self.senha_global,end_dspace)
                self.token_global = token 
                g_token = token
                print(g_token)
                
                #dados_login = Autentica.inf_login()
                
                if self.link_global != "":
                
                    if cod == "0" :
                        
                        return HttpResponseRedirect('/revista')
                        
    #                    if user.is_active:
    #                        login(request,user)
    #                        return HttpResponseRedirect('/revista')
    #                    else:
    #                        return HttpResponse("Your account was inactive.")
    
                    else:
                        mensagem = "Login Inválido"
                        return render(request, 'revista/login.html', {"mensagem": mensagem})
                else:
                    mensagem = "ISSN incorreto"
                    return render(request, 'revista/login.html', {"mensagem": mensagem})
            else:
                mensagem = "Campos faltando"
                return render(request, 'revista/login.html', {"mensagem": mensagem})
                
        else:
            
            
            return render(request, 'revista/login.html', {})
        
   
    def retornoinfo(self):
        
        global g_link

        print("\n\n Revista = "+g_link)
        retorno = g_link
        
        return retorno
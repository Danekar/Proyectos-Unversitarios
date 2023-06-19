import sys
from traceback import print_tb
import requests
import Bateria
import os
import sys
import colorama
import asyncio
from colorama import Fore


urlLink = ""
inputLink=""
payloadsValidos = []
posicionRespuesta=0
respuesta=""    

def ResetRespuestaYPosicion():
    myobj = {inputLink: "payloads"}
    x = requests.get(url = urlLink, params = myobj)
    global respuesta 
    respuesta = x.text
    global posicionRespuesta 
    posicionRespuesta = respuesta.find("payloads")

def TextoOriginalComp(posicionRespuesta, payloads):
    #print(respuesta[posicionRespuesta] +"  "+ respuesta[posicionRespuesta+len(payloads)-1])
    if(posicionRespuesta!=-1):
        payloadsValidos.append(payloads)
        return True
        
#and respuesta[posicionRespuesta-1]=='<' or respuesta[posicionRespuesta+len(payloads)-1]=='>'
def EntreEtiquetasComp(respuesta, posicionRespuesta, payloads):
    if(respuesta[posicionRespuesta-1]=='>' or respuesta[posicionRespuesta+len(payloads)]=='<'):
       payloadsValidos.append(payloads)
       return True
 
def EntreComillasComp(respuesta, posicionRespuesta, payloads):
    if(respuesta[posicionRespuesta-1]=='"' and respuesta[posicionRespuesta+len(payloads)]=='"'):
        payloadsValidos.remove(payloads)
        #print(respuesta[posicionRespuesta]+"  "+ respuesta[posicionRespuesta+len(payloads)])
        if(respuesta[posicionRespuesta]=='"' and respuesta[posicionRespuesta+1]=='>'):
            payloadsValidos.append(payloads)

def EmpiezaComillasComp(respuesta, posicionRespuesta, payloads):
    #print(respuesta[posicionRespuesta] +"  "+ respuesta[posicionRespuesta+len(payloads)-1:posicionRespuesta+len(payloads)+10])
    if(respuesta[posicionRespuesta]=='"' and respuesta[posicionRespuesta+len(payloads)]=='"'):
        payloadsValidos.append(payloads) 

def DentroDeScript(respuesta, posicionRespuesta):
    abiertoScript = respuesta.find("<script>")
    cerradoScript = respuesta.find("</script>",abiertoScript)
    #print (str(abiertoScript)+" : "+str(posicionRespuesta)+ " : "+str(cerradoScript))
    if(posicionRespuesta > abiertoScript and posicionRespuesta < cerradoScript):
        return True

def DobleBarra(respuesta, posicionRespuesta, payloads):
    if(respuesta[posicionRespuesta-1]=='\\' and respuesta[posicionRespuesta]=='\\'):
        payloadsValidos.append(payloads)
        return True
    if(respuesta[posicionRespuesta-1]=='\\' and not respuesta[posicionRespuesta]=='\\' ):
        payloadsValidos.remove(payloads)
        return False 

def HayBarra(respuesta, posicionRespuesta, payloads):
    if(respuesta[posicionRespuesta-1]=='\\'):
        return True
    else:
        if(respuesta[posicionRespuesta]=='\\'):
            payloadsValidos.remove(payloads)
            
def EsHref(respuesta, posicionRespuesta):
    hrefAbierta = respuesta.find("href")
    hrefCerrada = respuesta.find('">',hrefAbierta)
    #print (str(hrefAbierta)+" : "+str(posicionRespuesta)+ " : "+str(hrefCerrada))
    if(hrefAbierta < posicionRespuesta and hrefCerrada > posicionRespuesta):
        return True

def EntreCorchetesStringEncodeIf(respuesta, posicionRespuesta):
    #si esta entre corchetes
    corcheteAbierto = respuesta.find("{")
    corcheteCerrado = respuesta.find('}',corcheteAbierto)
    if(corcheteAbierto < posicionRespuesta and corcheteCerrado > posicionRespuesta):
        return True
        #meter el string encode
    
def CorchetePuntoYComa(respuesta,posicionRespuesta,payloads):
    corcheteAbierto = respuesta.find("{")
    corcheteCerrado = respuesta.find('}',corcheteAbierto)
    puntoYcoma = respuesta.find(';')
    if(puntoYcoma > corcheteCerrado and payloads.find('{')!= -1):
        if(respuesta[posicionRespuesta+len(payloads)-3] == "}"):
            payloadsValidos.append(payloads)
            return True
        else:
            payloadsValidos.remove(payloads)
        
    if(respuesta[posicionRespuesta+len(payloads)-3] == "}" and puntoYcoma ==-1):
        payloadsValidos.remove(payloads)
        return False

def AbreCorchete(payloads):
    if(payloads.find('{')!= -1): 
        payloadsValidos.remove(payloads)
        return True
    
def BuscaComillas(respuesta,posicionRespuesta,payloads):
    if(respuesta[posicionRespuesta-1]=='"' and respuesta[posicionRespuesta]=='"'):
        payloadsValidos.append(payloads)
        return True
    else:
        payloadsValidos.remove(payloads)
    
    if(respuesta[posicionRespuesta-1]=="'" and  respuesta[posicionRespuesta]=="'"):
        payloadsValidos.append(payloads)
        return True
    else:
        payloadsValidos.remove(payloads)
            
async def main(): 
    global respuesta
    global posicionRespuesta
    global urlLink
    global inputLink
    global payloadsValidos

    ResetRespuestaYPosicion()

    if not (EsHref(respuesta, posicionRespuesta)):
        if not(DentroDeScript(respuesta, posicionRespuesta)):
            #Comprobando si se escribe en texto claro el xss
            bateria = Bateria.payloadsEtiquetas
            for payloads in bateria:
                myobj = {inputLink: payloads}
                x = requests.get(url = urlLink, params = myobj)
                respuesta = x.text
                posicionRespuesta = respuesta.find(payloads)
                if(TextoOriginalComp(posicionRespuesta, payloads)):
                    EntreComillasComp(respuesta, posicionRespuesta, payloads)
                    #EmpiezaComillasComp(respuesta, posicionRespuesta, payloads) 

                bateria = Bateria.payloadsSinEtiquetas

                for payloads in bateria:
                    myobj = {inputLink: payloads}
                    x = requests.get(url = urlLink, params = myobj)
                    respuesta = x.text
                    #print (respuesta)
                    posicionRespuesta = respuesta.find(payloads)
                    if(TextoOriginalComp(posicionRespuesta, payloads)):
                        if(EntreEtiquetasComp(respuesta, posicionRespuesta, payloads)):
                            payloadsValidos = list(dict.fromkeys(payloadsValidos))
                            print(payloads)
                            payloadsValidos.remove(payloads)
                        else:
                            EmpiezaComillasComp(respuesta, posicionRespuesta, payloads)
        else:   
            bateria = Bateria.payloadsVariables
            for payloads in bateria:
                myobj = {inputLink: payloads}
                x = requests.get(url = urlLink, params = myobj)
                respuesta = x.text
                posicionRespuesta = respuesta.find(payloads)
                if(TextoOriginalComp(posicionRespuesta, payloads)):
                    if(HayBarra(respuesta, posicionRespuesta, payloads)):
                        DobleBarra(respuesta, posicionRespuesta, payloads)
                        #AnadeBarra(respuesta, posicionRespuesta, payloads)

        ResetRespuestaYPosicion()
    else:
        bateria = Bateria.payloadHref
        print("Para este tipo de payload necesitarás que darle al \nlink que genera la pagina para que salte el XSS")
        for payloads in bateria:
            myobj = {inputLink: payloads}
            x = requests.get(url = urlLink, params = myobj)
            respuesta = x.text
            posicionRespuesta = respuesta.find(payloads)
            if(TextoOriginalComp(posicionRespuesta, payloads)):
                print
                        
    ResetRespuestaYPosicion()

    if (EntreCorchetesStringEncodeIf(respuesta, posicionRespuesta)):
        bateria = Bateria.payloadStringEncode
        for payloads in bateria:
            myobj = {inputLink: payloads}
            x = requests.get(url = urlLink, params = myobj)
            respuesta = x.text
            posicionRespuesta = respuesta.find(payloads)
            if(TextoOriginalComp(posicionRespuesta, payloads)):
                try:
                    BuscaComillas(respuesta,posicionRespuesta,payloads)
                    if(CorchetePuntoYComa(respuesta,posicionRespuesta,payloads)):
                        print
                    else:
                        try:
                            payloadsValidos = list(dict.fromkeys(payloadsValidos))
                            AbreCorchete(payloads)
                        except:
                            print
                except:
                    print      

    payloadsValidos = list(dict.fromkeys(payloadsValidos))

    if(payloadsValidos):
        print("\n -------------------------------------------Estos payloads servirían---------------------------------- \n")
        for payloads in payloadsValidos:
            print(payloads)
            print("\n")
        print("\n")
    else:
        numDeChars=0
        normalResult=""
        if (os.popen("wafw00f "+ urlLink).read()):
            directories = os.popen("wafw00f "+ urlLink).read()
            if(directories.find("No WAF detected by the generic detection") != -1):
                print("No hay WAF en esta pagina pero por desgracia,\nel programa aun no tiene suficientes payloads para\n la pagina proporcionada")
            else:
                isBehind = directories.find("is behind")
                waf = directories.find("WAF.",isBehind)
                blueResult = directories[isBehind+len("is behind")+8:waf-4]
                for i in range(len(blueResult)):
                    numDeChars = ord(blueResult[i])
                    normalResult += Fore.WHITE + chr(numDeChars) 
                print("Existe un WAF en esta pagina y es: "+normalResult)
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Para encontrar el WAF, se necesita instalar wafw00f en el sistema operativo\nsino el programa no funcionrá")









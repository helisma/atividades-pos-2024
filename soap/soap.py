import requests
from xml.dom.minidom import parseString
# URL do serviço SOAP
url = "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso"

print("Escolha as opções a seguir:\n1 - Para saber a capital do país\n2 - Para saber que moeda o país utiliza\n3 - Para retornar o idioma apartir do CÓDIGO")
print("-"*30)
campo = int(input("Qual opção?"))

if campo ==1:
  country= str(input("Digite a SIGLA do país (em maiúsculo): "))
  # XML estruturado
  payload = f"""<?xml version="1.0" encoding="utf-8"?>
  <soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
    <soap:Body>
      <CapitalCity xmlns="http://www.oorsprong.org/websamples.countryinfo">
        <sCountryISOCode>{country}</sCountryISOCode>
      </CapitalCity>
    </soap:Body>
  </soap:Envelope>"""
  # headers
  headers = {
    'Content-Type': 'text/xml; charset=utf-8'
  }
  # request POST
  response = requests.request("POST", url, headers=headers, data=payload)

  # imprime a resposta
  content = parseString(response.text)
  print(content.documentElement.getElementsByTagName("m:CapitalCityResult")[0].firstChild.nodeValue)

elif campo ==2:
  country= str(input("Digite a SIGLA do país (em maiúsculo): "))
  # XML estruturado
  payload = f"""<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <CountryCurrency xmlns="http://www.oorsprong.org/websamples.countryinfo">
      <sCountryISOCode>{country}</sCountryISOCode>
    </CountryCurrency>
  </soap:Body>
</soap:Envelope>"""
  # headers
  headers = {
    'Content-Type': 'text/xml; charset=utf-8'
  }
  # request POST
  response = requests.request("POST", url, headers=headers, data=payload)

  # imprime a resposta
  content = parseString(response.text)
  print(content.documentElement.getElementsByTagName("m:sName")[0].firstChild.nodeValue)

elif campo ==3:
  cod= str(input("Digite o CÓDIGO do idioma(em maiúsculo. Ex: ENG): "))
  # XML estruturado
  payload = f"""<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <LanguageName xmlns="http://www.oorsprong.org/websamples.countryinfo">
      <sISOCode>{cod}</sISOCode>
    </LanguageName>
  </soap:Body>
</soap:Envelope>"""
  # headers
  headers = {
    'Content-Type': 'text/xml; charset=utf-8'
  }
  # request POST
  response = requests.request("POST", url, headers=headers, data=payload)

  # imprime a resposta
  content = parseString(response.text)
  print(content.documentElement.getElementsByTagName("m:LanguageNameResult")[0].firstChild.nodeValue)
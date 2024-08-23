#foi dividido em partes

import zeep

# Define a URL do WSDL para o serviço CountryInfoService
wsdl_url = "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso?WSDL"

# Define a URL do WSDL para o serviço NumberConversion
wsdl_url = "https://www.dataaccess.com/webservicesserver/NumberConversion.wso?WSDL"

# Inicializa o cliente zeep
client = zeep.Client(wsdl=wsdl_url)

# Define o código do país para Noruega (NO)
country_code = "NO"

# Faz a chamada do serviço para obter o nome da capital
result = client.service.CapitalCity(
    sCountryISOCode=country_code
)

# Imprime o nome da capital da Noruega
print(f"A capital da Noruega (NO) é {result}")


# Inicializa o cliente zeep
client = zeep.Client(wsdl=wsdl_url)

# Define o número a ser convertido
number_to_convert = 223

# Faz a chamada do serviço para converter o número por extenso
result = client.service.NumberToWords(
    ubiNum=number_to_convert
)

# Imprime o número por extenso em inglês
print(f"O número {number_to_convert} por extenso é: {result}")

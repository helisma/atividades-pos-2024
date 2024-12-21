import zeep

# define a URL do WSDL
url_countries = "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso?WSDL"
url_number = "https://www.dataaccess.com/webservicesserver/NumberConversion.wso?WSDL"

# inicializa o cliente zeep
client = zeep.Client(wsdl=url_countries)
fun_number = zeep.Client(wsdl=url_number)

print("1 - Para saber o nome do país\n2 - Para ter numeros em extenso")
print("-"*30)
op= int(input("Qual opção: "))

if op==1:
	# define o código do país para BR
	country= str(input("Digite a SIGLA do país (em maiúsculo): "))

	# faz a chamada do serviço
	result = client.service.CountryName(
		sCountryISOCode=country
	)
	# imprime o resultado
	print(f"O nome de/o {country} é: {result}")

elif op == 2:
	num= int(input("Digite o número: "))

	# faz a chamada do serviço
	result = fun_number.service.NumberToWords(
		ubiNum=num
	)
	# imprime o resultado
	print(f"O nome de/o {num} é: {result}")
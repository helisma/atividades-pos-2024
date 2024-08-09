import xml.etree.ElementTree as ET
import json

# Função para parsear um elemento XML para um dicionário Python
def parse_element(element):
    parsed = {}
    if element.text and element.text.strip():
        parsed[element.tag] = element.text.strip()
    for child in element:
        if child.tag not in parsed:
            parsed[child.tag] = parse_element(child)
        else:
            if not isinstance(parsed[child.tag], list):
                parsed[child.tag] = [parsed[child.tag]]
            parsed[child.tag].append(parse_element(child))
    return parsed

# Função para parsear a propriedade 'proprietario'
def parse_proprietario(proprietario):
    result = {}
    for child in proprietario:
        if child.tag == 'nome':
            result['nome'] = child.text
        elif child.tag == 'email':
            result['email'] = {
                'type': child.attrib.get('type', 'pessoal'),
                'value': child.text
            }
        elif child.tag == 'telefone':
            if 'telefone' not in result:
                result['telefone'] = []
            result['telefone'].append(child.text)
    return result

# Função para parsear a estrutura XML
def parse_xml_to_json(xml_string):
    root = ET.fromstring(xml_string)
    imobiliaria = []

    for imovel in root.findall('imovel'):
        imovel_data = {}
        imovel_data['descricao'] = imovel.find('descricao').text

        proprietario = imovel.find('proprietario')
        if proprietario is not None:
            imovel_data['proprietario'] = parse_proprietario(proprietario)

        endereco = imovel.find('endereco')
        if endereco is not None:
            endereco_data = {
                'rua': endereco.find('rua').text,
                'bairro': endereco.find('bairro').text,
                'cidade': endereco.find('cidade').text
            }
            numero = endereco.find('numero')
            if numero is not None and numero.text:
                endereco_data['numero'] = numero.text
            imovel_data['endereco'] = endereco_data

        caracteristicas = imovel.find('caracteristicas')
        if caracteristicas is not None:
            imovel_data['caracteristicas'] = {
                'tamanho': caracteristicas.find('tamanho').text,
                'numQuartos': caracteristicas.find('numQuartos').text,
                'numBanheiros': caracteristicas.find('numBanheiros').text
            }

        imovel_data['valor'] = imovel.find('valor').text
        imobiliaria.append(imovel_data)

    return {'imobiliaria': imobiliaria}

# Exemplo de uso
xml_data = '''<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE imobiliaria [
<!ELEMENT imobiliaria (imovel+)>
<!ELEMENT imovel (descricao, proprietario, endereco, caracteristicas, valor)>
<!ELEMENT descricao (#PCDATA)>
<!ELEMENT proprietario ((nome, email, telefone+)|(nome, telefone))>
<!ELEMENT nome (#PCDATA)>
<!ELEMENT email (#PCDATA)>
<!ELEMENT telefone (#PCDATA)>
<!ELEMENT endereco (rua, bairro, cidade, (numero)?)>
<!ELEMENT rua (#PCDATA)>
<!ELEMENT bairro (#PCDATA)>
<!ELEMENT cidade (#PCDATA)>
<!ELEMENT numero (#PCDATA)>
<!ELEMENT caracteristicas (tamanho, numQuartos+, numBanheiros+)>
<!ELEMENT tamanho (#PCDATA)>
<!ELEMENT numQuartos (#PCDATA)>
<!ELEMENT numBanheiros (#PCDATA)>
<!ELEMENT valor (#PCDATA)>
<!ATTLIST email type (pessoal|trabalho|outro) "pessoal">
]>
<imobiliaria>
    <imovel>
        <descricao>Casa ampla com jardim</descricao>
        <proprietario>
            <nome>Fernanda Santos</nome>
            <email type="pessoal">fernanda.santos@example.com</email>
            <telefone>(11) 9876-5432</telefone>
        </proprietario>
        <endereco>
            <rua>Av. das Palmeiras</rua>
            <bairro>Jardins</bairro>
            <cidade>São Paulo</cidade>
            <numero>345</numero>
        </endereco>
        <caracteristicas>
            <tamanho>300 m²</tamanho>
            <numQuartos>4</numQuartos>
            <numBanheiros>3</numBanheiros>
        </caracteristicas>
        <valor>R$ 1,200,000.00</valor>
    </imovel>
    <imovel>
        <descricao>Apartamento moderno próximo ao metrô</descricao>
        <proprietario>
            <nome>Carlos Lima</nome>
            <email type="trabalho">carlos.lima@corretora.com</email>
            <telefone>(21) 7654-3210</telefone>
        </proprietario>
        <endereco>
            <rua>Rua do Comércio</rua>
            <bairro>Centro</bairro>
            <cidade>Rio de Janeiro</cidade>
            <numero>789, apto 502</numero>
        </endereco>
        <caracteristicas>
            <tamanho>120 m²</tamanho>
            <numQuartos>2</numQuartos>
            <numBanheiros>2</numBanheiros>
        </caracteristicas>
        <valor>R$ 500,000.00</valor>
    </imovel>
    <imovel>
        <descricao>Casa térrea com piscina</descricao>
        <proprietario>
            <nome>Ana Souza</nome>
            <telefone>(31) 1234-5678</telefone>
        </proprietario>
        <endereco>
            <rua>Av. das Flores</rua>
            <bairro>Vila Verde</bairro>
            <cidade>Belo Horizonte</cidade>
        </endereco>
        <caracteristicas>
            <tamanho>250 m²</tamanho>
            <numQuartos>3</numQuartos>
            <numBanheiros>2</numBanheiros>
        </caracteristicas>
        <valor>R$ 800,000.00</valor>
    </imovel>
    <imovel>
        <descricao>Chácara com vista panorâmica</descricao>
        <proprietario>
            <nome>Ricardo Oliveira</nome>
            <email type="pessoal">ricardo.oliveira@example.com</email>
            <telefone>(41) 8765-4321</telefone>
            <telefone>(41) 9876-5432</telefone>
        </proprietario>
        <endereco>
            <rua>Estrada das Águias</rua>
            <bairro>Jardim das Águas</bairro>
            <cidade>Curitiba</cidade>
            <numero/>
        </endereco>
        <caracteristicas>
            <tamanho>1500 m²</tamanho>
            <numQuartos>5</numQuartos>
            <numBanheiros>4</numBanheiros>
        </caracteristicas>
        <valor>R$ 2,000,000.00</valor>
    </imovel>
    <imovel>
        <descricao>Loft sofisticado no centro histórico</descricao>
        <proprietario>
            <nome>Patrícia Costa</nome>
            <email type="trabalho">patricia.costa@arquiteta.com</email>
            <telefone>(51) 2345-6789</telefone>
        </proprietario>
        <endereco>
            <rua>Rua do Rosário</rua>
            <bairro>Centro Histórico</bairro>
            <cidade>Porto Alegre</cidade>
            <numero>123, loft 3</numero>
        </endereco>
        <caracteristicas>
            <tamanho>80 m²</tamanho>
            <numQuartos>1</numQuartos>
            <numBanheiros>1</numBanheiros>
        </caracteristicas>
        <valor>R$ 350,000.00</valor>
    </imovel>
</imobiliaria>'''

# Parse XML and convert to JSON
parsed_data = parse_xml_to_json(xml_data)
json_data = json.dumps(parsed_data, indent=4, ensure_ascii=False)

# Exibir JSON
print(json_data)

#fiquei com preguiça de especificar o xmlKKKKKK ;-; mas é só ir na pasta xml e olhar

from xml.dom.minidom import parse
dom = parse("cardapio.xml")

from xml.dom import minidom

# Função para carregar e parsear o arquivo XML
def load_xml(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return minidom.parse(file)

# Função para exibir o menu de pratos
def display_menu(pratos):
    print("Menu de Pratos:")
    for prato in pratos:
        prato_id = prato.getAttribute('id')
        nome = prato.getElementsByTagName('nome')[0].firstChild.data
        print(f"ID: {prato_id}, Nome: {nome}")

# Função para exibir detalhes do prato
def display_detalhes(prato):
    nome = prato.getElementsByTagName('nome')[0].firstChild.data
    descricao = prato.getElementsByTagName('descricao')[0].firstChild.data
    ingredientes = [i.firstChild.data for i in prato.getElementsByTagName('ingrediente')]
    preco = prato.getElementsByTagName('preco')[0].firstChild.data
    calorias = prato.getElementsByTagName('calorias')[0].firstChild.data
    tempopreparo = prato.getElementsByTagName('tempopreparo')[0].firstChild.data

    print(f"\nDetalhes do prato:")
    print(f"Nome: {nome}")
    print(f"Descrição: {descricao}")
    print(f"Ingredientes: {', '.join(ingredientes)}")
    print(f"Preço: {preco}")
    print(f"Calorias: {calorias}")
    print(f"Tempo de preparo: {tempopreparo}")

def main():
    # Carregar o arquivo XML
    xml_doc = load_xml('cardapio.xml')
    
    # Obter todos os pratos
    pratos = xml_doc.getElementsByTagName('prato')

    while True:
        # Exibir menu
        display_menu(pratos)
        
        # Obter o ID do prato desejado
        prato_id = input("\nDigite o ID do prato para ver os detalhes (ou 'sair' para encerrar): ").strip()
        
        if prato_id.lower() == 'sair':
            print("Saindo...")
            break
        
        # Procurar o prato com o ID fornecido
        prato_encontrado = None
        for prato in pratos:
            if prato.getAttribute('id') == prato_id:
                prato_encontrado = prato
                break
        
        if prato_encontrado:
            display_detalhes(prato_encontrado)
        else:
            print("Prato não encontrado. Tente novamente.")

if __name__ == "__main__":
    main()

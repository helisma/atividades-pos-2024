import requests

api_url= 'https://jsonplaceholder.typicode.com/users/'

print("1 - Para listar todos os usuários\n2 - Para listar tarefa de um usuário \n3 - Para configurações de usuário")
print("-"*30)
campo = int(input("Informe: "))

if campo == 1:
    response = requests.get(api_url).json()
    for user in response:
        print(f"{user['id']} - {user['name']}")

elif campo == 2:
    user_id= int(input("Digite o IDENTIFICADOR do usuário: "))
    response = requests.get(f"{api_url}/{user_id}/todos").json()
    usuario = requests.get(f"{api_url}/{user_id}").json()
    print("-"*30)
    print(f"Tarefas de: {usuario['name']}")
    for todo in response:
        print(f"  {todo['title']}")
        

elif campo == 3:
    print("1 - Para criar usuário\n2 - Para listar dados de um usuário\n3 - Para atualizar dados do usuário\n4 - Para deletar usuário")
    print("-"*30)
    campo = int(input("Informe: "))
    
    if campo == 1:
       
        name = input("Digite o nome do usuário: ")
        username = input("Digite o apelido do usuário: ")
        email =  input("Digite o email do usuário: ")

        print("-"*30)
        print('Outros dados:')

        city= input('Informe a cidade: ')
        street = input('Informe a rua:')

        user_address={
            'city': city,
            'street':street
        }

        user_data= {
            'name': name,
            'username':username,
            'email': email,
            'address': user_address
        }

        #json=user_data: envia o conteúdo de user_data como um JSON no corpo da requisição. 
        response = requests.post(api_url, json=user_data).status_code

        if response == 201:
            print('Show! Você criou um novo usuário')
        else:
            print('Dançou! Tente novamente, algo de errado aconteceu :( )')


    elif campo ==2:
        user_id= int(input("Digite o IDENTIFICADOR do usuário: "))
        response = requests.get(f"{api_url}/{user_id}").json()
        print("-"*30)
        print(f"Nome: {response['name']}\nNome de usuário: {response['username']}\nEmail: {response['email']}")

    elif campo == 3:
        user_id= int(input("Digite o IDENTIFICADOR do usuário: "))

        user_url = (f"{api_url}/{user_id}")

        response = requests.get(user_url).json()
        print("-"*30)
        print(f"Você está atualizando o usuário: {response['name']}")

        name = input("Digite o novo nome do usuário: ")
        username = input("Digite o novo apelido do usuário: ")
        email =  input("Digite o novo email do usuário: ")

        user_data= {
            'name': name,
            'username':username,
            'email': email

        }

        response = requests.patch(user_url, json=user_data).status_code

        if response == 200:
            print('Show! Você atualizou o usuário')
        else:
            print('Dançou! Tente novamente, algo de errado aconteceu :( ')

    elif campo == 4:
        user_id= int(input("Digite o IDENTIFICADOR do usuário: "))
        user_url = (f"{api_url}/{user_id}")
        response = requests.get(user_url).json()

        print(f"Você esta prestes a DELETAR o usuário: {response['name']}")
        campo= input("Prosseguir? (s/n):  ")

        if campo =='s':
            response = requests.delete(user_url).status_code

            if response == 200:
                print('Usuário deletado!')
            else:
                print('Aconteceu algo de errado!')
        elif campo =='n':
            print('Tudo bem!')
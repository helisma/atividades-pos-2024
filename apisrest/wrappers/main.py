from user_wrapper import user_wrapper

# instancia
api = user_wrapper()

print("1 - Para listar usuários\n2 - Para ler um usuário\n3 - Para atualizar dados do usuário\n4 - Para deletar usuário\n5 - Para criar um usuário")
print("-"*30)

campo = int(input("Informe: "))

if campo == 1:
    for user in api.list_user():
        print(f"{user['id']} - {user['name']}")

elif campo == 2:
    user_id = input("Digite o ID do usuário: ")
    user = api.read_user(user_id)
    print(f"{user['name']} - {user['username']} - {user['email']}")

elif campo ==3:
    user_id= int(input("Digite o IDENTIFICADOR do usuário: "))

    old_user = api.read_user(user_id)
    print("-"*30)
    print(f"Você está atualizando o usuário: {old_user['name']}")

    name = input("Digite o novo nome do usuário: ")
    username = input("Digite o novo apelido do usuário: ")
    email =  input("Digite o novo email do usuário: ")

    user_data= {
        'name': name,
        'username':username,
        'email': email

    }

    status = api.update_user(user_id, user_data)
    if status == 200:
        print('Show! Você atualizou o usuário')
    else:
        print('Dançou! Tente novamente, algo de errado aconteceu :( ')



elif campo == 4:
    user_id = input("Digite o ID do usuário: ")
    status = api.delete_user(user_id)
    if status == 200:
        print("Show! você deletou o usuário")
    else:
        print("Algo de errado aconteceu :( ")

elif campo == 5:
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

    status = api.create_user(user_data)
    if status == 201:
            print('Show! Você criou um novo usuário')
    else:
        print('Dançou! Tente novamente, algo de errado aconteceu :( )')
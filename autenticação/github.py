import requests
from requests.auth import HTTPBasicAuth

password = "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"

print("Escolha uma opção:")
print("1: Seguir um usuário")
print("2: Parar de seguir um usuário")
print("3: Listar seus seguidores")
opcao = int(input("Digite a opção: "))

# Seguir um usuário
if opcao == 1:
    user = input("Digite o login do usuário para seguir: ")
    response = requests.put(f'https://api.github.com/user/following/{user}',
                            auth=HTTPBasicAuth('helisma', password))
    if response.status_code == 204:
        print(f"Você seguiu {user} com sucesso!")
    else:
        print(f"Erro ao seguir {user}: {response.status_code}")

# Parar de seguir um usuário
elif opcao == 2:
    user = input("Digite o login do usuário para parar de seguir: ")
    response = requests.delete(f'https://api.github.com/user/following/{user}',
                               auth=HTTPBasicAuth('helisma', password))
    if response.status_code == 204:
        print(f"Você parou de seguir {user} com sucesso!")
    else:
        print(f"Erro ao parar de seguir {user}: {response.status_code}")

# Listar seguidores do usuário logado
elif opcao == 3:
    response = requests.get('https://api.github.com/user/followers',
                            auth=HTTPBasicAuth('helisma', password))
    if response.status_code == 200:
        followers = response.json()
        if followers:
            print("Seus seguidores:")
            for follower in followers:
                print(f"- {follower['login']}")
        else:
            print("Você não tem seguidores.")
    else:
        print(f"Erro ao listar seguidores: {response.status_code}")

# Opção inválida
else:
    print("Opção inválida. Por favor, escolha 1, 2 ou 3.")
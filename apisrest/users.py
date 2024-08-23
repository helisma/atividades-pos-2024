import argparse
import json

# Dados fornecidos
users_data = [
    {
        "id": 1,
        "name": "Leanne Graham",
        "username": "Bret",
        "email": "Sincere@april.biz",
        "address": {
            "street": "Kulas Light",
            "suite": "Apt. 556",
            "city": "Gwenborough",
            "zipcode": "92998-3874",
            "geo": {
                "lat": "-37.3159",
                "lng": "81.1496"
            }
        },
        "phone": "1-770-736-8031 x56442",
        "website": "hildegard.org",
        "company": {
            "name": "Romaguera-Crona",
            "catchPhrase": "Multi-layered client-server neural-net",
            "bs": "harness real-time e-markets"
        }
    },
    {
    "id": 2,
    "name": "Ervin Howell",
    "username": "Antonette",
    "email": "Shanna@melissa.tv",
    "address": {
      "street": "Victor Plains",
      "suite": "Suite 879",
      "city": "Wisokyburgh",
      "zipcode": "90566-7771",
      "geo": {
        "lat": "-43.9509",
        "lng": "-34.4618"
      }
    },
    "phone": "010-692-6593 x09125",
    "website": "anastasia.net",
    "company": {
      "name": "Deckow-Crist",
      "catchPhrase": "Proactive didactic contingency",
      "bs": "synergize scalable supply-chains"
    }
  },
  {
    "id": 3,
    "name": "Clementine Bauch",
    "username": "Samantha",
    "email": "Nathan@yesenia.net",
    "address": {
      "street": "Douglas Extension",
      "suite": "Suite 847",
      "city": "McKenziehaven",
      "zipcode": "59590-4157",
      "geo": {
        "lat": "-68.6102",
        "lng": "-47.0653"
      }
    },
    "phone": "1-463-123-4447",
    "website": "ramiro.info",
    "company": {
      "name": "Romaguera-Jacobson",
      "catchPhrase": "Face to face bifurcated interface",
      "bs": "e-enable strategic applications"
    }
  },
  {
    "id": 4,
    "name": "Patricia Lebsack",
    "username": "Karianne",
    "email": "Julianne.OConner@kory.org",
    "address": {
      "street": "Hoeger Mall",
      "suite": "Apt. 692",
      "city": "South Elvis",
      "zipcode": "53919-4257",
      "geo": {
        "lat": "29.4572",
        "lng": "-164.2990"
      }
    },
    "phone": "493-170-9623 x156",
    "website": "kale.biz",
    "company": {
      "name": "Robel-Corkery",
      "catchPhrase": "Multi-tiered zero tolerance productivity",
      "bs": "transition cutting-edge web services"
    }
  },
  {
    "id": 5,
    "name": "Chelsey Dietrich",
    "username": "Kamren",
    "email": "Lucio_Hettinger@annie.ca",
    "address": {
      "street": "Skiles Walks",
      "suite": "Suite 351",
      "city": "Roscoeview",
      "zipcode": "33263",
      "geo": {
        "lat": "-31.8129",
        "lng": "62.5342"
      }
    },
    "phone": "(254)954-1289",
    "website": "demarco.info",
    "company": {
      "name": "Keebler LLC",
      "catchPhrase": "User-centric fault-tolerant solution",
      "bs": "revolutionize end-to-end systems"
    }
  },
  {
    "id": 6,
    "name": "Mrs. Dennis Schulist",
    "username": "Leopoldo_Corkery",
    "email": "Karley_Dach@jasper.info",
    "address": {
      "street": "Norberto Crossing",
      "suite": "Apt. 950",
      "city": "South Christy",
      "zipcode": "23505-1337",
      "geo": {
        "lat": "-71.4197",
        "lng": "71.7478"
      }
    },
    "phone": "1-477-935-8478 x6430",
    "website": "ola.org",
    "company": {
      "name": "Considine-Lockman",
      "catchPhrase": "Synchronised bottom-line interface",
      "bs": "e-enable innovative applications"
    }
  },
  {
    "id": 7,
    "name": "Kurtis Weissnat",
    "username": "Elwyn.Skiles",
    "email": "Telly.Hoeger@billy.biz",
    "address": {
      "street": "Rex Trail",
      "suite": "Suite 280",
      "city": "Howemouth",
      "zipcode": "58804-1099",
      "geo": {
        "lat": "24.8918",
        "lng": "21.8984"
      }
    },
    "phone": "210.067.6132",
    "website": "elvis.io",
    "company": {
      "name": "Johns Group",
      "catchPhrase": "Configurable multimedia task-force",
      "bs": "generate enterprise e-tailers"
    }
  },
  {
    "id": 8,
    "name": "Nicholas Runolfsdottir V",
    "username": "Maxime_Nienow",
    "email": "Sherwood@rosamond.me",
    "address": {
      "street": "Ellsworth Summit",
      "suite": "Suite 729",
      "city": "Aliyaview",
      "zipcode": "45169",
      "geo": {
        "lat": "-14.3990",
        "lng": "-120.7677"
      }
    },
    "phone": "586.493.6943 x140",
    "website": "jacynthe.com",
    "company": {
      "name": "Abernathy Group",
      "catchPhrase": "Implemented secondary concept",
      "bs": "e-enable extensible e-tailers"
    }
  },
  {
    "id": 9,
    "name": "Glenna Reichert",
    "username": "Delphine",
    "email": "Chaim_McDermott@dana.io",
    "address": {
      "street": "Dayna Park",
      "suite": "Suite 449",
      "city": "Bartholomebury",
      "zipcode": "76495-3109",
      "geo": {
        "lat": "24.6463",
        "lng": "-168.8889"
      }
    },
    "phone": "(775)976-6794 x41206",
    "website": "conrad.com",
    "company": {
      "name": "Yost and Sons",
      "catchPhrase": "Switchable contextually-based project",
      "bs": "aggregate real-time technologies"
    }
  },
  {
    "id": 10,
    "name": "Clementina DuBuque",
    "username": "Moriah.Stanton",
    "email": "Rey.Padberg@karina.biz",
    "address": {
      "street": "Kattie Turnpike",
      "suite": "Suite 198",
      "city": "Lebsackbury",
      "zipcode": "31428-2261",
      "geo": {
        "lat": "-38.2386",
        "lng": "57.2232"
      }
    },
    "phone": "024-648-3804",
    "website": "ambrose.net",
    "company": {
      "name": "Hoeger LLC",
      "catchPhrase": "Centralized empowering task-force",
      "bs": "target end-to-end models"
    }
  }
]
    # Outros usuários...

# Funções CRUD
def listar_usuarios():
    for user in users_data:
        print(json.dumps(user, indent=4))

def obter_usuario(user_id):
    user = next((user for user in users_data if user["id"] == user_id), None)
    if user:
        print(json.dumps(user, indent=4))
    else:
        print(f"Usuário com ID {user_id} não encontrado.")

def criar_usuario(user):
    users_data.append(user)
    print("Usuário criado com sucesso!")

def atualizar_usuario(user_id, updated_user):
    index = next((i for i, user in enumerate(users_data) if user["id"] == user_id), None)
    if index is not None:
        users_data[index].update(updated_user)
        print("Usuário atualizado com sucesso!")
    else:
        print(f"Usuário com ID {user_id} não encontrado.")

def deletar_usuario(user_id):
    global users_data
    users_data = [user for user in users_data if user["id"] != user_id]
    print(f"Usuário com ID {user_id} deletado com sucesso!")

def listar_todos_usuario(user_id):
    # Este método é uma simulação, pois os "todos" não foram fornecidos nos dados.
    # Em um caso real, seria necessário buscar essa informação de uma fonte.
    print(f"Listando tarefas para o usuário com ID {user_id}... (Esta é uma função simulada)")

# CLI usando argparse
def main():
    parser = argparse.ArgumentParser(description="CLI para Gerenciamento de Usuários da JSON Placeholder")

    subparsers = parser.add_subparsers(dest="comando", required=True)

    # Listar todos os usuários
    subparsers.add_parser("listar_usuarios", help="Lista todos os usuários")

    # Listar as tarefas de um usuário específico
    todos_parser = subparsers.add_parser("listar_todos", help="Lista as tarefas de um usuário específico")
    todos_parser.add_argument("user_id", type=int, help="ID do usuário")

    # Criar um novo usuário
    criar_parser = subparsers.add_parser("criar_usuario", help="Cria um novo usuário")
    criar_parser.add_argument("--id", type=int, required=True, help="ID do usuário")
    criar_parser.add_argument("--name", type=str, required=True, help="Nome do usuário")
    criar_parser.add_argument("--username", type=str, required=True, help="Nome de usuário")
    criar_parser.add_argument("--email", type=str, required=True, help="Email")
    criar_parser.add_argument("--phone", type=str, required=True, help="Telefone")
    criar_parser.add_argument("--website", type=str, required=True, help="Website")

    # Obter detalhes de um usuário específico
    obter_parser = subparsers.add_parser("obter_usuario", help="Obtém detalhes de um usuário específico")
    obter_parser.add_argument("user_id", type=int, help="ID do usuário")

    # Atualizar um usuário existente
    atualizar_parser = subparsers.add_parser("atualizar_usuario", help="Atualiza um usuário existente")
    atualizar_parser.add_argument("user_id", type=int, help="ID do usuário")
    atualizar_parser.add_argument("--name", type=str, help="Nome do usuário")
    atualizar_parser.add_argument("--username", type=str, help="Nome de usuário")
    atualizar_parser.add_argument("--email", type=str, help="Email")
    atualizar_parser.add_argument("--phone", type=str, help="Telefone")
    atualizar_parser.add_argument("--website", type=str, help="Website")

    # Deletar um usuário
    deletar_parser = subparsers.add_parser("deletar_usuario", help="Deleta um usuário")
    deletar_parser.add_argument("user_id", type=int, help="ID do usuário")

    args = parser.parse_args()

    if args.comando == "listar_usuarios":
        listar_usuarios()
    elif args.comando == "listar_todos":
        listar_todos_usuario(args.user_id)
    elif args.comando == "criar_usuario":
        user = {
            "id": args.id,
            "name": args.name,
            "username": args.username,
            "email": args.email,
            "phone": args.phone,
            "website": args.website,
            "address": {},
            "company": {}
        }
        criar_usuario(user)
    elif args.comando == "obter_usuario":
        obter_usuario(args.user_id)
    elif args.comando == "atualizar_usuario":
        updated_user = {
            "name": args.name,
            "username": args.username,
            "email": args.email,
            "phone": args.phone,
            "website": args.website
        }
        atualizar_usuario(args.user_id, {k: v for k, v in updated_user.items() if v is not None})
    elif args.comando == "deletar_usuario":
        deletar_usuario(args.user_id)

if __name__ == "__main__":
    main()

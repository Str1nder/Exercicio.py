user = ["Guilherme", "Gustavo", "Rodrigo"]
senha = ["g111", "g222", "r333"]

input_user = input("Entre com o nome de usuário: ").lower()
input_senha = input("Entre com a senha do usuário: ").lower()

for index in range(0,len(user)):
    if (input_user == user[index]) and (input_senha == senha[index]):
        print("Sucesso")
    else: ("Dados incorretos.")
acesso = input("Digite seu nível de acesso: ")
genero = input("Digite seu gênero: ")

acesso = acesso.upper()
genero = genero.upper()

if acesso == "ADM" and genero == "HOMEM":
   print("Olá administrador!")
elif acesso == "ADM" and genero == "MULHER":
   print("Olá administradora!")
elif acesso == "USER" and genero == "HOMEM":
   print("Olá usuário!")
elif acesso == "USER" and genero == "MULHER":
   print("Olá usuária!")
elif acesso == "GUEST":
   print("Olá visitante!")
else:
   print("Olá desconhecido")

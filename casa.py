graduacao = str(input(" digite qual graduação você faz:  ")).title()
if graduacao == "Tecnologo" and graduacao == "Tecnólogo":
    print (" tecnologo tem duração de 2 a 3 anos ")
elif graduacao == "Bacharelado":
    print ("a duração de um Bacharelado é de 4 a 5 anos.")
else:
    print ("curso não encontrada")

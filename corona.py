nome=input("digite seu nome: ")
idade=int(input("digite sua idade: "))
doença_infectocontagiosa=input("suspeita de doença infectocontagiosa?").upper()
if idade >=65 and doença_infectocontagiosa=="SIM":
    print("o paciente será direcionado para a sala AMARELA -COM PRIORIDADE!!")
elif idade < 65 and doença_infectocontagiosa == "SIM":
    print("o paciente será direcionado para a sala AMARELA -SEM PRIORIDADE!!")
elif idade >=65 and doença_infectocontagiosa == "NÃO":
    print("o paciente será direcionado para a sala BRANCA -COM PRIORIDADE!!")
elif idade >=65 and doença_infectocontagiosa == "NÃO":
    print("o paciente será direcionado para a sala BRANCA -COM PRIORIDADE!!")
else:
    print("responda a suspeita de doença infectocotagiosa com SIM ou NÃO")


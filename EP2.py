import random

while True:

	lista_de_inspermons=["Hsumon","Diegomon","Hsumon","Teramon"]  # Criação dos Inspermons

	print("Bem vindo ao Inspermón")  # Início do jogo

	nome = input("Qual o nome do seu Inspermón? ")  # Caracterização do próprio personagem
	ataque1=5
	defesa=5
	vida=20
# Início do jogo:
	while True:  # Jogo
		comando = input("O que você deseja fazer? (passear ou dormir")  # Pergunta sobre o que o usuário deseja fazer

		if comando == "dormir":   # Dormir: para o jogo e salva os dados
			break

# Inspermon adversário:
		elif comando == "passear":   # Passear em busca de novos inspermons
			x=random.randint(0,len(lista_de_inspermons))   # Escolha aleatória do inspermon adversário
			print("Voce esta batalhando contra {}".format(x))  

			ataque_oponente=random.randint(1,10)  # Definição aleatória do atributos do Inspermon adversário
			defesa_oponente=random.randint(1,10)
			vida_oponente=random.randint(10,20)

			print("Este Inspermón possui os seguintes atributos: {} de ataque, {} de defesa e {} de vida" .format (ataque_oponente, defesa_oponente, vida_oponente))

# Batalha:
			while True:

				ataque_ativo=int(input("Qual ataque deseja usar? "))  # Escolha do ataque a ser utilizado

				if ataque_ativo == 1:  # Ataque 1 é o ataque do inspermon igual a seu atributo
					if ataque1-defesa_oponente>0:
						vida_oponente=vida_oponente-(ataque1-defesa_oponente)

						if vida_oponente>0:  # Realização do ataque e atualização da vida restante
							print("{} deu {} de dano em seu oponente, agora ele tem {} de vida".format(nome,ataque1-defesa_oponente,vida_oponente))  # Cálculo da vida restante
							continue

					if ataque1-defesa_oponente<=0:
						print("{} não deu dano em seu oponente, ele continua com {} de vida".format(nome,vida_oponente))
						continue

					if vida_oponente<=0:
						print("Voce derrotou esse Inspermon!")
						break

				elif ataque_ativo == 2:
					ataque2=random.randint(1,10)

					if ataque2-defesa_oponente>0:
						vida_oponente=vida_oponente-(ataque2-defesa_oponente)

						if vida_oponente>0:  # Realização do ataque e atualização da vida restante
							print("{} deu {} de dano em seu oponente, agora ele tem {} de vida".format(nome,ataque2-defesa_oponente,vida_oponente))  # Cálculo da vida restante
							continue

					if ataque2-defesa_oponente<=0:
						print("{} não deu dano em seu oponente, ele continua com {} de vida".format(nome,vida_oponente))
						continue

					if vida_oponente<=0:
						print("Voce derrotou esse Inspermon!")
						break
				else:
					print("Digite um ataque valido!")
					continue

			continue

		else:
			print("Digite um comando válido.")

	print("Até a proxima!")

	continue

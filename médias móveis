    opcao = 1
tamanho_da_curta= int(input("digite o tamanho da média curta: "))
tamanho_da_longa= int(input("digite o tamanho da média longa: "))
serie= []
media_curta =[]
media_longa = []
tendencia = []
gambiarra = -1
def entrada():
    valores_entrada = float(input("Digite o valor de entrada: "))
    serie.append(valores_entrada)

def calculo_media(serie,media,tamanho):
    posicao = len(serie) - 1             #acha a posição do valor adicionado  
    if len(serie)<tamanho:
        auxiliar = []
        for i in range(len(serie)):
            auxiliar.append(serie[posicao - i])
        media.append(sum(auxiliar)/len(auxiliar))
    else:
        auxiliar = []
        for i in range(tamanho):
            auxiliar.append(serie[posicao - i])
        media.append(sum(auxiliar)/tamanho)

def calculotendencia(media_curta,media_longa,tendencia,gambiarra):
    if media_curta>media_longa and tendencia[gambiarra] != "alta":
        gambiarra = len(tendencia)
        tendencia.append("alta")
    elif media_curta<media_longa and tendencia[gambiarra]!= "queda":
        gambiarra = len(tendencia)
        tendencia.append("queda")
    else:
        tendencia.append("constante")

    return gambiarra


while opcao !=0:
    print("")
    print("1 -adicionar dados")
    print("2 - mostrar série atual")
    print("3 - alterar item")
    print("4 - mostrar as médias e tendências")
    print("5 - sair")
    opcao = int(input("Digite a opção:" ))
    if opcao == 1:
        entrada()
        #calcular as médias aqui dentro, por facilidade
        calculo_media(serie,media_curta,tamanho_da_curta)
        calculo_media(serie,media_longa,tamanho_da_longa)
        gambiarra = calculotendencia(media_curta,media_longa,tendencia,gambiarra)
    elif opcao == 2:
        print(serie)
    elif opcao == 3:
        qual_item = int(input("Digite a posição do item que quer alterar: "))
        tamanho_da_serie = len(serie)
        if qual_item >=0 and qual_item < tamanho_da_serie:
            serie[qual_item] = float(input("Digite um novo valor: "))
        else:
            print("posição não cadastrada")
    elif opcao == 4:
        aux = []
        teste = []
        matriz = []
        for i in range(len(media_curta)-1):
            aux.append(media_curta[i])
            aux.append(media_longa[i])
            aux.append(tendencia[i])
            matriz.append(aux)
            aux = []
        print("================== MÉDIAS E TENDÊNCIAS ===============")
        print("MM3 - MM5 - TENDÊNCIA")
        for i in range(len(media_curta)):
            print("{:.3f} - {:.3f} - {}".format(media_curta[i],media_longa[i], tendencia[i]))
            print("---------------------------------------------------")

    elif opcao == 5:
        print("Programa finalizado.")
    
    else:
        print("opçao invalida!")


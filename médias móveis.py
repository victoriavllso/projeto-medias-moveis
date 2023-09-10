tamanho_da_curta = int(input("Digite o tamanho da média curta: "))
tamanho_da_longa = int(input("Digite o tamanho da média longa: "))
serie = []
media_curta = []
media_longa = []
tendencia = []

def entrada():
    valores_entrada = float(input("Digite o valor de entrada: "))
    serie.append(valores_entrada)

def calculo_media(serie, tamanho):
    if len(serie) < tamanho:
        return sum(serie) / len(serie)
    else:
        return sum(serie[-tamanho:]) / tamanho

def calculo_tendencia(media_curta, media_longa, tendencia):
    if media_curta > media_longa:
        tendencia.append("alta")
    elif media_curta < media_longa:
        tendencia.append("queda")
    else:
        tendencia.append("constante")

while True:
    print("\n1 - Adicionar dados")
    print("2 - Mostrar série atual")
    print("3 - Alterar item")
    print("4 - Mostrar médias e tendências")
    print("5 - Sair")
    
    opcao = int(input("Digite a opção: "))

    if opcao == 1:
        entrada()
        media_curta_atual = calculo_media(serie, tamanho_da_curta)
        media_longa_atual = calculo_media(serie, tamanho_da_longa)
        calculo_tendencia(media_curta_atual, media_longa_atual, tendencia)
    elif opcao == 2:
        print(serie)
    elif opcao == 3:
        qual_item = int(input("Digite a posição do item que quer alterar: "))
        tamanho_da_serie = len(serie)
        if 0 <= qual_item < tamanho_da_serie:
            serie[qual_item] = float(input("Digite um novo valor: "))
        else:
            print("Posição não cadastrada")
    elif opcao == 4:
        print("================== MÉDIAS E TENDÊNCIAS ===============")
        print("MM3 - MM5 - TENDÊNCIA")
        for i in range(len(serie)):
            if i < tamanho_da_curta - 1:
                media_curta_atual = calculo_media(serie[:i + 1], i + 1)
            else:
                media_curta_atual = calculo_media(serie[i - tamanho_da_curta + 1:i + 1], tamanho_da_curta)
            if i < tamanho_da_longa - 1:
                media_longa_atual = calculo_media(serie[:i + 1], i + 1)
            else:
                media_longa_atual = calculo_media(serie[i - tamanho_da_longa + 1:i + 1], tamanho_da_longa)
            
            calculo_tendencia(media_curta_atual, media_longa_atual, tendencia)
            
            print("{:.3f} - {:.3f} - {}".format(media_curta_atual, media_longa_atual, tendencia[i]))
            print("---------------------------------------------------")
    elif opcao == 5:
        print("Programa finalizado.")
        break
    else:
        print("Opção inválida!")

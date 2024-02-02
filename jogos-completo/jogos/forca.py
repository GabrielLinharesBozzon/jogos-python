def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")
    palavra_secreta="banana" 
    enforcou = False
    acertou = False
    while(not enforcou and not acertou):
        chute=input("Digite uma letra:\n").strip().lower()
        index=0 
        for letra in palavra_secreta:   
            if(chute==letra):
                print("Encontrei a letra {} na posição{}".format(chute,index))
        index = index + 1    
        print("jogando...")


if(__name__ == "__main__"):
    jogar()

print("Fim do jogo")
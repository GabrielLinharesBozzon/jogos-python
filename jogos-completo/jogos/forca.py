def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")
    palavra_secreta="banana" 
    enforcou = False
    acertou = False
    chute=input("Digite uma letra:\n")
    while(not enforcou and not acertou): 
        for letra in palavra_secreta:   
            if(chute==letra):
                print("Encontrei a letra {} na posição{}".format(chute,index))
        index=index+1    
    print("jogando...")
print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()

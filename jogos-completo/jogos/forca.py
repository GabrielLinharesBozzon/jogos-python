import random
def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")
    palavras_para_forca = ["python", "javascript", "java", "ruby", "html", "css", "react", "angular", "django", "flask"]
    palavra_secreta=random.choice(palavras_para_forca) 
    #                       variável de descarte
    letras_acertadas = ["_" for _ in palavra_secreta]#compreensão de lista
    enforcou = False
    acertou = False

    erros= 0 

    while(not enforcou and not acertou):
        chute=input("Digite uma letra:\n").strip().lower()
        index=0     
        
        if (chute in palavra_secreta):
            for letra in palavra_secreta:   
                if(chute == letra):
                    letras_acertadas[index]=letra     
                index += 1        
        else:
            erros+=1

        enforcou = erros==6  
        acertou = "_" not in letras_acertadas 
        print(letras_acertadas)
        print("jogando...")
        
    if(acertou):        
        print("Acertou!!!")
    else:
        print("Voce perdeu a palavra era:\n{}".format(palavra_secreta))
        

        
if(__name__ == "__main__"):
    jogar()

print("Fim do jogo")
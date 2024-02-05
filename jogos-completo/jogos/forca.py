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

        enforcou = erros==7  
        acertou = "_" not in letras_acertadas 
        print(letras_acertadas)
        print("jogando...")
        print("  _______     ")
        print(" |/      |    ")

        if(erros == 1):
            print(" |      (_)   ")
            print(" |            ")
            print(" |            ")
            print(" |            ")
    
        if(erros == 2):
            print(" |      (_)   ")
            print(" |      \     ")
            print(" |            ")
            print(" |            ")
    
        if(erros == 3):
            print(" |      (_)   ")
            print(" |      \|    ")
            print(" |            ")
            print(" |            ")

        if(erros == 4):
            print(" |      (_)   ")
            print(" |      \|/   ")
            print(" |            ")
            print(" |            ")

        if(erros == 5):
            print(" |      (_)   ")
            print(" |      \|/   ")
            print(" |       |    ")
            print(" |            ")

        if(erros == 6):
            print(" |      (_)   ")
            print(" |      \|/   ")
            print(" |       |    ")
            print(" |      /     ")

        if (erros == 7):
            print(" |      (_)   ")
            print(" |      \|/   ")
            print(" |       |    ")
            print(" |      / \   ")

        print(" |            ")
        print("_|___         ")
        print()
        
    if(acertou):        
        print("Acertou!!!")
        print("Parabéns, você ganhou!")
        print("       ___________      ")
        print("      '._==_==_=_.'     ")
        print("      .-\\:      /-.    ")
        print("     | (|:.     |) |    ")
        print("      '-|:.     |-'     ")
        print("        \\::.    /      ")
        print("         '::. .'        ")
        print("           ) (          ")
        print("         _.' '._        ")
        print("        '-------'       ")
    else:
        print("Voce perdeu a palavra era:\n{}".format(palavra_secreta))
        print("A palavra era {}".format(palavra_secreta))
        print("    _______________         ")
        print("   /               \       ")
        print("  /                 \      ")
        print("//                   \/\  ")
        print("\|   XXXX     XXXX   | /   ")
        print(" |   XXXX     XXXX   |/     ")
        print(" |   XXX       XXX   |      ")
        print(" |                   |      ")
        print(" \__      XXX      __/     ")
        print("   |\     XXX     /|       ")
        print("   | |           | |        ")
        print("   | I I I I I I I |        ")
        print("   |  I I I I I I  |        ")
        print("   \_             _/       ")
        print("     \_         _/         ")
        print("       \_______/           ")
        

        
if(__name__ == "__main__"):
    jogar()

print("Fim do jogo")
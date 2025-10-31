import random

def jogo_forca():
    palavras = ['python', 'programacao', 'computador', 'algoritmo', 'desenvolvimento']
    palavra = random.choice(palavras)
    letras_corretas = []
    tentativas = 6
    
    while tentativas > 0:
        # Mostrar palavra com underscores
        palavra_mostrada = ''
        for letra in palavra:
            if letra in letras_corretas:
                palavra_mostrada += letra + ' '
            else:
                palavra_mostrada += '_ '
        
        print(f"\nPalavra: {palavra_mostrada}")
        print(f"Tentativas restantes: {tentativas}")
        
        if '_' not in palavra_mostrada:
            print("🎉 Parabéns! Você ganhou!")
            break
            
        palpite = input("Digite uma letra: ").lower()
        
        if palpite in palavra:
            letras_corretas.append(palpite)
        else:
            tentativas -= 1
            print("Letra incorreta!")
    else:
        print(f"💀 Game Over! A palavra era: {palavra}")

jogo_forca()

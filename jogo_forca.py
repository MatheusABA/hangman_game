
import os

palavra_secreta = "FUTEBOL"
resposta = palavra_secreta.translate("*"*256)
letras_acertadas = ''
tentativas_user = 0


print('Bem-vindo ao jogo da palavra secreta!')
while True:

    letra_user = input('Para começar, digite uma letra qualquer: ')
    letra_user = letra_user.capitalize()

    if len(letra_user) > 1 and letra_user == 'Sair':
            print('O jogo será fechado, obrigado por jogar!')
            
            break
        
        
    elif len(letra_user) > 1:
        print('Mais de uma letra foi digitada, tente novamente!!')
        continue
        
        
    elif len(letra_user) == 1:
        tentativas_user += 1
        if letra_user in palavra_secreta and letra_user not in letras_acertadas:
            letras_acertadas += letra_user
    
               
        elif letra_user in palavra_secreta and letra_user  in letras_acertadas:
            print('Letra ja foi acertada ')

            
            
        elif letra_user not in palavra_secreta:
            print('Letra não aparece na palavra secreta')
    
        
        
        palavra_certa = ''
        for letra_secreta in palavra_secreta:
            if letra_secreta in letras_acertadas:
                palavra_certa += f'{letra_secreta}'
            else:
                palavra_certa += '_'
        
        print(palavra_certa)

                
        if palavra_certa == palavra_secreta:
            os.system('cls')
            print(
                f'Parabens!!! Você ganhou. A palavra secreta era {palavra_secreta}')
            print(
                f'Quantidade de tentativas do usuário: {tentativas_user}')
            break
        
                          
        
        
        
        
    
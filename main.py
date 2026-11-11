character_list = []
decision = 0

def create_character(name_character, classes, level, strength):

    #modifier = (strength - 10) // 2

    character = (name_character, classes, level, strength)
    return character_list.append(character)
    


def list_character(character_list):
    if not character_list:
        print('Nenhum personagem criado ainda.\n')
    index = 1
    for name_character, classes, level, strength in character_list:
        print(f'Personagem {index}\nNome: {name_character}\nClasse: {classes}\nNível: {level}\nForça: {strength}')
        index += 1

while decision != 3:
    print('[1] Criar personagem')
    print('[2] Listar personagem')
    print('[3] Sair')
    print()
    try:
        decision = int(input('O que deseja? '))
    except ValueError:
        print('Digite um número inteiro.')
        continue

    if decision == 1:
        name_character = input('Qual o nome do personagem: ')
        classes = input('Qual a classe do personagem: ')
        level = 1
        strength = int(input('Força: '))
        create_character(name_character, classes, level, strength)
    elif decision == 2:
        list_character(character_list)
    else:
        break

print('Obrigado por fazer sua ficha de personagem conosco.')

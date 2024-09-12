import os
from models.restaurant import Restaurant

# Exemplos de restaurantes cadastrados
restaurant_lolita = Restaurant('lolita', 'francês')
restaurant_doce_cabana = Restaurant('doce cabana', 'argentino')
restaurant_mineiro_de_comer = Restaurant('mineiro de comer', 'brasileiro')

def clear_menu():
    os.system('cls')


def return_menu():
    input('\n⬅️   Digite ENTER para voltar ao menu principal.')
    clear_menu()


def input_validation(input_name):
    while True:
        if input_name == '':
            input_name = input(
                '\n🚫  Por favor, informe uma entrada válida: ')
        else:
            break

    return input_name


def exit_the_program():
    clear_menu()
    print('\nOBRIGADO POR USAR O APP SABOR EXPRESS, VOLTE SEMPRE❗')


def register_restaurant():
    print('\n1. CADASTRAR RESTAURANTE')

    name_restaurant = input('\n⚠️   Informe o nome do restaurante: ', )
    name_restaurant = input_validation(name_restaurant)

    category_restaurant = input('\n⚠️   Informe o tipo do restaurante: ', )
    category_restaurant = input_validation(category_restaurant)

    Restaurant(name_restaurant, category_restaurant)

    print('\n✅  Cadastro do restaurante efetuado com sucesso.')


def active_restaurant():
    print('3. ALTERNAR SITUAÇÃO DO RESTAURANTE\n')

    Restaurant.restaurant_list()

    restaurant_name = input(
        '\n⚠️   Digite o nome do restaurante que deseja alterar o status: ')

    restaurant_name = input_validation(restaurant_name)
    restaurant_found = Restaurant.change_restaurant_status(restaurant_name)

    if restaurant_found == False:
        print(f'\n🚫  Restaurante não encontrado.')
    else:
        print(f'\n✅  Status do restaurante alterado com sucesso.')


def review_restaurant():
    print('4. AVALIAR RESTAURANTE\n')

    Restaurant.restaurant_list()

    client_name = input(
        '\n⚠️   Digite o seu nome: ')
    client_name = input_validation(client_name)

    rating = input(
        '\n⚠️   Digite uma nota entre 0 e 5 para avaliar o restaurante: ')
    rating = input_validation(rating)

    rating = float(rating)

    while True:
        if rating < 0 or rating > 5:
            rating = input(
            '\n🚫  Digite uma nota entre 0 e 5, sua nota digitada não pode ser validada: ')
            rating = input_validation(rating)
            rating = float(rating)
        else:
            break    

    restaurant_name = input(
        '\n⚠️   Digite o nome do restaurante que deseja avaliar: ')
    restaurant_name = input_validation(restaurant_name)

    restaurant_review = Restaurant.receive_evaluation(
        restaurant_name, client_name, rating)

    if restaurant_review == False:
        print(f'\n🚫  Restaurante não encontrado.')
    else:
        print(f'\n✅  Restaurante avaliado com sucesso, sua nota foi {
              restaurant_review}')


def list_restaurant_review():
    print('5. LISTAR AVALIAÇÕES DO RESTAURANTE\n')

    Restaurant.restaurant_list()

    restaurant_name = input(
        '\n⚠️   Digite o nome do restaurante: ')
    restaurant_name = input_validation(restaurant_name)

    reviews = Restaurant.list_restaurant_reviews(restaurant_name)

    if reviews == []:
        print(f'\n⚠️   O restaurante {
              restaurant_name.title()} não recebeu nenhuma avaliação.')

    elif reviews == False:
        print(f'\n⚠️   Restaurante não encontrado.')

    else:
        print('\n')

        for review in reviews:
            print(review)


def menu():
    print('''
░█▀▀▀█ ─█▀▀█ ░█▀▀█ ░█▀▀▀█ ░█▀▀█ 　 ░█▀▀▀ ▀▄░▄▀ ░█▀▀█ ░█▀▀█ ░█▀▀▀ ░█▀▀▀█ ░█▀▀▀█
─▀▀▀▄▄ ░█▄▄█ ░█▀▀▄ ░█──░█ ░█▄▄▀ 　 ░█▀▀▀ ─░█── ░█▄▄█ ░█▄▄▀ ░█▀▀▀ ─▀▀▀▄▄ ─▀▀▀▄▄
░█▄▄▄█ ░█─░█ ░█▄▄█ ░█▄▄▄█ ░█─░█ 　 ░█▄▄▄ ▄▀░▀▄ ░█─── ░█─░█ ░█▄▄▄ ░█▄▄▄█ ░█▄▄▄█
''')

    print('\n🅼 🅴 🅽 🆄\n')
    menu_options = [
        '[1] Cadastrar restaurante',
        '[2] Listar restaurantes',
        '[3] Alternar situação do restaurante',
        '[4] Avaliar restaurante',
        '[5] Listar avaliações do restaurante por cliente',
        '[6] Sair'
    ]

    for option in menu_options:
        print(option)


def selection_of_menu_options():
    while True:
        menu()

        try:
            option_chosen = int(input('\nEscolha uma opção: '))

            match option_chosen:
                case 1:
                    clear_menu()
                    register_restaurant()
                    return_menu()
                case 2:
                    clear_menu()
                    print('2. LISTAR RESTAURANTES\n')
                    Restaurant.restaurant_list()
                    return_menu()
                case 3:
                    clear_menu()
                    active_restaurant()
                    return_menu()
                case 4:
                    clear_menu()
                    review_restaurant()
                    return_menu()
                case 5:
                    clear_menu()
                    list_restaurant_review()
                    return_menu()
                case 6:
                    exit_the_program()
                    break
                case _:
                    clear_menu()
                    print('\n🚫  Opção inválida, tente novamente.')
                    return_menu()

        except ValueError:
            clear_menu()
            print('\n🚫  Entrada inválida, tente novamente.')
            return_menu()


def main():
    selection_of_menu_options()


if __name__ == '__main__':
    main()

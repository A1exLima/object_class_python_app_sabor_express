from models.review_restaurant import Review_restaurant


class Restaurant:  # Cria uma classe do objeto Restaurante
    restaurants = []

    # Método para definir as propriedades do objeto
    def __init__(self, name, category):
        self._name = name.title()
        self._category = category.upper()
        self._active = False
        self._review = []
        self._average_reviews = 0
        Restaurant.restaurants.append(self)

    # Método para definir o retorno do objeto em formato string
    def __str__(self):
        return f'{self._name} | {self._category}'

    # Propriedade para exibir True ou False como Ativado ou desativado em formato str
    @property
    def active(self):
        return '✅ Ativado' if self._active else "❌ Inativo"

    # Propriedade para calcular a média das avaliações
    @property
    def average_reviews(self):
        if not self._review:
            self._average_reviews = 0
            return '-'
        else:
            media = sum(float(rating._rating)
                        for rating in self._review) / len(self._review)
            return round(media, 1)

    # Método próprio para listar restaurantes
    @classmethod
    def restaurant_list(cls):
        print(
            f'{'Índice':2} | {'Nome do Restaurante'.ljust(20)} | {'Categoria'.ljust(20)} | {'Status'.ljust(16)} | {'Média avaliações'} ')

        for index, restaurant in enumerate(cls.restaurants):
            print(
                f'{(index + 1):6} | {restaurant._name.ljust(20)} | {restaurant._category.ljust(20)} | {restaurant.active.ljust(15)} | {restaurant.average_reviews}')

    # Método próprio para ATIVAR ou DESATIVAR restaurante pelo nome
    def change_restaurant_status(name):
        restaurant_name = name.title()
        restaurant_found = False

        for restaurant in Restaurant.restaurants:
            if restaurant._name == restaurant_name:
                restaurant._active = not restaurant._active
                restaurant_found = True
                return restaurant_found

        return restaurant_found

        self._active = not self._active

    # Método próprio para buscar restaurante e armazenar um dicionário na variável restaurant._review com os dados individuais de cada avaliação por cliente
    def receive_evaluation(restaurant_name, client_name, rating):
        restaurant_name = restaurant_name.title()

        for restaurant in Restaurant.restaurants:
            if restaurant._name == restaurant_name:
                review = Review_restaurant(client_name, rating)
                restaurant._review.append(review)
                return rating

        return False

    # Método próprio para listar as avaliações efetuadas por cada cliente, exibindo o nome do cliente e nota data
    def list_restaurant_reviews(restaurant_name):
        restaurant_name = restaurant_name.title()

        for restaurant in Restaurant.restaurants:
            if restaurant._name == restaurant_name:
                return restaurant._review

        return False

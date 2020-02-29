import random
class Movie:
    """
    La clase Movie es una abstracción de los objetos movie. Y está conformoda por los métodos título,
    rank, like y dislike. 
    """
    def __init__(self, titulo):
        self.rank = random.randint(0,10)
        self.titulo = titulo.title() # con la función title() se le asignan mayúsculas al inicio de cada palabra
        print("La película " + self.titulo + " fue puntuada con: " + str(self.rank) + " puntos por los críticos.")
    
    def get_rank(self):
        return(str(self.rank))

    def get_titulo(self):
        return(str(self.titulo))

    def get_like(self):
        if self.rank + 1 <= 10:
            self.rank = self.rank + 1
            print("La película " + self.titulo + " se le sumó un punto y ahora tiene: " + str(self.rank))
        elif self.rank == 10:
            print("la película " + self.titulo + " ya no se le suma porque tiene un DIEZ.")
    
    def get_dislike(self):
        if self.rank - 1 > 0:
            self.rank = self.rank - 1
            print("La película " + self.titulo + " se le quitó un punto y ahora tiene una calificación de: " + str(self.rank))
        else:
            self.rank == 0
            print("la película " + self.titulo + " ya no se le resta porque tiene un CERO de calificación.")

roma = Movie("roma")
green = Movie("green book")
b2f = Movie("volver al futuro")
jok = Movie("joker")
son = Movie("sonic")
par = Movie("parásitos")
jojo = Movie("jojo rabbit")
jum = Movie("jumanji")
aves = Movie("aves de presa")
mul = Movie("mulán")

movies = [roma, green, b2f, jok, son, par, jojo, jum, aves, mul]

for movies in movies:
    print("+-+-+-+-+-+")
    movies.get_like()
    movies.get_dislike()
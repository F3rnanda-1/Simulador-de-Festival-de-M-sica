class Artista:
    def __init__(self, nombre, genero, popularidad):
        self.nombre = nombre
        self.genero = genero
        self.popularidad = popularidad

    def presentarse(self):
        print(f"Hola, soy {self.nombre}, interpreto {self.genero} y mi popularidad es {self.popularidad}/100.")

    def actuar(self):
        print("El artista va a realizar su presentación...")

    def despedirse(self):
        print(f"{self.nombre}: Gracias por el apoyo. Nos vemos pronto.\n")


class Cantante(Artista):
    def __init__(self, nombre, genero, popularidad, cancion_mas_popular):
        super().__init__(nombre, genero, popularidad)
        self.cancion_mas_popular = cancion_mas_popular

    def actuar(self):
        print(f"{self.nombre} canta su éxito '{self.cancion_mas_popular}' con mucha energía.")

class DJ(Artista):
    def __init__(self, nombre, genero, popularidad, estilo):
        super().__init__(nombre, genero, popularidad)
        self.estilo = estilo

    def actuar(self):
        print(f"El DJ {self.nombre} mezcla temas de estilo {self.estilo}, haciendo emocionar a los fans.") 

class Banda(Artista):
    def __init__(self, nombre, genero, popularidad, integrantes):
        super().__init__(nombre, genero, popularidad)
        self.integrantes = integrantes

    def actuar(self):
        print(f"Uno de los {self.integrantes} integrantes de la banda de {self.nombre} toca un increíble solo de guitarra.")

def iniciar_festival(lista_artistas):
    print("\n ¡Comienza el Festival de Música! \n")
    for artista in lista_artistas:
        artista.presentarse()
        artista.actuar()
        artista.despedirse()
        print("Fin de la actuación\n")
    print("El festival ha terminado. Gracias por asistir")


if __name__ == "__main__":
    lista_artistas = []

    n = int(input("¿Cuántos artistas se presentarán en el festival? "))

    for i in range(n):
        print(f"\nArtista {i+1}")
        tipo = input("Tipo de artista (Cantante/DJ/Banda): ").strip().lower()
        nombre = input("Nombre: ")
        genero = input("Género musical: ")
        popularidad = int(input("Popularidad (1 a 100): "))

        if tipo == "cantante":
            cancion = input("Canción más popular: ")
            artista = Cantante(nombre, genero, popularidad, cancion)

        elif tipo == "dj":
            estilo = input("Estilo musical: ")
            artista = DJ(nombre, genero, popularidad, estilo)

        elif tipo == "banda":
            integrantes = int(input("Número de integrantes: "))
            artista = Banda(nombre, genero, popularidad, integrantes)

        else:
            print("Tipo no reconocido. Intenta otra vez.")
            continue

        lista_artistas.append(artista)

    iniciar_festival(lista_artistas)

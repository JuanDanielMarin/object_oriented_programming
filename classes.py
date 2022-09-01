class Perro:

    # Definimos los atributos
    def __init__(self, nombre, color, tamano):

        self.nombre = nombre
        self.color = color
        self.tamano = tamano

    # Definimos los métodos
    def dormir(self):
        print('Estoy durmiendo')

    def hablar(self):
        print(f'Hola, mi nombre es {self.nombre}. Tengo el pelo {self.color} y soy de tamaño {self.tamano}.')

    def dar_pata(self):
        print('Toma mi patita')

perro1 = Perro('Dalan', 'beige y blanco', 'mediano')
perro1.hablar()

perro2 = Perro('Melao', 'marron y negro', 'grande')
perro2.hablar()
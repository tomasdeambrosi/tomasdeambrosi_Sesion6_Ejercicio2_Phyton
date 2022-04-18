''' En este segundo ejercicio, tendréis que crear un programa que tenga una clase llamada Alumno que tenga 
como atributos su nombre y su nota. Deberéis de definir los métodos para inicializar sus atributos, 
imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no. '''

class Alumno:
    nombre = None
    nota = None
    

    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def aprobado(self):
        if self.nota >= 6:
            return 'El alumno ' + self.nombre + ', con nota ' + str(self.nota) + ', está aprobado.'
        else:
            return 'El alumno ' + self.nombre + ', con nota ' + str(self.nota) + ', está desaprobado.'

juan = Alumno('Juan', 9)
print(juan.aprobado())

maria = Alumno('María', 5)
print(maria.aprobado())
 
class Clientes(): 
    def __init__(self,nombre, edad, sexo, direccion , correoElectronico):
        self.nombre = nombre
        self.edad = edad 
        self.sexo = sexo
        self.direccion = direccion
        self.correoElectronico = correoElectronico

    def comprar_producto(self,comprarProducto): 
        return f"El cliente compró un/a {comprarProducto}"

    def devolver_producto(self, devolverProducto):
        return f"El cliente pide reembolso de {devolverProducto}"

    def valorar_servicio(self,valorarServicio): 
        return f"Mi valoración: {valorarServicio}"
    
    def __str__(self): 
        return f"Hola, mi nombre es {self.nombre} tengo {self.edad} años y soy un/a {self.sexo}. Como cliente puedo comprar y devolver un producto, ademas de valorar el servicio." 
    

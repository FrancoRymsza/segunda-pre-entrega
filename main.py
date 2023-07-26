from ClaseClientes import * 

#Creacion del objeto cliente 
juan = Clientes("juan", 23 , "varon", "ayacucho 2050", "juan@gmail.com")

#Imprimiendo atributos y metodos. 
print(juan)
print(juan.nombre, juan.edad, juan.sexo, juan.direccion, juan.correoElectronico)
print(juan.comprar_producto("Ipad"))
print(juan.devolver_producto("Ipad"))
print(juan.valorar_servicio("El servicio es muy bueno, pude devolver mi compra sin ningun problema"))
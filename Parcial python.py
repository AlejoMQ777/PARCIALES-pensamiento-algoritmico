def clasificar_triangulo(a, b, c):
    #verifico si es un triángulo válido usando la desigualdad triangular
    if a + b <= c or a + c <= b or b + c <= a:
        return "No es un triángulo"
    
    #clasifico los tipos de triangulo si cumple la primera regla
    if a == b == c:
        return "Equilátero"
    elif a == b or a == c or b == c:
        return "Isósceles"
    else:
        return "Escaleno"
    
    #solicito los números al usuario
a = int(input("Ingrese el primer lado del triángulo: "))
b = int(input("Ingrese el segundo lado del triángulo: "))
c = int(input("Ingrese el tercer lado del triángulo: "))

#nombro la función para dar el resultado de esta
resultado = clasificar_triangulo(a, b, c)
print("El triángulo es:", resultado)

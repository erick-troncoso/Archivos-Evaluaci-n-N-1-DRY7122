# Función que determina el tipo de ACL IPv4
def tipo_acl(numero_acl):
    if numero_acl >= 1 and numero_acl <= 99:
        return "ACL Estándar"
    elif numero_acl >= 100 and numero_acl <= 199:
        return "ACL Extendida"
    else:
        return "El número no corresponde a una lista de acceso"

# se le Solicita al usuario el número de ACL IPv4
try:
    numero_acl = int(input("Introduce el número de ACL IPv4: "))
    tipo = tipo_acl(numero_acl)
    print("El número", numero_acl, "corresponde a una", tipo)
except ValueError:
    print("Por favor, introduce un número válido.")

numero_acl = int(input('Ingrese el número de ACL IPv4: '))
if 1 <= numero_acl <= 99:
    print('El valor indicado corresponde a una ACL Estándar')
elif 1300 <= numero_acl <= 1999:
    print('El valor indicado corresponde a una ACL estándar')
elif 100 <= numero_acl <= 199:
    print('El valor indicado corresponde a una ACL Extendida')
elif 2000 <= numero_acl <= 2699:
    print('El valor indicado corresponde a una ACL Extendida')
else:
    print("El número no corresponde a una lista de acceso")
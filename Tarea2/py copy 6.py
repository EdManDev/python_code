print("\033c")
# print("este programa va determinar el importe a pagar por concepto de estacionamiento")

# hora = int(input("digite horas de a: "))
# precio_hora = float(input("digite precio por hora: "))
# ars = (hora * precio_hora) * 0.02
# afp = (hora * precio_hora) * 0.0304
# sb = hora * precio_hora
# resultado = sb - ars - afp
# print("el importe a pagar por el concepto de estacionamiento es: ", resultado)



print('de terminar el importe a pagar por el concepto de estaciones...')

valor_pagar = str(input('ingrese el valor a pagar:  '))
horas = float(input('ingrese la Hora: '))
fraccion_hora = int(25)

sub_total = horas*fraccion_hora

print('El sueldo a pagar de la hora expresado es '+valor_pagar+' que es: '+str(sub_total)+' DOP por h/mn')

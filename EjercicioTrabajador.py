Nombre = str(input("Ingrese el nombre del empleado"))
Salario = float(input("Ingrese el salario del empleado"))

#C1 Inicio
Horas_extras = float(input("Ingrese las horas extras trabajadas"))
valor_hora = (Salario*0.35) + Salario
Total_Hextras = Horas_extras*valor_hora

#C2 Extras
Horas_trabajadas = float(input("Ingrese las horas normales trabajadas"))
valor_pagado = Horas_trabajadas * valor_hora
neto_pagar = Total_Hextras + valor_pagado
total_horas_trabajadas = Horas_trabajadas + Horas_extras

#C3 pagos
print("El trabajador ", Nombre, "Realizo ", Horas_trabajadas, "horas normales, ", "y", Horas_extras, "horas extras, para un total de ", total_horas_trabajadas, "Horas")
print("El salario base del trabajador es: ", Salario, "y por las horas laborales realizadas su ingreso total es de: ", neto_pagar)

#C4 Fin
horas_trabajadas = 48
valor_hora = 5000

porcentaje_retencion = 0.125 

salario_bruto = horas_trabajadas * valor_hora
retencion = salario_bruto * porcentaje_retencion
salario_neto = salario_bruto - retencion

print(f"El salario bruto es: ${salario_bruto:.0f}\n"
      f"La retención en la fuente es: ${retencion:.0f}\n"
      f"El salario neto es: ${salario_neto:.0f}")
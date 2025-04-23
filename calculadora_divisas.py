g
def exchange_money(budget, exchange_rate):
    resultado = budget / exchange_rate
    return resultado


print("Cambio en Japón:")
print(exchange_money(300, 0.0075))  


print("Cambio en México:")
print(exchange_money(300, 0.059))  

print("Cambio en Alemania:")
print(exchange_money(300, 1.07))   

print("\nCalculadora interactiva:")
presupuesto = float(input("¿Cuánto dinero quieres cambiar (USD)? "))
tasa = float(input("¿Cuál es la tasa de cambio del país? "))

valor_convertido = exchange_money(presupuesto, tasa)
print("Tendrás en la moneda local:", valor_convertido)

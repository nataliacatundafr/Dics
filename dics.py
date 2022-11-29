#tabela de preços

#Cachorro quente	100	1,20
#Bauru simples	101	1,30
#Bauru com ovo	102	1,50
#Hambúrger	103	1,20
#Cheeseburguer	104	1,30
#Refrigerante	105	1,00
TOTAL=0 # inicializo a variavel TOTAL.

#Dicionario como tabela de preços
produtos={
"100":1.20,
"101":1.30,
"102":1.50,
"103":1.20,
"104":1.30,
"105":1.00
}


##pede numero da mesa
NumeroMesa = int(input("Qual a mesa? "))
continuar = "sim" #inicia o while com a variavel continuat que recebe "sim"

#laço
while continuar =="sim":
    codigo = input("Qual codigo? ")
    quantidade = int(input("Quantidade: "))
    codigoTransformado = int(codigo)
#condições possiveis para que ocorra erro ou acerto
    if quantidade > 0 and (codigoTransformado > 99) and (codigoTransformado < 106): #testar se quantidade correta e codigo correto
        continuar = input("Deseja continuar ? ""sim ou não" )
        TOTAL = TOTAL + (produtos.get(codigo)*quantidade)
    elif  quantidade < 0 and (codigoTransformado < 99) and (codigoTransformado > 106): #testar se quantidade errada e codigo errado
        continuar = "sim"
        print("Código incorreto!")
        print("Erro! Quantidade menor do que a aceita.")

    elif quantidade > 0 and (codigoTransformado < 99) or (codigoTransformado > 106): #testar se quantidade correta e codigo errado
        print("Código incorreto!")
        continuar="sim"
    else: # quantidade errada e codigo correto
        print("Erro! Quantidade menor do que a aceita.")
        continuar = "sim"



#Conta
print("*******************************************")
print("MESA: ", NumeroMesa)
print("                                           ")
print("*******************************************")
print("ITEM                                  VALOR")
print("*******************************************")
print("SUBTOTAL:                         R$", TOTAL)
print("COMISSÃO (10%)                   +R$", TOTAL*0.1)
print("TOTAL:                             R$", TOTAL*1.1)
print("*******************************************")
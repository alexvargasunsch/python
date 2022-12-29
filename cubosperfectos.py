def cubos(n):
    if n > 0:
      a = n
      b = n+1
      c= a*b
      d = c/2
      respuesta = d**2
      
    else:
        if n == 0:
            respuesta = 0
        else:

            respuesta = 1
    return respuesta

print (cubos(10))


def SumarDigitos(numero):
  if num==0:
    resultado = 0
  else:
    resultado = num % 10 + SumarDigitos(numero // 10)

  return resultado 

print(SumarDigitos(246))


def resta (n):
    if n == 0:
        respuesta = 0
    else:
        if n < 0:
            respuesta = 0
        else:
            respuesta = n-resta(n-1)
    return respuesta

print (resta(2))


def fibonnacci(n):
    if n==0 or n==1:
        rpt=1
    else:
        if n<0:
            rpt=0
        else:
            rpt=fibonnacci(n-1)+fibonnacci(n-2)
    return rpt
print("caso 1 : ",fibonnacci(6))
print("\n")
#caso 2
def fibonacci2(n):
    if n>1 :
        res=fibonnacci(n-1)+fibonnacci(n-2)
    else :
        if n==0 or n==1:
            res=1
    return res



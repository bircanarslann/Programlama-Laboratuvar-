# ----FIBONACCİ,FAKTORİYEL VE ÜS----

def fibo_loop(n):
  a,b=0,1
  if(n==0):
    return 0
  for i in range(n-1):
    a,b=b,a+b
  return b

def fibo_recursive(n):
  if(n<2):
    return n
  else:
    return fibo_recursive(n-1)+fibo_recursive(n-2)

for i in range(20):
  r_1,r_2=fibo_loop(i),fibo_recursive(i)
  print("fibo loop: ", r_1, end= " ")
  print("fibo recursive: ",r_2)

def factorial(n):
  s=1
  for i in range (1,n+1):
    s=s*i
  return s
factorial(1)

def factorial_r(n):
  if(n==1):
    return 1
  else:
    return n*factorial_r(n-1)

print(factorial(5))
print(factorial_r(4))

#recursive ve loop sayac çağırım sayısını bulmak için
recursive_sayac=0
loop_sayac=0

def power_recursive(m,n):
  global recursive_sayac
  recursive_sayac=recursive_sayac+1
  if(n==0):
    return 1
  elif (n==1):
    return m
  elif (n//2==0):
    return power(m*m, int(n/2))
  elif(n//2!=0):
    return power_recursive(m*m, int(n/2))*m
print(power_recursive(1,2))

def power_loop(m,n):
  global loop_sayac
  s=1
  for i in range (n):
    s=s*m
    loop_sayac=loop_sayac+1
  return s
print(power_loop(2,0))

m=4
for i in range(2,10):
  r_1,r_2=power_loop(m,i),power_recursive(m,i)
  print("power loop: ", r_1, end=" ")
  print("power recursive: ", r_2)

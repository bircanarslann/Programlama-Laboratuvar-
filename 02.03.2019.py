# ----VECTORLERDE TOPLAMA,ÇIKARMA, SKALER ÇARPMA----

v=[1,2,3]
w=[2,4,6]

print(w+v)

def my_vector_Addition(v,w):
  size=len(v)
  my_result=[]
  for i in range (size):
    my_result.append(0)
  for i in range (size):
    my_result[i]=v[i]+w[i]
  return my_result

a=[1,2,3,2,4,6]
b=[11,22,33,22,44,66]

print(my_vector_Addition(a,b))

def my_vector_Substraction(v,w):
  size=len(v)
  my_result=[]
  for i in range (size):
    my_result.append(0)
  for i in range (size):
    my_result[i]=v[i]-w[i]
  return my_result

print(my_vector_Substraction(a,b))

def my_vector_Scaler_Product(alpha,v):
  size=len(v)
  my_result=[]
  for i in range (size):
    my_result.append(0)
  for i in range (size):
    my_result[i]=v[i]*alpha
  return my_result

print(my_vector_Scaler_Product(5,a))

a=[1,2,3,2,4,6]
b=[11,22,33,22,44,66]
alpha=5
beta=10

c=my_vector_Scaler_Product(alpha,a)
d=my_vector_Scaler_Product(beta,b)
e=my_vector_Addition(c,d)
f=my_vector_Substraction(a,b)

print(c)
print(d)
print(e)
print(f)

def my_vectors_ınner_product(v,w):
  size=len(v)
  my_result=[]
  for i in range (size):
    my_result.append(0)
  for i in range (size):
    my_result[i]=v[i]*w[i]
  t=0
  for i in range (size):
    t+=my_result[i]
  return t

k=[1,2]
l=[3,5]

print(my_vectors_ınner_product(k,l))

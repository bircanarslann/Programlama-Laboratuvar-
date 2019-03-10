import random
n=10
my_array=[]

def generate_an_array(n):
  for i in range(n):
    s=random.randint(0,100)
    my_array.append(s)
  return my_array
print(my_array)

for i in range(len(my_array)-1,0,-1):
  for j in range(i):
    if(my_array[j]>my_array[j+1]):
      t=my_array[j]
      my_array[j]=my_array[j+1]
      my_array[j+1]=t
print(my_array)

def my_bubble_sort (my_array):
    for i in range(len(my_array)-1,0,-1):
      for j in range(i):
        #print(j,i)
        if(my_array[j]>my_array[j+1]):
          t=my_array[j]
          my_array[j]=my_array[j+1]
          my_array[j+1]=t

def my_search_c(array_2,item):
    found= False
    indis=-1
    step=0
    for i in range(len(array_2)):
        step=step+1
        if array_2[i]==item:
            found=True
            indis=i
            break
    return (found, indis,step)

my_array=[]
my_array=generate_an_array(10)

print(my_bubble_sort(my_array))
print(my_array)
print(my_search_c(my_array,68))

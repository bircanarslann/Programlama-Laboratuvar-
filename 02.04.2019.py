#Listede string değer arama

#Bir fonksiyona iki parametre aktariliyor (text, string)
"""a) String , text te var ise True, yok ise False donderen fonksiyon yaziniz
   b) Eger bu string bulunursa textin icersinde, bulundugu ilk konumu return eden fonksiyon yaziniz.
   c) Ikinci gonderilen parametre birinci parametrede n defa bulunuyorsa, bulundugu yerlerin baslangic indislerini liste
halinde geri donduren fonksiyon yaziniz."""

import random
def my_function_create(m,n):
    my_list=[]
    for i in range(m):
        my_list.append([])
        for j in range(n):
            s=random.randint(-2,2)
            #s=-1
            my_list[i].append(s)
    return my_list

def my_function_print(mylist):
    m=len(mylist)
    n=len(mylist[0])
    for i in range(m):
        for j in range(n):
            print(mylist[i][j],end=" ")
        print()

def my_function_convert_to_hash(mylist):
    my_dict={}
    m = len(mylist)
    n = len(mylist[0])
    for i in range(m):
        for j in range(n):
            my_dict[(i,j)]=mylist[i][j]
    return my_dict

def my_function_print_hash(myHashList):
    print(" ")
    for key in myHashList:
        print(myHashList[key],end=" ")

my_2d_array=my_function_create(3,2)
my_function_print(my_2d_array)
my_2d_hash=my_function_convert_to_hash(my_2d_array)
my_function_print_hash(my_2d_hash)


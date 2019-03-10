# ----SELECTION SORT----

def my_SearchSelection(my_array):
    swap_sayisi = 0 #Bul bubble ile karşılaştır
    for i in range(len(my_array)-1,0,-1):
        positionOfMax=0
        for location in range(1,i+1):#Kalanlar içinde arıyor
            #print("j: ",location,"i: "i, end="\n")
            if(my_array[location]>my_array[positionOfMax]):
                positionOfMax=location
        temp=my_array[location]
        my_array[location]=my_array[positionOfMax]
        my_array[positionOfMax]=temp
        swap_sayisi=swap_sayisi+1

    print("swap sayisi: ",swap_sayisi)
    return

my_arr=[21,12,13,44,25,2,7,16,14,35]
my_SearchSelection(my_arr)
print(my_arr)

# -----BINARY SORT----
def my_Binary_search(my_sorted_array,item):
    first=0
    last=len(my_sorted_array)-1
    found=False
    s=0
    while first<=last and not found:
        midpoint=(first+last)//2
        print("first - last : ", first, last)
        s=s+1
        if(my_sorted_array[midpoint]==item):
            found=True
        else:
            if(item<my_sorted_array[midpoint]):
                last=midpoint-1
            else:
                first=midpoint+1
    return found, midpoint, s #midpoint orta eleman

my_arr=[45,68,12,58,89,32,26]
print(my_Binary_search(my_arr,50)) #50 aranıyor
#Kaç stepte sonuca ulaşır s kısımları.

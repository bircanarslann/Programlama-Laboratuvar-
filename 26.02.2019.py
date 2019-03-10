# ----FREKANS----
# ....(Kendisine aktarılan bir listenin frekans tablosunu bulup tekrar eden bir fonksiyon yazınız)....

my_list=[2,3,2,5,8,2,4,3,3,2,8,5,2,4,4,4,4]
print(my_list)
#a=[2,3]
#b=(2,3)
#c={2:3}
#d=c.keys()
#for d in c.keys():
  #print(c[d])

"""a)Dictionary ve hash kullanarak oluşturma"""

def my_frekans_dict(list):
  frekans_dict={}
  for item in list:
    if(item in frekans_dict):
      frekans_dict[item]=frekans_dict[item]+1
    else:
      frekans_dict[item]=1
  return frekans_dict
print(my_frekans_dict(my_list))

"""b)Liste kullanarak oluşturma"""

def my_frekans_list(list_1):
  frekans_list=[]
  for i in range(len(list_1)):
    s=False
    for j in range(len(frekans_list)):
      if(list_1[i][0]==frekans_list[j][0]):
        frekans_list[j][1]=frekans_list[j][1]+1
        s=True
      else:
        frekans_list.append([list_1[i],1]) #indis[0]
        s=True
    if(s==False):
      frekans_list.append([list_1[i],1])
  return frekans_list

  my_list=[2,3,2,5,8,2,4,3,3,2,8,5,2,4,4,4,4]
  result_1=my_frekans_dict(my_list)
  result_2=my_frekans_list(my_list)
  print(result_1)
  print(result_2)

"""2x2lik matris de det(A) bulma"""
matrix_1=[[1,2],[3,4]]
matrix_2=[[1,2,3],[4,5,6],[7,8,9]]
"""print(matrix_1,matrix_2)
print(matrix_1[0]) #ilk elemanı verecek
print(matrix_1[0][0])"""

satir_sayisi=len(matrix_1)
sutun_sayisi=len(matrix_1[0])
print(satir_sayisi,sutun_sayisi)

def det_from_2_by_2(m_1):
s_1=m_1[0][0]*m_1[1][1]
s_2=m_1[0][1]*m_1[1][0]
s_3=s_1-s_2
return s_3

print(det_from_2_by_2(matrix_1))

def delete_row_col_from_matrix(m_1,m,n):
result=[]
size_1=(len(m_1))
size_2=(len(m_1[0]))
for i in range (size_1):
if(i==m):
continue
row_1=[]
for j in range(size_2):
if(j==n):
continue
row_1.append(m_1[i][j])
result.append(row_1)
return result

print(matrix_1)
m_2=delete_row_col_from_matrix(matrix_1,0,0)

"""3x3 lük matris de det(A) bulma"""
def det_from_3_by_3(m_1):
a_1=m_1[0][0]
a_2=delete_row_col_from_matrix(m_1,0,0)
a_3=det_from_2_by_2(a_2)
a_4=a_1*a_3

b_1=m_1[0][1]
b_2=delete_row_col_from_matrix(m_1,0,1)
b_3=det_from_2_by_2(b_2)
b_4=b_1*b_3

c_1=m_1[0][2]
c_2=delete_row_col_from_matrix(m_1,0,2)
c_3=det_from_2_by_2(c_2)
c_4=c_1*c_3

return a_4-b_4+c_4

print(matrix_2)
print(det_from_3_by_3(matrix_2))

"""4x4 lük matris de det(A) bulma"""
def det_from_4_by_4(m_1):
e_1=m_1[0][0]
e_2=delete_row_col_from_matrix(m_1,0,0)
e_3=det_from_3_by_3(e_2)
e_4=e_1*e_3

f_1=m_1[0][1]
f_2=delete_row_col_from_matrix(m_1,0,1)
f_3=det_from_3_by_3(f_2)
f_4=f_1*f_3

g_1=m_1[0][2]
g_2=delete_row_col_from_matrix(m_1,0,2)
g_3=det_from_3_by_3(g_2)
g_4=g_1*g_3

h_1=m_1[0][3]
h_2=delete_row_col_from_matrix(m_1,0,3)
h_3=det_from_3_by_3(h_2)
h_4=h_1*h_3

return e_4-f_4+g_4+h_4
matrix_4=[[1,0,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
print(det_from_4_by_4(matrix_4))

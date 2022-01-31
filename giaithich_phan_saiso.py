from  math import  *
import math
input = [1,1, 2,2, 4 ,4]
# input= [1,2,2,4,3,6]
def kiemtra_tamgiac(input):
    vecto_AB = [input[2] - input[0], input[3] - input[1]]
    vecto_BC = [input[4] - input[2], input[5] - input[3]]
    vecto_CA = [input[0] - input[4], input[1] - input[5]]
    """cần dùng round để chủ động làm tròn chứ ko để python tự làm tròn gay lỗi case [1,2,3,4,5,6]"""
    c= AB = round(math.sqrt((vecto_AB[0]) ** 2 + (vecto_AB[1]) ** 2), 4)
    a= BC = round(math.sqrt((vecto_BC[0]) ** 2 + (vecto_BC[1]) ** 2), 4)
    b= CA = round(math.sqrt((vecto_CA[0]) ** 2 + (vecto_CA[1]) ** 2), 4)
    AB = sqrt((vecto_AB[0]) ** 2 + (vecto_AB[1]) ** 2)
    BC = sqrt((vecto_BC[0]) ** 2 + (vecto_BC[1]) ** 2)
    CA = sqrt((vecto_CA[0]) ** 2 + (vecto_CA[1]) ** 2)
    print(AB,BC,CA)
    print(AB+BC)
    "+thêm .000000000000002 để bù phần làm tròn của python loại bỏ lỗi trong trường hợp case input = [ [1,1,2,2,4,4] """
    """nếu dùng round để xử lý input [ [1,1,2,2,4,4]  thì  sẽ phát sinh lỗi nếu input = [1,2,2,4,3,6] xem them tai giaithich_phan_saiso.py """
    if AB+BC>CA+0.000000000000002 and AB+CA>BC+0.000000000000002 and BC+CA > AB+0.000000000000002:
    # if AB + BC > CA and AB + CA > BC  and BC + CA > AB :
        return True # enough inputndition  is triangle
    else:
        return False
print(kiemtra_tamgiac(input))
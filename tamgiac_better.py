from  math import  *
inputtoado = input("Nhập tọa độ dạng list như sau [Ax, Ay, Bx, By, Cx, Cy] = ")
inputtoado = inputtoado.strip("[,]")
inputtoado = inputtoado.split(",")
input =[]
"""handle nếu input ko phải integer"""
"""update may moi 31.01.2022"""
try :
    for i in inputtoado:
        input.append(int(i))
except:
    print("Vui long nhap lai kieu du lieu phu hop")
    quit()
"""triangle or not?"""
def kiemtra_tamgiac(input):
    vecto_AB = [input[2] - input[0], input[3] - input[1]]
    vecto_BC = [input[4] - input[2], input[5] - input[3]]
    if vecto_AB[0]*vecto_BC[1] != vecto_AB[1]*vecto_BC[0]: #
        return True   # enough inputndition  is triangle
    else:
        return False  # not enough inputndition  is triangle
print(kiemtra_tamgiac(input))
"""canh & goc"""
if kiemtra_tamgiac(input) is True :
    def goccanh_tamgiac(input) :
        # initial vecto
        vecto_AB = [input[2] - input[0], input[3] - input[1]]
        vecto_BC = [input[4] - input[2], input[5] - input[3]]
        vecto_CA = [input[0] - input[4], input[1] - input[5]]
        vecto_AC = [input[4] - input[0], input[5] - input[1]]
        vecto_BA = [input[0] - input[2], input[1] - input[3]]
        vecto_CB = [input[2] - input[4], input[3] - input[5]]

        AB = sqrt((vecto_AB[0]) ** 2 + (vecto_AB[1]) ** 2)
        BC = sqrt((vecto_BC[0]) ** 2 + (vecto_BC[1]) ** 2)
        CA = sqrt((vecto_CA[0]) ** 2 + (vecto_CA[1]) ** 2)
        AC = sqrt((vecto_AC[0]) ** 2 + (vecto_AC[1]) ** 2)
        BA = sqrt((vecto_BA[0]) ** 2 + (vecto_BA[1]) ** 2)
        CB = sqrt((vecto_CB[0]) ** 2 + (vecto_CB[1]) ** 2)

        AB_r = round(AB, 2)
        BC_r = round(BC, 2)
        CA_r = round(CA, 2)

        cosAB_AC = (vecto_AB[0] * vecto_AC[0] + vecto_AB[1] * vecto_AC[1]) / (AB * AC)
        cosBC_BA = (vecto_BC[0] * vecto_BA[0] + vecto_BC[1] * vecto_BA[1]) / (BC * BA)
        cosCA_CB = (vecto_CA[0] * vecto_CB[0] + vecto_CA[1] * vecto_CB[1]) / (CA * CB)

        gocA = acos(cosAB_AC)
        gocB = acos(cosBC_BA)
        gocC = acos(cosCA_CB)
        # inputvert to degress
        gocA_r = round(degrees(gocA), 2)
        gocB_r = round(degrees(gocB), 2)
        gocC_r = round(degrees(gocC), 2)
        result = []
        for i in (AB_r, BC_r, CA_r, gocA_r, gocB_r, gocC_r):
            result.append(i)
        return result

    print(goccanh_tamgiac(input))
    """canh & goc"""
    def xet_tamgiac(input):
        AB,BC,CA,gocA,gocB,gocC = goccanh_tamgiac(input)
        if AB == CA and gocA ==(90):
           return "ABC la tam giac vuong can tai dinh A"
        elif BC == AB and gocB ==(90):
           return "ABC la tam giac vuong can tai dinh B"
        elif CA == BC and gocC ==(90):
           "ABC la tam giac vuong can tai dinh C"
        elif AB == BC == CA:
           return "ABC là tam giac deu"
        else:
            return "ABC la tam giac binh thuong"
    print(xet_tamgiac(input))

    def dientich_tamgiac(input):
        AB,BC,CA,gocA,gocB,gocC = goccanh_tamgiac(input)
        h = sin(radians(gocA))*CA
        return round(AB*h/2,2)
    print(dientich_tamgiac(input))

    def duongcao_tamgiac(input):
        AB,BC,CA = goccanh_tamgiac(input)[0:3]
        """Cong thuc heron ha = 2*sqrt(p*(p - a) * (p - b) * (p - c))/a"""
        p = (AB + BC + CA) / 2
        dcA = round(2 * sqrt(p * (p - AB) * (p - BC) * (p - CA)) / BC, 2)
        dcB = round(2 * sqrt(p * (p - AB) * (p - BC) * (p - CA)) / CA, 2)
        dcC = round(2 * sqrt(p * (p - AB) * (p - BC) * (p - CA)) / AB, 2)
        return [dcA,dcB,dcC]
    print(duongcao_tamgiac(input))

    def trungtuyen_tamgiac(input):
        """ct: ma = sqrt((2 * (b ** 2 + c ** 2) - a ** 2) / 4"""
        AB, BC, CA = goccanh_tamgiac(input)[0:3]
        ttA = round(sqrt((2 * (AB ** 2 + CA ** 2) - BC ** 2) / 4), 2)
        ttB = round(sqrt((2 * (AB ** 2 + BC ** 2) - CA ** 2) / 4), 2)
        ttC = round(sqrt((2 * (CA ** 2 + BC ** 2) - AB ** 2) / 4), 2)
        return [ttA,ttB,ttC]
    print(trungtuyen_tamgiac(input))

    def tam_tamgiac(input):
        trongtam_x = round((input[0]+input[2]+input[4])/3,2)
        trongtam_y = round((input[1]+input[3]+input[5])/3,2)
        """tìm giao 2 duong cao,AH vuong goc BC, BH vuong goc AC giai he phuong trinh"""
        """
         vecto_AH = [tructam_x-input[0],tructam_y-input[1]]
         vecto_BH = [tructam_x - input[2], tructam_y - input[3]]
         vecto_AH*vecto_BC = 0
         vecto_BC[0] * vecto_AH[0] + vecto_BC[1] * vecto_AH[1] =0
         veinputt_BH * veinputc_AC =0
         vecto_AC[0] * vecto_BH[0] + vecto_AC[0] * vecto_BH[1] = 0
    
         vecto_BC[0] * (tructam_x - input[0]) +   vecto_BC[1] *(tructam_y - input[1]) = 0
         vecto_AC[0] * (tructam_x - input[2]) +   vecto_AC[1] *(tructam_y - input[3]) =  0
         vecto_BC[0] * tructam_x + vecto_BC[1] *tructam_y = vecto_BC[0]*input[0] +vecto_BC[1]*input[1]
         vecto_AC[0] * tructam_x + vecto_AC[1] * tructam_y = vecto_AC[0] * input[2] + vecto_AC[1] * input[3]
         apply Cramer D = a1b2-a2b1 Dx= c1b2-c2b1)  Dy = a1c2-a2c1
        """
        vecto_AC = [input[4] - input[0], input[5] - input[1]]
        vecto_BC = [input[4] - input[2], input[5] - input[3]]
        a1 = vecto_BC[0]
        b1 = vecto_BC[1]
        c1 = vecto_BC[0]*input[0] +vecto_BC[1]*input[1]
        a2 = vecto_AC[0]
        b2 = vecto_AC[1]
        c2 = vecto_AC[0] * input[2] + vecto_AC[1] * input[3]
        D = a1*b2 - a2*b1
        Dx = c1*b2 - c2*b1
        Dy = a1*c2 - a2*c1
        tructam_x = round(Dx/D,2)
        tructam_y = round(Dy/D,2)
        return [trongtam_x, trongtam_y,tructam_x,tructam_y]
    print(tam_tamgiac(input))

def giaima_tamgiac(input):
    if kiemtra_tamgiac(input) is False:
        print("A, B, C khong hop thanh mot tam giac")
    else :
        print("A, B, C hop thanh mot tam giac")
        print("1. So do co ban cua tam giac:")
        print("Chieu dai canh AB:", goccanh_tamgiac(input)[0])
        print("Chieu dai canh BC:", goccanh_tamgiac(input)[1])
        print("Chieu dai canh CA:", goccanh_tamgiac(input)[2])
        print("Goc A:", goccanh_tamgiac(input)[3])
        print("Goc B:", goccanh_tamgiac(input)[4])
        print("Goc C:", goccanh_tamgiac(input)[5])
        print(xet_tamgiac(input))
        print("2. Dien tich cua tam giac ABC: SABC",dientich_tamgiac(input))
        print("3. So do nang cao tam giac ABC:")
        print("Do dai duong cao tu dinh A:", duongcao_tamgiac(input)[0])
        print("Do dai duong cao tu dinh B:", duongcao_tamgiac(input)[1])
        print("Do dai duong cao tu dinh C:", duongcao_tamgiac(input)[2])
        print("Khoang cach den trong tam tu dinh A:", trungtuyen_tamgiac(input)[0])
        print("Khoang cach den trong tam tu dinh B:", trungtuyen_tamgiac(input)[1])
        print("Khoang cach den trong tam tu dinh C:", trungtuyen_tamgiac(input)[2])
        print("4. Toa do mot so diem dac biet cua tam giac ABC:")
        print("Toa do trong tam:", tam_tamgiac(input)[0:2])
        print("Toa do truc tam:", tam_tamgiac(input)[2:4])
giaima_tamgiac(input)

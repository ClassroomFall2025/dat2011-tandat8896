#tinh tien nuoc
import math
import datetime

history_menu= []

def tinh_tien_nuoc(so_nuoc: int) -> float:
    gia_ban_duoc= (7500, 8800, 12000, 20000)
    tien_nuoc= 0
    if so_nuoc <= 10:
        tien_nuoc= so_nuoc * gia_ban_duoc[0]
    elif so_nuoc <=20:
        tien_nuoc= 10 * gia_ban_duoc[0] + (so_nuoc - 10) * gia_ban_duoc[1]
    elif so_nuoc <= 30:
        tien_nuoc= 10 * gia_ban_duoc[0] + (so_nuoc - 10) * gia_ban_duoc[1] + (so_nuoc -20) * gia_ban_duoc[2]
    else:
        tien_nuoc= 10 * gia_ban_duoc[0] + (so_nuoc - 10) * gia_ban_duoc[1] + (so_nuoc -20) * gia_ban_duoc[2] + (so_nuoc -30) * gia_ban_duoc[3]
    return tien_nuoc
    

# tinh nguyen lieu lam banh
def tinh_nguyen_lieu_lam_banh(sl_bdx, sl_btc, sl_bd):
    banh_dau_xanh= {"duong":0.04, "dau": 0.07}
    banh_thap_cam= {"duong": 0.06, "dau": 0}
    banh_deo= {"duong":0.02, "dau": 0.02}
    nguyen_lieu= {}
    duong_hop_banh= sl_bdx * banh_dau_xanh["duong"] + sl_btc * banh_thap_cam["duong"] + sl_bd * banh_deo["duong"]
    dau_hop_banh= sl_bdx * banh_dau_xanh["dau"] + sl_btc * banh_thap_cam["dau"] + sl_bd * banh_deo["dau"]
    nguyen_lieu= {"duong": duong_hop_banh, "dau": dau_hop_banh}
    return nguyen_lieu


def filter_so_nguyen():
    my_list_so_nguyen_to = []
    input_lst= list(map(int, input("Nhap vao day so nguyen").split(',')))
    for i in range(len(input_lst)):
        if input_lst[i] % 2== 0:
            print(f"so nguyen to {input_lst[i]}")
            my_list_so_nguyen_to.append(input_lst[i])
    return my_list_so_nguyen_to


def filter_so_nguyen_1():
    input_lst= list(map(int, input("Nhap vao day so nguyen").split(',')))
    check_so_nguyen = lambda x: x % 2 == 0 
    filter_list = list(filter(check_so_nguyen, input_lst))
    print(f"Danh sach so chan: {filter_list}")  # Thêm dòng này để debug
    return filter_list



# def main():
#     nhap_so_nuoc= int(input("Nhap so nuoc: "))
#     tinh_tien_nuoc(nhap_so_nuoc)
#     nhap_so_banh= int(input("Nhap so banh: "))
#     nhap_so_btc= int(input("Nhap so btc: "))
#     nhap_so_bd= int(input("Nhap so bd: "))
#     tinh_nguyen_lieu_lam_banh(nhap_so_banh, nhap_so_btc, nhap_so_bd)


def addition(a, b):
    return a + b

def substract(a, b):
    return a-b

def multiply(a, b):
    return a*b

def divide(a, b):
    if b==0:
        print("Không thể chia cho 0")
    else:
        return a/b

def exponential_a_b(a, b):
    return a**b

def sqrt(a):
    if a<0:
        print("Không thể lấy căn bậc hai của số âm")
    else:
        return math.sqrt(a)

def sin(a):
    radius= math.radians(a)
    return math.sin(radius)
    

def cos(a):
    radius= math.radians(a)
    return math.cos(radius)

def tan(a):
    radius= math.radians(a)
    return math.tan(radius)

def log10(a):
    return math.log10(a)


def log_a_b(a, b):
    return math.log(a, b)

def solve_linear_equation(a, b):
    if a==0:
        if b==0:
            return "Phương trình có vô số nghiệm"
        else:
            return "Phương trình vô nghiệm"
    else:
        return -b/a

def solve_quadratic_equation(a, b, c):
    delta = b**2 - 4*a*c


    if a==0:
        if b==0:
            if c==0:
                print("Phương trình có vô số nghiệm")
        else:
            x=-c/b
            print(f"Phương trình có nghiệm x = {x}")

    else:
        if delta<0:
            print("Phương trình vô nghiệm")
        elif delta==0:
            x=-b/(2*a)
            print(f"Phương trình có nghiệm kép x = {x}")
        else:
            x1=(-b+math.sqrt(delta))/(2*a)
            x2=(-b-math.sqrt(delta))/(2*a)
            print(f"Phương trình có 2 nghiệm phân biệt: x1 = {x1}, x2 = {x2}")



def history(history_menu):
    print("===== LỊCH SỬ TÍNH TOÁN =====")
    if len(history_menu) == 0:
        print("Chưa có phép tính nào.")
    else:
        for i, item in enumerate(history_menu, 1):
            print(f"{i}. {item}")




def may_tinh():
    print("=" * 30)
    
    while True:
        print("\n MENU:")
        print("1  Phép tính 2 số: + - x ÷ ^")
        print("2  Phép tính 1 số: √ sin cos tan log")
        print("3  Giải phương trình")
        print("4  Xem lịch sử")
        print("5  Xem thời gian")
        print("0  Thoát")
        print("=" * 30)
        
        try:
            chon = int(input("Chọn: "))
            
            if chon == 0:
                print(" Thoat Chuong trinh!")
                break
            elif chon == 1:
                print("\n PHÉP TÍNH 2 SỐ:")
                print("1: +  2: -  3: x  4: ÷  5: ^")
                phep = int(input("Chọn phép: "))
                a = float(input("Số 1: "))
                b = float(input("Số 2: "))
                
                if phep == 1:
                    kq = addition(a, b)
                    print(f" {a} + {b} = {kq}")
                    history_menu.append(f"{a} + {b} = {kq}")
                elif phep == 2:
                    kq = substract(a, b)
                    print(f" {a} - {b} = {kq}")
                    history_menu.append(f"{a} - {b} = {kq}")
                elif phep == 3:
                    kq = multiply(a, b)
                    print(f" {a} x {b} = {kq}")
                    history_menu.append(f"{a} x {b} = {kq}")
                elif phep == 4:
                    kq = divide(a, b)
                    if kq is not None:
                        print(f" {a} ÷ {b} = {kq}")
                        history_menu.append(f"{a} ÷ {b} = {kq}")
                elif phep == 5:
                    kq = exponential_a_b(a, b)
                    print(f" {a}^{b} = {kq}")
                    history_menu.append(f"{a}^{b} = {kq}")
                else:
                    print(" Phép tính không hợp lệ!")
                    
            elif chon == 2:
                print("\n PHÉP TÍNH 1 SỐ:")
                print("1: sqrt : sin  3: cos  4: tan  5: log")
                phep = int(input("Chọn phép: "))
                a = float(input("Nhập số: "))
                
                if phep == 1:
                    kq = sqrt(a)
                    if kq is not None:
                        print(f" căn {a} = {kq}")
                        history_menu.append(f"sqrt{a} = {kq}")
                elif phep == 2:
                    kq = sin(a)
                    print(f" sin({a}°) = {kq}")
                    history_menu.append(f"sin({a}) = {kq}")
                elif phep == 3:
                    kq = cos(a)
                    print(f" cos({a}°) = {kq}")
                    history_menu.append(f"cos({a}) = {kq}")
                elif phep == 4:
                    kq = tan(a)
                    print(f" tan({a}°) = {kq}")
                    history_menu.append(f"tan({a}) = {kq}")
                elif phep == 5:
                    kq = log10(a)
                    print(f" log({a}) = {kq}")
                    history_menu.append(f"log({a}) = {kq}")
                else:
                    print(" Phép tính không hợp lệ!")
                    
            elif chon == 3:
                print("\n GIẢI PHƯƠNG TRÌNH:")
                print("1: Bậc 1 (ax + b = 0)")
                print("2: Bậc 2 (ax^2 + bx + c = 0)")
                bac = int(input("Chọn bậc: "))
                
                if bac == 1:
                    a = float(input("Hệ số a: "))
                    b = float(input("Hệ số b: "))
                    kq = solve_linear_equation(a, b)
                    print(f" Kết quả: {kq}")
                    history_menu.append(f"PT bậc 1: {kq}")
                        
                elif bac == 2:
                    a = float(input("Hệ số a: "))
                    b = float(input("Hệ số b: "))
                    c = float(input("Hệ số c: "))
                    kq = solve_quadratic_equation(a, b, c)
                    if kq is not None:
                        print(f" Kết quả: {kq}")
                        history_menu.append(f"PT bậc 2: {kq}")
                else:
                    print(" Bậc không hợp lệ!")
                    
            elif chon == 4:
                history(history_menu)

                
            elif chon == 5:
                thoi_gian = now()
                print(f" Thời gian hiện tại: {datetime.datetime.now()}")
                
            else:
                print(" Lựa chọn không hợp lệ!")
                
        except ValueError:
            print(" Vui lòng nhập số!")






def now():
    return datetime.datetime.now()






if __name__ == "__main__":
    main()
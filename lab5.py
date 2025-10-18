import math
import datetime
class SanPham_Bai1:
    def __init__(self, ten_san_pham="", don_gia=0, giam_gia=0):
        self.__ten_san_pham = ten_san_pham
        self.__don_gia = don_gia
        self.giam_gia = giam_gia

    def thue_thu_nhap(self, thue_thu_nhap=0.1):
        return self.gia * thue_thu_nhap

    def nhap_thong_tin(self):
        self.ten_san_pham = input("Nhap ten san pham: ")
        self.gia= float(input("Nhap gia san pham: "))
        self.__giam_gia= float(input("Nhap giam gia san pham: "))

    def nhap_thong_tin_san_pham(self):
        self.ten_san_pham = input("Nhap ten san pham: ")
        self.gia= float(input("Nhap gia san pham: "))
        self.__giam_gia= float(input("Nhap giam gia san pham: "))

    def xuat_thong_tin(self):
        return f"Ten san pham: {self.ten_san_pham}, Gia san pham: {self.gia}, Giam gia san pham: {self.__giam_gia}, thue thu nhap: {self.thue_thu_nhap()}"
    
    def __str__(self):
        return f"Ten san pham: {self.ten_san_pham}, Gia san pham: {self.gia}, Giam gia san pham: {self.__giam_gia}, thue thu nhap: {self.thue_thu_nhap()}"





class SanPham_Bai2:
    def __init__(self, ten_san_pham="", don_gia=0, giam_gia=0):
        self.__ten_san_pham = ten_san_pham
        self.__don_gia = don_gia
        self.giam_gia = giam_gia

    def set_ten_san_pham(self):
        self.__ten_san_pham = input("Nhap ten san pham: ")
    
    def set_gia(self):
        self.__don_gia = float(input("Nhap gia san pham: "))
    
    def get_ten_san_pham(self):
        return self.__ten_san_pham
    
    def get_gia(self):
        return self.__don_gia

    def xuat_thong_tin(self):
        return f"{self.__ten_san_pham} {self.__don_gia} {self.giam_gia}"


class SanPham_Bai3:
    def __init__(self):
        self.__ten= ""
        self.__gia= 0
        self.__giam_gia= 0


    def tinh_thue_nhap_khau(self, muc_thue:float=0.1) -> float:
        self.muc_thue= muc_thue
        return self.__gia * self.muc_thue / 100

    def setter(self):
        self.__ten= input("Nhap ten san pham: ")
        self.__gia= float(input("Nhap gia san pham: "))
        self.__giam_gia= float(input("Nhap giam gia san pham: "))

    def getter(self):
        return self.__ten, self.__gia, self.__giam_gia

    def xuat_thong_tin(self) -> str:
        san_pham= self.getter()
        return san_pham





class SanPham_Bai4:
    def __init__(self):
        self.__ten= ""
        self.__gia= 0
        self.__giam_gia= 0


    def tinh_thue_nhap_khau(self, muc_thue:float=0.1) -> float:
        self.muc_thue= muc_thue
        return self.__gia * self.muc_thue / 100

    def setter(self):
        self.__ten= input("Nhap ten san pham: ")
        self.__gia= float(input("Nhap gia san pham: "))
        self.__giam_gia= float(input("Nhap giam gia san pham: "))

    def getter(self):
        return self.__ten, self.__gia, self.__giam_gia

    def xuat_thong_tin(self) -> str:
        san_pham= self.getter()
        return san_pham


class SinhVien:
    def __init__(self, ten="", nam_sinh="", truong_hoc=""):
        self.__ten = ten
        self.__nam_sinh = nam_sinh
        self.__truong_hoc = truong_hoc
    
    def set_ten(self, ten):
        self.__ten = ten
    
    def set_nam_sinh(self, nam_sinh):
        self.__nam_sinh = nam_sinh
    
    def set_truong_hoc(self, truong_hoc):
        self.__truong_hoc = truong_hoc
    
    def get_ten(self):
        return self.__ten
    
    def get_nam_sinh(self):
        return self.__nam_sinh
    
    def get_truong_hoc(self):
        return self.__truong_hoc
    
    def xuat_thong_tin(self):
        return f"{self.get_ten()} {self.get_nam_sinh()} {self.get_truong_hoc()}"
    
    def xuat_thong_tin_sau_khi_set_lai(self):
        return f"{self.get_ten()} {self.get_nam_sinh()} {self.get_truong_hoc()}"
    


class MayTinhBoTui:
    def __init__(self):
        self.history = []
    
    def cong(self, a, b):
        return a + b
    
    def tru(self, a, b):
        return a - b
    
    def nhan(self, a, b):
        return a * b
    
    def chia(self, a, b):
        if b == 0:
            print("Không thể chia cho 0")
            return None
        return a / b
    
    def mu(self, a, b):
        return a ** b
    
    def can_bac_hai(self, a):
        if a < 0:
            print("Không thể lấy căn bậc hai của số âm")
            return None
        return math.sqrt(a)
    
    def sin(self, a):
        return math.sin(math.radians(a))
    
    def cos(self, a):
        return math.cos(math.radians(a))
    
    def tan(self, a):
        return math.tan(math.radians(a))
    
    def log(self, a):
        return math.log10(a)
    
    def xem_lich_su(self):
        if not self.history:
            print("Lịch sử trống!")
        else:
            print("\n=== LỊCH SỬ TÍNH TOÁN ===")
            for i, item in enumerate(self.history, 1):
                print(f"{i}. {item}")
    
    def xem_thoi_gian(self):
        print(f"Thời gian hiện tại: {datetime.datetime.now()}")
    
    def menu(self):
        print("=" * 30)
        print(" MENU:")
        print("1  Phép tính 2 số: + - x ÷ ^")
        print("2  Phép tính 1 số: sqrt sin cos tan log")
        print("3  Xem lịch sử")
        print("4  Xem thời gian")
        print("0  Thoát")
        print("=" * 30)
        
        while True:
            chon = input("Chọn: ")
            
            if chon == "0":
                print("Thoát chương trình!")
                break
            elif chon == "1":
                print("\n PHÉP TÍNH 2 SỐ:")
                print("1: +  2: -  3: x  4: ÷  5: ^")
                phep = input("Chọn phép: ")
                a = float(input("Số 1: "))
                b = float(input("Số 2: "))
                
                if phep == "1":
                    kq = self.cong(a, b)
                    print(f" {a} + {b} = {kq}")
                    self.history.append(f"{a} + {b} = {kq}")
                elif phep == "2":
                    kq = self.tru(a, b)
                    print(f" {a} - {b} = {kq}")
                    self.history.append(f"{a} - {b} = {kq}")
                elif phep == "3":
                    kq = self.nhan(a, b)
                    print(f" {a} x {b} = {kq}")
                    self.history.append(f"{a} x {b} = {kq}")
                elif phep == "4":
                    kq = self.chia(a, b)
                    if kq is not None:
                        print(f" {a} ÷ {b} = {kq}")
                        self.history.append(f"{a} ÷ {b} = {kq}")
                elif phep == "5":
                    kq = self.mu(a, b)
                    print(f" {a}^{b} = {kq}")
                    self.history.append(f"{a}^{b} = {kq}")
                else:
                    print(" Phép tính không hợp lệ!")
                    
            elif chon == "2":
                print("\n PHÉP TÍNH 1 SỐ:")
                print("1: sqrt  2: sin  3: cos  4: tan  5: log")
                phep = input("Chọn phép: ")
                a = float(input("Nhập số: "))
                
                if phep == "1":
                    kq = self.can_bac_hai(a)
                    if kq is not None:
                        print(f" căn {a} = {kq}")
                        self.history.append(f"sqrt{a} = {kq}")
                elif phep == "2":
                    kq = self.sin(a)
                    print(f" sin({a}°) = {kq}")
                    self.history.append(f"sin({a}) = {kq}")
                elif phep == "3":
                    kq = self.cos(a)
                    print(f" cos({a}°) = {kq}")
                    self.history.append(f"cos({a}) = {kq}")
                elif phep == "4":
                    kq = self.tan(a)
                    print(f" tan({a}°) = {kq}")
                    self.history.append(f"tan({a}) = {kq}")
                elif phep == "5":
                    kq = self.log(a)
                    print(f" log({a}) = {kq}")
                    self.history.append(f"log({a}) = {kq}")
                else:
                    print(" Phép tính không hợp lệ!")
                    
            elif chon == "3":
                self.xem_lich_su()
                
            elif chon == "4":
                self.xem_thoi_gian()
                
            else:
                print(" Lựa chọn không hợp lệ!")
    
    
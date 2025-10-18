class HinhChuNhat():
    def __init__(self, chieu_dai=0, chieu_rong=0):
        self.__chieu_dai = chieu_dai
        self.__chieu_rong = chieu_rong
    
    def set_chieu_dai(self, chieu_dai):
        self.__chieu_dai = chieu_dai
    
    def set_chieu_rong(self, chieu_rong):
        self.__chieu_rong = chieu_rong
    
    def get_chieu_dai(self):
        return self.__chieu_dai
    
    def get_chieu_rong(self):
        return self.__chieu_rong

    
    def tinh_chu_vi(self):
        return (self.get_chieu_dai() + self.get_chieu_rong()) * 2
    
    def tinh_dien_tich(self):
        return self.get_chieu_dai() * self.get_chieu_rong()
    
    def xuat_thong_tin(self):
        return f"Chieu dai la {self.get_chieu_dai()}, chieu rong la {self.get_chieu_rong()}, chu vi la {self.tinh_chu_vi()}, dien tich la {self.tinh_dien_tich()}"



class HinhVuong(HinhChuNhat):
    def __init__(self, canh=0):
        self.__canh = canh
        super().__init__(canh, canh)
    
    def set_canh(self, canh):
        self.__canh = canh
    
    def get_canh(self):
        return self.__canh

    def tinh_chu_vi(self):
        return self.get_canh() * 4
    
    def tinh_dien_tich(self):
        return self.get_canh() * self.get_canh()
    
    def xuat_thong_tin(self):
        return f"Canh la {self.get_canh()}, chu vi la {self.tinh_chu_vi()}, dien tich la {self.tinh_dien_tich()}"



class SinhVienPoly:
    def __init__(self,
                 ten="",
                 nghanh=""):
        self.__ten = ten
        self.__nghanh = nghanh

    def set_ten(self):
        self.__ten = input("Nhap ten sinh vien: ")

    def get_ten(self):
        return self.__ten

    def set_nghanh(self):
        self.__nghanh = input("Nhap nghanh sinh vien: ")

    def get_nghanh(self):
        return self.__nghanh

    def set_diem(self):
        self.diem = float(input("Nhap diem sinh vien: "))

    def get_diem(self):
        return self.diem

    def get_hoc_luc(self):
        if self.diem >= 9:
            return "Xuat Xac"
        elif self.diem >= 8 and self.diem < 9:
            return "Gioi"
        elif self.diem >= 7 and self.diem < 8:
            return "Kha"
        elif self.diem >= 5 and self.diem < 7:
            return "Trung Binh"
        else:
            return "Yeu"

    def xuat_thong_tin(self):
        return f"Ten sinh vien: {self.get_ten()}, Nghanh sinh vien: {self.get_nghanh()}, Diem sinh vien: {self.get_diem()}, Hoc luc sinh vien: {self.get_hoc_luc()}"

    def __str__(self):
        return f"Ten sinh vien: {self.get_ten()}, Nghanh sinh vien: {self.get_nghanh()}, Diem sinh vien: {self.get_diem()}, Hoc luc sinh vien: {self.get_hoc_luc()}"

# sv1 = SinhVienPoly()
# sv1.set_ten()
# sv1.set_nghanh()
# sv1.xuat_thong_tin()


class SinhVienIT(SinhVienPoly):
    def __init__(self, ten_sinh_vien="", nghanh_hoc="", java=0, html=0, css=0):
        super().__init__(ten_sinh_vien, nghanh_hoc)
        self.java = java
        self.html = html
        self.css = css
    
    def set_java(self):
        self.java = float(input("Nhap diem java: "))
    
    def get_java(self):
        return self.java
    
    def set_html(self):
        self.html = float(input("Nhap diem html: "))
    
    def get_html(self):
        return self.html
    
    def set_css(self):
        self.css = float(input("Nhap diem css: "))
    
    def get_css(self):
        return self.css

    def get_diem(self):
        return self.java*2 + self.html*2 + self.css*1


    def get_hoc_luc(self):
        return self.get_diem()
    
    def xuat_thong_tin(self):
        diem= {
            "ten": self.get_ten(),
            "nghanh": self.get_nghanh(),
            "diem": self.get_diem(),
            "java": self.get_java(),
            "html": self.get_html(),
            "css": self.get_css(),
            "diem": self.get_diem(),
            "hoc_luc": self.get_hoc_luc(),
        }
        print(diem)
        return diem




class SinhVienBiz(SinhVienPoly):
    def __init__(self, ten_sinh_vien="", nghanh_hoc="", marketing=0, sales=0):
        super().__init__(ten_sinh_vien, nghanh_hoc)
        self.marketing = marketing
        self.sales = sales
    
    def set_marketing(self):
        self.marketing = float(input("Nhap diem marketing: "))
    
    def get_marketing(self):
        return self.marketing
    
    def set_sales(self):
        self.sales = float(input("Nhap diem sales: "))
    
    def get_sales(self):
        return self.sales
    
    def get_diem(self):
        return self.marketing*2 + self.sales*3
    
    def get_hoc_luc(self):
        diem = self.get_diem()
        if diem >= 9:
            return "Xuat Xac"
        elif diem >= 8 and diem < 9:
            return "Gioi"
        elif diem >= 7 and diem < 8:
            return "Kha"
        elif diem >= 5 and diem < 7:
            return "Trung Binh"
        else:
            return "Yeu"
    
    def xuat_thong_tin(self):
        diem= {
            "ten": self.get_ten(),
            "nghanh": self.get_nghanh(),
            "marketing": self.get_marketing(),
            "sales": self.get_sales(),
            "diem": self.get_diem(),
            "hoc_luc": self.get_hoc_luc()
        }
        print(diem)
        return diem

class Quanlysinhvien:
    def __init__(self):
        self.sinhvien = []
    
    def them_sinhvien(self, sinhvien):
        self.sinhvien.append(sinhvien)
    
    def xuat_sinhvien(self):
        if not self.sinhvien:
            print("Danh sach sinh vien trống!")
            return
        print("\n=== DANH SACH SINH VIEN ===")
        for i, sv in enumerate(self.sinhvien, 1):
            print(f"{i}. {sv}")
    
    def xuat_sinhvien_gioi(self):
        if not self.sinhvien:
            print("Danh sach sinh vien trong!")
            return
        print("\n=== DANH SACH SINH VIEN GIOI ===")
        count = 0
        for sv in self.sinhvien:
            if sv.get_hoc_luc() == "Gioi":
                print(f"- {sv}")
                count += 1
        if count == 0:
            print("Khong co sinh vien nao co hoc luc Gioi!")
    
    def sap_xep_theo_diem(self):
        if not self.sinhvien:
            print("Danh sach sinh vien trong!")
            return
        self.sinhvien.sort(key=lambda x: x.get_diem(), reverse=True)
        print("\n=== DANH SACH SINH VIEN SAU KHI SAP XEP ===")
        for i, sv in enumerate(self.sinhvien, 1):
            print(f"{i}. {sv}")
    
    def nhap_sinhvien(self):
        print("\n=== NHAP THONG TIN SINH VIEN ===")
        print("Chon loai sinh vien:")
        print("1. Sinh vien Poly")
        print("2. Sinh vien IT")
        print("3. Sinh vien Biz")
        
        choice = input("Nhap lua chon (1-3): ")
        
        if choice == "1":
            sv = SinhVienPoly()
            sv.set_ten()
            sv.set_nghanh()
            sv.set_diem()
            self.them_sinhvien(sv)
            print("Da them sinh vien Poly thanh cong!")
            
        elif choice == "2":
            sv = SinhVienIT()
            sv.set_ten()
            sv.set_nghanh()
            sv.set_java()
            sv.set_html()
            sv.set_css()
            self.them_sinhvien(sv)
            print("Da them sinh vien IT thanh cong!")
            
        elif choice == "3":
            sv = SinhVienBiz()
            sv.set_ten()
            sv.set_nghanh()
            sv.set_marketing()
            sv.set_sales()
            self.them_sinhvien(sv)
            print("Da them sinh vien Biz thanh cong!")
        else:
            print("Lua chon khong hop le!")
    
    def menu(self):
        print("\n" + "="*50)
        print("1. Nhap danh sach sinh vien")
        print("2. Xuat thong tin danh sach sinh vien")
        print("3. Xuat danh sach sinh vien co hoc luc gioi")
        print("4. Sap xep danh sach sinh vien theo diem")
        print("5. Ket thuc")
        print("="*50)
        
        while True:
            choice = input("Nhap lua chon (1-5): ")
            
            if choice == "1":
                self.nhap_sinhvien()
            elif choice == "2":
                self.xuat_sinhvien()
            elif choice == "3":
                self.xuat_sinhvien_gioi()
            elif choice == "4":
                self.sap_xep_theo_diem()
            elif choice == "5":
                print("Cam on ban da su dung chuong trinh!")
                break
            else:
                print("Lua chon khong hop le! Vui long chon lai.")



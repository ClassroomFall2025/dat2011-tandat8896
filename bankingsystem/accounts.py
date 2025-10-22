import re
import csv
from typing import List, Dict
from simple_jwt import SimpleJWT
from customers import KhachHang

class TaiKhoan:
    __database = {}

    def __init__(self,
                ten_tai_khoan="",
                loai_tai_khoan=['T', 'P'],
                khach_hang: KhachHang = None):
        self.__so_tai_khoan = ""
        self.__ten_tai_khoan = ten_tai_khoan
        self.loai_tai_khoan = loai_tai_khoan
        self.__so_du = 0
        self.khach_hang = khach_hang

    def tao_tai_khoan(self):
        while True:
            so_tai_khoan = input("Nhap so tai khoan: ")
            ten_tai_khoan = input("Nhap ten tai khoan: ")
            loai_tai_khoan = input("Nhap loai tai khoan: ")
            
            # Nhập thông tin khách hàng từ class KhachHang
            self.khach_hang = KhachHang.nhap_thong_tin_khach_hang()
            
            if so_tai_khoan == "" or ten_tai_khoan == "" or loai_tai_khoan == "":
                print("Ten tai khoan và loai tai khoan không được để trống")
                continue
            
            elif len(so_tai_khoan) != 10 or not re.match(r"^[0-9]{10}$", so_tai_khoan):
                print("So tai khoan phai du 10 chu số & phai la so")
                continue
            elif loai_tai_khoan not in ['T', 'P']:
                print("Loai tài khoản không hợp lệ")
                continue
            elif so_tai_khoan in TaiKhoan.__database.keys():
                print("So tai khoan đã tồn tại")
                continue
            else:
                print("So tai khoan đã được tạo")
                # Thêm tài khoản vào danh sách của khách hàng
                self.khach_hang.them_tai_khoan(self)
                
                # Lưu vào database
                self.__so_tai_khoan = so_tai_khoan
                self.__ten_tai_khoan = ten_tai_khoan
                self.loai_tai_khoan = loai_tai_khoan
                TaiKhoan.__database[self.__so_tai_khoan] = {
                    "ten_tai_khoan": self.__ten_tai_khoan,
                    "loai_tai_khoan": self.loai_tai_khoan,
                    "so_du": self.__so_du,
                    "khach_hang": self.khach_hang
                }
                return so_tai_khoan


    def hien_thi_tai_khoan(self) -> list[dict]:
        """Hiển thị thông tin tài khoản với menu chọn mode"""
        print("\n=== CHON MODE ===")
        print("1. Admin (cần token)")
        print("2. User")
        print("3. Public")
        
        choice = input("Chọn mode (1/2/3): ")
        
        if choice == "1":
            token = input("Nhập token Admin: ")
            if not token:
                print("Cần nhập token Admin để xem tất cả tài khoản")
                return []
            elif not SimpleJWT.is_admin(token):
                print("Token Admin không hợp lệ hoặc đã hết hạn")
                return []
            else:
                print("\n=== TAT CA TAI KHOAN (ADMIN) ===")
                if not TaiKhoan.__database:
                    print("Chua co tai khoan nao")
                    return []
                for so_tai_khoan, thong_tin in TaiKhoan.__database.items():
                    print(f"STK: {so_tai_khoan} - Ten: {thong_tin['ten_tai_khoan']} - Loai: {thong_tin['loai_tai_khoan']} - So du: {thong_tin['so_du']}")
                    khach_hang = thong_tin['khach_hang']
                    khach_hang.hien_thi_tai_khoan()
                    
                    print("-" * 30)
                return []
        
        elif choice == "2":
            print("\n=== THONG TIN TAI KHOAN (USER) ===")
            stk_an = "***" + self.__so_tai_khoan[-4:]
            print(f"STK: {stk_an} - Ten: {self.__ten_tai_khoan} - Loai: {self.loai_tai_khoan} - So du: {self.__so_du}")
            if self.khach_hang:
                self.khach_hang.hien_thi_tai_khoan()
            return []
        
        elif choice == "3":  # Public
            print("\n=== THONG TIN TAI KHOAN (PUBLIC) ===")
            stk_an = "***" + self.__so_tai_khoan[-4:]
            print(f"STK: {stk_an} - Ten: {self.__ten_tai_khoan} - Loai: {self.loai_tai_khoan} - So du: {self.__so_du}")
            if self.khach_hang:
                self.khach_hang.hien_thi_tai_khoan()
            return []
        else:
            print("Lựa chọn không hợp lệ")
            return []

    def hien_thi_tat_ca_tai_khoan_khach_hang(self):
        """Hiển thị tất cả tài khoản của khách hàng"""
        if self.khach_hang:
            print(f"\n=== TAT CA TAI KHOAN CUA {self.khach_hang.ten.upper()} ===")
            self.khach_hang.hien_thi_tai_khoan()
        else:
            print("Khong co thong tin khach hang")

    def gui_tien(self, so_tien:float)-> bool:
        if so_tien > 0:
            self.__so_du += so_tien
            return True
        else:
            return False

    def rut_tien(self, so_tien:float)-> bool:
        if so_tien > self.__so_du:
            return False
        else:
            self.__so_du -= so_tien
            return True

    def kiem_tra_so_du(self)-> float:
        return self.__so_du
    
    def to_dict(self)-> dict:
        return {
            "so_tai_khoan": self.__so_tai_khoan,
            "ten_tai_khoan": self.__ten_tai_khoan,
            "loai_tai_khoan": self.loai_tai_khoan,
            "so_du": self.__so_du
        }
    
    # def __str__(self)-> str:
    #     return f"STK: {self.__so_tai_khoan} - Ten: {self.__ten_tai_khoan} - Loai: {self.loai_tai_khoan} - So du: {self.__so_du}"
    
    # def __repr__(self)-> str:
    #     return f"TaiKhoan({self.__so_tai_khoan}, {self.__ten_tai_khoan}, {self.loai_tai_khoan}, {self.__so_du})"


def docTaiKhoanTuCSV(filename="taikhoan.csv"):
    """Đọc dữ liệu tài khoản từ file CSV"""
    danh_sach_tai_khoan = []
    try:
        with open(filename, 'r', encoding='utf-8', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Tạo object TaiKhoan từ dữ liệu CSV
                tai_khoan = TaiKhoan()
                tai_khoan._TaiKhoan__so_tai_khoan = row['so_tai_khoan']
                tai_khoan._TaiKhoan__ten_tai_khoan = row['ten_tai_khoan']
                tai_khoan.loai_tai_khoan = row['loai_tai_khoan']
                tai_khoan._TaiKhoan__so_du = float(row['so_du'])
                
                # Tạo thông tin khách hàng nếu có
                if row.get('ten_khach_hang'):
                    khach_hang = KhachHang(
                        row['ten_khach_hang'],
                        row.get('sdt', ''),
                        row.get('email', ''),
                        row.get('dia_chi', '')
                    )
                    tai_khoan.khach_hang = khach_hang
                    khach_hang.them_tai_khoan(tai_khoan)
                
                danh_sach_tai_khoan.append(tai_khoan)
                # Thêm vào database
                TaiKhoan._TaiKhoan__database[tai_khoan._TaiKhoan__so_tai_khoan] = {
                    "ten_tai_khoan": tai_khoan._TaiKhoan__ten_tai_khoan,
                    "loai_tai_khoan": tai_khoan.loai_tai_khoan,
                    "so_du": tai_khoan._TaiKhoan__so_du,
                    "khach_hang": tai_khoan.khach_hang
                }
        
        print(f"Đã đọc thành công {len(danh_sach_tai_khoan)} tài khoản từ {filename}")
        return danh_sach_tai_khoan
        
    except FileNotFoundError:
        print(f"Không tìm thấy file {filename}")
        return []
    except Exception as e:
        print(f"Lỗi khi đọc file CSV: {e}")
        return []


def ghiTaiKhoanVaoCSV(danh_sach, filename="taikhoan.csv"):
    """Ghi danh sách tài khoản vào file CSV"""
    try:
        with open(filename, 'w', encoding='utf-8', newline='') as file:
            fieldnames = [
                'so_tai_khoan', 'ten_tai_khoan', 'loai_tai_khoan', 'so_du',
                'ten_khach_hang', 'sdt', 'email', 'dia_chi'
            ]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            
            for tai_khoan in danh_sach:
                row = {
                    'so_tai_khoan': tai_khoan._TaiKhoan__so_tai_khoan,
                    'ten_tai_khoan': tai_khoan._TaiKhoan__ten_tai_khoan,
                    'loai_tai_khoan': tai_khoan.loai_tai_khoan,
                    'so_du': tai_khoan._TaiKhoan__so_du,
                    'ten_khach_hang': tai_khoan.khach_hang.ten if tai_khoan.khach_hang else '',
                    'sdt': tai_khoan.khach_hang.sdt if tai_khoan.khach_hang else '',
                    'email': tai_khoan.khach_hang.email if tai_khoan.khach_hang else '',
                    'dia_chi': tai_khoan.khach_hang.dia_chi if tai_khoan.khach_hang else ''
                }
                writer.writerow(row)
        
        print(f"Đã ghi thành công {len(danh_sach)} tài khoản vào {filename}")
        return True
        
    except Exception as e:
        print(f"Lỗi khi ghi file CSV: {e}")
        return False

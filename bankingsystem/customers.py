class KhachHang:
    def __init__(self, ten, sdt, email, dia_chi):
        self.ten = ten
        self.sdt = sdt
        self.email = email
        self.dia_chi = dia_chi
        self.tai_khoan = []
    
    def them_tai_khoan(self, tai_khoan):
        self.tai_khoan.append(tai_khoan)
    
    @classmethod
    def nhap_thong_tin_khach_hang(cls):
        """Nhập thông tin khách hàng từ bàn phím với validation"""
        print("\n=== NHAP THONG TIN KHACH HANG ===")
        
        while True:
            try:
                ten = input("Nhap ten khach hang: ")
                if ten == "":
                    print("Ten khach hang khong duoc de trong")
                    continue
                break
            except KeyboardInterrupt:
                print("\nThoat chuong trinh")
                return None
            except Exception as e:
                print(f"Loi nhap ten: {e}")
                continue
        
        while True:
            try:
                sdt = input("Nhap SDT khach hang: ")
                if sdt == "":
                    print("SDT khong duoc de trong")
                    continue
                elif not sdt.isdigit() or len(sdt) != 10:
                    print("SDT phai co 10 chu so")
                    continue
                break
            except KeyboardInterrupt:
                print("\nThoat chuong trinh")
                return None
            except Exception as e:
                print(f"Loi nhap SDT: {e}")
                continue
        
        while True:
            try:
                email = input("Nhap email khach hang: ")
                if email == "":
                    print("Email khong duoc de trong")
                    continue
                elif "@" not in email or "." not in email:
                    print("Email khong hop le")
                    continue
                break
            except KeyboardInterrupt:
                print("\nThoat chuong trinh")
                return None
            except Exception as e:
                print(f"Loi nhap email: {e}")
                continue
        
        while True:
            try:
                dia_chi = input("Nhap dia chi khach hang: ")
                if dia_chi == "":
                    print("Dia chi khong duoc de trong")
                    continue
                break
            except KeyboardInterrupt:
                print("\nThoat chuong trinh")
                return None
            except Exception as e:
                print(f"Loi nhap dia chi: {e}")
                continue
        
        return cls(ten, sdt, email, dia_chi)
    
    def hien_thi_tai_khoan(self):
        if not self.tai_khoan:
            print("Khach hang chua co tai khoan nao")
            return
        
        print(f"Thong tin khach hang: {self.ten}")
        print(f"SDT: {self.sdt}")
        print(f"Email: {self.email}")
        print(f"Dia chi: {self.dia_chi}")
        print(f"So tai khoan cua khach hang: {len(self.tai_khoan)}")
        print("Danh sach tai khoan:")
        for i, tk in enumerate(self.tai_khoan, 1):
            print(f"{i}. So tai khoan: {tk._TaiKhoan__so_tai_khoan}")
            print(f"   Ten tai khoan: {tk._TaiKhoan__ten_tai_khoan}")
            print(f"   So du: {tk._TaiKhoan__so_du}")
            print(f"   Loai tai khoan: {tk.loai_tai_khoan}")

class NhanVien ():
    def __init__(self, ma_nv="", ten_nv="", luong_thang=0):
        self.ma_nv = ma_nv
        self.ten_nv = ten_nv
        self.luong_thang = luong_thang
    
    def set_ma_nv(self, ma_nv):
        self.ma_nv=ma_nv
    def nhap_thong_tin(self,ds_nhanvien):
        print("Nhập thông tin :")
        
        # while True:
        #     self.ma_nv = input("Nhập mã nv: ")
        #     if kiem_tra_trung_ma(self.ma_nv, ds_nhanvien):
        #         print("Mã nhân viên đã tồn tại, vui lòng nhập mã khác.")
        #         continue
        #     else:
        #         break   
        self.ten_nv = input("Nhập tên nhân viên: ")
        while True:
            try:
                self.luong_thang = int(input("Nhập lương tháng:"))
                break
            except ValueError:
                print("Vui lòng nhập đúng định dạng số")
        return self

    def tinh_thu_nhap(self):
        return self.luong_thang
    
    def tinh_thue_thu_nhap(self):
        if self.tinh_thu_nhap() < 9000000 :
            return 0
        elif self.tinh_thu_nhap() < 15000000 :
            return (self.tinh_thu_nhap()-9000000) * 0.1
        else:
            return (self.tinh_thu_nhap()-15000000) * 0.12 + 600000
        
    def xuat_thong_tin(self) -> str:
        return f"| {self.ma_nv:^10} | {self.ten_nv:^20} | {self.luong_thang:^15,} | "
    
    def thu_nhap_sau_thue(self):
        return self.tinh_thu_nhap()-self.tinh_thue_thu_nhap()
    
    def xuat_thong_tin_co_ban(self):
        return f"| {self.ma_nv:^10} | {self.ten_nv:^20} | {self.luong_thang:^15,}VND   |"
class NhanVienTiepThi(NhanVien):
    def __init__(self, ma_nv = "", ten_nv = "", luong_thang = 0,doanh_so = 0,ti_le_hoa_hong = 0):
        super().__init__(ma_nv, ten_nv, luong_thang)
        self.doanh_so = doanh_so
        self.ti_le_hoa_hong=ti_le_hoa_hong
    
    def nhap_thong_tin(self,ds_nhanvien):
        super().nhap_thong_tin(ds_nhanvien)
        while True:
            try:
                self.doanh_so=int(input("Nhập doanh số: "))
                break
            except ValueError:
                print("Vui lòng nhập đúng định dạng số")
        while True:
            try:
                self.ti_le_hoa_hong=float(input("Nhập tỉ lệ hoa hồng (%): "))/100
                break
            except ValueError:
                print("Vui lòng nhập đúng định dạng số!")
        return self
    
    def tinh_thu_nhap(self) -> float:
        return self.luong_thang + self.doanh_so*self.ti_le_hoa_hong
    def xuat_thong_tin(self) -> str:
        return f"| {self.ma_nv:^10} | {self.ten_nv:^20} | {self.luong_thang:^15,} | {self.doanh_so:^15} | {self.ti_le_hoa_hong:^15} | "
class TruongPhong(NhanVien):
    def __init__(self, ma_nv = "", ten_nv = "", luong_thang = 0,luong_trach_nhiem = 0):
        super().__init__(ma_nv, ten_nv, luong_thang)
        self.luong_trach_nhiem=luong_trach_nhiem
        
    def nhap_thong_tin(self,ds_nhanvien):
        super().nhap_thong_tin(ds_nhanvien)
        while True:
            try:
                self.luong_trach_nhiem = int(input("Nhập lương trách nhiệm: "))
                break
            except ValueError:
                print("Vui lòng nhập đúng định dạng số")
        return self
        
    def tinh_thu_nhap(self):
        return self.luong_thang + self.luong_trach_nhiem
    
    def xuat_thong_tin(self):
        return f"| {self.ma_nv:^10} | {self.ten_nv:^20} | {self.luong_thang:^15,} | {self.luong_trach_nhiem:^17} | "

 
def kiem_tra_trung_ma(ma_nv, danh_sach_nv):
#for list in dict (loai_nhan_vien là 1 list trong dict ds_nhanvien)
    for loai_nhan_vien in danh_sach_nv:
        if loai_nhan_vien.ma_nv == ma_nv:
                return True
    return False


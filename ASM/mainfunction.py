from class_manager import * 

ds_nhanvien ={
        "Hành chính" :[],
        "Tiếp thị" :[],
        "Trưởng phòng": [] 
    }
hanh_chinh = 0
tiep_thi = 0
truong_phong = 0

def nhap_ds_nv():
    print("Chọn Loại Nhân Viên Muốn Nhập")

    while True:
        print("\nChọn loại nhân viên:")
        print("1. Hành chính")
        print("2. Tiếp thị") 
        print("3. Trưởng phòng")
        print("0. Thoát")
        
        try:
            the_loai= int(input("Nhập Thể Loại Nhân Viên:"))
        except ValueError:
            print("Vui lòng nhập lại lựa chọn 1, 2, 3 để nhập danh sách nhân viên hoặc 0 để thoát")
            continue
        
        if the_loai == 1:
            global hanh_chinh
            nhap_nhan_vien = NhanVien().nhap_thong_tin(ds_nhanvien["Hành chính"])
            ma_nv="HC"+str(hanh_chinh+1)
            nhap_nhan_vien.set_ma_nv(ma_nv)
            hanh_chinh+=1
            ds_nhanvien["Hành chính"].append(nhap_nhan_vien)
            
        elif the_loai == 2:
            global tiep_thi
            nhap_nhan_vien_tiep_thi = NhanVienTiepThi().nhap_thong_tin(ds_nhanvien["Tiếp thị"])
            ds_nhanvien["Tiếp thị"].append(nhap_nhan_vien_tiep_thi)
            ma_nv="TT"+str(tiep_thi+1)
            nhap_nhan_vien_tiep_thi.set_ma_nv(ma_nv)
            tiep_thi+=1
            
        elif the_loai == 3:
            global truong_phong
            nhap_truong_phong = TruongPhong().nhap_thong_tin(ds_nhanvien["Trưởng phòng"])
            ds_nhanvien["Trưởng phòng"].append(nhap_truong_phong)
            ma_nv="TP"+str(truong_phong+1)
            nhap_truong_phong.set_ma_nv(ma_nv)
            truong_phong+=1
            
        elif the_loai ==0 :
            break
        else:
            print("Vui lòng nhập lại lựa chọn 1, 2, 3 để nhập danh sách nhân viên hoặc 0 để thoát")
    return ds_nhanvien

def ghi_file():
    dinh_dang_file=".txt"
    try:
        print("Đang ghi file...")
        with open(file= "danhsach_nhanvien"+ dinh_dang_file, mode="a", encoding= 'utf8') as file:            
            for loai,danh_sach in ds_nhanvien.items():
                file.write(f"\n Loại nhân viên: {loai}\n")
                if loai == "Hành chính":
                    file.write("="*55+"\n")
                    file.write(f"| {'Mã NV':^10} | {'Tên NV':^20} | {'Lương':^15} |\n")
                    file.write("-"*55+"\n")
                elif loai == "Tiếp thị":
                    file.write("="*91+"\n")
                    file.write(f"| {'Mã NV':^10} | {'Tên NV':^20} | {'Lương':^15} | {'Doanh số':^15} | {'Tỉ lệ hoa hồng':^15} |\n")
                    file.write("-"*91+"\n")
                elif loai == "Trưởng phòng":
                    file.write("="*75+"\n")
                    file.write(f"| {'Mã NV':^10} | {'Tên NV':^20} | {'Lương':^15} | {'Lương trách nhiệm':^17} |\n")
                    file.write("-"*75+"\n")
                for nv in danh_sach:
                    file.write(nv.xuat_thong_tin())   
                    file.write("\n") 
        print("Ghi file thành công!")
    except ValueError:
        print("Ghi file không thành công!")

def doc_file(file_name):
    try:
        with open(file= file_name, mode="r", encoding= 'utf8') as file:
            for line in file:
                print(line)
    except ValueError:
        print("Đọc file không thành công")

#Mới thêm cái này (xuất nhân viên theo loại ,truyên vào loại và danh sách theo loại đó để xuất ra theo định dạng tương ứng)
def xuat_ds_theo_loai(loai,danh_sach: list):
    if loai == "Hành chính" and len(danh_sach) != 0:
        print(f"\nLoại nhân viên: {loai}")
        print("="*55)
        print(f"| {'Mã NV':^10} | {'Tên NV':^20} | {'Lương':^15} |")
        print("-"*55)
        for nv in danh_sach:
            print(nv.xuat_thong_tin())
        print("="*55)
        
    elif loai == "Tiếp thị" and len(danh_sach) != 0:
        print(f"\nLoại nhân viên: {loai}")
        print("="*91)
        print(f"| {'Mã NV':^10} | {'Tên NV':^20} | {'Lương':^15} | {'Doanh số':^15} | {'Tỉ lệ hoa hồng':^15} |")
        print("-"*91)
        for nv in danh_sach:
            print(nv.xuat_thong_tin())
        print("="*91)
        
    elif loai == "Trưởng phòng" and len(danh_sach) != 0:
        print(f"\nLoại nhân viên: {loai}")
        print("="*75)
        print(f"| {'Mã NV':^10} | {'Tên NV':^20} | {'Lương':^15} | {'Lương trách nhiệm':^17} |")
        print("-"*75)
        for nv in danh_sach:
            print(nv.xuat_thong_tin())
        print("="*75)

    else :
        print("Loại nhân viên: ", loai)
        print("Không có nhân viên!")

#Mới thêm cái này (xuất nhân viên theo phòng ban có lựa chọn phòng ban muôn xuất)
def xuat_ds_theo_phong_ban(ds : dict):
    while True:
        while True:
            try:
                print("Chọn loại nhân viên cần xuất: ")
                print("1. Hành chính")
                print("2. Tiếp thị")
                print("3. Trưởng phòng")
                print("0. Quay lại menu chính")
                loai=int(input("Nhập lựa chọn của bạn (0-3): "))
                if loai in [0,1,2,3]:
                    break
                else:
                    print("Lựa chọn không hợp lệ, vui lòng nhập lại")
            except ValueError:
                print("Vui lòng nhập đúng định dạng số")
        match loai:
            case 1:
                xuat_ds_theo_loai("Hành chính",ds["Hành chính"])
            case 2:
                xuat_ds_theo_loai("Tiếp thị",ds["Tiếp thị"])
            case 3: 
                xuat_ds_theo_loai("Trưởng phòng",ds["Trưởng phòng"])
            case 0:
                break

# đã sửa cái này theo cái trên (xuất toàn bộ danh sách nhân viên theo loại)        
def xuat_ds(danh_sach_nhan_vien: dict  ):
    print("="* 30 ,"DANH SÁCH NHÂN VIÊN", "="*30)
    for loai,danh_sach in danh_sach_nhan_vien.items():
        xuat_ds_theo_loai(loai,danh_sach)
       
def tim_nv_theo_luong (ds_nhanvien :dict):
    tim_kiem_nv_theo_luong = []
    while True:
        try:
            min_sal = int(input("Nhập lương tối thiểu: "))
            break
        except ValueError:
            print("Mức lương nhập không hợp lệ, vui lòng nhập lại")

    while True:
        try:
            max_sal = int(input("Nhập lương tối đa: "))
            break
        except ValueError:
            print("Mức lương nhập không hợp lệ, vui lòng nhập lại")
            
    for loai_nv in ds_nhanvien.values():
        for employee in loai_nv:
            if min_sal <= employee.tinh_thu_nhap() <= max_sal:
                tim_kiem_nv_theo_luong.append(employee)
        else:
            print(f"Không tìm thấy nhân viên trong khoảng mức lương từ {min_sal:,} tới {max_sal:,}!")
    return tim_kiem_nv_theo_luong

def tim_nv_theo_ma():
    ma_nv = input("Nhập mã nhân viên: ")
    for loai, danh_sach in ds_nhanvien.items():
        for nv in danh_sach:
            if nv.ma_nv == ma_nv:
                return nv, loai
    return None,None

# đã sửa , isinstance là kiểm tra đối tượng thuộc cả lớp cha và lớp con nên phải kiểm tra theo thứ tự lớp con trước.    
def tim_kiem_nhan_vien():
    kq_tim_kiem = {
        "Hành chính": [],
        "Tiếp thị": [],
        "Trưởng phòng": []
    }
    print("*"*15+" TÌM KIẾM NHÂN VIÊN "+"*"*15)
    print("|    1. Tìm kiếm nhân viên theo mã               |")
    print("|    2. Tìm kiếm nhân viên theo khoảng lương     |")
    print("*"*50)
    print("Chọn phương thức tìm kiếm")
    while True:
        try:
            tim_kiem = int(input("Bạn hãy chọn 1 hoặc 2: "))
            if tim_kiem in [1,2]:
                break
        except ValueError:
            print("Lựa chọn không hợp lệ ! Vui lòng nhập lại lựa chọn.")
    if tim_kiem == 1:
        result, loai =tim_nv_theo_ma()
        #Neu result khong rong thi moi append
        if result is not None:
            if loai == "Hành chính":
                kq_tim_kiem["Hành chính"].append(result)
            elif loai == "Tiếp thị":
                kq_tim_kiem["Tiếp thị"].append(result)
            else:
                kq_tim_kiem["Trưởng phòng"].append(result)
        else:
            print("Không tìm thấy nhân viên trong danh sách.")
    else :
        list_tim_kiem =tim_nv_theo_luong(ds_nhanvien)
        for nv in list_tim_kiem:
            if isinstance(nv, NhanVienTiepThi):
                kq_tim_kiem["Tiếp thị"].append(nv)
            elif isinstance(nv, TruongPhong):
                kq_tim_kiem["Trưởng phòng"].append(nv)
            elif isinstance(nv, NhanVien):
                kq_tim_kiem["Hành chính"].append(nv)
    return kq_tim_kiem
    
def xoa_nv_theo_ma():
    result, loai = tim_nv_theo_ma()
    if result is not None:
        for loai_nhanvien in ds_nhanvien.keys():
            for nv in ds_nhanvien[loai_nhanvien]:
                if result.ma_nv == nv.ma_nv:
                    print(f"Đã xóa nhân viên mã {result.ma_nv}")
                    ds_nhanvien[loai_nhanvien].remove(result)
                    return
    else:
        print("Không có nhân viên cần xóa trong danh sách!")  
        return    
            
def sap_xep_nv_theo_thu_nhap():
    check = {}
    for loai, ds_nv in ds_nhanvien.items():
        check[loai] = sorted(ds_nv, key=lambda nv:nv.tinh_thu_nhap(), reverse= True)
    return check

def sap_xep_nv_theo_ho_ten():
    check = {}
    for loai, ds_nv in ds_nhanvien.items():
        check[loai] = sorted(ds_nv, key=lambda nv:nv.ten_nv, reverse= False)
    return check

def sap_xep_nv():
    print("*"*15+" SẮP XẾP NHÂN VIÊN "+"*"*16)
    print("|    1. Sắp xếp nhân viên theo tên               |")
    print("|    2. Sắp xếp nhân viên theo thu nhập          |")
    print("*"*50)
    print("Chọn phương thức tìm kiếm")
    kqua_sap_xep = {}
    while True:
        try:
            sap_xep = int(input("Bạn hãy chon 1 hoặc 2: "))
            if sap_xep in [1,2]:
                break
        except ValueError:
            print("Lựa chọn không hợp lệ ! Vui lòng nhập lại lựa chọn.")
    if sap_xep == 1:
        kqua_sap_xep=sap_xep_nv_theo_ho_ten()
    elif sap_xep == 2:
        kqua_sap_xep=sap_xep_nv_theo_thu_nhap()
    else:
        print("Thoát sắp xếp")
    return kqua_sap_xep

def xuat_5_nv_thu_nhap_cao_nhat():
    check =[]
    for ds_nhan_vien in ds_nhanvien.values():
        for nhan_vien in ds_nhan_vien:
            check.append(nhan_vien)
    sort_lst= sorted(check, key=lambda nv:nv.tinh_thu_nhap() , reverse= True)
    return sort_lst[:5]

def cap_nhat_tt_theo_ma(ds_nhanvien):
    nv_can_sua, loai = tim_nv_theo_ma()
    if nv_can_sua is not None:
        
            #Nhap ten moi
            print(f"Tìm thấy nhân viên tên:{nv_can_sua.ten_nv} thuộc loại: {loai}")
            ten_moi = input("Nhập tên mới ( hoặc nhập q để bỏ qua):")
            if ten_moi.strip() and ten_moi != "q":
                nv_can_sua.ten_nv = ten_moi
                
            #Nhap luong moi
            while True:
                luong_moi = input("Nhập lương mới (hoặc nhập q để bỏ qua): ")
                try:
                    if luong_moi.strip() and luong_moi != "q":
                        nv_can_sua.luong_thang = int(luong_moi)
                    break
                except ValueError:
                    print("Nhập sai! Vui lòng nhập lại")
            
                
        #Sua lai thong tin nhan vien tiep thi 
            if isinstance(nv_can_sua,NhanVienTiepThi):
                #Sua lai doanh so
                dso_moi = input("Nhập doanh số mới (hoặc nhập q để bỏ qua): ")
                while True:
                    if dso_moi.strip() and dso_moi != "q":
                        nv_can_sua.doanh_so = int(dso_moi)
                        break
                    else:
                        print("Giá trị không hợp lệ, vui lòng nhập lại")
                
                    
                #Sua lai ty le hoa hong
                hoa_hong_moi = input("Nhập tỷ lệ hoa hồng mới (hoặc nhập q để bỏ qua):")
                while True:
                    if hoa_hong_moi.strip() and hoa_hong_moi != "q":
                        nv_can_sua.ti_le_hoa_hong = int(hoa_hong_moi)
                        break
                    else:
                        print("Giá trị không hợp lệ, vui lòng nhập lại")
                
                    
        #Sua lai thong tin truong phong
            if isinstance(nv_can_sua,TruongPhong):
                #Sua lai luong trach nhiem
                luong_trach_nhiem_moi = input("Nhập lương trách nhiệm mới (hoặc nhập q để bỏ qua): ")
                while True:
                    if luong_trach_nhiem_moi.strip() and luong_trach_nhiem_moi != "q":
                        nv_can_sua.luong_trach_nhiem = int(luong_trach_nhiem_moi)
                        break
                    else:
                        print("Giá trị không hợp lệ, vui lòng nhập lại")
                
            print("\n")
            xuat_ds(ds_nhanvien)
    else:
        print("Không tìm thấy nhân viên trong danh sách.")
    
    

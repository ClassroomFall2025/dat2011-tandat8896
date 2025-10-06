from class_manager import * 

ds_nhanvien ={
        "Hành chính" :[],
        "Tiếp thị" :[],
        "Trưởng phòng": [] 
    }



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
            nhap_nhan_vien = Nhan_Vien().nhap_thong_tin(ds_nhanvien["Hành chính"])
            ds_nhanvien["Hành chính"].append(nhap_nhan_vien)
        elif the_loai == 2:
            nhap_nhan_vien_tiep_thi = Nhan_Vien_Tiep_Thi().nhap_thong_tin(ds_nhanvien["Tiếp thị"])
            ds_nhanvien["Tiếp thị"].append(nhap_nhan_vien_tiep_thi)
        elif the_loai == 3:
            nhap_truong_phong = Truong_Phong().nhap_thong_tin(ds_nhanvien["Trưởng phòng"])
            ds_nhanvien["Trưởng phòng"].append(nhap_truong_phong)
        elif the_loai ==0 :
            break
        else:
            print("vui lòng nhập lại lựa chọn 1, 2, 3 để nhập danh sách nhân viên hoặc 0 để thoát")
    return ds_nhanvien
    
# nhap_ds_nv()




def luu_file():
    pass


def doc_tu_file():
    pass

def xuat_ds(ds_nhanvien):
    print("="* 14 ,"Danh sach nhan vien", "="*15)
    for loai,danh_sach in ds_nhanvien.items():
        print(f"\n Loai nhan vien {loai}")
        if len(danh_sach) == 0:
            print("Chua co nhan vien")
        else:
            for nv in danh_sach:
                nv.xuat_thong_tin()
    


def tim_nv_theo_luong (ds_nhanvien:dict):
    tim_kiem_nv_theo_luong = []
    min_sal = int(input("Nhap min salary: "))
    max_sal = int(input("Nhap max salary: "))
    for loai_nv in ds_nhanvien.values():
        for employee in loai_nv:
            if min_sal <= employee.tinh_thu_nhap() <= max_sal:
                tim_kiem_nv_theo_luong.append(employee)
    return tim_kiem_nv_theo_luong

def tim_nv_theo_ma():
    ma_nv = input("Nhap ma nhan vien : ")
    for loai, danh_sach in ds_nhanvien.items():
        for nv in danh_sach:
            if nv.ma_nv == ma_nv:
                return nv
    # print("")
    return None
    
                

def tim_kiem_nhan_vien():
    list_tim_kiem = []
    print("*"*15+" TÌM KIẾM NHÂN VIÊN "+"*"*15)
    print("|    1. Tìm kiếm nhân viên theo mã               |")
    print("|    2. Tìm kiếm nhân viên theo khoảng lương     |")
    print("*"*50)
    print("Chọn phương thức tìm kiếm")
    while True:
        try:
            tim_kiem = int(input("Bạn hãy chon 1 hoặc 2: "))
            if tim_kiem in [1,2]:
                break
        except ValueError:
            print("Lựa chọn không hợp lệ ! Vui lòng nhập lại lựa chọn.")
    if tim_kiem == 1:
        result =tim_nv_theo_ma()
        #Neu result khong rong thi moi append
        if result is not None:
            list_tim_kiem.append(result)
    else :
        list_tim_kiem =tim_nv_theo_luong(ds_nhanvien)
    return list_tim_kiem
    
                    


def xoa_nv_theo_ma():
    result = tim_nv_theo_ma()
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
    pass

def sap_xep_nv_theo_ho_ten():
    pass

def sap_xep_nv_():
    print("*"*15+" SẮP XẾP NHÂN VIÊN "+"*"*16)
    print("|    1. Sắp xếp nhân viên theo tên               |")
    print("|    2. Sắp xếp nhân viên theo thu nhập          |")
    print("*"*50)
    print("Chọn phương thức tìm kiếm")
    while True:
        try:
            sap_xep = int(input("Bạn hãy chon 1 hoặc 2: "))
            if sap_xep in [1,2]:
                break
        except ValueError:
            print("Lựa chọn không hợp lệ ! Vui lòng nhập lại lựa chọn.")
    if sap_xep == 1:
        list_tim_kiem=sap_xep_nv_theo_ho_ten()
    elif sap_xep == 2:
        list_tim_kiem=sap_xep_nv_theo_thu_nhap()
    else:
        print("Thoát sắp xếp")
    return 

def cap_nhat_tt_theo_ma(ds_nhanvien):
    ma_nv_sua = input("Nhap ma nhan vien can sua: ")
    for loai, danh_sach in ds_nhanvien.items():
        for nv in danh_sach:
            if nv.ma_nv == ma_nv_sua:
                #Nhap ten moi
                print(f"Tìm thấy nhân viên tên:{nv.ten_nv} thuộc loại: {loai}")
                ten_moi = input("Nhập tên mới ( hoặc nhập 0 để bỏ qua):")
                if ten_moi.strip() and ten_moi != "0":
                    nv.ten_nv = ten_moi
                #Nhap luong moi
                luong_moi = (input("Nhập lương mới (hoặc nhập 0 để bỏ qua): "))
                if luong_moi.strip() and luong_moi != "0":
                    nv.luong_thang = int(luong_moi)
                #Sua lai thong tin nhan vien tiep thi 
                if isinstance(nv,Nhan_Vien_Tiep_Thi):
                    
                    #Sua lai doanh so
                    ds_moi = input("Nhập doanh số mới (hoặc nhập 0 để bỏ qua): ")
                    if ds_moi.strip() and ds_moi != "0":
                        nv.doanh_so = int(ds_moi)
                        
                    #Sua lai ty le hoa hong
                    hoa_hong_moi = input("Nhập tỷ lệ hoa hồng mới (hoặc nhập 0 để bỏ qua):")
                    if hoa_hong_moi.strip() and hoa_hong_moi != "0":
                        nv.ti_le_hoa_hong = int(hoa_hong_moi)
                #Sua lai thong tin truong phong
                if isinstance(nv,Truong_Phong):
                    
                    #Sua lai luong trach nhiem
                    luong_trach_nhiem_moi = input("Nhập lương trách nhiệm mới (hoặc nhập 0 để bỏ qua): ")
                    if luong_trach_nhiem_moi.strip() and luong_trach_nhiem_moi != "0":
                        nv.luong_trach_nhiem = int(luong_trach_nhiem_moi)
                print("\n")
                xuat_ds(ds_nhanvien)


def xuat_5_nv_thu_nhap_cao_nhat():
    check =[]
    for loai_nhan_vien in ds_nhanvien.values():
        for nhan_vien in loai_nhan_vien:
            check.append(nhan_vien)
    sort_lst= sorted(check, key=lambda nv:nv.tinh_thu_nhap() , reverse= True)
    return sort_lst[:5]

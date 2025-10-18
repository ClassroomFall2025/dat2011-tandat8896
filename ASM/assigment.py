from mainfunction import *

menu_list = {
    0: "Thoát chương trình",
    1: "Nhập danh sách nhân viên từ bàn phím và lưu vào file",
    2: "Đọc thông tin nhân viên từ file và xuất danh sách",
    3: "Tìm kiếm nhân viên",
    4: "Xóa nhân viên theo mã",
    5: "Cập nhật thông tin nhân viên theo mã",
    6: "Sắp xếp danh sách nhân viên",
    7: "Xuất 5 nhân viên có thu nhập cao nhất",
    8: "Xuất nhân viên theo phòng ban"  
}

def menu():
    while True:
        print("="*24+"MENU CHƯƠNG TRÌNH"+"="*23)
        for key, value in menu_list.items():
            print(f"| {key} : {value} {(55 - len(value)) * ' '} |")
        print("="*64)  
              
        while True:
            try:
                lua_chon = int(input("Nhập lựa chọn của bạn từ 0 - 8: "))
                break
            except ValueError:
                print("Lựa chọn không hợp lệ,vui lòng nhập lại lựa chọn")
                
        match lua_chon:
            case 0:
                print("Cảm ơn đã sử dụng chương trình!")
                break
            case 1:
                nhap_ds_nv()
                ghi_file()
            case 2:
                xuat_ds(ds_nhanvien)   
            case 3:
                ds_timkiem=tim_kiem_nhan_vien()
                if not (ds_timkiem["Hành chính"]==[] and ds_timkiem["Tiếp thị"]==[] and ds_timkiem["Trưởng phòng"]==[]):
                    if ds_timkiem["Hành chính"] != []:
                        xuat_ds_theo_loai("Hành chính",ds_timkiem["Hành chính"])
                    if ds_timkiem["Tiếp thị"] != []:
                        xuat_ds_theo_loai("Tiếp thị",ds_timkiem["Tiếp thị"])
                    if ds_timkiem["Trưởng phòng"] != []:
                        xuat_ds_theo_loai("Trưởng phòng",ds_timkiem["Trưởng phòng"])
            case 4:
                xoa_nv_theo_ma()
                ghi_file()    
            case 5:
                cap_nhat_tt_theo_ma(ds_nhanvien)  
            case 6:
                xuat_ds(sap_xep_nv())    
            case 7:
                result = xuat_5_nv_thu_nhap_cao_nhat()
                
                for i in result:
                    print("="*60+"")
                    print(f"| {'Mã NV':^10} | {'Tên NV':^20} | {'Lương':^20} |" )
                    print(i.xuat_thong_tin_co_ban())
            case 8:
                xuat_ds_theo_phong_ban(ds_nhanvien)
            case _:
                print("Lựa chọn không hợp lệ.")

menu()
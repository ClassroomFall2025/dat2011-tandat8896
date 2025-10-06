from mainfunction import *

menu_list = {
    0: "Thoát chương trình",
    1: "Nhập danh sách nhân viên từ bàn phím và lưu vào file",
    2: "Đọc thông tin nhân viên từ file và xuất danh sách",
    3: "Tìm kiếm nhân viên",
    4: "Xóa nhân viên theo mã",
    5: "Cập nhật thông tin nhân viên theo mã",
    6: "Sắp xếp danh sách nhân viên",
    7: "Xuất 5 nhân viên có thu nhập cao nhất"  
}
def menu():
    print("="*24+"MENU CHƯƠNG TRÌNH"+"="*23)
    for key, value in menu_list.items():
        print(f"| {key} : {value} {(55 - len(value)) * ' '} |")
    print("="*64)


    while True:
        while True:
            try:
                lua_chon = int(input("Nhập lựa chọn của bạn từ 0 - 7: "))
                break
            except ValueError:
                print("Lựa chọn không hợp lệ,vui lòng nhập lại lựa chọn")
        match lua_chon:
            case 0:
                break
            case 1:
                nhap_ds_nv()
                luu_file()
            case 2:
                #doc_tu_file()
                xuat_ds(ds_nhanvien)
            case 3:
                ds_timkiem=tim_kiem_nhan_vien()
                # print(ds_timkiem[0])
                if len(ds_timkiem) == 0:
                    print("Không tìm thấy nhân viên phù hợp")
                else:
                    print(f"Tìm thấy {len(ds_timkiem)} nhân viên phù hợp")
                    for nv in ds_timkiem:
                        nv.xuat_thong_tin()
            case 4:
                xoa_nv_theo_ma()
                
            case 5:
                cap_nhat_tt_theo_ma(ds_nhanvien)
                
            case 6:
                sap_xep_nv_()
            case 7:
                result= xuat_5_nv_thu_nhap_cao_nhat()
                for i in result:
                    i.xuat_thong_tin()
            case _:
                print("Lựa chọn không hợp lệ.")

def main():
    menu()

if __name__ == "__main__":
    main()
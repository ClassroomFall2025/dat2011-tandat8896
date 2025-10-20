import re
from accounts import TaiKhoan, docTaiKhoanTuCSV, ghiTaiKhoanVaoCSV
from simple_jwt import SimpleJWT

menu_list = {
    "1": "Tạo tài khoản",
    "2": "Gửi tiền",
    "3": "Rút tiền",
    "4": "Kiểm tra số dư",
    "5": "Danh sách tất cả tài khoản",
    "6": "Đóng (Xóa) tài khoản",
    "7": "Chinh sua thong tin tai khoản",
    "8": "Tìm kiếm thông tin tài khoản",
    "9": "Xuất báo cáo thống kê",
    "10": "Đọc dữ liệu từ CSV",
    "11": "Lưu dữ liệu vào CSV",
    "12": "Chọn tài khoản hiện tại",
    "0": "Thoát"
}

# Tính chiều rộng cột
width = max(len(f"{k}. {v}") for k, v in menu_list.items())

# Vẽ menu liền mạch - đã chuyển vào hàm hien_thi_menu()

# Khởi tạo biến toàn cục
current_account = None
all_accounts = []

def hien_thi_menu():
    """Hiển thị menu"""
    print("\n" + "="*50)
    print("HE THONG QUAN LY TAI KHOAN NGAN HANG")
    print("="*50)
    
    # Hiển thị trạng thái hiện tại
    if current_account:
        print(f"Tài khoản hiện tại: {current_account._TaiKhoan__so_tai_khoan} - Số dư: {current_account._TaiKhoan__so_du}")
    else:
        print("Chưa có tài khoản nào được chọn")
    
    print(f"Tổng số tài khoản: {len(all_accounts)}")
    print("="*50)
    
    print("+" + "-" * (width + 2) + "+")
    # Sắp xếp theo thứ tự số thay vì alphabet
    sorted_keys = sorted(menu_list.keys(), key=lambda x: int(x) if x.isdigit() else float('inf'))
    for i, k in enumerate(sorted_keys):
        print(f"| {k}. {menu_list[k]:<{width}} |")
    print("+" + "-" * (width + 2) + "+")
def main():
    global current_account, all_accounts
    
    while True:
        try:
            hien_thi_menu()
            lua_chon = int(input("Nhap lựa chon: "))
            
            match lua_chon:
                case 1: 
                    print("\n=== TAO TAI KHOAN ===")
                    account = TaiKhoan()
                    result = account.tao_tai_khoan()
                    if result:  # Nếu tạo thành công
                        current_account = account
                        all_accounts.append(account)
                        print("Tạo tài khoản thành công!")
                    else:
                        print("Tạo tài khoản thất bại!")
                    
                case 2:
                    if current_account:
                        print("\n=== GUI TIEN ===")
                        print(f" current_account = {current_account}")
                        print(f"so_tai_khoan = {current_account._TaiKhoan__so_tai_khoan}")
                        so_tien = float(input("Nhập số tiền gửi: "))
                        if current_account.gui_tien(so_tien):
                            print(f"Gửi tiền thành công! Số dư hiện tại: {current_account._TaiKhoan__so_du}")
                        else:
                            print("Số tiền không hợp lệ!")
                    else:
                        print("Chưa có tài khoản nào được chọn!")
                        print(f"Debug: current_account = {current_account}")
                        
                case 3:
                    if current_account:
                        print("\n=== RUT TIEN ===")
                        so_tien = float(input("Nhập số tiền rút: "))
                        if current_account.rut_tien(so_tien):
                            print(f"Rút tiền thành công! Số dư hiện tại: {current_account._TaiKhoan__so_du}")
                        else:
                            print("Số tiền không hợp lệ hoặc không đủ số dư!")
                    else:
                        print("Chưa có tài khoản nào được chọn!")
                        
                case 4:
                    if current_account:
                        print("\n=== KIEM TRA SO DU ===")
                        print(f"Số dư hiện tại: {current_account._TaiKhoan__so_du}")
                    else:
                        print("Chưa có tài khoản nào được chọn!")
                        
                case 5:
                    print("\n=== DANH SACH TAT CA TAI KHOAN ===")
                    if current_account:
                        current_account.hien_thi_tai_khoan()
                    else:
                        print("Chưa có tài khoản nào!")
                        
                case 6:
                    if current_account:
                        print("\n=== DONG TAI KHOAN ===")
                        confirm = input("Bạn có chắc muốn đóng tài khoản? (y/n): ")
                        if confirm.lower() == 'y':
                            # Xóa tài khoản khỏi database
                            if current_account._TaiKhoan__so_tai_khoan in TaiKhoan._TaiKhoan__database:
                                del TaiKhoan._TaiKhoan__database[current_account._TaiKhoan__so_tai_khoan]
                                print("Đóng tài khoản thành công!")
                                current_account = None
                            else:
                                print("Không tìm thấy tài khoản trong database!")
                    else:
                        print("Chưa có tài khoản nào được chọn!")
                        
                case 7:
                    if current_account:
                        print("\n=== CHINH SUA THONG TIN TAI KHOAN ===")
                        print("Chức năng chỉnh sửa thông tin tài khoản")
                        print("Thông tin tài khoản hiện tại:")
                        current_account.hien_thi_tai_khoan()
                        print("Để chỉnh sửa, vui lòng tạo tài khoản mới với thông tin cập nhật")
                    else:
                        print("Chưa có tài khoản nào được chọn!")
                        
                case 8:
                    print("\n=== TIM KIEM THONG TIN TAI KHOAN ===")
                    stk = input("Nhập số tài khoản cần tìm: ")
                    if stk in TaiKhoan._TaiKhoan__database:
                        print("Tìm thấy tài khoản!")
                        # Tạo object tạm để hiển thị
                        temp_account = TaiKhoan()
                        temp_account._TaiKhoan__so_tai_khoan = stk
                        temp_account._TaiKhoan__ten_tai_khoan = TaiKhoan._TaiKhoan__database[stk]['ten_tai_khoan']
                        temp_account.loai_tai_khoan = TaiKhoan._TaiKhoan__database[stk]['loai_tai_khoan']
                        temp_account._TaiKhoan__so_du = TaiKhoan._TaiKhoan__database[stk]['so_du']
                        temp_account.khach_hang = TaiKhoan._TaiKhoan__database[stk]['khach_hang']
                        temp_account.hien_thi_tai_khoan()
                    else:
                        print("Không tìm thấy tài khoản!")
                        
                case 9:
                    print("\n=== XUAT BAO CAO THONG KE ===")
                    if current_account:
                        current_account.hien_thi_tat_ca_tai_khoan_khach_hang()
                    else:
                        print("Chưa có tài khoản nào!")
                        
                case 10:
                    print("\n=== DOC DU LIEU TU CSV ===")
                    filename = input("Nhập tên file CSV (mặc định: taikhoan.csv): ").strip()
                    if not filename:
                        filename = "taikhoan.csv"
                    loaded_accounts = docTaiKhoanTuCSV(filename)
                    if loaded_accounts:
                        # Xóa danh sách cũ
                        all_accounts.clear()
                        # Thêm tài khoản mới
                        all_accounts.extend(loaded_accounts)
                        # Set tài khoản đầu tiên làm current
                        current_account = loaded_accounts[0]
                        print(f"Đã tải {len(loaded_accounts)} tài khoản!")
                        print(f"Tài khoản hiện tại: {current_account._TaiKhoan__so_tai_khoan}")
                    else:
                        print("Không có dữ liệu để tải!")
                    
                case 11:
                    print("\n=== LUU DU LIEU VAO CSV ===")
                    if all_accounts:
                        filename = input("Nhập tên file CSV (mặc định: taikhoan.csv): ").strip()
                        if not filename:
                            filename = "taikhoan.csv"
                        if ghiTaiKhoanVaoCSV(all_accounts, filename):
                            print("Lưu dữ liệu thành công!")
                        else:
                            print("Lưu dữ liệu thất bại!")
                    else:
                        print("Không có dữ liệu để lưu!")
                        
                case 12:
                    print("\n=== CHON TAI KHOAN HIEN TAI ===")
                    if all_accounts:
                        print("Danh sách tài khoản có sẵn:")
                        for i, account in enumerate(all_accounts):
                            print(f"{i+1}. STK: {account._TaiKhoan__so_tai_khoan} - Tên: {account._TaiKhoan__ten_tai_khoan} - Số dư: {account._TaiKhoan__so_du}")
                        
                        try:
                            choice = int(input("Chọn tài khoản (nhập số thứ tự): ")) - 1
                            if 0 <= choice < len(all_accounts):
                                current_account = all_accounts[choice]
                                print(f"Đã chọn tài khoản: {current_account._TaiKhoan__so_tai_khoan}")
                            else:
                                print("Lựa chọn không hợp lệ!")
                        except ValueError:
                            print("Vui lòng nhập số!")
                    else:
                        print("Chưa có tài khoản nào!")
                        
                case 0:
                    print("Kết thúc chương trình")
                    break
                    
                case _:
                    print("Lựa chọn không hợp lệ vui lòng nhập lại")

        except ValueError:
            print("Lựa chọn không hợp lệ vui lòng nhập lại")
        except Exception as e:
            print(f"Lỗi: {e}")

if __name__ == "__main__":
    main()
        


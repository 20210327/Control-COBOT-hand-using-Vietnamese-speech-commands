import os
import shutil

def copy_files(source_dir, destination_dir, keyword):
    """
    Di chuyển các file có chứa keyword trong tên từ thư mục nguồn sang thư mục đích.
    
    :param source_dir: Thư mục nguồn chứa các file
    :param destination_dir: Thư mục đích để lưu file
    :param keyword: Từ khóa đặc trưng trong tên file
    """

    # Lấy danh sách file trong thư mục nguồn
    files = os.listdir(source_dir)

    for file_name in files:
        # Kiểm tra xem từ khóa có trong tên file không
        if keyword in file_name:
            # Đường dẫn file nguồn và đích
            source_path = os.path.join(source_dir, file_name)
            destination_path = os.path.join(destination_dir, file_name)
            
            # Copy file
            shutil.copy(source_path, destination_path)
            #print(f"Đã di chuyển: {file_name}")

train_dir = "d:\doAnTN\data\Train"
val_dir = "d:\doAnTN\data\Validation"
test_dir = "d:\doAnTN\data\Test"

train_destination = "d:\doAnTN\splited_data\Train"
val_destination = "d:\doAnTN\splited_data\Validation"
test_destination = "d:\doAnTN\splited_data\Test"

for destination in [train_destination, val_destination, test_destination]:
    for label in os.listdir(destination):
        label_path = os.path.join(destination, label)
        for file in os.listdir(label_path):
            file_path = os.path.join(label_path, file)
            if os.path.isfile(file_path):  # Check if it's a file
                os.remove(file_path)  # Delete file

for id in os.listdir(train_dir):
    id_path = os.path.join(train_dir,id)
    copy_files(id_path, os.path.join(train_destination, 'dung'), 'Dung')
    copy_files(id_path, os.path.join(train_destination, 'tien_theo_truc_X'), 'Tx')
    copy_files(id_path, os.path.join(train_destination, 'lui_theo_truc_X'), 'Lx')
    copy_files(id_path, os.path.join(train_destination, 'tien_theo_truc_Y'), 'TY')
    copy_files(id_path, os.path.join(train_destination, 'lui_theo_truc_Y'), 'LY')
    copy_files(id_path, os.path.join(train_destination, 'tien_theo_truc_Z'), 'TZ')
    copy_files(id_path, os.path.join(train_destination, 'lui_theo_truc_Z'), 'LZ')
    copy_files(id_path, os.path.join(train_destination, 'quay_trai_theo_truc_X'), 'QtX')
    copy_files(id_path, os.path.join(train_destination, 'quay_phai_theo_truc_X'), 'QpX')
    copy_files(id_path, os.path.join(train_destination, 'quay_trai_theo_truc_Y'), 'QtY')
    copy_files(id_path, os.path.join(train_destination, 'quay_phai_theo_truc_Y'), 'QpY')
    copy_files(id_path, os.path.join(train_destination, 'quay_trai_theo_truc_Z'), 'QtZ')
    copy_files(id_path, os.path.join(train_destination, 'quay_phai_theo_truc_Z'), 'QpZ')
    copy_files(id_path, os.path.join(train_destination, 'gap_vat'), 'Gap')
    copy_files(id_path, os.path.join(train_destination, 'tha_vat'), 'Tha')

for id in os.listdir(val_dir):
    id_path = os.path.join(val_dir,id)
    copy_files(id_path, os.path.join(val_destination, 'dung'), 'Dung')
    copy_files(id_path, os.path.join(val_destination, 'tien_theo_truc_X'), 'Tx')
    copy_files(id_path, os.path.join(val_destination, 'lui_theo_truc_X'), 'Lx')
    copy_files(id_path, os.path.join(val_destination, 'tien_theo_truc_Y'), 'TY')
    copy_files(id_path, os.path.join(val_destination, 'lui_theo_truc_Y'), 'LY')
    copy_files(id_path, os.path.join(val_destination, 'tien_theo_truc_Z'), 'TZ')
    copy_files(id_path, os.path.join(val_destination, 'lui_theo_truc_Z'), 'LZ')
    copy_files(id_path, os.path.join(val_destination, 'quay_trai_theo_truc_X'), 'QtX')
    copy_files(id_path, os.path.join(val_destination, 'quay_phai_theo_truc_X'), 'QpX')
    copy_files(id_path, os.path.join(val_destination, 'quay_trai_theo_truc_Y'), 'QtY')
    copy_files(id_path, os.path.join(val_destination, 'quay_phai_theo_truc_Y'), 'QpY')
    copy_files(id_path, os.path.join(val_destination, 'quay_trai_theo_truc_Z'), 'QtZ')
    copy_files(id_path, os.path.join(val_destination, 'quay_phai_theo_truc_Z'), 'QpZ')
    copy_files(id_path, os.path.join(val_destination, 'gap_vat'), 'Gap')
    copy_files(id_path, os.path.join(val_destination, 'tha_vat'), 'Tha')

for id in os.listdir(test_dir):
    id_path = os.path.join(test_dir,id)
    copy_files(id_path, os.path.join(test_destination, 'dung'), 'Dung')
    copy_files(id_path, os.path.join(test_destination, 'tien_theo_truc_X'), 'Tx')
    copy_files(id_path, os.path.join(test_destination, 'lui_theo_truc_X'), 'Lx')
    copy_files(id_path, os.path.join(test_destination, 'tien_theo_truc_Y'), 'TY')
    copy_files(id_path, os.path.join(test_destination, 'lui_theo_truc_Y'), 'LY')
    copy_files(id_path, os.path.join(test_destination, 'tien_theo_truc_Z'), 'TZ')
    copy_files(id_path, os.path.join(test_destination, 'lui_theo_truc_Z'), 'LZ')
    copy_files(id_path, os.path.join(test_destination, 'quay_trai_theo_truc_X'), 'QtX')
    copy_files(id_path, os.path.join(test_destination, 'quay_phai_theo_truc_X'), 'QpX')
    copy_files(id_path, os.path.join(test_destination, 'quay_trai_theo_truc_Y'), 'QtY')
    copy_files(id_path, os.path.join(test_destination, 'quay_phai_theo_truc_Y'), 'QpY')
    copy_files(id_path, os.path.join(test_destination, 'quay_trai_theo_truc_Z'), 'QtZ')
    copy_files(id_path, os.path.join(test_destination, 'quay_phai_theo_truc_Z'), 'QpZ')
    copy_files(id_path, os.path.join(test_destination, 'gap_vat'), 'Gap')
    copy_files(id_path, os.path.join(test_destination, 'tha_vat'), 'Tha')
                

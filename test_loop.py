previous_state = False  # Trạng thái trước đó của nút bấm
read_once = False        # Biến để đảm bảo chỉ đọc một lần

while True:
    current_state = read_button_state()  # Hàm đọc trạng thái của nút bấm

    if current_state and not previous_state and not read_once:
        # Nếu nút bấm được nhấn và trước đó không nhấn
        result = client.read_coils(address=start_address, count=count, unit=unit_id)
        
        if result.isError():
            print("Lỗi khi đọc coil:", result)
        else:
            for i in range(count):
                print(f"Coil {start_address + i}: {'ON' if result.bits[i] else 'OFF'}")
        
        read_once = True  # Đánh dấu là đã đọc rồi

    elif not current_state:
        # Nếu nút bấm không được nhấn, reset biến read_once
        read_once = False

    previous_state = current_state  # Cập nhật trạng thái trước đó

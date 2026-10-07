
gia_thit = 100
gia_rau = 50
gia_traicay = 80
gia_xaphong = 20
gia = [100, 50, 80, 20]
gio_hang = ["thit", "rau", "traicay", "xaphong"]

def tinh_tien(name, gio_hang):

    tong_tien = 0
    for item in gio_hang: 
        if item == "thit":
            tong_tien = tong_tien + gia_thit*0.5
        elif item == "rau":
            tong_tien = tong_tien + gia_rau*0.6
        elif item == "traicay":
            tong_tien = tong_tien + gia_traicay*0.7
        elif item == "xaphong":
            tong_tien = tong_tien + gia_xaphong
    
    return {
        "ho_ten": name,
        "tong_tien": tong_tien,
    }

thong_tin_khach_hang = tinh_tien("Nguyen Phuc Hoai", gio_hang)
print(thong_tin_khach_hang)

from atm import atm
from dulieu import tenkh, tentk, mk, sodu, hanmuc, sodunganhang
header = '********************'
while True:
    if sodunganhang[0] <= 0:
        print(header.center(68))
        print('SỐ DƯ ATM ĐÃ HẾT, BẠN KHÔNG THỂ SỬ DỤNG CHỨC NĂNG RÚT VÀ CHUYỂN TIỀN')
        print(header.center(68))
    name = str(input('VUI LÒNG NHẬP TÊN ĐĂNG NHẬP: '))
    if name in tentk:
        i = tentk.index(name)
        atm(tenkh[i], mk[i], mk, sodu, hanmuc, sodunganhang, i)
    else:
        print(header.center(27))
        print('TÊN ĐĂNG NHẬP KHÔNG HỢP LỆ')
        print(header.center(27))

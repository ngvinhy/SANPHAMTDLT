def atm(tk, password, pin, changesodu, changehanmuc, sodu_atm, stt):
    header = '***************'
    dem = 1
    mapin = input('MÃ PIN (CÒN 3 LẦN THỬ): ')
    while dem <= 3:
        if mapin == str(password):
            break
        if dem == 3:
            print(header.center(39))
            print('   SAI MÃ PIN QUÁ SỐ LẦN QUY ĐỊNH!!!\nTHẺ CỦA BẠN SẼ BỊ KHÓA TRONG ÍT PHÚT!!!')
            print(header.center(39))
            return
        else:
            mapin = input(f'MÃ PIN KHÔNG HỢP LỆ (CÒN {3 - dem} LẦN THỬ): ')
            dem += 1
    print(header.center(27))
    print('BẠN ĐÃ ĐĂNG NHẬP THÀNH CÔNG')
    print(header.center(27))
    while True:
        print('*1. Tra cứu tài khoản\n*2. Rút tiền\n*3. Chuyển tiền\n*4. Thay đổi mã PIN\n*0. Thoát')
        chucnang = input('CHỌN CHỨC NĂNG BẠN MUỐN SỬ DỤNG: ')
        if chucnang == '1':
            chucnang1(header, tk, changesodu[stt], changehanmuc[stt])
            print('BẠN CÓ MUỐN TIẾP TỤC SỬ DỤNG DỊCH VỤ KHÔNG?\n*1. Có\n*2. Không')
            while True:
                q = input('Chọn: ')
                if int(q) == 1:
                    print(header.center(43))
                    print('BẠN SẼ ĐƯỢC CHUYỂN HƯỚNG ĐẾN MÀN HÌNH CHÍNH')
                    print(header.center(43))
                    break
                elif int(q) == 2:
                    print(header.center(27))
                    print('BẠN ĐÃ ĐĂNG XUẤT THÀNH CÔNG')
                    print(header.center(27))
                    return
                else:
                    print(header.center(44))
                    print('CHỨC NĂNG KHÔNG HỢP LỆ, XIN VUI LÒNG THỬ LẠI')
                    print(header.center(44))
        elif chucnang == '2':
            if sodu_atm[0] <= 0:
                break
            else:
                chucnang2(header, tk, changesodu[stt], changehanmuc[stt], changehanmuc, changesodu, sodu_atm, stt)
                print('BẠN CÓ MUỐN TIẾP TỤC SỬ DỤNG DỊCH VỤ KHÔNG?\n*1. Có\n*2. Không')
                while True:
                    q = input('Chọn: ')
                    if int(q) == 1:
                        print(header.center(43))
                        print('BẠN SẼ ĐƯỢC CHUYỂN HƯỚNG ĐẾN MÀN HÌNH CHÍNH')
                        print(header.center(43))
                        break
                    elif int(q) == 2:
                        print(header.center(27))
                        print('BẠN ĐÃ ĐĂNG XUẤT THÀNH CÔNG')
                        print(header.center(27))
                        return
                    else:
                        print(header.center(44))
                        print('CHỨC NĂNG KHÔNG HỢP LỆ, XIN VUI LÒNG THỬ LẠI')
                        print(header.center(44))
        elif chucnang == '3':
            if sodu_atm[0] <= 0:
                break
            else:
                chucnang3(header, changesodu[stt], changehanmuc[stt], changehanmuc, changesodu, sodu_atm, stt)
                print('BẠN CÓ MUỐN TIẾP TỤC SỬ DỤNG DỊCH VỤ KHÔNG?\n*1. Có\n*2. Không')
                while True:
                    q = input('Chọn: ')
                    if int(q) == 1:
                        print(header.center(43))
                        print('BẠN SẼ ĐƯỢC CHUYỂN HƯỚNG ĐẾN MÀN HÌNH CHÍNH')
                        print(header.center(43))
                        break
                    elif int(q) == 2:
                        print(header.center(27))
                        print('BẠN ĐÃ ĐĂNG XUẤT THÀNH CÔNG')
                        print(header.center(27))
                        return
                    else:
                        print(header.center(44))
                        print('CHỨC NĂNG KHÔNG HỢP LỆ, XIN VUI LÒNG THỬ LẠI')
                        print(header.center(44))
        elif chucnang == '4':
            chucnang4(header, pin, stt)
            print('BẠN CÓ MUỐN TIẾP TỤC SỬ DỤNG DỊCH VỤ KHÔNG?\n*1. Có\n*2. Không')
            while True:
                q = input('Chọn: ')
                if int(q) == 1:
                    print(header.center(43))
                    print('BẠN SẼ ĐƯỢC CHUYỂN HƯỚNG ĐẾN MÀN HÌNH CHÍNH')
                    print(header.center(43))
                    break
                elif int(q) == 2:
                    print(header.center(27))
                    print('BẠN ĐÃ ĐĂNG XUẤT THÀNH CÔNG')
                    print(header.center(27))
                    return
                else:
                    print(header.center(44))
                    print('CHỨC NĂNG KHÔNG HỢP LỆ, XIN VUI LÒNG THỬ LẠI')
                    print(header.center(44))
        elif chucnang == '0':
            print(header.center(27))
            print('BẠN ĐÃ ĐĂNG XUẤT THÀNH CÔNG')
            print(header.center(27))
            break
        else:
            print(header.center(44))
            print('CHỨC NĂNG KHÔNG HỢP LỆ, XIN VUI LÒNG THỬ LẠI')
            print(header.center(44))


def chucnang1(header, tk, tien, gioihan):
    print(header.center(27))
    print(f'CHỦ THẺ: {tk} \nSỐ DƯ: {tien} VNĐ \nHẠN MỨC GIAO DỊCH: {gioihan} VNĐ')
    print(header.center(27))


def chucnang2(header, tk,  tien, gioihan, changehanmuc, changesodu, sodu_atm, stt):
    if gioihan == 0:
        print(header.center(43))
        print('HẠN MỨC GIAO DỊCH TRONG NGÀY CỦA BẠN ĐÃ HẾT')
        print(header.center(43))
        return
    else:
        print(header.center(21))
        print('     [*0. Thoát]')
        while True:
            ruttien = input('NHẬP SỐ TIỀN CẦN RÚT: ')
            if int(ruttien) == 0:
                break
            if ruttien.isdigit():
                if int(ruttien) > sodu_atm[0]:
                    print('ATM KHÔNG ĐỦ SỐ DƯ THỰC HIỆN GIAO DỊCH, XIN VUI LÒNG THỬ LẠI!!!')
                elif int(ruttien) <= tien:
                    if gioihan < int(ruttien):
                        print('SỐ TIỀN VƯỢT QUÁ HẠN MỨC GIAO DỊCH TRONG NGÀY, XIN VUI LÒNG THỬ LẠI!!!')
                    else:
                        if int(ruttien) % 50000 == 0:
                            tien = tien - int(ruttien)
                            changesodu[stt] = tien
                            sodu_atm[0] -= int(ruttien)
                            gioihan = gioihan - int(ruttien)
                            changehanmuc[stt] = gioihan
                            print('BẠN CÓ MUỐN NHẬN HÓA ĐƠN KHÔNG?\n*1. Có\n*2. Không')
                            while True:
                                bienlai = input('Chọn: ')
                                if bienlai == '1':
                                    print(header.center(27))
                                    print(f'CHỦ THẺ: {tk}\nSỐ TIỀN ĐÃ RÚT: {int(ruttien)} VNĐ\nSỐ DƯ: {tien} VNĐ')
                                    print(header.center(27))
                                    return
                                elif bienlai == '2':
                                    print(header.center(48))
                                    print('GIAO DỊCH HOÀN THÀNH, XIN VUI LÒNG ĐỢI NHẬN TIỀN')
                                    print(header.center(48))
                                    return
                                else:
                                    print(header.center(44))
                                    print('CHỨC NĂNG KHÔNG HỢP LỆ, XIN VUI LÒNG THỬ LẠI')
                                    print(header.center(44))
                        else:
                            print('SỐ TIỀN GIAO DỊCH PHẢI LÀ BỘI SỐ CỦA 50000 VNĐ, XIN VUI LÒNG THỬ LẠI!!!')
                else:
                    print('SỐ DƯ KHÔNG ĐỦ, XIN VUI LÒNG THỬ LẠI!!!')
            else:
                print('SỐ TIỀN KHÔNG HỢP LỆ, XIN VUI LÒNG THỬ LẠI!!!')


def chucnang3(header, tien, gioihan, changehanmuc, changesodu, sodu_atm, stt):
    if gioihan == 0:
        print(header.center(43))
        print('HẠN MỨC GIAO DỊCH TRONG NGÀY CỦA BẠN ĐÃ HẾT')
        print(header.center(43))
        return
    else:
        print(header.center(39))
        print('              [*0. Thoát]')
        while True:
            stk = input('NHẬP SỐ TÀI KHOẢN BẠN MUỐN CHUYỂN TIỀN: ')
            if int(stk) == 0:
                break
            if stk.isdigit():
                chuyentien = input('NHẬP SỐ TIỀN CẦN CHUYỂN: ')
                if int(chuyentien) == 0:
                    break
                if chuyentien.isdigit():
                    if int(chuyentien) > sodu_atm[0]:
                        print('ATM KHÔNG ĐỦ SỐ DƯ THỰC HIỆN GIAO DỊCH, XIN VUI LÒNG THỬ LẠI!!!')
                    elif int(chuyentien) <= tien:
                        if gioihan < int(chuyentien):
                            print('SỐ TIỀN VƯỢT QUÁ HẠN MỨC GIAO DỊCH TRONG NGÀY, XIN VUI LÒNG THỬ LẠI!!!')
                        else:
                            if int(chuyentien) % 50000 == 0:
                                tien = tien - int(chuyentien)
                                changesodu[stt] = tien
                                sodu_atm[0] -= int(chuyentien)
                                gioihan = gioihan - int(chuyentien)
                                changehanmuc[stt] = gioihan
                                print('BẠN CÓ MUỐN NHẬN HÓA ĐƠN KHÔNG?\n*1. Có\n*2. Không')
                                while True:
                                    bienlai = input('Chọn: ')
                                    if bienlai == '1':
                                        print(header.center(27))
                                        print(f'SỐ TÀI KHOẢN NGƯỜI NHẬN: {stk}\nSỐ TIỀN ĐÃ CHUYỂN: {int(chuyentien)} VNĐ\nSỐ DƯ: {tien} VNĐ')
                                        print(header.center(27))
                                        return
                                    elif bienlai == '2':
                                        print(header.center(20))
                                        print('GIAO DỊCH HOÀN THÀNH')
                                        print(header.center(20))
                                        return
                                    else:
                                        print(header.center(44))
                                        print('CHỨC NĂNG KHÔNG HỢP LỆ, XIN VUI LÒNG THỬ LẠI')
                                        print(header.center(44))
                            else:
                                print('SỐ TIỀN GIAO DỊCH PHẢI LÀ BỘI SỐ CỦA 50000 VNĐ, XIN VUI LÒNG THỬ LẠI!!!')
                    else:
                        print('SỐ DƯ KHÔNG ĐỦ, XIN VUI LÒNG THỬ LẠI!!!')
                else:
                    print('SỐ TIỀN KHÔNG HỢP LỆ, XIN VUI LÒNG THỬ LẠI!!!')
            else:
                print('SỐ TÀI KHOẢN KHÔNG HỢP LỆ, XIN VUI LÒNG THỬ LẠI!!!')


def chucnang4(header, pin, stt):
    print(header.center(15))
    print('  [*0. Thoát]')
    while True:
        oldpin = input('NHẬP MÃ PIN CŨ: ')
        if oldpin.isdigit():
            if int(oldpin) == 0:
                break
            if int(oldpin) == pin[stt]:
                while True:
                    newpin = input('NHẬP MÃ PIN MỚI: ')
                    if newpin.isdigit():
                        if int(newpin) == 0:
                            return
                        else:
                            while True:
                                newpin1 = input('NHẬP LẠI MÃ PIN MỚI: ')
                                if newpin1.isdigit():
                                    if int(newpin1) == 0:
                                        return
                                    if int(newpin) == int(newpin1):
                                        pin[stt] = int(newpin)
                                        print(header.center(33))
                                        print('BẠN ĐÃ THAY ĐỔI THÀNH CÔNG MÃ PIN')
                                        print(header.center(33))
                                        return
                                    else:
                                        print(header.center(49))
                                        print('MÃ PIN MỚI KHÔNG TRÙNG KHỚP, XIN VUI LÒNG THỬ LẠI')
                                        print(header.center(49))
                                else:
                                    print(header.center(43))
                                    print('MÃ PIN PHẢI LÀ CHỮ SỐ, XIN VUI LÒNG THỬ LẠI')
                                    print(header.center(43))
                    else:
                        print(header.center(43))
                        print('MÃ PIN PHẢI LÀ CHỮ SỐ, XIN VUI LÒNG THỬ LẠI')
                        print(header.center(43))
            else:
                print(header.center(32))
                print('SAI MÃ PIN, XIN VUI LÒNG THỬ LẠI')
                print(header.center(32))
        else:
            print(header.center(43))
            print('MÃ PIN PHẢI LÀ CHỮ SỐ, XIN VUI LÒNG THỬ LẠI')
            print(header.center(43))

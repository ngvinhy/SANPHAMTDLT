def atm(tk, password, tien, gioihan, pin, changesodu, changehanmuc, sodu_atm, stt):
    header = '********************'
    dem = 1
    quest = [0]
    mapin = int(input('MÃ PIN: '))
    while dem <= 3:
        if mapin == password:
            break
        if dem == 3:
            print(header.center(39))
            print('   SAI MÃ PIN QUÁ SỐ LẦN QUY ĐỊNH!!!\nTHẺ CỦA BẠN SẼ BỊ KHÓA TRONG ÍT PHÚT!!!')
            print(header.center(39))
            exit()
        else:
            mapin = int(input(f'MÃ PIN KHÔNG HỢP LỆ (CÒN {3-dem} LẦN THỬ): '))
            dem += 1
    print(header.center(27))
    print('BẠN ĐÃ ĐĂNG NHẬP THÀNH CÔNG')
    print(header.center(27))
    while True:
        if sodu_atm[0] <= 0:
            print(header.center(42))
            print('SỐ DƯ ATM ĐÃ HẾT, XIN VUI LÒNG THỬ LẠI SAU')
            print(header.center(42))
            break
        print('*1. Tra cứu tài khoản\n*2. Rút tiền\n*3. Chuyển tiền\n*4. Thay đổi mã PIN\n*0. Thoát')
        chucnang = int(input('CHỌN CHỨC NĂNG BẠN MUỐN SỬ DỤNG: '))
        if chucnang == 1:
            chucnang1(header, tk, tien, gioihan)
            question(header, quest)
            if quest[0] == 1:
                print(header.center(43))
                print('BẠN SẼ ĐƯỢC CHUYỂN HƯỚNG ĐẾN MÀN HÌNH CHÍNH')
                print(header.center(43))
            elif quest[0] == 2:
                print(header.center(27))
                print('BẠN ĐÃ ĐĂNG XUẤT THÀNH CÔNG')
                print(header.center(27))
                break
        elif chucnang == 2:
            chucnang2(header, tk, tien, gioihan, changehanmuc, changesodu, sodu_atm, stt)
            question(header, quest)
            if quest[0] == 1:
                print(header.center(43))
                print('BẠN SẼ ĐƯỢC CHUYỂN HƯỚNG ĐẾN MÀN HÌNH CHÍNH')
                print(header.center(43))
            elif quest[0] == 2:
                print(header.center(27))
                print('BẠN ĐÃ ĐĂNG XUẤT THÀNH CÔNG')
                print(header.center(27))
                break
        elif chucnang == 3:
            chucnang3(header, tien, gioihan, changehanmuc, changesodu, sodu_atm, stt)
            question(header, quest)
            if quest[0] == 1:
                print(header.center(43))
                print('BẠN SẼ ĐƯỢC CHUYỂN HƯỚNG ĐẾN MÀN HÌNH CHÍNH')
                print(header.center(43))
            elif quest[0] == 2:
                print(header.center(27))
                print('BẠN ĐÃ ĐĂNG XUẤT THÀNH CÔNG')
                print(header.center(27))
                break
        elif chucnang == 4:
            chucnang4(header, pin, stt)
            break
        elif chucnang == 0:
            print(header.center(27))
            print('BẠN ĐÃ ĐĂNG XUẤT THÀNH CÔNG')
            print(header.center(27))
            break
        else:
            print(header.center(44))
            print('CHỨC NĂNG KHÔNG HỢP LỆ, XIN VUI LÒNG THỬ LẠI')
            print(header.center(44))


def chucnang1(header1, tk1, tien1, gioihan1):
    print(header1.center(27))
    print(f'CHỦ THẺ: {tk1} \nSỐ DƯ: {tien1} VNĐ \nHẠN MỨC GIAO DỊCH: {gioihan1} VNĐ')
    print(header1.center(27))


def chucnang2(header2, tk2,  tien2, gioihan2, changehanmuc2, changesodu2, sodu_atm2, stt2):
    while True:
        if gioihan2 == 0:
            print(header2.center(43))
            print('HẠN MỨC GIAO DỊCH TRONG NGÀY CỦA BẠN ĐÃ HẾT')
            print(header2.center(43))
            break
        else:
            ruttien = int(input('NHẬP SỐ TIỀN CẦN RÚT: '))
            if ruttien <= 0:
                print(header2.center(42))
                print('SỐ TIỀN KHÔNG HỢP LỆ, XIN VUI LÒNG THỬ LẠI')
                print(header2.center(42))
            elif ruttien > sodu_atm2[0]:
                print(header2.center(60))
                print('ATM KHÔNG ĐỦ SỐ DƯ THỰC HIỆN GIAO DỊCH, XIN VUI LÒNG THỬ LẠI')
                print(header2.center(60))
            elif ruttien <= tien2:
                if gioihan2 < ruttien:
                    print(header2.center(67))
                    print('SỐ TIỀN VƯỢT QUÁ HẠN MỨC GIAO DỊCH TRONG NGÀY, XIN VUI LÒNG THỬ LẠI')
                    print(header2.center(67))
                else:
                    if ruttien % 50000 == 0:
                        tien2 = tien2 - ruttien
                        changesodu2[stt2] = tien2
                        sodu_atm2[0] -= ruttien
                        gioihan2 = gioihan2 - ruttien
                        changehanmuc2[stt2] = gioihan2
                        print('BẠN CÓ MUỐN NHẬN HÓA ĐƠN KHÔNG?\n*1. Có\n*2. Không')
                        while True:
                            bienlai = int(input('Chọn: '))
                            if bienlai == 1:
                                print(header2.center(27))
                                print(f'CHỦ THẺ: {tk2}\nSỐ TIỀN ĐÃ RÚT: {ruttien} VNĐ\nSỐ DƯ: {tien2} VNĐ')
                                print(header2.center(27))
                                break
                            elif bienlai == 2:
                                print(header2.center(48))
                                print('GIAO DỊCH HOÀN THÀNH, XIN VUI LÒNG ĐỢI NHẬN TIỀN')
                                print(header2.center(48))
                                break
                            else:
                                print(header2.center(44))
                                print('CHỨC NĂNG KHÔNG HỢP LỆ, XIN VUI LÒNG THỬ LẠI')
                                print(header2.center(44))
                    else:
                        print(header2.center(68))
                        print('SỐ TIỀN GIAO DỊCH PHẢI LÀ BỘI SỐ CỦA 50000 VNĐ, XIN VUI LÒNG THỬ LẠI')
                        print(header2.center(68))
            else:
                print(header2.center(36))
                print('SỐ DƯ KHÔNG ĐỦ, XIN VUI LÒNG THỬ LẠI')
                print(header2.center(36))
        break


def chucnang3(header3, tien3, gioihan3, changehanmuc3, changesodu3, sodu_atm3, stt3):
    while True:
        if gioihan3 == 0:
            print(header3.center(43))
            print('HẠN MỨC GIAO DỊCH TRONG NGÀY CỦA BẠN ĐÃ HẾT')
            print(header3.center(43))
            break
        else:
            stk = int(input('NHẬP SỐ TÀI KHOẢN BẠN MUỐN CHUYỂN TIỀN: '))
            chuyentien = int(input('NHẬP SỐ TIỀN CẦN CHUYỂN: '))
            if chuyentien <= 0:
                print(header3.center(42))
                print('SỐ TIỀN KHÔNG HỢP LỆ, XIN VUI LÒNG THỬ LẠI')
                print(header3.center(42))
            elif chuyentien > sodu_atm3[0]:
                print(header3.center(60))
                print('ATM KHÔNG ĐỦ SỐ DƯ THỰC HIỆN GIAO DỊCH, XIN VUI LÒNG THỬ LẠI')
                print(header3.center(60))
            elif chuyentien <= tien3:
                if gioihan3 < chuyentien:
                    print(header3.center(67))
                    print('SỐ TIỀN VƯỢT QUÁ HẠN MỨC GIAO DỊCH TRONG NGÀY, XIN VUI LÒNG THỬ LẠI')
                    print(header3.center(67))
                else:
                    if chuyentien % 50000 == 0:
                        tien3 = tien3 - chuyentien
                        changesodu3[stt3] = tien3
                        sodu_atm3[0] -= chuyentien
                        gioihan3 = gioihan3 - chuyentien
                        changehanmuc3[stt3] = gioihan3
                        print('BẠN CÓ MUỐN NHẬN HÓA ĐƠN KHÔNG?\n*1. Có\n*2. Không')
                        while True:
                            bienlai = int(input('Chọn: '))
                            if bienlai == 1:
                                print(header3.center(27))
                                print(f'SỐ TÀI KHOẢN NGƯỜI NHẬN: {stk}\nSỐ TIỀN ĐÃ CHUYỂN: {chuyentien} VNĐ\nSỐ DƯ: {tien3} VNĐ')
                                print(header3.center(27))
                                break
                            elif bienlai == 2:
                                print(header3.center(20))
                                print('GIAO DỊCH HOÀN THÀNH')
                                print(header3.center(20))
                                break
                            else:
                                print(header3.center(44))
                                print('CHỨC NĂNG KHÔNG HỢP LỆ, XIN VUI LÒNG THỬ LẠI')
                                print(header3.center(44))
                    else:
                        print(header3.center(68))
                        print('SỐ TIỀN GIAO DỊCH PHẢI LÀ BỘI SỐ CỦA 50000 VNĐ, XIN VUI LÒNG THỬ LẠI')
                        print(header3.center(68))
            else:
                print(header3.center(36))
                print('SỐ DƯ KHÔNG ĐỦ, XIN VUI LÒNG THỬ LẠI')
                print(header3.center(36))
        break


def chucnang4(header4, pin4, stt4):
    while True:
        oldpin = int(input('NHẬP MÃ PIN CŨ: '))
        if oldpin == pin4[stt4]:
            newpin = int(input('NHẬP MÃ PIN MỚI: '))
            while True:
                newpin1 = int(input('NHẬP LẠI MÃ PIN MỚI: '))
                if newpin == newpin1:
                    pin4[stt4] = newpin
                    print(header4.center(80))
                    print('BẠN ĐÃ THAY ĐỔI THÀNH CÔNG MÃ PIN, XIN VUI LÒNG ĐĂNG NHẬP LẠI ĐỂ SỬ DỤNG DỊCH VỤ')
                    print(header4.center(80))
                    break
                else:
                    print(header4.center(49))
                    print('MÃ PIN MỚI KHÔNG TRÙNG KHỚP, XIN VUI LÒNG THỬ LẠI')
                    print(header4.center(49))
            break
        else:
            print(header4.center(32))
            print('SAI MÃ PIN, XIN VUI LÒNG THỬ LẠI')
            print(header4.center(32))


def question(header, changequest):
    print('BẠN CÓ MUỐN TIẾP TỤC SỬ DỤNG DỊCH VỤ KHÔNG?\n*1. Có\n*2. Không')
    while True:
        q = int(input('Chọn: '))
        if q == 1:
            changequest[0] = 1
            break
        elif q == 2:
            changequest[0] = 2
            break
        else:
            print(header.center(44))
            print('CHỨC NĂNG KHÔNG HỢP LỆ, XIN VUI LÒNG THỬ LẠI')
            print(header.center(44))

def atm(tk, password, pin, changesodu, changehanmuc, sodu_atm, stt):
    header = '***************'
    dem = 1
    quest = [0]
    mapin = input('MÃ PIN (CÒN 3 LẦN THỬ): ')
    while dem <= 3:
        if mapin == str(password):
            break
        if dem == 3:
            print(header.center(39))
            print('   SAI MÃ PIN QUÁ SỐ LẦN QUY ĐỊNH!!!\nTHẺ CỦA BẠN SẼ BỊ KHÓA TRONG ÍT PHÚT!!!')
            print(header.center(39))
            exit()
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
        elif chucnang == '2':
            if sodu_atm[0] <= 0:
                break
            else:
                chucnang2(header, tk, changesodu[stt], changehanmuc[stt], changehanmuc, changesodu, sodu_atm, stt)
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
        elif chucnang == '3':
            if sodu_atm[0] <= 0:
                break
            else:
                chucnang3(header, changesodu[stt], changehanmuc[stt], changehanmuc, changesodu, sodu_atm, stt)
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
        elif chucnang == '4':
            chucnang4(header, pin, stt)
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
        elif chucnang == '0':
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
            print(header2.center(21))
            print('     [*0. Thoát]')
            ruttien = input('NHẬP SỐ TIỀN CẦN RÚT: ')
            if int(ruttien) == 0:
                break
            if ruttien.isdigit():
                if int(ruttien) > sodu_atm2[0]:
                    print('ATM KHÔNG ĐỦ SỐ DƯ THỰC HIỆN GIAO DỊCH, XIN VUI LÒNG THỬ LẠI!!!')
                    continue
                elif int(ruttien) <= tien2:
                    if gioihan2 < int(ruttien):
                        print('SỐ TIỀN VƯỢT QUÁ HẠN MỨC GIAO DỊCH TRONG NGÀY, XIN VUI LÒNG THỬ LẠI!!!')
                        continue
                    else:
                        if int(ruttien) % 50000 == 0:
                            tien2 = tien2 - int(ruttien)
                            changesodu2[stt2] = tien2
                            sodu_atm2[0] -= int(ruttien)
                            gioihan2 = gioihan2 - int(ruttien)
                            changehanmuc2[stt2] = gioihan2
                            print('BẠN CÓ MUỐN NHẬN HÓA ĐƠN KHÔNG?\n*1. Có\n*2. Không')
                            while True:
                                bienlai = input('Chọn: ')
                                if bienlai == '1':
                                    print(header2.center(27))
                                    print(f'CHỦ THẺ: {tk2}\nSỐ TIỀN ĐÃ RÚT: {int(ruttien)} VNĐ\nSỐ DƯ: {tien2} VNĐ')
                                    print(header2.center(27))
                                    break
                                elif bienlai == '2':
                                    print(header2.center(48))
                                    print('GIAO DỊCH HOÀN THÀNH, XIN VUI LÒNG ĐỢI NHẬN TIỀN')
                                    print(header2.center(48))
                                    break
                                else:
                                    print(header2.center(44))
                                    print('CHỨC NĂNG KHÔNG HỢP LỆ, XIN VUI LÒNG THỬ LẠI')
                                    print(header2.center(44))
                        else:
                            print('SỐ TIỀN GIAO DỊCH PHẢI LÀ BỘI SỐ CỦA 50000 VNĐ, XIN VUI LÒNG THỬ LẠI!!!')
                            continue
                else:
                    print('SỐ DƯ KHÔNG ĐỦ, XIN VUI LÒNG THỬ LẠI!!!')
                    continue
            else:
                print('SỐ TIỀN KHÔNG HỢP LỆ, XIN VUI LÒNG THỬ LẠI!!!')
                continue
        break


def chucnang3(header3, tien3, gioihan3, changehanmuc3, changesodu3, sodu_atm3, stt3):
    while True:
        if gioihan3 == 0:
            print(header3.center(43))
            print('HẠN MỨC GIAO DỊCH TRONG NGÀY CỦA BẠN ĐÃ HẾT')
            print(header3.center(43))
            break
        else:
            print(header3.center(39))
            print('              [*0. Thoát]')
            stk = input('NHẬP SỐ TÀI KHOẢN BẠN MUỐN CHUYỂN TIỀN: ')
            if int(stk) == 0:
                break
            if stk.isdigit():
                chuyentien = input('NHẬP SỐ TIỀN CẦN CHUYỂN: ')
                if int(chuyentien) == 0:
                    break
                if chuyentien.isdigit():
                    if int(chuyentien) > sodu_atm3[0]:
                        print('ATM KHÔNG ĐỦ SỐ DƯ THỰC HIỆN GIAO DỊCH, XIN VUI LÒNG THỬ LẠI!!!')
                        continue
                    elif int(chuyentien) <= tien3:
                        if gioihan3 < int(chuyentien):
                            print('SỐ TIỀN VƯỢT QUÁ HẠN MỨC GIAO DỊCH TRONG NGÀY, XIN VUI LÒNG THỬ LẠI!!!')
                            continue
                        else:
                            if int(chuyentien) % 50000 == 0:
                                tien3 = tien3 - int(chuyentien)
                                changesodu3[stt3] = tien3
                                sodu_atm3[0] -= int(chuyentien)
                                gioihan3 = gioihan3 - int(chuyentien)
                                changehanmuc3[stt3] = gioihan3
                                print('BẠN CÓ MUỐN NHẬN HÓA ĐƠN KHÔNG?\n*1. Có\n*2. Không')
                                while True:
                                    bienlai = input('Chọn: ')
                                    if bienlai == '1':
                                        print(header3.center(27))
                                        print(f'SỐ TÀI KHOẢN NGƯỜI NHẬN: {stk}\nSỐ TIỀN ĐÃ CHUYỂN: {int(chuyentien)} VNĐ\nSỐ DƯ: {tien3} VNĐ')
                                        print(header3.center(27))
                                        break
                                    elif bienlai == '2':
                                        print(header3.center(20))
                                        print('GIAO DỊCH HOÀN THÀNH')
                                        print(header3.center(20))
                                        break
                                    else:
                                        print(header3.center(44))
                                        print('CHỨC NĂNG KHÔNG HỢP LỆ, XIN VUI LÒNG THỬ LẠI')
                                        print(header3.center(44))
                            else:
                                print('SỐ TIỀN GIAO DỊCH PHẢI LÀ BỘI SỐ CỦA 50000 VNĐ, XIN VUI LÒNG THỬ LẠI!!!')
                                continue
                    else:
                        print('SỐ DƯ KHÔNG ĐỦ, XIN VUI LÒNG THỬ LẠI!!!')
                        continue
                else:
                    print('SỐ TIỀN KHÔNG HỢP LỆ, XIN VUI LÒNG THỬ LẠI!!!')
                    continue
            else:
                print('SỐ TÀI KHOẢN KHÔNG HỢP LỆ, XIN VUI LÒNG THỬ LẠI!!!')
                continue
        break


def chucnang4(header4, pin4, stt4):
    print(header4.center(15))
    print('  [*0. Thoát]')
    while True:
        oldpin = input('NHẬP MÃ PIN CŨ: ')
        if oldpin.isdigit():
            if int(oldpin) == 0:
                break
            if int(oldpin) == pin4[stt4]:
                while True:
                    newpin = input('NHẬP MÃ PIN MỚI: ')
                    if newpin.isdigit():
                        if int(newpin) == 0:
                            break
                        while True:
                            newpin1 = input('NHẬP LẠI MÃ PIN MỚI: ')
                            if newpin1.isdigit():
                                if int(newpin1) == 0:
                                    break
                                if int(newpin) == int(newpin1):
                                    pin4[stt4] = int(newpin)
                                    print(header4.center(33))
                                    print('BẠN ĐÃ THAY ĐỔI THÀNH CÔNG MÃ PIN')
                                    print(header4.center(33))
                                    break
                                else:
                                    print(header4.center(49))
                                    print('MÃ PIN MỚI KHÔNG TRÙNG KHỚP, XIN VUI LÒNG THỬ LẠI')
                                    print(header4.center(49))
                                    continue
                            else:
                                print(header4.center(43))
                                print('MÃ PIN PHẢI LÀ CHỮ SỐ, XIN VUI LÒNG THỬ LẠI')
                                print(header4.center(43))
                                continue
                        break
                    else:
                        print(header4.center(43))
                        print('MÃ PIN PHẢI LÀ CHỮ SỐ, XIN VUI LÒNG THỬ LẠI')
                        print(header4.center(43))
                        continue
                break
            else:
                print(header4.center(32))
                print('SAI MÃ PIN, XIN VUI LÒNG THỬ LẠI')
                print(header4.center(32))
        else:
            print(header4.center(43))
            print('MÃ PIN PHẢI LÀ CHỮ SỐ, XIN VUI LÒNG THỬ LẠI')
            print(header4.center(43))


def question(header, changequest):
    print('BẠN CÓ MUỐN TIẾP TỤC SỬ DỤNG DỊCH VỤ KHÔNG?\n*1. Có\n*2. Không')
    while True:
        q = input('Chọn: ')
        if q == '1':
            changequest[0] = 1
            break
        elif q == '2':
            changequest[0] = 2
            break
        else:
            print(header.center(44))
            print('CHỨC NĂNG KHÔNG HỢP LỆ, XIN VUI LÒNG THỬ LẠI')
            print(header.center(44))

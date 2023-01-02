from random import randint as ran

def convert_number_to_string(num):
    if num == 1:
        return 'Cop'
    elif num == 2:
        return 'Bau'
    elif num == 3:
        return 'Ga'
    elif num == 4:
        return 'Tom'
    elif num == 5:
        return 'Ca'
    else:
        return 'Cua'

def compare_result(bet, result1, result2, result3):
    if bet == result1 or bet == result2 or bet == result3:
        return True
    return False

def input_players():
    so_nguoi = int(input('Nhap so nguoi choi: '))
    tien = [0] * so_nguoi
    for i in range(so_nguoi):
        tien[i] = int(input(f'Nhap tien cuoc cua nguoi thu {i+1}: '))
    return so_nguoi, tien

def input_bets(so_nguoi):
    cuoc = [''] * so_nguoi
    for i in range(so_nguoi):
        cuoc[i] = input(f'Moi nguoi choi {i+1} cuoc:')
    return cuoc

print('___Bau Cua___')
print('Nha cai: Nghiax Doan')
print('----------')

so_nguoi, tien = input_players()
print('----------')
print('Vay tai khoan cua cac nguoi choi la: ')
for i in range(so_nguoi):
    print(f'Nguoi {i+1} co {tien[i]} dong')
print('----------')

cuoc = input_bets(so_nguoi)
print('----------')

#Computer
xuc_xac1 = convert_number_to_string(ran(1,6))
xuc_xac2 = convert_number_to_string(ran(1,6))
xuc_xac3 = convert_number_to_string(ran(1,6))

print('Ket qua xuc xac 1: ', xuc_xac1)
print('Ket qua xuc xac 2: ', xuc_xac2)
print('Ket qua xuc xac 3: ', xuc_xac3)
print('----------')

for i in range(so_nguoi):
    if compare_result(cuoc[i], xuc_xac1, xuc_xac2, xuc_xac3):
        tien[i] += tien[i]
    else:
        tien[i] = 0
print('----------')
print('Vay tai khoan cua cac nguoi choi sau khi choi la: ')
for i in range(so_nguoi):
    print(f'Tai khoan cua nguoi choi {i+1} la: {tien[i]} dong')

from random import randint as ran
print('___Bau Cua___')
print('Nha cai: Nghiax Doan')
print('----------')
#Players
so_nguoi = int(input('Nhap so nguoi choi: '))
print('----------')
tien = [0]*so_nguoi
for i in range(so_nguoi):
    tien[i] = int(input(f'Nhap tien cuoc cua nguoi thu {i+1}: '))
print('----------')
print('Vay tai khoan cua cac nguoi choi la: ')
for i in range(so_nguoi):
    print(f'Nguoi {i+1} co {tien[i]} dong')
print('----------')
cuoc = ['']*so_nguoi
for i in range(so_nguoi):
    cuoc[i] = input(f'Moi nguoi choi {i+1} cuoc:')
print('----------')
#Computer
xuc_xac1 = ran(1,6)
xuc_xac2 = ran(1,6)
xuc_xac3 = ran(1,6)
if xuc_xac1 == 1:
    xuc_xac1 = 'Cop'
elif xuc_xac1 == 2:
    xuc_xac1 = 'Bau'
elif xuc_xac1 == 3:
    xuc_xac1 = 'Ga'
elif xuc_xac1 == 4:
    xuc_xac1 = 'Tom'
elif xuc_xac1 == 5:
    xuc_xac1 = 'Ca'
else:
    xuc_xac1 = 'Cua'

if xuc_xac2 == 1:
    xuc_xac2 = 'Cop'
elif xuc_xac2 == 2:
    xuc_xac2 = 'Bau'
elif xuc_xac2 == 3:
    xuc_xac2 = 'Ga'
elif xuc_xac2 == 4:
    xuc_xac2 = 'Tom'
elif xuc_xac2 == 5:
    xuc_xac2 = 'Ca'
else:
    xuc_xac2 = 'Cua'
    
if xuc_xac3 == 1:
    xuc_xac3 = 'Cop'
elif xuc_xac3 == 2:
    xuc_xac3 = 'Bau'
elif xuc_xac3 == 3:
    xuc_xac3 = 'Ga'
elif xuc_xac3 == 4:
    xuc_xac3 = 'Tom'
elif xuc_xac3 == 5:
    xuc_xac3 = 'Ca'
else:
    xuc_xac3 = 'Cua'

print('Ket qua xuc xac 1: ',xuc_xac1)
print('Ket qua xuc xac 2: ',xuc_xac2)
print('Ket qua xuc xac 3: ',xuc_xac3)
print('----------')
#Compare
for i in range(so_nguoi):
    if cuoc[i] == 'Cop':
        if xuc_xac1 == 'Cop':
            tien[i]+=tien[i]
        elif xuc_xac2 == 'Cop':
            tien[i]+=tien[i]
        elif xuc_xac3 == 'Cop':
            tien[i]+=tien[i]
        else:
            tien[i] = 0
    elif cuoc[i] == 'Bau':
        if xuc_xac1 == 'Bau':
            tien[i]+=tien[i]
        elif xuc_xac2 == 'Bau':
            tien[i]+=tien[i]
        elif xuc_xac3 == 'Bau':
            tien[i]+=tien[i]
        else:
            tien[i] = 0
    elif cuoc[i] == 'Ga':
        if xuc_xac1 == 'Ga':
            tien[i]+=tien[i]
        elif xuc_xac2 == 'Ga':
            tien[i]+=tien[i]
        elif xuc_xac3 == 'Ga':
            tien[i]+=tien[i]
        else:
            tien[i] = 0
    elif cuoc[i] == 'Tom':
        if xuc_xac1 == 'Tom':
            tien[i]+=tien[i]
        elif xuc_xac2 == 'Tom':
            tien[i]+=tien[i]
        elif xuc_xac3 == 'Tom':
            tien[i]+=tien[i]
        else:
            tien[i] = 0
    elif cuoc[i] == 'Ca':
        if xuc_xac1 == 'Ca':
            tien[i]+=tien[i]
        elif xuc_xac2 == 'Ca':
            tien[i]+=tien[i]
        elif xuc_xac3 == 'Ca':
            tien[i]+=tien[i]
        else:
            tien[i] = 0
    elif cuoc[i] == 'Cua':
        if xuc_xac1 == 'Cua':
            tien[i]+=tien[i]
        elif xuc_xac2 == 'Cua':
            tien[i]+=tien[i]
        elif xuc_xac3 == 'Cua':
            tien[i]+=tien[i]
        else:
            tien[i] = 0
print('Sau khi so sanh, tai khoan cua cac bao thu la:')
for i in range(so_nguoi):
    print(f'Tai khoan cua nguoi choi {i+1} la: {tien[i]} dong')

V = ['S', 'A', 'B', 'C', 'D', 'E', 'F', 'H', 'G']
E = [[0, 1, 1, 1, 0, 0, 0, 0, 0],
     [1, 0, 1, 0, 1, 0, 0, 0, 0],
     [1, 1, 0, 1, 1, 0, 1, 0, 1],
     [1, 0, 1, 0, 0, 0, 1, 0, 0],
     [0, 1, 1, 0, 1, 0, 0, 0, 0],
     [0, 0, 0, 0, 1, 0, 1, 0, 1],
     [0, 0, 1, 1, 0, 1, 0, 1, 0],
     [0, 0, 0, 0, 0, 0, 1, 0, 1],
     [0, 0, 1, 0, 0, 1, 0, 1, 0]]
# Trả lời: Dán code vào bên dưới
# E là ma trận MxM với M là số đỉnh, có thứ tự tương ứng với thứ tự các đỉnh trong V. Với mỗi E[x,y]
# là đường đi từ đỉnh thứ x đến đỉnh thứ y, bằng 1 nếu có đường đi và bằng 0 nếu không có đường đi
# hoặc đi đến chính nó.
# ví dụ E[3,6] = 1 là đường đi từ đỉnh thứ 3(‘C’) đến đỉnh thứ 6(‘F’) có thể đi được,
# E[0,0] là đường đi từ đỉnh thứ 0(‘S’) đến chính nó là không thể đi đ


# (3 điểm) Hãy viết chương trình sử dụng thuật toán tìm kiếm theo chiều sâu (DFS) để tìm đường đi từ
# đỉnh “S” đến đỉnh “H” trong đồ thị được biểu diễn ở câu a). Trong chương trình, hãy in ra thứ tự đỉnh
# khám phá trong quá trình tìm kiếm. Nếu không tìm thấy thì in “Khong tim thay duong di”


start = 0
open = [start]
close = []
success = False
count = 0
dinhcha = {}
while len(open) >= 1:
    count += 1
    O = open.pop(0)
    close.append(O)
    if O == 8:
        success = True
        break
    khampha = []
    for y in range(0, 9):
        if E[O][y] == 0:
            continue
        if y in close or y in open:
            continue
        khampha.append(y)
    dinh = []
    for i in khampha:
        dinh.append(V[i])
        dinhcon = i
        open.insert(0, dinhcon)
        dinhcha[dinhcon] = O
    print("Kham pha ra dinh: ", dinh)
if success == False:
    print("Khong tim thay duong di")
else:
    truyvet = [V[O]]
    while dinhcha.get(O) != None:
        O = dinhcha.get(O)
        truyvet.append(V[O])
    truyvet.reverse()
    print("Duong di: ")
    print(*truyvet)

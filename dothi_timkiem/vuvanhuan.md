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

Trả lời: Dán code vào bên dưới
 E là ma trận MxM với M là số đỉnh, có thứ tự tương ứng với thứ tự các đỉnh trong V. Với mỗi E[x,y]

 là đường đi từ đỉnh thứ x đến đỉnh thứ y, bằng 1 nếu có đường đi và bằng 0 nếu không có đường đi

 hoặc đi đến chính nó.

 ví dụ E[3,6] = 1 là đường đi từ đỉnh thứ 3(‘C’) đến đỉnh thứ 6(‘F’) có thể đi được,

 E[0,0] là đường đi từ đỉnh thứ 0(‘S’) đến chính nó là không thể đi đ
 

 (3 điểm) Hãy viết chương trình sử dụng thuật toán tìm kiếm theo chiều sâu (DFS) để tìm đường đi từ

 đỉnh “S” đến đỉnh “H” trong đồ thị được biểu diễn ở câu a). Trong chương trình, hãy in ra thứ tự đỉnh

 khám phá trong quá trình tìm kiếm. Nếu không tìm thấy thì in “Khong tim thay duong di”



Câu 3 A* :
b) (2 điểm) Hãy viết chương trình sử dụng thuật toán A* để tìm đường đi từ đỉnh “S” đến  các đỉnh có trọng 
số trên đỉnh bằng 0. Trong chương trình, hãy in ra thứ tự đỉnh khám phá trong quá trình tìm kiếm. 
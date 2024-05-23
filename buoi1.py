import re
numbers = [2, 3, 4]
print(numbers)
var = "James" * 2 * 3
print(var)


x = 36 / 4 * (3 + 2) * 4 + 2
print(x)

# sampleList = ["Jon", "Kelly", "Jessa"]
# sampleList.append(2, "Scott")

# =>append() trong Python chỉ nhận một tham số duy nhất - đối tượng cần thêm vào cuối danh sách
# sampleList.insert(2, "Scott")
# print(sampleList) : lỗi

# for x in range(0.5, 5.5, 0.5):
#   print(x) // lỗi 'float' object cannot be interpreted as an integer range() không hỗ trợ các giá trị không phải là số nguyên và cũng không hỗ trợ bước nhảy là số thập phân.


# listOne = [20, 40, 60, 80]
# listTwo = [20, 40, 60, 80]

# print(listOne == listTwo)
# print(listOne is listTwo)
# True
# True

# True
# False


# => == so sánh giá trị của hai dánh sách
# is : so sánh vị trí trong bộ nhớ của hai danh sách
class Foo:
    def printLine(self, line='Python'):
        print(line)


o1 = Foo()
o1.printLine('Java')
# in ra Java
# Ý nghĩa của hàm __init__() trong Python là gì? được gọi khi 1 object đc khởi tạo


class Point:
    def __init__(self, x=0, y=0):
        self.x = x+1
        self.y = y + 1


p1 = Point()
print(p1.x, p1.y)


# kế thừa
class Foo:
    pass


class Hoo(Foo):
    pass


# class Point:
#      def __init__(self, x = 0, y = 0):        self.x = x        self.y = y
#      def __sub__(self, other):        x = self.x + other.x        y = self.y + other.


#      x = self.x + other.x        y = self.y + other.y        return Point(x,y)

# def f(value):
#     while True:
#         value = (yield value)
# a = f(10)
# print(next(a))
# print(next(a))
# print(a.send(20)) #10 none 20

# round(4.576) : 5
# print (all([2,4,0,6]))

# print (all(3,0,4.2)) '' loi


# Output của chương trình dưới đây là gì?
# x = 50
# def func():
# global x
# print('Giá trị của x là', x)
# x = 2
# print('Giá trị của x được thay đổi thành', x)
# func()
# print('Giá trị hiện tại của x là', x)
# 50 2 2


# try: # đoạn code có thể gây ra lỗi     pass
# except (TypeError, ZeroDivisionError):
# print("Python Quiz") In ra ' Python Quiz ' nếu một trong hai ngoại lệ TypeError và ZeroDivisionError xảy ra.

# a = 5
# b= 5
# print(a is b)

# def a(a,b):
#     return a + b
# print (a(2,3))

x = 2.01
print(x * 100)


winner = None
print(winner is None)
# Hoắc so sánh khác sử dụng is not
print('True division 3/2:', 3 / 2)
print('True division -3/2:', -3 / 2)
print('Integer division 3//2:', 3 // 2)
print('Integer division -3//2:', -3 // 2)
list = ["a", "b"]
for index, value in enumerate(list):
    print(index, value)

    # String
print("""Tháp mười đẹp nhất bông sen
 Việt Nam đẹp nhất có tên Bác Hồ""")


str1 = "Python"
print(str1[:-2])  # lấy từ vị trí đầu tiên đến trước kí tự thứ 3

print('%.2f' % x)

x = 1.333355453
format_float = "{:.2f}".format(x)
print(format_float)
print(str1.replace('P', 'Ph'))


def greeter(name,
            title='Dr',
            prompt='Welcome',
            message='Live Long and Prosper'):
    """
    This function takes defines 4 parameters;
    name, title, prompt and message
    """
    print(prompt, title, name, '-', message)


greeter("Quyen")
greeter(message='We like Python', name='Lisa')
greeter('Rossie', message='We like Python')


max = 100


def print_max():
    global max
    max = max + 1
    print(max)


print_max()
print(max)


def outer():
    title = 'original title'

    def inner():
        nonlocal title  # giá trị ngoài hàm
        print('inner:', title)
        title = 'another title'
        print('inner:', title)
    inner()
    print('outer:', title)


outer()

text1 = 'john williams'
pattern = r'[Jj]ohn'
if re.search(pattern, text1):
    print('Match has been found')

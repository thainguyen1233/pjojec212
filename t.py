#a = float(input('nhập số của bạn :'))
#print('kết quả',a)
#a=eval(input('nhập một số thứ nhất :'))
#b= eval(input('nhập vào một số thứ 2:'))
#print("tổng của{} là{}".format(a,b,a+b))

#r=float(input('nhập số:'))
#s=3.14*r*r
#print('diện tích là .%2f',s)
'''
kiểu số thực và số nguyên :
số nguyên bao gồm số nguyên dương và số nguyên âm 
a=4 # gán bầng cho biến a có giá trị là 4
số thực :f=1.23 có cả số nguyên và số không nguyên và số 0 
int
float 
double
long 
char
type : kiểm tra dữ liệu của một đối tượng 
1.8.1.3 các toán tử cơ bản với kiểu dữ liệu số:
thư viện math 
from math import*: thư viện toán học 
trunc(x): trả về một số nguyên là phần nguyên của x
floor(X): trả về một số nguvyeen được làm tròn từ số x , kết quả luôn nhỏ hơn hoặc bằng x
celi(x): trả về kết quả một số nguyên được làm tròn từ số x , kết quả luôn lớn hơn hoặc bằng x
fabs(x): trả về mooht số thực có giá trị tuyệt x:
sqrt(X): trả về căn bặc 2 của x:
gcd(x,y): trả về một số nguyên là ước số chung lớn nhaastx x và y 
exp(X): trả về kết quả của e^X
log(x): trả về két quả logarit x, với x>0
log10(x): tương tự như hàm log(), nhưng là dạng logarit cơ số 10
pow(X,y): trả về kết quả cao nhất của phép x^y
round(x,n) làm tròn chữ số x với n chữ số sau dấu chấm thập phân 
cos(X):trả về cos x với kết quả theo radian 
sin(x): trả về sin x với kết quả theo radian 
1.8.2 kiểu chuỗi 
- dữ liệu kiểu chuỗi 
vd:
print("hello world!")
print('hello world!')
-biến chuỗi :
str1="xin chào bạn!"
print(str1)

- chuỗi đa dòng:
ta có thể gán một chuỗi nhiều dòng cho 1 biến  bằng cách sử dụng  3 dấu ngoặc kép hoặc 3 dấu nháy đơn 
-các kí tự đặc biệt:
\n: ký tự xuống dòng 
/t" ký tự tab 
\r: về đầu dòng 
\s khoảng trắng 
\r\n: xuống dòng + quay đầu dòng 
s="khoa công nghệ thông \n tin đại học mỏ địa chất "
print(S,end="")

-truy cập các phần tử trong chuỗi :
 -các chuỗi trong python là mảng các byte đại diện cho các ký tự unicode
- tuy nhiên , python không có kiểu dữ liệu ký tự , một ký tự đơn giản chỉ là một chuỗi có độ dài bằng 1
-dấu ngoặc [] có thể được sử dung để truy cập các phần tử của chuỗi 
vd:



ký tự đàu tiên có chỉ số là 0
chỉ định chỉ mục bắt đầu và chỉ mục kết thúc được phân tách bằng dấu 2 chấm , để trả về một phần của chuỗi 
#str_1="hello world!"
#print(str_1[2])
#truy cập chuỗi bằng chỉ mục âm 
sử dụng các chỉ mục âm để lấy ra chuỗi con bắt đầu từ cuối chuỗi 
-một số thao tác cơ bản với chuỗi :
toán tử +
hàm len(...)
a = " hello world"
print(len(a))
-dùng để nối 2 chuỗi lại với nhau
cú pháp :
 a + b(với a và b là chuỗi )
 s="hello world"
 s+='python"#tương tự câu lệnh  s= s+'python"
 print(s)
toán tử in :
khi sử dụng toán tử này , bạn chỉ có thể nhận được 1 trong 2 đáp án đó là true hoặc false
cú pháp :
s in A ( với s và A là chuỗi )
kết quả sẽ là true nếu chuỗi s xuất hiện trong chuỗi A. ngược lại sẽ là False


'''
#a = 7.3
#print(type(a))
#from math import*
#print(help(math))
#from math import*
#print(trunc(3.9))
#print(sqrt(4))
#print(fabs(-3))
#print(gcd(6,4))

#str_1="""ví dụ nhập chuỗi nhiều dòng trong python 
    #   đây là dòng thứ 2 
     #  đây là dòng thứ 3
      #  đây là dòng thư 4
     #print(str_1)
#str_1= "helllo world"
#print(str_1[:5])
#print(str_1[0:])
#print(str_1[:])
#print(str_1[1:4])
#rint(str_1[0:2])
#str_1 ="hello worl"
#print(str_1[-1])
#print(str_1[-5:-2])
a = " hello world"
print( len(a))
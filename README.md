# FACIAL RECOGNITION ATTENDANCE SYSTEM


## 1) Cài đặt XAMPP MySQL
> https://www.apachefriends.org/download.html

-Sau khi đã cài đặt xong,Mở XAMPP lên .Ở cột MySQL và Apeche chọn Start như hình :

![Image](https://github.com/user-attachments/assets/9418c017-79e0-41ba-a93f-9573bab24345)

-Nếu không Start đc Apeche đổi cổng thành 8080.

-MYSQL để mặc định ,không cần chỉnh sửa gì. 

-Sau khi đã Start thành công Apache và MySQL mở PHPMyAdmin bằng đường dẫn: 

>http://localhost/phpmyadmin/

nếu đổi port Apeche sang 8080 thì truy cập:

>http://localhost:8080/phpmyadmin/

## 2) Tạo CSDL

+ Sau khi vào trang chủ phpMyAdmin chọn "New"

![Image](https://github.com/user-attachments/assets/40022d21-494d-4985-8235-d29e9f206b33)

+ Nhập database name: face_recognizer.sql . Click chọn "Create"

![Image](https://github.com/user-attachments/assets/3b1cab84-3aeb-4958-b472-4aeccaca4f32)

+ Chọn database mới tạo và nhấn Import để thêm file sql đã download về
 
![Image](https://github.com/user-attachments/assets/b57c2646-4620-4597-8f7a-99cfb7e705e2)

+ Click Chọn file và chọn file ".sql" trong source code

## 3) Cài đặt Python (khuyên dùng bản 3.6.5) và Pycharm(Hoặc IDE nào có hỗ trợ Python)

Cài đặt các thư viện cần thiết để chạy App
  
+ Mở thư mục chương trình bằng Pycharm
+ Cài đặt các thư viện sau bằng cách mở Terminal và nhập:
    >pip install -r requirements.txt

    hoặc 
    
    >pip + tên thư viện
  
*** Nếu thiếu thư viện nào bạn cài thêm nhé.

## 4) Sau khi đã cài đặt xong Run file "login.py" để chạy chương trình
	
Bạn có thể đăng nhập bằng tài khoản Admin bằng cách chọn đăng nhập bằng Admin
	
    Username:admin 
    Password:123456
	
## 5) Hướng dẫn sử dụng
Bạn có thể đăng nhập phần mềm bằng tài khoản admin hoặc tài khoản giáo viên.

#### * Admin: cho phép sử dụng tất cả các chức năng của phần mềm.

- Sinh viên: Thêm, sửa ,xóa thông tin sinh viên,Chụp ảnh sinh viên bằng Webcam.

    ###### (Sau khi đã chụp ảnh sinh viên xong. Chọn Training Data để Train model nhận dạng sinh viên.)

- Giáo viên: Thêm, sửa ,xóa thông tin giáo viên.


- Môn học: Quản lý thông tin môn học,Đăng ký môn học cho sinh viên,Thêm môn học cho giảng viên.
    ###### (Phải thêm môn học cho sinh viên và giảng viên để điểm danh)

- Buổi học: Thêm,sửa,xóa thông tin buổi học của từng môn học.


- Xem ảnh:Xem tất cả các ảnh của sinh viên đã chụp trong máy.


- Nhận dạng: Đối với Admin, cho phép điểm danh tất cả các buổi học trong ngày của tất cả các giáo viên
	
  + Chọn "Moonhoc/Id" Bài học có trong ngày sau đó chọn Mở Camera để bắt đầu điểm dan

  + Hệ thống sẽ thông báo ra màn hình những sinh viên điểm danh thành công và lưu lên database.

  + Những sinh viên chưa có dữ liệu khuôn mặt hoặc không có trong tiết học sẽ thông báo lên màn hình.

  + Kiểm tra thời gian vào,ra lớp và so sánh với thời gian bắt đầu/kết thúc của tiết học qua đó lưu trạng thái điểm danh (Đi muộn,vắng,Có mặt) lên DB


- Điểm danh: Cho phép xem thông tin tất cả các bản điểm danh đc lưu trữ trên DB


-  Thống kê: Thống kê các sinh viên đi muộn, trốn về sớm  hoặc không điểm danh

#### * Giáo viên: Cho phếp sử dụng chức năng: Sinh viên, Thống kê, nhận dạng

- Nhận dạng: cho phép điểm danh tất cả các buổi học trong ngày mà giảng viên được sắp xếp dạy

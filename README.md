# BaiTieuLuan_python
##link youtube bài thuyết trình: https://youtu.be/4FV5y877dGQ?si=sswoad5LfimEarcs
### ĐỀ BÀI
Đầu bài:
Triển khai game Tic-Tac-Toe (Chapter 6) với giao diện tkinter: bảng 3×3 và thông báo kết quả.
Đầu vào – đầu ra:
Đầu vào: Click vào ô vuông (Button).
Đầu ra: X hoặc O hiện lên, hiển thị người thắng hoặc hoà.
Tính năng yêu cầu:
Theo dõi turn, legal_moves, winner.
Reset game.
Tắt nút sau khi click.
Kiểm tra & kết quả mẫu:
Dàn xếp thắng hàng ngang → Hiển thị “X thắng!”
Các bước triển khai:
Class TTTBoard chứa logic.
Tạo 9 nút Button trên grid.
Gắn event click: gọi make_move(), cập nhật text nút.
Kiểm tra thắng/thua sau mỗi nước.


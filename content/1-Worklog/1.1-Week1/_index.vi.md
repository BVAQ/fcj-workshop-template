---
title: "Worklog Tuần 1"
date: 2026-06-15
weight: 1
chapter: false
pre: " <b> 1.1. </b> "
---

### Mục tiêu:

* Kết nối và làm quen với các thành viên của First Cloud AI Journey (FCAJ).
* Hiểu các dịch vụ cơ bản của AWS và điều hướng AWS Management Console & CLI.

### Nhiệm vụ:
| Ngày | Nhiệm vụ | Ngày bắt đầu | Ngày hoàn thành | Tài liệu tham khảo |
| --- | ---------------------------------------------------------------------------------------------------- | ---------- | --------------- | ----------------------------------------- |
| 1 | - Làm quen với các thành viên FCAJ.<br>- Đọc và ghi chú về nội quy, quy định của đơn vị thực tập. | 15/06/2026 | 15/06/2026 | Tài liệu Onboarding FCAJ |
| 2 | - Tìm hiểu về AWS và các nhóm dịch vụ:<br>&emsp;+ Compute<br>&emsp;+ Storage<br>&emsp;+ Networking<br>&emsp;+ Database | 16/06/2026 | 16/06/2026 | cloudjourney.awsstudygroup.com |
| 3 | - Tạo tài khoản AWS Free Tier.<br>- Tìm hiểu về AWS Console & AWS CLI.<br>- Thực hành:<br>&emsp;+ Tạo tài khoản AWS<br>&emsp;+ Cài đặt & cấu hình AWS CLI | 17/06/2026 | 17/06/2026 | cloudjourney.awsstudygroup.com |
| 4 | - Tìm hiểu EC2 cơ bản:<br>&emsp;+ Các loại instance, AMI, EBS<br>- Các phương thức kết nối SSH đến EC2.<br>- Tìm hiểu về Elastic IP. | 18/06/2026 | 18/06/2026 | cloudjourney.awsstudygroup.com |
| 5 | - Thực hành:<br>&emsp;+ Khởi chạy một EC2 instance<br>&emsp;+ Kết nối qua SSH<br>&emsp;+ Gắn một EBS volume | 19/06/2026 | 19/06/2026 | cloudjourney.awsstudygroup.com |
| 6 | - Đọc và thảo luận whitepaper thuật toán Raft.<br>- Phân tích đặc tả dự án awsplace.<br>- Khởi tạo repository: CMakeLists.txt, presets, GoogleTest. | 15/06/2026 | 15/06/2026 | Báo cáo C++ RaftDB |
| 7 | - Cài đặt CI/CD cơ bản (GitHub Actions).<br>- Thiết kế kiến trúc Network Server (epoll/kqueue).<br>- Soạn thảo PROTOCOL.md.<br>- Định nghĩa Error Codes và cơ chế Leader Redirect. | 15/06/2026 | 15/06/2026 | Báo cáo C++ RaftDB |

### Thành tựu:

* Hoàn thành xuất sắc quá trình onboarding AWS và nắm vững các khái niệm điện toán đám mây nền tảng, đặc biệt là các dịch vụ Compute, Storage, Networking và Database.
* Thiết lập thành công môi trường phát triển AWS hoàn chỉnh, bao gồm tài khoản Free Tier được cấu hình chuẩn, quyền truy cập AWS Management Console và thiết lập AWS CLI bảo mật.
* Thể hiện kỹ năng thực hành vững vàng thông qua việc khởi chạy và kết nối thành công với Amazon EC2 instance qua SSH, cũng như gắn và quản lý các EBS volumes.
* Đặt nền móng vững chắc cho dự án RaftDB C++ bằng cách xây dựng hệ thống build mạnh mẽ với CMake và Ninja, tích hợp đầy đủ các preset biên dịch (ASan, UBSan, Release, Fuzz).
* Thiết kế kiến trúc mạng ban đầu cho server tận dụng các mô hình I/O bất đồng bộ (asynchronous non-blocking) hiệu năng cao (epoll/kqueue) nhằm tối ưu hóa tốc độ xử lý.
* Soạn thảo chi tiết các đặc tả kỹ thuật, bao gồm tài liệu đặc tả Protocol cho giao tiếp nhị phân và định nghĩa trước các mã lỗi (Error Codes) cho cơ chế Leader Redirect.
* Tự động hóa quy trình phát triển bằng cách tích hợp GitHub Actions (CI/CD), đảm bảo mọi commit đều được tự động kiểm tra bản build và chạy unit tests.

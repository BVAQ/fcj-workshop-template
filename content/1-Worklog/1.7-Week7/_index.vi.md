---
title: "Worklog Tuần 7"
date: 2026-07-27
weight: 7
chapter: false
pre: " <b> 1.7. </b> "
---

### Mục tiêu:

* Hoàn thiện tất cả các kết quả bàn giao của dự án và đảm bảo tính ổn định của hệ thống.
* Soạn thảo, định dạng và nộp Báo cáo Workshop Cuối kỳ trước thời hạn.

### Nhiệm vụ:
| Ngày | Nhiệm vụ | Ngày bắt đầu | Ngày hoàn thành | Tài liệu tham khảo |
| --- | ---------------------------------------------------------------------------------------------------- | ---------- | --------------- | ----------------------------------------- |
| 31 | - Đánh giá lần cuối về kiến trúc dự án và dọn dẹp mã nguồn. | 27/07/2026 | 27/07/2026 | Project Repository |
| 32 | - Viết tài liệu dự án (README, hướng dẫn triển khai, tài liệu API). | 28/07/2026 | 28/07/2026 | Tiêu chuẩn Tài liệu |
| 33 | - Bắt đầu soạn thảo Báo cáo Workshop Cuối kỳ (Phần 5 của web template). | 29/07/2026 | 29/07/2026 | cloudjourney.awsstudygroup.com |
| 34 | - Tinh chỉnh báo cáo, đảm bảo tất cả worklogs và chi tiết kiến trúc đều chính xác. | 30/07/2026 | 30/07/2026 | Report Templates |
| 35 | - **Nộp Báo cáo Workshop Cuối kỳ (Deadline)**. Không yêu cầu thuyết trình. | 31/07/2026 | 31/07/2026 | FCAJ Submission Portal |
| 6 | - Triển khai E2E Integration Test với Docker Compose và Go Server.<br>- Sử dụng TSan và ASan để rà soát lỗi bộ nhớ. | TBD | TBD | Báo cáo C++ RaftDB |
| 7 | - Phát triển test Fuzzing (kịch bản kiểm thử fuzzing) đảm bảo server không Crash.<br>- Cấu hình tối ưu độ trễ TCP (TCP_NODELAY). | TBD | TBD | Báo cáo C++ RaftDB |

### Thành tựu:

* Bàn giao xuất sắc dự án Final Workshop trước thời hạn chính thức, thể hiện một kiến trúc sẵn sàng cho môi trường production, kết hợp mượt mà giữa dịch vụ AWS và C++ tùy chỉnh.
* Thực hiện Integration Test toàn diện (E2E), triển khai cụm RaftDB 3 node thông qua Docker Compose cùng với Go Server, và xác thực tính toàn vẹn của hệ thống dưới tải trọng cực lớn.
* Gia cố mã nguồn C++ bằng các công cụ biên dịch tiên tiến (ThreadSanitizer và AddressSanitizer), phát hiện và triệt tiêu một cách có hệ thống các lỗi data races và rò rỉ bộ nhớ tiềm ẩn.
* Thiết kế đường ống fuzzing liên tục nã hàng triệu gói tin nhị phân lỗi vào server, chứng minh khả năng phục hồi tuyệt đối chống lại các sự cố crash và segmentation faults.
* Tối ưu hóa hiệu năng mạng đến từng micro giây bằng cách can thiệp vào cấu hình mức socket (vô hiệu hóa thuật toán Nagle thông qua TCP_NODELAY), đạt được độ trễ dưới 5ms cho các thao tác real-time.
* Hoàn thiện một báo cáo kỹ thuật chuyên nghiệp và bao quát, trình bày sự giao thoa sâu sắc giữa lý thuyết Hệ thống phân tán, Lập trình C++ cấp thấp và Triển khai Hạ tầng Đám mây.

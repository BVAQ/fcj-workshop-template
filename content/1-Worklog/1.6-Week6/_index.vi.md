---
title: "Worklog Tuần 6"
date: 2026-07-20
weight: 6
chapter: false
pre: " <b> 1.6. </b> "
---

### Mục tiêu:

* Phát triển và triển khai các thành phần frontend.
* Tích hợp frontend với backend và kiểm thử toàn bộ luồng ứng dụng.

### Nhiệm vụ:
| Ngày | Nhiệm vụ | Ngày bắt đầu | Ngày hoàn thành | Tài liệu tham khảo |
| --- | ---------------------------------------------------------------------------------------------------- | ---------- | --------------- | ----------------------------------------- |
| 26 | - Phát triển các thành phần giao diện người dùng (UI) frontend. | 20/07/2026 | 20/07/2026 | Bản nháp UI/UX |
| 27 | - Cấu hình S3 bucket cho static website hosting và phân phối bằng CloudFront. | 21/07/2026 | 21/07/2026 | Tài liệu AWS CloudFront |
| 28 | - Kết nối ứng dụng frontend với API Gateway/Backend. | 22/07/2026 | 22/07/2026 | Đặc tả API |
| 29 | - Thực hiện kiểm thử End-to-End (E2E) và sửa lỗi. | 23/07/2026 | 23/07/2026 | Testing Frameworks |
| 30 | - Cấu hình Amazon CloudWatch để giám sát và thu thập log. | 24/07/2026 | 24/07/2026 | Tài liệu AWS CloudWatch |
| 6 | - Hiện thực hệ thống Snapshot (Copy-On-Write hoặc Stop-The-World).<br>- Đồng bộ Snapshot qua mạng (InstallSnapshot RPC). | TBD | TBD | Báo cáo C++ RaftDB |
| 7 | - Tích hợp cơ chế khôi phục (Restore): Nạp Snapshot vào RAM và replay WAL. | TBD | TBD | Báo cáo C++ RaftDB |

### Thành tựu:

* Thiết kế và hiện thực hệ thống Snapshot tinh vi cho RaftDB, hỗ trợ dump bộ nhớ tốc độ cao thông qua kỹ thuật Copy-On-Write nhằm giảm thiểu thời gian tạm dừng hệ thống (Stop-The-World).
* Phát triển cơ chế InstallSnapshot RPC, cho phép các node Follower bị tụt hậu có thể đồng bộ trực tiếp các tập dữ liệu lớn từ Leader thông qua mạng lưới.
* Xây dựng quy trình khôi phục hệ thống siêu tốc, chủ động nạp snapshot vào RAM và chỉ replay lại các đoạn Write-Ahead Log (WAL) bị thiếu một cách an toàn.
* Hoàn thiện đường ống triển khai AWS bằng cách tinh chỉnh các script CDK, đảm bảo toàn bộ cấu trúc liên kết hạ tầng có thể được khởi tạo đáng tin cậy chỉ bằng một lệnh duy nhất.
* Hoàn thành kiểm thử chức năng nghiêm ngặt cho tất cả các thành phần đám mây được tích hợp, xác nhận tính sẵn sàng cao và khả năng chịu lỗi xuyên suốt kiến trúc.
* Bắt đầu tổng hợp hành trình kỹ thuật, ghi chép lại một cách tường tận các quyết định về kiến trúc, cấu hình bảo mật và chiến lược tối ưu hiệu năng để chuẩn bị cho báo cáo cuối khóa.

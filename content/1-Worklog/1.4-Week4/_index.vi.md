---
title: "Worklog Tuần 4"
date: 2026-07-06
weight: 4
chapter: false
pre: " <b> 1.4. </b> "
---

### Mục tiêu:

* Hiểu mô hình điện toán serverless sử dụng AWS Lambda và API Gateway.
* Lựa chọn và lên kế hoạch kiến trúc cho dự án thực tập cuối kỳ.

### Nhiệm vụ:
| Ngày | Nhiệm vụ | Ngày bắt đầu | Ngày hoàn thành | Tài liệu tham khảo |
| --- | ---------------------------------------------------------------------------------------------------- | ---------- | --------------- | ----------------------------------------- |
| 16 | - Tìm hiểu cơ bản về AWS Lambda và API Gateway. | 06/07/2026 | 06/07/2026 | cloudjourney.awsstudygroup.com |
| 17 | - Thực hành: Xây dựng serverless REST API đơn giản bằng Lambda và API Gateway. | 07/07/2026 | 07/07/2026 | FCAJ Serverless Guide |
| 18 | - Khởi động Dự án: Lên ý tưởng và chọn chủ đề dự án. | 08/07/2026 | 08/07/2026 | Hướng dẫn Dự án |
| 19 | - Thiết kế Kiến trúc: Phác thảo sơ đồ kiến trúc cho dự án đã chọn. | 09/07/2026 | 09/07/2026 | AWS Architecture Center |
| 20 | - Trình bày kế hoạch và kiến trúc dự án cho mentors để phê duyệt. | 10/07/2026 | 10/07/2026 | Ghi chú Phản hồi từ Mentor |
| 6 | - Nâng cấp AppendEntries RPC: Gửi kèm Log Entries.<br>- Tối ưu hóa gửi Batch để tăng thông lượng. | TBD | TBD | Báo cáo C++ RaftDB |
| 7 | - Hiện thực logic giải quyết xung đột (Conflict Resolution).<br>- Hiện thực cơ chế tính toán Commit Index. | TBD | TBD | Báo cáo C++ RaftDB |

### Thành tựu:

* Chuyển đổi thành công từ việc vận hành thủ công trên AWS Console sang phương pháp Infrastructure as Code (IaC) thông qua việc làm chủ AWS Cloud Development Kit (CDK).
* Khởi tạo và triển khai hạ tầng có khả năng mở rộng tự động bằng cách sử dụng các template AWS CloudFormation sinh ra từ CDK.
* Cấu trúc lại các thiết lập trước đó (VPC, EC2, S3) thành các module CDK có thể tái sử dụng, tăng tốc độ và độ nhất quán khi triển khai.
* Nâng cấp thành công AppendEntries RPC của cụm Raft, cho phép truyền tải chính xác các Log Entries thực tế từ Leader sang các Follower.
* Tối ưu hóa thông lượng mạng bằng cách thiết kế cơ chế gửi Batch, giảm thiểu đáng kể chi phí RPC cho các luồng dữ liệu khối lượng lớn.
* Hiện thực xuất sắc logic Giải quyết xung đột (Conflict Resolution) của Raft, giúp Leader tự động phát hiện sai lệch và ghi đè các log bị lỗi trên Follower một cách mượt mà.
* Phát triển cơ chế tính toán Commit Index chuẩn xác, đảm bảo State Machine chỉ thực thi những lệnh đã đạt được sự đồng thuận của đa số node một cách an toàn.

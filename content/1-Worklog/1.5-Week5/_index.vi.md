---
title: "Worklog Tuần 5"
date: 2026-07-13
weight: 5
chapter: false
pre: " <b> 1.5. </b> "
---

### Mục tiêu:

* Thiết lập hạ tầng nền tảng cho dự án cuối kỳ.
* Triển khai các thành phần backend và lược đồ cơ sở dữ liệu.

### Nhiệm vụ:
| Ngày | Nhiệm vụ | Ngày bắt đầu | Ngày hoàn thành | Tài liệu tham khảo |
| --- | ---------------------------------------------------------------------------------------------------- | ---------- | --------------- | ----------------------------------------- |
| 21 | - Triển khai VPC, Subnets, và Security Groups cho dự án. | 13/07/2026 | 13/07/2026 | Sơ đồ Kiến trúc đã duyệt |
| 22 | - Thiết lập cơ sở dữ liệu (RDS/DynamoDB) và cấu hình bảng/lược đồ ban đầu. | 14/07/2026 | 14/07/2026 | Yêu cầu Dự án |
| 23 | - Phát triển các kịch bản backend/hàm Lambda cốt lõi. | 15/07/2026 | 15/07/2026 | Tài liệu AWS SDK |
| 24 | - Tích hợp backend với cơ sở dữ liệu và thử nghiệm các thao tác CRUD. | 16/07/2026 | 16/07/2026 | Yêu cầu Dự án |
| 25 | - Thiết lập IAM roles và các chính sách phân quyền chặt chẽ cho dịch vụ backend. | 17/07/2026 | 17/07/2026 | Tài liệu AWS IAM |
| 6 | - Đấu nối State Machine với tầng Network: Phản hồi client sau khi Committed.<br>- Xử lý lỗi NOT_LEADER để client tự kết nối lại. | TBD | TBD | Báo cáo C++ RaftDB |
| 7 | - Hiện thực các tập lệnh cơ bản trong command engine: GET, SET, EXISTS, DEL.<br>- Đảm bảo tính nguyên tử (Atomicity) cho thao tác ghi đè. | TBD | TBD | Báo cáo C++ RaftDB |

### Thành tựu:

* Tích hợp mô hình điện toán serverless vào dự án bằng cách phát triển và triển khai các hàm AWS Lambda để xử lý logic backend.
* Xây dựng kiến trúc hướng sự kiện (event-driven) thông qua Amazon EventBridge và SNS để kích hoạt các workflow serverless một cách bất đồng bộ.
* Thiết lập thành công cầu nối quan trọng giữa State Machine của RaftDB và tầng Network, đảm bảo client chỉ nhận được phản hồi "OK" sau khi lệnh đã được cụm đồng thuận (Committed).
* Hiện thực cơ chế phản hồi lỗi NOT_LEADER, trao quyền cho client tự động khám phá và kết nối lại với Leader đang hoạt động mà không cần can thiệp thủ công.
* Xây dựng nhóm lệnh cốt lõi của storage engine, hỗ trợ hoàn chỉnh các thao tác KV chuẩn trên RAM như GET, SET, EXISTS và DEL.
* Đảm bảo tính nguyên tử (atomicity) tuyệt đối cho các thao tác ghi đè dữ liệu, giúp cơ sở dữ liệu hoàn toàn miễn nhiễm với các lỗi race condition khi truy cập đồng thời.
* Tổng hợp các thành phần serverless của AWS với các dịch vụ backend tự xây dựng, kết hợp hoàn hảo giữa dịch vụ đám mây và sức mạnh xử lý thuần túy của C++.

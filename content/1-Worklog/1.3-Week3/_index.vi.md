---
title: "Worklog Tuần 3"
date: 2026-06-29
weight: 3
chapter: false
pre: " <b> 1.3. </b> "
---

### Mục tiêu:

* Hiểu các khái niệm cơ bản về networking trên AWS (VPC).
* Tìm hiểu các dịch vụ cơ sở dữ liệu quan hệ và phi quan hệ trên AWS.

### Nhiệm vụ:
| Ngày | Nhiệm vụ | Ngày bắt đầu | Ngày hoàn thành | Tài liệu tham khảo |
| --- | ---------------------------------------------------------------------------------------------------- | ---------- | --------------- | ----------------------------------------- |
| 11 | - Tìm hiểu cơ bản về Amazon VPC: Subnets, Route Tables, Internet Gateways. | 29/06/2026 | 29/06/2026 | cloudjourney.awsstudygroup.com |
| 12 | - Thực hành: Xây dựng VPC tuỳ chỉnh với public/private subnets, NAT Gateway. | 30/06/2026 | 30/06/2026 | FCAJ Networking Modules |
| 13 | - Tìm hiểu các khái niệm và engines của Amazon RDS. | 01/07/2026 | 01/07/2026 | Tài liệu AWS RDS |
| 14 | - Thực hành: Triển khai RDS MySQL instance và kết nối qua EC2 trong private subnet. | 02/07/2026 | 02/07/2026 | FCAJ Database Modules |
| 15 | - Tìm hiểu Amazon DynamoDB (NoSQL, Tables, Items, Partition Keys). | 03/07/2026 | 03/07/2026 | cloudjourney.awsstudygroup.com |
| 6 | - Xây dựng Core State Machine của Raft .<br>- Cài đặt bộ đếm thời gian ngẫu nhiên (Randomized Election Timeout). | TBD | TBD | Báo cáo C++ RaftDB |
| 7 | - Hiện thực chức năng nhận/gửi RequestVote RPC: Xử lý logic từ chối và chấp thuận vote, xử lý Split-brain. | TBD | TBD | Báo cáo C++ RaftDB |

### Thành tựu:

* Làm chủ các khái niệm mạng AWS bằng cách thiết kế và cung cấp một Virtual Private Cloud (VPC) tùy chỉnh, hoàn chỉnh với các public và private subnet.
* Cấu hình cơ chế định tuyến và bảo mật mạnh mẽ, triển khai thành công Route Tables, Internet Gateways và các Security Groups nghiêm ngặt để kiểm soát lưu lượng ra/vào.
* Khám phá các dịch vụ cơ sở dữ liệu được quản lý bằng cách triển khai Amazon RDS, hiểu rõ những lợi ích vận hành so với cơ sở dữ liệu tự lưu trữ.
* Thiết kế thành công Core State Machine cho thuật toán đồng thuận Raft, định nghĩa và chuyển đổi chính xác giữa các trạng thái Follower, Candidate và Leader.
* Hiện thực cơ chế Randomized Election Timeout quan trọng, giảm thiểu hiệu quả rủi ro chia rẽ phiếu bầu (split votes) và đụng độ bầu cử trong cụm Raft.
* Phát triển logic RequestVote RPC phức tạp, cho phép các node đánh giá thông minh các term và log index để chấp thuận hoặc từ chối bầu cử thủ lĩnh.
* Xây dựng khả năng xử lý mạnh mẽ cho các tình huống chia cắt mạng (Split-brain), đảm bảo hệ thống phân tán duy trì tính nhất quán dữ liệu trong điều kiện mạng khắc nghiệt.

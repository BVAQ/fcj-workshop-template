---
title: "Blog 3 - Sử dụng Amazon EFS cho container RaftDB trên ECS Fargate"
date: 2024-01-01
weight: 3
chapter: false
pre: " <b> 3.3. </b> "
---

# LƯU TRỮ BỀN VỮNG CHO CONTAINER STATEFUL TRÊN ECS FARGATE SỬ DỤNG AMAZON EFS

Bài blog kỹ thuật này giải quyết bài toán lưu trữ bền vững cho sidecar container C++23 RaftDB chạy trên Amazon ECS Fargate, giải thích cách Amazon EFS và EFS Access Points bảo toàn write-ahead log cùng trạng thái ứng dụng qua mỗi lần thay thế task.

### Các điểm kỹ thuật nổi bật trong bài blog:

- **Bài toán Ephemeral Storage**: Giải thích vì sao storage phạm vi task của Fargate gây mất dữ liệu ở mỗi lần deploy, khi mỗi **cdk deploy** hoặc **force-new-deployment** thay task bằng một task hoàn toàn mới, xóa sạch WAL và snapshot mà RaftDB đã ghi.

- **Phân tích các lựa chọn Storage**: Đánh giá EBS (giới hạn single-attach không tương thích với việc thay thế task), S3 (object storage không tương thích với ghi WAL tại chỗ), và ephemeral volume (bị hủy cùng task) trước khi chọn EFS là lựa chọn duy nhất vừa tuân thủ POSIX, vừa hỗ trợ multi-attach và sống lâu hơn task.

- **Quản lý Identity qua EFS Access Point**: Trình bày cách EFS Access Point áp đặt quyền sở hữu UID/GID (**10001:10001**) và permission thư mục (**0750**) ở cấp filesystem, loại bỏ nhu cầu quyền root hoặc script entrypoint chạy **chown** trong container.

- **Phân quyền Mount theo IAM**: Chỉ ra cách IAM policy giới hạn action **ClientMount** và **ClientWrite** vào đúng một Access Point ARN cụ thể, ngăn task role chạm vào bất kỳ thư mục nào khác trên cùng file system.

- **Chiến lược Deploy Stop-Then-Start**: Mô tả cấu hình **minHealthyPercent: 0** và **maxHealthyPercent: 100** buộc ECS phải dừng task đang chạy trước khi khởi tạo task thay thế, ngăn hai writer cùng ghi vào WAL gây hỏng dữ liệu.

- **Chu trình Graceful Shutdown và Recovery**: Giải thích toàn bộ vòng đời từ xử lý **SIGTERM** với **stopTimeout** 120 giây để xuất checkpoint, qua kiểm tra startup với xác minh snapshot và replay phần cuối WAL, đảm bảo tính toàn vẹn dữ liệu qua mỗi lần deploy.

---

### Bài viết trên cộng đồng Facebook

![Bài viết trên Facebook](/images/3-BlogPosted/fb-post-blog3.png)

- **Link bài viết gốc**: [Bài đăng Facebook cộng đồng AWS Study Group](https://www.facebook.com/groups/awsstudygroupfcj/permalink/2228318824599744/)
- **Đối tượng mục tiêu**: Cloud Engineers, Backend Developers, Systems Architects
- **Tương tác cộng đồng**: Được đăng trên nền tảng cộng đồng AWS Study Group để nhận phản hồi và đánh giá từ cộng đồng.

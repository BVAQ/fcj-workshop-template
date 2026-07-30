---
title: "Các bài blogs đã đăng"
date: 2024-01-01
weight: 3
chapter: false
pre: " <b> 3. </b> "
---

Dưới đây là danh sách các bài blog chia sẻ về quá trình thực tập và triển khai dự án thực tế trên hạ tầng AWS:

###  [Blog 1 - Tự dựng GitLab Runner với khả năng Auto Scaling trên AWS EC2](3.1-Blog1/)
Blog này chia sẻ hành trình thiết kế và triển khai một GitLab Runner tự động mở rộng (Auto Scaling) trên AWS EC2. Thay vì dùng máy cá nhân cấu hình thấp, hệ thống sử dụng Docker Autoscaler và tự động scale-to-zero khi không có job, giúp tiết kiệm chi phí trong khi vẫn giải quyết được tình trạng thắt cổ chai khi chạy pipeline CI/CD.

###  [Blog 2 - Thiết lập xác thực OpenID Connect (OIDC) giữa GitLab CI và AWS](3.2-Blog2/)
Blog này đi sâu vào cách loại bỏ AWS Access Keys tĩnh trong pipeline CI/CD bằng việc thiết lập OpenID Connect (OIDC). Thay vì lưu secret dài hạn, GitLab CI sử dụng JWT ngắn hạn để xác thực với AWS IAM role, kết hợp với các bước kiểm tra nghiêm ngặt giúp đảm bảo một chuỗi giám hộ (chain of custody) an toàn từ mã nguồn tới lúc deploy.

###  [Blog 3 - Sử dụng Amazon EFS cho container RaftDB trên ECS Fargate](3.3-Blog3/)
Blog này giải quyết bài toán lưu trữ trạng thái bền vững (persistent storage) cho sidecar container C++ RaftDB chạy trên Amazon ECS Fargate. Bằng việc sử dụng Amazon EFS và EFS Access Points, hệ thống đã vượt qua được giới hạn lưu trữ của Fargate, giúp bảo toàn toàn bộ write-ahead log và trạng thái ứng dụng qua mỗi đợt triển khai mới.
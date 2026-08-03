---
title: "Blog 1 - Tự dựng GitLab Runner với Auto Scaling trên AWS EC2"
date: 2024-01-01
weight: 1
chapter: false
pre: " <b> 3.1. </b> "
---

# TỰ DỰNG GITLAB CI/CD RUNNER VỚI KHẢ NĂNG AUTO SCALING TRÊN AWS EC2 SỬ DỤNG DOCKER AUTOSCALER VÀ TERRAFORM

Bài blog kỹ thuật này chia sẻ quá trình thiết kế và triển khai một GitLab Runner tự động tạo các EC2 worker tạm thời thông qua AWS Auto Scaling Group, tự scale về không khi rảnh và khởi tạo instance mới khi có job cần chạy.

### Các điểm kỹ thuật nổi bật trong bài blog:

- **Docker Autoscaler Executor**: Giải thích mô hình executor Docker Autoscaler của GitLab Runner, trong đó một Runner Manager nhẹ liên tục lắng nghe job và giao việc build cho các EC2 instance ngắn hạn được quản lý bởi Fleeting AWS plugin.

- **Kiến trúc Scale-to-Zero**: Trình bày cấu hình Auto Scaling Group với **desired_capacity = 0** và **idle_count = 0**, đảm bảo không có EC2 instance nào tồn tại khi không có pipeline nào chạy, giảm chi phí gần như về không trong thời gian rảnh.

- **Worker dùng một lần**: Mô tả cấu hình **capacity_per_instance = 1** và **max_use_count = 1** đảm bảo mỗi EC2 instance chỉ xử lý đúng một job trước khi bị terminate, cung cấp môi trường build sạch và dễ dự đoán cho mỗi pipeline.

- **Phối hợp giữa Terraform và Fleeting Plugin**: Giải quyết bài toán hai controller khi Terraform tạo ASG nhưng Fleeting plugin quản lý **desired_capacity** lúc runtime, sử dụng **ignore_changes** trong lifecycle block để tránh xung đột cấu hình.

- **Bake sẵn VM image bằng Packer**: Mô tả việc sử dụng HashiCorp Packer để build custom Amazon Machine Image (AMI) đã có sẵn Docker và CI image, loại bỏ thời gian cold-start khi worker mới khởi động.

- **Prebuilt CI Docker Image qua GitHub Actions**: Giải thích workflow tự động build và publish image môi trường CI lên GitHub Container Registry (GHCR), đảm bảo mọi worker dùng chung một môi trường build giống hệt nhau.

---

### Bài viết trên cộng đồng Facebook

![Bài viết trên Facebook](/images/3-BlogPosted/fb-post-blog1.png)

- **Link bài viết gốc**: [Bài đăng Facebook cộng đồng AWS Study Group](https://www.facebook.com/groups/awsstudygroupfcj/permalink/2225051181593175/)
- **Đối tượng mục tiêu**: DevOps Engineers, Cloud Infrastructure Engineers, CI/CD Practitioners
- **Tương tác cộng đồng**: Được đăng trên nền tảng cộng đồng AWS Study Group để nhận phản hồi và đánh giá từ cộng đồng.

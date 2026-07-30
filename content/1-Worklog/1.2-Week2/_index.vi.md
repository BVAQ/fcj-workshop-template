---
title: "Worklog Tuần 2"
date: 2026-06-22
weight: 2
chapter: false
pre: " <b> 1.2. </b> "
---

### Mục tiêu:

* Hiểu sâu hơn về mở rộng EC2 và phân phối tải.
* Nắm vững các giải pháp lưu trữ AWS, đặc biệt là Amazon S3 và EFS.

### Nhiệm vụ:
| Ngày | Nhiệm vụ | Ngày bắt đầu | Ngày hoàn thành | Tài liệu tham khảo |
| --- | ---------------------------------------------------------------------------------------------------- | ---------- | --------------- | ----------------------------------------- |
| 6 | - Tìm hiểu các loại Elastic Load Balancing (ELB) (ALB, NLB).<br>- Hiểu Auto Scaling Groups (ASG). | 22/06/2026 | 22/06/2026 | cloudjourney.awsstudygroup.com |
| 7 | - Thực hành: Cấu hình Application Load Balancer trỏ tới nhiều EC2 instances. | 23/06/2026 | 23/06/2026 | FCAJ Compute Modules |
| 8 | - Tìm hiểu cơ bản về Amazon S3 (Buckets, Objects, Storage Classes, Versioning). | 24/06/2026 | 24/06/2026 | Tài liệu AWS S3 |
| 9 | - Thực hành: Tạo S3 bucket, upload file, cấu hình static website hosting. | 25/06/2026 | 25/06/2026 | cloudjourney.awsstudygroup.com |
| 10 | - Khám phá Amazon EFS và so sánh với EBS, S3.<br>- Thực hành: Mount EFS lên nhiều EC2 instances. | 26/06/2026 | 26/06/2026 | FCAJ Storage Modules |
| 6 | - Hiện thực module máy chủ TCP (Client Sessions, EPOLLIN/EPOLLOUT).<br>- Viết module phân tách gói tin (Frame Parser), xử lý TCP fragmentation/coalescing. | TBD | TBD | Báo cáo C++ RaftDB |
| 7 | - Hiện thực tầng Reliable UDP.<br>- Viết Unit test: Fuzzing TCP Parser để từ chối các gói tin sai định dạng. | TBD | TBD | Báo cáo C++ RaftDB |

### Thành tựu:

* Thiết kế và triển khai thành công môi trường auto-scaling sử dụng Application Load Balancer (ALB) để phân phối tải hiệu quả qua nhiều EC2 instances.
* Nắm vững các tính năng của Amazon S3 thông qua việc tạo bucket, quản lý object và cấu hình thành công môi trường hosting cho static website.
* Xây dựng sự hiểu biết toàn diện về các giải pháp lưu trữ AWS, phân biệt rõ ràng sự khác biệt trong kiến trúc, đặc tính hiệu năng và use case tối ưu cho EBS, EFS và S3.
* Hiện thực thành công tầng mạng cốt lõi cho RaftDB, quản lý tốt các phiên kết nối (client sessions) phức tạp và xử lý chính xác các sự kiện EPOLLIN/EPOLLOUT cấp thấp.
* Phát triển một module Frame Parser mạnh mẽ, có khả năng xử lý mượt mà tình trạng phân mảnh (fragmentation) và dồn gói (coalescing) của TCP, đảm bảo trích xuất dữ liệu tin cậy mà không bị tràn bộ đệm.
* Mở rộng khả năng kết nối mạng bằng việc hiện thực tầng Reliable UDP (RUDP) nhằm thúc đẩy giao tiếp nội bộ cụm với tốc độ cao.
* Củng cố độ bền bỉ của bộ phân tách mạng bằng cách viết các unit test nghiêm ngặt, đặc biệt sử dụng kỹ thuật fuzzing để tự động từ chối các gói tin TCP sai định dạng.

---
title: "Tự đánh giá"
date: 2024-01-01
weight: 6
chapter: false
pre: " <b> 6. </b> "
---

### Tổng quan Hành trình 8 Tuần

Nhìn lại hành trình 8 tuần tham gia chương trình First Cloud AI Journey (FCJ) (từ 15/06/2026 đến 14/08/2026), tôi có thể khẳng định đây là một cột mốc quan trọng trong sự nghiệp phát triển chuyên môn của mình. Không chỉ dừng lại ở các kiến thức lý thuyết, chương trình đã cung cấp một môi trường thực hành thực tế nơi tôi phải tự tay thiết kế, xây dựng và triển khai dự án Awsplace - một ứng dụng hoàn chỉnh trên nền tảng điện toán đám mây.

Quá trình này đánh dấu sự chuyển đổi lớn từ việc nắm bắt lý thuyết về Cloud sang khả năng thực hành kỹ thuật Cloud thực tế. Tôi đã tích lũy được kinh nghiệm thiết kế kiến trúc hệ thống với tính sẵn sàng cao, đảm bảo an toàn bảo mật và tối ưu hóa chi phí vận hành. Hơn thế nữa, tính chất nghiêm ngặt của chương trình cùng với các thời hạn hoàn thành công việc hàng tuần đã rèn luyện đáng kể tính kỷ luật, sự tập trung và khả năng làm việc hiệu quả trong môi trường chuyên nghiệp (Agile/Scrum).

---

### Ma trận Đánh giá Năng lực Cốt lõi

Thay vì những đánh giá chung chung, tôi đã lượng hóa sự phát triển của mình qua từng năng lực cụ thể dựa trên trải nghiệm triển khai dự án Awsplace.

| Tiêu chí Đánh giá | Tự chấm điểm | Phân tích & Minh chứng Cụ thể |
| :--- | :---: | :--- |
| **Thiết kế Kiến trúc Cloud** | 4/5 | Nắm vững các nguyên tắc của kiến trúc 3 tầng (3-tier architecture). Hiểu sâu sắc sự tương tác giữa Compute (EC2), Database (RDS), Storage (S3), và CDN (CloudFront). Chuyển đổi thành công các sơ đồ kiến trúc thành các hệ thống vận hành thực tế. |
| **Bảo mật & Quản lý IAM** | 5/5 | Tuân thủ nghiêm ngặt Nguyên tắc Đặc quyền tối thiểu (Principle of Least Privilege). Thành thạo trong việc tạo và quản lý IAM Users, Roles và Policies. Cấu hình thành công các quy tắc Security Group và tích hợp chứng chỉ SSL thông qua AWS Certificate Manager (ACM) để thực thi mã hóa HTTPS. |
| **Mạng & Định tuyến DNS** | 4/5 | Xử lý thành công các thiết lập mạng phức tạp: triển khai VPC, Public/Private Subnets, và Internet Gateways. Tích lũy kinh nghiệm thực tế về quản lý DNS, cấu hình bản ghi CNAME/ALIAS thông qua Route 53 và các nhà cung cấp bên thứ ba. |
| **CI/CD & Hosting Web (Amplify)** | 5/5 | Làm chủ quy trình Tích hợp liên tục / Triển khai liên tục (CI/CD) thông qua AWS Amplify tích hợp với GitHub. Xử lý hiệu quả các lỗi biên dịch và tự động hóa trơn tru quy trình triển khai lên môi trường production. |
| **Khắc phục Sự cố Nâng cao** | 5/5 | Phát triển tư duy kỹ thuật chuyên nghiệp trong việc giải quyết sự cố: phân tích log có hệ thống, tra cứu tài liệu AWS và cô lập vấn đề để debug hiệu quả, giảm thiểu đáng kể thời gian xử lý các lỗi phân quyền và cấu hình. |
| **Viết Tài liệu Kỹ thuật** | 4/5 | Xây dựng thói quen ghi chép lại mọi cấu hình, lựa chọn kiến trúc và lỗi gặp phải. Duy trì các báo cáo công việc hàng tuần rõ ràng, toàn diện bằng định dạng Markdown, hỗ trợ việc tái tạo lại các bước triển khai một cách dễ dàng. |

---

### Bộ Kỹ năng Kỹ thuật Chuyên sâu Đạt được

Chương trình FCJ đã giúp tôi xây dựng một bộ công nghệ mạnh mẽ và có nhu cầu cao:
- **Compute & Storage:** Tự tin khởi tạo và quản lý các máy chủ ảo EC2 (Linux/Windows). Quản lý tài nguyên tĩnh hiệu quả với Amazon S3 và cấu hình không gian lưu trữ với EBS.
- **Database Management:** Triển khai và quản lý cơ sở dữ liệu quan hệ bằng Amazon RDS (MySQL/PostgreSQL), hiểu rõ về sao lưu dự phòng và triển khai Multi-AZ.
- **Networking & Content Delivery:** Sử dụng Route 53 để quản lý tên miền và cấu hình CloudFront như một CDN toàn cầu để tăng tốc độ phân phối nội dung.
- **Version Control & DevOps:** Thành thạo sử dụng Git và GitHub để quản lý mã nguồn, chiến lược phân nhánh và tích hợp mã an toàn.

---

### Những Thách thức Chính đã Vượt qua

1. **Cấu hình Tên miền Tùy chỉnh & SSL:** Giai đoạn đầu, tôi gặp khó khăn đáng kể với việc Xác thực Chứng chỉ SSL và trỏ bản ghi DNS (CNAME/ALIAS) sang AWS CloudFront. Bằng cách nghiên cứu kỹ lưỡng về quá trình truyền bá DNS (DNS propagation) và cơ chế của Route 53, tôi đã giải quyết thành công các vấn đề, đảm bảo ứng dụng hoạt động ổn định và được bảo mật bằng HTTPS.
2. **Lỗi Từ chối Quyền IAM:** Đã đối mặt với các lỗi truy cập hệ thống (ví dụ: một máy chủ EC2 không thể đọc dữ liệu từ S3). Thay vì cấp quyền Admin toàn diện, tôi đã sử dụng log CloudTrail và IAM policy simulators để phân tích và chỉ cấp chính xác các quyền tối thiểu cần thiết.

---

### Kế hoạch Hành động Chiến lược Tương lai

Việc hoàn thành chương trình này đóng vai trò như một nền tảng vững chắc cho sự phát triển chuyên môn trong tương lai. Dưới đây là các mục tiêu chiến lược của tôi trong 3-6 tháng tới:

1. **Đạt được Chứng chỉ AWS Toàn cầu:**
   - Dành thời gian ôn tập chuyên sâu để thi đạt chứng chỉ AWS Certified Solutions Architect – Associate nhằm chính thức khẳng định kỹ năng kiến trúc và chuyên môn về điện toán đám mây.
2. **Triển khai Cơ sở hạ tầng dưới dạng Mã hóa (IaC):**
   - Chuyển đổi từ việc sử dụng AWS Management Console sang quản lý hạ tầng bằng mã hóa thông qua việc học Terraform hoặc AWS CloudFormation để cung cấp và quản lý hệ thống tự động.
3. **Nghiên cứu Tích hợp Trí tuệ Nhân tạo (AI/ML):**
   - Khám phá các dịch vụ như Amazon Bedrock, Amazon SageMaker, và Amazon Rekognition để tích hợp các tính năng thông minh (như chatbot AI hoặc phân tích hình ảnh) vào các ứng dụng trong tương lai.

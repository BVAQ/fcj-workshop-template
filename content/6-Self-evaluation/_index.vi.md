---
title: "Tự đánh giá"
date: 2024-01-01
weight: 6
chapter: false
pre: " <b> 6. </b> "
---

### 🌟 Tổng quan Hành trình 8 Tuần

Nhìn lại hành trình 8 tuần tham gia chương trình thực tập/workshop **AWS - First Cloud AI Journey (FCJ)** (từ **15/06/2026** đến **14/08/2026**), tôi tự hào khẳng định đây là một trong những cột mốc quan trọng nhất trong sự nghiệp học tập và phát triển chuyên môn của mình. Không chỉ dừng lại ở các khái niệm lý thuyết sách vở, chương trình đã ném tôi vào một môi trường thực chiến nơi tôi phải tự tay thiết kế, xây dựng và vận hành dự án **Awsplace** - một ứng dụng hoàn chỉnh trên nền tảng điện toán đám mây.

Quá trình này là một sự chuyển đổi lớn từ việc "biết về Cloud" sang "làm được Cloud". Tôi đã học được cách kiến trúc một hệ thống có khả năng mở rộng, đảm bảo tính bảo mật cao, và tối ưu hóa chi phí vận hành. Hơn thế nữa, thông qua cường độ làm việc cao và những deadline khắt khe hàng tuần, tôi đã rèn luyện được tính kỷ luật, sự tập trung và khả năng làm việc độc lập cũng như cộng tác nhóm trong một môi trường làm việc chuyên nghiệp (Agile/Scrum).

---

### 📊 Ma trận Đánh giá Năng lực Cốt lõi

Thay vì những đánh giá chung chung, tôi đã lượng hóa sự phát triển của mình qua từng năng lực cụ thể dựa trên trải nghiệm triển khai dự án Awsplace.

| Tiêu chí Đánh giá | Tự chấm điểm | Phân tích & Minh chứng Cụ thể |
| :--- | :---: | :--- |
| **Thiết kế Kiến trúc Cloud** | ⭐⭐⭐⭐ | Nắm vững các nguyên tắc của kiến trúc 3 tầng (3-tier architecture). Hiểu sâu sắc sự tương tác giữa Compute (EC2), Database (RDS), Storage (S3), và CDN (CloudFront). Chuyển đổi thành công các sơ đồ kiến trúc thành các triển khai thực tế có thể hoạt động. |
| **Bảo mật & Quản lý IAM** | ⭐⭐⭐⭐⭐ | Tuân thủ nghiêm ngặt Nguyên tắc Đặc quyền tối thiểu (Principle of Least Privilege). Rất thành thạo trong việc tạo và quản lý IAM Users, Roles và Policies. Cấu hình thành công các quy tắc Security Group chính xác và tích hợp chứng chỉ SSL thông qua AWS Certificate Manager (ACM) để thực thi mã hóa HTTPS. |
| **Mạng & Định tuyến DNS** | ⭐⭐⭐⭐ | Xử lý thành công các thiết lập mạng phức tạp: triển khai VPC, Public/Private Subnets, và Internet Gateways. Tích lũy kinh nghiệm thực tế sâu rộng về quản lý DNS, cấu hình bản ghi CNAME/ALIAS thông qua Route 53 và các nhà cung cấp bên thứ ba (như Namecheap). |
| **CI/CD & Hosting Web (Amplify)** | ⭐⭐⭐⭐⭐ | Hoàn toàn làm chủ pipeline Tích hợp liên tục / Triển khai liên tục (CI/CD) bằng AWS Amplify tích hợp với GitHub. Nhanh chóng giải quyết các lỗi build và tự động hóa quy trình triển khai lên môi trường production một cách trơn tru. |
| **Khắc phục Sự cố Nâng cao** | ⭐⭐⭐⭐⭐ | Đây là kỹ năng được cải thiện nhiều nhất của tôi. Thay vì hoảng hốt trước các lỗi "403 Access Denied", tôi đã phát triển một tư duy kỹ thuật trưởng thành: phân tích log, đi sâu vào tài liệu AWS và cô lập vấn đề một cách có hệ thống để debug hiệu quả. |
| **Viết Tài liệu Kỹ thuật** | ⭐⭐⭐⭐ | Xây dựng thói quen tốt trong việc ghi chép lại mọi cấu hình, lựa chọn kiến trúc và lỗi gặp phải. Duy trì các báo cáo công việc (worklog) hàng tuần rõ ràng và toàn diện bằng Markdown, giúp người khác dễ dàng tái tạo lại các bước triển khai của tôi. |

---

### 🛠️ Bộ Kỹ năng Kỹ thuật Chuyên sâu Đạt được

Chương trình FCJ đã giúp tôi xây dựng một bộ công nghệ mạnh mẽ và có nhu cầu cao:
- **Compute & Storage:** Tự tin khởi tạo và quản lý các instance **EC2** (Linux/Windows). Quản lý tài nguyên tĩnh hiệu quả với **Amazon S3** và cấu hình block storage với **EBS**.
- **Database Management:** Triển khai và quản lý cơ sở dữ liệu quan hệ với **Amazon RDS** (MySQL/PostgreSQL), hiểu rõ về sao lưu dự phòng và triển khai Multi-AZ.
- **Networking & Content Delivery:** Sử dụng **Route 53** để quản lý tên miền (vd: `bvaq-workshop.space`) và cấu hình **CloudFront** như một CDN toàn cầu để tăng tốc độ phân phối nội dung.
- **Version Control & DevOps:** Thành thạo sử dụng **Git** và **GitHub** để quản lý mã nguồn, chiến lược phân nhánh và merge an toàn.

---

### 🏆 Những Thách thức Chính đã Vượt qua

1. **Cấu hình Tên miền Tùy chỉnh & SSL:** Ban đầu, tôi gặp khó khăn đáng kể với việc Xác thực Chứng chỉ SSL và trỏ bản ghi DNS (CNAME/ALIAS) từ Namecheap sang AWS CloudFront. Nhờ kiên nhẫn nghiên cứu về truyền bá DNS (DNS propagation) và cơ chế của Route 53, tôi đã giải quyết hoàn toàn các vấn đề, mang lại một ứng dụng ổn định và được bảo mật bằng HTTPS.
2. **Lỗi Từ chối Quyền IAM:** Đã có những lúc hệ thống báo lỗi truy cập (vd: một instance EC2 không thể đọc từ S3). Thay vì cấp quyền Admin toàn diện một cách nguy hiểm như một cách sửa lỗi nhanh, tôi đã học cách đọc log CloudTrail và policy simulators của IAM để cấp chính xác các quyền tối thiểu cần thiết.

---

### 🎯 Kế hoạch Hành động Chiến lược Tương lai

Sự kết thúc của chương trình này không phải là vạch đích; đó là một bệ phóng. Dưới đây là các mục tiêu hành động của tôi trong 3-6 tháng tới:

1. **Đạt được Chứng chỉ AWS Toàn cầu:**
   - Dành thời gian học tập tập trung để thi đậu chứng chỉ **AWS Certified Solutions Architect – Associate** nhằm chính thức khẳng định kỹ năng kiến trúc và chuyên môn về cloud của mình.
2. **Nâng cấp với Infrastructure as Code (IaC):**
   - Mặc dù AWS Management Console rất tuyệt vời cho việc học tập, nó không thể mở rộng cho các dự án doanh nghiệp. Tôi sẽ bắt đầu học **Terraform** hoặc **AWS CloudFormation** để cung cấp và quản lý hạ tầng hoàn toàn thông qua code.
3. **Nghiên cứu Sâu về Tích hợp AI/ML:**
   - Đón đầu làn sóng AI, tôi dự định khám phá các dịch vụ như **Amazon Bedrock**, **Amazon SageMaker**, và **Amazon Rekognition** để tích hợp các tính năng thông minh (như chatbot AI tạo sinh hay phân tích hình ảnh) vào các ứng dụng tương lai của mình.

---

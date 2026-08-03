---
title: "Blog 2 - Thiết lập xác thực OpenID Connect (OIDC) giữa GitLab CI và AWS"
date: 2024-01-01
weight: 2
chapter: false
pre: " <b> 3.2. </b> "
---

# LOẠI BỎ HOÀN TOÀN STATIC KEY: BẢO MẬT PIPELINE GITLAB CI/CD BẰNG OPENID CONNECT VÀ AWS IAM

Bài blog kỹ thuật này giải thích cách loại bỏ AWS Access Key dài hạn khỏi pipeline CI/CD trên GitLab tự dựng bằng cách triển khai OpenID Connect (OIDC) federation, cho phép các job assume một IAM role với credential ngắn hạn được giới hạn theo project và branch cụ thể.

### Các điểm kỹ thuật nổi bật trong bài blog:

- **Kiến trúc OIDC Federation**: Giải thích cách GitLab đóng vai một OpenID Connect identity provider, phát hành JWT ngắn hạn cho mỗi job khai báo **id_tokens**, trong khi AWS IAM xác thực chữ ký token thông qua OIDC provider đã đăng ký và JWKS endpoint.

- **Trust Policy với Subject Pinning**: Trình bày chi tiết IAM trust policy thực hiện exact-match trên claim **aud** và pattern-match trên claim **sub** (**project_path:…:ref_type:branch:ref:main**), đảm bảo chỉ đúng project và branch mới có thể assume role deploy.

- **Giảm thiểu phơi nhiễm Credential**: Mô tả cách chỉ 3 trong 14 job (**push-ecr**, **publish-raftdb-image**, **deploy-to-aws**) khai báo **id_tokens** và nhận AWS credential, trong khi 11 job còn lại, bao gồm cả job build image RaftDB, chạy mà không có bất kỳ identity AWS nào.

- **Chuỗi giám hộ (Chain of Custody) cho Container Image**: Trình bày quy trình xác minh nhiều bước: image RaftDB được build mà không có AWS credential, scan bằng Trivy, chuyển giao qua artifact kèm file bằng chứng, đối chiếu từng byte sau khi upload lên ECR, và test lại từ registry trước khi deploy.

- **Truy vết STS Session**: Chỉ ra cách **--role-session-name "GitLabCI-${CI_PIPELINE_ID}"** nhúng pipeline ID vào mọi entry trên CloudTrail, cho phép truy vết đầy đủ từ AWS API call ngược về pipeline CI/CD cụ thể.

- **Immutable Image Tag trên ECR**: Giải thích cấu hình tag mutability trên ECR sử dụng **MUTABLE_WITH_EXCLUSION** với wildcard filter trên **raftdb-***, ngăn việc ghi đè image production đã publish trong khi các tag khác vẫn có thể di chuyển.

---

### Bài viết trên cộng đồng Facebook

![Bài viết trên Facebook](/images/3-BlogPosted/fb-post-blog2.png)

- **Link bài viết gốc**: [Bài đăng Facebook cộng đồng AWS Study Group](https://www.facebook.com/groups/awsstudygroupfcj/permalink/2227894604642166/)
- **Đối tượng mục tiêu**: DevOps Engineers, Security Engineers, Cloud Architects
- **Tương tác cộng đồng**: Được đăng trên nền tảng cộng đồng AWS Study Group để nhận phản hồi và đánh giá từ cộng đồng.

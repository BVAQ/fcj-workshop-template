---
title: "Chia sẻ & Đóng góp ý kiến"
date: 2024-01-01
weight: 7
chapter: false
pre: " <b> 7. </b> "
---

Nhìn lại toàn bộ hành trình 8 tuần cùng **First Cloud AI Journey (FCJ)**, mình có rất nhiều cảm xúc và suy nghĩ muốn chia sẻ. Dưới đây là những đánh giá chân thực nhất của cá nhân mình về chương trình, không còn là những gạch đầu dòng khô khan nữa.

### 🌟 Đánh giá chung về chương trình

**1. Môi trường và cường độ làm việc**  
Cá nhân mình thấy môi trường của FCJ thực sự mang đậm tính "thực chiến". Nó không giống như việc đi học lý thuyết trên trường hay xem các tutorial trên mạng. Cường độ làm việc khá cao với các deadline hàng tuần rất gắt gao. Ban đầu mình hơi ngợp, nhưng chính áp lực này lại ép mình phải rèn luyện tính kỷ luật và khả năng quản lý thời gian. Cộng đồng trên group (Discord/Zalo) hoạt động cực kỳ sôi nổi, nhiều khi 1-2 giờ sáng hỏi bài vẫn có người nhảy vào support hoặc cùng nhau debug. Cảm giác không bị đơn độc trong một môi trường remote thực sự rất tuyệt vời.

**2. Tinh thần Tự học và Hỗ trợ từ Cộng đồng (Community Support)**  
Chương trình này đề cao tinh thần tự học, không có mentor cầm tay chỉ việc. Ban đầu mình khá "sốc nhiệt" vì phải tự bơi giữa biển tài liệu AWS khổng lồ. Tuy nhiên, chính việc phải tự mày mò khi kẹt ở lỗi "403 Access Denied" hay CI/CD build xịt đã rèn luyện cho mình kỹ năng tự research cực kỳ tốt. Thay vì hỏi và có ngay đáp án, mình học cách đọc CloudTrail, tra cứu Stack Overflow và tài liệu chính thức của AWS. Điểm sáng lớn nhất là sự hỗ trợ từ cộng đồng anh em cùng cohort; mọi người review lỗi cho nhau, cùng thảo luận tìm hướng giải quyết, tạo nên một môi trường tự học nhưng không hề cô độc. Team Admin cũng rất chu đáo, luôn nhắc nhở deadline và support nhiệt tình các vấn đề về tài khoản.

**3. Mức độ bám sát thực tế và chuyên ngành**  
Những gì mình học được ở trường (như kiến thức mạng cơ bản, hệ điều hành) chỉ là nền tảng. Khi vào FCJ, việc tự tay cấu hình VPC, Public/Private Subnet, hay thiết lập Route 53 thực sự đã biến những lý thuyết khô khan đó thành kiến thức sống. Các công việc trong dự án Awsplace bám sát 100% với nhu cầu tuyển dụng Cloud/DevOps hiện nay ở các doanh nghiệp.

**4. Kỹ năng thu nhận được (Không chỉ là Technical)**  
Tất nhiên, về mặt kỹ thuật, mình đã nắm được kiến trúc 3-tier, biết dùng EC2, RDS, S3, Amplify... Nhưng điều mình quý giá hơn cả là **kỹ năng xử lý sự cố (troubleshooting)** và **kỹ năng viết tài liệu (documentation)**. Trước đây mình rất ghét đọc log, thấy lỗi là cuống cuồng đi hỏi. Giờ thì mình đã có phản xạ bình tĩnh đọc log, tra cứu AWS Docs và tự khoanh vùng lỗi. Việc phải viết báo cáo hàng tuần bằng Markdown cũng giúp tư duy trình bày vấn đề của mình rành mạch hơn rất nhiều.

---

### 💡 Trả lời một số câu hỏi khảo sát

**Điều gì làm bạn hài lòng nhất trong suốt quá trình tham gia?**  
Khoảnh khắc nhìn thấy trang web của mình thực sự chạy được trên tên miền tùy chỉnh với ổ khóa xanh HTTPS (chứng chỉ SSL), và mỗi lần push code lên GitHub là hệ thống tự động deploy (CI/CD)... Cảm giác "thành tựu" đó vô cùng lớn. Nó chứng minh rằng mình hoàn toàn có thể tự tay xây dựng một hệ thống thật từ con số không.

**Theo bạn, chương trình cần cải thiện điều gì để tốt hơn cho các lứa (cohort) sau?**  
Mình nghĩ ban tổ chức có thể làm thêm một buổi hướng dẫn thật kỹ (hoặc một tài liệu riêng) về **Quản lý chi phí (Billing & Cost Management)** ngay từ tuần đầu tiên. Dù AWS có Free Tier, nhưng nhiều bạn (trong đó có mình) đôi khi cấu hình nhầm hoặc quên tắt dịch vụ dẫn đến bị trừ tiền oan. Nếu có cảnh báo rõ ràng hơn về các dịch vụ dễ phát sinh chi phí, trải nghiệm sẽ trọn vẹn hơn. Ngoài ra, nếu có thêm 1-2 buổi seminar trực tuyến chia sẻ kinh nghiệm thực tế từ các kỹ sư đang làm Cloud thì sẽ rất truyền cảm hứng.

**Bạn có sẵn sàng giới thiệu chương trình này cho bạn bè không?**  
Chắc chắn là **CÓ**. Mình đã giới thiệu cho vài người bạn cùng khóa. Nếu ai thực sự muốn chuyển mình từ một sinh viên chỉ biết code chay sang một người biết cách vận hành cả một hệ thống trên Cloud, FCJ là môi trường "khắc nghiệt nhưng cực kỳ xứng đáng" để trải nghiệm.

---

### 🎯 Lời kết

Kết thúc 8 tuần không có nghĩa là dừng lại. Trải nghiệm tại FCJ đã cung cấp cho mình một bệ phóng vô cùng vững chắc. Mình muốn gửi lời cảm ơn chân thành đến đội ngũ Ban tổ chức và đặc biệt là toàn thể anh em trong cộng đồng đã đồng hành, hỗ trợ lẫn nhau trong suốt chặng đường qua. Chúc cho cộng đồng FCJ ngày càng phát triển và tạo ra nhiều thế hệ kỹ sư Cloud chất lượng!
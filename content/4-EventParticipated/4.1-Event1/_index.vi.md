---
title: "Event 1: Agentic AI Build Week (AABW) Hackathon"
date: 2024-01-01
weight: 1
chapter: false
pre: " <b> 4.1. </b> "
---

# Báo cáo Sự kiện: Agentic AI Build Week (AABW) Hackathon

### Mục tiêu Sự kiện (Event Objectives)

- Khám phá tiềm năng vô hạn và ứng dụng thực tế của **Agentic AI** (Trí tuệ nhân tạo có khả năng tự trị và hành động) thông qua hệ sinh thái Amazon Web Services (AWS), đặc biệt là việc làm chủ công nghệ lõi **Amazon Bedrock**.
- Trải nghiệm cường độ làm việc thực chiến của một cuộc thi **Hackathon 24 giờ**: từ việc thai nghén ý tưởng, vẽ nháp kiến trúc trên bảng trắng, code prototype, gỡ lỗi (debug) thâu đêm, đến việc hoàn thiện pitch deck và demo sản phẩm trực tiếp trước ban giám khảo.
- Rèn luyện kỹ năng giải quyết vấn đề (problem-solving) cực hạn, thiết kế hệ thống có khả năng mở rộng (scalable) nhưng vẫn phải tối ưu hóa chi phí nghiêm ngặt (cost optimization), và làm việc nhóm liên tục trong điều kiện áp lực thời gian cực cao.
- Khuyến khích tư duy "Customer-obsessed" (ám ảnh khách hàng) - nguyên tắc tối thượng của AWS: Luôn đi từ những "nỗi đau" (pain points) có thật của doanh nghiệp, sau đó mới tìm kiếm và áp dụng các giải pháp công nghệ phù hợp nhất để giải quyết, chứ không phải làm ngược lại.

### Danh sách các Đội thi & Diễn giả (Teams & Speakers)

Tại sự kiện AABW lần này, thay vì lắng nghe các chuyên gia thuyết trình một chiều như các buổi hội thảo truyền thống, điểm nhấn thuộc về màn trình diễn của các đội thi. Họ vừa là thí sinh, vừa là diễn giả mang đến những giải pháp công nghệ đột phá được xây dựng chỉ trong vỏn vẹn 24 giờ:
- **Đội OneTeam (Quán quân):** Anh Duy, Tran Dong, Doan Trung, Minh Viet, Anshul Roy.
- **Đội 3KA:** Huỳnh An Khương, Nguyễn Quốc Huy, Ngô Quang Khôi, Hoàng Lê Thành Đức, Đặng Nguyễn Phước Lộc, Đặng Trường Hưng.
- **Đội Plan V:** Pham Tien Thuan Phat, Huynh Hoang Long, Le Minh Nghia, Tran Dai Vi, Nguyen An.
- **Đội Dream AI Team:** Le Tan Luc, Do Hoang Hieu, Trieu Quoc Hao, Nguyen Van Duy Khiem, Nguyen Cong Minh, Nguyen Tran Minh Quan.

---

### Điểm nhấn Chính (Key Highlights)

Khối lượng kiến thức lớn nhất của sự kiện nằm ở các phiên phân tích mổ xẻ kiến trúc kỹ thuật của 4 sản phẩm xuất sắc nhất. Mỗi đội mang đến một bài toán ngành (domain) riêng biệt và những cách giải quyết cực kỳ sáng tạo.

#### 1. Bài toán tự động hóa đặt hàng F&B - OneTeam (KFC Bot Agent)

**Nhận diện vấn đề (The Problem):**
- Ngành F&B gặp khó khăn khủng khiếp với tự động hóa hội thoại (Conversational Ordering). Đội OneTeam dẫn chứng một câu chuyện đắt giá: Ông lớn McDonald's đã phải ngậm ngùi chấm dứt chuỗi thử nghiệm hệ thống AI drive-thru tại hơn 100 cửa hàng ở Mỹ. Bài học rút ra là: **Đặt hàng là một bài toán hệ thống (system problem) vô cùng phức tạp**, không phải cứ lắp AI vào là xong.
- Ngôn ngữ tự nhiên của con người thì lộn xộn, đa nghĩa, viết tắt (Natural language is messy), nhưng quy tắc kinh doanh của ngành F&B lại tuyệt đối khắt khe (Business rules are strict - ví dụ: combo này không được đổi thức uống, mã giảm giá chỉ áp dụng sau 9h tối).
- **Hành trình đánh mất đơn hàng (The Moment the Brand Loses the Order):** Khách hàng đang chat vui vẻ trên mạng xã hội -> Xuất hiện nhu cầu ăn uống -> Bị thương hiệu ép phải thoát app đang chat để tải ứng dụng riêng -> Trải qua các rào cản ma sát (đăng nhập, tải app, mò mẫm menu chậm chạp) -> Tụt cảm xúc và **Hủy đơn (Lost order)**. Đội ngũ nhân viên chat hỗ trợ thủ công (Human-only chat) thì không bao giờ có thể mở rộng (scale) nổi trong các đợt bùng nổ lưu lượng (traffic spikes).

**Giải pháp Kiến trúc Hiện đại (KFC Bot Agent):**
- **Không tải app, không tạo tài khoản (Zero Friction):** Khách hàng đặt hàng, tùy chỉnh món ăn trực tiếp qua Zalo OA, Messenger mà không cần rời khỏi môi trường chat yêu thích.
- **Mô hình Agent 5 bước (The Model understands, the Tools decide what is real):** 
  1. **Goal:** Hiểu ý định thật sự của người dùng.
  2. **Plan:** Lập kế hoạch các bước API cần gọi.
  3. **Tools:** Truy xuất dữ liệu kinh doanh đáng tin cậy.
  4. **Act:** Thêm món vào giỏ hàng thực tế và áp mã khuyến mãi.
  5. **Verify:** Đối chiếu độ chính xác với giỏ hàng.
- **Kiến trúc "Design Once, Deploy Everywhere":** 
  - **Lớp Ingestion:** Sử dụng Web Application Firewall (WAF) bảo vệ API Gateway, sau đó gọi Lambda và đẩy message vào hàng đợi SQS để đảm bảo không rớt tin nhắn.
  - **Lớp AgentCore Runtime:** Xử lý cốt lõi bằng **Amazon Bedrock**, làm nhiệm vụ phân rã ngôn ngữ, lập kế hoạch (Orchestration) và sử dụng công cụ (Tool use).
  - **Lớp Memory & Data:** Lưu trạng thái phiên chat (Session/State) bằng DynamoDB, tìm kiếm Full-text bằng OpenSearch Service, cache bằng ElastiCache, và mã hóa bảo mật toàn bộ dữ liệu người dùng qua KMS.

**Tác động (Impact):** Giải pháp này mang lại độ trễ luồng tin nhắn siêu tốc chỉ **3-5 giây**, chi phí vận hành siêu rẻ chưa đến **$0.006 / đơn hàng**, tổng chi phí hạ tầng khoảng **$88/tháng**, và nhờ AgentCore tự động hóa định tuyến, nhóm đã cắt giảm tới **60%** lượng mã nguồn hạ tầng.

#### 2. Giám sát An ninh và Đám đông Chủ động bằng AI - Đội 3KA (S.H.E.P.H.E.R.D)

**Nhận diện vấn đề (The Problem):**
- Ban quản lý tại các sự kiện lớn hoặc nhà ga, sân bay hiện nay phải dùng nhân viên ngồi dán mắt vào hàng chục màn hình camera. Cách làm này thụ động, chậm chạp, dễ dẫn đến quá tải thông tin, bỏ sót các sự kiện bất thường và không thể dự báo trước các điểm đen ùn tắc sắp xảy ra.

**Giải pháp & Công nghệ sử dụng:**
- **S.H.E.P.H.E.R.D** (Smart Human-flow Evaluation, Prediction, Hazard Detection, Response, and Dispatch) được thiết kế để phân tích trực tiếp luồng camera sống (live stream) và biến chúng thành các chỉ số vận hành có thể hành động được (actionable operational information).
- **Khả năng cốt lõi:** Nhận diện và theo dõi lộ trình di chuyển của từng người, đo lường mật độ đám đông, đánh giá tình trạng hàng đợi, dự báo áp lực kẹt xe trong 15 phút tới và chủ động bắn cảnh báo (proactive alerts) cho đội ngũ điều phối.
- **Kiến trúc:** 
  - Lớp thị giác máy tính (Computer Vision): Áp dụng **YOLO + ByteTrack** để tracking đối tượng với độ chính xác cao.
  - Lớp Suy luận đám mây (Cloud Inference): Chạy các tác vụ học máy nặng nề thông qua **Amazon SageMaker**.
  - Lớp Agentic AI: Sử dụng **Amazon Bedrock AgentCore + Strands Agent** để xây dựng tính năng "Operator Copilot" - một trợ lý ảo cho phép nhân viên gõ câu hỏi bằng ngôn ngữ tự nhiên (VD: "Khu vực sảnh A có đang đông không?") và nhận về câu trả lời kèm dữ liệu thời gian thực. Bảng điều khiển (Dashboard) được xây dựng trên nền tảng **React**.

**Thử thách kỹ thuật & Vượt khó:**
- Đội thi chia sẻ những khó khăn cực độ: Lần đầu tiên tiếp xúc với hệ sinh thái AWS, không hề có background chuyên sâu về AI, và đặc biệt là bài toán tối ưu độ trễ suy luận (inference latency) cũng như việc duy trì độ ổn định của luồng video trực tiếp trên cloud. Mọi thứ được đánh đổi bằng 5 lon Redbull và những ca debug kéo dài đến tận 3 giờ sáng.

#### 3. Trợ lý Sinh Kiến trúc Hệ thống tự động - Đội Plan V (SA Professional Native App)

**Nhận diện vấn đề (The Problem):**
- Trong môi trường công ty công nghệ thực tế, một Solution Architect (SA) thường xuyên nhận được những yêu cầu "trên trời rớt xuống": "Hãy thiết kế cho tôi một hệ thống AI theo chuẩn SOP, cần xong trước thứ Năm tuần này!".
- Quy trình làm việc truyền thống cực kỳ mệt mỏi: SA phải ngồi đọc tài liệu yêu cầu (BRD/PRD) dài hàng chục trang một cách thủ công, bắt đầu phác thảo kiến trúc từ một tờ giấy trắng (blank page), mất hàng giờ để vẽ các sơ đồ hạ tầng chi tiết, và cuối cùng là đau đầu tính toán chi phí (cost estimation) một cách cảm tính và thiếu chính xác.

**Giải pháp Đột phá:**
- Ứng dụng **Solution Architect Professional AI Native App**.
- **Luồng xử lý (Workflow) thông minh:**
  - Ứng dụng tiếp nhận đầu vào là các đoạn chat yêu cầu bằng ngôn ngữ tự nhiên. AI sẽ phân tích và trích xuất yêu cầu (Requirement Extraction).
  - Đề xuất các bản phác thảo kiến trúc đa nền tảng (Hybrid-cloud aware) tuân thủ đúng các tiêu chuẩn bảo mật của công ty.
  - Tự động sinh ra mã XML để import thẳng vào phần mềm **Draw.io**, sử dụng đúng các biểu tượng (icons) chuẩn mực của AWS.
  - Tự động sinh mã nguồn khởi tạo hạ tầng Infrastructure as Code (IaC) như Terraform/CloudFormation.
  - Sinh ra bảng dự toán chi phí chi tiết (AWS cost estimates) cho khu vực Châu Á (ap-southeast-1).
- Thay vì làm mọi thứ từ con số 0, giờ đây SA làm việc qua một khung chat bên hông (chat sidebar), liên tục yêu cầu AI tinh chỉnh và hoàn thiện bản nháp. Tốc độ thiết kế giảm từ vài ngày xuống còn vài phút.

#### 4. Khai phá Dữ liệu và Phân tích Tín hiệu Chiến lược - Đội Dream AI (Signal Scout)

**Nhận diện vấn đề (The Problem):**
- Trong thế giới B2B, các tập đoàn lớn cần một công cụ tình báo (Intelligence tool) để phát hiện sớm các động thái tái cấu trúc, thay đổi nhân sự cấp cao, hoặc chuyển hướng chiến lược của đối thủ cạnh tranh. Các tín hiệu này thường nằm rải rác trên báo chí, báo cáo tài chính, và mạng xã hội.

**Giải pháp (Signal Scout):**
- Nền tảng Dashboard tự phục vụ (Self-service dashboard) cho phép đội ngũ chiến lược theo dõi tự động các doanh nghiệp mục tiêu.
- Hệ thống thu thập hàng ngàn tín hiệu rời rạc, làm sạch, kết nối chúng thành một chuỗi sự kiện rõ ràng và minh bạch. Đặc biệt, mọi kết luận AI đưa ra đều phải kèm theo nguồn bằng chứng (evidence-backed).
- Hỗ trợ ra quyết định kinh doanh cốt lõi: Tiếp tục duy trì (Maintain), thay đổi thích ứng (Adapt), hoặc tăng tốc đầu tư (Accelerate).

**Kiến trúc & Nghệ thuật Tối ưu Chi phí (FinOps):**
- Thu thập dữ liệu thông qua LangFuse, TinyFish, và Apify.
- Đội Dream AI gây ấn tượng mạnh với Ban Giám khảo nhờ việc hoạch định chi phí cực kỳ rõ ràng, phản ánh tư duy kinh doanh sắc bén. Họ vẽ ra 3 kịch bản vận hành hàng tháng trên AWS:
  - **Kịch bản Tối thiểu (Min):** ~ $81/tháng (Chi phí AWS chỉ $17, còn lại cho API bên thứ 3). Sử dụng DynamoDB, API Gateway, và Lambda để tiết kiệm tối đa.
  - **Kịch bản Trung bình (Mid):** ~ $94/tháng.
  - **Kịch bản Tối đa (Max):** ~ $359/tháng (Chạy max công suất Bedrock token và AgentCore Runtime).

---

### Bài học kinh nghiệm cốt lõi (Key Takeaways)

#### 1. Tư duy Thiết kế Sản phẩm (Design Mindset)
- **Kinh doanh đi trước, Công nghệ theo sau (Business-first approach):** Đội OneTeam (KFC) đã chứng minh chân lý này một cách xuất sắc. AI LLM (Large Language Models) chỉ là phần bề nổi để hiểu ngôn ngữ; phần lõi của ứng dụng phải là một bộ máy xử lý triệt để logic kinh doanh (kiểm tra tồn kho, trạng thái giỏ hàng, xác thực mã giảm giá). Đội Dream AI (Signal Scout) cũng tương tự khi đặt tính "minh bạch, có thể xác minh được" của dữ liệu lên hàng đầu để phục vụ các Giám đốc Chiến lược (CxO).
- **Phạm vi quản lý (Bounded Contexts) & Chia để trị:** Để xây dựng một hệ thống lớn trong 24 giờ, các đội phải định nghĩa cực kỳ rõ ràng giới hạn của hệ thống. Nhóm 3KA chỉ thu thập dữ liệu một cụm camera nhỏ để phân tích, thay vì ôm đồm toàn bộ tòa nhà. Điều này giúp hệ thống hoạt động ổn định và có thể đem đi biểu diễn (demo) thành công.

#### 2. Kiến trúc Kỹ thuật (Technical Architecture)
- **Quyền năng của Agentic AI:** Trong tương lai gần, AI sẽ không chỉ dừng lại ở việc sinh ra văn bản (Generative AI Chatbot). Với AgentCore, AI có khả năng **Suy luận (Reasoning) -> Chọn công cụ (Tools) -> Thực thi hành động (Act)**. Điều này đồng nghĩa với việc AI có thể trực tiếp ghi dữ liệu vào Database, gọi API thanh toán, hay tạo mã IaC. Nó thay thế một lượng lớn code Backend truyền thống.
- **Kiến trúc hướng sự kiện (Event-driven Architecture):** Để hệ thống không bị "treo" khi có hàng ngàn user cùng chat một lúc, việc áp dụng SQS (Simple Queue Service) làm bộ đệm giữa API Gateway và Lambda là một pattern kinh điển và cực kỳ hiệu quả mà các đội thi đã áp dụng.
- **Năng lực kiểm soát chi phí (Cost Estimation/FinOps):** Trong môi trường Cloud, nếu không ước tính chi phí, bạn có thể nhận những tờ hóa đơn khổng lồ. Việc các đội thi tính toán chi li từng token của Bedrock, từng request của DynamoDB, hay phí WAF chứng tỏ sự trưởng thành trong tư duy kiến trúc sư Đám mây.

#### 3. Chiến lược Sinh tồn tại Hackathon (Hackathon Survival Strategy)
- **Bắt đầu nhỏ, hoàn thiện nhanh (Small, finished work beats big, broken ideas):** Thà làm một chức năng duy nhất chạy trơn tru mượt mà, còn hơn vẽ ra 10 chức năng nhưng đến lúc Demo thì app bị crash (sập). "Done" (hoàn thành) quan trọng hơn "Perfect" (hoàn hảo).
- **Chuẩn bị trước không phải là gian lận:** Việc có sẵn các boilerplate code, template React, thiết lập sẵn tài khoản AWS, và phân vai trò rạch ròi (người lo backend, người code frontend UI, người chuyên thiết kế slide pitch deck) là bí quyết sống còn để vượt qua giới hạn thời gian.

---

### Kế hoạch Ứng dụng vào Công việc (Applying to Work)

Những công nghệ và tư duy từ cuộc thi này quá sát với thực tế, và mình đã vạch ra lộ trình để ứng dụng ngay vào công việc/dự án cá nhân:
1. **Thiết lập Agentic Workflow cho quy trình vận hành:** Mình sẽ không dừng lại ở việc gọi API OpenAI/Bedrock để tạo text thông thường. Mình sẽ bắt đầu nghiên cứu **Amazon Bedrock Agents** để cấu hình các luồng tự động (tương tự như cách nhóm Plan V tạo IaC). Mình muốn tạo ra một Bot có khả năng đọc log lỗi trên CloudWatch và tự động đề xuất hướng fix lỗi trực tiếp vào Slack của team.
2. **Nâng cấp Kiến trúc thành Event-driven:** Thay vì các hệ thống monolithic gọi API đồng bộ (synchronous) đang làm app bị nghẽn, mình sẽ bắt tay vào refactor các module gửi email thông báo, tạo báo cáo... sang dùng **Amazon SQS** và **Lambda** để xử lý bất đồng bộ, giúp hệ thống chịu tải tốt hơn (scale mượt mà hơn).
3. **Thực hành kỷ luật FinOps:** Bắt đầu từ tháng tới, trước khi đưa ra bất kỳ đề xuất triển khai dịch vụ AWS mới nào, mình sẽ bắt buộc bản thân phải lên một bảng Excel tính toán chi phí (dựa trên AWS Pricing Calculator) với ít nhất 2 kịch bản (Low traffic và High traffic) giống hệt cách team Signal Scout đã thực hiện, để rèn luyện tư duy kinh doanh.

---

### Trải nghiệm Sự kiện (Event Experience)

Việc trải qua trọn vẹn sự kiện AABW Hackathon giống hệt như một chuyến tàu lượn siêu tốc về mặt cảm xúc (emotional rollercoaster). Đây không chỉ là một khóa học, đây là một thao trường thực sự.

####  Đấu trí và Cọ xát kỹ thuật cực độ (Hands-on Technical Pressure)
- Bắt đầu với sự hoang mang (Overwhelmed): 2 giờ đầu tiên là khoảng thời gian kinh khủng nhất khi đứng trước một "vùng biển lớn" các dịch vụ AWS và không biết phải lắp ghép chúng như thế nào. Nhưng ngay sau khi bản thiết kế trên bảng trắng được chốt, mọi người rơi vào trạng thái dòng chảy (In the zone) - tiếng gõ phím vang lên liên tục không ngừng nghỉ.
- Đối mặt với khủng hoảng: Trải nghiệm code báo lỗi liên tục lúc 3 giờ sáng, quên commit code lên Github dẫn đến conflict từa lưa, hay pha "đứng tim" khi vô tình push file **.env** chứa mật khẩu lên public repo... Đó là những kinh nghiệm xương máu không một giảng đường hay sách vở nào dạy được.

####  Tinh thần đồng đội và Mở rộng mối quan hệ (Networking and Collaboration)
- Áp lực khủng khiếp đã gắn kết những con người xa lạ. Việc cùng nhau nhai vội miếng gà rán KFC lúc nửa đêm, đi dạo quanh khuôn viên Vinhomes lúc 2h sáng để đầu óc tỉnh táo lại, và động viên nhau sửa từng dòng bug đã tạo nên một sợi dây liên kết tuyệt vời.
- Giao lưu với các đội thi khác và các mentor từ AWS giúp mình nhận ra kiến thức của mình còn quá nhỏ bé, nhưng đồng thời cũng thấy rõ con đường mình cần đi để trở thành một Solution Architect thực thụ.

####  Sự giác ngộ sau sự kiện (The Pride)
- Khoảnh khắc nhìn thấy sản phẩm của team thực sự hoạt động, có thể chat được, phân tích được hình ảnh, và xử lý được dữ liệu ngay trên Cloud là cảm giác tự hào (Proud) khó tả.
- Sự kiện này giúp mình phá vỡ giới hạn tâm lý: Mình từng nghĩ phải mất nhiều tháng để làm một sản phẩm AI phức tạp, nhưng Hackathon đã chứng minh rằng: Nếu bạn tập trung cao độ, phân bổ nguồn lực tốt và dùng đúng công cụ Cloud mạnh mẽ, bạn có thể biến một ý tưởng điên rồ thành hiện thực chỉ trong vỏn vẹn 24 giờ đồng hồ.

####  Một vài hình ảnh tại Sự kiện (Event photos)
<div style="display: flex; justify-content: center; gap: 10px;">
  <img src="/images/4-Event/z8093879699810_c69fefaf8ebc56abaa36cba73d596f48.jpg" style="width: 30%; object-fit: cover;" />
  <img src="/images/4-Event/z8093879709518_706d9214a0e85dbf18454836f36e3b10.jpg" style="width: 30%; object-fit: cover;" />
  <img src="/images/4-Event/z8093879712854_b2c5d2eca158a3ecabd73b0369e16770.jpg" style="width: 30%; object-fit: cover;" />
</div>




---
title: "Event 1: Agentic AI Build Week (AABW) Hackathon"
date: 2024-01-01
weight: 1
chapter: false
pre: " <b> 4.1. </b> "
---

# Summary Report: Agentic AI Build Week (AABW) Hackathon

### Event Objectives

- **Uncover the limitless potential of Agentic AI:** Moving beyond standard chatbots to autonomous agents that take action using the Amazon Web Services (AWS) ecosystem, particularly mastering **Amazon Bedrock**.
- **Experience the raw intensity of a 24-hour Hackathon:** Navigating the entire product lifecycle—from whiteboard ideation, coding the initial prototype, and 3 AM debugging sessions, to finalizing the pitch deck and executing a live demo in front of a judging panel.
- **Harden critical engineering skills:** Pushing the limits of problem-solving, architecting highly scalable systems while strictly adhering to cost optimization (FinOps), and sustaining intense teamwork under extreme time constraints.
- **Cultivate a "Customer-Obsessed" mindset:** True to AWS's leadership principles, the goal is to identify genuine business pain points first, and only then architect the technological solution to address them, rather than building technology for technology's sake.

### Teams & Speakers

In this unique AABW event, the spotlight was entirely on the hackathon participants. Instead of traditional keynote speakers, the teams themselves took the stage to present groundbreaking solutions engineered in just a single day:
- **Team OneTeam (Winner):** Anh Duy, Tran Dong, Doan Trung, Minh Viet, Anshul Roy.
- **Team 3KA:** Huỳnh An Khương, Nguyễn Quốc Huy, Ngô Quang Khôi, Hoàng Lê Thành Đức, Đặng Nguyễn Phước Lộc, Đặng Trường Hưng.
- **Team Plan V:** Pham Tien Thuan Phat, Huynh Hoang Long, Le Minh Nghia, Tran Dai Vi, Nguyen An.
- **Dream AI Team:** Le Tan Luc, Do Hoang Hieu, Trieu Quoc Hao, Nguyen Van Duy Khiem, Nguyen Cong Minh, Nguyen Tran Minh Quan.

---

### Key Highlights

The core of the event revolved around deep technical dissections of the top 4 products. Each team tackled a distinct industry domain with exceptionally creative architectural solutions.

#### 1. Revolutionizing F&B Automated Ordering - OneTeam (KFC Bot Agent)

**The Problem (The Systemic Failure of Conversational Ordering):**
- The F&B industry faces immense hurdles with automation. OneTeam underscored this by pointing out that McDonald’s ended its AI drive-thru trial in over 100 US locations. The fundamental lesson? **Ordering is an inherently complex system problem, not just an AI language problem.**
- **Natural language is messy** (users use slang, typos, and fragmented sentences), but **business rules are unforgivingly strict** (e.g., combos have specific beverage rules, vouchers are time-bound).
- **The Journey of the Lost Order:** When a customer is casually chatting and feels hungry, forcing them to switch from their social app to download a proprietary app introduces fatal friction (login walls, slow menus). This disruption kills momentum, resulting in a lost order. Meanwhile, human-only chat support simply cannot scale during traffic spikes.

**The Modern Architecture Solution (KFC Bot Agent):**
- **Zero Friction (No App, No Account):** Customers customize and place orders directly within their native chat environment (Zalo OA, Messenger).
- **The 5-Step Agentic Model (The Model understands, the Tools decide what is real):** 
  1. **Goal:** Comprehend the true intent behind messy human text.
  2. **Plan:** Orchestrate the necessary sequence of API calls.
  3. **Tools:** Interrogate trusted backend databases.
  4. **Act:** Modify the live shopping cart and apply business logic (promotions).
  5. **Verify:** Cross-check the AI's output against the actual cart state to prevent hallucinations.
- **"Design Once, Deploy Everywhere" Architecture:** 
  - **Ingestion Layer:** Web Application Firewall (WAF) -> API Gateway -> Lambda -> SQS (to decouple and ensure no message is dropped during surges).
  - **AgentCore Runtime:** Powered entirely by **Amazon Bedrock** for intent parsing, orchestration, and tool execution.
  - **Memory & Data Layer:** Session states maintained in DynamoDB, full-text search via OpenSearch Service, caching through ElastiCache, and strict data encryption managed by KMS.

**Impact:** The architecture achieved a blazingly fast end-to-end latency of **3-5 seconds**, absurdly low operational costs of **$0.006 per order** (totaling roughly **$88/month** for infrastructure), and a staggering **60% reduction** in manual infrastructure code thanks to Bedrock's automatic routing.

#### 2. Proactive Crowd & Security AI Monitoring - Team 3KA (S.H.E.P.H.E.R.D)

**The Problem:**
- Venue operators currently rely on security personnel staring at dozens of monitors. This approach is highly reactive, painfully slow, impossible to scale, and heavily prone to human fatigue, leading to missed incidents and an inability to predict imminent congestion.

**The Solution & Technology:**
- **S.H.E.P.H.E.R.D** (Smart Human-flow Evaluation, Prediction, Hazard Detection, Response, and Dispatch) directly ingests live camera feeds and transforms them into actionable operational metrics.
- **Core Capabilities:** Real-time object tracking, precise crowd density measurement, queue condition estimation, congestion pressure forecasting (15 minutes ahead), and proactive alerting.
- **Architecture:** 
  - **Computer Vision Layer:** Employs **YOLO + ByteTrack** for high-fidelity object detection and trajectory tracking.
  - **Cloud Inference:** Heavy machine learning tasks execute on **Amazon SageMaker**.
  - **Agentic AI Layer:** Uses **Amazon Bedrock AgentCore + Strands Agent** to forge an "Operator Copilot." This allows staff to query the system using natural language (e.g., "Is the main lobby getting crowded?") and receive data-backed answers instantly. The real-time dashboard was built with **React**.

**Technical Challenges & Triumphs:**
- The team candidly shared their brutal challenges: having absolutely no AI background, using AWS for the very first time, struggling to maintain a reliable video stream to the cloud, and battling inference latency. They overcame these hurdles with 5 cans of Redbull and relentless debugging sessions that lasted until 3:00 AM.

#### 3. Automating System Architecture - Team Plan V (SA Professional Native App)

**The Problem:**
- In the fast-paced tech industry, a Solution Architect (SA) is constantly hit with demands like: "Design a secure AI system for me by Thursday!"
- The traditional workflow is exhausting: SAs must manually read lengthy Business Requirement Documents (BRD/PRD), start architecting from a blank page, spend hours dragging and dropping icons in diagram tools, and finally guess the AWS cost estimation based on fragmented pricing tables.

**The Breakthrough Solution:**
- The **Solution Architect Professional AI Native App**.
- **Intelligent Workflow:**
  - The app ingests natural language prompts and document files, utilizing AI for rigorous Requirement Extraction.
  - It drafts high-level, hybrid-cloud aware architectures that inherently align with corporate security standards.
  - It automatically generates raw XML code to render editable **Draw.io** diagrams using official AWS architecture icons.
  - It autonomously writes Infrastructure as Code (IaC) templates (Terraform/CloudFormation).
  - It computes highly specific, directional AWS cost estimates (e.g., tailored for the `ap-southeast-1` region).
- SAs no longer stare at a blank page. They use a chat sidebar to iteratively refine and critique the AI’s high-quality first draft, compressing days of architectural design into mere minutes.

#### 4. Corporate Strategic Signal Intelligence - Dream AI Team (Signal Scout)

**The Problem:**
- In the B2B enterprise space, C-level executives struggle to detect early strategic pivots, executive reshuffles, or market shifts of their competitors because critical signals are buried in scattered press releases, financial reports, and social media.

**The Solution (Signal Scout):**
- A self-service executive dashboard that automates the tracking of target corporations.
- The system aggregates thousands of fragmented signals, cleanses the data, and weaves them into a transparent, chronological narrative. Crucially, every AI-generated conclusion is strictly evidence-backed.
- It empowers core business decisions: Maintain current strategy, Adapt to the shift, or Accelerate investments.

**Architecture & the Art of FinOps (Cost Optimization):**
- Data scraping and validation via LangFuse, TinyFish, and Apify.
- Dream AI stunned the judges with their rigorous financial planning. They architected three precise monthly operational tiers on AWS:
  - **Minimum Scenario:** ~ $81/month (AWS infrastructure accounting for only $17). Leverages DynamoDB, API Gateway, and Lambda for maximum cost efficiency.
  - **Medium Scenario:** ~ $94/month.
  - **Maximum Scenario:** ~ $359/month (Assuming maximum throughput on Bedrock tokens and AgentCore Runtime).

---

### Core Lessons Learned (Key Takeaways)

#### 1. Product Design Mindset
- **Business-First Approach:** Team OneTeam (KFC) proved that Large Language Models (LLMs) are just the tip of the iceberg for understanding text; the true engine must handle unforgiving business logic (inventory checks, cart states, voucher validation). Dream AI (Signal Scout) reinforced this by prioritizing "verifiable transparency" above all else to cater to C-suite executives.
- **Bounded Contexts & Divide and Conquer:** Building a massive system in 24 hours requires ruthless prioritization. Team 3KA succeeded because they severely limited their MVP scope to monitoring a single camera feed rather than trying to build a global surveillance network.

#### 2. Technical Architecture Insights
- **The Power of Agentic AI:** We are moving past Generative AI chatbots that merely generate text. With AgentCore, AI now has the sequence: **Reasoning -> Tool Selection -> Action**. This means AI can directly write to databases, invoke payment gateways, or generate IaC, replacing massive chunks of traditional backend code.
- **Event-Driven Resilience:** To prevent system crashes during concurrent user spikes, deploying SQS (Simple Queue Service) as a buffer between API Gateway and Lambda is a classic, battle-tested pattern that the top teams executed flawlessly.
- **Mastering FinOps (Cost Estimation):** In the cloud, deploying without a budget leads to catastrophic billing surprises. Calculating costs down to the Bedrock token, DynamoDB read/write unit, and WAF request—as Dream AI demonstrated—is a critical survival skill for modern Cloud Engineers.

#### 3. Hackathon Survival Strategy
- **Small, Finished Work Beats Big, Broken Ideas:** It is infinitely better to present one buttery-smooth, fully functional feature than to pitch 10 grandiose ideas that result in a crashed app during the live demo. "Done" is better than "Perfect".
- **Preparation is Not Cheating:** Having boilerplate code, React templates, pre-configured AWS accounts, and strict role assignments (backend developer, frontend UI, pitch deck designer) is the secret weapon to beating the clock.
- **Networking & Human Connection:** The late-night struggles—accidentally pushing `.env` files to public GitHub repos, arguing over Git merge conflicts, and chugging 5 Redbulls at 3 AM—forge bonds and teach practical lessons that no university lecture can replicate.

---

### Applying Knowledge to Real Work

The technologies and philosophies showcased at this event are directly applicable to my daily work. I have mapped out the following action plan:
1. **Implement Agentic Workflows in Operations:** I will move beyond simple text-generation API calls. My next goal is to experiment with **Amazon Bedrock Agents** to orchestrate automated workflows (similar to Plan V's IaC generation). I plan to build a bot that can read CloudWatch error logs, reason through the stack trace, and automatically suggest code fixes directly in our team's Slack channel.
2. **Refactor Towards Event-Driven Architecture:** Instead of relying heavily on synchronous, monolithic API calls that bottleneck our applications, I will begin refactoring notification modules (email dispatch, report generation) to utilize **Amazon SQS** and **AWS Lambda** for asynchronous, highly scalable processing.
3. **Enforce FinOps Discipline:** Starting next month, before proposing any new AWS service deployment, I will force myself to build a comprehensive cost estimation spreadsheet (using the AWS Pricing Calculator) featuring at least two traffic scenarios (Low and High). This will mirror Team Signal Scout's approach and sharpen my business acumen.

---

### Event Experience (The Emotional Journey)

Participating in the **AABW Hackathon** was a true emotional rollercoaster. It was less of a tech conference and more of a technological proving ground.

#### 🧠 The Intense Mental & Technical Crucible
- **Overwhelmed at the Start:** The first two hours were terrifying. Staring into the vast ocean of AWS services without knowing how to piece them together was daunting. However, once the whiteboard architecture was locked in, the team entered a deep state of "flow"—the sound of typing didn't stop for hours.
- **Embracing the Chaos:** Experiencing cascading code failures at 3:00 AM, dealing with messy Git merge conflicts because someone forgot to commit, and the heart-stopping panic of almost exposing credentials... these are the visceral, high-stakes lessons that forge real engineers.

#### 🤝 Team Spirit & Networking
- **Bonds Forged in Fire:** The immense pressure united a group of strangers. Eating cold fried chicken at midnight, taking a 2:00 AM walk around the Vinhomes campus just to stay awake, and motivating each other to fix just one more bug created an incredible sense of camaraderie.
- **Learning from the Best:** Engaging with other teams and AWS mentors made me realize how much I still have to learn, but it also clearly illuminated the path I need to take to become a true Solution Architect.

#### 💡 The Pride of Creation
- **The 'Aha' Moment:** The exact moment our team's product actually worked—when the AI successfully analyzed data on the cloud and responded correctly—brought an indescribable feeling of pride.
- **Shattering Mental Barriers:** I used to believe that building a complex AI product required months of planning and development. This hackathon proved a profound truth: If you have intense focus, clear resource allocation, and the right Cloud tools, you can transform a crazy idea into a stunning, functional reality in exactly 24 hours.

#### 📸 A Few Memories from the Event
<div style="display: flex; justify-content: center; gap: 10px;">
  <img src="/images/4-Event/z8093879699810_c69fefaf8ebc56abaa36cba73d596f48.jpg" style="width: 30%; object-fit: cover;" />
  <img src="/images/4-Event/z8093879709518_706d9214a0e85dbf18454836f36e3b10.jpg" style="width: 30%; object-fit: cover;" />
  <img src="/images/4-Event/z8093879712854_b2c5d2eca158a3ecabd73b0369e16770.jpg" style="width: 30%; object-fit: cover;" />
</div>



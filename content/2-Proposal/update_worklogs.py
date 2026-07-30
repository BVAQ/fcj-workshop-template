import os
import shutil
import re

base_dir = r"d:\HK252\AWS\fcj-workshop-template\content\1-Worklog"

# Delete Week 8 and 9
for week in ["1.8-Week8", "1.9-Week9"]:
    path = os.path.join(base_dir, week)
    if os.path.exists(path):
        shutil.rmtree(path)
        print(f"Deleted {path}")

# Tasks for Ngươi A in Vietnamese (for _index.vi.md)
tasks_vi = {
    "1.1-Week1": [
        "- Đọc và thảo luận whitepaper thuật toán Raft.<br>- Phân tích đặc tả dự án awsplace.<br>- Khởi tạo repository: CMakeLists.txt, presets, GoogleTest.",
        "- Cài đặt CI/CD cơ bản (GitHub Actions).<br>- Thiết kế kiến trúc Network Server (epoll/kqueue).<br>- Soạn thảo PROTOCOL.md.<br>- Định nghĩa Error Codes và cơ chế Leader Redirect."
    ],
    "1.2-Week2": [
        "- Hiện thực src/net/tcp_server.cpp (Client Sessions, EPOLLIN/EPOLLOUT).<br>- Viết module phân tách gói tin (Frame Parser), xử lý TCP fragmentation/coalescing.",
        "- Hiện thực tầng Reliable UDP (rudp.cpp).<br>- Viết Unit test: Fuzzing TCP Parser để từ chối các gói tin sai định dạng."
    ],
    "1.3-Week3": [
        "- Xây dựng Core State Machine của Raft trong src/raft/node.cpp.<br>- Cài đặt bộ đếm thời gian ngẫu nhiên (Randomized Election Timeout).",
        "- Hiện thực chức năng nhận/gửi RequestVote RPC: Xử lý logic từ chối và chấp thuận vote, xử lý Split-brain."
    ],
    "1.4-Week4": [
        "- Nâng cấp AppendEntries RPC: Gửi kèm Log Entries.<br>- Tối ưu hóa gửi Batch để tăng thông lượng.",
        "- Hiện thực logic giải quyết xung đột (Conflict Resolution).<br>- Hiện thực cơ chế tính toán Commit Index."
    ],
    "1.5-Week5": [
        "- Đấu nối State Machine với tầng Network: Phản hồi client sau khi Committed.<br>- Xử lý lỗi NOT_LEADER để client tự kết nối lại.",
        "- Hiện thực các tập lệnh cơ bản trong src/engine/commands.cpp: GET, SET, EXISTS, DEL.<br>- Đảm bảo tính nguyên tử (Atomicity) cho thao tác ghi đè."
    ],
    "1.6-Week6": [
        "- Hiện thực hệ thống Snapshot (Copy-On-Write hoặc Stop-The-World).<br>- Đồng bộ Snapshot qua mạng (InstallSnapshot RPC).",
        "- Tích hợp cơ chế khôi phục (Restore): Nạp Snapshot vào RAM và replay WAL."
    ],
    "1.7-Week7": [
        "- Triển khai E2E Integration Test với Docker Compose và Go Server.<br>- Sử dụng TSan và ASan để rà soát lỗi bộ nhớ.",
        "- Phát triển test Fuzzing (fuzz_tcp_frame.cpp) đảm bảo server không Crash.<br>- Cấu hình tối ưu độ trễ TCP (TCP_NODELAY)."
    ]
}

# Tasks for Ngươi A in English (for _index.md)
tasks_en = {
    "1.1-Week1": [
        "- Read and discuss Raft algorithm whitepaper.<br>- Analyze awsplace project specifications.<br>- Initialize repository: CMakeLists.txt, presets, GoogleTest.",
        "- Setup CI/CD (GitHub Actions).<br>- Design Network Server architecture (epoll/kqueue).<br>- Draft PROTOCOL.md.<br>- Define Error Codes and Leader Redirect mechanism."
    ],
    "1.2-Week2": [
        "- Implement src/net/tcp_server.cpp (Client Sessions, EPOLLIN/EPOLLOUT).<br>- Write Frame Parser module, handle TCP fragmentation/coalescing.",
        "- Implement Reliable UDP layer (rudp.cpp).<br>- Write Unit tests: Fuzzing TCP Parser to reject malformed packets."
    ],
    "1.3-Week3": [
        "- Build Raft Core State Machine in src/raft/node.cpp.<br>- Implement Randomized Election Timeout.",
        "- Implement RequestVote RPC logic: Handle vote rejection/approval, handle Split-brain."
    ],
    "1.4-Week4": [
        "- Upgrade AppendEntries RPC: Send Log Entries.<br>- Optimize Batch sending to increase throughput.",
        "- Implement Conflict Resolution logic.<br>- Implement Commit Index calculation mechanism."
    ],
    "1.5-Week5": [
        "- Connect State Machine to Network layer: Respond to client after Committed.<br>- Handle NOT_LEADER error for client reconnection.",
        "- Implement basic commands in src/engine/commands.cpp: GET, SET, EXISTS, DEL.<br>- Ensure Atomicity for overwrite operations."
    ],
    "1.6-Week6": [
        "- Implement Snapshot system (Copy-On-Write or Stop-The-World).<br>- Synchronize Snapshot over network (InstallSnapshot RPC).",
        "- Integrate Restore mechanism: Load Snapshot into RAM and replay WAL."
    ],
    "1.7-Week7": [
        "- Deploy E2E Integration Test with Docker Compose and Go Server.<br>- Use TSan and ASan to check for memory errors.",
        "- Develop Fuzzing tests (fuzz_tcp_frame.cpp) to ensure zero crashes.<br>- Optimize TCP latency (TCP_NODELAY)."
    ]
}

# Find all week folders
weeks = ["1.1-Week1", "1.2-Week2", "1.3-Week3", "1.4-Week4", "1.5-Week5", "1.6-Week6", "1.7-Week7"]

for week in weeks:
    # Process EN
    en_path = os.path.join(base_dir, week, "_index.md")
    if os.path.exists(en_path):
        with open(en_path, "r", encoding="utf-8") as f:
            content = f.read()
        
        # We need to find the table rows and append our new tasks.
        # Find the last row of the Tasks table.
        # Let's extract the start/end dates from the first task row of the week.
        match = re.search(r'\|\s*1\s*\|\s*-.*?\|\s*([\d\/]+)\s*\|\s*([\d\/]+)\s*\|', content)
        start_date = match.group(1) if match else "TBD"
        end_date = match.group(2) if match else "TBD"
        
        # We will add 2 rows.
        day1 = "6"
        day2 = "7"
        row1 = f"| {day1} | {tasks_en[week][0]} | {start_date} | {end_date} | RaftDB C++ Report |"
        row2 = f"| {day2} | {tasks_en[week][1]} | {start_date} | {end_date} | RaftDB C++ Report |"
        
        # Insert before "\n### Achievements:"
        if "\n### Achievements:" in content:
            content = content.replace("\n### Achievements:", f"{row1}\n{row2}\n\n### Achievements:")
        
        with open(en_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated {en_path}")

    # Process VI
    vi_path = os.path.join(base_dir, week, "_index.vi.md")
    if os.path.exists(vi_path):
        with open(vi_path, "r", encoding="utf-8") as f:
            content = f.read()
        
        match = re.search(r'\|\s*1\s*\|\s*-.*?\|\s*([\d\/]+)\s*\|\s*([\d\/]+)\s*\|', content)
        start_date = match.group(1) if match else "TBD"
        end_date = match.group(2) if match else "TBD"
        
        day1 = "6"
        day2 = "7"
        row1 = f"| {day1} | {tasks_vi[week][0]} | {start_date} | {end_date} | Báo cáo C++ RaftDB |"
        row2 = f"| {day2} | {tasks_vi[week][1]} | {start_date} | {end_date} | Báo cáo C++ RaftDB |"
        
        if "\n### Thành tựu:" in content:
            content = content.replace("\n### Thành tựu:", f"{row1}\n{row2}\n\n### Thành tựu:")
        
        with open(vi_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated {vi_path}")

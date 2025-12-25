import subprocess
import datetime

# 1. Cấu hình
SERVICE_NAME = "apache2"
LOG_FILE = "/var/log/apache_monitor.log"

def log_message(message):
    """Hàm ghi log kèm thời gian"""
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a") as f:
        f.write(f"[{now}] {message}\n")

def check_and_restart():
    # 2. Kiểm tra trạng thái service
    # Chạy lệnh: systemctl is-active apache2
    result = subprocess.run(
        ["systemctl", "is-active", SERVICE_NAME], 
        capture_output=True, 
        text=True
    )
    
    status = result.stdout.strip()
    
    # 3. Xử lý logic
    if status == "active":
        print(f"{SERVICE_NAME} dang chay tot.")
    else:
        print(f"CANH BAO: {SERVICE_NAME} da dung! Dang khoi dong lai...")
        log_message(f"CRITICAL: {SERVICE_NAME} is DOWN. Restarting service...")
        
        # Lệnh khởi động lại
        subprocess.run(["systemctl", "start", SERVICE_NAME])
        
        # Ghi log kết quả
        log_message(f"INFO: {SERVICE_NAME} has been restarted successfully.")

if __name__ == "__main__":
    check_and_restart()
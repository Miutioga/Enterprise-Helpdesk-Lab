#!/bin/bash

# 1. Khai báo biến
BACKUP_DIR="/var/backups/osticket"
DB_NAME="database_name"      
DB_USER="user_name"             
DB_PASS="*******"
DATE=$(date +%Y-%m-%d_%H-%M-%S)
FILE_NAME="backup_$DATE.sql"

# 2. Thực hiện Backup (Dump)
echo "Dang tien hanh backup database..."
mysqldump -u $DB_USER -p$DB_PASS $DB_NAME > $BACKUP_DIR/$FILE_NAME

# 3. Kiểm tra kết quả
if [ $? -eq 0 ]; then
   echo "Backup thanh cong! File luu tai: $BACKUP_DIR/$FILE_NAME"
else
   echo "Backup THAT BAI!"
fi
copy gpsLogger.service to /etc/systemd/system

sudo systemctl daemon-reload          # Reload systemd to recognize the new service file
sudo systemctl enable gpsLogger.service  # Enable the service to start on boot
sudo systemctl start gpsLogger.service

sudo systemctl status gpsLogger.service

copy rtcSync.service to /etc/systemd/system

sudo systemctl daemon-reload          # Reload systemd to recognize the new service file
sudo systemctl enable rtcSync.service  # Enable the service to start on boot
sudo systemctl start rtcSync.service

sudo systemctl status rtcSync.service
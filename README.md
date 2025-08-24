# Time and Location services

These are the various services run a raspberry pi to support getting the current time and location. It uses Real time clock hardware (DS3231) to syncronize the system clock on startup. It uses a NEO-6M gps to get the Latitude and Longitude and store them in a gps.json file. The system clock and gps.json info. is made available to AI LLM agents using the mcpTime and mcpGPS services.

## Deamon services setup

The time sync and GPS logging services are run as background systemd deamons.

### gpsLogger
copy gpsLogger.service to /etc/systemd/system

- sudo systemctl daemon-reload          # Reload systemd to recognize the new service file
- sudo systemctl enable gpsLogger.service  # Enable the service to start on boot
- sudo systemctl start gpsLogger.service

- sudo systemctl status gpsLogger.service

### rtcService
copy rtcSync.service to /etc/systemd/system

- sudo systemctl daemon-reload          # Reload systemd to recognize the new service file
- sudo systemctl enable rtcSync.service  # Enable the service to start on boot
- sudo systemctl start rtcSync.service

- sudo systemctl status rtcSync.service

### mcpTime
copy mcpTime.service to /etc/systemd/system

- sudo systemctl daemon-reload          # Reload systemd to recognize the new service file
- sudo systemctl enable mcpTime.service  # Enable the service to start on boot
- sudo systemctl start mcpTime.service

- sudo systemctl status mcpTime.service
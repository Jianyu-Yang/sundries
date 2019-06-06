@TITLE BAT脚本例子2
@COLOR 7
@echo -----------TEST-----------
@echo=
@echo influxdb start
start /min /d "D:\Program Files\influxdb-1.7.6-1" influxd -config influxdb.conf
start /min /d "D:\Program Files\telegraf" telegraf -config telegraf.conf
start /min /d "D:\Program Files\grafana-6.1.6\bin" grafana-server.exe
start /min /d "D:\Program Files\chronograf-1.7.11_windows_amd64\chronograf-1.7.11-1" chronograf.exe
choice /t 5 /d y /n >nul
start Chrome http://localhost:8888
start Chrome http://localhost:3000
CALL ..\venv\Scripts\activate
START python ..\exporter.py
START prometheus --config.file=..\config\prometheus.yml

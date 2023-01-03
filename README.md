# Tesla Charger Metrics

## Getting Started

### Exporter
```shell
exporter.py
```

### Prometheus
```shell
prometheus --config.file=config\prometheus.yml
```

### Grafana
Start Grafana Service...

```shell
grafana-server -homepath "C:\Program Files\GrafanaLabs\grafana" -config "config\grafana.ini"
```

## Endpoints
- [Exporter](http://localhost:5000)
- [Grafana](http://localhost:3000)
- [Prometheus](http://localhost:9090)

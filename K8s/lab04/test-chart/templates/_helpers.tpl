{{- define "test-chart.labels" -}}
app.kubernetes.io/name: {{ .Chart.Name }}
app.kubernetes.io/instance: {{ .Release.Name }}
{{- end -}}

{{- define "test-chart.fullname" -}}
{{ printf "%s-%s" .Release.Name .Chart.Name }}
{{- end -}}
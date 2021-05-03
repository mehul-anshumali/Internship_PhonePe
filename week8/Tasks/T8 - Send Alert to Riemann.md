# Metrics such as disk usage/ram usage/HWM etc should have a threshold (80%) and should send a critical alert to riemann once the threshold is breached.
- ## Script:- https://github.com/mehul-anshumali/Internship_PhonePe/blob/main/week8/Tasks/scripts/send_riemann.py
- Define the function in script to change the state according to the usage-percentage of metrics. 
  ```python
  def find_state(metric_percent):
    if metric_percent < 40:
        return 'ok'
    elif metric_percent >= 40 and metric_percent <= 80:
        return 'warning'
    else:
        return 'critical'
  ```

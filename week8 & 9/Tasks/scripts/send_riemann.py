import psutil as ps, bernhard, requests, json

host = '192.168.159.43'
# Client connection
r_client = bernhard.Client()

metrics_dict =  dict()

def send_to_riemann(service, metric, state):
    r_client.send({'host': host, 'service': service, 'metric': metric, 'state': state})

def collect_metrics():
    '''
    metrics_list = [
             'cpu_usage_percentage',
             'ram_usage',
             'disk_usage',
             'swap_usage',
             'rabbitmq_queues',
             'rabbitmq_hwm'
         ]
    '''
    cpu = ps.cpu_percent(interval=0.5)
    update_metrics_dict('cpu_usage_percentage', cpu, cpu)

    ram_usage = ps.virtual_memory().total - ps.virtual_memory().available
    update_metrics_dict('ram_usage', ram_usage, ps.virtual_memory().percent)
    
    swap_usage = ps.swap_memory().used
    update_metrics_dict('swap_usage', swap_usage, ps.swap_memory().percent)

    memory = ps.disk_usage('/')
    update_metrics_dict('disk_usage', memory[1], memory.percent)

    '''
    Collecting RMQ metrics
    '''
    get_queue = "queues/%2f"
    get_hwm = "nodes"

    queue_response = make_request_to_rmq(get_queue)
    hwm_response = make_request_to_rmq(get_hwm)
    
    json_data = json.loads(queue_response.text) 

    for queue in json_data:
        # Update metrcics dictionary
        update_metrics_dict(queue['name'] + str('(Queue Messages)'), queue['messages'], '')
    
    json_data = json.loads(hwm_response.text) 

    for node in json_data:
        mem_used = node['mem_used']
        # Calculating RabbitMQ memory usage per node.
        mem_usage_percent = (mem_used / (1024 ** 2)) / (410/100)
        
        # Update metrcics dictionary
        update_metrics_dict(node['name'] + str('(Memory Used)'), node['mem_used'], mem_usage_percent)
   
    '''
    Collected RMQ metrics
    '''
    for service, metrics in metrics_dict.items():
            for list in range(len(metrics)-1):
                metric = metrics[list]
                state = metrics[list+1]
                
            # Sending the metrics to riemann ser
            send_to_riemann(service, metric, state)

def make_request_to_rmq(endpoint):
    api = "http://{}:{}/api/".format(host, 15672)
    headers = {'Content-type': 'application/json'}
    response = requests.get(url = api+endpoint ,auth=('mehul', 'mehul'), headers=headers)

    return response
    

def update_metrics_dict(service_name, metric_value, metric_value_percent):
    if metric_value_percent:
        metrics_dict.update({service_name : [metric_value, find_state(metric_value_percent)]})
    else: 
        metrics_dict.update({service_name : [metric_value, '']})

def find_state(metric_percent):
    if metric_percent < 40:
        return 'ok'
    elif metric_percent >= 40 and metric_percent <= 80:
        return 'warning'
    else:
        return 'critical'


collect_metrics()




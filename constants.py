from lib2to3.pgen2.token import COLON, SLASH

# NFV service name
NFV_FACE_DETECTION_SERVICE_NAME = "face-detection"
NFV_BACKGROUND_BLUR_SERVICE_NAME = "background-blur"
NFV_SOURCE_STREAMING_SERVICE_NAME = "source-streaming"
NFV_MATCH_AUDIO_VIDEO_SERVICE_NAME = "match-av"
NFV_TRANSCODER_SERVICE_NAME = "transcoder"

#Transcoder resolution
R_1080P = 1080
R_720P = 720
R_480P = 480
R_360P = 360
R_144P = 144

# HOST IP
MASTER_HOST = "localhost"
MASTER_USERNAME = "controller"
MASTER_PASSWORD = "1"
PI_IP = "192.168.101.48"
PI_USERNAME = "pi"
PI_PASSWORD = "1"
SERVER_IP = "192.168.101.101"
SERVER_USER = "server"
PI4_IP = "192.168.101.17"
PI4_USER = "pi4"

# CALCULATING_HOSTNAME = "server"
# CALCULATING_INSTANCE = "192.168.101.101"

# PORT
PROMETHEUS_PORT = "8080"

# Common
COLON = ":"
SLASH = "/"
TEST_MODE = False

# Network interfacte
NETWORK_INTERFACE = "ens33"

PROMETHEUS_DOMAIN = "http://" + MASTER_HOST + \
    COLON + PROMETHEUS_PORT + "/api/v1/query?query="
SERVICE_DOMAIN = "http://detection.default.svc.cluster.local"

# QUERY
VALUE_POD_STATUS_QUERY = "kube_pod_status_phase{job='kube-state-metrics',namespace='default'}"
VALUE_POD_TERMINATE_QUERY = "kube_pod_container_status_terminated{job='kube-state-metrics',namespace='default',container='user-container'}"
VALUES_CPU_QUERY = "100-(avg%20by%20(instance,job)(irate(node_cpu_seconds_total{{mode='idle',job='node_exporter',instance='{}:9100'}}[30s])*100))"
VALUES_PODS_QUERY = "kubelet_running_pods{{kubernetes_io_hostname='{}'}}"
VALUES_MEMORY_QUERY = "((node_memory_MemTotal_bytes{{job='node_exporter',instance='{}:9100'}}-node_memory_MemAvailable_bytes{{job='node_exporter',instance='{}:9100'}})/(node_memory_MemTotal_bytes{{job='node_exporter',instance='{}:9100'}}))*100"
RUNNING_PODS_QUERY = "kubelet_running_pods{{kubernetes_io_hostname='{}'}}"
POD_STATUS_PHASE_QUERY = "kube_pod_status_phase{namespace='capture',job='Kubernetes'}"
VALUES_NETWORK_RECEIVE_QUERY = "rate(node_network_receive_bytes_total{{device='" + \
    NETWORK_INTERFACE+"',instance='{}:9100'}}[1m])/(1024*1024)"

# FOLDER
SERVER_FOLDER = "server"
DATA_UMMETER_FOLDER = "data_ummeter"
PULLING_TIME_FOLDER = "pulling_time"
PI4_FOLDER = "pi4"

# FILE NAME
POD_START_TIME_FILENAME = "pod_start_time_{}_{}.csv"
DATA_PROMETHEUS_AT_SERVER_FILENAME = "data-prometheus_{}_{}_server.csv"
DATA_PROMETHEUS_AT_PI4_FILENAME = "data-prometheus_{}_{}_pi4.csv"
TIMESTAMP_FILENAME = "timestamps_{}_{}_server.csv"
DATA_UMMETER_FILENAME = "data_ummeter_{}_{}.csv"
DATA_PULLING_IMAGE_FILENAME = "data_pulling_image_{}_{}.csv"

# DIRECTORIES
DATA_DIRECTORY = "/home/controller/knative-caculation/data/"
POD_START_TIME_DATA_FILE_DIRECTOR = DATA_DIRECTORY + POD_START_TIME_FILENAME
DATA_PROMETHEUS_AT_SERVER_FILE_DIRECTORY = DATA_DIRECTORY + \
    SERVER_FOLDER + SLASH + DATA_PROMETHEUS_AT_SERVER_FILENAME
DATA_PROMETHEUS_AT_PI4_FILE_DIRECTORY = DATA_DIRECTORY + \
    PI4_FOLDER + SLASH + DATA_PROMETHEUS_AT_PI4_FILENAME
DATA_UMMETER_FILE_DIRECTORY = DATA_DIRECTORY + \
    DATA_UMMETER_FOLDER + SLASH + DATA_UMMETER_FILENAME
TIMESTAMP_DATA_FILE_DIRECTORY = DATA_DIRECTORY + \
    SERVER_FOLDER + SLASH + TIMESTAMP_FILENAME
PULLING_TIME_DATA_FILE_DIRECTORY = DATA_DIRECTORY + \
    PULLING_TIME_FOLDER + SLASH + DATA_PULLING_IMAGE_FILENAME

DATA_PROMETHEUS_FILE_DIRECTORY = "/home/controller/knative-caculation/data/{}/{}/data_prom_target_pod_{}_repeat_time_{}_video_{}_{}_{}.csv"
DATA_TIMESTAMP_FILE_DIRECTORY = "/home/controller/knative-caculation/data/timestamp/{}/{}/data_timestamp_target_pod_{}_repeat_time_{}_video_{}_{}_{}.csv"

# COMMAND
START_UMMETER_CMD = '/usr/bin/python3 /home/controller/knative-caculation/usbmeter.py --addr 00:16:A5:00:0F:65 --out /home/controller/knative-caculation/data/data_ummeter/data_ummeter_{}_{} --time {}'
UPDATE_REPLICAS_CMD = '/usr/bin/python3 /home/controller/knative-caculation/main_rebuild.py changevalue {} {} {}'
RUN_UMMETER_AT_PI4_CMD = "/usr/bin/python3 /home/pi/knative-caculation/run_on_pi4/usbmeter.py {} {} {} {}"

# STATUS
COLD_START_STATUS = "cold_start"
COLD_DONE_STATUS = "cold_done"
COLD_END_STATUS = "cold_end"
WARM_START_STATUS = "warm_start"
WARM_DONE_STATUS = "warm_done"
WARM_END_STATUS = "warm_end"
DELETE_START_STATUS = "delete_start"
DELETE_DONE_STATUS = "delete_done"
POD_DELETE_AFTER_STATUS = "pods_deleted_after"
PENDING_STATUS = "Pending"
RUNNING_STATUS = "Running"
TERMINATING_STATUS = "Terminating"

NULL_PROCESSING = "null_processing"
COLD_PROCESSING = "cold_processing"
COLD_AFTER_DEPLOY_PROCESSING = "cold_after_deploy"
COLD_TO_WARM_PROCESSING = "cold_to_warm_processing"
COLD_START_PROCESSING = "cold_start_processing"
WARM_PROCESSING = "warm_processing"
WARM_TO_COLD_PROCESSING = "warm_to_cold_processing"
ACTIVE_PROCESSING = "active_processing"
DELETE_PROCESSING = "delete_processing"

COLD_JOB = "cold"
COLD_AFTER_DEPLOY_JOB = "cold_after_deploy"
COLD_TO_WARM = "cold_to_warm"
WARM_JOB = "warm"
WARM_TO_COLD_JOB = "warm_to_cold"
ACTIVE_JOB = "active"
DELETE_JOB = "delete"

########################## Rebuild ######################
# State
NULL_STATE = "empty"
COLD_START_STATE = "cold_start"
WARM_STATE = "warm"
COLD_STATE = "cold"
ACTIVE_STATE = "active"

# Action

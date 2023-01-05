from kubernetes import client, config
config.load_kube_config()
AppV1 = client.AppsV1Api()

body = (
    client.V1Deployment(
        api_version="apps/v1",
        kind="Deployment",
        metadata=client.V1ObjectMeta(
            name="source-streaming-deployment"
        ),
        spec=client.V1DeploymentSpec(
            selector=client.V1LabelSelector(
                match_labels={"app":"source-streaming-deployment"}
            ),
            template=client.V1PodTemplateSpec(
                metadata=client.V1ObjectMeta(
                    labels={"app":"source-streaming-deployment"}
                ),
                spec=client.V1PodSpec(
                    containers=[client.V1Container(
                        name="source-streaming",
                        image="hctung57/source-streaming-ffmpeg:1.0",
                        ports=[client.V1ContainerPort(
                            container_port=1935,
                            name="container-port"
                        )]
                    )]
                )
            )
        )
        
    )
)
resp = AppV1.create_namespaced_deployment(
            body=body, namespace="default")
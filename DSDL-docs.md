 PDF To Markdown Converter
Debug View
Result View
Splunk
®
App for Data Science and Deep Learning
Use the Splunk App for Data Science and Deep
Learning 5.2.
Generated: 10/09/2025 12:44 pm

Copyright (c) 2025 Splunk LLC All Rights Reserved

Table of Contents
Table of Contents
About the Splunk App for Data Science and Deep Learning...........................................................................................
Splunk App for Data Science and Deep Learning overview......................................................................................
How the Splunk App for Data Science and Deep Learning can help you..................................................................
Splunk App for Data Science and Deep Learning architecture.................................................................................
Splunk App for Data Science and Deep Learning advanced architecture and workflow...........................................
Splunk App for Data Science and Deep Learning components...............................................................................
Install and configure the Splunk App for Data Science and Deep Learning.................................................................
Install or upgrade the Splunk App for Data Science and Deep Learning................................................................
Configure the Splunk App for Data Science and Deep Learning.............................................................................
Install and configure the Splunk App for Data Science and Deep Learning in an air-gapped environment............
and Deep Learning................................................................................................................................................. Reduce system load by managing and retrieving search result caches in the Splunk App for Data Science
Configure OpenShift integration for the Splunk App for Data Science and Deep Learning.....................................
Configure Kubernetes integration for the Splunk App for Data Science and Deep Learning..................................
Splunk App for Data Science and Deep Learning certificate settings and JupyterLab password...........................
Set up the Splunk App for Data Science and Deep Learning using AWS and EKS................................................
Firewall requirements for the Splunk App for Data Science and Deep Learning.........................................................
Firewall requirements for Splunk and Docker communication.................................................................................
Firewall requirements for Splunk and Kubernetes communication..........................................................................
Use the Splunk App for Data Science and Deep Learning.............................................................................................
Leverage the examples provided in the Splunk App for Data Science and Deep Learning....................................
Splunk App for Data Science and Deep Learning example workflow......................................................................
Develop a model using JupyterLab.........................................................................................................................
Using multi-GPU computing for heavily parallelled processing...............................................................................
Splunk App for Data Science and Deep Learning commands.................................................................................
Performance tuning and handling large datasets....................................................................................................
Advanced HPC and GPU usage..............................................................................................................................
Extend the Splunk App for Data Science and Deep Learning with custom notebooks...........................................
Container monitoring and logging............................................................................................................................
Container management and scaling........................................................................................................................
Advanced container customization..........................................................................................................................
Model governance and security in the Splunk App for Data Science and Deep Learning......................................
Splunk App for Data Science and Deep Learning Assistants........................................................................................
Using the Neural Network Designer Assistant.........................................................................................................
Using the Deep Learning Text Classification Assistant...........................................................................................
Using the Deep Learning Text Summarization Assistant......................................................................................
LLM-RAG Assistants........................................................................................................................................................
About LLM-RAG....................................................................................................................................................
Set up LLM-RAG...................................................................................................................................................
Set up additional LLM-RAG configurations............................................................................................................
About the compute command................................................................................................................................
LLM-RAG use cases..............................................................................................................................................
Use Standalone LLM............................................................................................................................................. LLM-RAG Assistants
Use Standalone VectorDB.....................................................................................................................................
Use Document-based LLM-RAG...........................................................................................................................
Use Function Calling LLM-RAG.............................................................................................................................
Encode data into a vector database......................................................................................................................
Query LLM with vector data...................................................................................................................................
Troubleshooting...............................................................................................................................................................
Troubleshoot the Splunk App for Data Science and Deep Learning.....................................................................
Additional resources........................................................................................................................................................
Support for the Splunk App for Data Science and Deep Learning........................................................................
Learn more about the Splunk App for Data Science and Deep Learning..............................................................
About the Splunk App for Data Science and Deep Learning...........................................................................................
Splunk App for Data Science and Deep Learning overview......................................................................................
The Splunk App for Data Science and Deep Learning (DSDL) is a free app you can download from Splunkbase.

The Splunk App for Data Science and Deep Learning (DSDL) extends the Splunk platform to provide advanced analytics,
machine learning, and deep learning, by leveraging external containerized environments and popular data science
frameworks.

DSDL supports prebuilt Docker containers that ship with libraries including TensorFlow, PyTorch, NLP, and classical
machine learning tools. These containers allow for more resource-intensive tasks to run externally, freeing your Splunk
search head from heavy computational loads.

DSDL supports building, training, and operationalizing models with or without GPU acceleration. DSDL also preserves
familiar Splunk Machine Learning Toolkit (MLTK) commands, making the end-to-end model development process
cohesive and intuitive, all while integrating into your existing Splunk workflows.

The following image shows a high-level workflow you can follow when using DSDL:

The Splunk App for Data Science and Deep Learning is not a default solution, but a way to create custom machine
learning models. It's helpful to have domain knowledge, Splunk Search Processing Language (SPL) knowledge, Splunk
platform experience, Splunk Machine Learning Toolkit (MLTK) experience, and Python and Jupyter Lab Notebook
experience when using DSDL.
Splunk App for Data Science and Deep Learning features

DSDL can enhance your data analytics capabilities in the following ways:

Empowering advanced analytics: Access advanced data science, machine learning, and deep learning tools
within the Splunk environment.
•
Optimizing resources: Offload computationally intensive tasks to external computing resources to prevent
overburdening your Splunk infrastructure performance when completing other critical tasks. Choose computing
resources that best fit your needs, whether on-premises servers, cloud-based solutions, or specialized hardware.
•
Streamlining workflows: Integrate data ingestion, model development, training, and deployment within a single,
unified platform, reducing the complexity of managing multiple tools.
•
Facilitating collaboration: Collaborate effectively by sharing models, code, and insights within your team using
integrated tools like Jupyter notebooks and MLflow. Empower data scientists and analysts to work together more
effectively with shared tools and environments.
•
Enhancing scalability: Easily scale computational resources to handle growing data volumes and more complex
models.
•
Enhancing observability: Monitor and troubleshoot your models and infrastructure using Splunk Observability
tools, ensuring reliability and optimal performance.
Requirements for the Splunk App for Data Science and Deep Learning

In order to successfully run the Splunk App for Data Science and Deep Learning, the following is required:

Splunk Enterprise 8.2.x or higher, or Splunk Cloud Platform.
Installation of the correct version of the Python for Scientific Computing (PSC) add-on from Splunkbase.
♦ Mac OS environment.
♦ Windows 64-bit environment.
♦ Linux 64-bit environment.
•
Installation of the Splunk Machine Learning Toolkit app from Splunkbase.
An internet connected container environment:
Docker: Set up a straightforward environment, typically without Transport Layer Security (TLS), for
smaller or development use cases.
♦
Kubernetes: Orchestrate larger-scale environments using TLS-enabled Kubernetes clusters. For
example, Amazon EKS or Red Hat OpenShift. This option provides secure, scalable deployment of
containers.
♦
•
Using predefined workflows

DSDL provides predefined JupyterLab Notebooks for building, testing, and operationalizing models within the Splunk
ecosystem. DSDL supports both CPU and GPU containers to address diverse performance needs. You can interact with
your data in the following ways:

Pulling data directly from Splunk into JupyterLab using the Splunk REST API for interactive exploration.
Pushing data from Splunk searches into the container environment for structured model development using
mode=stage.
•
Splunk App for Data Science and Deep Learning roles

The Splunk App for Data Science and Deep Learning includes the following 2 roles:

Role name Description
mltk_container_user
This role inherits from default Splunk platform user role and extends it with 2 capabilities:
Ability to list container models as visible on the container dashboard.
Ability to start or stop containers.
mltk_container_admin
This role inherits capabilities from mltk_container_user and also has the following capability:
Ability to access the setup page and make configuration changes.
To learn more about managing Splunk platform users and roles, see Create and manage roles with Splunk Web in the
Securing Splunk Enterprise manual.

Splunk App for Data Science and Deep Learning permissions

The Splunk App for Data Science and Deep Learning includes the following 3 permissions:

Permission Description
configure_mltk_container Ability to access the setup page and make configuration changes.
list_mltk_container Ability to list container models as visible on the container dashboard.
control_mltk_container Ability to start or stop containers.
Splunk App for Data Science and Deep Learning restrictions

The DSDL model-building workflow includes processes that occur outside of the Splunk platform ecosystem, leveraging
third-party infrastructure such as Docker, Kubernetes, OpenShift, and custom Python code defined in JupyterLab. Any
third-party infrastructure processes are out of scope for Splunk platform support or troubleshooting.
See the following table for DSDL app limitations and restrictions:

App limitation or
restriction
Description
Docker, Kubernetes, and
OpenShift environments The architecture only supports Docker, Kubernetes, and OpenShift as target container environments.
No indexer distribution
Data is processed on the search head and sent to the container environment. Data cannot be processed in a
distributed manner, such as streaming data in parallel from indexers to one or many containers. However, all
advantages of search in a distributed Splunk platform deployment still exist.
Security protocols Data is sent from a search head to a container over HTTPS protocol. Splunk administrators must take steps tosecure the setup of DSDL and container environment accordingly.
Atomar container model Models created using the Splunk App for Data Science and Deep Learning (DSDL) are atomar in that each modelis served by one container.
Global model sharing Models must be shared if they need to be served from a dedicated container. Set the model permission to Global.
Model naming convention Model names must not include white spaces for model configuration to work properly.
How the Splunk App for Data Science and Deep Learning can help you..................................................................
The Splunk App for Data Science and Deep Learning (DSDL) extends the Splunk platform to provide advanced analytics,
machine learning, and deep learning by leveraging external containerized environments and popular data science
frameworks.

DSDL can help you in the following ways:

Advanced analytics and machine learning integration
Seamless data handling
Model training and deployment
Integration and automation
Container environment options
Advanced analytics and machine learning integration

DSDL includes the following options to perform advanced analytics and machine learning integration:

Option Description
Option Description
Deep learning
frameworks
Incorporate libraries such as TensorFlow, PyTorch, and Keras for neural network tasks like image recognition and
natural language processing (NLP).
External computing
resources
Offload resource-intensive computations to external container environments, optionally leveraging GPUs for
accelerated model training.
Data science
environments
Use tools such as JupyterLab, MLflow, and optionally Spark, and TensorBoard for development, experimentation,
and visualization.
Seamless data handling

DSDL offers the following data handling options:

Option Description
Data ingestion Ingest and index data at scale, in real time or batch mode, using Splunk.
In-place data
transformation Use Splunk Search Processing Language (SPL) to clean, enrich, and transform data at the source.
Pull data into notebooks Use the Splunk REST API to execute SPL searches within JupyterLab.
Push data to the notebook Use staging commands such as DSDL container. | fit MLTKContainer mode=stage... to transfer data from Splunk to the
Feature engineering Leverage SPL or Python-based transformations to create refined features for improved model accuracy.
Model training and deployment

DSDL includes the following model training and deployment options:

Option Description
Model training Execute model training on GPU or CPU enabled containers, mitigating Splunk search head load and speeding up deeplearning.
Inference
execution Perform inference in the external container environment and pull results back into the Splunk platform or dashboards.
Results integration Return inference outputs to the Splunk platform using the Splunk HTTP Event Collector (HEC) for real-time monitoring.
Integration and automation

DSDL supports the following integrations to other apps and products:

Integration Description
Splunk REST API Dynamically pull data into notebooks or from Splunk, fostering an iterative approach.
Splunk HTTP Event Collector
(HEC) Stream inference results and logs back into Splunk for further analysis and alerting.
DSDL API Run model training and inference commands from the Splunk search head, while containers handle thecompute.
Notebook environments Develop and monitor experiments using Jupyter, and optionally MLflow, Spark, and TensorBoard.
Splunk Observability Monitor containers, inference processes, and performance metrics to ensure a stable and efficientdeployment.
Container environment options

DSDL offers the following container environments options:

Container
option
Description
Docker Set up a straightforward environment, typically without Transport Layer Security (TLS), for smaller or development usecases.
Kubernetes Orchestrate larger-scale environments using TLS-enabled Kubernetes clusters such as Amazon EKS or Red Hat OpenShift.This option provides a secure, scalable deployment of containers.
Splunk App for Data Science and Deep Learning architecture.................................................................................
The Splunk App for Data Science and Deep Learning (DSDL) allows you to integrate advanced custom machine learning
and deep learning systems with the Splunk platform.

The following image shows where DSDL fits into a machine learning workflow:

The Splunk App for Data Science and Deep Learning offers an integrated architecture with the Splunk platform. In the
following diagram, the architecture is represented as follows:

The Splunk platform is represented on the far left in the black box.
The container environment is represented in the center of the diagram in the light blue box.
The Splunk Observability Suite is represented in a labeled box in the top right of the diagram.
DSDL connects your Splunk platform deployment to a container environment such as Docker, Kubernetes, or OpenShift.
With the help of the container management interface, DSDL uses configured container environment APIs to start and stop
development or production containers. DSDL users can interactively deploy containers based on need, and access those
containers over external URLs from JuypterLab, or other browser-based tools like TensorBoard, MLflow, or the Spark
user interface for job tracking.

The development and production containers offer additional interfaces, most importantly endpoint URLs that facilitate
bi-directional data transfer between the Splunk platform and the algorithms running in the containers. Optionally,
containers can send data to the Splunk HTTP Event Collector (HEC) or app users can send ad-hoc search queries to the
Splunk REST API to retrieve data interactively in Juypter for experimentation, analysis tasks, or modeling.

An optional function is having all container endpoints get automatically instrumented with OpenTelemetry, and analyzed in
the Splunk Observability Suite. Additionally the container environment can be monitored in the Splunk Observability Suite
for further operational insights such as memory load and CPU utilization.

Splunk App for Data Science and Deep Learning advanced architecture and workflow...........................................
The Splunk App for Data Science and Deep Learning (DSDL) processes data through containerized environments,
manages logs and metrics, and scales to support enterprise-level model training and inference.

The following are some key concepts for working with DSDL:

DSDL concept Description
ML-SPL search
commands The fit, apply, and summary commands that trigger container-based operations in DSDL.
DSDL container A Docker, Kubernetes, or OpenShift pod running advanced libraries such as TensorFlow or PyTorch.
Data exchange The process where data flows from the Splunk search head to the container through HTTPS, with results returningthe same way.
Notebook workflows JupyterLab notebooks that define custom code for runtime. fit and apply functions, exported into Python modules at
Overview

When you use DSDL, the Splunk platform connects to an external container environment such as Docker, Kubernetes, or
OpenShift, to offload compute-intensive machine learning and deep learning workloads. This design allows you to achieve
the following outcomes:

Use GPUs for faster training and inference.
Scale horizontally by running multiple containers concurrently.
Isolate resource-heavy tasks from main processes for the Splunk platform.
Monitor container logs, performance metrics, and model lifecycle within the Splunk platform or other observability
platforms.
•
Architecture

The following diagram illustrates a typical DSDL setup in a production environment.

While the specifics differ slightly across Docker, Kubernetes, or OpenShift platforms, the core components remain the
same.

Architecture
component
Description
Splunk search head
Hosts Splunk App for Data Science and Deep Learning, Splunk Machine Learning Toolkit (MLTK), and the Python
for Scientific Computing (PSC) add-on.
Allows users to run the SPL searches that trigger container-based training or inference.
Container environment
Can be a single Docker host, or a cluster orchestrated by Kubernetes or OpenShift.
DSDL automatically starts and stops containers or pods based on user requests or scheduled
searches.
Machine learning libraries
Contains Python, TensorFlow, PyTorch, and more in Docker images or pods.
Can optionally use GPUs for acceleration if the environment supports it.
Route, services, and ports Allow communication to flow over HTTPS from the Splunk search head to the container's API endpoint, then backto the Splunk platform with results.
Data lifecycle

DSDL data undergoes the following lifecycle:

Lifecycle stage Description
Run an SPL search
A user runs a search in the Splunk platform with an ML-SPL command.
Example:
index=my_data
| fit MLTKContainer algo=my_notebook epochs= ...
into app:my_custom_model
Prepare data
The Splunk platform retrieves the relevant data from indexes. For example, the date from the _time field and
feature_* columns.
If mode=stage is specified, the data is staged to the container environment for interactive
development in JupyterLab.
Call Container API
The DSDL app packages data and metadata such as features and parameters, into CSV and JSON, then sends it to
the container over HTTPS.
In Kubernetes or OpenShift, this is typically a route or service endpoint. In Docker, it might be a
TCP port such as port 5000.
Run model training or
inference
The container reads the data, loads the relevant Python code as defined in a Jupyter notebook or .py module, and runs
training or inference using TensorFlow, PyTorch, or other libraries.
Send results and logs
When complete, the container sends metrics and model output back to the Splunk platform.
You can also stream logs through the HTTP Event Collector (HEC), or ingest container logs for
debugging.
Lifecycle stage Description
Store model If you used re-apply them later or track training metrics in the Splunk platform.into app:<model_name>, the model artifacts such as weights and config are persisted so you can
Container lifecycle

Review the following descriptions of a container lifecycle:

Lifecycle stage Description
Launch container
In developer (DEV) mode run | fit MLTKContainer algo=... mode=stage to launch a container with
JupyterLab, TensorBoard, and other dev tools. You can open Jupyter in a browser for iterative
notebook development.
In production (PROD) mode, when you omitmode=stageor explicitly set a production container,
DSDL typically launches a minimal container that runs only the required services without Jupyter. This
conserves resources and reduces the attack surface.
Stop and clean up
container
In many orchestration platforms such as Kubernetes, DSDL container management automatically stops or scales down
pods after idle time, or when tasks complete.
In Docker, containers might remain running for certain user sessions. You can stop them manually in
DSDL or in the Splunk platform.
Log containers and
collect metrics
If you use the HTTP Event Collector (HEC), the container can push logs or custom metrics back to the Splunk platform.
If you use Splunk Observability Cloud or other monitoring solutions, you can track CPU, GPU, and
memory usage for each container or pod.
Multi-container scaling and GPU usage options

DSDL includes the following options for container scaling and GPU:

Option Description
Horizontal scaling
Kubernetes : Kubernetes supports scaling from the container management interface.You can define multiple replicas of the
DSDL container if your workload is concurrency-based with many inference jobs. DSDL might spawn multiple pods in
parallel for large scheduled searches.
Docker : Docker is typically limited to a single container per host unless you orchestrate multiple Docker
hosts.
OpenShift : OpenShift supports scaling from the container management interface.
Acceleration
Docker : If your Docker host has GPUs and uses the NVIDIA runtime, DSDL can run GPU-enabled images.
Kubernetes : Kubernetes supports node labeling for GPU nodes, which allows GPU-based pods to
schedule automatically.
OpenShift : OpenShift supports node labeling for GPU nodes and automatic scheduling after device
plugins are configured.
Tuning resource
requests
CPU and memory limits : In Kubernetes and OpenShift, specify CPU and memory requests and limits in your container
image or deployment.
GPU requests : For GPU usage, define nvidia.com/gpu in the container resource spec file, letting the
scheduler handle GPU allocation.
Monitoring and logging options

DSDL integrates with Splunk platform logging and observability to facilitate troubleshooting, performance analysis, and
real-time metrics capturing.

Option Description
Container logs in the
Splunk platform
You can aggregate the standard container stdout and stderr logs with Splunk Connect for Kubernetes, a Docker
logging driver, or a manually configured HEC endpoint.
Check container logs to diagnose training or inference failures such as Python exceptions, and
out-of-memory errors.
Metrics and observability
Using Splunk Observability Cloud, integrate your container environment for real-time dashboards such asCPU,
memory, disk I/O, and network.
Track your metrics with built-in tools. For Docker, use docker stats. For Kubernetes, use kubectl
top pods/nodes. For OpenShift, the web console provides metrics.
Training and inference
telemetry
Use notebooks to push custom metrics like training loss, or accuracy per epoch back into the Splunk platform.
You can create dashboards or alerts in the Splunk platform to track these metrics and detect
model drift or performance issues.
Checking pre-container
startup logs in the Splunk
platform
If you suspect network timeouts or container launch failures before the container becomes fully available, search for
error messages in Splunk internal logs:
index=_internal "mltk-container"
This search reveals any error messages generated by DSDL container management, such as:
Network timeout which indicates firewall or network configuration issues blocking connections to the
container environment.
Platform errors which show if the Docker or Kubernetes API returned an error code.
TLS or certificate problems which show any SSL handshake or certificate mismatch issues during
container setup.
Note: By reviewing _internal logs for mltk-container, you can diagnose pre-launch issues that might not appear in the
container's own logs if the container never successfully started. Look for repeated attempts to connect, timeouts, or
permission errors to pinpoint the root cause.
Architecture best practices

See the following best practices for your DSDL architecture:

Best practice Details
Separate your development and
production environments
Maintain a development container environment for notebook exploration, and a separate, minimal
environment for production inference.
Use GPU nodes for deep learning tasks Ensure GPU scheduling is configured so you can significantly reduce training time.
Log everything
Route container logs to the Splunk platform for quick debugging and performance monitoring. For
example stdout, stderr, and training logs.
Monitor the _internal logs for mltk-container to spot pre-startup or network issues.
Manage the container lifecycle Clean up or scale down containers after tasks finish to avoid unnecessary resource usage.
Secure data flows Use TLS or HTTPS for traffic between the Splunk platform and containers. Set up firewall rules to
restrict traffic to authorized IPs.
Best practice Details
Version your notebooks Maintain a Git or CI/CD pipeline for your Jupyter notebooks to keep track of changes and ensurereproducibility.
See also

Learn how to create custom notebook code for specialized algorithms and integrated ML-SPL commands. See Extend the
Splunk App for Data Science and Deep Learning with custom notebooks.

Splunk App for Data Science and Deep Learning components...............................................................................
The Splunk App for Data Science and Deep Learning (DSDL) enhances your data analytics capabilities with advanced
analytics, external computing resources, streamlined workflows, model collaboration, and model monitoring.

DSDL is comprised of the following components:

Splunk Machine Learning Toolkit (MLTK) app and Python for Scientific Computing (PSC) add-on
Splunk search head with DSDL installed
External containerized environment
Integration components
Splunk Machine Learning Toolkit app and Python for Scientific Computing add-on

DSDL relies on both the Splunk Machine Learning Toolkit (MLTK) and its dependency, the Python for Scientific
Computing (PSC) add-on. Both must be installed on your Splunk search head.

MLTK provides machine learning commands in the Splunk platform, including fit and apply, which are essential for
training and applying models within Splunk searches. MLTK also stores model names and manages non-DSDL models
trained directly on the search head. DSDL introduces the additional benefit of executing inference on external container
resources.

PSC supplies the Python libraries and dependencies required for scientific computing and machine learning tasks within
the Splunk platform.

Splunk search head with DSDL installed

DSDL is installed on the Splunk search head alongside MLTK and PSC, providing the interface and commands necessary
to integrate with external data science environments.

This set up provides the following benefits:

Centralized management: Configure data science tasks, manage models, and run searches from the Splunk
search head.
•
Extended capabilities: Offload inference and training to external containers, adding scalability and GPU
acceleration.
•
Shared resources: In a distributed setup, DSDL commands can be accessed by other search heads if
permissions are configured accordingly.
•
External containerized environment

DSDL connects the Splunk platform to an external, containerized environment where advanced computations take place.

This external containerized environment includes the following options and benefits:

Notebook environments: Run Jupyter, MLflow, and optionally Spark and TensorBoard.
GPU utilization: Speed-up deep learning tasks by taking advantage of GPU hardware.
Splunk REST API access: Execute SPL searches directly in notebooks for real-time data exploration. See
Creating searches using the REST API in the REST API Tutorials manual.
•
Integration components

DSDL can integrate with other components in the Splunk platform:

Splunk REST API: Enable interactive data retrieval from Splunk into the container environment.
Splunk HTTP Event Collector (HEC): Send inference results and logs back to Splunk.
DSDL API: Run model training and inference commands in external containers.
Splunk Observability: Monitor performance and container health using Splunk Observability tools.
Install and configure the Splunk App for Data Science and Deep Learning.................................................................
Install or upgrade the Splunk App for Data Science and Deep Learning................................................................
The Splunk App for Data Science and Deep Learning integrates advanced custom machine learning and deep learning
systems with the Splunk platform. Use the following directions to install or upgrade the Splunk App for Data Science and
Deep Learning.

Version dependencies

The Splunk App for Data Science and Deep Learning (DSDL) relies on the Splunk Machine Learning Toolkit (MLTK) app.
See the following table to ensure you are running compatible versions of the apps:

DSDL
version
MLTK app
version
PSC add-on
version
Python
version
Splunk platform version
5.2.
5.6.1 3.2.3, 3.2.4, or 4.2.3 3.
Splunk Enterprise 8.2.x, 9.0.x, 9.1.x, 9.2.x, 9.3.x, 9.4.x,
or 10.x,
or Splunk Cloud Platform
5.6.0 3.2.3, 3.2.4, or 4.2.3 3.
Splunk Enterprise 8.2.x, 9.0.x, 9.1.x, 9.2.x, 9.3.x, 9.4.x,
or 10.x,
or Splunk Cloud Platform
5.5.0 3.2.2 or 4.2.2 3.9 Splunk Enterprise 8.2.x, 9.0.x, 9.1.x, 9.2.x, or 10.x,or Splunk Cloud Platform
5.4.2 4.2.1 3
Splunk Enterprise 8.2.x, 9.0.x, 9.1.x, 9.2.x, 9.3.x, or
9.4.x,
or Splunk Cloud Platform
5.4.2 3.2.1 3
Splunk Enterprise 8.2.x, 9.0.x, 9.1.x, 9.2.x, 9.3.x, or
9.4.x,
or Splunk Cloud Platform
5.2.
5.6.1 3.2.3, 3.2.4, or 4.2.3 3.
Splunk Enterprise 8.2.x, 9.0.x, 9.1.x, 9.2.x, 9.3.x, 9.4.x,
or 10.x,
or Splunk Cloud Platform
5.6.0 3.2.3, 3.2.4, or 4.2.3 3.
Splunk Enterprise 8.2.x, 9.0.x, 9.1.x, 9.2.x, 9.3.x, 9.4.x,
or 10.x,
or Splunk Cloud Platform
5.5.0 3.2.2 or 4.2.2 3.9 Splunk Enterprise 8.2.x, 9.0.x, 9.1.x, 9.2.x, or 10.x,or Splunk Cloud Platform
5.4.2 4.2.1 3
Splunk Enterprise 8.2.x, 9.0.x, 9.1.x, 9.2.x, 9.3.x, or
9.4.x,
or Splunk Cloud Platform
5.4.2 3.2.1 3
Splunk Enterprise 8.2.x, 9.0.x, 9.1.x, 9.2.x, 9.3.x, or
9.4.x,
or Splunk Cloud Platform
5.2.0 5.6.1 3.2.3, 3.2.4, or 4.2.3 3.9 Splunk Enterprise 8.2.x, 9.0.x, 9.1.x, 9.2.x, 9.3.x, 9.4.x,
or 10.x,
or Splunk Cloud Platform
DSDL
version
MLTK app
version
PSC add-on
version
Python
version
Splunk platform version
5.6.0 3.2.3, 3.2.4, or 4.2.3 3.
Splunk Enterprise 8.2.x, 9.0.x, 9.1.x, 9.2.x, 9.3.x, 9.4.x,
or 10.x,
or Splunk Cloud Platform
5.5.0 3.2.2 or 4.2.2 3.
Splunk Enterprise 8.2.x, 9.0.x, 9.1.x, 9.2.x, 9.3.x, or
9.4.x,
or Splunk Cloud Platform
5.4.2 4.2.1 3
Splunk Enterprise 8.2.x, 9.0.x, 9.1.x, 9.2.x, 9.3.x, or
9.4.x,
or Splunk Cloud Platform
5.4.2 3.2.1 3
Splunk Enterprise 8.2.x, 9.0.x, 9.1.x, 9.2.x, 9.3.x, or
9.4.x,
or Splunk Cloud Platform
5.1.2 5.4.0 3.1.0, 4.1.0, or 4.1.2 3 Splunk Enterprise 8.1.x, 8.2.x, 9.0.x, 9.1.x, or 9.2.x
or Splunk Cloud Platform
5.1.1 5.4.0 3.1.0, 4.1.0, or 4.1.2 3 Splunk Enterprise 8.1.x, 8.2.x, 9.0.0, 9.0.1, or 9.1.
or Splunk Cloud Platform
5.1.0 5.4.0 3.1.0, 4.1.0, or 4.1.2 3 Splunk Enterprise 8.1.x, 8.2.x, 9.0.0, or 9.0.
or Splunk Cloud Platform
5.0.
5.4.0 3.1.0 or 4.1.0 3 Splunk Enterprise 8.1.x, 8.2.x, 9.0.0, or 9.0.1or Splunk Cloud Platform
5.0.0 5.3.3 3.0.2, 3.1.0, 4.0.0, or4.1.0 3 Splunk Enterprise 8.1.x, 8.2.x, or 9.0.0or Splunk Cloud Platform
5.0.0 5.3.1 3.0.0, 3.0.1, or 3.0.2 3 Splunk Enterprise 8.0.x, 8.1.x, 8.2.x, or 9.0.0or Splunk Cloud Platform
5.0.0 5.3.0 3.0.0, 3.0.1, or 3.0.2 3 Splunk Enterprise 8.0.x, 8.1.x, 8.2.x, or 9.0.0or Splunk Cloud Platform
5.0.0 5.2.2 2.0.0, 2.0.1, or 2.0.2 3 Splunk Enterprise 8.0.x, 8.1.x, or 8.2.0or Splunk Cloud Platform
5.0.0 5.2.1 2.0.0, 2.0.1, or 2.0.2 3 Splunk Enterprise 8.0.x, 8.1.x, or 8.2.0or Splunk Cloud Platform
5.0.0 5.2.0 2.0.0, 2.0.1, or 2.0.2 3 Splunk Enterprise 8.0.x, 8.1.x, or 8.2.0or Splunk Cloud Platform
5.0.0 5.1.0 2.0.0, 2.0.1, or 2.0.2 3 Splunk Enterprise 8.0.x or 8.1.xor Splunk Cloud Platform
5.0.0 5.0.0 2.0.0, 2.0.1, or 2.0.2 3 Splunk Enterprise 8.0.x or 8.1.xor Splunk Cloud Platform
Where to install the Splunk App for Data Science and Deep Learning

The Splunk App for Data Science and Deep Learning works both for Splunk on-premises and Splunk Cloud Platform. You
must provide additional security and configurations such as IP address and port allow listing through ACS for Splunk
Cloud Platform. For distributed Splunk Enterprise deployments, install DSDL on the search head or search head cluster.
You don't need to install DSDL on indexers.

The two typical scenarios for setting up DSDL are single-instance and side-by-side:

Single-instance runs the containers on the same instance as the Splunk search head. This setup is useful for
local development purposes or for small to medium sized production environments.
•
Side-by-side is typically used for production environments where the search head connects to a dedicated
Kubernetes cluster or dedicated Docker host.
•
About search head load

While DSDL offloads major computational tasks like model training and inference to external containers, the following
activities still occur on the Splunk search head:

Search preparation: When data is prepared or staged, the search head handles SPL searches and organizes
data before sending it to the container.
•
Data transfer: Large datasets or frequent searches can affect search head performance if numerous staging
commands are running concurrently.
•
Local MLTK usage: If you run models directly on the search head using MLTK commands, resource usage can
spike, particularly during heavy training tasks.
•
Consider the following guidelines:

Configure a dedicated search head or scale appropriately when running frequent or large-scale model training
workloads.
•
Use the container-based approach provided by DSDL to reduce impact on core Splunk performance. For
example, mode=stage, GPU training.
•
To manage resource intensive MLTK training jobs, see Configure algorithm performance costs in the MLTK User
Guide
•
Install the Splunk App for Data Science and Deep Learning

DSDL installation includes both some prerequisites and installation steps. If you work in an air-gapped environment, see
Install and configure the Splunk App for Data Science and Deep Learning in an air-gapped environment.

Prerequisites

You must complete the following prerequisites to successfully run the Splunk App for Data Science and Deep Learning:

Splunk Enterprise 8.2.x or higher, or Splunk Cloud Platform.
Install the Splunk Machine Learning Toolkit (MLTK) app.
MLTK provides machine learning commands, such as fit and apply for model training, and manages
non-DSDL models trained directly on the search head.
♦
♦ Set the MLTK app permissions to Global so that knowledge objects are shared across the deployment.
•
Install the Python for Scientific Computing (PSC) add-on.
PSC supplies Python libraries and dependencies required for scientific computing and machine learning
tasks.
♦
•
A Docker or Kubernetes container environment.
An internet connection is required to pull the prebuilt Docker container images from the public Docker hub
repository.
♦
•
Installation steps

Follow these steps to install the Splunk App for Data Science and Deep Learning:

Download and install the Splunk App for Data Science and Deep Learning from Splunkbase.
Install the Splunk App for Data Science and Deep Learning from the Manage Apps tab. In Splunk Web, select
the Manage Apps icon next to Apps in the left navigation bar.
2.
On the Apps page, select Install app from file.
Select Choose File to navigate to and select the package file for the Splunk App for Data Science and Deep
Learning. Then click Open.
4.
Select Upload.
Restart your Splunk instance after installing the Splunk App for Data Science and Deep Learning.
Ensure your internet connected Docker, Kubernetes, or Openshift environment is accessible with permissions to
pull the prebuilt MLTK container images and start containers.
7.
Set up the Splunk App for Data Science and Deep Learning by connecting it to your environment using the
Configuration > Setup page of the app.
8.
Test the connection and save the configuration.
Start a development container from the Containers tab of the app.
Data is sent from a Splunk search head to containers using HTTPS for the endpoint URL. A self-signed
certificate is provided with the app which works with the prebuilt images. For further security requirements talk
to your system administrators about the set up of the app and your container environment.
10.
Depending on your selected image (Golden Image CPU or GPU), run one of the following examples from the
Examples tab to verify that the Splunk App for Data Science and Deep Learning is working:
♦ Neural Network Classifier Example for Tensorflow
♦ Logistic Regression Classifier Example for PyTorch
11.
Upgrade the Splunk App for Data Science and Deep Learning

The Splunk App for Data Science and Deep Learning (DSDL) regularly releases new features and enhancements. To
learn about features and enhancements by released version, see New features for the Splunk App for Data Science and
Deep Learning in the Release Notes manual.

Upgrade requirements

Running version 5.2.0 of DSDL requires Splunk Enterprise 8.2.x or higher, or Splunk Cloud Platform.

You must also be running version 5.4.2 or higher of the Splunk Machine Learning Toolkit (MLTK). MLTK relies on the
Python for Scientific Computing (PSC) add-on. For details on compatible versions of DSDL, MLTK, and PSC, see Version
dependencies.

Update the app in Splunk Web

In Splunk Web, an Update option shows on the app icon in the left-hand Apps menu when a new version of an app is
available on Splunkbase. Click that Update option to initiate the app update process.

Alternatively, you can perform the following steps:

Download the latest version of the app from Splunkbase.
In Splunk Web, click on the gear icon next to Apps in the left navigation bar.
On the Apps page, click Install app from file.
Click Choose File , navigate to and select the package file for the app or add-on, then click Open.
Check the Upgrade app box.
Click Upload.
(Optional) Run the Configuration > Setup of the app to make sure all container configuration is still valid and that
new configuration items are reflected after the app upgrade installation.
7.
Configure the Splunk App for Data Science and Deep Learning.............................................................................
The Splunk App for Data Science and Deep Learning (DSDL) extends the Splunk platform to enable advanced analytics,
machine learning, and deep learning capabilities by integrating with external containerized environments.

Before you can begin using DSDL you must set up at least one container environment. DSDL requires this external
containerized environment to execute resource-intensive computations, such as model training and inference. You can
choose Docker or Kubernetes based on your performance and security needs:

Docker configuration
Kubernetes configuration
You can also choose to set up the Splunk HTTP Event Collector (HEC) and the Splunk access token:

Configure HTTP Event Collector
Configure Splunk access token
Prerequisites

Before configuring DSDL both the Splunk Machine Learning Toolkit (MLTK) and the Python for Scientific Computing
(PSC) add-on must be installed on your Splunk search head. See Install the Splunk App for Data Science and Deep
Learning.

Configuration guidelines

Consider the following guidelines when making configuration changes to DSDL:

Item Details
SSL and TLS certificates • For production environments, provide your own certificates.
Configure certificate paths in the DSDL setup page for HTTPS connections.
Endpoint tokens and passwords
Set custom tokens and passwords for container endpoints such as API and Jupyter..
Rotate credentials regularly.
Item Details
Access controls • Limit Splunk access and HEC tokens to necessary indexes and roles.For Kubernetes, use Role-Based Access Control (RBAC) to manage permissions and enforce
network policies.
Docker configuration

If you have a single-instance Splunk deployment use Docker for development and testing purposes. Docker is ideal for
scenarios where it runs side by side with the Splunk search head on the same machine.

Docker limitations

Consider the following limitations if choosing to use Docker:

Security: Docker integration does not support Transport Layer Security (TLS) which might not meet security
requirements for production environments.
•
Scalability: Docker is less suitable for large-scale or production workloads as compared to Kubernetes.
Configuration steps

Complete the following steps to configure a connection to Docker:

Set up Docker environment. Install Docker on the host machine where the Splunk search head is running.
Make sure that the Docker daemon is running and accessible.
1.
Configure Docker settings in Splunk:
Setting Details
Docker host
Linux, same machine: unix://var/run/docker.sock
Windows or TCP access: tcp://localhost:2375
Remote Docker daemon: tcp://remote.host.com:2375
Endpoint URL The hostname or IP where containers will be accessible. For example localhost.
External URL If different from the endpoint URL, specify how containers are accessed externally.
Security Communication is unencrypted. Limit Docker to trusted or local environments.
2.
Kubernetes configuration

Choose Kubernetes for production environments where scalability, high availability, and security are critical. Kubernetes
allows you to orchestrate containers across multiple machines, providing resource utilization and reliability.

Kubernetes features

Using Kubernetes offers the following features:

Scalability: Scale resources on demand.
Security: Supports TLS communication and fine-grained access controls.
Flexibility: Compatible with various on-premises or cloud providers including EKS, OpenShift, GKE, and AKS.
Configuration steps

Complete the following steps to configure a connection to Kubernetes:

Set up a Kubernetes cluster. You can deploy a Kubernetes cluster using your preferred platform. Options include
but are not limited to Amazon Elastic Kubernetes Service (EKS), Red Hat OpenShift, Google Kubernetes Engine
(GKE), Azure Kubernetes Service (AKS), or your own on-premises deployment.
Ensure that the cluster is accessible and properly configured for your environment.
1.
Configure Kubernetes settings in Splunk:
Setting Description
Authentication Mode Cert & Key, User Token, AWS IAM, or other methods as supported by your cluster.
Cluster Base URL Typically https://<api-server-host>:6443.
Credentials Provide token or cert/key pair for secure communication.
Service Type LoadBalancer, NodePort, Route (OpenShift), or Ingress to expose DSDL containers.
Namespace Specify the Kubernetes namespace for DSDL container deployments.
2.
Container Deployment:
Use provided Kubernetes manifests or Helm charts to deploy DSDL containers in your cluster.
Adjust CPU and GPU resource limits, storage, and networking to match your requirements.
3.
Security:
Enable TLS for secure communications.
Use Role-Based Access Control (RBAC) to control permissions and network policies to restrict traffic.
4.
Test and troubleshoot the Docker or Kubernetes configuration

After completing the setup, test the connection between Splunk and the external container environment.

On the DSDL Configuration page , select Test & Save to validate connectivity with Docker or Kubernetes.
Verify that DSDL can communicate with the external environment:
1. Pull data: In a Jupyter Notebook, use SplunkSearch.SplunkSearch() to searchdata from Splunk.
Push data: Use | fit MLTKContainer mode=stage ... in Splunk to send datasets to the container
environment.
2.
2.
Troubleshoot the configuration

Try the following if you are experiencing issues with the configuration:

Check network connectivity and firewall settings.
Review Splunk logs and container logs for errors.
Verify that all tokens and credentials are correctly entered.
Configure HTTP Event Collector

Splunk HTTP Event Collector (HEC) allows external DSDL containers to send inference results and logs back to the
Splunk platform. For more information on HEC see Set up and use HTTP Event Collector in Splunk Web in the Splunk
Enterprise manual.

HEC security considerations

Review the following security considerations if choosing to use HEC:

SSL and TLS: Set up SSL and TLS for HEC to secure data transmission.
Token permissions: Restrict the HEC token to necessary indexes and source types.
Firewall settings: Ensure that the HEC port is properly secured and not exposed to untrusted networks.
HEC configuration steps

Complete the following configuration steps:

Enable HEC in Splunk:
Go to Settings, then Data Inputs , and then HTTP Event Collector.
Set All Tokens to Enabled.
(Optional) If required, also set SSL to Enabled.
1.
Create a new HEC token:
Provide a name, select a source type, and specify an index.
Copy the generated token value.
2.
Configure DSDL for HEC:
In the DSDL configuration, enable Splunk HEC.
Provide the HEC token and endpoint URL. For example https://<splunk-host>:8088.
3.
Configure Splunk access token

The Splunk access token allows JupyterLab Notebooks or other container environments to connect to Splunk using the
Splunk REST API, supporting interactive data pulls or staging commands.

Access token security considerations

Review the following security considerations if choosing to use Splunk access token:

Token permissions: Assign minimal necessary permissions to the API token.
Secure storage: Use environment variables or secure methods to store tokens in notebooks.
Access token configuration steps

Complete the following steps:

Create an API token in Splunk:
Go to Settings , then Tokens , and then select Create New Token.
Grant appropriate permissions and copy the generated token.
1.
Configure DSDL:
In the DSDL setup page, enable Splunk Access for Jupyter.
Provide the Splunk Access Token, host address, and management port. An example host address is
host.docker.internal. The default management port is 8089.
2.
Install and configure the Splunk App for Data Science and Deep Learning in an air-gapped environment............
For security or compliance reasons your organization might restrict outbound internet connections and operate an
air-gapped environment. The Splunk App for Data Science and Deep Learning (DSDL) can still run in these environments
by manually managing container images, having local Python dependencies, and making Splunk configuration steps
offline.

In a typical DSDL set up the following components are required:

Splunk Enterprise or Splunk Cloud with the Machine Learning Toolkit (MLTK) app and Python for Scientific
Computing (PSC) and add-on.
•
A container environment of Docker, Kubernetes, or OpenShift to run external code.
Internet access to pull official DSDL images from Docker Hub. For example
splunk-mltk-container-golden-image-cpu.
•
In an air-gapped environment you must complete the following in order to successfully set up and run DSDL:

Manually transfer container images to your private registry or local Docker host. See Offline container image
management.
•
Manually install MLTK, PSC, and other dependencies on Splunk. See Offline installation of MLTK, PSC, and
DSDL.
•
Access example notebooks offline. See Offline access of example notebooks.
Manage sending traces to Splunk Observability Cloud. See Observability and telemetry in air-gapped
environment.
•
Manage models offline. See Offline model management.
See also:

Example offline workflow
Troubleshoot DSDL in an air-gapped environment
DSDL in an air-gapped environment guidelines

Review these guidelines if you plan to use DSDL in an air-gapped environment:

Guideline Description
Document the transfer workflow Keep a written record of the process for how images are built, scanned, saved, and loaded in the offlineenvironment.
Use Git locally If you want versioning for your notebooks, store them in an on-premises Git server, or use secure copyprotocol (SCP) based workflows. See https://git-scm.com/.
Minimize image bloat Large images can be tedious to move offline. Only install the libraries you truly need.
Guideline Description
Test in a staging environment Validate each new container version or MLTK code change in a staging area before transferring to production.
Turn off features that rely on
external network calls
You might want to remove or turn off features that rely on external network calls such as downloading
notebook examples from GitHub, or certain tokens that require calling out to Splunk Observability tools.
Offline container image management

See the following sections for steps to manage offline containers:

Build or pull images on a connected host
Transfer to the air-gapped environment
Update available images in Splunk
Build or pull images on a connected host

Complete these steps to build or pull images on a connected host:

On a machine with internet choose 1 of these options:
Pull the official images from Docker Hub. For example
phdrieger/mltk-container-golden-image-cpu:5.1.0.
♦
Use scripts from [splunk-mltk-container-docker](#) to build custom images. For example build.sh,
bulk_build.sh.
♦
1.
If your security policy requires, scan the images for vulnerabilities. For example if using Trivy use using
scan_container.sh.
2.
Save the images to .TAR files.
Example: docker save phdrieger/mltk-container-golden-image-cpu:5.1.0 -o golden_cpu_5.1.0.tar
Example if using your own custom images:
docker save myregistry.local/golden-cpu-custom:5.2.0 -o golden_cpu_custom_5.2.0.tar
3.
Transfer to the air-gapped environment

Complete these steps to transfer images to the air-gapped environment:

Copy the .TAR files into the offline environment with a USB drive, secure network copy, or similarly secure option.
Load the images into your local Docker or private registry as shown in the following example: docker load -i
golden_cpu_custom_5.2.0.tar
2.
(Optional) If you want multiple hosts to pull the images, tag and push the images to an internal registry.
Example:
docker tag golden-cpu-custom:5.2.0 registry.local/golden-cpu-custom:5.2.0
docker push registry.local/golden-cpu-custom:5.2.0
3.
Update available images in Splunk

In DSDL, you must tell Splunk which images are available.

Complete these steps to update the available images in Splunk:

If you built images from [splunk-mltk-container-docker](#), generate an images.conf snippet using the
build.sh scripts. This is typically placed in the $SPLUNK_HOME/etc/apps/mltk-container/local/images.conf file.
1.
Edit it manually, referencing your new offline image tags.
Example:
[my_custom_image]
repo = registry.local/
image = golden-cpu-custom:5.2.0
runtime = none
short_name = Golden CPU Custom
Confirm that your container environment references the same local registry or Docker tags so DSDL can pull
them.
2.
Offline installation of MLTK, PSC, and DSDL

See the following table for how to complete an offline installation of required components:

Component Description
MLTK and PSC
Download the Splunk Machine Learning Toolkit (MLTK) app and Python for Scientific Computing (PSC) add-on SPL
packages from Splunkbase on a connected machine.
Then transfer the packages to your offline Splunk instance using removable media or secure file
copy. Install the packages in Splunk:
If using Splunk Web go to Manage Apps and choose Install app from file.
Or manually add the file in $SPLUNK_HOME/etc/apps/.
DSDL
Download the Splunk App for Data Science and Deep Learning (DSDL) SPL package from Splunkbase or from your
custom fork.
Then transfer the package to your offline Splunk instance using removable media or secure file
copy. Install the package in Splunk:
If using Splunk Web go to Manage Apps and choose Install app from file.
Or manually add the file in $SPLUNK_HOME/etc/apps/.
Additional Python
dependencies
If you have custom libraries in your Jupyter notebooks you must ensure they're in the container image. If you also rely
on PSC for local Splunk usage, confirm you've installed the correct PSC version offline.
Offline access of example notebooks

See the following table for how to access example notebooks offline:

Type of
notebook
How to access offline
Built-in example
notebooks
DSDL ships with example notebooks under $SPLUNK_HOME/etc/apps/<DSDL_app>/notebooks/. You can use the
notebooks offline if they're included in the default distribution.
Additional
examples from
GitHub
If you want extra examples from [splunk-mltk-container-docker/notebooks](#) or third-party sources, you must
manually download them from a connected machine, then place them in your offline environment. Note: DSDL's default
scripts will attempt to fetch updates from GitHub. Disable or remove those steps if you're fully offline.
Observability and telemetry in an air-gapped environment

If you're offline the container cannot automatically send Open Telemetry (Otel) traces to Splunk Observability Cloud. You
have the following options:

Skip Observability usage entirely in air-gapped mode.
Use a custom Observability Gateway on your intranet if you have a specialized network architecture.
You can still collect container logs in _internal or using local Docker drivers. HPC or dev logs can be manually
forwarded to Splunk if you have local connections.
Offline model management

See the following table for how to manage models offline:

Model function How to manage offline
Automatic notebook
and model sync
DSDL continues to store notebooks and models on the Splunk instance, unaffected by being offline. If ephemeral
containers vanish, you can relaunch them and retrieve the same code.
Versioning Even offline, you can keep your .IPYNB code in a local Git server or a secure copy protocol (SCP) workflow. Thisensures you can track and revert changes.
Container security
With no external net, scanning might be done on a staging machine. Ensure you replicate the same images in
production. Trivy or other scanners can run offline if you maintain local Common Vulnerabilities and Exposures (CVE)
databases.
Example offline workflow

The following is an example workflow when using DSDL with Docker in an air-gapped environment:

Prepare: On a connected host, build or pull your desired images.
Scan: Use scan_container.sh or a third-party product such as Trivy. See https://trivy.dev/latest/.
Save: Use docker save <your_image> -o <your_file>.tar.
Transfer: Copy .TAR files to the offline environment. Use a USB or other secure copy protocol (SCP).
Load: Use docker load -i <your_file>.tar.
Configure: Update the $SPLUNK_HOME/etc/apps/mltk-container/local/images.conf file or update using DSDL
container setup, referencing your local Docker tags.
6.
Install: MLTK, PSC, and DSDL .SPL packages offline in Splunk.
Use: Run | fit MLTKContainer algo=... referencing your offline container image. Notebooks and models
remain in Splunk's local storage for ephemeral container cycles.
8.
Troubleshoot DSDL in an air-gapped environment

Issue Likely cause Where to check
Cannot pull image:
not found
Image not loaded or incorrectly
tagged in the offline Docker registry.
Check Docker images. Confirm images.conf references the correct repo or
tag.
Splunk
Observability not
working
Container endpoints can't reach
Splunk Observability Cloud.
Observability is typically unavailable in a fully offline context unless a custom
local gateway is set up.
"No module named
X" in your Jupyter
code
Custom Python library not built into
the container image.
Rebuild or add library to requirements_files/ before docker build or
build.sh.
HPC nodes can't
see your local
registry
No local registry credentials or
misconfigured insecure-registry
flags.
Check Docker daemon config on HPC nodes, or add a CA cert if your local
registry uses TLS with a custom CA.
Issue Likely cause Where to check
Missing examples
or notebooks
The default DSDL examples are
present, but advanced examples
from GitHub are not included in your
offline environment.
Manually copy the advanced examples from GitHub from an internet host and
place them in $SPLUNK_HOME/etc/apps/dsdlt-app/notebooks/, or
container volume.
Reduce system load by managing and retrieving search result caches in the
Splunk App for Data Science and Deep Learning
When working with compute-intensive algorithms like large language models (LLMs), it is crucial to efficiently manage and
retrieve search results in order to reduce system load and ensure timely access to valuable insights.

The Splunk App for Data Science and Deep Learning (DSDL) version 5.2.1 introduce Search History that uses the
Splunk platform built-in summary index to persist and reuse expensive search results.

Benefits of using search history

Review the following table for benefits of the search history feature:

Benefit Description
Persist valuable outputs By default, search results in DSDL are not stored. If you need a result again, you must rerun the search. Usingsearch history saves search results for future access.
Performance and
efficiency
Storing results in a summary index means you can quickly retrieve previously processed data, reducing the need to
repeat resource-heavy computations. This is especially beneficial for algorithms that return lengthy text outputs or
when auditing past analyses.
Reuses standard Splunk
platform features
By using the Splunk platform built-in summary index, the feature ensures compatibility, reliability, and security for
your stored search data.
Turn on search history

To access previously cached search results in the Splunk App for DSDL, complete the following steps:

Turning on history for algorithms that output large numeric tables might lead to significant performance or storage
concerns. Consider selectively enabling this feature only where high resource consumption or frequent result reuse is
expected.
Turn on Essential Saved Searches in your Splunk platform instance. These settings are stored in the saved
searches settings:
♦ get_search_jobs_save_to_summary
♦ get_search_results_save_to_summary
1.
Select the algorithms you want to toggle on for history retention:
Edit the search_history_enabled_algos.csv lookup table containing both algo_name and algo_enabled.
Find the name of the algorithm you want to enable and set its value in the algo_enabled column to 1.
By default, only LLM algorithms have history enabled, because they often involve lengthy processing
times and generate extensive text outputs.
2.
After you turn on search history, the following changes take effect:

Results for selected algorithms are stored in summary indexes.
Users can retrieve these results instantly for quick analysis or auditing, without the need to rerun the original,
potentially expensive, search.
•
See also

For more information on how the Splunk platform summary index can accelerate searches and enhance data
management efficiency, see Use summary indexing for increased search efficiency.

Configure OpenShift integration for the Splunk App for Data Science and Deep Learning.....................................
Integrate the Splunk App for Data Science and Deep Learning (DSDL) with Red Hat OpenShift to run data science
workloads in a scalable, secure, and enterprise-ready manner. OpenShift provides a Kubernetes-based platform with
additional features such as Routes for external service exposure, integrated software-defined networking (SDN), and
robust role-based access control (RBAC). This integration is suitable for production environments where performance,
reliability, and security are essential.

For OpenShift documentation see https://docs.openshift.com/.

Prerequisites

The following prerequisites must be met to configure an OpenShift integration for DSDL:

Splunk Enterprise installed and running.
Splunk Machine Learning Toolkit (MLTK) and Python for Scientific Computing (PSC) installed on the Splunk
Enterprise instance.
•
DSDL installed on the Splunk Enterprise instance.
Access to an OpenShift cluster with appropriate permissions.
The OpenShift Container Platform command-line interface tool (oc) configured to interact with your OpenShift
cluster.
•
Network connectivity between the Splunk Enterprise instance and the OpenShift cluster.
OpenShift configuration guidelines

Consider the following guidelines if you are configuring OpenShift integration for DSDL:

Guideline Description
Secure authentication Use secure authentication rather than basic authentication for certificates or tokens.
Publicly signed certificates Using publicly signed certificates minimizes browser warnings and security risks.
Transport layer security (TLS)
termination
Match the container's certificate approach with Route settings. For example use passthrough for
self-signed, and reencrypt for custom certificates.
Permissions Assign minimal permissions to your service accounts or user tokens.
Component updates Keep OpenShift, MLTK, DSDL, and any containers updated to their latest and compatible versions to benefitfrom security fixes and performance improvements..
Monitor resources Use OpenShift's built-in monitoring or external tools to monitor CPU and memory usage.
Guideline Description
Network policies If you need advanced security, define that explicitly to control Pod traffic.
Project isolation Keep DSDL workloads in a dedicated project for clarity and resource governance.
NFS storage Optional. If you have an external NFS server, installing the NFS container storage interface (CSI) driver canenable a shared filesystem for DSDL data across Pods.
Set up an OpenShift cluster

Before integrating with DSDL, set up an OpenShift cluster that meets the following requirements:

Requirement Details
OpenShift version Version 4.x or higher is needed for compatibility with DSDL.
Networking Verify that Pods can communicate across the cluster using the integrated software-defined networking(SDN).
OpenShift uses an integrated SDN. Ensure proper configuration.
Ingress controller and routes OpenShift uses Routes for external services.
Ensure the default OpenShift Router is configured and can expose routes.
Persistent storage
DSDL requires PersistentVolumeClaims (PVCs) for model data and logs.
Set up a storage provisioner, such as NFS, OpenShift Container Storage, or other CSI
solutions.
Role-based access control
(RBAC) DSDL does not automate RBAC creation. You can manually assign RBAC details in the DSDL setup page.
Configuration steps

Complete the following steps to configure an OpenShift cluster:

Install an OpenShift cluster:
Use the OpenShift installer or an operator-based approach. See https://docs.openshift.com/.
Ensure nodes are active and can communicate..
1.
Configure networking:
Validate the integrated SDN configuration.
Confirm Pods can communicate across the cluster.
2.
Set up persistent storage:
Install a storage provisioner. For example OpenShift Container Storage, NFS CSI driver, or another CSI
solution.
1.
Create a StorageClass for dynamic PersistentVolumeClaim (PVC).
Test by creating a sample PVC to ensure it binds properly.
3.
Verify OpenShift router configuration:
Confirm the default router is running.
Configure wildcard DNS if needed for dynamic Route hostnames.
4.
Test cluster functionality:
Deploy a simple app to ensure services are reachable using Routes.
5.
(Optional) Use NFS for persistent storage

If you prefer to use Network File Storage (NFS) for shared persistent storage, you can configure an NFS CSI driver in
your OpenShift cluster. This setup is useful if you plan to run models in their dedicated containers and require storage to
be accessible by multiple containers.

Complete the following steps:

Install the NFS CSI driver. See https://github.com/kubernetes-csi/csi-driver-nfs.
See the following example:
oc apply -k "github.com/kubernetes-csi/csi-driver-nfs/deploy/kubernetes/overlays/stable?ref=master"
Adjust the path and version for your cluster.
1.
Configure an NFS server:
Ensure you have an NFS server accessible to OpenShift worker nodes.
Export a share, for example /srv/nfs, with the correct permissions.
2.
Create a StorageClass that references the NFS CSI driver, as shown in the following example:
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
name: nfs-csi
provisioner: nfs.csi.k8s.io
parameters:
server: <NFS_SERVER_IP_OR_HOSTNAME>
share: /srv/nfs
reclaimPolicy: Delete
volumeBindingMode: Immediate
Replace <NFS_SERVER_IP_OR_HOSTNAME> with your NFS server address.
3.
Verify that a PVC can bind using this storage class as shown in the following example: oc create -f - <<EOF
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
name: test-nfs
spec:
storageClassName: nfs-csi
accessModes:
ReadWriteMany
resources:
requests:
storage: 5Gi
EOF
Confirm the PVC transitions to Bound.
4.
Use the NFS StorageClass in your DSDL configuration:
In the DSDL Setup page, specify nfs-csi, or the name you created, as the Storage Class.
DSDL automatically creates PVCs using NFS for storing data and model artifacts.
5.
Configure DSDL for OpenShift

Once your cluster is ready, configure DSDL within Splunk Enterprise:

In DSDL, go to Configuration and then Setup.
Select OpenShift and enter your cluster details:
1. Authentication Mode. For example Cert & Key, User Token.
2.
Cluster Base URL. For example https://api.<cluster-domain>:6443.
Namespace. Use an OpenShift Project, for example dsdl-project.
Storage Class for PVCs. For example nfs-csi or ocs-storagecluster-ceph-rbd.
Service type: Typically Route in OpenShift for external exposure.
Route hostname: Provide a hostname. For example dsdl.apps.<cluster-domain> if you want a custom route.
Test and save: DSDL will attempt to deploy containers in your OpenShift project.
Automatic deployment

After saving the necessary details on the DSDL setup page in Splunk Enterprise, DSDL automatically deploys its
containers, persistent storage, and additional resources to your OpenShift cluster, simplifying the integration process.

Authentication modes

DSDL supports multiple authentication modes to connect to OpenShift. Choose the mode that best suits your
environment:

Authentication
mode
Details When to use
Certificate and Key
Cluster base URL:
https://api.<cluster-domain>:6443
Cluster certificate authority: Path to CA cert signing the
OpenShift API.
Client certificate or client key: Typically retrieved from oc
whoami --show-client-certificate and oc whoami
--show-client-key.
Use for strong, mutual TLS authentication.
Offers direct client certificates from OpenShift
or a custom CA.
User Token • Cluster base URL: The OpenShift API address.User token: Bearer token from a service account. For example,
oc sa get-token dsdl-user.
Use for quick setup with minimal certificate
handling. Ideal if you prefer to manage
service accounts with limited permissions.
User Login • User name and password: Basic authorization credentials.
Cluster CA: CA certificate.
Not suitable for production due to less secure
authentication.
Service Account
(In-Cluster) • Namespace: The project containing the service account.
Use if Splunk Enterprise itself is deployed
inside OpenShift.
Service types

In OpenShift, the common approach is using Routes, but NodePort is also supported:

Service
type
Details
Route Route hostname example: dsdl.apps.<cluster-domain>
TLS termination:
Use passthrough if you use self-signed certificates in the container.
Use edge or reencrypt if you have your own publicly signed certificates.
Note: Mismatching TLS termination with the container's certificate expectations can cause SSL handshake errors. For example, if
the container uses self-signed certificates, passthrough is often required.
Service
type
Details
NodePort Exposes a static port on each node. Common option for internal use or development and testing scenarios.
Namespace and resource management guidelines

See the following guidelines for namespace and resource management when using OpenShift:

Use oc new-project dsdl-project to create a new project for DSDL.
Specify dsdl-project as the Namespace in the DSDL Configuration page.
Adjust resource requests and set limits for large workloads.
Certificate guidelines

See the following guidelines for transport layer security (TLS) and certificate management when using OpenShift:

Self-signed certificates trigger browser warnings and potential vulnerabilities. For external production, use publicly
signed certificates such as Let's Encrypt, DigiCert, or an internal certificate authority (CA).
•
Generate or obtain certificates matching your domain.
Add the certificates to the certificates directory in your DSDL container build context. For example dltk.pem,
dltk.key.
•
Build and push a custom container image if needed.
Configure your Route for either reencrypt or edge TLS.
If you want to enforce domain matching enable Hostname Verification in DSDL.
Firewall considerations

Configure firewall rules to ensure secure communication between Splunk and OpenShift:

Component Description
OpenShift API Port 6443. Outbound traffic from Splunk to manage resources.
DSDL API Port 5000 or dynamically generated port. Bidirectional traffic for fit, apply, and summary commands.
Splunk REST API Port 8089. Use if the container-based notebooks or services call back to Splunk.
Splunk HTTP Event Collector (HEC) Port 8088 for on-premises or port 443 for Splunk Cloud.
When making any firewall rule changes, ensure the cluster nodes can reach Splunk on the relevant ports, and Splunk
can reach the cluster API.
Configure TLS in an OpenShift Sandbox

The following are example steps for using OpenShift Sandbox or a development trial environment and want Transport
Layer Security (TLS):

Set the Route to passthrough for DSDL notebooks including Jupyter and TensorBoard.
Extract the container's self-signed certificate with the command of openssl s_client -connect ... -showcerts.
Add the .pem path in the DSDL setup under Certificate Settings.
Manually create or delete PVCs in the sandbox if they get stuck.
TLS in an OpenShift Sandbox has the following limitations:

Only gp2 storage class is typically available. Storage classes such as gp3 or NFS might not be supported.
NodePort or advanced network settings might not be allowed.
You might need to manually configure pass-through routes for self-signed certificate usage.
Troubleshoot OpenShift configuration

Issue Troubleshoot
502 Bad Gateway or invalid and incomplete
response
This can be due to TLS mismatch or incorrect pass-through settings.
Ensure termination is set to passthrough if the container is using self-signed
certificates.
Authentication failures
Can occur because of incorrect tokens or expired service account.
Fix this by regenerating tokens and updating DSDL configuration. For example
oc sa get-token.
Service exposure problems
Can be caused by Route not pointing to the correct service or to an invalid TLS termination.
Check the router logs and verify that your Route's hostname and port are
correct.
Resource limitations
Pods can be stuck in "Pending" if there is insufficient CPU and memory or a lack of storage.
Scale your resources or adjust requests and limits..
Storage issues
Permanent Virtual Circuits (PVCs) can remain in "Pending" if no suitable StorageClass is
available.
For NFS, confirm the NFS CSI driver installation and server accessibility.
Verify the cluster's storage operator or logs for errors.
Configure Kubernetes integration for the Splunk App for Data Science and Deep Learning..................................
Integrate the Splunk App for Data Science and Deep Learning (DSDL) with a Kubernetes environment to run data science
workloads in a scalable and secure manner. Kubernetes provides container orchestration to manage and deploy
containerized applications across a cluster of machines. This integration is suitable for production environments where
performance, reliability, and security are critical.

For Kubernetes documentation see https://kubernetes.io/docs/home/.

Prerequisites

The following prerequisites must be met to configure a Kubernetes integration for DSDL:

Splunk Enterprise installed and running.
Splunk Machine Learning Toolkit (MLTK) and Python for Scientific Computing (PSC) installed on the Splunk
Enterprise instance.
•
DSDL installed on the Splunk Enterprise instance.
Access to a Kubernetes cluster with appropriate permissions.
The Kubernetes command-line tool (kubectl) configured to interact with your Kubernetes cluster.
Network connectivity between the Splunk Enterprise instance and the Kubernetes cluster.
Kubernetes configuration guidelines

Consider the following guidelines if you are configuring Kubernetes integration for DSDL:

Guideline Description
Secure authentication Use secure authentication for certificates or bearer tokens with limited RBAC privileges.
Transport layer security
(TLS) Ensure the Kubernetes API server and set any external DSDL endpoints to use SSL.
Permissions Assign minimal permissions to manage pods and resources.
Monitor and scale Use Splunk Observability or cluster metrics to watch resource usage and scale as needed.
Component updates Keep Kubernetes, DSDL, and related components updated to their latest and compatible versions to benefit fromsecurity fixes and performance improvements.
Set up a Kubernetes cluster

Before integrating with DSDL, set up a Kubernetes cluster that meets the following requirements:

Requirement Details
Kubernetes version Version 1.16 or higher is needed for compatibility with DSDL.
Networking Provide connectivity between Splunk Enterprise and the cluster. Configure network plugins such as Calicoand Flannel as needed.
Load balancer or Ingress
controller Expose services externally for production use if required.
Persistent storage Configure dynamic PVC provisioning if you plan to store model artifacts or data externally.
Role-based access control
(RBAC) DSDL does not automate RBAC creation. You can manually assign RBAC details in the DSDL setup page.
Configuration steps

Complete the following steps to configure a Kubernetes cluster:

Install Kubernetes cluster:
Use kubeadm or a managed provider such as Amazon EKS, Red Hat OpenShift, GKE, or AKS to install the
cluster.
1.
Ensure that all nodes communicate with each other and the control plane.
1.
Configure network plugin:
Choose a plugin that matches your cluster's version.
Install using directions from the plugin's documentation.
2.
Set up persistent storage:
Install a storage provisioner such as NFS, Ceph, or AWS EBS.
Create a StorageClass for dynamic provisioning.
Test by creating and binding a sample PersistentVolumeClaim (PVC).
3.
Install ingress controller or load balancer:
Use an ingress controller such as NGINX Ingress Controller or configure a load balancer. For example
AWS Elastic Load Balancing (ELB).
1.
4.
Enable SSL/TLS termination if you need secure external access.
Verify cluster functionality:
Deploy a simple test application.
Confirm that services and the ingress controller or load balancer configurations work as expected.
5.
Configure DSDL for Kubernetes

Once the Kubernetes cluster is set up, you can configure DSDL in Splunk Enterprise to deploy and manage your
containerized data science workloads:

In DSDL, go to Configuration and then Setup.
Select Kubernetes and enter your cluster details.
Choose the Service type.
Provide a hostname. For example dsdl.apps.<cluster-domain> if you want a custom route.
Test and save: DSDL will attempt to deploy containers in your Kubernetes project.
Automatic deployment

After saving the necessary details on the DSDL setup page in Splunk Enterprise, DSDL automatically triggers the
deployment of its containers and any required Kubernetes resources. This includes creating pods, persistent volumes,
and services according to your configuration.

Authentication modes

DSDL supports multiple authentication methods for connecting to your Kubernetes cluster. Choose the mode that best
suits your environment and security requirements:

Authentication
mode
Details When to use
Certificate and Key
Cluster base URL:
https://api.<cluster-domain>:6443
Cluster certificate authority: The CA certificate path that signed
the Kubernetes server's certificate.
Client certificate or client key: Paths to your client certificate
and private key.
Note: Obtain certificates from a trusted CA rather than self-signing
certificates.
Use for high-security environments where
you have properly signed certificates. Use if
you prefer mutual TLS over other
mechanisms.
User Token
Use a bearer token associated with a Kubernetes service account:
Cluster base URL:
https://api.<cluster-domain>:6443
User token: The bearer token for a Kubernetes service
account.
Steps: Create the service account, bind appropriate roles, and
retrieve the token using kubectl.
Use when you want a simple setup without
managing certificates. Service accounts can
have minimal or limited permissions through
RBAC.
User Login Use a username and password for basic authentication:
Cluster base URL:
https://api.<cluster-domain>:6443
User name and password: Credentials for basic authorization.
(Optional) CA certificate: Required if you need TLS.
Use for simple testing or development. Not
suitable for production due to weaker
security.
Authentication
mode
Details When to use
Service Account
(In-Cluster)
Use a service account automatically when Splunk Enterprise runs inside
the same Kubernetes cluster:
Cluster base URL: Might be auto-discovered if in-cluster.
Namespace: The namespace containing the service account.
Use if Splunk Enterprise is itself deployed on
Kubernetes. Use for in-cluster authentication
for DSDL tasks.
Service types

Choose how DSDL services such as notebooks and API endpoints are exposed within Kubernetes:

Service
type
Details When to use
LoadBalancer SpecifyDSDL configuration. Namespace and StorageClass in Use for direct external access on cloud providers such as AWS, Azure, and GCPthat support external load balancers.
NodePort Provide internal and external hostnames ifneeded. Use for internal or test environments where you bind a high port on each node.Use for quick, local testing without an ingress.
Ingress
Ingress host pattern. For example
*.example.com.
Annotations: Custom Ingress
settings.
Use when you want advanced routing, TLS termination, or path-based rules.
Note: An ingress controller must be installed in your cluster.
Namespace and resource management guidelines

See the following guidelines for namespace and resource management when using Kubernetes:

Use dsdl-namespace to create a new namespace and isolate the DSDL workloads.
Specify the Namespace in the DSDL Configuration page.
Set resource requests and limits. Ensure DSDL pods have enough CPU and memory if performing large-scale
model training.
•
Storage configuration

Use persistent storage for storing models, logs, and data. Complete the following steps:

Verify the StorageClass: kubectl get storageclass
Specify Storage Class in DSDL Configuration.
Check that dynamic provisioning is working by creating sample PVCs.
Certificate guidelines

See the following guidelines for certificate management when using Kubernetes:

Self-signed certificates trigger browser warnings and potential vulnerabilities. For external production, use publicly
signed certificates such as Let's Encrypt, DigiCert, or an internal certificate authority (CA).
•
Include certificates in your DSDL container. Place dltk.pem and dltk.key in the /dltk/.jupyter/ location or
specify a custom path in the DSDL configuration.
•
Enable Hostname Verification in DSDL. Set "Check Hostname" to "Enabled" in the DSDL setup page.
Firewall considerations

DSDL requires certain ports to communicate with Kubernetes resources:

Component Description
Kubernetes API Port 6443. Outbound traffic from Splunk to manage cluster.
DSDL API Port 5000 or dynamically generated. Bidirectional traffic for fit, apply, and summary commands.
Splunk REST API Port 8089. If container-based notebooks call back to Splunk.
Splunk HTTP Event Collector
(HEC)
Port 8088 for on-premises or port 443 for Splunk Cloud. Outbound traffic from notebooks and pods to Splunk
for logs and results.
Ensure your firewall rules allow necessary ports, especially for any dynamic assignments in development (DEV) mode.
For example Jupyter on port 8888, or TensorBoard on port 6006.
Troubleshoot Kubernetes configuration

Issue Troubleshoot
Authentication failures Check that tokens, certificates, or user credentials are valid. Confirm RBAC roles and permissions in your cluster.
Service exposure
problems
Verify correct service type of NodePort, LoadBalancer, or Ingress. Check ingress controller logs or load balancer
configuration if external access fails.
Resource limitations
Pods can be stuck in "Pending" if there is insufficient CPU and memory or a lack of storage.
Scale your resources or adjust requests and limits.
Networking issues DNS resolution within the cluster might need debugging if Splunk cannot reach container endpoints. Check yourcluster's network policy or plugin settings.
Storage issues
PersistentVolumeClaims (PVCs) can remain in "Pending" if no suitable StorageClass is available.
Review the provisioner logs for errors.
Splunk App for Data Science and Deep Learning certificate settings and JupyterLab password...........................
The Splunk App for Data Science and Deep Learning (DSDL) connects from the search head to the container endpoints
over HTTPS. By default, a self-signed certificate is provided in the prebuilt DSDL containers for development. For
development purposes hostname checking for self-signed certificates is disabled. You can turn hostname checking on if
needed in your production setup.

By default DSDL tries to retrieve the SSL certificate from its container endpoint. If you want to point DSDL to your own
certificate or CA chain on your Splunk platform instance you can enter a path or filename on the Configuration > Setup
page in the section labeled Certificate and Password Settings.

By default DSDL containers use a certificate for all endpoints for HTTPS communication. If you work with an ingress or
load balancer setup in your container environment like Kubernetes, you likely terminate HTTPS at this point. In those
cases you can optionally configure the containers to not use the self-signed certificate, but your own. You must ensure
your ingress takes care of all HTTPS and certificate handling. All data transfer related communication is forced to HTTPS,
meaning there is no option for unencrypted HTTP traffic.

For production use of DSDL use your own certificate. Generate the certificate according to the security requirements in
your environment and build it into your container images, or configure it in your container environment.
JupyterLab password settings

After you complete the connection between DSDL and a container such as Docker, you can open a new container and
begin using JupyterLab Notebooks to experiment on your data and create models. You can also learn from and leverage
the provided pre-built JupyterLab Notebooks, each of which corresponds to one of the DSDL Examples.

When you first select the JupyterLab icon on the Configuration > Containers page you are prompted for a password.
The default password is Splunk4DeepLearning.

You can reset the password in the Jupyter Password field on the Setup page. This password change takes effect on any
newly started containers. Leave the field blank to keep the default password. Alternatively you can manage this in your
container environment by overriding the JUPYTER_PASSWD environment variable.

Set up the Splunk App for Data Science and Deep Learning using AWS and EKS................................................
Amazon Web Services (AWS) Elastic Kubernetes Service (EKS) is a frequently used managed service for running
container workloads in the Cloud. Splunk App for Data Science and Deep Learning (DSDL) customers can use this
managed service on AWS, connect DSDL to EKS, and run workloads there.

Prerequisites

The following is required for a successful set up:

An AWS account with sufficient administrator permissions
DSDL app installed and configured on your Splunk platform instance
Set up steps

Complete these steps to use DSDL with AWS:

Create a new IAM user and role
Install and configure the AWS CLI
Install the eksctl command line utility
Create an Amazon EKS cluster
Set up an EFS CSI driver in EKS
Connect DSDL to the AWS EKS cluster
(Optional) Configure Observability
Create a new IAM user and role

AWS Identity and Access Management (IAM) is an Amazon web service that helps you securely control access to any
AWS resources. IAM enables shared access to your AWS account and resources while protecting your AWS account
root-user information.

In your AWS account, create a new user. Create a user name that identifies it as DSDL related, for example,
dltk-admin.
1.
For the AWS Credential type, select Access key - programmatic access.
For permissions, choose Add user to group and Create group. For the permission boundary, choose "Create
user without a permission boundary".
3.
Create a name for the new group that identifies it as DSDL related, for example, dltk-admin-group. Select
"AdministratorAccess" from the policy menu.
4.
Click Create group.
Add the user you created in step 1 to the group you created in step 3. When complete, keep the confirmation
page open in order to use the Access Key ID and Secret Access Key in the next section.
6.
Install and configure the AWS CLI

Download and configure the AWS command line interface using the Access Key ID and Secret Access Key login
credentials from the previous step. For more information, see https://aws.amazon.com/cli/

Install the eksctl command line utility

You can use Amazon Elastic Kubernetes Service (Amazon EKS) to run Kubernetes on AWS without installing or
maintaining your own Kubernetes control plane or nodes. The eksctl command line tool is used for creating and
managing Kubernetes clusters on Amazon EKS.

For more information,, see https://docs.aws.amazon.com/eks/latest/userguide/eksctl.html and
https://eksctl.io/introduction/#installation

Create an Amazon EKS cluster

In Amazon EKS, create a cluster. You can refer to the following example for guidance:

eksctl create cluster --name dltk-cluster --version 1.21 --region eu-central-1 --nodegroup-name dltk-nodes
--node-type t2.xlarge --nodes 2

Add the cluster to Amazon EKS and verify the cluster is up and running.

Set up an EFS CSI driver in EKS

Verify you can use the Storage Class of efs-sc and set up and configure the Amazon Elastic File System (EFS) Container
Storage Interface (CSI) driver.

For more information, see https://docs.aws.amazon.com/eks/latest/userguide/efs-csi.html

Connect DSDL to the AWS EKS cluster

Complete the following steps:

In DSDL, go to Configuration > Setup and scroll down to the input panel for Kubernetes. Fill in the fields to
connect DSDL to the AWS EKS cluster, using the cluster name created in a previous step.
On Splunk Cloud the inbound and outbound traffic to reach the cluster and its endpoints must be enabled. For
example, using ACS. For more information, see Splunk Cloud Self-Service: Announcing The New Admin
Config Service API.
1.
From Configuration > Containers , launch a development (DEV) container and verify the Kubernetes container
is running.
2.
In AWS EKS, verify that the DEV deployment exists.
If you are setting up DSDL for the first time, verify that one of the Examples is running without any errors.
Running an example after the container environment setup is a simple way to confirm that an algorithm can run.
4.
(Optional) Configure Observability

If you want to use Splunk Observability Cloud (O11y) to monitor the Kubernetes that DSDL uses take steps to configure
observability. To learn more about this product offering, see Splunk Observability.

Complete the following steps:

In Splunk Observability Cloud configure a new integration as shown in the following image.
Complete the Configure Integration fields as follows:
Field name Value
Splunk Access Token Default
Cluster Name Enter the name of the cluster you created in an earlier step
Provider Amazon Web Services
Distribution Amazon EKS
Add Gateway No
Log Collection True
Next, follow the Install Integration steps as shown in the following image.
Lastly, look over the Review Inventory page for the cluster added as shown in the following image. Pay attention
to CPU utilization on the cluster when running a DSDL container workload.
3.
Firewall requirements for the Splunk App for Data Science and Deep Learning.........................................................
Firewall requirements for Splunk and Docker communication.................................................................................
Docker integration with the Splunk App for Data Science and Deep Learning (DSDL) is suitable for single-machine setups
with minimal firewall rules. External exposure is optional, and primarily for Jupyter or other data science interfaces.

Docker integration is not suitable for production environments due to the lack of Transport Layer Security (TLS ) on port

Always verify the exact port mappings in the DSDL UI or logs before adjusting firewall rules. Use Kubernetes if you
need secure, scalable, multi-instance deployments.
All external container processes such as Docker, Kubernetes, JupyterLab, and GPU management, including firewall
management, are out of scope for Splunk platform support. Ensure that your environment is configured to securely
connect Splunk to the container resources.
Docker integration summary

Local integration:

Designed for single-machine setups with minimal firewall rules.
External exposure is optional, primarily for Jupyter or other data science interfaces.
Remote integration:

Not advisable for production due to a lack of TLS on port 2375.
Use Kubernetes if you need secure, scalable, multi-instance deployments.
Dynamic ports:

In DEV mode, DSDL can dynamically assign ports to Jupyter and Spark, for example.
Always verify the exact port mappings in the DSDL UI or logs before adjusting firewall rules.
Docker integration limitations

The following are limitations of Docker integration with DSDL:

Security: Docker integration in DSDL does not support Transport Layer Security (TLS ) on port 2375.
♦ Remote connections over port 2375 are unencrypted which is insecure for production.
•
Scalability: Docker is less flexible for distributed or large-scale deployments.
Kubernetes is a better option for secure, large-scale, or multi-instance environments, and resource
management.
♦
Kubernetes supports TLS for the API and provides good scalability, making it a more robust solution for
production.
♦
•
Local Docker integration

When Docker and the Splunk search head are co-located on the same machine, no external firewall rules are typically
needed for Docker's communication with Splunk. Docker interacts through a local socket of unix://var/run/docker.sock
or local port 2375, which does not require external exposure.

If certain DSDL services such as Jupyter or MLflow need external access, you must open the appropriate ports. In most
local setups these services are only accessed from the same machine.
See the following table for a summary of guidelines for local Docker integration:

Local integration Description
Docker
No additional firewall rules:
Docker to Splunk communication typically uses a local socket or 2375 on the
same host.
External firewall settings are rarely needed.
External services: Jupyter, TensorBoard, MLflow, or
Spark
If Jupyter, TensorBoard, MLflow, or Spark must be accessed from outside, open their
respective ports:
Jupyter: Inbound if external usage is required. Default port 8888.
MLflow: Optional if this service is exposed outside the local machine. Default
port 6060.
Spark: Optional if this service is exposed outside the local machine. Default port
4040.
TensorBoard: Optional if this service is exposed outside the local machine.
Default port 6006.
Remote Docker integration

While Docker can be configured for remote access, it poses a security risk to production environments due to the lack of
TLS on port 2375. If you must temporarily enable remote Docker, consider the following fiewall rules:

Traffic
direction
Port Purpose Firewall rule
Outbound 2375. no TLS Docker API for containermanagement. Required for remote access to Docker and remoteDocker management.
Bidirectional 8089 Splunk REST API. Optional. Use to connect container to the SplunkREST API.
Bidirectional 5000 or dynamically assigned DSDL commands such as apply. fit and Required for DSDL operations.
Inbound 443 for Splunk Cloudotherwise 8088 Splunk HEC for data submissions. Optional if using HEC ingestion.
External 8888, 6060, 4040, 6006 Jupyter, MLflow, Spark,TensorBoard Only open if externally accessed.
See the following table for further information on both Splunk and service ports:

Port Description
Docker API port
Port 2375 provides remote Docker control without encryption.
Security warning: Unencrypted traffic is not suitable for sensitive or production deployments.
Firewall rule: Outbound traffic from Splunk to 2375 if Splunk needs to manage Docker containers remotely.
Port Description
Splunk management
port • • Used for the Splunk REST API, which containers might call.Firewall rule: If container-based services need to query Splunk, allow bidirectional access on port 8089.
DSDL API port • DSDL typically runs on port 5000 in DEV mode, but it can change dynamically.
Firewall rule: Allow bidirectional access on port 5000 or the assigned port for DSDL operations.
Splunk HEC port
If containerized tasks must send data to Splunk:
Port 443 for Splunk Cloud.
Port 8088 for Splunk on-premises.
Firewall rule: Inbound on the relevant port to receive data from Docker containers.
Jupyter • Default port 8888.Used for accessing Jupyter notebooks. Inbound traffic on port 8888, or dynamically assigned port. Mandatory if
accessing Jupyter from outside the machine.
MLflow • Default port 6060.Used for tracking experiments and managing models. By default, these services run locally in DEV mode. If you
expose ports to external networks, open inbound rules for port 6060. Optional.
Spark • Default port 4040Used for monitoring Spark job execution. By default, these services run locally in DEV mode. If you expose
ports to external networks, open inbound rules for port 4040. Optional.
TensorBoard • Default port 6006Used for real-time insights into model training. By default, these services run locally in DEV mode. If you
expose ports to external networks, open inbound rules for port 6006. Optional.
Firewall requirements for Splunk and Kubernetes communication..........................................................................
When the Splunk App for Data Science and Deep Learning (DSDL) integrates with Kubernetes, you must ensure that the
necessary ports are open to allow communication between the Splunk search head, the Kubernetes environment, and
DSDL services. These firewall rules help data flow securely and efficiently, especially when containers are dynamically
assigned ports at runtime in development (DEV) mode.

In production (PROD) mode, fewer ports are exposed, typically limiting external access to only the required endpoints.
In DEV mode, additional ports for Jupyter, TensorBoard, MLflow, and Spark can be opened for interactive
development.
Kubernetes firewall rules summary

Use this summary to confirm required, recommended, or optional ports. Adjust for your specific environment and security
policies:

Component Required? Port Description
Component Required? Port Description
Kubernetes API Yes 6443 Required for Splunk to manage pods.
Splunk REST API No 8089 Optional if container-based calls to Splunk are needed.
DSDL API Yes 5000 or dynamic Required for training and inference commands.
Splunk HEC No 443 or 8088 Optional if streaming data or logs back into Splunk.
Jupyter No 8888 Used in DEV mode or specific workflows; open only if needed.
MLflow No 6060 Used in DEV mode or specific workflows; open only if needed.
Spark No 4040 Used in DEV mode or specific workflows; open only if needed.
TensorBoard No 6006 Used in DEV mode or specific workflows; open only if needed.
Firewall configuration for the Splunk search head

See the following table for information on traffic direction and port requirements for the Splunk search head:

Traffic
direction
Port Required? Description
Outbound 6443 Required for Kubernetes use. Kubernetes API server. Manage pods,resources.
Bidirectional 8089 Optional. Needed if containers call back toSplunk using REST. Splunk REST API communication withcontainers.
Bidirectional 5000 or dynamic Required for DSDL operations. DSDL API commands including apply, and summary. fit,
Inbound 8088 for on-premises or 443 forSplunk Cloud. Optional if using HEC ingestion. Splunk HEC for receiving data fromcontainers.
See the following table for further information on Splunk ports:

Port Description
Kubernetes API port • Splunk needs outbound access to port 6443 to manage Kubernetes resources.
Firewall rule: Outbound traffic on port 6443 to the Kubernetes API server.
Splunk management
port
If containerized services in Kubernetes need to communicate with the Splunk REST API, open port 8089 in
both directions.
Firewall rule: Bidirectional traffic on port 8089 if you enable Splunk's REST API calls from containers.
DSDL API port • By default, DSDL uses port 5000 for data science operations in DEV mode. In PROD mode, the DSDLcontainer typically runs on port 5000 but can dynamically assign a different port.
Firewall rule: Bidirectional traffic on 5000 or the dynamically assigned port.
Splunk HEC port
For inbound traffic from Kubernetes (notebooks, inference scripts) to Splunk:
♦ On-premises Splunk often uses 8088.
♦ Splunk Cloud typically uses 443.
Firewall rule: Inbound traffic on the relevant port (8088 or 443).
Firewall configuration for the machine running Kubernetes

See the following table for information on traffic direction and port requirements for the machine running Kubernetes:

Traffic direction Port Required? Description
Bidirectional 8089 Optional. Use if needed for container communication tothe Splunk REST API.
REST API
communication
with Splunk.
Bidirectional 5000 or dynamic Required for DSDL operations.
DSDL API
commands with
Splunk.
Outbound 443 for Splunk Cloud or 8088 for Splunkon-premises. Optional. Use for HEC ingestion. HEC for sendingdata to Splunk.
Inbound 6443 Required to manage cluster resources.
Kubernetes API
access from
Splunk.
Inbound 8888 or dynamic Required in DEV if Jupyter is used. Jupyter Notebooks(DEV mode).
Inbound 6060 or dynamic Optional. Use with MLflow. MLflow tracking(DEV mode).
Inbound 4040 or dynamic Optional. Use with Spark. Spark monitoring(DEV mode).
Inbound 6006 or dynamic Optional. Use with TensorBoard. TensorBoard (DEVmode).
See the following table for further information on both Splunk and service ports:

Port Description
Splunk management port • If containers require Splunk REST API access, keep 8089 open in both directions.
Firewall rule: Bidirectional traffic on port 8089.
DSDL API port • The container typically communicates with Splunk using port 5000. If you enable dynamic portassignment, open the assigned port.
Firewall rule: Bidirectional traffic on port 5000 or the chosen dynamic port.
Splunk HEC port • Containers in Kubernetes need outbound access to Splunk HEC if they send data or logs back toSplunk.
Firewall rule: Outbound traffic on port 443 for Splunk Cloud or port 8088 for Splunk on-premises.
Kubernetes API port • Splunk uses inbound access to manage or query Kubernetes resources using port 6443.
Firewall rule: Inbound traffic on port 6443 from the Splunk Search Head.
Optional Services (DEV
Mode)
Jupyter: Port 8888. Inbound if you use Jupyter notebooks.
MLflow: Port 6060. Inbound if MLflow experiment tracking is enabled.
Spark: Port 4040. Inbound if Spark monitoring is used.
TensorBoard: Port 6006. Inbound if deep learning visualization is needed.
Firewall rule: Inbound traffic on these ports or the dynamically assigned ones.
Development versus production usage

See the following table for firewall usage in development (DEV) versus production (PROD) mode:

Mode Description
Development (DEV) mode
Containers might expose multiple ports for Jupyter, MLflow, Spark, and TensorBoard.
The Splunk search head or the Kubernetes environment will dynamically assign ports, which appear in the
DSDL UI.
These ports are convenient for interactive development and debugging.
Production (PROD) mode • • Typically limits exposed ports to only the DSDL API. Port 5000 or a single dynamic port.Jupyter, TensorBoard, MLflow, and Spark interfaces are disabled or not exposed.
This reduces the attack surface and simplifies firewall management.
Next steps

Complete the following steps after completing the steps in the previous sections:

Align ports with your environment:
Verify which ports your containers actually use by checking the DSDL user interface or logs.
Update firewall rules to cover both default and dynamically assigned ports.
1.
Implement network security best practices:
Restrict ports to trusted networks where possible.
Enable TLS (especially for Kubernetes in production) to safeguard data in transit.
Limit the container's inbound connectivity if you only need to push data out to Splunk.
2.
Monitor and test:
After configuring your firewall, run test searches, attempt container connections, and confirm that data
can flow in both directions as needed.
1.
For ongoing monitoring, leverage Splunk Observability, container logs, and standard Splunk dashboards
to ensure stable communication.
2.
3.
Use the Splunk App for Data Science and Deep Learning.............................................................................................
Leverage the examples provided in the Splunk App for Data Science and Deep Learning....................................
The Splunk App for Data Science and Deep Learning (DSDL) ships with more than thirty data science, deep learning, and
machine learning example techniques that showcase different algorithms for classification, regression, forecasting,
clustering, natural language processing (NLP), graph analytics, and data mining applied to sample data.. These example
techniques are available from the Examples tab of the main menu, organized by algorithm type.

Every example includes a related Jupyter Notebook that defines how the technique is implemented. You can explore
these examples and leverage the SPL code and Notebook content as a means to implement your own use-cases in
DSDL.

Classifier examples

Neural Network Classifier Example: Shows how to use a binary neural network classifier build on keras and
TensorFlow.
•
Logistic Regression Classifier Example: Shows a simple logistic regression using PyTorch.
Multiclass Neural Network Classifier: Shows a simple multiclass neural network classifier using PyTorch with
GPU.
•
Neural Network Classifier DGA: Shows a simple neural network example using PyTorch for building a multiclass
classifier applied to the DGA dataset.
•
Spark Gradient Boosting Classifier DGA: Shows a simple gradient boosting model with Spark's MLLib applied to
the DGA dataset.
•
Explainable Machine Learning with XGBoost and SHAP: Shows how to introduce explainability in machine
learning models with the help of SHAP.
•
Autosklearn Classification Example: Shows an automated machine learning approach to generate a classifier with
autosklearn.
•
Regression examples

Example Linear Regression: Shows a simple linear regression using the TensorFlow estimator class.
Deep Neural Network Regressor: Shows a simple regression using the TensorFlow Deep Neural Network (DNN)
estimator class.
•
Example XGBoost Regression: Shows a simple regression example with XGBoost.
Example GridSearch SVM: Shows how grid search can be used with a Support Vector Regressor.
Multivariate LSTM Regressor: Shows a multivariate Long Short-Term Memory (LSTM) network to predict AC
power on an example dataset from the Splunk Machine Learning Toolkit (MLTK).
•
Forecasting examples

Internet Traffic Forecast using a Convolutional Neural Network: Shows an example for forecasting a univariate
time series with a convolutional neural network using TensorFlow.
•
App Expense Forecast using LSTM: Shows forecasting a univariate time series with a long short term neural
network using TensorFlow.
•
Example Forecast with Prophet: Shows how to use the Prophet library for forecasting.
Clustering examples

Autoencoder: Shows a basic auto encoder using TensorFlow returning hidden layer representation and
reconstruction loss measurements.
•
Distributed KMeans algorithm with Dask: Shows how to distribute algorithm execution with Dask using KMeans.
Clustering with UMPA and DSCAN: Shows the dimensionality reduction technique UMAP in combination with
DBSCAN for distance based clustering.
•
Host Clustering using UMAP on JA3 Signatures: Demonstrates use of the JA3 encoder notebook which uses
UMAP to identify similarities and differences between JA3 signatures.
•
NLP examples

Entity Recognition and Extraction Example using the spaCy Library: Shows a simple NER (Named Entity
Recognition) using spaCy.
•
Entity Recognition and Extraction Example for Japanese using spaCy + Ginza Library: Shows a simple NER
(Named Entity Recognition) for Japan ese using spaCy and Ginza.
•
Sentiment Analysis using spaCy: Shows a simple sentiment analysis using spaCy.
Graphs examples

Graph Analysis Example for Bitcoin Transactions: Shows how to calculate centrality measures in a bitcoin
transaction graph using NetworkX.
•
Graph Analysis Example for Community Detection with Louvain Modularity: Shows the Louvain Modularity
method for community detection running on GPU.
•
Causal Inference: Shows how you can use Bayesian Networks to combine machine learning and domain
expertise for causal reasoning.
•
Data Mining examples

Frequent Itemsets for Shopping Analysis: Shows how to find frequent itemsets using FP Growth algorithm from
Spark MLLib.
•
Collaborative Filtering Recommendations: Shows how to get recommendations using Collaborative Filtering from
Spark MLLiib.
•
Rapids UMAP on DGA: Shows how to analyze the DGA dataset with Rapiid's UMAP running on GPU.
Example for Process Mining with PM4Py: Shows how process mining with PMPy can be integrated with the app.
Time Series Anomalies with STUMPY: Shows how to detect anomalies in time series using matrix profiles.
Example for Bayesian Online Change Point Detection: Shows how to detect change points or drift in time series
using Bayesian Online Change Point Detection.
•
Anomaly Detection with Random Cut Forest: Shows how to detect anomalies using the Random Cut Forest
algorithm.
•
Seasonality and Trend Decomposition (STL): Shows how to decompose a time series into its trend and
seasonality components.
•
Example for Hidden Markov Models applied to punct notations: Shows a very simple application of creating a
Hidden Markov Model (HMM) based on the sequence of characters in punct notations.
•
Example Online Learning Anomaly Detection: Shows how to utilize an online learning anomaly detection model
using the HalfSpaceTree algorithm in River.
•
Anomaly Detection with PyOD: Shows an Unsupervised Outlier Detection using Empirical Cumulative Distribution
functions utilizing the PyOD library.
•
Basic examples

Correlation Matrix and Pair Plot: Show how to do a simple correlation matrix and embed graphic plots from
seaborn.
•
Spark Pi Example: Shows a basic hello world example for Spark Pi.
Seasonality and Trend Decomposition (STL): Shows how to decompose a time series into its trend and
seasonality components.
•
Splunk App for Data Science and Deep Learning example workflow......................................................................
The Splunk App for Data Science and Deep Learning (DSDL) lets you to integrate advanced custom machine learning
and deep learning systems with the Splunk platform. You can build, test, and operationalize customized models that
leverage GPUs for compute intense training tasks.

After installing and configuring DSDL you can follow these high-level steps to use the app for your own business case:

Launch a new development container
Open your preferred third-party tool
Build and iterate the model
Monitor and manage DSDL
The DSDL model-building workflow includes processes that occur outside of the Splunk platform ecosystem, leveraging
third-party infrastructure such as Docker, Kubernetes, OpenShift, and custom Python code defined in JupyterLab. Any
third-party infrastructure processes are out of scope for Splunk platform support or troubleshooting.
Launch a new development container

Take the following steps to launch a new development container in DSDL:

From the Configuration tab, select Containers. Come back to this page at anytime to see the number and status
of your containers, and to stop or start containers.
Containers can take a few seconds to start and stop.
1.
Make a selection from the Container Image drop-down menu. There are several pre-built images for specific
libraries, including Spark, River or Rapids.
The Golden Image for CPU and GPU contains most of the recent popular libraries including TensorFlow,
PyTorch and others.
♦
You can choose to build your own image from the public github repository for DSDL. See,
https://github.com/splunk/splunk-mltk-container-docker.
♦
You can choose to make a customized container rather than use a pre-built one. See,
https://anthonygtellez.github.io/2020/01/10/Creating-Custom-Containers-DLTK.html.
♦
2.
Choose the GPU runtime drop-down value. The GPU runtime menu is populated based on the chosen Container
Image.
3.
Choose the Cluster target drop-down value.
Select Start to create the development container.
Open your preferred third-party tool

Affer the container is running, you can open the third-party tool of your choice. Options include JupyterLab, TensorBoard,
MLFlow, and Spark UI. Selecting the third-party tool opens a new browser tab.

Build and iterate the model

Use your preferred third-party tool to load your dataset, choose algorithms and parameters, and build, test, and iterate
your machine learning or deep learning model. For more detailed steps, see Develop a model using JupyterLab.

Monitor and manage DSDL

DSDL includes the following pages from which you can monitor and manage your containers and deployment of the app:

DSDL page Description
Configuration >
Containers
An overview of your development and production containers. The dashboard refreshes every 5 seconds. Choose to stop or
start any of your containers from this page.
Operations >
Operations
Overview
A visual overview of DSDL app operations including your total container images.
Operations >
Container Status
An in-depth set of dashboard panels including container activity logs, fit command, apply command, and summary
command duration statistics, and an error counter. Note: You need access to the _internal index to see information on the
Container Status page.
Operations >
Runtime
Benchmarks
Informative dashboards on the runtime behavior of DSDL for different dataset sizes. The available benchmarks only profile
single-instance DSDL deployments that do not utilize any parallelization or distribution strategies. Use the benchmarks as a
baseline for algorithms operating on small to medium sized datasets. Note: Algorithms and dataset size can result in very
different runtime behavior, and is worth investigating on a case-by-case basis.
Example use case with JupyterLab

To gain familiarity on how to use the Splunk App for Data Science and Deep Learning, you can explore the Notebook
examples and how the related pre-built model can be viewed in the Splunk platform.

Perform the following steps to explore one of the Jupyter examples:

From the Configurations > Containers page, select the JupyterLab button.
The JupyterLab interface opens in a new tab. Login to JupyterLab with the default password of
Splunk4DeepLearning.
2.
From the notebooks menu, select the drift_detection.ipynb Notebook.
In this example Notebook or any of the other pre-built Notebooks, you can interactively run the code cells and
create additional cells for any additional code you want to test or develop. This can also include visualizations or
any other functionality available in Python libraries or JupyterLab.
4.
Navigate back to the tab for your Splunk platform instance and select Examples > Data Mining > Example for
Bayesian Online Change Point Detection.
5.
Select Submit.
On this dashboard you can see how the Drift Detection algorithm is working on the sample data. On the Raw Data
panel you can see some sample data of ping events with the numeric field rtt extracted. This field contains
measures of ping round-trip times. The Drift Detection algorithm is applied to this target variable.
7.
From the Example for detecting drift in network round trip time measurements panel, select the Open in Search
icon. This opens a new tab where you can view the underlying SPL.
8.
The SPL shows how the Drift Detection algorithm is integrated into the search pipeline. The first six lines perform
all the necessary data preprocessing. The | fit MLTKContainer statement passes the dataframe over to the
container to run the algo=drift_detection with the given parameters. The additional column drift gets added to
the search results and contains the detected drifts with a simple binary 0 or 1 mark.
9.
Develop a model using JupyterLab.........................................................................................................................
The Splunk App for Data Science and Deep Learning (DSDL) leverages predefined JupyterLab Notebook workflows so
you can build, test, and operationalize customized models with the Splunk platform.

The DSDL model building workflow includes processes that occur outside of the Splunk platform ecosystem, leveraging
third-party infrastructure such as Docker, Kubernetes, and JupyterLab. Any third-party infrastructure processes are not
supported by Splunk.
After installing and configuring DSDL, you can perform the following high-level steps to build a model using the Splunk
App for Data Science and Deep Learning with JupyterLab:

Preprocess and select your data
Create a new Notebook in JupyterLab
Send sample data to a container
Develop Notebook code in JupyterLab
Train the model
Inspect and validate the model
Test the model
Iterate or retrain the model in JupyterLab
Operationalize the model
Preprocess and select your data

DSDL works best when you provide a clean matrix of data as the foundation for building your model. Complete any data
preprocessing using SPL to take full advantage of the Assistant's capabilities. To learn more, see Preparing your data for
machine learning in the MLTK User Guide.

Complete the following steps:

In the Splunk App for Data Science and Deep Learning, select Configuration > Containers and make sure that
the __dev__ container is running, and that you can access JupyterLab.
1.
Use the Search tab to identify the data from which you want to develop a model.
Create a new Notebook in JupyterLab

Complete these steps in JupyterLab:

From Configuration > Containers , select the JupyterLab button. This opens JupyterLab in a new tab.
Open the barebone_template.ipynb file from the Notebooks folder. This file is pre-populated with helpful
Notebook steps you can leverage or edit to match your use case.
2.
From the JupyterLab main menu click File > Save Notebook As. Save this copy of the Notebook with a
well-defined naming convention.
Names must not include spaces but can include underscores.
3.
As soon as you save your Jupyter Notebook, all relevant cells that contain the predefined functions are
automatically exported into a Python module. This file is located in the /app/model folder and is then called
dynamically from your fit, apply, and summary command.
4.
Send sample data to a container

Complete the following steps:

Select a subset of the data you want to use for your model. Optionally you can use the sample command as
shown in the following example:
.... | sample 1000
1.
Send the sample data to the container. Include the features that you are looking to model in the search command
as shown in the following example:
| fit MLTKContainer mode=stage algo=my_notebook features_* into app:MyFirstModel
2.
The mode=stage setting does not actually fit the data. This command indicates that you want to transfer a dataset over
to the container to be worked on in the JupyterLab environment. In most cases you can start with a simple, small
dataset of a given structure of features. This helps you to speed up the typical data science iteration cycle.
Develop Notebook code in JupyterLab

Complete the following steps:

Write your code in the JupyterLab Notebook you created. Test that the Notebook operates on the data sent over
to the container in the previous task. Take advantage of JupyterLab Notebooks to execute parts of your code and
rapidly develop your modeling ideas.
1.
You may choose to resend a different subset of your data during this code development phase if the original
sample does not contain enough records or features for testing purposes
2.
After you are satisfied that your code is operating as expected, make sure to save the Notebook.
Check that the corresponding .py module file in the /app/model/ directory correctly reflects the code of your
Notebook and does not contain any Python indentation or spelling errors which can break your code.
4.
Changes in model code are available at the next call of your model. This call can be triggered by a scheduled search or
when users work with your model.

Use robust naming conventions that clearly separate models in development from those in production. Additionally you
can use GIT or MLflow for enhanced version control or model lifecycle management.
Train the model

Complete the following steps:

Split your data into a training set and a testing set. Optionally you can use the sample command for this split or
Jupyter if preferred. You can use partitions and seed values for consistent sampling as shown in the following
example:
... | sample partitions=10 seed=42 | where partition_number<7
1.
Run the fit command for your algorithm on the training dataset as shown in the following example:
... | fit MLTKContainer algo=my_notebook epochs=100 features_* into app:MyFirstModel.
2.
Ensure that you are passing in the correct features and parameters. You can pass any key=value based
parameters which are exposed in the parameters of the fit and apply functions in your Notebook.
3.
If training runs successfully, the training results are returned to you.
If you receive errors, check the job inspector and the search.log. You might need to return to the Jupyter Notebook to
update the code.

Inspect and validate the model

You can use TensorBoard to check and validate how your neural network model evolved over its training epochs. Review
histograms and other insights provided in TensorBoard to further improve or tune your model.

Select the TensorBoard button on the Containers page.

Test the model

Complete the following steps:

Select the test dataset by partitioning the data again as shown in the following example:
... | sample partitions=10 seed=42 | where partition_number>=7
1.
Apply the model on the test dataset. as shown in the following example:
... | apply MyFirstModel
2.
Use the score command to evaluate the accuracy of the model using relevant metrics. For example, a
classification report or confusion matrix for a classification algorithm, or R squared and RMSE for a regression or
forecast algorithm.
3.
If you receive errors, check the job inspector and the search.log. You might need to return to the Jupyter Notebook to
update the code.

Iterate or retrain the model in JupyterLab

After the model is tested and achieves good results, revisit your model to adapt to new data or updated business
requirements. Revisiting the model is an opportunity to improve your model code or retrain it with new data.

Operationalize the model

After the model is performing to an acceptable standard, create an alert, report, or dashboard to monitor new data as it
comes into the Splunk platform. Use the apply command on the data features identified with the trained model.

You can use the Splunk platform to monitor your model performance and results, including keeping track of metrics and
alerting on model degradation.

DSDL models can be shared by changing permission of the model to global if the model needs to be served from a
dedicated container.

Using multi-GPU computing for heavily parallelled processing...............................................................................
Use the multi-GPU computing option for heavily parallelled processing such as training of deep neural network models.
You can leverage a GPU infrastructure if you are using NVIDIA and have the needed hardware in place. For more
information on NVIDIA GPU management and deployment, see https://docs.nvidia.com/deploy/index.html.

The Splunk App for Data Science and Deep Learning (DSDL) allows containers to run with GPU resource flags added so
that NVIDIA-docker is used, or GPU resources in a Kubernetes cluster are attached to the container.

To start your development or production container with GPU support, you must select NVIDIA as the runtime for your
chosen image. From the Configurations > Containers dashboard, you can set up the runtime for each container you
run.

The following image shows an example console leveraging four GPU devices for model training.

If you want to use multi-GPU computing, review the strategies provided for your chosen framework:

For Distributed Training with TensorFlow, see https://www.tensorflow.org/guide/distributed_training
For Using multiple GPUs with TensorFlow, see https://www.tensorflow.org/guide/gpu#using_multiple_gpus
For Using multiple GPUs with PyTorch, see
https://pytorch.org/tutorials/beginner/former_torchies/parallelism_tutorial.html
•
For Data Parallelism with PyTorch, see https://pytorch.org/tutorials/beginner/blitz/data_parallel_tutorial.html
Splunk App for Data Science and Deep Learning commands.................................................................................
The Splunk App for Data Science and Deep Learning (DSDL) integrates advanced custom machine learning and deep
learning systems with the Splunk platform. The app extends the Splunk platform with prebuilt Docker containers for
TensorFlow and PyTorch, and additional data science, NLP, and classical machine learning libraries.

Familiar SPL syntax from MLTK, including the ML-SPL commands fit, apply, and summary, is used to train and
operationalize models in a container environment such as Docker, Kubernetes, or OpenShift.

Any processes that occur outside of the Splunk platform ecosystem that leverage third-party infrastructure such as
Docker, Kubernetes, or OpenShift, are out of scope for Splunk platform support or troubleshooting.
Using the fit command

You can use the fit command to train a machine learning model on data within the Splunk platform. This command
sends data and parameters to a container environment and saves the resulting model with the specified name.

When you run the fit command without additional parameters, training is performed based on the code in the associated
notebook. When you include mode=stage, data is transferred to the container for development in JupyterLab without
running full training.

Syntax

| fit MLTKContainer algo= mode=stage <feature_list> into app:<model_name>

Parameters

Parameter Description
algo Specifies the notebook name or algorithm in the container environment.
mode When set to stage, the command sends data to the container but does not perform training.
features_<feature_list> Defines the feature fields to include in training.
into app:<model_name> Saves the model or staged data in DSDL under the specified name.
Examples

The following example stages data without training so you can work iteratively in JupyterLab:

| fit MLTKContainer mode=stage algo=my_notebook into app:barebone_template

The following example sends additional data, including the _time field and feature*, to the barebone_template notebook
for iterative development in JupyterLab:

| fit MLTKContainer mode=stage algo=barebone_template time feature* i into app:barebone_template

Using the apply command

Use the apply command to generate model predictions on new data within Splunk. This step can be automated through
scheduled searches or integrated into dashboards and alerts for real-time monitoring.

Syntax

| apply <model_name>

Parameters

Parameter Description
model_name The name of the model to apply. This corresponds to the name used in the into app: clause when the model was trained.
Example

The following example runs inference on a dataset using the model named barebone_template. You can follow this with
the score command to evaluate model performance, such as accuracy metrics for classification or R-squared for
regression:

| apply barebone_template

Using the summary command

Use the summary command to retrieve model metadata and configuration details, including hyperparameters and feature
lists. This command helps track or inspect the exact parameters used in training.

Syntax

| summary <model_name>

Parameters

Parameter Description
model_name The name of the model for which to retrieve metadata.
Examples

The following example retrieves metadata for app:barebone_template, including training configurations and feature
names.

| summary app:barebone_template

Using commands in a workflow

The following is a workflow of how you can use the different ML-SPL commands available in DSDL:

Data exploration

You can identify and refine your data in Splunk using SPL.
If you are using the Splunk access token, you can pull data interactively with SplunkSearch.SplunkSearch().
For data exploration with JupyterLab you can push a sample using | fit MLTKContainer mode=stage ....

Data staging and preparation

You can use | fit MLTKContainer mode=stage ... to transfer data and metadata to the container.
Clean and configure the staged dataset within JupyterLab.

Model training

Model names must not include white spaces.
You can use | fit MLTKContainer algo= ... on your final training data.
Leverage GPUs if needed. Monitor progress in JupyterLab.

Model inference

You can use | apply <model_name> to generate predictions.
Integrate with Splunk dashboards, alerts, or scheduled searches for operational use.

Model evaluation

You can use | score for classification or regression metrics.
Return to JupyterLab to refine or retrain the model if needed.

Summary and monitoring

You can use | summary <model_name> to review metadata and configurations.
Set model permissions to Global if it needs to be served from a dedicated container.
Monitor performance in Splunk dashboards or alerts and detect potential drift.

Pull data using Splunk REST API

You can interactively search Splunk from JupyterLab, provided your container can connect to the Splunk REST API and
you have configured a valid Splunk auth token in the DSDL setup page. This is useful for quickly testing different SPL

queries, exploring data in a Pandas DataFrame, or refining your search logic without leaving Jupyter.

Complete the following steps:

This approach returns raw search results only. No metadata or parameter JSON is generated. If you need structured
metadata, use the fit command with mode=stage to push data to the container.
Generate a Splunk token:
In the Splunk platform, go to Settings and then Tokens to create a new token.
Copy the generated token for use in DSDL.
1.
(Optional) Set up Splunk access in Jupyter:
In DSDL, go to Configuration and then Setup.
Locate Splunk Access Settings and enter your Splunk host and the generated token. This makes the
Splunk REST API available within your container environment.
The default management port is 8089.
2.
2.
Now that Splunk access is configured, you can pull data interactively in JupyterLab:
from dsdlsupport import SplunkSearch
# Option A: Open an interactive search box
search = SplunkSearch.SplunkSearch()
# Option B: Use a predefined query
search = SplunkSearch.SplunkSearch(search='| makeresults count=10 \n'
'| streamstats c as i \n'
'| eval s = i%3 \n'
'| eval feature_{s}=0 \n'
'| foreach feature_* [eval <<FIELD>>=random()/pow(2,31)] \n'
'| fit MLTKContainer mode=stage algo=barebone_template _time feature_* i into
app:barebone_template')
# Option C: Use a referenced query
example_query = '| makeresults count=10 \n'
'| streamstats c as i \n'
'| eval s = i%3 \n'
'| eval feature_{s}=0 \n'
'| foreach feature_* [eval <<FIELD>>=random()/pow(2,31)] \n'
'| fit MLTKContainer mode=stage algo=barebone_template _time feature_* i into
app:barebone_template')
search = SplunkSearch.SplunkSearch(search=example_query)
# Run the search and then retrieve the results
df = search.as_df()
df.head()
3.
Push data using the fit command

You can send data from the Splunk platform to the container using the following command:

fit MLTKContainer mode=stage

This writes both the dataset and relevant metadata, such as feature lists and parameters, to the container environment as
CSV and JSON files. This approach is well suited for building or modifying a notebook in JupyterLab, while referencing a
known dataset structure and configuration.

Example

The following example uses the fit command to send data from the Splunk platform to a container:

| fit MLTKContainer mode=stage algo=barebone_template time feature* i into app:barebone_template

Retrieve data in notebook
def stage(name):
with open("data/"+name+".csv", 'r') as f:
df = pd.read_csv(f)
with open("data/"+name+".json", 'r') as f:
param = json.load(f)
return df, param

df, param = stage("barebone_template")

Performance tuning and handling large datasets....................................................................................................
Combine the power of the Splunk platform search with container-based machine learning workloads using tThe Splunk
App for Data Science and Deep Learning (DSDL). It is important to manage large datasets with millions or billions of
events effectively, so you don't push container memory and CPU usage to the limit and affect your costs and app
performance.

When you run the fit or apply commands on multiple terabytes of data in the Splunk platform, the container environment
handles that data in memory or stream it in a distributed manner. This can lead to the following issues:

Container memory overruns if the container tries to load a large DataFrame at once.
Container memory times out if the job exceeds the maximum search or container run time.
Excessive CPU usage overtaxes the high-performance computing (HPC) or container node due to no data
sampling or partitioning.
•
To avoid performance issues with large datasets, follow these best practices for performance tuning, data partitioning,
data preprocessing, sampling strategies, and resource configuration in Docker, Kubernetes, or OpenShift when working
with large datasets.

Data filtering and partitioning

Review the options to filter and partition your data.

Use SPL to filter and summarize data

You can filter your data with SPL before sending it to the container as shown in the following example:

index=your_big_index
| search eventtype=anomalies source="some_path"
| stats count by user
| fit MLTKContainer ...
Aggregate or summarize large logs if you only need aggregated features. For time-series events, consider summarizing
by the minute or hour.

Running the fit command on raw events can cause excessive memory consumption. Follow best practices for data
preparation.
Use data splitting or partitioning

For large training sets, partition them in multiple Splunk platform searches or chunked intervals:

Index the data as shown in the following example:

index=your_big_index earliest=-30d latest=-15d
| fit MLTKContainer mode=stage ...
Then index another chunked interval from latest=-15d to present.

If your algorithm or code supports incremental or partial training, your notebook can handle partial merges or
checkpointing.
Set container resource tuning

Review the following options for container resource tuning.

CPU and memory requests

In Kubernetes or OpenShift, set the resources.requests.memory and resources.limits.memory attributes to a higher
amount if you anticipate large in-memory DataFrames.

Example:

resources:
requests:
memory: "4Gi"
limits:
memory: "16Gi"
In Docker single-host setups, pass --memory 16g --cpus 4 to limit the memory to 16GB and 4 CPU cores. Adjust to your
usage.

GPU considerations

If your algorithm relies on GPUs, ensure GPU resource requests with nvidia.com/gpu:1. GPU usage helps with large
neural network training, but you must optimize your code for multi-GPU or HPC if you exceed the capacity of a single
GPU.

Development and production containers

Development containers might only need a small memory limit for iterative notebook coding with a sample dataset.
Production containers often require more robust resource allocations if the final dataset is large. Plan your HPC node or
Docker host capacity accordingly.

Data sampling and splitting with SPL

Review methods by which you can use SPL for data sampling and data splitting.

Use the sample command

Using the ML-SPL sample command as follows can randomly downsample events to 10,000, giving a quick dataset for
development or prototyping:
| sample 10000
For final model training, remove or reduce sample command usage, or use partial sampling as shown in the following
example:
| sample partitions=10 seed=42 | where partition_number<7

Partition large datasets

You can partition data using sample partitions=N or a JSON modulo operator (%).
If your code supports incremental training, you can feed in each partition separately as shown in the following example:

index=your_big_index
| sample partitions=10 seed=42
| where partition_number < 8
| fit MLTKContainer algo=...
Then combine or continue training with other partitions in separate runs.

Reduce data volume with data summaries

For extremely large sets of raw data, you can run an initial stats or timechart command to reduce the data volume as
shown in the following example:

index=your_big_index
| stats avg(value) as avg_value, count by some_field
| fit MLTKContainer ...

This approach is useful for time series or aggregator-based machine learning tasks.
Managing memory-intensive code

Consider the following options when managing memory-intensive machine learning code.

Option Description
In-notebook chunking
If your code reads the entire DataFrame at once, consider chunking inside the notebook. For example, using
pandas.read_csv(..., chunksize=100000) if you load data from a .CSV.
For multi-million row data, libraries like Dask, Vaex, or Spark in your container might help and can
handle out-of-core operations.
Partial-fit or streaming
algorithms
Some scikit-learn or River libraries support partial_fit for incremental learning.
If you define partial_fit logic in your notebook, you can stage data chunks one-by-one from the
Splunk platform.
HPC and distributed
approaches
For extremely large datasets, you can perform distributed training with Spark, PyTorch DDP, or Horovod. DSDL can
start the container, but you handle multi-node distribution.
Alternatively, rely on a separate HPC job manager to orchestrate multi-node training, then push
the final results back into the Splunk platform.
Option Description
Managing timeout and resource limits

Review the following table for options to manage your timeout and resource limits:

Option Details
Max search runtime
By default, the Splunk platform can stop searches that exceed certain CPU or wall-clock times. You can increase or
remove that limit if your training or inference is known to be long. Caution: Be mindful if you are increasing from the
default limits to avoid causing issues on your search head.
DSDL container max
time
In DSDL, you can configure a maximum model runtime or idle the stop threshold. If you expect a multi-hour HPC training
job, increase these timeouts so the model doesn't terminate prematurely.
HPC queue or Splunk
search scheduler
If HPC usage is managed by a queue system such as Slurm, you might want to orchestrate jobs outside of the Splunk
platform scheduling. Alternately you can set extended Splunk search timeouts so HPC tasks can complete properly.
Using Splunk Observability for large jobs

Review this table for options using Splunk Observability for large, data intensive jobs:

Option Details
Resource metrics
For large workloads, track container CPU and memory or GPU usage in Splunk Observability or _internal logs.
If usage spikes or the container hits the OOM killers, you see it in container logs or HPC logs.
Step-by-step
logging
If your training takes hours, consider streaming intermediate logs to Splunk HEC, or partial logs in stdout, so you can see
progress.
Alerts from the Splunk platform or Splunk Observability can notify you if usage patterns deviate from
normal. For example, if your memory is climbing unexpectedly.
Example: Large dataset workflow

The following is an example of a large dataset workflow:

Prepare your data. The following example code summarizes data before sending it to the container.
index=huge_data
| search user_type=customer
| stats count, avg(metric) as avg_metric by user
| fit MLTKContainer algo=big_notebook into app:BigModel
1.
Create the container. For Docker or Kubernetes choose 16GB memory, 4 CPU, or possibly 1 GPU.
The code in your notebook uses scikit-learn or PyTorch with chunked data reading as needed.
2.
Set the time. The Splunk platform might only hold the search open for 2 hours. If so, set max time or rely on HPC
queue outside of Splunk.
Container logs or partial metrics appear in _internal or the container logs index.
3.
Save the model. The model is saved as app:BigModel. HPC ephemeral volumes are irrelevant because DSDL
syncs the final artifacts to the Splunk platform.
4.
Troubleshooting performance tuning and large datasets

See the following table for issues you might experience and how to resolve them:

Problem Cause Solution
Container hits OOM killer mid-training. The dataset is too large or thecontainer memory limit is too low.
Increase memory requests in Kubernetes or Docker
--memory. Reduce data size using SPL, or chunk your
data.
The Splunk platform stops the search after N
minutes.
The Splunk platform default
search timeout, or MLTK
container maximum run time, is
too small.
Adjust the max_search_runtime setting or the
container idle stop threshold in DSDL under Setup.
HPC cluster node runs out of GPU memory. The model or data batch size istoo large on the GPU. Adjust your code to reduce batch size, use smallermodel layers, or move to multi-GPU.
You see "RuntimeError:
CUDNN_STATUS_ALLOC_FAILED" in
container logs.
You are out of memory on GPU,
or there is another resource
conflict.
Check the container logs and consider a smaller batch
size. You can also re-check HPC job scheduling if
multiple GPU tasks are overlapping.
Partial data is loaded, but the container never
finishes the fit command.
There is insufficient filtering or no
chunking method in your code,
leading to a large data load.
Use SPL to summarize or chunk data. Consider adding
partial_fit logic in the notebook.
Advanced HPC and GPU usage..............................................................................................................................
The Splunk App for Data Science and Deep Learning (DSDL) integrates with containerized machine learning. DSDL
supports graphics processing unit (GPU) acceleration, large-scale, high-performance computing (HPC) clusters, and
distributed training in Docker, Kubernetes, or OpenShift.

Optimize HPC workflows, including multi-GPU usage, node labeling, ephemeral volumes, and typical HPC environment
considerations.

Overview

When you run the fit or apply commands with DSDL, the external container environment can tap into the following
high-performance computing resources:

GPUs for deep learning acceleration.
Multi-node HPC clusters for distributed training or parallel inference.
Custom scheduling policies to handle concurrency.
DSDL provides a Splunk platform based orchestration of data flows. HPC nodes perform the heavy machine learning
tasks and the Splunk platform manages search, scheduling, and logs. DSDL also offers container images with advanced
libraries such as TensorFlow and PyTorch, with optional GPU support.

With DSDL you can turn on iterative development with development containers, while production HPC containers run with
minimal overhead.

Advanced HPC and GPU requirements

You must meet the following requirements to use advanced HPC and GPU in DSDL:

Requirement Details
HPC cluster
Kubernetes or OpenShift typically orchestrates HPC resources.
Alternatively, single-host Docker HPC can run multi-GPU servers.
For multi-node HPC with Slurm or other schedulers, you can wrap the container environment inside
those HPC job scripts.
GPU drivers and
libraries
NVIDIA GPU nodes typically need the NVIDIA device plugin in Kubernetes or OpenShift.
On Docker single-host environments, you must install nvidia-docker2 or the --gpus runtime.
You must have CUDA and cuDNN libraries and other frameworks in your container if you're doing
deep learning.
HPC network and
storage
HPC nodes typically use high-bandwidth interconnects such as InfiniBand, 10/40/100GbE.
DSDL containers can rely on ephemeral volumes for short data staging, but HPC contexts need
persistent or parallel file systems, such as NFS or GlusterFS.
DSDL continues to sync notebooks and models to the Splunk platform, mitigating ephemeral
volume losses.
Multi-GPU and node labeling

See the following for descriptions of multi-GPU and node labeling in DSDL.

GPU resource requests

In Kubernetes or OpenShift, define GPU requests in your pod or deployment specification as shown in the following
example:

resources:
limits:
nvidia.com/gpu: 1
requests:
nvidia.com/gpu: 1
DSDL automatically uses the GPU if your container image includes GPU libraries such as golden-gpu. The Splunk
platform calls | fit MLTKContainer ... to schedule pods with nvidia.com/gpu:1.

Node labeling and taints

HPC clusters might label GPU nodes such as gpu=true, or add taints so that only GPU workloads land on them.
In DSDL, set the appropriate node selector or tolerations in your container environment and Kubernetes cluster
configuration if you want certain tasks only on GPU nodes.

Single and multi-GPU tasks

For single-GPU tasks, request nvidia.com/gpu:1.
For multi-GPU tasks such as distributed data parallel training, request multiple GPUs in your Pod spec or define a
ReplicaSet with multiple GPU pods. This is an advanced option and requires your notebook code such as PyTorch DDP,
or Horovod, to handle multi-GPU scaling.

Distributed training approaches

Review the following distributed training approaches for HPU and GPU usage:

Training approach Description
Single container, multiple
GPUs
This is the simplest approach for HPC. A single container hosts multiple GPUs.
Within your notebook code, use the PyTorch DataParallel or TensorFlow MirroredStrategy to
leverage multiple GPUs in one host.
You don't need to make any changes to your Splunk platform search logic because DSDL
considers it 1 container.
Multi-container, inter-node
communication
For large HPC or multi-node distributed training, you can spawn multiple containers or pods, that communicate
through MPI or the PyTorch torch.distributed package.
DSDL does not manage multi-node orchestration by default but you can set it up with your
HPC scheduler or an advanced Kubernetes operator.
Searching or scheduling in the Splunk platform triggers the job, but the container's code
handles multi-node communication.
DSDL integration
In advanced HPC workflows, you can call the fit or apply commands, but your notebook code must handle
the distributed logic.
HPC node ephemeral logs or partial metrics route to Splunk through HEC or container logs.
About development and production HPC containers

See the following for key points about development and production HPC containers.

Development HPC containers

Uses JupyterLab plus GPU libraries.
Lets data scientists refine code on a single HPC node with 1 to 2 GPUs or smaller data subsets.
Is potentially ephemeral because after the development session ends, the container is stopped.
Production HPC containers

Uses minimal overhead because it uses no Jupyter or development tools.
Runs multi-GPU or multi-node distributed tasks.
Is used by scheduled searches or repeated inference jobs in the Splunk platform.
Must have defined GPU resource requests if you need GPU acceleration.
How HPC is used in Splunk Observability

See the following for descriptions of Splunk Observability and HPC.

HPC monitoring

HPC clusters typically ship with node-level metrics such as Ganglia or Prometheus. You can forward these metrics to the
Splunk platform or Splunk Observability to unify HPC usage with container-level insights.

GPU telemetry

For GPU usage, consider NVIDIA DCGM or device plugin exporters that feed GPU metrics into Splunk Observability. If
you turn on Splunk Observability in DSDL, you can automatically instrument each container endpoint, although HPC
multi-node training might require custom tracing logic in your code.

Security and governance

See the following for descriptions of security and governance options available for HPC and GPU usage:

Option Description
Container registry and
minimal GPU images
HPC clusters typically have a local Docker registry. You can build or pull GPU images such as golden-gpu and then
push them to your HPC registry.
Use minimal or specialized images to reduce overhead. An air-gapped DSDL setup might apply if
HPC has no external net. See Install and configure the Splunk App for Data Science and Deep
Learning in an air-gapped environment.
Role-based access to
GPU nodes
In Kubernetes and OpenShift, use RBAC or taints and tolerations so that only power users, or HPC roles, can
schedule GPU containers.
In Docker single-host HPC, you must rely on local user constraints or Docker group membership.
Automatic notebook
sync
DSDL design means that HPC ephemeral volumes are not at risk of losing code.
For HPC operators you can treat ephemeral container usage as stateless, letting the Splunk
platform manage the notebooks.
Example: HPC workflow

The following is an example of a high-performance computing (HPC) workflow:

Create a Kubernetes HPC cluster with GPU nodes labeled as gpu=true.
Create a custom-built my-gpu-image container image with frameworks and libraries such as Torch, CUDA, and
cuDNN.
2.
Make sure the file points to myregistry.local/my-gpu-image:latest in the images.conf file.
Complete the DSDL setup fields:
1. Container type: GPU runtime.
2. Resource requests: nvidia.com/gpu:1.
3. Container mode: DEV or PROD.
4.
Run the following search:
index=my_data
| fit MLTKContainer algo=my_gpu_notebook features_* into app:MyHPCModel
5.
Kubernetes schedules a pod on a GPU node. The container loads your code, trains a PyTorch model, and
streams logs or partial metrics to the Splunk platform.
6.
The model is now available in DSDL as app:MyHPCModel.
HPC ephemeral volumes are irrelevant because the code and final artifacts are synced to DSDL.
7.
Troubleshooting HPC and GPU usage

See the following table for issues you might experience and how to resolve them:

Issue Cause Solution
Container never
schedules on GPU node
You might be missing the nvidia.com/gpu:1
request, or the HPC node is not labeled for
GPU.
Check your Kubernetes pod spec or the images.conf file to confirm
HPC node labeling is gpu=true. Additionally, check the device
plugin.
Multi-GPU training fails
silently
Notebook code is not configuring multi-GPU, or
it is missing distribution logic.
HPC logs in containers of stdout and stderr. See if the PyTorch
DataParallel configuration or multi-node configuration is correct.
Docker single-host HPC
container sees no GPUs
You might not be using --gpus all or
runtime=nvidia for Docker run commands.
Check the Docker CLI usage or logs for "no GPU devices found"
errors.
HPC cluster can't pull
the GPU image
Private registry authentication error or
air-gapped images might be missing.
Re-check credentials or ensure you loaded .TAR files on the HPC
node registry.
HPC ephemeral volumes
losing code in notebooks
DSDL sync scripts or configuration might be
failing.
Check _internal "mltk-container" logs for sync errors.
Note: The Splunk platform automatically persists notebooks, so
ephemeral is acceptable.
Extend the Splunk App for Data Science and Deep Learning with custom notebooks...........................................
You can define custom notebooks for specialized machine learning or deep learning tasks with the Splunk App for Data
Science and Deep Learning (DSDL). By writing your own Jupyter notebooks, you can incorporate custom algorithms,
advanced Python libraries, domain-specific logic, and pull in data from the Splunk platform within the same environment.

Create, export, and maintain notebooks so that they seamlessly integrate with the ML-SPL commands of fit, apply, and
summary.

Overview

When you develop a notebook in DSDL you can perform the following tasks:

Write Python code for data preprocessing, model training, or inference.
Expose that code to ML-SPL by defining functions such as fit and apply within special notebook cells.
Automatically export the code into a Python module at runtime.
Call those functions from Splunk platform searches.
Pull data directly from the Splunk platform using the Splunk Search API integration, allowing for interactive data
exploration in your Jupyter notebook environment.
•
Your custom code operates in the external container environment while staying fully integrated with Splunk platform
search processing.
DSDL notebook components

A DSDL notebook typically includes the following components:

Component Description
Component Description
Imports and setup
Imported libraries such as NumPy, Pandas, and PyTorch.
Can define global constants or utility functions.
fit function
A Python function that trains or fits your model.
Accepts data as a Pandas DataFrame and hyperparameters, returning model artifacts.
apply function
(Optional) Used for inference or prediction.
Accepts new data and the trained model, and returns predictions.
summary function (Optional) Provides metadata about the model such as hyperparameters or training stats.
Other utility functions (Optional) Runs data cleaning, advanced transforms, or direct data pulls using the Splunk Search API.
When you save a notebook, DSDL automatically generates a corresponding .py file in /srv/notebooks/app/ directory or
a similar directory. The corresponding .py file uses the same base name as the notebook, for example
my_notebook.py. When saved, the fit, apply, and summary functions can be called from ML-SPL.
The following example notebook is comprised of different components:

---
jupyter:
jupytext:
formats: ipynb,py
notebook_metadata_filter: all
---
import json
import numpy as np
import pandas as pd
import os

MODEL_DIRECTORY = "/srv/app/model/data/"

from dsdlsupport import SplunkSearch as SplunkSearch
search = SplunkSearch.SplunkSearch()
df = search.as_df()
df

def init(df,param):
model = {}
model['hyperparameter'] = 42.0
return model

model = init(df,param)
print(model)

def fit(model,df,param):
info = {"message": "model trained"}
return info

print(fit(model,df,param))

def apply(model,df,param):
y_hat = df.index

result = pd.DataFrame(y_hat, columns=['index'])
return result

print(apply(model,df,param))

def summary(model=None):
returns = {"version": {"numpy": np.version, "pandas": pd.version} }
return returns

Notebook-to-module mechanism

DSDL runs the following internal mechanism that scans the notebook for functions named fit, apply, and summary:

Trigger autosave: Each time you save the notebook in JupyterLab, a conversion step occurs.
Export Python: Relevant Python cells such as a cell containing the fit function, are written into a .PY module. For
example /srv/notebooks/app/<notebook_name>.py.
2.
Run ML-SPL lookup: The MLTKContainer command dynamically imports <notebook_name> at runtime to run the
fit, apply, and summary functions.
3.
You can help ensure this internal mechanism runs well in the following ways:

Avoid function name collisions such as 2 separate fit definitions in the same notebook.
If you rename your notebook file, a new .PY module is created but the older file isn't deleted. Remove older
references that you no longer need.
•
Defining and passing parameters

Document your notebook's expected parameters so users know which SPL arguments to provide. Use sensible defaults
to avoid a Python KeyError if a parameter (param) is missing. All parameter values from ML-SPL are strings. You can
convert parameters toint,float, orboolas needed.

In the following example, all ML-SPL arguments after algo=<my_notebook> are passed to your notebook's Python code as
the param dictionary:

| fit MLTKContainer algo=my_notebook alpha=0.01 epochs=10 ...

def fit(df, param):
alpha = float(param.get('alpha', 0.001))
epochs = int(param.get('epochs', 10))
...

Use param.get('key', default_value) to handle optional arguments.
Stage data with iterative development in notebooks

You can use mode=stage for iterative development and data staging. Complete the following steps:

If you want to push only a subset of Splunk platform data to your notebook without training, follow this syntax:
| fit MLTKContainer mode=stage algo=my_notebook features_* into app:MyDevModel
This sends .CSV data to the container but does not call the fit command.
1.
Open JupyterLab, and define or call a helper function as follows:
def stage(name):
with open("data/"+name+".csv", 'r') as f:
df = pd.read_csv(f)
2.
with open("data/"+name+".json", 'r') as f:
param = json.load(f)
return df, param
df, param = stage("MyDevModel")
To debug, open my_notebook.ipynb in JupyterLab to test or modify code, using the staged data.
Manually call your init, fit, or apply functions on that data to debug as needed.
Pull data directly into a notebook using the Splunk Search API

In addition to staging data with mode=stage, you can pull data directly using the Splunk Search API.

Complete the following steps:

Turn on access to the Splunk platform on the DSDL Setup page. Provide your Splunk host, port 8089, and a valid
token.
1.
Import SplunkSearch in your notebook, then either use an interactive search widget or define a predefined query.
Run the query to retrieve data into a Pandas DataFrame in your notebook.
For example:
from dsdlsupport import SplunkSearch
search = SplunkSearch.SplunkSearch()
df = search.as_df()
df
If you encounter connectivity issues, confirm firewall rules or check the _internal logs for mltk-container errors
referencing timeouts.
3.
Storing and sharing notebooks

Apply the following methods for version control and collaboration with custom models:

Store notebooks in a Git repo, allowing for merges, pull requests, and versioning.
By default, notebooks are stored in /srv/notebooks/. You can sort them by projects or by teams.
Jupyter saves automatically, but you can consider manually committing .IPYNB and .PY changes to Git for
auditing.
•
Advanced notebook patterns

You can use advanced notebook patterns with custom models:

Notebook pattern Description
Multiple models per
notebook
You can define multiple training algorithms in a single .IPYNB file, but only one fit method is recognized. If you
want to differentiate between them, parse extra arguments in param or create separate notebooks for clarity.
Additional utility
functions
You can define custom data preparation, feature engineering, or advanced plotting in separate Python cells. As long
as they're not named fit, apply, or summary, they won't be exported to ML-SPL.
Auto-generating
additional metrics
You can log metrics or epoch-by-epoch logs to the Splunk platform. For example, you can write them to a CSV file
that's forwarded, or send them to HTTP Event Collector (HEC) in real time.
Best practices for creating notebooks

Consider the following when creating custom notebooks:

DSDL only recognizes exact cell names. Be mindful of any typos when using init, fit, apply, and summary.
All parameter values from ML-SPL are strings. You can convert parameters to int, float, or bool as needed.
If your container image lacks large libraries, it results in an ImportError. Add large libraries through Docker.
Use unique .IPYNV filenames to help avoid conflicts or overwriting the file in /srv/notebooks/app/.
If you rely on Splunk search, ensure the container can reach the Splunk platform firewall, DNS, and TLS settings.
Example: Create a custom notebook

The following is an example workflow of creating a custom notebook:

Start a dev container in DSDL, then open JupyterLab.
Create a notebook and save it as my_custom_algo.ipynb in JupyterLab.
Define code: Write cells for init, fit, apply, and summary, optionally using the Splunk Search API.
Pull data with df, param = stage("MyTestModel") or use the Splunk Search API.
Test logic interactively.
4.
Save your file. DSDL exports your code to my_custom_algo.py.
Train the model in the Splunk platform:
index=my_data
| fit MLTKContainer algo=my_custom_algo features_* into app:MyProdModel
6.
Apply the model:
index=my_data
| apply my_custom_algo
7.
Container monitoring and logging............................................................................................................................
The Splunk App for Data Science and Deep Learning (DSDL) leverages external containers for computationally intensive
tasks. It is crucial to monitor these containers for debugging, operational awareness, seamless model development, and a
stable production environment.

Learn about collecting logs, capturing performance metrics, automatically instrumenting containers with OpenTelemetry,
and surfacing container health in the Splunk platform or Splunk Observability Cloud.

Overview

When you run the fit or apply commands in DSDL, a Docker, Kubernetes, or OpenShift container is spun up to run
model training or inference.

Splunk Observability Cloud performs the following actions to help inform container health:

Collects container logs of stdout, stderr, and custom logs in the Splunk platform to debug errors or confirm job
completion.
•
Captures performance metrics like CPU, memory, and GPU usage in real time to diagnose slow jobs or resource
bottlenecks.
•
Enables OpenTelemetry instrumentation for container endpoints in Splunk Observability Cloud if toggled in the
DSDL Observability settings.
•
Ensures enterprise-level reliability by setting up dashboards, alerts, or autoscaling triggers based on these
metrics.
•
DSDL includes the following logs and telemetry data to inform container health:

Splunk _internal index logs about container management.
Container logs of stdout and stderr like ML library messages, and Python prints.
Custom logs or metrics you send to Splunk HTTP Event Collector (HEC).
OpenTelemetry data sent to Splunk Observability Cloud after you enable observability in the DSDL setup.
Container logs in the Splunk platform

The following container logs are provided in the Splunk platform.

MLTK container logs

The MLTK container logs in the _internal index generate when DSDL tries to start or stop a container, or hits network
issues. These logs are stored in the _internal index with "mltk-container" in the messages.

For example, index=_internal "mltk-container".

If containers fail to launch, these logs show network errors or Docker or Kubernetes API rejections. Repeated
connection attempts can indicate firewall or TLS misconfigurations.
Automatic container logs with the Splunk platform REST API

After a container is successfully deployed, DSDL automatically collects logs through the Splunk REST API. Automatic
container logs are useful for quick debugging or reviewing final outputs when a machine learning job is complete.

If the container fails before initialization, automatic container logs might not appear. Check the _internal index logs
instead.
You can view the logs by navigating in DSDL to Configuration , then Containers , and then selecting the container name.
For example, DEV.

The selected container page shows the following details:

Container Controls: The container image, cluster target, GPU runtime, and container mode of DEV or PROD.
Container Details: Key-value pairs for api_url, runtime, mode, and others.
Container Logs: A table or search result similar to the following:
| rest splunk_server=local services/mltk-container/logs/<container_name>
| eval _time = strptime(_time,"%Y-%m-%dT%H:%M:%S.%9N")
| sort - _time
| fields - splunk_server
The Container Logs surfaces the real-time logs captured from the container after it's fully deployed.
•
Custom Python logging

If your notebook code logs with print(...) or with the Python logging module, logs get stored in the stdout or stderr
container.

High-performance computing (HPC) tasks with high verbosity can produce large volumes of logs. Consider limiting the
logs to show only INFO or WARN log levels.
Resource metrics

Tracking resource usage can help you identify if your training jobs are hitting resource bottlenecks or if you need better
scheduling or bigger node types.

See the following table for what metrics are available by container provider:

Container Description
Docker Use platform or Splunk Observability Cloud.docker stats for ephemeral checks, or use a cAdvisor-based approach to forward metrics into the Splunk
Kubernetes or
OpenShift
Use the Kubernetes metrics API or Splunk Connect for Kubernetes for CPU, memory, and node metrics. Note: GPU
usage requires the NVIDIA device plugin or GPU operator.
You can also set up alerts for abnormal usage patterns or container crash loops, which can also improve your resource
reliability.

Automatic OpenTelemetry instrumentation

OpenTelemetry instrumentation can provide advanced insights into container endpoint usage, request durations, and data
flow, for HPC or microservices-based machine learning pipelines.

After you turn on Splunk Observability Cloud, DSDL can automatically instrument container endpoints with
OpenTelemetry:

In DSDL, go to Setup , and then Observability Settings.
Select Yes to turn on Observability.
Complete the required fields:
1. Splunk Observability Access Token: Add your Observability ingest token.
2. Open Telemetry Endpoint: Set your endpoint. For example, https://ingest.eu0.signalfx.com.
3. Open Telemetry Servicename: Enter the service name you want to open. For example, dsdl.
3.
Save your changes
Upon completion, all container endpoints including training and inference calls, generate Otel traces. These traces are
automatically stored in Splunk Observability Cloud for deeper analysis, including request latency and container-level CPU
and memory correlation.

Instrumentation is done automatically. You do not need to manually set up Otel libraries in your notebook code.
Sending model or training logs to the Splunk platform

Review the following options for sending model or training logs to the Splunk platform as a DSDL user.

Splunk HEC in DSDL

The Splunk HTTP Event Collector (HEC) option in DSDL lets you view partial results or step-by-step logs. You can
combine HEC with container logs for full details.

In DSDL, navigate to the Setup page and provide your HEC token in the Splunk HEC Settings panel. Save your
changes.

In your notebook, use the following code:

from dsdlsupport import SplunkHEC
hec = SplunkHEC.SplunkHEC()
hec.send({'event': {'message': 'operation done'}, 'time': 1692812611})
Logging epoch metrics

You can use epoch metrics to visualize model training progression in near real time.

See the following example of how to view epoch metrics:

def fit(model, df, param):
for epoch in range(10):

...
hec.send({
'event': {
'epoch': epoch,
'loss': 0.1234,
'status': 'in_progress'
}
})
return {"message": "model trained"}
In the Splunk platform you can use the following as an example of how to view epoch metrics:

index=ml_logs status=in_progress
| timechart avg(loss) by epoch
Example workflow

The following is an example workflow for monitoring container health:

You set up the Docker or Kubernetes environment with Splunk Connect or a Splunk Observability Cloud agent.
You launch a container:
| fit MLTKContainer algo=...
2.
After the container launches, DSDL automatically collects logs. In DSDL, you go to Configuration , then
Containers , then <container_name> to see container details and logs.
3.
If Splunk Observability Cloud is enabled, container endpoints generate Otel traces. CPU and memory metrics flow
to Splunk Observability Cloud.
4.
If DSDL calls hec.send(...), partial training logs appear in the Splunk platform.
All data, including logs, traces, and metrics correlates for a 360 degree view.
Container monitoring guidelines

Consider the following guidelines when implementing container monitoring:

Limit log verbosity. HPC tasks can produce large logs. Use moderate logging levels.
Check the _internal index. For container startup or firewall issues, search _internal "mltk-container".
Secure observability. Use transport layer security (TLS) for container endpoints, and secure tokens for Splunk
Observability.
•
Combine with container management. For concurrency, GPU usage, or development or production containers,
see Container management and scaling.
•
Troubleshooting container monitoring

See the following issues you might experience with container monitoring and how to resolve them:

Issue How to troubleshoot
Container fails to launch
Likely caused by Docker or Kubernetes being unreachable, with a firewall
setting blocking the management port.
Check the _internal logs for "mltk-container" for network or
authorization errors.
Observability is toggled on, but no Otel traces appear
Likely caused by an incorrect Splunk Observability Cloud token, or endpoint, or
the container configuration is not updated.
In DSDL go to Setup then Observability Settings.
Confirm a valid token and endpoints. Restart the container if you
make any changes.
2.
High-performance computing (HPC) tasks with large logs are
flooding your Splunk platform instance
Likely caused by overly verbose training prints or debug mode.
Switch to INFO or WARN level, or only send partial logs with Splunk
HTTP Event Collector (HEC).
GPU usage not recognized in Splunk Observability Cloud
dashboards
Likely caused by a missing NVIDIA device plugin or GPU operator in
Kubernetes or OpenShift.
Check node labeling, device plugin logs, and GPU operator
deployment.
HEC events missing in the Splunk platform
Likely caused by the wrong HEC token, disabled HEC, or an endpoint
mismatch.
Check the _internal logs for "Token or HEC" errors. Ensure HEC
is enabled and the 443/8088 port is open.
Container management and scaling........................................................................................................................
Use external containers with the Splunk App for Data Science and Deep Learning (DSDL) to offload resource-heavy
machine learning tasks from the Splunk search head. This architecture isolates potentially large workloads, and allows for
horizontal scaling, GPU acceleration, and robust environment management.

Review the following guidelines to manage container lifecycles, scale concurrency, and optimize resource usage when
running DSDL in Docker, Kubernetes, or OpenShift.

Overview

When you run DSDL commands such as | fit MLTKContainer ... or | apply ..., DSDL communicates with an
external container platform. DSDL communicates with Docker on a single host, or with a cluster orchestrated by
Kubernetes or OpenShift.

By default, development (DEV) mode containers include JupyterLab, TensorBoard, and other developer tools. Production
(PROD) mode containers are minimal, running just the Python processes required for model training and inference.

Understanding how these containers are launched, monitored, and scaled can help with efficient resource usage and
robust enterprise-grade workflows.

Container lifecycle

Review the following descriptions of a container lifecycle:

Lifecycle stage Description
Trigger container
launch
When a user runs an ML-SPL command in the Splunk platform, such as | fit MLTKContainer
algo=..., DSDL checks if a container or pod is already running with the correct configuration. If not, a new
one is launched.
If a scheduled search includes thefitorapplycommands, DSDL might spin up containers in the background
at regular intervals.
If a user manually starts a container in DSDL, such as for developmental tasks or to use Jupyter, DSDL
launches the container.
Initialize container
DSDL calls the Docker, Kubernetes, or OpenShift API to create a container or pod based on your chosen image. For
example golden-cpu image.
The container environment variables are set in DSDL configuration. Example variables include
JUPYTER_PASSWD and container_enable_https.
Run active container
Once started, the container is available to handle fit or apply commands.
In DEV mode, JupyterLab or TensorBoard endpoints can be accessed through mapped ports,
Routes, or NodePorts.
Stop idle container After a period of inactivity and depending on your setup, DSDL might automatically stop the container to free resources.
Remove and clean
up container
Older or crashed containers are removed from the system. On Kubernetes or OpenShift pods are ephemeral by design
and typically cleaned up automatically.
Comparing Docker, Kubernetes, and OpenShift containers

Review the following differences between Docker, Kubernetes, and OpenShift containers in DSDL:

Container Typical use case Network setup Scaling Management
Single-host
Docker
Smaller dev or test
environments or single
Splunk platform instance
with Docker on the same
machine.
By default, the container might be on
unix://var/run/docker.sock or
tcp://localhost:2375, without TLS.
Usually limited to 1
container or pod per
host unless you
manually script
multiple Docker hosts.
DSDL starts and stops the
container through the Docker
API. Development containers
might keep running until
manually stopped.
Kubernetes
or OpenShift
Production-scale or
distributed environments.
Use TLS or HTTPS from the Splunk
platform to the Kubernetes or OpenShift
You can define
multiple replicas, or
DSDL translates container
requests into pod
API server on port 6443. rely on Kubernetes
Horizontal Pod
Autoscaler (HPA) for
concurrency.
deployments. You can
configure resource requests,
node labeling (GPU), and
advanced security contexts.
Container Typical use case Network setup Scaling Management
Concurrency and scaling patterns

Review the following descriptions of concurrency and scaling patterns in DSDL:

Pattern Description
Horizontal Pod Autoscaler (HPA)
on Kubernetes or OpenShift
HPA can auto-scale pods based on CPU or memory usage.
For DSDL, you might define an HPA that spawns additional pods if usage surpasses
certain thresholds.
HPA helps handle multiple concurrent Splunk platform searches that call the fit or
apply commands simultaneously.
Docker Compose or scripts
If you're using single-host Docker, scaling typically involves manually launching multiple containers or
writing scripts to do so.
DSDL won't automatically create multiple containers on Docker unless you handle it
outside of the Splunk platform.
GPU scheduling
For GPU-based containers in Kubernetes or OpenShift, assign a label or request nvidia.com/gpu:
1 so that the container lands on GPU-enabled nodes.
In Docker, ensure --gpus all or similar flags are used if you want GPU acceleration.
Comparing development and production containers

Review the following descriptions of development (DEV) and production (PROD) containers:

Container
type
Description
DEV containers
Uses JupyterLab for interactive notebook development.
TensorBoard or other development tooling might be exposed on additional ports such as 8888 for
Jupyter, or 6006 for TensorBoard.
Typically used short-term to refine code, test data staging, or debug advanced logic.
PROD containers
Uses minimal setup, containing only the necessary Python environment for model training and inference.
No Jupyter or development ports are exposed which reduces the attack surface and resource overhead.
Might run on multiple replicas if concurrency is high.
Configuring DSDL operations

Review this overview of the DSDL operations you can access in DSDL:

DSDL
operation
Where to find it Description
DSDL
operation
Where to find it Description
View container
dashboard In DSDL select Configuration , and then Containers.
You can see currently running containers and pods, start or stop
them, and open Jupyter or TensorBoard if you're in DEV mode.
View logs and
diagnostics
Check Splunk _internal logs with
"mltk-container" to reveal container startup errors,
such as network timeouts or Docker and Kubernetes
rejections.
You can forward container logs to the Splunk platform, letting you
see Python exceptions from the fit or apply commands.
Clean up idle
containers
Configure idle containers to stop after a certain timeout in
the DSDL app.
DSDL typically stops idle containers after a certain timeout. In
Kubernetes and OpenShift, old pods might remain in a
"Completed" or "Terminated" state, but cluster housekeeping
eventually prunes them.
Resource allocation and scheduling

Review the following options for resource allocation and scheduling in DSDL:

Option Description
CPU and memory
requests
In Kubernetes, define requests and limits in your pod or deployment specification. This ensures the container won't
exceed certain CPU or memory usage.
On Docker, you can specify --cpus or --memory if you manually run containers.
GPU resources
On Kubernetes or OpenShift, you must configure GPU node drivers or device plugins such as NVIDIA so that pods
requesting nvidia.com/gpu: 1 schedule properly.
On Docker, use the runtime=nvidia setting or an environment variable to link GPU libraries.
Production best
practices
Monitor ephemeral storage usage because large data staging or logs can fill ephemeral volumes.
Monitor container logs for OOM killer events, which indicate insufficient memory limits.
Typical container management and scaling use cases

See the following common use cased for container management and scaling:

Use case Description
Multiple DEV containers Each data scientist spawns a personal DEV container with Jupyter. They eventually merge and storecode in Git.
1 PROD container in Docker Single-host environment with moderate concurrency. The Splunk platform calls 1 container to handlemodel training and inference sequentially.
Kubernetes high-performance
computing (HPC)
Large-scale HPC environment with multiple GPU nodes. Kubernetes auto-scales pods so concurrent
machine learning tasks each get their own container.
OpenShift Enterprise Container
Platform Large-scale HPC environment integrated with the Red Hat security or operator frameworks.
Troubleshooting container management and scaling

See the following issues you might experience and how to resolve them:

Problem Solution
Container fails to start
Check _internal logs for mltk-container messages about Docker or Kubernetes API errors or
timeouts.
Ensure the Docker REST socket or Kubernetes API server is reachable.
Development (DEV) container
times out If DEV containers auto-stop, adjust the idle timeout or manually keep them active in the DSDL app.
Resource exhaustion If logs indicate Out of Memory (OOM) kills, or CPU throttling, raise the memory or CPU requests inKubernetes, or refine Docker resource constraints.
GPU not recognized
Confirm that you have the correct GPU drivers, device plugins, or runtime=nvidia if using Docker.
Check container logs or the _internal index for GPU scheduling errors.
Example: Kubernetes multi-pod setup

The following steps are for an example multi-pod setup in Kubernetes:

Configure DSDL. In DSDL go to Setup , then select Connect to your Kubernetes cluster.
Define a deployment. DSDL automatically creates a deployment for DEV or PROD containers. You can edit the
resource specs or add a Horizontal Pod Autoscaler (HPA) as follows:
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
name: dsdl-hpa
spec:
scaleTargetRef:
apiVersion: apps/v1
kind: Deployment
name: dsdl-dev
minReplicas: 1
maxReplicas: 5
metrics:
type: Resource
resource:
name: cpu
target:
type: Utilization
averageUtilization: 70
2.
Use DSDL. The Splunk platform calls the fit or apply commands, and DSDL spawns pods. If CPU usage is high,
Horizontal Pod Autoscaler (HPA) scales up.
3.
Observe container states. In the Kubernetes dashboard or on the DSDL Containers page, you can see how many
pods are active.
4.
Advanced container customization..........................................................................................................................
The Splunk App for Data Science and Deep Learning (DSDL) relies on container images for CPU or GPU-based machine
learning workloads. The app ships with certain default images, including Golden CPU and Golden GPU.

Your organization might need to modify, secure, or extend these images for specialized libraries, security requirements, or
offline, otherwise known as air-gapped environments. The splunk-mltk-container-docker GitHub repository provides the
Dockerfiles, requirements files, and scripts required to build, customize, and manage these container images.

You can use the repository to build and tailor container images for high-performance computing (HPC) -level model
training, specialized Python dependencies, or compliance with internal security standards. By understanding the scripts,
tag_mapping.csv, and Dockerfiles, you can complete the following tasks:

Add new libraries or pinned dependencies.
Switch to GPU runtimes or different base OS images.
Scan containers for vulnerabilities.
Automate builds with a continuous integration (CI) pipeline.
Integrate seamlessly with the images.conf file for a frictionless DSDL experience.
If you require additional customization such as Red Hat environment compliance, or packaging proprietary libraries, the
flexible scripting approach in the build.sh, bulk_build.sh, and compile_image_python_requirements.sh files ensures you
can keep your images in sync with your enterprise policies. Combine this customization with other DSDL advanced
workflows to fully operationalize machine learning at scale within the Splunk platform.

What's in the splunk-mltk-container-docker repository

The splunk-mltk-container-docker GitHub repository hosts the Dockerfiles, scripts, and requirements needed to create
the container images used by DSDL.

Review the following table for descriptions of the repository components:

Component Description
/dockerfiles/
Contains multiple Dockerfiles and includes files in different base operating systems such as Debian and UBI, and
library sets such as golden-cpu, minimal-cpu, spark, and rapids.
For example, Dockerfile.debian.golden-cpu installs an array of data science libraries on Debian.
Dockerfile.redhat.ubi.golden-cpu does the same for Red Hat UBI9.
/requirements_files/
Houses Python requirements files that define which libraries get installed in each image variant.
Each image is typically split into base_requirements and specific_requirements to handle
minimal and golden additions.
/scripts/
Shell scripts for building, bulk-building, scanning, and testing images.
For example:
The build.sh shell script builds a single image based on a chosen tag from tag_mapping.csv.
The bulk_build.sh builds multiple images from a list of tags.
The scan_container.sh uses Trivy to scan for vulnerabilities.
The test_container.sh runs Playwright-based UI tests on a container.
tag_mapping.csv
A critical .CSV file enumerating build configurations. For example, golden-cpu, golden-gpu, and minimal-cpu.
Each row maps a tag to the base image, Dockerfile, requirements files, and runtime flags.
/images_conf_files/
Stores the generated images.conf stanzas that you can merge into the Splunk platform
/mltk-container/local/ directory.
Each .conf file corresponds to a built image, letting DSDL know which images are available.
Configuring the main scripts in the splunk-mltk-container-docker repository

Review the following descriptions of the main scripts and how they fit into a typical build pipeline:

All scripts are in the /scripts/ directory of the repository.
build.sh

Script information Description
Overview Build a single container image using configuration from tag_mapping.csv.
Syntax ./build.sh <build_configuration_tag> <repo_name> <version>
Parameters • • build_configuration_tagrepo_name: Optional prefix for the Docker repo.: References a row in tag_mapping.csv.
version: A version tag for the final image.
Example ./build.sh golden-cpu splunk/ 5.1.1
Workflow
Reads the row for golden-cpu in tag_mapping.csv to find the base image, Dockerfile, and
requirements files.
1.
Optionally compiles Python requirements if not pre-compiled.
Executes docker build with the chosen Dockerfile and context.
Generates a .conf file in /images_conf_files/ describing the new image.
bulk_build.sh

Script information Description
Overview Builds all containers or a subset from a CSV listing.
Key step Iterates over each line in tag_mapping.csv to call build.sh for each configured tag.
Syntax ./bulk_build.sh <tag_mapping.csv> <repo_name> <version>
Example ./bulk_build.sh tag_mapping.csv splunk/ 5.1.1
compile_image_python_requirements.sh

Script
information
Description
Overview Pre-compiles or locks Python dependencies for a given image variant to reduce build-time or avoid dynamicdependency resolution.
Syntax ./compile_image_python_requirements.sh <tag_name>
Workflow 1. 2. Builds a minimal environment Dockerfile to resolve Python packages.Outputs a pinned/locked requirements file in requirements_files/compiled_*.txt.
Speeds up future builds by installing pinned versions of each library.
test_container.sh

Script
information
Description
Script
information
Description
Overview Runs a set of integration tests against a built container using Playwright or other testing frameworks. Used to simulateSplunk platform and Jupyter interactions or to validate container endpoints are running as expected.
Prerequisite A local Python virtual environment or system Python with the correct dependencies to run Playwright.
Syntax ./test_container.sh <tag_name> <repo_name> <version>
scan_container.sh

Script information Description
Overview Uses Trivy to scan the built container for vulnerabilities.
Syntax ./scan_container.sh <tag_name> <repo_name> <version>
Benefits • Identifies potential Common Vulnerabilities or Exposures (CVEs) or insecure packages in the finalimage.
Ensures compliance with security standards for production-grade images.
Configuring tag mapping

The tag_mapping.csv file orchestrates the following build logic:

Column name Details
Tag
Short name for the image variant. For example golden-cpu, minimal-cpu, or ubi-golden-cpu.
Used as <build_configuration_tag> in build.sh.
base_image
Base operating system (OS) image. For example debian:bullseye or
registry.access.redhat.com/ubi9/ubi:latest.
Note: Must be accessible to docker pull.
dockerfile
The Dockerfile to use. For example Dockerfile.debian.golden-cpu.
Is located in /dockerfiles/.
base_requirements
The base Python requirements file. For example base_functional.txt.
Is found in /requirements_files/.
specific_requirements
Additional specialized libraries. For example specific_golden_cpu.txt.
Is usually large ML libs like TensorFlow or PyTorch.
runtime
Is none or nvidia for GPU usage.
If nvidia the script sets up GPU libraries.
requirements_dockerfile
Optional Docker file used for pre-compiling Python dependencies.
For example Dockerfile.debian.requirements.
The following is an example of the content found within 1 row of the tag_mapping.csv file:

Tag,base_image,dockerfile,base_requirements,specific_requirements,runtime,requirements_dockerfile

golden-cpu,deb:bullseye,Dockerfile.debian.golden-cpu,base_functional.txt,specific_golden
_cpu.txt,none,Dockerfile.debian.requirements

Customize container images

Review the options for customizing container images.

Add extra libraries

If you need a library such as pyarrow or transformers that is not included in specific_golden_cpu.txt you can complete
these steps:

Fork or clone the repository.
Edit or create a new requirements_files/ text file with your library pinned. For example:
# my_custom_libraries.txt
pyarrow==10.0.1
transformers==4.25.1
2.
Create or edit a row in tag_mapping.csv referencing your new file. For example:
Tag,base_image,dockerfile,base_requirements,specific_requirements,runtime,requirements_dockerfile
golden-cpu-custom,deb:bullseye,Dockerfile.debian.golden-cpu,base_functional.txt,my_custom
_libraries.txt,none,Dockerfile.debian.requirements
3.
Build the custom variant. For example:
./build.sh golden-cpu-custom splunk/ 5.2.0
4.
After building, your new image is tagged as splunk/golden-cpu-custom:5.2.0, plus a .conf file is created in
images_conf_files/ that you can merge into the Splunk platform images.conf.
5.
Use a Red Hat Universal Base Image (UBI) minimal approach

If you need a Red Hat UBI9 base for enterprise compliance, complete these steps:

Select a row or create a row referencing Dockerfile.redhat.ubi.golden-cpu.
Edit the ubi-minimal or ubi-golden-cpu Dockerfile for your internal repos and set tag_mapping.csv accordingly.
Accommodate air-gapped deployments

If your deployment is air-gapped or offline, complete these steps:

Bulk build images on an internet-connected machine using bulk_build.sh.
Scan the images with scan_container.sh.
Push to a local registry or save as a .TAR file using Docker Save.
Transfer to the offline environment and use Docker Load.
Update the Splunk platform images.conf to point to your internal registry references.
Guidelines for using customized containers

Consider the following guidelines when using customized containers:

Component Guideline
Python dependency
conflicts
Some advanced ML libraries conflict with older ones. Always run scan_container.sh and consider using
compile_image_python_requirements.sh to lock consistent versions.
Component Guideline
Large image sizes Golden CPU or GPU images can be multiple gigabytes (GB) in size. Consider minimal images if you need only a subsetof libraries.
Requirements
Dockerfile
If you update requirements_files/, remove or regenerate compiled files in /requirements_files/compiled_* or they won't
reflect new pins.
No official support Some scripts and Dockerfiles are unofficial or community features. The Splunk platform fully supports only the officialDSDL containers for standard usage. Caution: Use your custom builds at your own risk.
Security hardening For production, consider scanning your images frequently and applying OS-level hardening. The scan_container.sh scriptis useful, but you can also consider removing unneeded packages or reduce root privileges in Dockerfiles.
Version
management
Maintain a separate branch or fork of the splunk-mltk-container-docker repository. Tag each commit with the
container version you produce so you can replicate or revert builds if needed.
Example: Container customization

The following is an example workflow for a custom golden-cpu image with pinned requirements:

Clone the repo:
git clone https://github.com/splunk/splunk-mltk-container-docker
cd splunk-mltk-container-docker
1.
Create or edit your row in tag_mapping.csv:
Tag,base_image,dockerfile,base_requirements,specific_requirements,runtime,requirements_dockerfile
golden-cpu-custom,deb:bullseye,Dockerfile.debian.golden-cpu,base_functional.txt,my_custom
_libraries.txt,none,Dockerfile.debian.requirements
2.
(Optional) Pre-compile Python requirements:
./compile_image_python_requirements.sh golden-cpu-custom
3.
Build the new image:
./build.sh golden-cpu-custom splunk/ 5.2.0
4.
Scan the built image:
./scan_container.sh golden-cpu-custom splunk/ 5.2.0
5.
Push the image to your Docker registry:
docker push splunk/golden-cpu-custom:5.2.0
6.
Copy the generated .conf snippet in ./images_conf_files/ into your Splunk search head
mltk-container/local/images.conf file.
7.
Restart the Splunk platform or reload DSDL to see the new container listed.
Use the new container in DSDL commands:
index=my_data
| fit MLTKContainer algo=barebone_template mode=stage into app:MyNewModel
container_image="splunk/golden-cpu-custom:5.2.0"
9.
Model governance and security in the Splunk App for Data Science and Deep Learning......................................
Train and serve advanced ML models in containerized environments with tThe Splunk App for Data Science and Deep
Learning (DSDL). Enterprise-grade machine learning might require model governance, secure container management,
and strict access controls to ensure that data, models, and container images meet compliance and operational standards.

Ensure you fulfill these model governance and security requirements for your advanced ML models.

Overview

DSDL supports the following model governance features:

Model training or versioning
Automatic sync for notebooks and models
Container image security, including private registries, image scanning, restricted GPU usage, and custom TLS
certificates
•
Roles, capabilities, and container access
Auditing and traceability
Transport Layer Security (TLS) and data encryption
The following permissions are available with your models:

Permissions Description
App context By default, model names such as app:MyModel are recognized by DSDL.
Sharing Splunk knowledge object sharing can be set to User, App, or Global.
User Visible only to the model creator.
App Shared by users of the same Splunk app.
Global Visible across the Splunk platform and suitable for widely used HPC or production models.
Model retraining or versioning

First, run the following command to create and train a new model:

| fit MLTKContainer algo=my_notebook ... into app:MyModel
DSDL spins up a container, runs the training, and saves model artifacts underapp:MyModel.

The model is stored in the container environment during training, but references appear in the Splunk platform.
To retrain the model, run the following command with new data or parameters. This overwrites old artifacts:

| fit MLTKContainer algo=my_notebook ... into app:MyModel
To version the model , for exampleMyModel_v2, specify a new name in theinto app: clause.

Store ML-SPL and .ipynb code in Git to revert changes easily.
Automatic sync for notebooks and models

DSDL automatically stores your notebooks and model files in the Splunk platform instance. Because containers are
ephemeral by default, automatic sync prevents data loss if ephemeral or NFS volumes go offline and lets new containers
retrieve the same notebooks and models.

The SyncHandler and related scripts remove orphaned containers, reconcile stanzas with actual containers, and ensure
ephemeral data is synced. This preserves your environment from data loss, letting you focus on the machine learning
workflow, rather than container lifecycle details.

Container image security

Review the following options to secure your container images.

Private registry and air-gapped images

You can use a private Docker registry or an air-gapped approach. Push images from golden-cpu, golden-gpu, or custom
to your internal registry. In DSDL go to Setup and then Container Settings , and specify that private registry URL so
DSDL pulls from it.

If your environment doesn't have internet use docker save or load or use bulk_build.sh. Keep a separate Git or artifact
repository with Dockerfiles and pinned requirements.
Image scanning and hardening

Follow these best practices for image scanning and hardening:

Use scripts from [splunk-mltk-container-docker](#) or tools such as Trivy to detect known common
vulnerabilities and exposures (CVE).
•
Remove unneeded packages for minimal images.
Patch OS-level vulnerabilities regularly such as Debian, Red Hat UBI, and so on.
GPU resource restrictions

In Kubernetes or OpenShift, define resource requests so only authorized machine learning tasks can claim GPUs. In
single-host Docker containers, pass --gpus or runtime=nvidia to control GPU usage.

Embedding custom certificates for production HTTPS

In production environments, you must have trusted HTTPS on container endpoints. DSDL images can include your own
TLS certificates instead of the default, self-signed certificates. The splunk-mltk-container-docker repo includes a
certificates folder showing how to embed custom certificates.

For development environments, you can use a self-signed certificate. For production environments, consider using your
organization's CA-signed certificate for higher security.
Follow these steps:

Clone the repo:
git clone https://github.com/splunk/splunk-mltk-container-docker
1.
Place your certificates in the certificates directory, named dltk.key for the private key, and dltk.pem for the
certificate.
2.
(Optional) Generate self-signed certificates for testing:
openssl req -x509 -nodes -days 3650 -newkey rsa:2048 \
-keyout dltk.key -out dltk.pem \
3.
-subj "/CN=bobobobobbo"
Alternatively, create your own CA-signed certificates with the same filenames and dimensions.
Build your container image using scripts:
./build.sh golden-cpu-custom splunk/ 5.2.0
The Docker build automatically copies dltk.key and dltk.pem into /dltk/.jupyter/. This sets up the container to
serve HTTPS endpoints with your certificate.
4.
Make sure the certificate file names are dltk.key and dltk.pem or adapt the Dockerfile references so the container
recognizes them. Only these exact filenames are used at runtime.
Roles, capabilities, and container access

Review the following for information on roles and permissions in DSDL.

DSDL roles and capabilities

DSDL offers the following container-related capabilities:

Capability Description
configure_mltk_container Manages container settings such as Observability tokens, and certificate configurations.
list_mltk_container Lists containers on the container dashboard.
control_mltk_container Starts or stops containers from the DSDL app.
Consider limiting configure_mltk_containercapabilities for Splunk admins, control_mltk_containerfor data-science roles,
and list_mltk_container for general usage.
Model permissions

The following permissions are available with your models:

Permissions Description
App context By default, model names such asapp:MyModelare recognized by DSDL.
Sharing Shares Splunk knowledge objects at the user, app, or global level.
User Shares the model only to the model creator.
App Shares the model to users of the same Splunk app.
Global Shares the model across the Splunk platform. Suitable for widely used HPC or production models.
By default, only the model creator sees the model. For HPC or large production usage, set model sharing to Global.

Securing HEC, Observability, and container endpoints

Use Splunk HEC tokens carefully if you log partial training data. If Observability is enabled, guard your Observability
Access Token. If you want production-level TLS in the container, use embedding custom certificates.

Auditing and traceability

Review the following options for model auditing and traceability.

Option Description
Track model creation in _internal
logs
Use _internal logs to help track who trained which model and when. When you runfit ... into
app:MyModel, logs appear in _internal, referencing information including container staging.
For example:
index=_internal "mltk-container" "into=app:MyModel"
Audit with model summary and
metadata
Running summary MyModel returns model information such as hyperparameters and creation time.
You can build a model catalog or store these events in a dedicated Splunk index for
extended auditing.
Collaborate on and roll back changes
with notebook versioning in Git
DSDL automatically syncs notebooks to the Splunk platform, but you can also store .ipynb files in Git for
collaboration and rollback.
TLS and data encryption

Review the following table for information on TLS and data encryption in model governance and security:

Option Description
TLS from the Splunk platform
to container
Developer containers can use self-signed certificates. Production containers must have properly signed
certificates for TLS.
For a Docker single-host container, the container endpoints handle TLS. For Kubernetes,
often an Ingress object handles TLS termination.
GPU data in transit
Data from the Splunk platform is subject to TLS encryption, even if the container uses GPUs.
The ephemeral GPU usage does not affect encryption but matters for ephemeral volumes,
mitigated by the automated sync to the Splunk platform.
Governance and security guidelines

Review the following guidelines for model governance and security:

Restrict advanced container management capabilities to admin or power users.
Use minimal images, adding only the libraries you need.
•
Use minimal images, adding only the libraries you need.
Use DSDL's automatic sync to avoid ephemeral data loss, and store .ipynb files in Git for version control.
Scan container images with Trivy or the built-in scripts from splunk-mltk-container-docker.
Use custom certificates for production HTTPS in containers.
If Observability is toggled on in DSDL, container endpoints are auto-instrumented with OTel. Confirm your
endpoint, token, and service name.
•
Troubleshooting model governance and security

See the following table for issues you might experience and how to resolve them:

Problem Cause Solution
You see the error model
not found: MyModel
The model is private or in a different
app context.
Adjust sharing permissions or confirm container logs. Search the
_internal logs for mltk-container for references to your model.
HPC node can't pull image There is a private registry or TLS error. Check your Docker or Kubernetes credentials, or check yourimages.conf file references to the registry.
Observability instrumentation
not active on endpoints
Observability is toggled off or has an
invalid token in DSDL.
n DSDL, go to Setup, then Observability Settings. You might need to
restart the container with new configurations.
Notebooks vanish after
container restarts
Ephemeral volume is wiped or NFS is
gone.
Restore the notebooks with the automatic notebook to model sync in
the Splunk platform. Check the _internal logs and
mltk-container for any sync errors.
You see Invalid
certificate on container
endpoint
The container uses self-signed or
misnamed cerificatest, or the container
lacks your official CA.
Place your real certificate in certificates/dltk.pem and
certificates/dltk.key and the rebuild container. Review Docker
logs for TLS load errors.
Splunk App for Data Science and Deep Learning Assistants........................................................................................
Using the Neural Network Designer Assistant.........................................................................................................
The Neural Network Designer Assistant helps you accelerate experimentation and the creation of neural network models
within three steps. The Neural Network Designer Assistant provides a guided workflow to define your dataset, train a
binary neural network classifier, and evaluate the results. Steps are numbered in the Assistant user interface.

This Assistant works best on a densely connected neural network with a binary target variable. Ensure your data is
clean and well-prepared before using it with the Assistant.
Prerequisites

Make sure you have a Golden Image CPU or GPU development container up and running, and that it contains the
binary_nn_classifier_designer.ipynb notebook.

The Assistant works best when you provide a clean matrix of data as the foundation for building your model. Complete
any data preprocessing using SPL to take full advantage of the Assistant's capabilities. To learn more, see Preparing your
data for machine learning in the Splunk Machine Learning Toolkit User Guide.

Neural Network Designer Assistant architecture

The architecture of this neural network is derived from the classic archetype of a Multilayer Perceptron and its typical
architecture. The following diagram represents that architecture:

The network architecture consists of the following components:

An input layer with different input types
Multiple densely connected hidden layers with rectified linear unit (ReLU) activation functions ,and a dropout layer
for regularization purposes
•
A binary output layer
For each training epoch the weights in the neural network are calculated by backpropagation using an Adam optimizer
and binary cross-entropy. You can define the hidden layer structure, batch size, and other options in the Assistant.

The input layer can be flexibly composed with different input types. See the following table for details.

Input
layer
Description
Numerical
Useful for purely numerical fields. You must ensure that only numeric values are present in your dataset for the selected
numerical fields, otherwise conversion and casting errors will occur during training. You might want to consider standardizing your
numerical fields with MinMaxScaler preprocessing or similar techniques for better convergence of your model.
Categorical
Useful for fields that contain categories. The data in categorical fields is automatically one-hot encoded according to a retrieved
dictionary of all found distinct categories (the vocabulary of the dictionary). If a field is of high cardinality (>100s or >1000s of
dimensions) it might be a better candidate to define it as an embedding layer.
Embedding
Useful for freeform text fields or fields with high cardinality. As the number of categories grows large, it becomes infeasible to train
a neural network using one-hot encodings. We can use an embedding column to overcome this limitation. Instead of representing
the data as a one-hot vector of many dimensions, an embedding column represents that data as a lower-dimensional, dense
vector in which each cell can contain any number, not just 0 or 1.
This approach was inspired by the TensorFlow Tutorial for working with structured data. See,
https://www.tensorflow.org/tutorials/structured_data/feature_columns.

Assistant workflow

The Assistant guided workflow consisted of three major steps: Define your dataset, Train your neural network model, and
Evaluate your model.

The Assistant is populated with the diabetes.csv dataset from MLTK, acting as a working example you can follow. This
working example is limited to showcasing the Assistant workflow. You can modify the Assistant field configurations based

on your own data and use case.

From the working example you can also change and optimize the neural network source code, and tune hyperparameters
in the binary_nn_classifier_designer.ipynb notebook. You can check TensorBoard to investigate the progress of your
model training and how your neural network converges.

From the Neural Network Designer Assistant page, select the Define your dataset icon to begin.

Each stage of the workflow offers dashboard panels where you can further explore the defined dataset and the resulting
model. The bottom of each step of the guided workflow is where you can select the next step of the workflow.

Using the Deep Learning Text Classification Assistant...........................................................................................
The Deep Learning Text Classification Assistant lets you develop deep-learning-based text classification solutions. This
Assistant is available in both English and Japanese.

Text classification is the task to categorize given text into one or several predefined classes. Using deep, bidirectional,
pre-trained language models on text classification has shown superior performance over conventional methods. This
Assistant trains a classifier based on your customized text data and defined target classes.

The Deep Learning Text Classification Assistant uses the Bidirectional Encoder Representations from Transformers
(BERT) model as the base model for text classification tasks. Text can be a sentence or a dialog. The BERT model is a
Transformer-based language model pre-trained on large unlabeled datasets to learn the high-level representations of
natural language sequences, and can be flexibly fine-tuned to various downstream tasks, including text classification. The
Assistant has two linear layers with one non-linear ReLU activation in-between. This non-linear layer is included in the
BERT model to perform text classification tasks.

To learn more about the Bidirectional Encoder Representations from Transformers (BERT) model, see
https://arxiv.org/pdf/1810.04805.pdf

Based on the BERT model, the Deep Learning Text Classification Assistant guides you through the following model
development phases:

A fine-tuning stage to create text classification models with customizable data inputs.
An evaluation stage to validate the performances of the fine-tuned text classification models.
A management stage for the model files.
Prerequisites

In order to successfully use the Deep Learning Text Classification Assistant, the following is required:

You must have a Docker container up and running.
You must have a transformers-GPU or a transformers-CPU development container up and running. This
development container must include the transformers_summarization.ipynb notebook.
•
For improved performance, run the transformer-GPU container on a GPU machine. The minimum GPU machine
specs are as follows:
♦ 1 GPU
♦ 4 vCPU
♦ 16 GB RAM
♦ 200 GB Disk Storage
•
Before you begin

You can configure a macro for the index name storing your Splunk App for Data Science and Deep Learning (DSDL)
Docker logs. This enables you to track progress at the fine-tuning stage. You can still fine-tune a model without the DSDL
Docker logging, but any fine-tuning progress tracking is disabled. To learn how to configure DSDL Docker logging, see
Configure the Splunk App for Data Science and Deep Learning.

Running the fit command for fine-tuning can be time consuming. Depending on the amount of data and the epoch
number, the run time can vary greatly. For a use case with 5000 utterances running for 10 epochs, it might take
approximately 5000 seconds, or 83 minutes to run. Larger data amounts and larger epoch numbers increase these run
times.

On the search head, the fit command terminates if running the command takes longer than the max_fit_time. The fit
process keeps running in the DSDL container, trying to complete building a model. Under these circumstances, the stub
model cannot pass the parameters to the model in the DSDL container. Start with fitting a small amount of data to ensure
you have the stub model properly passing in parameters to the DSDL container. An example of a small amount of data is
fitting with less than 1000 utterances for less than 5 epochs.

You can improve the performance of the fit command in DSDL by increasing the max_fit_time to at least 7200 for the
MLTKContainer algorithm. To learn how to change this value, see Edit default settings in the MLTK app in the Splunk
Machine Learning Toolkit User Guide.

Fine-tuning stage

Use the fine-tuning stage to define your customized data, configure the fine-tuning parameters, and fine-tune the base
model for the text classification task.

The fine-tuning process allows the users to define their customized data, configure the fine-tuning parameters and
fine-tune the base model for the text classification task.

Select Fine-tune your Transformers BERT model panel to start fine-tuning a text classification model. The Assistant
guides you through the next steps.

Prepare training data

You must provide at least 5,000 events in your training data to have satisfying results.
Training data must contain a text field with the field name of text, and one or more class fields that contain 1 or 0
indicating whether the text is categorized to the class or not. Because the fine-tuner takes all the fields other than the text
field as class input fields, make sure you remove all the unnecessary fields before proceeding.

In cases where some classes belong to the same category, rename the class fields with prefixes such as cat1_, cat2_,
and catn_* depending on the category that class belongs to.

The Assistant displays the following example SPL in the data input field. You can explore the Assistant using the provided
example prior to working with your own data:

| inputlookup classification_en.csv

| fields - TITLE ID

| rename * as cat1_*, cat1_ABSTRACT as text

| head 10

When working with your own training data, input it to the Assistant as a lookup table.

Your training data must have the exact names of text for the text field to ensure successful fine-tuning.
When ready, click the search icon on the right side of the search bar. The search results are generated and the
Fine-Tuning Settings panel appears at the bottom of the page, leading you to the next step in the fine-tuning process.

Set fine-tuning settings

In this step select the language, base model, and training parameters for your model:

Select the language from the drop-down menu. The default language is English (en).
Select the base model for fine-tuning from the drop-down menu. The drop-down menu includes the
bert_classification_en base model and other models you have created. The fine-tuning is performed on the
selected base model.
2.
Set your training parameters. See the following table for parameter descriptions:
Parameter name Type Description
Default
value
Target model name string The name of the output model after fine-tuning. This cannot be the same name to thebase model. tbd
Batch size integer The batch size of training data during fine-tuning. Reduce the batch size when memorysize is limited. 4
Max epoch integer The maximum training epochs for the fine-tuning. 10
3.
Parameter name Type Description
Default
value
Select Review Fine-Tuning SPL. Use the resulting review to examine your settings before you run the
fine-tuning.
4.
Run fine-tuning SPL

You can assess the fine-tuning of the training data by selecting a score type from the Score dropdown menu. The score
type default is Confusion Matrix. Accuracy, Precision and Recall are also supported. Scoring results are displayed at the
bottom of the page. For all types of scores, the closer the values are to 1 indicate better performance.

You can also choose that a category prefix be displayed in the results. The default category prefix is cat1.

Begin the fine-tuning process by selecting Run Fine-Tuning SPL. A new panel appears to display the estimated
fine-tuning process duration.

If you have configured DSDL Docker logs, then the logging information appears with the training process duration and
includes the following values:

Value Description
done_epoch Number of finished training epochs.
elapsed_time Duration of the past epoch.
training_loss Value of training loss. The reduction of training loss indicates successful fine-tuning progress.
valid_loss Value of validation loss. Validation loss should be reduced along with the training loss. Overgrowing of validation lossindicates overfitting of the training.
When the fine-tuning is finished, a Fine-Tuning Results panel appears at the bottom of the page. This panel displays the
following fields:

Field Description
text_snip A shortened version of the input text.
cat* Ground truth of the classification target class.
predicted_cat* The predicted class of the text.
Once you are happy with the fine-tuning outcome, select Done. Once done you can copy the fine-tuning SPL to use it in
your scheduled search to periodically run the fine-tuning process to fit your business needs.

Evaluation stage

Use the evaluation stage to score the model performance on customized input data. Select the Evaluate your model
panel to start evaluating a text classification model. The Assistant guides you through the next steps.

Prepare test data

Preparation of the test data is similar to the training data preparation in the fine-tuning phase. The test data needs to
contain a text field with field name text and one or more class fields that contain a 1 or 0 indicating whether the text is
categorized to the class or not.

Choose the Evaluation settings

Select the language and the model you want to evaluate from the dropdown menus at the bottom of the page. Select
Review Evaluation SPL to move on to the next step.

Run the Evaluation SPL

Begin by selecting a score type from the Score dropdown menu. The score type default is Confusion Matrix. Accuracy,
Precision and Recall are also supported. Scoring results are displayed at the bottom of the page. For all types of scores,
the closer the values are to 1 indicate better performance.

You can also choose that a category prefix be displayed in the results. The default category prefix is cat1.

Select Run Evaluation SPL to start the model evaluation process. A new panel appears displaying the estimated
evaluation duration. Once the evaluation is finished you can view the Evaluation Results panel. The panel displays the
following fields:

Field name Field content
text_snip A shortened version of the input text.
cat* Ground truth of the classification target class.
predicted_cat* The predicted class of the text.
Select Done to complete the Evaluation stage. Once done you can copy the evaluation SPL to use it in a scheduled
search to run the evaluation process to fit your business needs.

Management stage

Use the management stage to retrieve information on your existing model files in the containers, and to remove any
unused model files.

Transformers models can be large. Monitor the available storage space in your fine-tuning progress panel and free up
space by removing unnecessary models.
Use the Manage your models panel to access the management interface of the text classification models. In the model
management interface, the information of all existing classification models is displayed in the order of language, class,
model, size, and container. The class information indicates whether it is a base model or an inheritor (fine-tuned model).

You can remove any inheritor model by selecting Delete.

Use the Delete action with caution as model deletion cannot be undone.
Using the Deep Learning Text Summarization Assistant......................................................................................
The Deep Learning Text Summarization Assistant lets you develop deep-learning-based text summarization solutions.
This Assistant is available in both English and Japanese.

Text summarization produces a shorter version of a text document while preserving its important information. With the
development of deep neural networks, transformer-based models are capable of generating abstractive summaries that
are informative, close to natural language, and that achieve state-of-the-art performance.

The base model provided by the Deep Learning Text Summarization Assistant is equipped with basic text summarization
capabilities. The Assistant leverages the Text-To-Text Transfer Transformers (T5) model as the base model for text
summarization tasks. The T5 model is a transformer-based language model pre-trained on large unlabeled datasets to
learn the high-level representations of natural language sequences. The T5 model can be fine-tuned to various
downstream tasks, including text summarization.

To learn more about the Text-to-Text Transfer Transformers (T5) model, see
https://ai.googleblog.com/2020/02/exploring-transfer-learning-with-t5.html.

Based on the text-to-text T5 model, the Deep Learning Text Summarization Assistant guides you through the following
model development phases:

A fine-tuning stage to create text summarization models with customizable data inputs.
An evaluation stage to validate the performances of the fine-tuned text summarization models.
A management stage to retrieve information on existing model files and remove unused model files.
Prerequisites

In order to successfully use the Deep Learning Text Summarization Assistant, the following is required:

You must have a Docker container up and running.
You must have a transformers-GPU or a transformers-CPU development container up and running. This
development container must include the transformers_summarization.ipynb notebook.
•
For improved performance, run the transformer-GPU container on a GPU machine. The minimum GPU machine
specs are as follows:
♦ 1 GPU
♦ 4 vCPU
♦ 16 GB RAM
♦ 200 GB Disk Storage
•
Before you begin

You can configure a macro for the index name storing your Splunk App for Data Science and Deep Learning (DSDL)
Docker logs. This enables you to track progress at the fine-tuning stage. You can still fine-tune a model without the DSDL
Docker logging, but any fine-tuning progress tracking is disabled. To learn how to configure DSDL Docker logging, see
Configure the Splunk App for Data Science and Deep Learning.

Running the fit command for fine-tuning can be time consuming. Depending on the amount of data and the epoch
number, the run time can vary greatly. For a use case with 5000 utterances running for 10 epochs, it might take
approximately 5000 seconds, or 83 minutes to run. Larger data amounts and larger epoch numbers increase these run
times.

On the search head, the fit command terminates if running the command takes longer than the max_fit_time. The fit
process keeps running in the DSDL container, trying to complete building a model. Under these circumstances, the stub
model cannot pass the parameters to the model in the DSDL container. Start with fitting a small amount of data to ensure
you have the stub model properly passing in parameters to the DSDL container. An example of a small amount of data is
fitting with less than 1000 utterances for less than 5 epochs.

You can improve the performance of the fit command in DSDL by increasing the max_fit_time to at least 7200 for the
MLTKContainer algorithm. To learn how to change this value, see Edit default settings in the MLTK app in the Splunk
Machine Learning Toolkit User Guide.

Fine-tuning stage

Use the fine-tuning stage to define your customized data, configure the fine-tuning parameters, and fine-tune the base
model for the text summarization task.

Select Fine-tune your Transformers T5 model to start fine-tuning a text summarization model. The Assistant guides you
through the next steps.

Prepare training data

You must provide at least 5,000 events in your training data to have satisfying results.
Prepare your training data so that text and summary fields are paired:

The text field is for the text data from which you want to extract summaries.
The summary field is for the summary of the corresponding text as the ground-truth of the summarization task.
The Assistant displays the following example SPL in the data input field. You can explore the Assistant using the provided
example prior to working with your own data:

| inputlookup customer_support_en | head 3

When working with your own training data, input it to the Assistant as a lookup table.

Your training data must have the exact names of text for the text field and summary for the summary field to ensure
successful fine-tuning.
When ready, click the search icon on the right side of the search bar. The search results are generated and the
Fine-Tuning Settings panel appears at the bottom of the page, leading you to the next step in the fine-tuning process.

Set fine-tuning settings

In this step select the language, base model, and training parameters for your model:

Select the language from the drop-down menu. The default language is English (en).
Select the base model for fine-tuning from the drop-down menu. The drop-down menu includes the
t5_summarization_en base model and other models you have created. The fine-tuning is performed on the
selected base model.
2.
Set your training parameters. See the following table for parameter descriptions:
Parameter
name
Type Description Default value
Target model
name string
The name of the output model after fine-tuning. Add to or edit this name to suit
your needs and naming conventions. This cannot be the same name to the
base model.
The name of the
selected base model
plus an underscore.
Batch size integer The batch size of training data during fine-tuning. Reduce the batch size whenmemory size is limited. 4
Max epoch integer The maximum training epochs for the fine-tuning. 10
Beam size integer Configuration for beam search during model inference. A higher value canindicate better performance but will reduce the computational speed. 1
Select Review Fine-Tuning SPL. Use the resulting review to examine your settings before you run the
fine-tuning.
4.
Run fine-tuning SPL

Begin the fine-tuning process by selecting Run Fine-Tuning SPL. A new panel appears to display the estimated
fine-tuning process duration.

If you have configured DSDL Docker logs, then the logging information appears with the training process duration and
includes the following values:

Value Description
done_epoch Number of epochs finished training.
elapsed_time Duration of the past epoch.
training_loss Value of training loss. A reduction of training loss indicates successful fine-tuning progress.
valid_loss Value of validation loss. Validation loss can be reduced along with the training loss. Overgrowing of validation loss indicatesoverfitting of the training.
When the fine-tuning is finished, a Fine-Tuning Results panel appears at the bottom of the page. This panel displays the
following fields:

Field Description
summary The ground truth.
extracted_summary Generated summarization result.
rouge_score The evaluated score of the results. Field value indicates how much where 1.0 is the best and 0 is the worst. extracted_summary reproduces summary,
Once you are happy with the fine-tuning outcome, select Done. Once done you can copy the fine-tuning SPL to use it in
your scheduled search to periodically run the fine-tuning process to fit your business needs.

Evaluation stage

Use the evaluation stage to score the model performance on customized input data. Select the Evaluate your model
panel to start evaluating a text summarization model. The Assistant guides you through the next steps.

Prepare test data

Preparation of the test data is similar to the training data preparation in the fine-tuning phase. Pair text and summary data
with exact field names and input to the search bar.

Choose Evaluation settings

Select the language and the model you want to evaluate from the drop-down menus at the bottom of the page. Select
Review Evaluation SPL to move on to the next step.

Run the Evaluation SPL

Select Run Evaluation SPL to start the model evaluation process. A new panel appears displaying the estimated
evaluation duration.

If you have configured the DSDL Docker logs, the logging information appears along with the training progress information
including the following fields:

Field name Field content
max_apply Number of input utterances for summarization evaluation.
done_apply Number of finished utterances.
elapsed_time Duration of each utterance.
Once the evaluation is finished you can view the Evaluation Results panel. The panel displays the following fields:

Field name Field content
summary The ground-truth.
extracted_summary Generated summarization result.
rouge_score The evaluated score of the results. This field indicates how much extracted_summary reproduces summary, where 1.0is the best and 0 is the worst. The average rouge_score is also displayed.
Select Done to complete the Evaluation stage. Once done you can copy the evaluation SPL to use it in a scheduled
search to run the evaluation process to fit your business needs.

Management stage

Use the management stage to retrieve information on your existing model files in the containers, and to remove any
unused model files.

Transformers models can be large. Monitor the available storage space in your fine-tuning progress panel and free up
space by removing unnecessary models.
Use the Manage your models panel to access the management interface of the text summarization models. In the model
management interface, the information of all existing summarization models is displayed in the order of language, class,
model, size, and container. The class information indicates whether it is a base model or an inheritor (fine-tuned model).

You can remove any inheritor model by selecting the Delete.

Use the Delete action with caution as model deletion cannot be undone.

LLM-RAG Assistants........................................................................................................................................................
About LLM-RAG....................................................................................................................................................
As technologies around large language models (LLMs) evolve, several key challenges have emerged:

How to use LLM services securely.
How to generate beneficial and accurate answers for your organization.
Current LLM services are commonly provided as Software-as-a-Service (SaaS) products, with customer data and
searches sent through public clouds. This practice poses significant obstacles for many organizations aiming to use LLMs
securely.

Additionally, LLMs generate responses based on their training data, making it challenging to produce answers that are
relevant to customers' specific use cases without the latest information or access to internal knowledge.

To address these challenges, version 5.2.1 and higher includes both cloud-based and on-premises LLM options. With
cloud-based solutions, organizations can leverage the scalability and ease of deployment offered by the cloud. For those
requiring full control over their data, on-premises LLMs allow secure hosting within your environment. To further enhance
accuracy and relevance, the use of retrieval-augmented generation (RAG) enables integration of up-to-date and internal
knowledge into LLM-generated responses.

RAG uses customizable knowledge bases as additional contextual information to enhance the LLMs' responses.
Typically, materials containing the additional knowledge, such as internal documents and system log messages, are
vectorized and stored in a vector database (vectorDB). When a search is run, related knowledge content is identified
through vector similarity search and added to the context of the LLM prompt to assist the generation process.

Only Docker deployments are supported for running LLM-RAG on the Splunk App for Data Science and Deep Learning
(DSDL).
LLM-RAG features

LLM-RAG provides a compute command , which accelerates DSDL searches, as well as dashboards to extend the Splunk
App for Data Science and Deep Learning (DSDL). There are 3 key components to the LLM-RAG features:

A DSDL container that includes the Python scripts and support packages.
An LLM module that runs LLMs locally.
A vector database (DB) to store vectorized knowledge bases.
In DSDL you can find the dashboards under the Assistants tab. The dashboards are grouped by the following operations:

Encoding data to a vector database.
Searching LLM with vector data.
LLM-RAG architecture

The following image shows the architecture of an LLM-RAG system:

The LLM-RAG system includes an LLM module using Ollama or Cloud-based LLM services, a DSDL container, and a
vectorDB module using Milvus. The DSDL container is the framework that orchestrates the LLM and vectorDB modules
for RAG operations.

To learn more about Ollama and Milvus products, see https://ollama.com/ and https://milvus.io/.

LLM-RAG use cases

The LLM-RAG functionalities with assistive guidance handle the following use cases:

Use case Description
Standalone LLM Use Standalone LLM for direct use of the LLM for Q&A inference or chat.
Standalone VectorDB Use Standalone VectorDB when you want to encode machine data and conduct similarity searches.
Document-based
LLM-RAG
Use Document-based LLM-RAG when you want to encode arbitrary documents and use them as additional contexts
when prompting LLM models.. Model generation is based on an internal knowledge database.
Function Calling
LLM-RAG
Use Function Calling LLM-RAG for the LLM to execute customizable function tools to obtain contextual information for
response generation.
By default, a set of Splunk platform searching tools are provided, including Search Splunk, List
indexes, Get index info, List saved searches, List users, Get indexes and sourcetypes, and Splunk
health check.
To use these tools, users must complete the Splunk Access Settings panel on the DSDL Setup
page.
Learn more

See the following for additional information:

For more information on the compute command, see About the compute command.
For more information on LLM-RAG features, see Encode data into a vector database, and Query LLM with vector
data.
•
For more information on LLM-RAG use cases, see LLM-RAG use cases.
Set up LLM-RAG...................................................................................................................................................
Complete the following steps to set-up and begin using large language model retrieval-augmented generation
(LLM-RAG).

Only Docker deployments are supported for running LLM-RAG on the Splunk App for Data Science and Deep Learning
(DSDL).
Prerequisites

If you have not done so already, install or upgrade to DSDL version 5.2.1 and its dependencies. See Install or upgrade the
Splunk App for Data Science and Deep Learning.

After installation, go to the setup page and configure Docker. See Configure the Splunk App for Data Science and Deep
Learning.

Have Docker installed. See https://docs.docker.com/engine/install

Have Docker Compose installed. See https://docs.docker.com/compose/install

Make sure that the Splunk search head can access the Docker host on port 5000 for API communication, and port
2375 for the Docker agent.
Set up container environment

Follow these steps to configure a Docker host with the required container images. If you use an air-gapped environment,
see Set-up LLM-RAG in an air-gapped environment.

Run the following command to pull the LLM-RAG image to your Docker host:
docker pull splunk/mltk-container-ubi-llm-rag:5.2.1
1.
Get the Docker Compose files from the Github public repository as follows:
wget
https://raw.githubusercontent.com/splunk/splunk-mltk-container-docker/v5.2/beta_content/passive_deployment
_prototypes/prototype_ollama_example/compose_files/milvus-docker-compose.yml
wget
https://raw.githubusercontent.com/splunk/splunk-mltk-container-docker/v5.2/beta_content/passive_deployment
_prototypes/prototype_ollama_example/compose_files/ollama-docker-compose.yml
wget
https://raw.githubusercontent.com/splunk/splunk-mltk-container-docker/v5.2/beta_content/passive_deployment
_prototypes/prototype_ollama_example/compose_files/ollama-docker-compose-gpu.yml
2.
Run Docker Compose command

Follow these steps to run the Docker Compose command:

Install Ollama Module.
For CPU machines, run this command:
docker compose -f ollama-docker-compose.yml up --detach
For GPU machines with the NVIDIA driver installed, run this command:
docker compose -f ollama-docker-compose-gpu.yml up --detach
1.
Install Milvus Module:
docker compose -f milvus-docker-compose.yml up --detach
2.
As a final check, make sure the Ollama image has been spun up and is under the Docker network named
dsenv-network:
docker ps
docker inspect <Container ID of Ollama>
3.
Pull LLM to your local machine by running the following command. Replace MODEL_NAME with the specific model
name listed in the Ollama library at https://ollama.com/library:
curl http://localhost:11434/api/pull -d '{ "name": "MODEL_NAME"}'
You can also pull models in at a later stage using the Splunk DSDL command or dashboard.
4.
Configure DSDL for LLM-RAG

Complete these steps to configure DSDL for LLM-RAG:

Navigate to Configuration , then Setup , and then select Setup.
Input dsenv-network in the Docker network box, as shown in the following image. This step ensures
communication between your DSDL container and the other containers created by Docker compose.

If you want to use the default Function Calling tools that search the Splunk platform, configure the Splunk
Access Settings :
3.
Navigate to Configuration and Setup and select Setup LLM-RAG (optional). Input the configurations for your
LLM, Embedding, VectorDB, and GraphDB.
For more information on this additional setup page, see Set up additional LLM-RAG configurations.
4.
Navigate to Configuration , then Containers and start the Red Hat LLM RAG CPU (5.2.1) container from the
Development Container panel.
5.
Set up additional LLM-RAG configurations............................................................................................................
DSDL version 5.2.1 introduces an optional setup page that allows you to configure additional LLM-RAG features. You can
tailor your configurations for Large Language Models (LLM), embedding models, vector databases (VectorDB), and graph
databases (GraphDB) modules in the setup page.

Version 5.2.1 includes cloud-based options for more customizations. You can select from the following options for each
module:

Feature Options
Large Language Models
Ollama for local LLM
Azure OpenAI
OpenAI
Bedrock
Gemini
Embedding models
Huggingface for local embedding
Ollama for local embedding
Azure OpenAI
OpenAI
Bedrock
Gemini
Vector DB
Milvus
Pinecone
AlloyDB
Note: AlloyDB users must create a table on AlloyDB prior to using the table as a collection.
Graph DB • Neo4j
DGraph
You can configure multiple options for the same module, and switch between them, by using the fit command and by
specifying the option. For example, llm_service=bedrock.
The Setup LLM-RAG (optional) page is where you can input configurations for each service. When you select Save ,
your customizations are saved into the llm.conf configuration file. Any password-related items are encrypted and kept in
secret storage.

These configurations are integrated into the container environment upon startup. To apply changes restart the active
LLM-RAG container.
The following image shows the Setup LLM-RAG (optional) page before any settings are configured:

Configure the settings panel

On this setup page, only 1 configuration is allowed for each option. However, for local LLM models on Ollama and local
embedding models on Huggingface, you can override the default settings by specifying the model name in the fit
command. For example model_name=llama3.3.

By default, Ollama is enabled for LLM, Huggingface is enabled for Embedding and Milvus is enabled for VectorDB. These
default configurations follow the setup in DSDL version 5.2.0, where the LLM and VectorDB modules share the same
Docker network with the LLM-RAG container.

To configure an option on Setup LLM-RAG (optional) page, follow these steps:

The model name you set on this setup page serves as the default model when no model name is specified in the fit
command.
Begin by selecting an option name within the panel of the module you want. For example, select Bedrock or
LLM.
1.
Select Yes for Enable Service.
Fill out the required fields for the chosen option.
You can modify the endpoint URLs for Ollama and Milvus to fit your specific environment.
For embedding models, you must specify the output dimensionality in the Output Dimensions field.
4.
Configure LLM or embedding models for DSDL on Splunk Enterprise

If you are using DSDL on Splunk Enterprise and want to configure multiple LLM or embedding models under the same
option, such as Azure OpenAI, you have an alternative method available. Instead of using the standard setup
configuration, follow these steps:

Using this method means that password-related items in the llm_config.json file are not encrypted. You must
acknowledge the associated security risks when opting for this approach.
Create an llm_config.json configuration file based on the example template at
https://github.com/huaibo-zhao-splunk/mltk-container-docker-521/blob/main/llm_config.json. In the example, 2
LLM models are configured under Azure OpenAI as a list. You can use this approach to configure multiple items
for the service of your choice.
1.
Place the llm_config.json file in the $SPLUNK_HOME/etc/apps/mltk-container/local directory.
Open the $SPLUNK_HOME/etc/apps/mltk-container/bin/start_handler.py file. Uncomment lines 59 through 65
and comment lines 66 through 71. This modification ensures that the llm_config.json configuration file you created
is directly passed into the container, bypassing the default Splunk configuration files.
3.
About the compute command................................................................................................................................
The Splunk App for Data Science and Deep Learning (DSDL) version 5.2.0 introduces the compute command. This
command provides an alternative to the fit command from the Splunk Machine Learning Toolkit (MLTK), and accelerates
the DSDL search.

The compute command is a streaming command that uses Python functions in the DSDL container without creating a
model.

When you use the compute in a pipeline, the search results and parameters specified in the key:value format are sent to
the FastAPI endpoint on the container side. During the data flow, the search results are kept in JSON format without any
conversion. Similarly, the computation results are generated and received in JSON format when using compute.

When using the compute command, only the compute() module of the Python code is called, limiting the workflow to the
necessary parts and increasing search concurrency. When tested on the same computations in DSDL, the compute
command is more efficient with a shorter runtime than the fit command.

The compute command is unlike the fit command, which converts search results into a Pandas DataFrame. The fit
command follows a specific workflow in which a model file must be created. This requirement limits search concurrency
when using fit for Python functions that do not need a model created.

LLM-RAG use cases..............................................................................................................................................
The large language model retrieval-augmented generation (LLM-RAG) functionalities with assistive guidance dashboards
handles the following use cases:

Standalone LLM
Standalone VectorDB
Document-based LLM-RAG
Function Calling LLM-RAG
Standalone LLM

Use Standalone LLM for direct use of the LLM for Q&A inference or chat. For additional details, see Using Standalone
LLM.

As shown in the following image, when using Standalone LLM, you initialize a search with a prompt as well as text data
searched from the Splunk platform. The prompt is sent to the DSDL container, where the LLM module's API is called to
generate responses. The responses are then returned to the Splunk platform search as search results.

Standalone VectorDB

Use Standalone VectorBD when you want to encode machine data and conduct similarity search. For additional details,
see Using Standalone VectorDB.

As shown in the following image, when using Standalone VectorDB you initially encode Splunk log data into a collection
within the vector database. When an unknown log data occurs, you can conduct a vector search against the pre-encoded
data to find similar recorded log data.

Document-based LLM-RAG

Use Document-based LLM-RAG when you want to encode arbitrary documents and use them as additional contexts
when prompting LLM models. Document-based LLM-RAG provides results based on an internal knowledge database. For
additional details, see Using Document-based LLM-RAG.

Document-based LLM-RAG has 2 steps:

Document encoding
Document pieces appended
In the first step you encode any documents stored in a directory of the Docker host into a vectorDB collection.

The following image shows the document encoding step:

When you initialize a search that requires the knowledge from the documents, the DSDL container conducts a vector
search on the encoded document collection to find related pieces of those documents.

In the second step the related pieces of documents are appended to the original search as additional contexts and the
search is sent to the LLM. The LLM responses are then returned to the Splunk platform search as search results.

The following image shows the DSDL container vector search of the encoded documents:

Function Calling LLM-RAG

Use Function Calling LLM-RAG for the LLM to run customizable function tools to obtain contextual information for
response generation. The Function Calling LLM-RAG provides default tools for searching Splunk platform data and
service status. For additional details, see Using Function Calling LLM-RAG.

Similar to document-based LLM-RAG, function calling LLM-RAG also obtains additional information prior to generating the
final response. The difference is that with function calling a set of function tools are made accessible to the LLM.

When additional context is needed, such as how many error logs are in a Splunk platform instance, the LLM automatically
runs the functions to obtain the information and uses it to generate responses.

The following image shows Function Calling LLM-RAG architecture:

Use Standalone LLM
You can use Standalone LLM through a set of dashboards. The following processes are covered:

Download LLM models
Inference with LLM
All the dashboards are powered by the fit command. The dashboards showcase Standalone LLM functionalities. You
are not limited to the options provided on the dashboards. You can tune the parameters on each dashboard, or embed a
scheduled search that runs automatically.

Download LLM models

If you want to use local LLMs from Ollama. Complete the following steps:"

In the Splunk App for Data Science and Deep Learning (DSDL), navigate to Assistants , then LLM-RAG , then
Querying LLM , and select Local LLM and Embedding Management.
1.
On the settings panel, select PULL from the Task drop-down menu and Ollama from Service Type, as shown in
the following image:
2.
In the Model Name field, enter the name of the LLM you want to download. For model name references, see the
Ollama library page at https://ollama.com/library.
3.
Select Submit to start downloading. You see an on-screen confirmation after the download completes.
Confirm your download by selecting Refresh Page. Make sure that the LLM model name shows on the Existing
LLM models panel.
5.
Inference with LLM

Complete the following steps:

In DSDL, navigate to Assistants , then LLM-RAG , then Querying LLM , and select Standalone LLM.
A search bar is provided in the dashboard to conduct inference and natural language processing (NLP) tasks on
the text data stored in Splunk. Use the rename command in combination with as text to search the text data
stored in the Splunk platform.
If you do not want to use text data, leave the default search command empty or tune the prompt with the
search command.
2.
After inferencing completes, a panel for inference settings is available. On this panel you can choose LLM models
and input your search.
3.
Examples

The following example uses text data and a Standalone LLM search:

The following example uses a one-shot prompt:

Use Standalone VectorDB.....................................................................................................................................
Use Standalone VectorDB to run a vector search through a set of dashboards. The following processes are covered:

Download embedder models
Encode Splunk data into VectorDB
Conduct Vector search
All the dashboards are powered by the fit command. The dashboards showcase Standalone VectorDB functionalities.
You are not limited to the options provided on the dashboards. You can tune the parameters on each dashboard, or
embed a scheduled search that runs automatically.

Configure embedding models

Complete the following steps:

Make sure that you have configured the embedding service on the Setup LLM-RAG (optional) page prior to
spinning up the container. If you haven't, finish the configuration and restart the container.
1.
When configuring the embedding service, specify the output dimensionality of the model in the Output
Dimensions field.
If you have downloaded local Huggingface embedding models, add the prefix /srv/app/model/ to the
Embedding Model Name of your choice.
2.
To download a Huggingface embedding model prior to the configuration, navigate to Assistants , then LLM-RAG ,
then Querying LLM , and then select Local LLM and Embedding Management.
3.
On the page, select PULL from the Task drop-down menu and Huggingface from Service Type and input the
model name.
4.
Select Submit to download the embedding model locally.
Encode data into a VectorDB

Complete the following steps to encode Splunk platform data into a VectorDB:

In DSDL, navigate to Assistants , then LLM-RAG , then Encoding data to Vector Database , and then select
Encode data from Splunk.
1.
On the search bar of the dashboard, search for the data that you want to encode. You have 2 options:
♦ You can search for data stored in Splunk platform indexes and create a table.
♦ You can use the inputlookup command to load a lookup table.
2.
In Target Field Name enter the field name that contains data you wish to encode. For example, enter _raw for
raw log events.
The other fields in the search result are automatically added to the collection as metadata fields stored in plain
text.
3.
Create a unique name for a new Collection Name. If you want to add data to an existing collection, use the
existing name.
4.
For Vector Service and Embedding Service , choose the services you have enabled in the Setup LLM-RAG
(optional) page.
5.
Select Encode to start encoding. A list of messages is shown in the associated panel after the encoding finishes.
Select Return to Menu and then select Manage and Explore your Vector Database. You see the collection
listed on the main panel.
It might take a few minutes for the complete number of rows to display.
On this page you can also delete any collection.
7.
Conduct vector search

Complete the following steps:

In DSDL, navigate to Assistants , then LLM-RAG , then Encoding data to Vector Database , and then select
Conduct Vector Search on Splunk data.
1.
In Collection Name , select an existing collection on which you want to search. Select the same vector service
and embedding service that you used for encoding.
2.
Select a number for the Number of Results to control the top N results.
Select Submit to proceed.
On the search bar, search for data to conduct vector search on. The result should be a table containing only the
field you want to search on.
5.
Select any data to conduct vector search against it. The top N results from the collection are listed in the panel,
along with the metadata saved in the collection, as shown in the following image:
6.
Use Document-based LLM-RAG...........................................................................................................................
Use Document-based large language model retrieval-augmented generation (LLM-RAG) through a set of dashboards.

The following processes are covered:

Configure LLM and Embedding services
Encode document to VectorDB
Use LLM-RAG
All the dashboards are powered by the fit command. The dashboards showcase Document-based LLM-RAG
functionalities. You are not limited to the options provided on the dashboards. You can tune the parameters on each
dashboard, or embed a scheduled search that runs automatically.

Configure LLM and Embedding services

Make sure that you have enabled the LLM services and Embedding services of your choice on the Setup LLM-RAG
(optional) page prior to starting the container. If you have not, finish the configuration and restart the container. See Set
up LLM-RAG additional configurations.

For downloading local LLMs or embedding models, refer to the relevant sections in the Use Standalone LLM and Use
Standalone VectorDB documents.

Encode documents into VectorDB

Complete the following steps:

Gather the documents you want to encode into a single collection. The supported document extensions are TXT,
PDF, DOCX, CSV, XML, and IPYNB.
1.
Upload the documents through JupyterLab or add the documents to the Docker volume:
Upload option Description
JupyterLab Create a folder at any location in JupyterLab, for example notebooks/data/MyData, and upload all the filesinto the folder.
Add the documents to
the Docker volume
Your files must exist on your Docker host. The Docker volume must be at
/var/lib/docker/volumes/mltk-container-data/_data.
Create a folder under this example path:
/var/lib/docker/volumes/mltk-container-data/_data/notebooks/data/MyData
Copy the documents into this path.
2.
In DSDL, navigate to Assistants , then LLM-RAG , then Encoding data into Vector Database , and then select
Encode documents.
3.
On the dashboard, input the data path with prefix "/srv". For example, if you have a folder on JupyterLab
notebooks/data/Buttercup, your input would be /srv/notebooks/data/Buttercup.
4.
Create a unique name for a new Collection Name. If you want to add more data to an existing collection, use the
existing name.
5.
Choose the configured VectorDB service and Embedding service.7.
Select Encode to start encoding. A list of messages is shown in the associated panel after the encoding finishes.
Select Return to Menu and then select Manage and Explore your Vector Database. You will see the collection
listed on the main panel.
It might take a few minutes for the complete number of rows to display.
On this page you can also delete any collection.
9.
Use LLM-RAG

Complete the following steps:

In DSDL, navigate to Assistants , then LLM-RAG , then Querying LLM , and then select RAG-based LLM.
In Collection Name , select an existing collection on which you would like to search. Select the same VectorDB
service and Embedding service that you used for encoding.
2.
Select the LLM service of your choice.
Select Next to submit the settings.
An Input your Query field becomes available. Enter your search and select Query as shown in the following
image:
5.
Use Function Calling LLM-RAG.............................................................................................................................
You can use Function Calling-based LLM through a set of dashboards. The following processes are covered:

Configure LLM service
Implement Function tool
Use Function Calling LLM-RAG
All the dashboards are powered by the fit command. The dashboards showcase Function Calling LLM-RAG
functionalities. You are not limited to the options provided on the dashboards. You can tune the parameters on each
dashboard, or embed a scheduled search that runs automatically.

The results you see when using Function Calling LLM-RAG depend on your customizations. The examples provided here
do not necessarily reflect the custom tools you might use in your own use cases.

Configure LLM service

Make sure that you have enabled the LLM service(s) of your choice on the Setup LLM-RAG (optional) page prior to
starting the container. If you have not, finish the configuration and restart the container.

For downloading local LLMs, refer to the relevant sections in Use Standalone LLM.

Implement the Function tool

Complete the following steps:

Select the JupyterLab link listed on the container management page. The default is https://:8888.
Navigate to notebooks and open the notebook named llm_rag_function_calling.ipynb.
In the cell Stage 0 - import libraries you can find the following pre-defined Python functions:
♦ Search splunk
♦ List indexes
♦ Get index info
♦ List saved searches
♦ List users
♦ Get indexes and sourcetypes
♦ Splunk health check
These functions are wrapped as Function Tools at the bottom of the cell as follows:
search_splunk_tool = FunctionTool.from_defaults(fn=search_splunk)
list_indexes_tool = FunctionTool.from_defaults(fn=list_indexes)
get_index_info_tool = FunctionTool.from_defaults(fn=get_index_info)
list_saved_searches_tool = FunctionTool.from_defaults(fn=list_saved_searches)
list_users_tool = FunctionTool.from_defaults(fn=list_users)
get_indexes_and_sourcetypes_tool = FunctionTool.from_defaults(fn=get_indexes_and_sourcetypes)
health_check_tool = FunctionTool.from_defaults(fn=health_check)
3.
You can add comments to each function explaining the format and meaning of each input variable. This allows
the LLM to set each parameter when it calls the function. To give the LLM access to a certain function tool use the
cell Stage 4 - apply the model.
4.
In the cell, a list called tool_list is created and the function tool objects initialized in Stage 0 are appended to the
list. By appending the function tool to the list, the LLM can access to the function tool and runs the tool when
necessary to gain additional contextual information.
5.
Implement your own Function Tool

You can register your own function tool by completing the following steps:

Write a simple Python function in the cell Stage 0 - import libraries : def MyFunction(a: int, b: int):
return a + b
1.
Wrap the Python function as a Function Tool in the cell Stage 0 - import libraries : MyFunctionTool =
FunctionTool.from_defaults(fn=MyFunction)
2.
Register the function to the tool list in the cell Stage 4 - apply the model : tool_list = [..., MyFunctionTool,
...]
worker = ReActAgentWorker.from_tools(tool_list, llm=llm)
3.
The input parameters of the fit command are Booleans that indicate if you are using Function 1 (func=1) or Function 2
(func2=0). If you implement your own function tool but want to keep the default fit command syntax, you must substitute
the default tools with your own function tools in the positions of func1 and func2 when you wrap the functions in the cells.

Alternatively, you can define new parameters of the fit command or hardcode the tool list.

Use Function Calling LLM-RAG

Complete the following steps:

In DSDL, navigate to Assistants , then LLM-RAG , then Querying LLM , and then select LLM with Function
Calling.
1.
On the LLM-RAG settings panel, select the LLM service you want to use.
Select Next to submit the settings.
An Input your query field becomes available. Input your query and select Query. The final output for the LLM
and the result for each function tool appears.
4.
Encode data into a vector database......................................................................................................................
To encode data into a vector database, complete these tasks:

Encode documents: Uses vectorizing data and stores the vectors in Milvus collections. You can then use
documents in later stages of the LLM-RAG process.
•
Encode data from the Splunk platform: Uses vectorizing data and stores the vectors in Milvus collections. You can
use data in later stages of the LLM-RAG process.
•
Conduct vector search: Conduct vector similarity search on Splunk log data.
Manage and explore your vector database: List, pull, and delete your vector database.
Encode documents

Go to the Encode documents page:

In the Splunk App for Data Science and Deep Learning (DSDL), go to Assistants.
Select LLM-RAG , then Encoding Data to Vector Database , and then Encode documents.
Parameters

The Encode documents page has the following parameters:

Parameter Description
data_path The directory on Docker volume where you store the raw document data. Sub-directories are read automatically andCSV, PDF, TXT, DOCX, XML, and IPYNB files are encoded.
collection_name A unique name of the collection to store the vectors in. The name must start with a letter or a number and contain nospaces. If you are adding data to an existing collection, make sure to use the same embedder model.
vectordb_service Type of VectorDB service. Choose from milvus, pinecone, and alloydb.
embedder_service Type of embedding service. Choose from gemini. huggingface, ollama, azure_openai, openai, bedrock, and
embedder_name Name of embedding model. Optional if configured on the Setup LLM-RAG page.
embedder_dimension Output dimensionality of the model. Optional if configured on the Setup LLM-RAG page.
Run the fit or compute command

Use the following syntax to run the fit command or the compute command:

Run the fit command:
| makeresults
| fit MLTKContainer algo=llm_rag_document_encoder data_path="/srv/notebooks/data/Buttercup"
vectordb_service=milvus embedder_service=azure_openai collection_name="document_collection_example"
_time into app:llm_rag_document_encoder as Encoding
•
Run the compute command:
| makeresults
| compute algo:llm_rag_document_encoder data_path:"/srv/notebooks/data/Buttercup/"
vectordb_service:"milvus" embedder_service:"azure_openai"
collection_name:"document_collection_example" _time
•
Dashboard view

The following image shows the dashboard view for the Encode documents page:

The dashboard view includes the following components:

Dashboard
component
Description
Data Path The directory on docker volume where you store the raw document data. Sub-directories are read automatically andfiles with extensions .CSV, .PDF, .TXT, .DOCX, .XML, and .IPYNB are encoded.
Collection Name A unique name of the collection to store the vectors in. The name should start with an alphabet or a number and containno space. If you are adding data to an existing collection, make sure to use the same embedder model.
VectorDB Service Type of VectorDB service.
Embedding Service Type of Embedding service.
Encode Select to start encoding after finishing all the inputs.
Conduct Vector
Search Jump to Vector search dashboard.
RAG-based LLM Jump to RAG-based LLM dashboard.
Create a New
Encoding Reset all the tokens on this dashboard.
Return to Menu Return to the main menu.
Encode data from the Splunk platform

In the Splunk App for Data Science and Deep Learning (DSDL), navigate to Assistants , then LLM-RAG , then Encoding
Data to Vector Database , and then select Encode data from Splunk.

Concatenate the command to a search pipeline that produces a table containing only a field of the log data you want to
encode as well as other fields of metadata you want to add. Avoid using embeddings or label as field names in the table,
as these 2 field names are used in the vector database by default.

Encoding too much data at once can cause a failure. Keep the cardinality of logs under 30,000.
Parameters

The Encode data from Splunk page has the following parameters:

Parameters Description
label_field_name Name of the field you want to encode. All the other fields in the table are treated as metadata in the collection.
collection_name A unique name of the collection to store the vectors in. The name must start with a letter or a number and contain nospaces. If you are adding data to an existing collection, make sure to use the same embedder model.
vectordb_service Type of VectorDB service. Choose from milvus, pinecone, and alloydb.
embedder_service Type of embedding service. Choose from gemini. huggingface, ollama, azure_openai, openai, bedrock, and
embedder_name Name of embedding model. Optional if configured on the Setup LLM-RAG page.
embedder_dimension Output dimensionality of the model. Optional if configured on the Setup LLM-RAG page.
Run the fit or compute command

Use the following syntax to run the fit command or the compute command:

Run the fit command:
index=_internal error | table _raw sourcetype source | head 100 | fit MLTKContainer
algo=llm_rag_log_encoder collection_name="test" vectordb_service=milvus
embedder_service=azure_openai embedder_dimension=3072 label_field_name=_raw * into
app:llm_rag_log_encoder as Encode
•
Run the compute command:
index=_internal error | table _raw sourcetype source | head 100 | compute algo:llm_rag_log_encoder
collection_name:"test" vectordb_service:milvus embedder_service:azure_openai embedder_dimension:3072
label_field_name:_raw sourcetype source
The wildcard character ( * ) is not supported in the compute command. You must specify all the input fields
within the command.
•
Dashboard view

The following image shows the dashboard view for the Encode data from Splunk page:

The dashboard view includes the following components:

Dashboard
component
Description
Search bar Search Splunk log data to encode. This search produces a table containing only a field of the log data you want toencode, as well as other fields of metadata you want to add.
Target Field Name The name of the field you want to encode. All the other fields in the table are treated as metadata in the collection.
Collection Name A unique name of the collection to store the vectors in. The name must start with a letter or number and do not includeany spaces. If you are adding data to an existing collection, make sure to use the same embedder model.
VectorDB Service Type of VectorDB service.
Embedding Service Type of Embedding service.
Encode Select to start encoding after finishing all the inputs.
Conduct Vector
Search Jump to Vector search dashboard.
RAG-based LLM Jump to RAG-based LLM dashboard.
Create a New
Encoding Reset all the tokens on this dashboard.
Return to Menu Return to the main menu.
Conduct vector search

In the Splunk App for Data Science and Deep Learning (DSDL), navigate to Assistants , then LLM-RAG , then Encoding
Data to Vector Database , and then select Conduct Vector Search on log data.

Concatenate the command to a search pipeline that produces a table containing only a field of the log data you want to
conduct similarity search on. Rename the field as "text".

Parameters

The Encode data from Splunk page has the following parameters:

Parameters Description
collection_name The existing collection to conduct similarity search on.
vectordb_service Type of VectorDB service. Choose from milvus, pinecone, and alloydb.
embedder_service Type of embedding service. Choose from gemini. huggingface, ollama, azure_openai, openai, bedrock, and
embedder_name Name of embedding model. Optional if configured on the Setup LLM-RAG page.
embedder_dimension Output dimensionality of the model. Optional if configured on the Setup LLM-RAG page.
top_k Number of top results to return.
Run the fit or compute command

Use the following syntax to run the fit command or the compute command:

Run the fit command:
| search ...
| table text
| fit MLTKContainer algo=llm_rag_milvus_search collection_name=test embedder_service=huggingface
vectordb_service=milvus top_k=5 text into app:llm_rag_milvus_search
Run the compute command:
| search ...
| table text
| compute algo:llm_rag_milvus_search collection_name:test embedder_service:huggingface
vectordb_service:milvus top_k:5 text
•
Dashboard view

The following image shows the dashboard view for the Conduct vector search on log data page:

The dashboard view includes the following components:

Dashboard
component
Description
Collection Name A unique name of the collection to store the vectors in. The name must start with a letter or number and do not includeany spaces. If you are adding data to an existing collection, make sure to use the same embedder model.
VectorDB Service Type of VectorDB service.
Embedding Service Type of Embedding service.
Submit Select after finishing all the inputs.
Search bar Search Splunk log data to conduct similarity search. This search produces a table containing only a field of the log datayou want to search on. Select the specific log message to kick off vector search.
Conduct a New Vector
Search Reset all the tokens on this dashboard.
Return to Menu Return to the main menu.
Manage and explore your vector database

In the Splunk App for Data Science and Deep Learning (DSDL), navigate to Assistants , then LLM-RAG , then Encoding
Data to Vector Database , and then select Manage and Explore your vector database.

Parameters

Manage and explore your vector database with the following parameters:

Parameters Description
task
The specific task for management. Use list_collections to list all the existing collections, delete_collection to
delete a specific collection, show_schema to print the schema of a specific collection, and show_rows to print the
number of vectors within a collection.
collection_name The specific collection name. Required for all tasks except list_collections.
Run the fit or compute command

Use the following syntax to run the fit command or the compute command:

Run the fit command:
| makeresults
| fit MLTKContainer algo=llm_rag_milvus_management task=delete_collection
collection_name=document_collection_example _time into app:llm_rag_milvus_management as RAG
•
Run the compute command:
| makeresults
| compute algo:llm_rag_milvus_management task:delete_collection
collection_name:document_collection_example _time
•
Dashboard view

The following image shows the dashboard view for the Manage and explore your vector database page:

The dashboard view includes the following components:

Dashboard component Description
Collection to delete The specific collection name you want to delete.
Submit Select to delete the input collection.
Refresh Refresh the list of collections.
Return to Menu Return to the main menu.
Next step

After pulling the LLM model to your local Docker container and encoding document or log data into the vector database,
you can carry out inferences using the LLM. See Query LLM with vector data.

Query LLM with vector data...................................................................................................................................
After pulling the LLM model to your local Docker container and encoding document or log data into the vector database,
you can carry out inferences using the LLM. See, Encode data into a vector database.

Before you begin make sure you have encoded some documents or log data into the vector database.
To search LLM with VectorDB, complete these tasks:

Standalone LLM: A one-shot Q&A agent to answer user's questions based on prior knowledge within the training
data.
•
RAG-based LLM: Uses additional knowledge that has been encoded in the vector database.
LLM with Function Calling: Runs predefined functions to acquire additional information and generate answers.
Local LLM and Embedding Management: List, pull, and delete LLM models in your on-premises environment.
Standalone LLM

You can use this standalone LLM to conduct text-based classification or summarization by passing the text field to the
algorithm along with a prompt that states the task.

Go to the Standalone LLM page:

In DSDL, go to Assistants.
Select LLM-RAG , then Querying LLM with Vector Data , and then Standalone LLM.
Parameters

The Standalone LLM page has the following parameters:

Parameter name Description
llm_service Type of LLM service. Choose from ollama, azure_openai, openai, bedrock and gemini.
model_name (Optional) The name of an LLM model.
Parameter name Description
prompt A prompt that explains the task to the LLM model.
Run the fit or compute command

Use the following syntax to run the fit command or the compute command:

Run the fit command:
| makeresults | eval text = "Email text: Click to win prize"
| fit MLTKContainer algo=llm_rag_ollama_text_processing llm_service=ollama prompt="You will examine
if the following email content is phishing." text into app:llm_rag_ollama_text_processing
•
Run the compute command:
Make sure you append the compute command to a search pipeline that generates a table with a field called
text to use Standalone LLM.
| makeresults | eval text = "Email text: Click to win prize"
| compute algo:llm_rag_ollama_text_processing llm_service:ollama prompt:"You will examine if the
following email content is phishing." text
•
Dashboard view

The following image shows the dashboard view for the Standalone LLM page:

The dashboard view includes the following components:

Dashboard component Description
Search bar
Create a search pipeline that generates a table with a field called text that contains the text you want to
search.
If there is no specific text to use, keep the search string as it is and search on that instead.
Select LLM Service Choose the LLM service.
Select LLM Model The name of an LLM model that exists in your environment. If no model is shown in the dropdown menu, goto the LLM management page to pull models.
Prompt Write a prompt explaining the task to the LLM. For example, "Is the following email phishing?"
Run Inference Start searching after finishing all the inputs.
Refresh Page Reset all the tokens on this dashboard.
Return to Menu Return to the main menu.
RAG-based LLM

In the Splunk App for Data Science and Deep Learning (DSDL), navigate to Assistants , then LLM-RAG , then Querying
LLM with Vector Data , and then RAG-based LLM.

Parameters

The RAG-based LLM page has the following parameters:

Parameter name Description
llm_service Type of LLM service. Choose from ollama, azure_openai, openai, bedrock, and gemini.
model_name (Optional) The name of an LLM model.
collection_name The existing collection to conduct similarity search on.
vectordb_service Type of VectorDB service. Choose from milvus, pinecone, and alloydb.
embedder_service Type of embedding service. Choose from huggingface, ollama, azure_openai, openai, bedrock, and gemini.
top_k Number of document pieces to retrieve for generation.
embedder_name Name of embedding model. Optional if configured on the Setup LLM-RAG page.
Run the fit or compute command

Use the following syntax to run the fit command or the compute command:

Run the fit command:
| makeresults
| eval query = "Tell me more about the Buttercup online store architecture"
| fit MLTKContainer algo=llm_rag_script llm_service=ollama model_name="llama3"
embedder_service=huggingface collection_name="document_collection_example" top_k=5 query into
app:llm_rag_script as RAG
•
Run the compute command:
| makeresults
•
| eval query = "Tell me more about the Buttercup online store architecture"
| compute algo:llm_rag_script llm_service:ollama model_name:"llama3" embedder_service:huggingface
collection_name:"document_collection_example" top_k:5 query
Dashboard view

The following image shows the dashboard view for the RAG-based LLM page:

The dashboard view includes the following components:

Dashboard component Description
VectorDB Service Type of vectorDB service.
Collection Name An existing collection you want to use for the LLM-RAG.
Embedder Service Type of embedding service.
LLM Service Type of LLM service.
LLM Model LLM model name. Only used for Ollama LLM service.
Number of docs to retrieve Number of document pieces or log messages you wish to use in the RAG.
Input your query Write your search in the text box.
Next Submit the inputs and move on to search input.
Query Select after entering your search and start Retrieval-Augmented Generation (RAG).
Refresh Page Reset all the tokens on this dashboard.
Return to Menu Return to the main menu.
LLM with Function Calling

There are a set of built-in function tools for the model to use:

Search splunk
List indexes
Get index info
List saved searches
List users
Get indexes and sourcetypes
Splunk health check
Use customization for specific use cases.

In the Splunk App for Data Science and Deep Learning (DSDL), navigate to Assistants , then LLM-RAG , then Querying
LLM , and then LLM with Function Calling.

Parameters

The LLM with Function Calling page has the following parameters:

Parameter name Description
prompt Search for the LLM in natural language.
llm_service Type of LLM service. Choose from gemini. ollama, azure_openai, openai, bedrock, and
model_name The name of an LLM model that exists in your environment.
Run the fit or compute command

Use the following syntax to run the fit command or the compute command:

Run the fit command:
| makeresults
| fit MLTKContainer algo=llm_rag_function_calling prompt="Search Splunk for index _internal and
sourcetype splunkd for events containing keyword error from 60 minutes ago to 30 minutes ago. Tell
me how many events occurred" llm_service=bedrock _time into app:llm_rag_function_calling as RAG
•
Run the compute command:
| makeresults
| compute algo:llm_rag_function_calling prompt:"Search Splunk for index _internal and sourcetype
splunkd for events containing keyword error from 60 minutes ago to 30 minutes ago. Tell me how many
events occurred" llm_service:bedrock _time
•
Dashboard view

The following image shows the dashboard view for the LLM with Function Calling page:

The dashboard view includes the following components:

Dashboard component Description
Select LLM Service Type of LLM service.
Select LLM model (Optional) Name of the Ollama model.
Input your query Write your search in the text box.
Next Submit the inputs and move on to search input.
Query Select after entering your search and start Retrieval-Augmented Generation (RAG).
Refresh Page Reset all the tokens on this dashboard.
Return to Menu Return to the main menu.
Local LLM and Embedding Management

In the Splunk App for Data Science and Deep Learning (DSDL), navigate to Assistants , then LLM-RAG , then Querying
LLM , and then Local LLM and Embedding Management.

Parameters

The Local LLM and Embedding Management page has the following parameters:

Parameter
name
Description
task The specific task for management. Choose PULL to download a model and DELETE to delete a model.
model_type Type of model to pull or delete. Choose from stored under /srv/app/model/data. LLM and embedder_model. Note: Downloaded embedder models are
model_name The specific model name. This field is required for downloading or deleting models.
Run the fit or compute command

Use the following syntax to run the fit command or the compute command:

Run the fit command:
| makeresults
| fit MLTKContainer algo=llm_rag_ollama_model_manager task=pull model_type=LLM model_name=mistral
_time into app:llm_rag_ollama_model_manager
•
Run the compute command:
| makeresults
| makeresults
| compute algo:llm_rag_ollama_model_manager task:list model_type:LLM _time
•
Dashboard view

The following image shows the dashboard view for the ' Local LLM and Embedding Management page:

The dashboard view includes the following components:

Dashboard component Description
Task The task to perform. Choose PULL to download a model and DELETE to delete a model.
Service Type Type of model to pull or delete. Choose from Ollama or Huggingface.
Model Name The name of the model to perform a certain task on.
Submit Select to run the task.
Refresh Page Reset all the tokens on this dashboard.
Return to Menu Return to the main menu.
Troubleshooting...............................................................................................................................................................
Troubleshoot the Splunk App for Data Science and Deep Learning.....................................................................
The following are issues you might experience when using the Splunk App for Data Science and Deep Learning and how
to resolve them.

First launch of container not allowing access to JupyterLab

Cause

When you launch a container for the first time, the selected container image is downloaded from Dockerhub automatically
in the background. Depending on your network, this process can take time to download the Docker image for the first time
as the image sizes range from 2-12 GB.

Solution

Allow time for the images to initially pull from Dockerhub. You can check which Docker images are available locally by
runningDocker images on your CLI.

Browser showing an insecure connection

Cause

The Splunk App for Data Science and Deep Learning version 3.5 and higher includes container images that use HTTPS
by default with self-signed certificates for the data transfer related API endpoints and JupyterLab. Many browsers show
"insecure connection" warnings and some allow you to suppress that for localhost connections used during development.

Solution

For production use, work with your Splunk administrator to secure your setup and build containers with your own
certificates, or use more advanced container environment setups.

The Example dashboards don't show results or show errors

Cause

Viewing the dashboard examples depends on the presence of a Container Image, the existence of Notebook code
associated to the Example in JupyterLab, and MLTK permissions being set to Global.

Solution

Perform the following steps to troubleshoot the Example dashboards:

Make sure that the right Container Image is downloaded and up and running for the specific Example. For
example, TensorFlow examples require a TensorFlow container.
1.
Verify that the associated Notebook code exists in JupyterLab and that you have explicitly saved the Notebook by
selecting the Save button. A Python module is saved and located in the /app/model folder in JupyterLab. This
Python module is required to run the Examples and populate the dashboards.
2.
Confirm that the MLTK app permissions are set to Global so that DSDL can use the lookup files required for most
of the Examples.
3.
Containers suddenly stop

About 1 minute after starting, my container suddenly stops.

Cause

Most likely you have two or more DSDL apps installed and configured to use the same container environment. In DSDL
3.x and higher, there is a scheduled search called the MLTK Container Sync that ensures synchronization of running
containers and associated models for the app. If more than one DSDL app is running, there can be synchronization
collisions and containers get stopped.

Solution

When using DSDL 3.x or higher, connect each DSDL app in a one-to-one relationship with your Docker or
Kubernetes environment.

Error following an app version update

After a version update I see the error "unable to read JSON response" when running a DSDL related search.

Cause

This error can indicate that some part of the local configuration of DSDL is out of sync.

Solution

Resolved this error by opening the Setup page with the existing settings and clicking Test and Save again to re-confirm
the configuration.

Where are my Notebooks stored in the Docker environment?

By default, there are 3 Docker volumes automatically mounted for persistence in your Docker environment. Those
volumes are named "mltk-container-app" and "mltk-container-notebooks". The volume "mltk-container-data" is actively
used. You can verify by running docker volume ls on your CLI. For DSDL version 3.1 and higher there is a new default
volume called "mltk-container-data".

What container environments are supported?

The Splunk App for Data Science and Deep Learning architecture supports Docker, Kubernetes, and OpenShift as target
container environments.

Does the app provide Indexer distribution?

No Indexer distribution. Data is processed on the search head and sent to the Splunk App for Data Science and Deep
Learning. Data cannot be processed in a distributed manner such as streaming data in parallel from indexers to one or
many containers. However, all advantages of search in a distributed Splunk platform deployment still exist.

How does the app manage security?

Data is sent from a search head to an MLTK Container uncompressed and unencrypted over HTTP protocol. With regards
to security requirements, Splunk Administrators must take steps to harden or secure the setup of the app and their
container environment accordingly. There are ways to configure the container environment so that it supports secured
communication.

Additional resources........................................................................................................................................................
Support for the Splunk App for Data Science and Deep Learning........................................................................
Support for the Splunk App for Data Science and Deep Learning is available through several channels:

Ask questions and get answers through community support at Splunk Answers.
Join the Splunk community for the Splunk App for Data Science and Deep Learning.
Join the Splunk user group Slack channel.
If you have a support contract, submit a case using the Splunk Support Portal.
For general Splunk platform support, see the Splunk Support Programs page.
To keep track of any product issues by release cycle see, Fixed issues and Known issues.
Learn more about the Splunk App for Data Science and Deep Learning..............................................................
There are many opportunities and options to learn more about the Splunk App for Data Science and Deep Learning:

Read more about machine learning tools in Splunk Blogs.
Join the Splunk user group Slack channel.
Sign up to learn more with Splunk Training & Certification.
Read use cases from Splunk platform experts in the Splunk Lantern Customer Success Center.
Be part of the conversation on the Splunk Community page.
Find answers to common questions related to DSDLin Splunk Answers.
Extend the app with custom MLTK Containers. If you want to rebuild the existing MLTK Container images or want
to build your own custom images, see Splunk MLTK Container Docker.
•
Access source code and build scripts on the Splunk MLTK Container for Docker GitHub Repository.
This is a offline tool, your data stays locally and is not send to any server!
Feedback & Bug Reports
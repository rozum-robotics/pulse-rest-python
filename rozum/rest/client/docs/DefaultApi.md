# swagger_client.DefaultApi

All URIs are relative to *http://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**change_base**](DefaultApi.md#change_base) | **POST** /base | Change robot User Base
[**change_tool**](DefaultApi.md#change_tool) | **POST** /tool | Change robot tool
[**close_gripper**](DefaultApi.md#close_gripper) | **PUT** /gripper/close | Ask robot to Close Gripper
[**freeze**](DefaultApi.md#freeze) | **PUT** /freeze | Freezes robot
[**get_base**](DefaultApi.md#get_base) | **GET** /base | Current User Base
[**get_pose**](DefaultApi.md#get_pose) | **GET** /pose | Current Pose
[**get_position**](DefaultApi.md#get_position) | **GET** /position | Returns current position of Robot
[**get_tool**](DefaultApi.md#get_tool) | **GET** /tool | Current Tool
[**identifier**](DefaultApi.md#identifier) | **GET** /robot/id | Get robot unique identifier
[**open_gripper**](DefaultApi.md#open_gripper) | **PUT** /gripper/open | Ask robot to Open Gripper
[**relax**](DefaultApi.md#relax) | **PUT** /relax | Relaxes robot
[**run_poses**](DefaultApi.md#run_poses) | **PUT** /poses/run | Run poses
[**run_positions**](DefaultApi.md#run_positions) | **PUT** /positions/run | Run positions
[**set_pose**](DefaultApi.md#set_pose) | **PUT** /pose | Set new pose for Robot
[**set_position**](DefaultApi.md#set_position) | **PUT** /position | Set new position for Robot
[**status_motion**](DefaultApi.md#status_motion) | **GET** /status/motion | Status of Motion
[**status_motors**](DefaultApi.md#status_motors) | **GET** /status/motors | Status of Motors


# **change_base**
> Position change_base(body)

Change robot User Base

Change robot User Base current to specified

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
body = swagger_client.Position() # Position | Request Body

try:
    # Change robot User Base
    api_response = api_instance.change_base(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->change_base: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Position**](Position.md)| Request Body | 

### Return type

[**Position**](Position.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_tool**
> Tool change_tool(body)

Change robot tool

Change robot tool current to specified

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
body = swagger_client.Tool() # Tool | Request Body

try:
    # Change robot tool
    api_response = api_instance.change_tool(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->change_tool: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Tool**](Tool.md)| Request Body | 

### Return type

[**Tool**](Tool.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **close_gripper**
> close_gripper(timeout=timeout)

Ask robot to Close Gripper

Ask robot to Close Gripper

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
timeout = 8.14 # float | Time to wait for gripper closing (optional)

try:
    # Ask robot to Close Gripper
    api_instance.close_gripper(timeout=timeout)
except ApiException as e:
    print("Exception when calling DefaultApi->close_gripper: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **float**| Time to wait for gripper closing | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **freeze**
> freeze()

Freezes robot

Freezes robot

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()

try:
    # Freezes robot
    api_instance.freeze()
except ApiException as e:
    print("Exception when calling DefaultApi->freeze: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_base**
> Position get_base()

Current User Base

Returns current Robot User Base

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()

try:
    # Current User Base
    api_response = api_instance.get_base()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_base: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Position**](Position.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pose**
> Pose get_pose()

Current Pose

Returns current pose of Robot

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()

try:
    # Current Pose
    api_response = api_instance.get_pose()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_pose: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Pose**](Pose.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_position**
> Position get_position()

Returns current position of Robot

Returns current position of Robot

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()

try:
    # Returns current position of Robot
    api_response = api_instance.get_position()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_position: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Position**](Position.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tool**
> Tool get_tool()

Current Tool

Returns current Robot Tool

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()

try:
    # Current Tool
    api_response = api_instance.get_tool()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_tool: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Tool**](Tool.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **identifier**
> identifier()

Get robot unique identifier

Get robot unique identifier

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()

try:
    # Get robot unique identifier
    api_instance.identifier()
except ApiException as e:
    print("Exception when calling DefaultApi->identifier: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **open_gripper**
> open_gripper(timeout=timeout)

Ask robot to Open Gripper

Ask robot to Open Gripper

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
timeout = 8.14 # float | Time to wait for gripper opening (optional)

try:
    # Ask robot to Open Gripper
    api_instance.open_gripper(timeout=timeout)
except ApiException as e:
    print("Exception when calling DefaultApi->open_gripper: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **float**| Time to wait for gripper opening | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **relax**
> relax()

Relaxes robot

Relaxes robot

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()

try:
    # Relaxes robot
    api_instance.relax()
except ApiException as e:
    print("Exception when calling DefaultApi->relax: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **run_poses**
> run_poses(body, speed)

Run poses

Run poses

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
body = [swagger_client.Pose()] # list[Pose] | Request Body
speed = 1.2 # float | Speed of Robot

try:
    # Run poses
    api_instance.run_poses(body, speed)
except ApiException as e:
    print("Exception when calling DefaultApi->run_poses: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[Pose]**](Pose.md)| Request Body | 
 **speed** | **float**| Speed of Robot | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: test/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **run_positions**
> run_positions(body, speed)

Run positions

Run positions

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
body = [swagger_client.Position()] # list[Position] | Request Body
speed = 1.2 # float | Speed of Robot

try:
    # Run positions
    api_instance.run_positions(body, speed)
except ApiException as e:
    print("Exception when calling DefaultApi->run_positions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[Position]**](Position.md)| Request Body | 
 **speed** | **float**| Speed of Robot | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: test/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_pose**
> set_pose(body, speed=speed)

Set new pose for Robot

Set new pose for Robot

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
body = swagger_client.Pose() # Pose | Request Body
speed = 1.2 # float | Speed of Robot (optional)

try:
    # Set new pose for Robot
    api_instance.set_pose(body, speed=speed)
except ApiException as e:
    print("Exception when calling DefaultApi->set_pose: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Pose**](Pose.md)| Request Body | 
 **speed** | **float**| Speed of Robot | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_position**
> Position set_position(body, speed)

Set new position for Robot

Set new position for Robot

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
body = swagger_client.Position() # Position | Request Body
speed = 1.2 # float | Speed of Robot

try:
    # Set new position for Robot
    api_response = api_instance.set_position(body, speed)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->set_position: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Position**](Position.md)| Request Body | 
 **speed** | **float**| Speed of Robot | 

### Return type

[**Position**](Position.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **status_motion**
> MotionStatus status_motion()

Status of Motion

Status of Motion

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()

try:
    # Status of Motion
    api_response = api_instance.status_motion()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->status_motion: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**MotionStatus**](MotionStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **status_motors**
> list[MotorStatus] status_motors()

Status of Motors

Status of Motors

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()

try:
    # Status of Motors
    api_response = api_instance.status_motors()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->status_motors: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[MotorStatus]**](MotorStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


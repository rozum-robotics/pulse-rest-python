# rozum.rest.robot.Robot
Simplified version of api. 
All URIs are relative to *http://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**await_motion**](#await_motion) | uses  [**status_motion**](#status_motion) | Waiting till robot finishes motion.
[**close_gripper**](#close_gripper) | **PUT** /gripper/close | Ask robot to Close Gripper
[**freeze**](#freeze) | **PUT** /freeze | Freezes robot
[**get_pose**](#get_pose) | **GET** /pose | Current Pose
[**get_position**](#get_position) | **GET** /position | Returns current position of Robot
[**open_gripper**](#open_gripper) | **PUT** /gripper/open | Ask robot to Open Gripper
[**relax**](#relax) | **PUT** /relax | Relaxes robot
[**run_poses**](#run_poses) | **PUT** /poses/run | Run poses
[**run_positions**](#run_positions) | **PUT** /positions/run | Run positions
[**set_pose**](#set_pose) | **PUT** /pose | Set new pose for Robot
[**set_position**](#set_position) | **PUT** /position | Set new position for Robot
[**status_motion**](#status_motion) | **GET** /status/motion | Status of Motion
[**status_motors**](#status_motors) | **GET** /status/motors | Status of Motors

# **await_motion**
> await_motion(asking_interval)

Ask robot to wait until it finishes motion.

### Example
```python
from __future__ import print_function
import rozum.rest.client
from rozum.rest.client.rest import ApiException
from rozum.rest.client.models import Pose
# create an instance of the API class
robot = rozum.rest.Robot()

try:
    # Tell robot to go somewhere
    robot.set_pose(Pose([0, 0, 0, 0, 0, 0]), speed=100)
    # Wait till movement finishes.
    robot.await_motion()
except ApiException as e:
    print("Exception when calling Robot: %s\n" % e)
```

### Parameters
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asking_interval** | **float**| time in seconds | default = 0.1 s

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **close_gripper**
> close_gripper()

Ask robot to Close Gripper

Ask robot to Close Gripper

### Example
```python
from __future__ import print_function
import rozum.rest.client
from rozum.rest.client.rest import ApiException

# create an instance of the API class
robot = rozum.rest.Robot()

try:
    # Ask robot to Close Gripper
    robot.close_gripper()
except ApiException as e:
    print("Exception when calling Robot->close_gripper: %s\n" % e)
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

# **freeze**
> freeze()

Freezes robot

Freezes robot

### Example
```python
from __future__ import print_function
import rozum.rest.client
from rozum.rest.client.rest import ApiException

# create an instance of the API class
robot = rozum.rest.Robot()

try:
    # Freezes robot
    robot.freeze()
except ApiException as e:
    print("Exception when calling Robot->freeze: %s\n" % e)
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

# **get_pose**
> Pose get_pose()

Current Pose

Returns current pose of Robot

### Example
```python
from __future__ import print_function
import rozum.rest
from rozum.rest.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
robot = rozum.rest.Robot()

try:
    # Current Pose
    pose = robot.get_pose()
    pprint(pose)
except ApiException as e:
    print("Exception when calling Robot->get_pose: %s\n" % e)
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
import rozum.rest
from rozum.rest.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
robot = rozum.rest.Robot()

try:
    # Returns current position of Robot
    position = robot.get_position()
    pprint(position)
except ApiException as e:
    print("Exception when calling Robot->get_position: %s\n" % e)
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

# **open_gripper**
> open_gripper()

Ask robot to Open Gripper

Ask robot to Open Gripper

### Example
```python
from __future__ import print_function
import rozum.rest
from rozum.rest.client.rest import ApiException

# create an instance of the API class
robot = rozum.rest.Robot()

try:
    # Ask robot to Open Gripper
    robot.open_gripper()
except ApiException as e:
    print("Exception when calling Robot->open_gripper: %s\n" % e)
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

# **relax**
> relax()

Relaxes robot

Relaxes robot

### Example
```python
from __future__ import print_function
import rozum.rest
from rozum.rest.client.rest import ApiException

# create an instance of the API class
robot = rozum.rest.Robot()

try:
    # Relaxes robot
    robot.relax()
except ApiException as e:
    print("Exception when calling Robot->relax: %s\n" % e)
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
> run_poses(body, speed=speed)

Run poses

Run poses

### Example
```python
from __future__ import print_function
import rozum.rest
import rozum.rest.client
from rozum.rest.client.rest import ApiException

# create an instance of the API class
robot = rozum.rest.Robot()
body = [rozum.rest.client.Pose()] # list[Pose] | Request Body
speed = 1.2 # float | Speed of Robot in percents (required)

try:
    # Run poses
    robot.run_poses(body, speed=speed)
except ApiException as e:
    print("Exception when calling Robot->run_poses: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[Pose]**](Pose.md)| Request Body | 
 **speed** | **float**| Speed of Robot in percents | [required] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: test/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **run_positions**
> run_positions(body, speed=speed)

Run positions

Run positions

### Example
```python
from __future__ import print_function
import rozum.rest
import rozum.rest.client
from rozum.rest.client.rest import ApiException

# create an instance of the API class
robot = rozum.rest.Robot()
body = [rozum.rest.client.Position()] # list[Position] | Request Body
speed = 1.2 # float | Speed of Robot in percents.

try:
    # Run positions
    robot.run_positions(body, speed=speed)
except ApiException as e:
    print("Exception when calling Robot->run_positions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[Position]**](Position.md)| Request Body | 
 **speed** | **float**| Speed of Robot in percents. | [required] 
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
import rozum.rest
import rozum.rest.client
from rozum.rest.client.rest import ApiException

# create an instance of the API class
robot = rozum.rest.Robot()
body = rozum.rest.client.Pose() # Pose | Request Body
speed = 1.2 # float | Speed of Robot in percents (required)

try:
    # Set new pose for Robot
    robot.set_pose(body, speed=speed)
except ApiException as e:
    print("Exception when calling Robot->set_pose: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Pose**](Pose.md)| Request Body | 
 **speed** | **float**| Speed of Robot in percents | [required] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_position**
> Position set_position(body, speed=speed)

Set new position for Robot

Set new position for Robot

### Example
```python
from __future__ import print_function
import rozum.rest.client
from rozum.rest.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
robot = rozum.rest.Robot()
body = rozum.rest.client.Position() # Position | Request Body
speed = 1.2 # float | Speed of Robot in percents. (required)

try:
    # Set new position for Robot
    api_response = robot.set_position(body, speed=speed)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling Robot->set_position: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Position**](Position.md)| Request Body | 
 **speed** | **float**| Speed of Robot in percents. | [required] 

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
import rozum.rest.client
from rozum.rest.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
robot = rozum.rest.Robot()

try:
    # Status of Motion
    status = robot.status_motion()
    pprint(status)
except ApiException as e:
    print("Exception when calling Robot->status_motion: %s\n" % e)
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
import rozum.rest
from rozum.rest.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
robot = rozum.rest.Robot()

try:
    # Status of Motors
    status = robot.status_motors()
    pprint(status)
except ApiException as e:
    print("Exception when calling Robot->status_motors: %s\n" % e)
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


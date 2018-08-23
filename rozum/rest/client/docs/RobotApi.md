# swagger_client.RobotApi

All URIs are relative to *http://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**change_base**](RobotApi.md#change_base) | **POST** /base | Setting a new zero point position
[**change_tool**](RobotApi.md#change_tool) | **POST** /tool | Setting tool properties
[**close_gripper**](RobotApi.md#close_gripper) | **PUT** /gripper/close | Asking the arm to close the gripper
[**freeze**](RobotApi.md#freeze) | **PUT** /freeze | Asking the arm to go to the freeze state
[**get_base**](RobotApi.md#get_base) | **GET** /base | Getting the actual position of the arm base
[**get_digital_output**](RobotApi.md#get_digital_output) | **GET** /signal | Get level of digital output signal
[**get_pose**](RobotApi.md#get_pose) | **GET** /pose | Getting the actual arm pose
[**get_position**](RobotApi.md#get_position) | **GET** /position | Getting the actual arm position
[**get_tool**](RobotApi.md#get_tool) | **GET** /tool | Getting actual tool properties
[**identifier**](RobotApi.md#identifier) | **GET** /robot/id | Getting the arm ID
[**open_gripper**](RobotApi.md#open_gripper) | **PUT** /gripper/open | Asking the arm to open the gripper
[**relax**](RobotApi.md#relax) | **PUT** /relax | Asking the arm to relax
[**run_poses**](RobotApi.md#run_poses) | **PUT** /poses/run | Asking the arm to move to a pose
[**run_positions**](RobotApi.md#run_positions) | **PUT** /positions/run | Asking the arm to move to a position
[**set_digital_output_high**](RobotApi.md#set_digital_output_high) | **PUT** /signal/high | Set high level of digital output signal
[**set_digital_output_low**](RobotApi.md#set_digital_output_low) | **PUT** /signal/low | Set low level of digital output signal
[**set_pose**](RobotApi.md#set_pose) | **PUT** /pose | Setting a new arm pose
[**set_position**](RobotApi.md#set_position) | **PUT** /position | Setting a new arm position
[**status_motion**](RobotApi.md#status_motion) | **GET** /status/motion | Getting the actual motion status
[**status_motors**](RobotApi.md#status_motors) | **GET** /status/motors | Getting the actual status of servo motors


# **change_base**
> Position change_base(body)

Setting a new zero point position

The function enables setting a new zero point position of the robotic arm as required for the current user environment (e.g., considering the surrounding equipment). The new zero point position is described as a set of x, y, and z coordinates, as well as _roll_, _pitch_, and _yaw_ rotation angles. The coordinates define the desired offset (in meters) from the physical centerpoint of the arm base (original zero point) along the x, y, and z axes accordingly. _Roll_ stands for the rotation angle around the x axis; _pitch_ - the rotation angle around the y axis; _yaw_ - the rotation angle around the z axis. All rotation angles are in radians and relative to the physical centerpoint of the arm base.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RobotApi()
body = swagger_client.Position() # Position | Request Body

try:
    # Setting a new zero point position
    api_response = api_instance.change_base(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RobotApi->change_base: %s\n" % e)
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

Setting tool properties

The function enables setting new TCP to account for the properties of an attached or changed work tool. The tool properties define the following: - _name_ - any random name of the work tool defined by the user (e.g., \"gripper\") - _position_ - a set of x, y, and z coordinates and rotation angles - _roll_, _pitch_, and _yaw_. The coordinates define the actual distance (in meters) from the arm's zero point to the new TCP along the x, y, and z axes accordingly. _Roll_ stands for the rotation angle of the new TCP around the x axis; _pitch_ - the rotation angle around the y axis; _yaw_ - the rotation angle of the new TCP around the z axis. All rotation angles are in radians. - _radius_ - radius of the work tool (in meters) measured from its physical center point.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RobotApi()
body = swagger_client.Tool() # Tool | Request Body

try:
    # Setting tool properties
    api_response = api_instance.change_tool(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RobotApi->change_tool: %s\n" % e)
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

Asking the arm to close the gripper

The function commands the robot to close the gripper. It has no request body, but the user can optionally set how long (in milliseconds) the arm should remain idle, waiting for the gripper to close. The default manufacturer-preset value is 500 ms. ### Note: Setting the parameter, it is recommended to use values above 0 ms.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RobotApi()
timeout = 8.14 # float | Time in milliseconds to wait for gripper closing (optional)

try:
    # Asking the arm to close the gripper
    api_instance.close_gripper(timeout=timeout)
except ApiException as e:
    print("Exception when calling RobotApi->close_gripper: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **float**| Time in milliseconds to wait for gripper closing | [optional] 

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

Asking the arm to go to the freeze state

The function sets the arm in the \"freeze\" state. The arm stops moving, retaining its last position. ### Note: In the state, it is not advisable to move the arm by hand as this can cause damage to its components.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RobotApi()

try:
    # Asking the arm to go to the freeze state
    api_instance.freeze()
except ApiException as e:
    print("Exception when calling RobotApi->freeze: %s\n" % e)
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

Getting the actual position of the arm base

The function returns the actual position of the arm's zero point in the user environment. The actual zero point position is described as a set of x, y, and z coordinates, as well as _roll_, _pitch_, and _yaw_ rotation angles. The coordinates define the offset (in meters) from the physical centerpoint of the arm base (original zero point) to the actual zero point position along the x, y, and z axes accordingly. _Roll_ stands for the rotation angle around the x axis; _pitch_ - the rotation angle around the y axis; _yaw_ - the rotation angle around the z axis. All rotation angles are in radians and relative to the physical centerpoint of the arm base.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RobotApi()

try:
    # Getting the actual position of the arm base
    api_response = api_instance.get_base()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RobotApi->get_base: %s\n" % e)
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

# **get_digital_output**
> Signal get_digital_output(port)

Get level of digital output signal

The function get level of digital output signal on the specified port. The port is a number described on which psychical port you want to set high level signal.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RobotApi()
port = 8.14 # float | Number of output digital port that you want to set high level.

try:
    # Get level of digital output signal
    api_response = api_instance.get_digital_output(port)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RobotApi->get_digital_output: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **port** | **float**| Number of output digital port that you want to set high level. | 

### Return type

[**Signal**](Signal.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pose**
> Pose get_pose()

Getting the actual arm pose

The function returns the actual pose of the robotic arm. The pose is described as a set of output flange angles (in degrees) of all the six servos in the arm joints.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RobotApi()

try:
    # Getting the actual arm pose
    api_response = api_instance.get_pose()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RobotApi->get_pose: %s\n" % e)
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

Getting the actual arm position

The function returns the actual position of the PULSE robotic arm, which is described as a set of x, y, and z coordinates, as well as _roll_, _pitch_, and _yaw_ rotation angles. The coordinates define the actual distance (in meters) from the zero point of the robotic arm to the tool center point (TCP) along the x, y, and z axes accordingly. _Roll_ stands for the TCP rotation angle around the x axis; _pitch_ - the TCP rotation angle around the y axis; _yaw_ - the TCP rotation angle around the z axis. All rotation angles are in radians and relative to the zero point.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RobotApi()

try:
    # Getting the actual arm position
    api_response = api_instance.get_position()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RobotApi->get_position: %s\n" % e)
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

Getting actual tool properties

The function returns the actual TCP position that accounts for the offset from the original TCP due to attaching/changing the work tool. The actual TCP position is described as a set of the following properties: - _name_ - any random name of the work tool defined by the user (e.g., \"gripper\") - _position_ - x, y, and z coordinates, as well as _roll_, _pitch_, and _yaw_ rotation angles. The coordinates define the distance (in meters) from the arm's zero point to the actual TCP along the x, y, and z axes accordingly. _Roll_ stands for the actual TCP rotation angle around the x axis; _pitch_ - the actual TCP rotation angle around the y axis; _yaw_ - the actual TCP rotation angle around the z axis. All rotation angles are in radians. - _radius_ - radius of the work tool (in meters) measured from its center point.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RobotApi()

try:
    # Getting actual tool properties
    api_response = api_instance.get_tool()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RobotApi->get_tool: %s\n" % e)
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
> str identifier()

Getting the arm ID

The function returns the unique identifier (ID) of the robotic arm. The ID is an alphanumeric designation that consists of individual servo motor identifications.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RobotApi()

try:
    # Getting the arm ID
    api_response = api_instance.identifier()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RobotApi->identifier: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **open_gripper**
> open_gripper(timeout=timeout)

Asking the arm to open the gripper

The function commands the robot to open the gripper. It has no request body, but the user can optionally set how long (in milliseconds) the arm should remain idle, waiting for the gripper to open. The default manufacturer-preset value is 500 ms. ### Note: Setting the parameter, it is recommended to use values above 0 ms.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RobotApi()
timeout = 8.14 # float | Time in milliseconds to wait for gripper opening (optional)

try:
    # Asking the arm to open the gripper
    api_instance.open_gripper(timeout=timeout)
except ApiException as e:
    print("Exception when calling RobotApi->open_gripper: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **float**| Time in milliseconds to wait for gripper opening | [optional] 

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

Asking the arm to relax

The function sets the arm in the \"relaxed\" state. The arm stops moving without retaining its last position. In this state, the user can move the robotic arm by hand (e.g., to verify/test a motion trajectory).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RobotApi()

try:
    # Asking the arm to relax
    api_instance.relax()
except ApiException as e:
    print("Exception when calling RobotApi->relax: %s\n" % e)
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
> str run_poses(body, speed)

Asking the arm to move to a pose

The function allows for setting a trajectory of one or more waypoints to move the robotic arm smoothly from one pose to another. In the trajectory, each waypoint is a set of output flange angles (in degrees) of the six servos in the arm joints. ### Note: Similarly, you can move the arm from one pose to another through one or more waypoints using the PUT/pose function. When the arm is executing a trajectory of PUT/pose waypoints, it stops for a short moment at each preset waypoint. With the PUT/poses/run function, however, the arm moves smoothly though all waypoints without stopping, which reduces the overall time of going from one pose to another.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RobotApi()
body = [swagger_client.Pose()] # list[Pose] | Request Body
speed = 1.2 # float | Speed of Robot

try:
    # Asking the arm to move to a pose
    api_response = api_instance.run_poses(body, speed)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RobotApi->run_poses: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[Pose]**](Pose.md)| Request Body | 
 **speed** | **float**| Speed of Robot | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **run_positions**
> str run_positions(body, speed)

Asking the arm to move to a position

The function allows for setting a trajectory of one or more waypoints to move the robotic arm smoothly from one position to another. In the trajectory, each waypoint is described as a set of x, y, and z coordinates, as well as _roll_, _pitch_, and _yaw_ rotation angles. The coordinates define the distance (in meters) from the zero point to the desired TCP along the x, y, and z axes accordingly. _Roll_ stands for the desired TCP rotation angle around the x axis; _pitch_ - the desired TCP rotation angle around the y axis; _yaw_ - the desired TCP rotation angle around the z axis. All rotation angles are in radians.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RobotApi()
body = [swagger_client.Position()] # list[Position] | Request Body
speed = 1.2 # float | Speed of Robot

try:
    # Asking the arm to move to a position
    api_response = api_instance.run_positions(body, speed)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RobotApi->run_positions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[Position]**](Position.md)| Request Body | 
 **speed** | **float**| Speed of Robot | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_digital_output_high**
> str set_digital_output_high(port)

Set high level of digital output signal

The function set high level of digital output signal on the specified port. The port is a number described on which psychical port you want to set high level signal.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RobotApi()
port = 8.14 # float | Number of output digital port that you want to set high level.

try:
    # Set high level of digital output signal
    api_response = api_instance.set_digital_output_high(port)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RobotApi->set_digital_output_high: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **port** | **float**| Number of output digital port that you want to set high level. | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_digital_output_low**
> str set_digital_output_low(port)

Set low level of digital output signal

The function set low level of digital output signal on the specified port. The port is a number described on which psychical port you want to set low level signal.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RobotApi()
port = 8.14 # float | Number of output digital port that you want to set low level.

try:
    # Set low level of digital output signal
    api_response = api_instance.set_digital_output_low(port)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RobotApi->set_digital_output_low: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **port** | **float**| Number of output digital port that you want to set low level. | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_pose**
> str set_pose(body, speed)

Setting a new arm pose

The function commands the arm to move to a new pose. A pose is described as a set of output flange angles (in degrees) of the six servos integrated into the robot joints.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RobotApi()
body = swagger_client.Pose() # Pose | Request Body
speed = 1.2 # float | Speed of Robot

try:
    # Setting a new arm pose
    api_response = api_instance.set_pose(body, speed)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RobotApi->set_pose: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Pose**](Pose.md)| Request Body | 
 **speed** | **float**| Speed of Robot | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_position**
> Position set_position(body, speed)

Setting a new arm position

The function commands the arm to move to a new position. The position is described as a set of x, y, and z coordinates, as well as _roll_, _pitch_, and _yaw_ rotation angles. The coordinates define the desired distance (in meters) from the zero point to the TCP along the x, y, and z axes accordingly. _Roll_ stands for the desired TCP rotation angle around the x axis; _pitch_ - the desired TCP rotation angle around the y axis; _yaw_ - the desired TCP rotation angle around the z axis. All rotation angles are in radians.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RobotApi()
body = swagger_client.Position() # Position | Request Body
speed = 1.2 # float | Speed of Robot

try:
    # Setting a new arm position
    api_response = api_instance.set_position(body, speed)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RobotApi->set_position: %s\n" % e)
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

Getting the actual motion status

The function returns the actual state of the robotic arm - whether it is running (in motion), or idle (not in motion), or in the zero gravity mode.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RobotApi()

try:
    # Getting the actual motion status
    api_response = api_instance.status_motion()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RobotApi->status_motion: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**MotionStatus**](MotionStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **status_motors**
> list[MotorStatus] status_motors()

Getting the actual status of servo motors

The function returns the actual states of the six servo motors integrated into the joints of the robotic arm. The states are described as arrays of values for the following properties: - _Angle_ - the actual angular position (in degrees) of the servo's output flange - _Rotor velocity_ - the actual rotor velocity (in RPM) - _RMS current_ - the actual input current (in Amperes) - _Phase current_ - the actual magnitude of alternating current (in Amperes) - _Supply voltage_ - the actual supply voltage (in Volts) - _Stator temperature_  - the actual temperature (in degrees C) as measured on the stator winding - _Servo temperature_ - the actual temperature (in degrees C) as measured on the MCU PCB - _Velocity setpoint_ - the user-preset rotor velocity (in RPM) - _Velocity output_ - the motor control current (in Amperes) based on the preset velocity - _Velocity feedback_ - the actual rotor velocity (in RPM) - _Velocity error_ - the difference between the preset and the actual rotor velocities (in RPM) - _Position setpoint_ - the user-preset position of the servo flange in degrees - _Position output_ - rotor velocity (in RPM) based on the position setpoint - _Position feedback_ - the actual position of the servo flange (in degrees) based on the encoder feedback - _Position error_ - the difference (in degrees) between the preset and the actual positions of the servo flange  Each property in an array has six values - one for each of the six servos in the arm joints.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RobotApi()

try:
    # Getting the actual status of servo motors
    api_response = api_instance.status_motors()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RobotApi->status_motors: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[MotorStatus]**](MotorStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


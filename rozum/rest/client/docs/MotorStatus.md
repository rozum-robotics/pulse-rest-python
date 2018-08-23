# MotorStatus

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**angle** | **float** | The actual angular position (in degrees) of the servo&#39;s output flange | [optional] 
**rotor_velocity** | **float** | The actual rotor velocity (in RPM) | [optional] 
**rms_current** | **float** | The actual input current (in Amperes) | [optional] 
**voltage** | **float** | The actual supply voltage (in Volts) | [optional] 
**phase_current** | **float** | Current value phase current for this motor | [optional] 
**stator_temperature** | **float** | The actual temperature (in degrees C) as measured on the stator winding | [optional] 
**servo_temperature** | **float** | The actual temperature (in degrees C) as measured on the MCU PCB | [optional] 
**velocity_error** | **float** | The difference between the preset and the actual rotor velocities (in RPM) | [optional] 
**velocity_setpoint** | **float** | The user-preset rotor velocity (in RPM) | [optional] 
**velocity_output** | **float** | The motor control current (in Amperes) based on the preset velocity | [optional] 
**velocity_feedback** | **float** | The actual rotor velocity (in RPM) | [optional] 
**position_error** | **float** | The difference between the preset and the actual positions of the servo flange (in degrees) | [optional] 
**position_setpoint** | **float** | The user-preset position of the servo flange in degrees | [optional] 
**position_output** | **float** | Rotor velocity (in RPM) based on the position setpoint | [optional] 
**position_feedback** | **float** | The actual position of the servo flange (in degrees) based on the encoder feedback | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



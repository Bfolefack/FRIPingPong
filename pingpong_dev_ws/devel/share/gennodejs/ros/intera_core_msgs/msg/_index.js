
"use strict";

let IOComponentStatus = require('./IOComponentStatus.js');
let AnalogIOState = require('./AnalogIOState.js');
let DigitalOutputCommand = require('./DigitalOutputCommand.js');
let HeadPanCommand = require('./HeadPanCommand.js');
let HeadState = require('./HeadState.js');
let DigitalIOStates = require('./DigitalIOStates.js');
let SEAJointState = require('./SEAJointState.js');
let InteractionControlState = require('./InteractionControlState.js');
let HomingCommand = require('./HomingCommand.js');
let EndpointState = require('./EndpointState.js');
let IONodeConfiguration = require('./IONodeConfiguration.js');
let JointCommand = require('./JointCommand.js');
let HomingState = require('./HomingState.js');
let AnalogOutputCommand = require('./AnalogOutputCommand.js');
let IODataStatus = require('./IODataStatus.js');
let NavigatorStates = require('./NavigatorStates.js');
let RobotAssemblyState = require('./RobotAssemblyState.js');
let IODeviceConfiguration = require('./IODeviceConfiguration.js');
let IOStatus = require('./IOStatus.js');
let CollisionDetectionState = require('./CollisionDetectionState.js');
let CollisionAvoidanceState = require('./CollisionAvoidanceState.js');
let NavigatorState = require('./NavigatorState.js');
let IOComponentCommand = require('./IOComponentCommand.js');
let URDFConfiguration = require('./URDFConfiguration.js');
let DigitalIOState = require('./DigitalIOState.js');
let CameraControl = require('./CameraControl.js');
let CameraSettings = require('./CameraSettings.js');
let EndpointNamesArray = require('./EndpointNamesArray.js');
let IOComponentConfiguration = require('./IOComponentConfiguration.js');
let AnalogIOStates = require('./AnalogIOStates.js');
let IODeviceStatus = require('./IODeviceStatus.js');
let EndpointStates = require('./EndpointStates.js');
let JointLimits = require('./JointLimits.js');
let InteractionControlCommand = require('./InteractionControlCommand.js');
let IONodeStatus = require('./IONodeStatus.js');
let CalibrationCommandResult = require('./CalibrationCommandResult.js');
let CalibrationCommandActionResult = require('./CalibrationCommandActionResult.js');
let CalibrationCommandActionGoal = require('./CalibrationCommandActionGoal.js');
let CalibrationCommandFeedback = require('./CalibrationCommandFeedback.js');
let CalibrationCommandAction = require('./CalibrationCommandAction.js');
let CalibrationCommandActionFeedback = require('./CalibrationCommandActionFeedback.js');
let CalibrationCommandGoal = require('./CalibrationCommandGoal.js');

module.exports = {
  IOComponentStatus: IOComponentStatus,
  AnalogIOState: AnalogIOState,
  DigitalOutputCommand: DigitalOutputCommand,
  HeadPanCommand: HeadPanCommand,
  HeadState: HeadState,
  DigitalIOStates: DigitalIOStates,
  SEAJointState: SEAJointState,
  InteractionControlState: InteractionControlState,
  HomingCommand: HomingCommand,
  EndpointState: EndpointState,
  IONodeConfiguration: IONodeConfiguration,
  JointCommand: JointCommand,
  HomingState: HomingState,
  AnalogOutputCommand: AnalogOutputCommand,
  IODataStatus: IODataStatus,
  NavigatorStates: NavigatorStates,
  RobotAssemblyState: RobotAssemblyState,
  IODeviceConfiguration: IODeviceConfiguration,
  IOStatus: IOStatus,
  CollisionDetectionState: CollisionDetectionState,
  CollisionAvoidanceState: CollisionAvoidanceState,
  NavigatorState: NavigatorState,
  IOComponentCommand: IOComponentCommand,
  URDFConfiguration: URDFConfiguration,
  DigitalIOState: DigitalIOState,
  CameraControl: CameraControl,
  CameraSettings: CameraSettings,
  EndpointNamesArray: EndpointNamesArray,
  IOComponentConfiguration: IOComponentConfiguration,
  AnalogIOStates: AnalogIOStates,
  IODeviceStatus: IODeviceStatus,
  EndpointStates: EndpointStates,
  JointLimits: JointLimits,
  InteractionControlCommand: InteractionControlCommand,
  IONodeStatus: IONodeStatus,
  CalibrationCommandResult: CalibrationCommandResult,
  CalibrationCommandActionResult: CalibrationCommandActionResult,
  CalibrationCommandActionGoal: CalibrationCommandActionGoal,
  CalibrationCommandFeedback: CalibrationCommandFeedback,
  CalibrationCommandAction: CalibrationCommandAction,
  CalibrationCommandActionFeedback: CalibrationCommandActionFeedback,
  CalibrationCommandGoal: CalibrationCommandGoal,
};

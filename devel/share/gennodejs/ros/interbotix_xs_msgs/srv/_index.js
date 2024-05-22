
"use strict";

let OperatingModes = require('./OperatingModes.js')
let TorqueEnable = require('./TorqueEnable.js')
let RegisterValues = require('./RegisterValues.js')
let Reboot = require('./Reboot.js')
let RobotInfo = require('./RobotInfo.js')
let MotorGains = require('./MotorGains.js')

module.exports = {
  OperatingModes: OperatingModes,
  TorqueEnable: TorqueEnable,
  RegisterValues: RegisterValues,
  Reboot: Reboot,
  RobotInfo: RobotInfo,
  MotorGains: MotorGains,
};

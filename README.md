# Armer Mico
[![QUT Centre for Robotics Open Source](https://github.com/qcr/qcr.github.io/raw/master/misc/badge.svg)](https://qcr.github.io)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Build Status](https://github.com/suddrey-qut/armer/workflows/Build/badge.svg?branch=master)](https://github.com/suddrey-qut/armer/actions?query=workflow%3ABuild)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/suddrey-qut/armer.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/suddrey-qut/armer/context:python)
[![Coverage](https://codecov.io/gh/suddrey-qut/armer/branch/master/graph/badge.svg)](https://codecov.io/gh/suddrey-qut/armer)

*To be used with the [Armer Driver](https://github.com/qcr/armer)*

This package launches the Mico drivers for use with the [Armer Driver](https://github.com/qcr/armer).

It interfaces with the [Mico drivers](https://github.com/Kinovarobotics/kinova-ros/tree/noetic-devel) so they must be installed and built as well.

## Installation

### Preinstallation step: Install UR drivers
1. Clone the driver to the Armer workspace

```
cd ~/armer_ws/src
git clone https://github.com/Kinovarobotics/kinova-ros.git kinova-ros
cd kinova-ros
rm -r kinova_moveit
rm -r kinova_gazebo
```

2. Setup arm permissions

To access the arm via usb copy the udev rule file 10-kinova-arm.rules from ~/catkin_ws/src/kinova-ros/kinova_driver/udev to /etc/udev/rules.d/:
```

sudo cp kinova_driver/udev/10-kinova-arm.rules /etc/udev/rules.d/
```
3. Install dependencies and build workspace
```
sudo apt update 
rosdep update 
cd ~/armer_ws
rosdep install --from-paths src --ignore-src -y
catkin_make
echo "Completed dependency install"
```

### Armer Mico installation
The following code snippet will download the Armer Mico hardware package to workspace ~/armer_ws. It will then install dependencies and rebuild the workspace.

```
cd ~/armer_ws
git clone https://github.com/qcr/armer_mico.git src/armer_mico
rosdep install --from-paths src --ignore-src -r -y 
catkin_make 
```

## Usage
```sh
roslaunch armer_mico robot_bringup.launch 
```
 By default this will launch to control a physical Mico. To run a Swift simulation the sim parameter can be set to true. For example:

```sh
roslaunch armer_ur robot_bringup.launch sim:=true
```


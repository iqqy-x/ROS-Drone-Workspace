### Install Dependencies
```
$ sudo apt update
$ sudo apt install python3-pip ros-humble-rosbridge-suite ros-humble-web-video-server
$ pip install opencv-python
```

### ws
```
$ mkdir your_ws
$ cd your_ws
$ git clone https://github.com/iqqy-x/ROS-Drone-Workspace.git src
```

### Build
```
$ cd ~/your_ws
$ colcon build
```

## Usage 
Pake launch aja ***d_bringup***
```
$ ros2 launch d_bringup sim_bringup.launch.yaml
```

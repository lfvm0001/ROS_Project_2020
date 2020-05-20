# ROS_Project_2020
Robotics project for mecathronics master

How to install ROS melodic on your machine. All the below steps were taken from
ROS wiki. (http://wiki.ros.org/melodic/Installation/Ubuntu) Refer to it for more information

1.  Prerequisites

    - Ubuntu 18.04 (or VM with it) because we are going to use ROS melodic

2. Installation

    2.1.  Configure your Ubuntu repositories

      Configure your Ubuntu repositories to allow "restricted," "universe," and
      "multiverse."

    2.2.  Setup your sources.list

        sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'

    2.3.  Set up your keys

      sudo apt-key adv --keyserver 'hkp://keyserver.ubuntu.com:80' --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654

    2.4.  Installation

      sudo apt update

      sudo apt install ros-melodic-desktop-full

    2.5.  Environment setup

      echo "source /opt/ros/melodic/setup.bash" >> ~/.bashrc

      source ~/.bashrc

    2.6. Dependencies for building packages

      sudo apt install python-rosdep python-rosinstall python-rosinstall-generator python-wstool build-essential

      sudo apt install python-rosdep

      sudo rosdep init

      rosdep update

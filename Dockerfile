FROM ros:humble

RUN apt-get update -y && apt-get install -y \
    ros-$ROS_DISTRO-rmw-cyclonedds-cpp \
    ros-$ROS_DISTRO-demo-nodes-cpp

ENV RMW_IMPLEMENTATION=rmw_cyclonedds_cpp

WORKDIR /ws
COPY . /ws/src

RUN . /opt/ros/$ROS_DISTRO/setup.sh \
    && colcon build

RUN echo "source /ws/install/setup.bash" >> /root/.bashrc

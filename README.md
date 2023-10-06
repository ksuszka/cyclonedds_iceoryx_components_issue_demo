

# Overview

This repository demonstrates an issue with a composable node not being loaded when CycloneDDS with Iceoryx is used.

# Steps to reproduce

## Preparation

Build docker image:

```
docker build -f Dockerfile -t cyclone-component-test .
```

Open three terminal windows.

In the first terminal window start a docker container with the iox-roudi memory server:

```
docker run -it --shm-size 1GB --rm --name cyclone-component-test cyclone-component-test iox-roudi
```

## Showing correct behavior with SHM disabled

First, run an example without shared memory to see the correct result.

In the second terminal window run the launch file which spawns 90 component_containers and loads a composable node into each:

```
docker exec -it --env=CYCLONEDDS_URI='<Domain id="any"><SharedMemory><Enable>false</></></>' cyclone-component-test bash -c ". /ws/install/setup.bash && ros2 launch /ws/src/composition.launch.py"
```

In the third terminal check how many component_containers were created:

```
docker exec -it cyclone-component-test bash -c "pgrep -f -c component_container"
```

You should get the number 90.

And now check how many nodes were created:

```
docker exec -it cyclone-component-test bash -c ". /ws/install/setup.bash && ros2 node list -c"
```

You should get the number 181 = 1 launch file + 90 containers + 90 composable nodes.


## Showing incorrect behavior with SHM enabled

Now abort an execution in the second terminal by Ctrl+C and run the same command enabling shared memory support:

```
docker exec -it --env=CYCLONEDDS_URI='<Domain id="any"><SharedMemory><Enable>true</></></>' cyclone-component-test bash -c ". /ws/install/setup.bash && ros2 launch /ws/src/composition.launch.py"
```

In the third terminal check how many component_containers were created:

```
docker exec -it cyclone-component-test bash -c "pgrep -f -c component_container"
```

You should again get the number 90.

And now check how many nodes were created:

```
docker exec -it cyclone-component-test bash -c ". /ws/install/setup.bash && ros2 node list -c"
```

You will probably get a number lower than 181 - not all composable nodes were loaded.

# Explanation

The issue was observed in ROS system with a few dozens of nodes. Starting the system with SHM enabled caused random nodes to not being loaded.

This repository contains a minimal example which demonstrates the issue using the standard Iceoryx compilation. As far as I tested, the type of composable node loaded doesn't matter, however in this repository the composable node with the /parameter_events publisher disabled is used so a large number of nodes can be spawned without triggering the https://github.com/eclipse-cyclonedds/cyclonedds/issues/1326#issuecomment-1181699596 issue.

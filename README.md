# Build the image

```docker build -t ros_app . ```

# Run the image

```docker-compose up ```

# Open a shell in a running image (do this a new terminal window)

``` docker exec -it ros_app_container bash```

## If you want to run a catkin_make with this shell, you will need to re-source ros before (there is no .bashrc in docker) with this command:

```source /opt/ros/noetic/setup.bash```
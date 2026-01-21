docker build -t ros_project .
docker run -it --rm --net=host --privileged --env="DISPLAY" --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" -v "$(pwd):/src" ros_project bash
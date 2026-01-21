docker build -t camera_subscriber .
docker run -it --rm --net=host --privileged --env="DISPLAY" --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" -v "$(pwd):/src" camera_subscriber bash
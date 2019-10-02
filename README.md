# rs_d435i

### realsense driver installation
- offical url: https://github.com/IntelRealSense/librealsense/blob/master/doc/installation.md

### realsense ros package installation
- offical url: https://github.com/IntelRealSense/librealsense/blob/master/doc/distribution_linux.md#installing-the-packages

### Environment setting
- Change the path of the following files: 
    * get_rs_image/scripts/get_rs_image.Get_Image.py
    * rs_d435i/test_rs_img/scripts/get_rs_module_img.py
- Change this: sys.path.insert(1, "/home/<your_pc_name>/.local/lib/python3.5/site-packages/")
- python may be different for different pc, please check your path

### Display image from d435i by using ros
```  
cd src/rs_d435i/
source create_catkin_ws.sh
cd ../..
. /devel/setup.bash
roslaunch realsense2_camera rs_rgbd.launch
```

open new terminal

```
. /devel/setup.bash 
. ../catkin_workspace/install/setup.bash --extend
rosrun test_rs_img get_rs_module_img.py
```
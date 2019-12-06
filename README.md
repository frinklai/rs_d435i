# rs_d435i

### realsense driver installation
- offical url: https://github.com/IntelRealSense/librealsense/blob/master/doc/installation.md

### realsense ros package installation
- offical url: https://github.com/IntelRealSense/librealsense/blob/master/doc/distribution_linux.md#installing-the-packages

### Environment setting
- Change the path of the following files: 
    * file1: get_rs_image/scripts/get_rs_image.Get_Image.py
    * file2: rs_d435i/test_rs_img/scripts/get_rs_module_img.py
- Change this: sys.path.insert(1, "/home/<your_pc_name>/.local/lib/python3.5/site-packages/")
    * Do change in file1 and file2
- Change this: sys.path.insert(2, "/home/<your_pc_name>/<your_workspace_name>/catkin_workspace/install/lib/python3/dist-packages")
    * Do change only in file2
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
rosrun test_rs_img get_rs_module_img.py
```
project(linear-filtering)
cmake_minimum_required(VERSION 2.8)

aux_source_directory(. SRC_LIST)
add_executable(${PROJECT_NAME} ${SRC_LIST})

target_link_libraries(${PROJECT_NAME} opencv_core opencv_highgui opencv_imgcodecs opencv_imgproc)

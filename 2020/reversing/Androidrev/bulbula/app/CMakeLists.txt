cmake_minimum_required(VERSION 3.4.1)

set(SOURCE_FILES
        src/main/cpp/scorechecker.cpp
        )

include_directories(src/main/cpp)

add_library(scorechecker SHARED
        ${SOURCE_FILES})


find_package(SWIG REQUIRED)
include(${SWIG_USE_FILE})


# Include libraries needed for scorechecker lib
target_link_libraries(scorechecker
                      android
                      log)

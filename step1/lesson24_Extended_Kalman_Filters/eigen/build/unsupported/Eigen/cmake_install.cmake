# Install script for directory: /home/leon/work/myHub/udacity-project/step1/lesson24_Extended_Kalman_Filters/eigen/unsupported/Eigen

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/usr/local")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "Release")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Devel")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/eigen3/unsupported/Eigen" TYPE FILE FILES
    "/home/leon/work/myHub/udacity-project/step1/lesson24_Extended_Kalman_Filters/eigen/unsupported/Eigen/AdolcForward"
    "/home/leon/work/myHub/udacity-project/step1/lesson24_Extended_Kalman_Filters/eigen/unsupported/Eigen/AlignedVector3"
    "/home/leon/work/myHub/udacity-project/step1/lesson24_Extended_Kalman_Filters/eigen/unsupported/Eigen/ArpackSupport"
    "/home/leon/work/myHub/udacity-project/step1/lesson24_Extended_Kalman_Filters/eigen/unsupported/Eigen/AutoDiff"
    "/home/leon/work/myHub/udacity-project/step1/lesson24_Extended_Kalman_Filters/eigen/unsupported/Eigen/BVH"
    "/home/leon/work/myHub/udacity-project/step1/lesson24_Extended_Kalman_Filters/eigen/unsupported/Eigen/EulerAngles"
    "/home/leon/work/myHub/udacity-project/step1/lesson24_Extended_Kalman_Filters/eigen/unsupported/Eigen/FFT"
    "/home/leon/work/myHub/udacity-project/step1/lesson24_Extended_Kalman_Filters/eigen/unsupported/Eigen/IterativeSolvers"
    "/home/leon/work/myHub/udacity-project/step1/lesson24_Extended_Kalman_Filters/eigen/unsupported/Eigen/KroneckerProduct"
    "/home/leon/work/myHub/udacity-project/step1/lesson24_Extended_Kalman_Filters/eigen/unsupported/Eigen/LevenbergMarquardt"
    "/home/leon/work/myHub/udacity-project/step1/lesson24_Extended_Kalman_Filters/eigen/unsupported/Eigen/MatrixFunctions"
    "/home/leon/work/myHub/udacity-project/step1/lesson24_Extended_Kalman_Filters/eigen/unsupported/Eigen/MoreVectorization"
    "/home/leon/work/myHub/udacity-project/step1/lesson24_Extended_Kalman_Filters/eigen/unsupported/Eigen/MPRealSupport"
    "/home/leon/work/myHub/udacity-project/step1/lesson24_Extended_Kalman_Filters/eigen/unsupported/Eigen/NonLinearOptimization"
    "/home/leon/work/myHub/udacity-project/step1/lesson24_Extended_Kalman_Filters/eigen/unsupported/Eigen/NumericalDiff"
    "/home/leon/work/myHub/udacity-project/step1/lesson24_Extended_Kalman_Filters/eigen/unsupported/Eigen/OpenGLSupport"
    "/home/leon/work/myHub/udacity-project/step1/lesson24_Extended_Kalman_Filters/eigen/unsupported/Eigen/Polynomials"
    "/home/leon/work/myHub/udacity-project/step1/lesson24_Extended_Kalman_Filters/eigen/unsupported/Eigen/Skyline"
    "/home/leon/work/myHub/udacity-project/step1/lesson24_Extended_Kalman_Filters/eigen/unsupported/Eigen/SparseExtra"
    "/home/leon/work/myHub/udacity-project/step1/lesson24_Extended_Kalman_Filters/eigen/unsupported/Eigen/SpecialFunctions"
    "/home/leon/work/myHub/udacity-project/step1/lesson24_Extended_Kalman_Filters/eigen/unsupported/Eigen/Splines"
    )
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Devel")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/eigen3/unsupported/Eigen" TYPE DIRECTORY FILES "/home/leon/work/myHub/udacity-project/step1/lesson24_Extended_Kalman_Filters/eigen/unsupported/Eigen/src" FILES_MATCHING REGEX "/[^/]*\\.h$")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for each subdirectory.
  include("/home/leon/work/myHub/udacity-project/step1/lesson24_Extended_Kalman_Filters/eigen/build/unsupported/Eigen/CXX11/cmake_install.cmake")

endif()


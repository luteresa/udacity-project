# Install script for directory: /home/leon/work/myHub/udacity-project/step1/lesson24_Extended_Kalman_Filters/eigen/Eigen

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
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/eigen3/Eigen" TYPE FILE FILES
    "/home/leon/work/myHub/udacity-project/step1/lesson24_Extended_Kalman_Filters/eigen/Eigen/CholmodSupport"
    "/home/leon/work/myHub/udacity-project/step1/lesson24_Extended_Kalman_Filters/eigen/Eigen/OrderingMethods"
    "/home/leon/work/myHub/udacity-project/step1/lesson24_Extended_Kalman_Filters/eigen/Eigen/Core"
    "/home/leon/work/myHub/udacity-project/step1/lesson24_Extended_Kalman_Filters/eigen/Eigen/StdList"
    "/home/leon/work/myHub/udacity-project/step1/lesson24_Extended_Kalman_Filters/eigen/Eigen/Jacobi"
    "/home/leon/work/myHub/udacity-project/step1/lesson24_Extended_Kalman_Filters/eigen/Eigen/Householder"
    "/home/leon/work/myHub/udacity-project/step1/lesson24_Extended_Kalman_Filters/eigen/Eigen/IterativeLinearSolvers"
    "/home/leon/work/myHub/udacity-project/step1/lesson24_Extended_Kalman_Filters/eigen/Eigen/StdDeque"
    "/home/leon/work/myHub/udacity-project/step1/lesson24_Extended_Kalman_Filters/eigen/Eigen/PaStiXSupport"
    "/home/leon/work/myHub/udacity-project/step1/lesson24_Extended_Kalman_Filters/eigen/Eigen/MetisSupport"
    "/home/leon/work/myHub/udacity-project/step1/lesson24_Extended_Kalman_Filters/eigen/Eigen/QtAlignedMalloc"
    "/home/leon/work/myHub/udacity-project/step1/lesson24_Extended_Kalman_Filters/eigen/Eigen/UmfPackSupport"
    "/home/leon/work/myHub/udacity-project/step1/lesson24_Extended_Kalman_Filters/eigen/Eigen/SparseQR"
    "/home/leon/work/myHub/udacity-project/step1/lesson24_Extended_Kalman_Filters/eigen/Eigen/SparseCore"
    "/home/leon/work/myHub/udacity-project/step1/lesson24_Extended_Kalman_Filters/eigen/Eigen/PardisoSupport"
    "/home/leon/work/myHub/udacity-project/step1/lesson24_Extended_Kalman_Filters/eigen/Eigen/StdVector"
    "/home/leon/work/myHub/udacity-project/step1/lesson24_Extended_Kalman_Filters/eigen/Eigen/SparseLU"
    "/home/leon/work/myHub/udacity-project/step1/lesson24_Extended_Kalman_Filters/eigen/Eigen/Cholesky"
    "/home/leon/work/myHub/udacity-project/step1/lesson24_Extended_Kalman_Filters/eigen/Eigen/SparseCholesky"
    "/home/leon/work/myHub/udacity-project/step1/lesson24_Extended_Kalman_Filters/eigen/Eigen/Geometry"
    "/home/leon/work/myHub/udacity-project/step1/lesson24_Extended_Kalman_Filters/eigen/Eigen/LU"
    "/home/leon/work/myHub/udacity-project/step1/lesson24_Extended_Kalman_Filters/eigen/Eigen/Sparse"
    "/home/leon/work/myHub/udacity-project/step1/lesson24_Extended_Kalman_Filters/eigen/Eigen/SuperLUSupport"
    "/home/leon/work/myHub/udacity-project/step1/lesson24_Extended_Kalman_Filters/eigen/Eigen/Eigenvalues"
    "/home/leon/work/myHub/udacity-project/step1/lesson24_Extended_Kalman_Filters/eigen/Eigen/SPQRSupport"
    "/home/leon/work/myHub/udacity-project/step1/lesson24_Extended_Kalman_Filters/eigen/Eigen/Dense"
    "/home/leon/work/myHub/udacity-project/step1/lesson24_Extended_Kalman_Filters/eigen/Eigen/Eigen"
    "/home/leon/work/myHub/udacity-project/step1/lesson24_Extended_Kalman_Filters/eigen/Eigen/SVD"
    "/home/leon/work/myHub/udacity-project/step1/lesson24_Extended_Kalman_Filters/eigen/Eigen/QR"
    )
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Devel")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/eigen3/Eigen" TYPE DIRECTORY FILES "/home/leon/work/myHub/udacity-project/step1/lesson24_Extended_Kalman_Filters/eigen/Eigen/src" FILES_MATCHING REGEX "/[^/]*\\.h$")
endif()


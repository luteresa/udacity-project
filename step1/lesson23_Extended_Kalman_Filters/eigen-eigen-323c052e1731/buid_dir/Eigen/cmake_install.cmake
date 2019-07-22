# Install script for directory: /home/leon/work/myHub/udacity-project/step1/lesson23_Extended_Kalman_Filters/eigen-eigen-323c052e1731/Eigen

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
    "/home/leon/work/myHub/udacity-project/step1/lesson23_Extended_Kalman_Filters/eigen-eigen-323c052e1731/Eigen/MetisSupport"
    "/home/leon/work/myHub/udacity-project/step1/lesson23_Extended_Kalman_Filters/eigen-eigen-323c052e1731/Eigen/Dense"
    "/home/leon/work/myHub/udacity-project/step1/lesson23_Extended_Kalman_Filters/eigen-eigen-323c052e1731/Eigen/SVD"
    "/home/leon/work/myHub/udacity-project/step1/lesson23_Extended_Kalman_Filters/eigen-eigen-323c052e1731/Eigen/Eigen"
    "/home/leon/work/myHub/udacity-project/step1/lesson23_Extended_Kalman_Filters/eigen-eigen-323c052e1731/Eigen/StdVector"
    "/home/leon/work/myHub/udacity-project/step1/lesson23_Extended_Kalman_Filters/eigen-eigen-323c052e1731/Eigen/Cholesky"
    "/home/leon/work/myHub/udacity-project/step1/lesson23_Extended_Kalman_Filters/eigen-eigen-323c052e1731/Eigen/Core"
    "/home/leon/work/myHub/udacity-project/step1/lesson23_Extended_Kalman_Filters/eigen-eigen-323c052e1731/Eigen/UmfPackSupport"
    "/home/leon/work/myHub/udacity-project/step1/lesson23_Extended_Kalman_Filters/eigen-eigen-323c052e1731/Eigen/StdDeque"
    "/home/leon/work/myHub/udacity-project/step1/lesson23_Extended_Kalman_Filters/eigen-eigen-323c052e1731/Eigen/Eigenvalues"
    "/home/leon/work/myHub/udacity-project/step1/lesson23_Extended_Kalman_Filters/eigen-eigen-323c052e1731/Eigen/PardisoSupport"
    "/home/leon/work/myHub/udacity-project/step1/lesson23_Extended_Kalman_Filters/eigen-eigen-323c052e1731/Eigen/LU"
    "/home/leon/work/myHub/udacity-project/step1/lesson23_Extended_Kalman_Filters/eigen-eigen-323c052e1731/Eigen/StdList"
    "/home/leon/work/myHub/udacity-project/step1/lesson23_Extended_Kalman_Filters/eigen-eigen-323c052e1731/Eigen/QtAlignedMalloc"
    "/home/leon/work/myHub/udacity-project/step1/lesson23_Extended_Kalman_Filters/eigen-eigen-323c052e1731/Eigen/OrderingMethods"
    "/home/leon/work/myHub/udacity-project/step1/lesson23_Extended_Kalman_Filters/eigen-eigen-323c052e1731/Eigen/IterativeLinearSolvers"
    "/home/leon/work/myHub/udacity-project/step1/lesson23_Extended_Kalman_Filters/eigen-eigen-323c052e1731/Eigen/SuperLUSupport"
    "/home/leon/work/myHub/udacity-project/step1/lesson23_Extended_Kalman_Filters/eigen-eigen-323c052e1731/Eigen/Geometry"
    "/home/leon/work/myHub/udacity-project/step1/lesson23_Extended_Kalman_Filters/eigen-eigen-323c052e1731/Eigen/PaStiXSupport"
    "/home/leon/work/myHub/udacity-project/step1/lesson23_Extended_Kalman_Filters/eigen-eigen-323c052e1731/Eigen/Householder"
    "/home/leon/work/myHub/udacity-project/step1/lesson23_Extended_Kalman_Filters/eigen-eigen-323c052e1731/Eigen/Sparse"
    "/home/leon/work/myHub/udacity-project/step1/lesson23_Extended_Kalman_Filters/eigen-eigen-323c052e1731/Eigen/SparseCholesky"
    "/home/leon/work/myHub/udacity-project/step1/lesson23_Extended_Kalman_Filters/eigen-eigen-323c052e1731/Eigen/CholmodSupport"
    "/home/leon/work/myHub/udacity-project/step1/lesson23_Extended_Kalman_Filters/eigen-eigen-323c052e1731/Eigen/SparseCore"
    "/home/leon/work/myHub/udacity-project/step1/lesson23_Extended_Kalman_Filters/eigen-eigen-323c052e1731/Eigen/QR"
    "/home/leon/work/myHub/udacity-project/step1/lesson23_Extended_Kalman_Filters/eigen-eigen-323c052e1731/Eigen/SparseLU"
    "/home/leon/work/myHub/udacity-project/step1/lesson23_Extended_Kalman_Filters/eigen-eigen-323c052e1731/Eigen/SPQRSupport"
    "/home/leon/work/myHub/udacity-project/step1/lesson23_Extended_Kalman_Filters/eigen-eigen-323c052e1731/Eigen/Jacobi"
    "/home/leon/work/myHub/udacity-project/step1/lesson23_Extended_Kalman_Filters/eigen-eigen-323c052e1731/Eigen/SparseQR"
    )
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Devel")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/eigen3/Eigen" TYPE DIRECTORY FILES "/home/leon/work/myHub/udacity-project/step1/lesson23_Extended_Kalman_Filters/eigen-eigen-323c052e1731/Eigen/src" FILES_MATCHING REGEX "/[^/]*\\.h$")
endif()


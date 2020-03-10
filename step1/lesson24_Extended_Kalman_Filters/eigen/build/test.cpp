#include <iostream>
#include <vector>
#include "Eigen/Dense"
 
using std::cout;
using std::endl;
using std::vector;
using Eigen::VectorXd;
using Eigen::MatrixXd;
 
// Kalman Filter variables
VectorXd x;	// object state
MatrixXd P;	// object covariance matrix
int main() {
	/**
	* Code used as example to work with Eigen matrices
	*/
	// design the KF with 1D motion
	x = VectorXd(2);
	x << 0, 0;
	std::cout<<"Matrix x:\n"<<x<<std::endl;
 
	P = MatrixXd(2, 2);
	P << 1000, 0, 0, 1000;
	std::cout<<"Matrix P:\n"<<P<<std::endl;
}

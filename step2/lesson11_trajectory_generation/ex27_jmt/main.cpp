#include <cmath>
#include <iostream>
#include <vector>


#include "grader.h"
#include "Eigen/Dense"


using std::vector;
using Eigen::MatrixXd;
using Eigen::VectorXd;

/**
 * TODO: complete this function
 */
vector<double> JMT(vector<double> &start, vector<double> &end, double T) {
  /**
   * Calculate the Jerk Minimizing Trajectory that connects the initial state
   * to the final state in time T.
   *
   * @param start - the vehicles start location given as a length three array
   *   corresponding to initial values of [s, s_dot, s_double_dot]
   * @param end - the desired end state for vehicle. Like "start" this is a
   *   length three array.
   * @param T - The duration, in seconds, over which this maneuver should occur.
   *
   * @output an array of length 6, each value corresponding to a coefficent in 
   *   the polynomial:
   *   s(t) = a_0 + a_1 * t + a_2 * t**2 + a_3 * t**3 + a_4 * t**4 + a_5 * t**5
   *
   * EXAMPLE
   *   > JMT([0, 10, 0], [10, 10, 0], 1)
   *     [0.0, 10.0, 0.0, 0.0, 0.0, 0.0]
   */
	MatrixXd A = MatrixXd(3,3);
	auto T2 = T*T;
  	auto T3 = T2*T;
	auto T4 = T2*T2;
	auto T5 = T3*T2;
	A << T3,T4,T5,
		3*T2,4*T3,5*T4,
		6*T, 12*T2,20*T3;
  	MatrixXd B = MatrixXd(3,1);
  	B << end[0] - (start[0] + start[1]*T + 0.5*start[2]*T2),
  	end[1] - (start[1] + start[2]*T),
  	end[2] - start[2];

	MatrixXd Ai = A.inverse();

	MatrixXd C = Ai*B;

  	vector<double> result = {start[0],start[1],0.5*start[2]};

	for (int i = 0; i < C.size(); i++) {
		result.push_back(C.data()[i]);
	}

	return result;
}


int main() {

  // create test cases
  vector< test_case > tc = create_tests();

  bool total_correct = true;

  for(int i = 0; i < tc.size(); ++i) {
    vector<double> jmt = JMT(tc[i].start, tc[i].end, tc[i].T);
    bool correct = close_enough(jmt, answers[i]);
    total_correct &= correct;

	std::cout<<"jmt,"<<i<<":"<<jmt[0]<<","<<jmt[1]<<","<<jmt[2]<<","<<jmt[3]<<","<<jmt[4]<<","<<jmt[5]<<","<<std::endl;
	std::cout<<"answers,"<<i<<":"<<answers[i][0]<<","<<answers[i][1]<<","<<answers[i][2]<<","<<answers[i][3]<<","<<answers[i][4]<<","<<answers[i][5]<<","<<std::endl;
  }

  if(!total_correct) {
    std::cout << "Try again!" << std::endl;
  } else {
    std::cout << "Nice work!" << std::endl;
  }

  return 0;
}

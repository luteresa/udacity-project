#include <iostream>
#include <vector>

using std::vector;

// initialize priors assuming vehicle at landmark +/- 1.0 meters position stdev
vector<float> initialize_priors(int map_size, vector<float> landmark_positions,
                                float position_stdev);

int main() {
  // set standard deviation of position
  float position_stdev = 1.0f;

  // set map horizon distance in meters 
  int map_size = 25;

  // initialize landmarks
  vector<float> landmark_positions {5, 10, 20};

  // initialize priors
  vector<float> priors = initialize_priors(map_size, landmark_positions,
                                           position_stdev);

  // print values to stdout 
  for (int p = 0; p < priors.size(); ++p) {
    std::cout << priors[p] << std::endl;
  }

  return 0;
}

// TODO: Complete the initialize_priors function
vector<float> initialize_priors(int map_size, vector<float> landmark_positions,
                                float position_stdev) {

  // initialize priors assuming vehicle at landmark +/- 1.0 meters position stdev

  // set all priors to 0.0
  vector<float> priors(map_size, 0.0);
    
  // TODO: YOUR CODE HERE
  float landmark_count = landmark_positions.size();
  landmark_count *= (1+2*position_stdev);
  float prob = 1.0/landmark_count;
  
  for (int i=0;i < landmark_positions.size();i++) 
  {
      for (int j=1; j<=position_stdev;j++)
      {
          priors[((int)(landmark_positions[i]-j+map_size))%map_size] = prob;
          priors[((int)(landmark_positions[i]+j+map_size))%map_size] = prob;
      }
      priors[(int)(landmark_positions[i])] = prob;
  }


  return priors;
}


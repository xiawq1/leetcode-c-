#include <iostream>
#include <time.h>
#include <string>
#include <opencv2/opencv.hpp>        //opencv库
#include "network.h"
using namespace std;
using namespace cv;

void saveWeight(string file, Network *network){   //保存各层权重到文件
  ofstream outfile(file);
  for (int i = 0; i < network-> mNumLayers; i++){
    Layer *layer = network->mLayers[i];
  }

}

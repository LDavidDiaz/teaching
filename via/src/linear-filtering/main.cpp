#include <opencv2/core.hpp>
#include <opencv2/highgui.hpp>
#include <opencv2/imgproc.hpp>

using namespace ::cv;
using namespace ::std;

int main(int argc, char* argv[])
{
    string filename = argv[1];

    Mat in = imread(filename, CV_LOAD_IMAGE_GRAYSCALE);

    Mat kernel = (Mat_<float>(3, 3) << -1, 0, 1,
                                       -2, 0, 2,
                                       -1, 0, 1);
    kernel *= 1.0 / 8.0;

    Mat out;
    filter2D(in, out, -1, kernel);

    const string in_window = "Input";
    const string out_window = "Output";

    imshow(in_window, in);
    imshow(out_window, out);

    moveWindow(in_window, 0, 0);
    moveWindow(out_window, in.cols, 0);

    waitKey();
}

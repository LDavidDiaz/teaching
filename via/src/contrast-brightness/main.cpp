#include <opencv2/core.hpp>
#include <opencv2/highgui.hpp>

using namespace ::cv;
using namespace ::std;

Mat ApplyContrastAndBrightness(const Mat& in,
                               const float& scale,
                               const float& offset) {
    Mat out(in.size(), CV_8U);

    for (int i = 0; i < in.rows; ++i) {
        for (int j = 0; j < in.cols; ++j) {
            float tmp = scale * in.at<unsigned char>(i, j) + offset;
            if (tmp < 255.0) {
                out.at<unsigned char>(i, j) = static_cast<int>(tmp);
            } else {
                out.at<unsigned char>(i, j) = 255;
            }
        }
    }

    return out;
}

int main(int argc, char* argv[])
{
    string filename = argv[1];
    float scale = atof(argv[2]);
    float offset = atof(argv[3]);

    Mat in = imread(filename, IMREAD_GRAYSCALE);

    Mat out = ApplyContrastAndBrightness(in, scale, offset);

    const string in_window = "Input";
    const string out_window = "Output";

    imshow(in_window, in);
    imshow(out_window, out);

    moveWindow(in_window, 0, 0);
    moveWindow(out_window, in.cols, 0);

    waitKey();
}

#include <iostream>

#include <opencv2/highgui/highgui.hpp>
#include <opencv2/imgproc/imgproc.hpp>

using namespace ::cv;
using namespace ::std;

Mat PlotHistogram(
	const Mat& histogram,
	const int& num_bins,
	const int& width,
	const int& height,
	const Scalar& background_color = Scalar(255, 255, 255),
	const Scalar& line_color = Scalar(0, 0, 0),
	const int& line_thickness = 3,
	const int& line_type = CV_AA) {
	const int bin_width = static_cast<int>(round(static_cast<double>(width) / num_bins));

	Mat canvas(height, width, CV_8UC3, background_color);

	Mat histogram_normalized;
	normalize(histogram, histogram_normalized, 0, canvas.rows, NORM_MINMAX, -1, Mat());

	const int shift = 0;
	for (int i = 1; i < num_bins; ++i) {
		int x0 = (i - 1) * bin_width;
		int x1 = i * bin_width;
		int y0 = height - static_cast<int>(round(histogram_normalized.at<float>(i - 1)));
		int y1 = height - static_cast<int>(round(histogram_normalized.at<float>(i)));

		line(canvas, Point(x0, y0), Point(x1, y1), line_color, line_thickness, line_type, shift);
	}

	return canvas;
}

int hist_w = 512; int hist_h = 400;

int main(int argc, char* argv[]) {
	string filename = argv[1];

	Mat in = imread(filename, IMREAD_GRAYSCALE);

	Mat histogram;
	float range[] = { 0, 256 };
	const float* histogram_range = { range };
	bool uniform_flag = true;
	bool accumulate_flag = false;
	int num_bins = 256;
	calcHist(&in, 1, NULL, Mat(), histogram, 1, &num_bins, &histogram_range, uniform_flag, accumulate_flag);

	const int height = in.rows;
	const int width = static_cast<int>(round(((1.0 + sqrt(5)) / 2.0) * height));
	Mat out = PlotHistogram(histogram, num_bins, width, height);

	const string in_window = "Input";
	const string out_window = "Output";

	imshow(in_window, in);
	imshow(out_window, out);

	moveWindow(in_window, 0, 0);
	moveWindow(out_window, in.cols, 0);

	waitKey();
}


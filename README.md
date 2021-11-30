Libraries Used
cv2 for feature extraction
g2opy for optimization (soon!)

Rendered Scene Test

./ma.py

NOTE: The test currently doesn't work reliably. It seems adding a small amount of Gaussian noise to the point positions can cause the optimizer to fall into really bad local minima. This may just be caused by poor initialization, as I'm not sure how stable Essential matricies are.


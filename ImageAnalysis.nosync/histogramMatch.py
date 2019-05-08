import numpy as np
"""
Histogram matching function.  This function is used to take a source image and template
image, from which there histograms will be matched. 

This function hist_match is being used from [1] “numpy - Histogram matching of two images 
in Python 2.x? - Stack Overflow.” [Online]. 
Available: 
https://stackoverflow.com/questions/32655686/histogram-matching-of-two-images-in-python-2-x. 
[Accessed: 19-Mar-2019].
Modifications by Neil Houston 
"""

def hist_match(source, template):
    """
    Adjust the pixel values of an image such that its histogram
    matches that of a target image. 

    Arguments:
    -----------
        source: np.ndarray
            Image to transform; the histogram is computed over the flattened
            array
        template: np.ndarray
            Template image; can have different dimensions to source
    Returns:
    -----------
        matched: np.ndarray
            The transformed output image the same shape as the source image and of
            type np.uint8 to match that of the source
    """

    oldshape = source.shape
    source = source.ravel()
    template = template.ravel()

    # Get the set of unique pixel values and their corresponding indices and counts
    s_values, bin_idx, s_counts = np.unique(source, return_inverse=True, return_counts=True)
    t_values, t_counts = np.unique(template, return_counts=True)

    # Take the cumsum of the counts and normalize by the number of pixels to get the 
    # empirical cumulative distribution functions for the source and template 
    # images (maps pixel value --> quantile)
    s_quantiles = np.cumsum(s_counts).astype(np.float64)
    s_quantiles /= s_quantiles[-1]
    t_quantiles = np.cumsum(t_counts).astype(np.float64)
    t_quantiles /= t_quantiles[-1]

    # Interpolate linearly to find the pixel values in the template image that correspond 
    # most closely to the quantiles in the source image
    interp_t_values = np.interp(s_quantiles, t_quantiles, t_values)

    return interp_t_values[bin_idx].reshape(oldshape).astype(np.uint8)
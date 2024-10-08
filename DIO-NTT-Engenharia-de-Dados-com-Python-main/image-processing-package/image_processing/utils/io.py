from skimage.io import imread, imsave

def read_img(path, is_gray = False):
    img = imread(path, as_gray = is_gray)
    return img

def save_img(img, path):
    imsave(path, img)
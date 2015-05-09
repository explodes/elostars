from __future__ import division

import sys

try:
    import cv
except ImportError:
    cv = None
from django.conf import settings
from PIL import Image


def DetectFace(image, faceCascade):
    # This function takes a grey scale cv image and finds
    # the patterns defined in the haarcascade function
    # modified from: http://www.lucaamore.com/?p=638

    # variables
    min_size = (20, 20)
    haar_scale = 1.1
    min_neighbors = 3
    haar_flags = 0

    # Equalize the histogram
    cv.EqualizeHist(image, image)

    # Detect the faces
    faces = cv.HaarDetectObjects(
        image, faceCascade, cv.CreateMemStorage(0),
        haar_scale, min_neighbors, haar_flags, min_size
    )

    # If faces are found
    if faces:
        return faces[0]


def pil2cvGrey(pil_im):
    # Convert a PIL image to a greyscale cv image
    # from: http://pythonpath.wordpress.com/2012/05/08/pil-to-opencv-image/
    pil_im = pil_im.convert('L')
    cv_im = cv.CreateImageHeader(pil_im.size, cv.IPL_DEPTH_8U, 1)
    cv.SetData(cv_im, pil_im.tostring(), pil_im.size[0])
    return cv_im


def cv2pil(cv_im):
    # Convert the cv image to a PIL image
    return Image.frombytes("L", cv.GetSize(cv_im), cv_im.tostring())


def imgCrop(image, cropBox, boxScale=1.0):
    # Crop a PIL image with the provided box [x(left), y(upper), w(width), h(height)]

    iw, ih = image.size
    x0, y0, w, h = cropBox

    dx = 0.5 * w * boxScale
    dy = 0.5 * w * boxScale

    x0 -= dx
    y0 -= dy

    x1 = x0 + w + 2 * dx
    y1 = y0 + h + 2 * dx

    # Convert cv box to PIL box [left, upper, right, lower]
    PIL_box = map(int, [max(0, x0),
               max(0, y0),
               min(iw, x1),
               min(ih, y1)])

    print dx
    print dy
    print cropBox
    print PIL_box

    crop = image.crop(PIL_box)

    return crop


def detect_face(image):
    """
    Attempt to detect a face in a PIL image.

    Returns the coordinates (0-1, 0-1) of the center of the detected face.
    Returns None if CV is not available.
    Returns None if no faces are found.

    :param image: PIL Image
    """

    if cv is None:
        return None

    cv_im = pil2cvGrey(image)
    try:
        faceCascade = cv.Load(settings.FACE_DETECTION_CASCADE)
    except TypeError as e:
        print >> sys.stdout, "%s" % e
        return None

    face = DetectFace(cv_im, faceCascade)
    if face:
        return imgCrop(image, face[0], boxScale=1.5)

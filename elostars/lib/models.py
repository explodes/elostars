import os

from django.db import models
from PIL import Image, ImageOps


class AutoImageSizingModel(models.Model):
    class Meta:
        abstract = True

    def source_photo(self):
        return self.image

    def upload_to(self):
        return 'images'

    def save_type(self):
        return ("jpg", "JPEG")

    def image_sizes(self):
        # ((prop, (width, height)), ...)
        return ()

    def save(self, *args, **kwargs):
        super(AutoImageSizingModel, self).save(*args, **kwargs)
        photo = self.source_photo()
        if photo:
            # this returns the full system path to the original file
            photopath = str(photo.path)

            # pull a few variables out of that full path
            filename = photopath.rsplit(os.sep, 1)[1].rsplit('.', 1)[0]
            fullpath = photopath.rsplit(os.sep, 1)[0]

            # open the image using PIL
            image = Image.open(photopath)

            save_ext, save_type = self.save_type()

            for key, size in self.image_sizes():
                thumb = ImageOps.fit(image, size, Image.ANTIALIAS)
                outname = '%s_%sx%s.%s' % (filename, size[0], size[1], save_ext)
                outpath = '%s%s%s' % (fullpath, os.sep, outname)
                thumb.save(outpath, save_type)
                result = "%s/%s" % (self.upload_to(), outname)
                setattr(self, key, result)
        else:
            for key, size in self.image_sizes():
                setattr(self, key, None)
        super(AutoImageSizingModel, self).save(*args, **kwargs)

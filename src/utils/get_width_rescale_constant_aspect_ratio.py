
from PIL import Image
from numpy import ndarray


def get_width_rescale_constant_aspect_ratio(
        image: Image,
        new_height_px: int,
) -> int:

    if issubclass(type(image), Image.Image):
        new_width_px = int(new_height_px / image.height * image.width)

    elif type(image) is ndarray:
        new_width_px = int(new_height_px / image.shape[1] * image.shape[0])
        print(new_width_px)

    else:
        raise TypeError(f'Unknown type of image: {type(image)}')

    return new_width_px

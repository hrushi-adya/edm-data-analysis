from PIL import Image, ImageFile
from io import BytesIO
import requests

def create_images_list(images: list) -> list:
    final_images = []
    for l in images:
        l_str = [str(ll) for ll in l]
        for individual_str in l_str:
            final_images.append(individual_str.split('\n'))

    return final_images

def load_image(url_or_path):
        try:
            # If url_or_path is a tuple, extract the first element
            if isinstance(url_or_path, tuple):
                url_or_path = url_or_path[0]

            url_or_path = url_or_path.strip()  # Clean up any extra whitespace or newlines
            print("TYPE OF url_or_path:", type(url_or_path))
            print("URL_OR_PATH:", url_or_path)

            if isinstance(url_or_path, str) and (url_or_path.startswith("http://") or url_or_path.startswith("https://")) and (url_or_path.endswith(".png") or url_or_path.endswith(".jpg") or url_or_path.endswith(".jpeg")):
                # return Image.open(requests.get(url_or_path, stream=True).raw)
                response = requests.get(url_or_path)
                image = Image.open(BytesIO(response.content)).convert('RGB')
                return image
        except Exception as e:
            print(f"error while opening file: {e}")
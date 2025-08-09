import base64
from io import BytesIO

def jpg_to_base64(pil_image):
    """
    Convert PIL images to Base64 encoded strings

    :param pil_image: PIL image
    :return: Re-sized Base64 string
    """

    buffered = BytesIO()
    pil_image.save(buffered, format="JPEG")  # You can change the format if needed
    img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")
    return img_str

def png_to_base64(pil_image):
    """
    Convert PIL images to Base64 encoded strings

    :param pil_image: PIL image
    :return: Re-sized Base64 string
    """

    buffered = BytesIO()
    pil_image.save(buffered, format="PNG")  # You can change the format if needed
    img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")
    return img_str

def bind_image_to_llm(image_input, llm):
    """
    Bind one or more base64-encoded images to an LLM.

    Args:
        image_input (str | list[str]): A single base64 image string or a list of them.
        llm: The language model instance (e.g., OllamaLLM).

    Returns:
        llm_with_image: LLM bound with provided images.
    """
    if isinstance(image_input, str):
        images = [image_input]
    elif isinstance(image_input, list) and all(isinstance(i, str) for i in image_input):
        images = image_input
    else:
        raise TypeError("image_input must be a base64 string or a list of base64 strings")

    return llm.bind(images=images)
# Helper functions for working with langchain

`png_to_base64(pil_image)` - converts a pil image to base64 to be used with a model

`jpg_to_base64(pil_image)` - converts a pil image to base64 to be used with a model

`bind_image_to_llm(image_b64, llm)` - binds a base64 encoded image to an llm and returns the llm to be used for queries
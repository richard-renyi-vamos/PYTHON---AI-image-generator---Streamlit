import streamlit as st
import requests
from PIL import Image
from io import BytesIO

# A placeholder function to call AI model API (e.g., DALL·E or any image generation API)
def generate_image_from_api(prompt):
    # Here you'd call your API. This is just a placeholder function.
    # For example, to use OpenAI's API, you'd do something like:
    # response = requests.post(API_URL, headers=headers, json={"prompt": prompt})
    # image_data = response.content
    # For now, let's return a placeholder image from an online source.
    response = requests.get("https://placekitten.com/800/600")  # Placeholder image URL
    return Image.open(BytesIO(response.content))

# Streamlit Web App
st.title("Mini AI Image Generator App")

# User input for image generation prompt
prompt = st.text_input("Enter an image description", "")

if st.button("Generate Image"):
    if prompt:
        with st.spinner("Generating..."):
            try:
                # Call the placeholder API function
                image = generate_image_from_api(prompt)
                st.image(image, caption="Generated Image", use_column_width=True)
            except Exception as e:
                st.error(f"Error: {str(e)}")
    else:
        st.warning("Please enter a description before generating.")

# Option to download the image
if st.button("Download Image"):
    if prompt:
        try:
            # Re-generate the image (normally you'd save the generated image previously)
            image = generate_image_from_api(prompt)
            img_buffer = BytesIO()
            image.save(img_buffer, format='PNG')
            img_buffer.seek(0)
            st.download_button(label="Download Image", data=img_buffer, file_name="generated_image.png")
        except Exception as e:
            st.error(f"Error: {str(e)}")

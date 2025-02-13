import streamlit as st

# Set page configuration for wide layout (must be the first Streamlit command)
st.set_page_config(layout="wide")

# List of image paths
image_paths = [
    "1.jpg",
    "2.jpg",
    "3.jpg",
    "4.jpg",
    "5.jpg",
    "6.jpg"
]  # Update paths based on your local files

# Create a layout with columns
cols = st.columns(len(image_paths))  # Create dynamic columns based on image count

# Display images in a grid
for col, img_path in zip(cols, image_paths):
    col.image(img_path, use_container_width=True)

import streamlit as st

# Set page configuration for wide layout (must be the first Streamlit command)
st.set_page_config(page_title="Ketan ❤️ Sonam", layout="wide")

# Display the Valentine's message
st.markdown(
    """
    <div style="text-align: center; padding: 50px;">
        <h1 style="color: red;">❤️ Happy Valentine's Day ❤️</h1>
        <p style="font-size: 20px; line-height: 1.6;">
            To my Sona ,Happy 6th Valentine's today.My understanding and loving wife,meeting you was the best thing that ever happened to me.
        </p>
        <p style="font-size: 20px; line-height: 1.6;">
            You're also my best friend to which i can share all my feelings(sometimes anger too :D) without any filters. 
            And now this year, we've our own cute gapdu to celebrate the valentine with us.Seeing you with our gapdu
            fills me more with love for you. Thank you this cute little teddy as valentine gift and taking care of me and gapdu shows just how awesome you truly are.
        </p>
        <p style="font-size: 20px; line-height: 1.6;">
            I love you.Our love story is just getting started, and I promise to love you every single day, now and always.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)
# List of image paths
image_paths = [
    "1.JPG",
    "2.jpg",
    "3.jpg",
    "4.jpg",
    "5.jpg",
    "6.jpg",
     "7.jpg"
]  # Update paths based on your local files

# Create a layout with columns
cols = st.columns(len(image_paths))  # Create dynamic columns based on image count

# Display images in a grid
for col, img_path in zip(cols, image_paths):
    col.image(img_path, use_container_width=True)




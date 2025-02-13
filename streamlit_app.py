import streamlit as st

# Set page configuration for wide layout (must be the first Streamlit command)
st.set_page_config(layout="wide")

# Display the Valentine's message
st.markdown(
    """
    <div style="text-align: center; padding: 50px;">
        <h1 style="color: red;">❤️ Happy Valentine's Day ❤️</h1>
        <p style="font-size: 20px; line-height: 1.6;">
            Four years ago, we began this beautiful journey together, stepping into an arranged marriage with hopes, dreams, 
            and a promise to build a life filled with love and understanding. Looking back, I can say with all my heart that 
            meeting you was the best thing that ever happened to me.
        </p>
        <p style="font-size: 20px; line-height: 1.6;">
            From the moment we became husband and wife, you have been my strength, my peace, and my greatest blessing. 
            And this year, as we hold our little bundle of joy in our arms, my love for you has only deepened. Seeing you as a mother 
            fills me with immense pride and admiration. The way you nurture, care, and love our baby boy shows me just how incredible you truly are.
        </p>
        <p style="font-size: 20px; line-height: 1.6;">
            You have filled our home with warmth, laughter, and unconditional love. Even on the toughest days, your presence alone 
            makes everything feel right. Every little moment—our late-night talks, the way you take care of every little detail, 
            and the smile that lights up our home—reminds me how lucky I am to have you.
        </p>
        <p style="font-size: 20px; line-height: 1.6;">
            On this special day, I just want to remind you how much I love you, how grateful I am for you, and how excited I am 
            for the beautiful future we will build together as a family. Our love story is just getting started, and I promise to cherish 
            and love you every single day, now and always.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)
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




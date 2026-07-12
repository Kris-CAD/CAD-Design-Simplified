import streamlit as st
import os

st.set_page_config(page_title="CAD Design Simplified", page_icon="📐", layout="wide")

# Channel Branding
st.title("📐 CAD Design Simplified")
st.markdown("### Interactive Tutorial Hub")
st.write("Click on any tutorial card below to download the Fusion 360 models and project resources.")
st.markdown("---")

# Folder setups
DOWNLOADS_DIR = "downloads"
IMAGES_DIR = "images"

# Make sure folders exist
for folder in [DOWNLOADS_DIR, IMAGES_DIR]:
    if not os.path.exists(folder):
        os.makedirs(folder)

# Define your video library here (Add new videos to this list)
tutorials = [
    {
        "title": "Fusion 360 Beginner Tutorial: Designing a Custom Mounting Bracket",
        "thumbnail": "images/spoon.png",  # Put your thumbnail image file name here
        "file_name": "spoon.f3d"     # Put the matching CAD file name here
    },
    {
        "title": "Advanced Sheet Metal Design Rules Explained Simply",
        "thumbnail": "images/thumbnail2.png",
        "file_name": "sheet_metal_housing.step"
    }
]

# Create an interactive grid layout (3 columns)
cols = st.columns(3)

for index, video in enumerate(tutorials):
    # This automatically distributes cards across the 3 columns
    with cols[index % 3]:
        st.markdown('<div style="border: 1px solid #e6e9ef; padding: 15px; border-radius: 10px; background-color: #ffffff;">', unsafe_allow_html=True)
        
        # 1. Display Thumbnail (handles missing image gracefully)
        if os.path.exists(video["thumbnail"]):
            st.image(video["thumbnail"], use_container_width=True)
        else:
            # Placeholder if you haven't dropped the image in yet
            st.warning(f"Drop thumbnail into: {video['thumbnail']}")
            
        # 2. Display Title
        st.markdown(f"##### {video['title']}")
        
        # 3. Handle Download Button logic
        file_path = os.path.join(DOWNLOADS_DIR, video["file_name"])
        if os.path.exists(file_path):
            with open(file_path, "rb") as file:
                st.download_button(
                    label="📥 Download CAD File",
                    data=file.read(),
                    file_name=video["file_name"],
                    mime="application/octet-stream",
                    key=f"btn_{index}",
                    use_container_width=True
                )
        else:
            st.error(f"Missing file: Place '{video['file_name']}' into downloads folder.")
            
        st.markdown('</div>', unsafe_allow_html=True)
        st.write("") # Spacer

st.markdown("---")
st.info("📺 Make sure to subscribe to **CAD Design Simplified** on YouTube for more Fusion 360 tutorials!")
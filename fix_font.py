import os
import requests

# The direct "Raw" download link for the font
FONT_URL = "https://github.com/dejavu-fonts/dejavu-fonts/raw/master/resources/ttf/DejaVuSans.ttf"
FILENAME = "DejaVuSans.ttf"

def fix_font():
    print("--- Starting Font Fixer ---")
    
    # 1. Remove old/corrupted file if it exists
    if os.path.exists(FILENAME):
        print(f"Removing existing {FILENAME}...")
        os.remove(FILENAME)

    # 2. Download the fresh file
    print(f"Downloading {FILENAME} from official source...")
    try:
        response = requests.get(FONT_URL, timeout=15)
        response.raise_for_status() # Check for download errors
        
        with open(FILENAME, "wb") as f:
            f.write(response.content)
            
        # 3. Verify Size
        size_kb = os.path.getsize(FILENAME) / 1024
        if size_kb > 700:
            print(f"✅ SUCCESS! {FILENAME} downloaded correctly.")
            print(f"Actual Size: {size_kb:.2f} KB")
            print(f"Location: {os.path.abspath(FILENAME)}")
        else:
            print(f"❌ ERROR: Downloaded file is only {size_kb:.2f} KB. It might be corrupted.")
            
    except Exception as e:
        print(f"❌ FAILED to download: {e}")

if __name__ == "__main__":
    fix_font()
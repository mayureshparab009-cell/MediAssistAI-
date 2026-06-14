import os
import zipfile

def zip_project():
    root_dir = os.path.dirname(os.path.abspath(__file__))
    zip_name = "MediAssistAI_Web.zip"
    zip_path = os.path.join(root_dir, zip_name)
    
    # Exclude files
    exclude_files = {zip_name, "zip_web.py"}
    
    print(f"Creating Web ZIP archive at: {zip_path}")
    
    count = 0
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for file in os.listdir(root_dir):
            if file in exclude_files or os.path.isdir(os.path.join(root_dir, file)):
                continue
                
            full_path = os.path.join(root_dir, file)
            zipf.write(full_path, file)
            print(f"  Added: {file}")
            count += 1
                
    print(f"Zip completed successfully! Added {count} files.")
    print(f"Saved to: {zip_path}")

if __name__ == "__main__":
    zip_project()

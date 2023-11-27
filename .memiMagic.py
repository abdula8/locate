import magic

def get_file_type(file_path):
    # mime = magic.Magic()
    # mime_type = mime.from_file(file_path)
    mime_type = magic.from_file(file_path, mime=True)
    if "audio" in mime_type:
        return "Audio"
    elif "video" in mime_type:
        return "Video"
    elif "image" in mime_type:
        return "Image"
    elif "text" in mime_type or "application/pdf" in mime_type:
        return "Document"
    else:
        return "Unknown"

# Example usage:
file_path = "path/to/your/file.pdf"
file_type = get_file_type(file_path)
print(f"File Type: {file_type}")

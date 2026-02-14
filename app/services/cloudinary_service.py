import cloudinary
import cloudinary.uploader
import os

class CloudinaryService:
    def __init__(self):
        cloudinary.config(
            cloud_name=os.getenv('CLOUDINARY_CLOUD_NAME'),
            api_key=os.getenv('CLOUDINARY_API_KEY'),
            api_secret=os.getenv('CLOUDINARY_API_SECRET')
        )
    
    def upload_image(self, file, folder='agrikonnect/products'):
        """Upload image to Cloudinary and return URL"""
        try:
            result = cloudinary.uploader.upload(
                file,
                folder=folder,
                resource_type='image',
                transformation=[
                    {'width': 800, 'height': 600, 'crop': 'limit'},
                    {'quality': 'auto'}
                ]
            )
            return result['secure_url']
        except Exception as e:
            raise Exception(f'Cloudinary upload failed: {str(e)}')
    
    def delete_image(self, public_id):
        """Delete image from Cloudinary"""
        try:
            cloudinary.uploader.destroy(public_id)
        except Exception as e:
            raise Exception(f'Cloudinary delete failed: {str(e)}')

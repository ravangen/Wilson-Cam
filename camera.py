from os import getenv
from subprocess import call

import dropbox


DROPBOX_IMAGE_NAME = '/img.jpeg'


def generate():
    call('fswebcam --config fswebcam.config image.jpeg', shell=True)
    return 'image.jpeg'


def upload(file_name):
    access_token = getenv('DROPBOX_TOKEN')
    if not access_token:
        raise ValueError('DROPBOX_TOKEN not set')
    client = dropbox.client.DropboxClient(access_token)
    
    # Get metadata of the current version of image
    try:
        file_metadata = client.metadata(DROPBOX_IMAGE_NAME)
    except dropbox.rest.ErrorResponse:
        file_metadata = {}
    parent_rev = file_metadata.get('rev')

    # Upload new version of image
    file_obj = open(file_name, 'rb')
    try:
        response = client.put_file(full_path=DROPBOX_IMAGE_NAME, file_obj=file_obj, parent_rev=parent_rev)
        print 'uploaded: ', response
    except dropbox.rest.ErrorResponse as e:
        print 'error: ', e.body
    finally:
        file_obj.close()


def main():
    file_name = generate()
    upload(file_name)


if __name__ == '__main__':
    main()

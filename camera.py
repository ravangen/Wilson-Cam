from __future__ import print_function
from os import getenv, path
from subprocess import call
import sys

import dropbox


DROPBOX_IMAGE_NAME = '/img.jpeg'
FSWEBCAM_CONFIG_NAME = 'fswebcam.config'


def error(*objs):
    print(*objs, file=sys.stderr)


def generate(file_name='image.jpeg'):
    directory = path.dirname(path.realpath(__file__))
    config_path = path.join(directory, FSWEBCAM_CONFIG_NAME)
    image_path = path.join(directory, file_name)
    call('fswebcam --config {config} {image}'.format(config=config_path, image=image_path), shell=True)
    return image_path


def upload(file_path):
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
    file_obj = open(file_path, 'rb')
    try:
        response = client.put_file(full_path=DROPBOX_IMAGE_NAME, file_obj=file_obj, parent_rev=parent_rev)
        print('uploaded: ', response)
    except dropbox.rest.ErrorResponse as e:
        error('error: ', e.body)
    finally:
        file_obj.close()


def main():
    file_path = generate()
    upload(file_path)


if __name__ == '__main__':
    main()

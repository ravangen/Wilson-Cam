# sudo pip install dropbox
# Create dropbox app at https://www.dropbox.com/developers/apps for Dropbox API with App Folder access type
# Generate an access token for your user to access this app folder

from subprocess import call

import dropbox

ACCESS_TOKEN = ''
DROPBOX_IMAGE_NAME = '/img.jpeg'


def generate():
    call('fswebcam --config fswebcam.config image.jpeg', shell=True)
    return 'image.jpeg'


def upload(file_name):
    client = dropbox.client.DropboxClient(ACCESS_TOKEN)
    try:
        file_metadata = client.metadata(DROPBOX_IMAGE_NAME)
    except dropbox.rest.ErrorResponse:
        file_metadata = {}
    parent_rev = file_metadata.get('rev')

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

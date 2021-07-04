import dropbox

class LearntoUseDrpbox:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.Az_9luqbgaHyGhgU-V0MATYbxw2bk7O13BgR-6walsMn7IMSpuFGPB18i1kyPcbeD_fOMg7sZXvn28yP27Ura1WBQzZETtKvB5zjYVtP68qGXQzUT42jZYDhAwEj4zMtW85BGs1Iqz0'
    transferData = LearntoUseDrpbox(access_token)

    file_from = 'secSam.txt'
    file_to = '/test_dropbox/secSam.txt'  # The full path to upload the file to, including the file name

    # API v2
    transferData.upload_file(file_from, file_to)

if __name__ == '__main__':
    main()
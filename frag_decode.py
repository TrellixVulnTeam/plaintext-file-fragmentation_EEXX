import os
import tarfile
import time

from frag_file import restore_files

this_folder = os.path.abspath(os.path.dirname(__file__))
source_folder = os.path.join(this_folder, r'ascii85_encoded')
output_folder = os.path.join(this_folder, r'output_decoded')

if __name__ == '__main__':
    # create folder to place plaintext fragment files
    if not os.path.isdir(source_folder):
        assert not os.path.exists(source_folder)
        os.makedirs(source_folder)
        print('source folder <{}> does not exist, creating...'.format(source_folder))

    # nothing to decode
    if len(os.listdir(source_folder)) == 0:
        print('nothing to decode, place files in <{}>'.format(source_folder))

    # start decoding
    else:
        if not os.path.isdir(output_folder):
            assert not os.path.exists(output_folder)
            os.makedirs(output_folder)
            print('output folder <{}> does not exist, creating...'.format(output_folder))

        t = time.time()

        # decode each bunch of fragments separately
        for temp_archive_path in restore_files(source_folder, password='password', verbose=True):

            # did not decode
            if temp_archive_path is None:
                continue
            # unzip
            print('restored to <{}>, unpacking archive...'.format(temp_archive_path))
            with tarfile.open(temp_archive_path, mode='r:gz') as tf:
                tf.extractall(path=output_folder)

            print('elapsed: {} seconds'.format(time.time() - t))

            # unpack and remove zip
            print('unpacked <{}>, deleting archive...'.format(temp_archive_path))
            os.remove(temp_archive_path)

            print('elapsed: {} seconds'.format(time.time() - t))

    print('done!')

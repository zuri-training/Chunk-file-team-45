from django.core.files.storage import FileSystemStorage
from django.conf import settings
from os.path import basename
from zipfile import ZipFile
import shutil
import json
import csv
import os


class Shredding:

    @staticmethod
    def yield_rows(reader, chunk_size):
        """
        Yield row chunks
        """
        chunk = []
        for counter, rows in enumerate(reader):
            if counter % chunk_size == 0 and counter > 0:
                yield chunk
                del chunk[:]
            chunk.append(rows)
        yield chunk

    @staticmethod
    def create_dir(filename):

        return os.makedirs(
            os.path.join(
                settings.MEDIA_ROOT, filename
            )
        )

    @staticmethod
    def shreding_csv_file(filepath, rows_num, filename):
        """
            Note: headers should be provided in the
            csv file.
        """

        with open(filepath, mode='r', encoding='windows-1252', newline='') as shred_file:
            reader = csv.DictReader(shred_file)
            shredit = Shredding.yield_rows(reader, int(rows_num))

            # creating a directory
            Shredding.create_dir(filename)

            for counter, shred in enumerate(shredit, start=1):
                with open(
                    os.path.join(
                        settings.MEDIA_ROOT, filename, f'{counter}-{filename}'
                    ),
                        mode='w', newline='') as shreded_file:
                    try:
                        fieldnames = list(shred[0].keys())
                        writer = csv.DictWriter(
                            shreded_file, fieldnames, quoting=csv.QUOTE_ALL)

                        writer.writeheader()
                        writer.writerows(shred)
                    except IndexError:
                        return False
        return True

    @staticmethod
    def shreding_json_file(filepath, rows_num, filename):
        try:
            with open(filepath, 'r', encoding='utf-8-sig', newline='') as file:
                json_file = json.load(file)
                file_length = len(json_file)

                # creating a directory
                Shredding.create_dir(filename)

                for shred in range(0, file_length, rows_num):
                    json.dump(json_file[shred:shred+rows_num],
                              open(os.path.join(
                                  settings.MEDIA_ROOT, filename,
                                  f'{filename}-{shred+1}.json'
                              ), 'w', encoding='utf8'),
                              ensure_ascii=False,
                              indent=True
                              )
        except:
            return None
        return True

    @staticmethod
    def zip_it(filename):
        directory = os.path.join(settings.MEDIA_ROOT, filename)
        zipped_file_path = os.path.join(
            settings.MEDIA_ROOT, f'{filename.split(".")[0]}.zip')
        try:
            zip_shred = ZipFile(zipped_file_path, 'w')
            # Iterate over all the files in directory
            for root, directories, files in os.walk(directory):
                for filename_ in files:
                    file_path = os.path.join(root, filename_)
                    zip_shred.write(file_path, basename(file_path))
        except:
            return None
        return os.path.abspath(zipped_file_path)

    @staticmethod
    def processing_file(request, file, chunk_num, size_type):

        # creating an uplaod Directory
        FileSystemStorage(
            location=os.path.join(settings.MEDIA_ROOT, 'alluploads')
        ).save(file.name, file)

        file_path = os.path.join(settings.MEDIA_ROOT, 'alluploads', file.name)

        if file.name.split('.')[-1] == 'csv':
            if Shredding.shreding_csv_file(file_path, chunk_num, file.name):
                if zip_it := Shredding.zip_it(file.name):
                    shutil.rmtree(os.path.join(settings.MEDIA_ROOT, file.name))
                    return zip_it

        if file.name.split('.')[-1] == 'json':
            if Shredding.shreding_json_file(file_path, chunk_num, file.name):
                if zip_it := Shredding.zip_it(file.name):
                    shutil.rmtree(os.path.join(settings.MEDIA_ROOT, file.name))
                    return zip_it

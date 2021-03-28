import requests


class YaUploader:
    def __init__(self, token: str):
        self.token = token
        if self.token == '':
            print('Укажите токен')

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def get_upload_url(self, yadisk_path):
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = self.get_headers()
        params = {'path': yadisk_path, 'overwrite': True}
        response = requests.get(upload_url, headers=headers, params=params)
        return response.json()['href']

    def upload(self, yadisk_path: str, file_path: str):
        """Метод загружает файл file_path на яндекс диск"""
        upload_url = self.get_upload_url(yadisk_path)
        response = requests.put(upload_url, data=open(file_path, 'rb'))
        if response.status_code == 200 or response.status_code == 201:
             print('Файл успешно загружен')
        else:
            print('Произошла ошибка загрузки файла')

from superhero import SuperHero
from yadisk import YaUploader
from stackoverflow import StackoverflowApi

if __name__ == '__main__':
    # определяем самого умного супергероя:
    TOKEN = '2619421814940190'
    superheroes_list = ['Hulk', 'Captain America', 'Thanos']
    superhero_api = SuperHero(TOKEN)
    superhero_api.most_intelligent_superhero(superheroes_list)

    # загружаем файл на Яндекс диск:
    TOKEN_YA = 'my_token'
    uploader = YaUploader(TOKEN_YA)
    result = uploader.upload('pics/Pencils.jpg', '/Users/Daria/Documents/Pencils.jpg')

    # получаем все вопросы за последние два дня с тэгом 'Python':
    python_questions = StackoverflowApi()
    python_questions.get_python_questions(tag='python')

# MemoMind

## Установка

- Необходимо установить Node.js LTS версии: https://nodejs.org/ru/
- А также Python 3.10.9 <a href="https://www.python.org/ftp/python/3.10.9/python-3.10.9-amd64.exe">Windows</a>, <a href="https://www.python.org/ftp/python/3.10.9/python-3.10.9-macos11.pkg">MacOS</a>.

Необходимо открыть командную строку в текущем проекте и установить зависимости:

```
npm -g i yarn
```

в папке 'frontend' выполнить команду:

```sh
yarn
```

а в папке 'backend':

```sh
pip install -r requirements.txt
```

Для того чтобы запустить проект локально, необходимо:

- Запустить клиентскую часть приложения в папке 'frontend'

```sh
yarn dev
```

- Запустить серверную часть в корневой папке проекта

```sh
uvicorn backend.main:app
```

- И запустить базу данных <a href='https://www.mongodb.com/'>MongoDB</a>
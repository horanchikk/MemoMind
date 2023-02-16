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

Теперь Вам необходимо запустить проект:

- Запуск клиентской части в папке Frontend

```sh
yarn dev
```

- Запуск серверной части в папке MemoMind

```sh
uvicorn backend.main:app
```

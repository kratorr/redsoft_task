# Тестовое задание Red Soft

## Примеры запуска cо встроенным dev сервером Django


## Сборка docker образа
Клонируем репозиторий:
```bash
git clone https://github.com/kratorr/redsoft_task
```
Сборка:
```bash
docker build --tag redsoft_task  .
docker run --rm -p 8000:8000 -d --name redsoft redsoft_task
```
Открыть swagger ui http://127.0.0.1:8000/api/schema/swagger-ui/

## Запуск из готового docker образа
```bash
docker run --rm -p 8000:8000 -d --name redsoft kratorr/redsoft_task 
```
Открыть swagger ui http://127.0.0.1:8000/api/schema/swagger-ui/

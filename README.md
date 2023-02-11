# Инструкция как работать с гитом для самых маленьких

## Ветка Main: 
1. В ветку main кладем только протестированные и готовые фичи\задачи. Можно всегда скачать ветку main и там все должно работать.
2. Никто не пишет в main код напрямую, кроме каких-то исключительных случаев (пофиксить 1-2 строчки кода). 

## Как разрабатывать
1. Для каждой фичи\задачи вы создаете новую ветку. Например, мы хотим добавить мультиплеер - будем работать в ветке multiplayer 
2. Первым делом обновим у себя на машине основную ветку, из которой отпочкуемся: 
```
git checkout main
git pull
```
3. Если вы успели что-то накодить в своей ветке main и возник конфликт - вы можете сделать
```
Откатить все ваши изменения на самый последний коммит, который был в этой ветке залит на github.com
git reset --hard HEAD
```
4. Далее создаем свою ветку для задачи и пишем код
```
git checkout -b multiplayer
и пишем-пишем. Можно создавать хоть сколько угодно коммитов - они все равно будут слеплены по итогу в 1 общий
как только все сделали:
git add .
git commit
git push
```
5. как только задача готова, протестирована - изменения нужно будет перенести в общий main
```
кто-то мог внести свои задачи в main до нас - поэтому сперва нужно получить актуальный main
git checkout main
git pull
далее слепляем main и нашу фичу
git merge multiplayer
смотрим есть ли конфликты или нет
git status
если есть - они будут красным обозначены - заходим в эти файлы, убираем комменты которые поставил гит и переписываем код так как считаем нужным
git add .
git commit
git push
ура, ваша задача теперь в main

6. далее multiplayer можно вообще удалить (в интерфейсе гита например) и делать новую задачу уже в новой ветке
(можно и продолжить работать, если поняли что есть какие-то доработки)  
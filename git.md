Даст список всех коммитов в репозитории
```git
git log --graph --pretty=format:'%C(yellow)%h%C(reset) %C(cyan)%d%C(reset) %C(green)(%ar) %C(bold blue)<%an>%C(reset)' --all
```

Даст полные изменения в файле в последних 10 коммитах
```git
git --no-pager log -p --color -n 10 lesson_1.py
```

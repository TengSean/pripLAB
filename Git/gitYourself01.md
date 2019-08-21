# Git 學習筆記 01 : 儲存庫的推拉
___
身為IT人，怎麼能不會用git呢?

## 建立多人儲存庫
___
假設在github上已經有一個現存儲存庫，此時大家都會用`git clone ...` 以取得完整的儲存庫。

##遠端儲存庫的開發流程
___
線假設`user1`和`user2`都擁有同一個repo，user1 在user2不知情的情況下推了一個b.txt上去，此時若`user2`想把自已本地的儲存庫push上去會發生錯誤，此時`user2`只需用`git pull --rebase`將遠端儲存庫的內容抓下來再用rebase去合併即可解決。

##常用的指令用alias縮寫
___
```
git config --global alias.sts  "status -s"
git config --global alias.lg5 "log --graph --pretty=format:'%Cred%h%Creset %ad |%C(yellow)%d%Creset %s %Cgreen(%cr)%Creset [%Cgreen%an%Creset]' --abbrev-commit --date=short -5"
git config --global alias.lg5 "log --graph --pretty=format:'%Cred%h%Creset %ad |%C(yellow)%d%Creset %s %Cgreen(%cr)%Creset [%Cgreen%an%Creset]' --abbrev-commit --date=short -5"
```

##Reference
___
[*參考於保哥的learn-git-in-30-days:*](https://github.com/doggy8088/Learn-Git-in-30-days)





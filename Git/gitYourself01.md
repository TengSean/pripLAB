# Git 學習筆記 01 : 儲存庫的推拉

身為IT人，怎麼能不會用git呢?
___
## 建立多人儲存庫

假設在github上已經有一個現存儲存庫，此時大家都會用`git clone ...` 以取得完整的儲存庫。
___
##遠端儲存庫的開發流程

線假設`user1`和`user2`都擁有同一個repo，user1 在user2不知情的情況下推了一個b.txt上去，此時若`user2`想把自已本地的儲存庫push上去會發生錯誤，此時`user2`只需用`git pull --rebase`將遠端儲存庫的內容抓下來再用rebase去合併即可解決。
___
##刪除最近一次的版本

假如想把當前最新的commit物件刪除變回上一個版本的話 (如下圖)
```
[83a841] > [0576e0] > [aef2a5]   ->   [83a841] > [0576e0]
```
可以透過`git reset --hard "HEAD^"`即可刪除HEAD這個版本。

**NOTE再命令字元下`^`是特殊符號，所以必須用雙引號刮起來**

此時可以看見，原本的最新版本已經刪除，那是因為`git reset --hard "HEAD^"`把HEAD指向的位址改到了前一個版本`(HEAD^)`，所以上一個版本物件`[aef2a5]`在`git log`中已經看不到了。

**[mark]add pic here**

事實上，`[aef2a5]`commit物件其實一直儲存在git除物件儲存區(object storage)中，也就是該物件一直存在於`./git/object`目錄下，換言之我們可以使用`git show aef2a5`取得該版本的詳細資料。
___
##重新提交一次最後的版本

倘若不小心把還未確定的版本`commit`出去了，此時可以用`git commit --amend`。這個指令可以把目前記錄在索引中得變更檔案，全部加到當前最新版之中，並要求你修改原本的紀錄訊息。

值得注意的是，最新版的`HEAD`已經是完全不同的commit物件了，所以用`git log`看到的commit物件跟之前的完全不同。

___
##常用的指令用alias縮寫

```
git config --global alias.sts  "status -s"
git config --global alias.lg5 "log --graph --pretty=format:'%Cred%h%Creset %ad |%C(yellow)%d%Creset %s %Cgreen(%cr)%Creset [%Cgreen%an%Creset]' --abbrev-commit --date=short -5"
git config --global alias.lg5 "log --graph --pretty=format:'%Cred%h%Creset %ad |%C(yellow)%d%Creset %s %Cgreen(%cr)%Creset [%Cgreen%an%Creset]' --abbrev-commit --date=short -5"
```
___
##Reference

[*參考於保哥的learn-git-in-30-days:*](https://github.com/doggy8088/Learn-Git-in-30-days)





# QQ ChatBot

人工智障聊天机器人，一些智障的词汇素材来自QQ2912441641此人聊天记录。

欢迎加入人工智障试验场QQ群号：229585706

## 服务器后台运行

```bash
$ nohup ./main.py &
```

## 二维码终端

修改配置文件：`~/.qqbot-tmp/v2.x.conf`

若 cmdQrcode 项设置为 True ，则会在 term 中以文本模式显示二维码。注意：要使用文本模式，需要自行安装 pillow 和 wcwidth 库，可使用 pip 安装。

`$ pip3 install pillow wcwidth`

## dependences

`$ pip3 install qqbot requests regex`

## License

This project is licensed under version 3 of the GNU General Public License.

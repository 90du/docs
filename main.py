#!/usr/bin/python3
# -*- coding: utf-8 -*-

import tuling
import qqbot
import time

# from qqbot import RunBot
# from qqbot import QQBot

# @qqbot.QQBotSlot
# def onQQMessage(bot, contact, member, content):
    # answer = tuling.answer(content)
    # if '@ME' in content:
        # bot.SendTo(contact, "干啥？")
        # bot.SendTo(contact, answer)

@qqbot.QQBotSlot
def onQQMessage(bot, contact, member, content):
    #bot     : QQBot 对象，提供 List/SendTo/Stop/Restart 四个接口
    #contact : QContact 对象，消息的发送者，具有 ctype/qq/uin/nick/mark/card/name 等属性
    #member  : QContact 对象，仅当本消息为 群或讨论组 消息时有效，代表实际发消息的成员
    #content : str 对象，消息内容

    answer = tuling.answer(content)
    time.sleep(1)
    bot.SendTo(contact, answer)
    bot.Restart()

    # if "@ME" in content:
    #     bot.SendTo(contact, "????")


# def main():
#     mybot = QQBot._bot
#     mybot.Login(['-q', '3311577599'])
#     mybot.pollForever()

    # target: 科研交流群
    # group_list = mybot.List("group")
    # for group in group_list:
    #     print(group)

    # target_group = mybot.List("group", "科研交流群")[0]
    # mybot.SendTo(target_group, "人工智障003已上线")

if __name__ == '__main__':
    # main()
    # 3311577599
    # 2943916806
    qqbot.RunBot(['-q', '3311577599'])

#!/usr/bin/python3
# -*- coding: utf-8 -*-

import qqbot
import random
import time
import sys
import os
import tuling

file = open('phrase.txt')
lines = file.readlines()

@qqbot.QQBotSlot
def onQQMessage(bot, contact, member, content):
    if bot.isMe(contact, member):
        return()

    if getattr(member, 'uin', None) == bot.conf.qq:
        return()

    # remove spaces.
    content = content.strip()

    if not content:
        answer = lines[random.randint(0, len(lines))]
        answer = answer.strip('\n')
    else:
        answer = tuling.answer(content, member.uin)

    sf = open('record.txt', 'a')
    sf.write("name: " + member.name + '\n')
    sf.write(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + '\n')
    sf.write("content: " + content + '\n')
    sf.write("answer: " + answer + "\n\n")
    sf.close()

    bot.SendTo(contact, answer)

def main():
    mybot = QQBot._bot
    mybot.Login(['-q', '3311577599'])
    mybot.pollForever()

    group_list = mybot.List('group')
    group = mybot.List('group', '科研交流群')[0]
    mybot.SendTo(group, "人工智障001已上线")

if __name__ == '__main__':
    qqbot.RunBot(['-q', '3311577599'])

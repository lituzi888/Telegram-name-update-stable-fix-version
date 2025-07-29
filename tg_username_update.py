import time
import os
import sys
import logging
import asyncio
from time import strftime
from telethon import TelegramClient
from telethon.tl.functions.account import UpdateProfileRequest
from telethon.errors import FloodWaitError
from emoji import emojize

# 本版由TG：@LiTuZi修复更新
all_time_emoji_name = ["clock12", "clock1230", "clock1", "clock130", "clock2", "clock230", "clock3", "clock330", "clock4", "clock430", "clock5", "clock530", "clock6", "clock630", "clock7", "clock730", "clock8", "clock830", "clock9", "clock930", "clock10", "clock1030", "clock11", "clock1130"]
time_emoji_symb = [emojize(":%s:" % s, use_aliases=True) for s in all_time_emoji_name]

# API 凭据
api_auth_file = 'api_auth'
if not os.path.exists(api_auth_file+'.session'):
    api_id = input('api_id: ')
    api_hash = input('api_hash: ')
else:
    api_id = 8888888
    api_hash = '888888'  # 更换属于自己的api_id与api_hash

client1 = TelegramClient(api_auth_file, api_id, api_hash)

# 日志设置
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

async def change_name_auto():
    print('将开始更改姓氏')
    while True:
        try:
            time_cur = strftime("%H:%M:%S:%p:%a", time.localtime())
            hour, minu, seco, p, abbwn = time_cur.split(':')
            if seco == '00':  # 仅在整分钟更新，减少 API 调用频率
                shift = 1 if int(minu) > 30 else 0
                hsym = time_emoji_symb[(int(hour) % 12) * 2 + shift]
                last_name = f'{hour}:{minu} {p} {hsym}'  # 仅保留此格式，例如 "12:30 🕐"
                await client1(UpdateProfileRequest(last_name=last_name))
                logger.info('更新成功 -> %s' % last_name)
                await asyncio.sleep(60)  # 等待 60 秒，避免频繁调用
            else:
                await asyncio.sleep(1)  # 非整分钟时每秒检查
        except FloodWaitError as e:
            logger.error(f'触发速率限制，需等待 {e.seconds} 秒')
            await asyncio.sleep(e.seconds)  # 等待 Telegram 要求的冷却时间
        except KeyboardInterrupt:
            print('\n将重置姓氏\n')
            await client1(UpdateProfileRequest(last_name=''))
            sys.exit()
        except Exception as e:
            logger.error(f'错误: {type(e).__name__}: {e}, 时间: {time_cur}')
            await asyncio.sleep(1)

async def main(loop):
    await client1.start()
    print('创建任务')
    task = loop.create_task(change_name_auto())
    await task
    await client1.run_until_disconnected()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(loop))
import http

import yadisk.exceptions

from disk.connect import client
import asyncio

async def main():
    try:
        await client.get_meta('Картинки')
        print('Есть')
    except yadisk.exceptions.PathNotFoundError:
        print('Нету')



if __name__ == '__main__':
    asyncio.run(main())

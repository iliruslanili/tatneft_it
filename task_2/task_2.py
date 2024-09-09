import os
import asyncio
import aiohttp
import aiofiles

urls = [
    'https://tatitneft.tatneft.ru',
    'https://tatneft.ru',
    'https://promo-tatneft.ru',
    'https://yandex.ru',
    'https://example.com',
    'https://python.org'
]


async def get_site_data(url):

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            html_data = await response.text()

    site_name = url.split('/')[-1]

    async with aiofiles.open(os.path.join('site_data', f'{site_name}.html'), 'w') as f:
        await f.write(html_data)

    return url


async def main(urls=urls):

    tasks = [asyncio.create_task(get_site_data(url)) for url in urls]

    results = await asyncio.gather(*tasks, return_exceptions=True)
    success = []
    error = []

    for i, result in enumerate(results):
        if isinstance(result, Exception):
            error.append(result)
        else:
            success.append(urls[i])

    success = [i for i in results if not isinstance(i, Exception)]
    errors = [urls[i] for i, result in enumerate(results) if isinstance(result, Exception)]

    print(f'Success: {success}')
    print(f'Errors: {errors}')

if __name__ == '__main__':
    asyncio.run(main())

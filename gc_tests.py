from typing import Awaitable


async def get_str() -> str:
    return "123"


async def get_func_str() -> Awaitable[str]:
    return await get_str()


if __name__ == "__main__":
    import asyncio
    print(asyncio.run(get_func_str()))

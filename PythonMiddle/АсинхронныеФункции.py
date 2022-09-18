'''
import asyncio

async def main():
    print('Hello ...')
    await asyncio.sleep(1)
    print('... World!')


print('Input data!')
asyncio.run(main())
print('Input data2!')
print('Input dat3!')
'''

import asyncio

async def foo():
    print('Running in foo')
    await asyncio.sleep(2)
    print('Explicit context switch to foo again')


async def bar():
    print('Explicit context to bar')
    await asyncio.sleep(0)
    print('Implicit context switch back to bar')


ioloop = asyncio.get_event_loop()
tasks = [ioloop.create_task(foo()), ioloop.create_task(bar())]
wait_tasks = asyncio.wait(tasks)
ioloop.run_until_complete(wait_tasks)
ioloop.close()
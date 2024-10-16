from aiohttp import web
import json


async def echo(request):
    # Get the request data
    data = await request.json()

    # Return the same data as a JSON response
    return web.json_response(data)


app = web.Application()
app.router.add_post('/echo', echo)

if __name__ == '__main__':
    web.run_app(app, host='127.0.0.1', port=8080)

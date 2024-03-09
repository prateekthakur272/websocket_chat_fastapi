from fastapi import Request, WebSocket
from fastapi.responses import HTMLResponse
from fastapi.routing import APIRouter
from fastapi.templating import Jinja2Templates;

templates = Jinja2Templates('templates')
router = APIRouter()

@router.get('/')
def root(request:Request):
    return templates.TemplateResponse('home_page.html', {'request':request})


@router.websocket('/')
async def web_socket(socket:WebSocket):
    await socket.accept()
    while True:
        message = await socket.receive_text()
        print(message)
        await socket.send_text("hello")
        
        
websocket_list=[]
@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
	await websocket.accept()
	if websocket not in websocket_list:
		websocket_list.append(websocket)
	while True:
		data = await websocket.receive_text()
		for web in websocket_list:
			if web!=websocket:
			    await web.send_text(f"{data}")


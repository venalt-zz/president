from jinja2 import Environment, PackageLoader #For templating
from president import president

env = Environment(loader=PackageLoader('game', 'templates'))

#Home page routes
@app.route('/')
def hello_world():
    template = env.get_template('waiting_room.html')
    return template.render(var='var')

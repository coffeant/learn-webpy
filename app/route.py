import web,os

app_root = os.path.dirname(__file__)
templates_root = os.path.join(app_root, 'template')
render = web.template.render(templates_root)

class route:
    def GET(self,path):
        print "path is %s ;"%path
        modPath = 'app.controller.' + path.replace('/','.');
        print "modPath = %s ;" % modPath
        className = modPath[ modPath.rfind('.')+1 : ]
        print "className = %s;" % className
        try:
            print local()
        except ImportError:
            print 'import error'
        return render.hello()

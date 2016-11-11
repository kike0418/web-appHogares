# encoding: utf-8
import csv
import web
render = web.template.render('views/')
urls = ('/index(.*)', 'index')

class index:  
    def GET(self, data):
        data = []
        temp = []
        
        with open("Proyecciones_hogares_indigenas.csv", "r") as file_open:
            dat = csv.reader(file_open, delimiter=",")
            for row in dat:
                data.append(row)
        return render.index(data)

if __name__ == '__main__':
    app = web.application(urls, globals())
    web.config.debug = True
    app.run()
     
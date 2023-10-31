from livereload import Server


def rebuild():
    print("Site rebuilt")


server = Server()
server.watch('dist/index.html', rebuild)
server.serve(root='.')
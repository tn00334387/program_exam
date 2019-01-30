 
urls = ["http://www.google.com/a.txt",
        "http://www.google.com.tw/a.txt",
        "http://www.google.com/download/c.jpg",
        "http://www.google.co.jp/a.txt",
        "http://www.google.com/b.txt",
        "https://facebook.com/movie/b.txt",
        "http://yahoo.com/123/000/c.jpg",
        "http://gliacloud.com/haha.png",]

filename = ""
filenames = {}

for i in urls:
    filename = i[i.rfind('/')+1:]
    if filenames.has_key(filename):
        filenames[filename] = filenames[filename] + 1
    else:
        filenames.update({filename:1})

s_filenames = sorted(filenames.items(), key=lambda filenames: filenames[0])

for key, value in s_filenames[0:3]:
    print key, value


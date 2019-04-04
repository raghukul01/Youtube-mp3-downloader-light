with open('youtube.html', 'r') as file:
    data = file.read().replace('\n', '')

common='"videoId":"'
urls = {}
for i in range(len(data)-11):
    if data[i:i+11] == common:
        j = i+11
        str_ = ''
        while(True):
            if data[j] == '"':
                break;
            str_ += data[j]
            j+=1
        urls[str_] = True


finalUrl = list(urls.keys())
for link in finalUrl:
    str_ = 'https://www.youtube.com/watch?v=' + link
    print(str_)
# print(len(data))

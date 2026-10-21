import re,urllib.request,base64,sys
UA={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/120 Safari/537.36'}
fams=['Old+Standard+TT:wght@400;700','Lobster','Neucha','Rubik:wght@400..900','Russo+One','Pangolin']
out=[]
for f in fams:
    css=urllib.request.urlopen(urllib.request.Request('https://fonts.googleapis.com/css2?family='+f+'&display=block',headers=UA)).read().decode()
    for sub,block in re.findall(r'/\* (\S+) \*/\s*(@font-face \{.*?\})',css,re.S):
        if sub not in('cyrillic','latin'): continue
        url=re.search(r'url\((.*?)\)',block).group(1)
        data=base64.b64encode(urllib.request.urlopen(urllib.request.Request(url,headers=UA)).read()).decode()
        out.append(block.replace(url,'data:font/woff2;base64,'+data).replace("format('woff2')","format('woff2')"))
open('fonts/fonts.css','w').write('\n'.join(out))
print(len(out),'faces', sum(len(o) for o in out)//1024,'KB')

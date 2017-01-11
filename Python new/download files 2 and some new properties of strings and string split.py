from urllib import request

url=''
def download_file():
    response=request.urlopen(url)   #connect with the file
    csv=response.read()
    csv_str=str(csv)
    lines=csv_str.split('\n')   #split on basis of ne;w line
    dest_url=r'goog.csv'
    fx=open(dest_url,"w")
    for line in lines:
        fx.write(line+"\n")
    fx.close()


line="      ae" \
     "efaef" \
     "afe"
print(line)

line1="""
dsfsd
dfij
"""
print(line1)
print(line1.split('\n'))
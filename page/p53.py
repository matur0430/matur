d={}
urls={"google":"google.com","naver":"naver.com",}
urls["daum"]="daum.com"
urls["daum"]="daum.net"
a=urls.pop("google")
print(urls)
print(a)
print(urls.get("naver"))
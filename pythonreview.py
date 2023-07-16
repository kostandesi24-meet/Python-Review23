def create_youtube_video(title,description):
	 youtubevid={"title"=title,"description"=description,"likes"=0,"dislikes"=0,"comments"= coment={},"hashtags"=list[]}
	 for i in 5:
	 	youtubevid["hashtags"][i]=input("enter any recomndation :")
	 	return youtubevid

def likes(youtubevid):
	if "likes" in youtubevid:
		youtubevid["likes"]=youtubevid["likes"]+1
	return youtubevid

def dislikes(youtubevid):
	if "dislikes" in youtubevid:
		youtubevid["dislikes"]=youtubevid["dislikes"]+1
	return youtubevid

def add_comment(youtubevid,username,comment_text):
	if "comments" in youtubevid:
		youtubevid["comments"]= youtubevid["coment"]["username"]="comment_text"
		return youtubevid

dect1= create_youtube_video("meety2","talks about meet's y2 students")
dect2= create_youtube_video("meety1","talks about meet's y1 students")
# for i in 495:
# 	likes(dect)
c=0
def simiularaty(dect1,dect2):
	for i in 5 :
		x = dect1["hashtags"][i]
		for j in 5:
			if x == dect2["hashtags"][j]:
				c=c+1
	print("the percentage of simiularaty : " + c*4 +"%")

# python3 pythonreview.py
def create_youtube_video(title, description):
    youtubevid = {"title": title, "description": description, "likes": 0, "dislikes": 0, "comments": {}, "hashtags": []}
    for i in range(5):
        youtubevid["hashtags"].append(input("Enter any recommendation: "))
    return youtubevid

def likes(youtubevid):
    if "likes" in youtubevid:
        youtubevid["likes"] += 1
    return youtubevid

def dislikes(youtubevid):
    if "dislikes" in youtubevid:
        youtubevid["dislikes"] += 1
    return youtubevid

def add_comment(youtubevid, username, comment_text):
    if "comments" in youtubevid:
        youtubevid["comments"][username] = comment_text
    return youtubevid

c = 0
def simiularaty(dect1, dect2):
    global c
    for i in range(5):
        x = dect1["hashtags"][i]
        for j in range(5):
            if x == dect2["hashtags"][j]:
                c += 1
    print("The percentage of similarity: " + str(c * 4) + "%")

dect1 = create_youtube_video("meety2", "talks about meet's y2 students")
dect2 = create_youtube_video("meety1", "talks about meet's y1 students")
simiularaty(dect1,dect2)

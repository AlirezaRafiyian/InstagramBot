from instagrapi import Client
from instagrapi.types import StoryMention

# Create an instance of the InstaGrapi client
client = Client()

# Login to your Instagram account
username = ''
password = ''

# request login info from user
username = input("Enter your username: ")
password = input("Enter your password: ")

client.login(username, password)

# Menu
def showMenu():
    print("""
    Choose from the options: 
        0. Terminate Action
        1. Upload Post (image)
        2. Upload Video (mp4)
        3. Upload Story (image)
    """)

# Get user request    
def getUserChoice():
    choice = input("Enter your choice (0-3): ")
    return int(choice)

# Get Post info
def photoPostUpload():
    photoPath = input("Enter the image path: ")
    caption = input("Enter the caption: ")

    return photoPath, caption

# Get Post(video) info
def videoPostUpload():
    videoPath = input("Enter the video path: ")
    caption = input("Enter the caption: ")

    return videoPath, caption
# Get Story infor
def photoStoryUpload():
    photoPath = input("Enter the image path: ")
    mention = input("The ID you want to be mentioed: ")

    return photoPath, mention


while True:
    showMenu()
    choice = getUserChoice()

    if choice == 1:
        postpic = photoPostUpload()
        pp , capt = postpic
        upload_id = client.photo_upload(pp, capt)
        print("Post uploaded")
    elif choice == 2:
        postvid = videoPostUpload()
        pv, capt = postvid
        upload_id = client.video_upload(pv, capt)
        print("Video uploaded")
    elif choice == 3:
        storypic = photoStoryUpload()
        pp, ment = storypic
        mentiom = client.user_info_by_username(ment)
        upload_id = client.photo_upload_to_story(pp, mentions=[StoryMention(user=mentiom, x=0.49892962, y=0.703125, width=0.8333333333333334, height=0.125)])
        print("Story uploaded")
    elif choice == 0:
        print("You selected to Terminate action")
        break
    else: 
        print("Wrong Choice!")


client.logout()

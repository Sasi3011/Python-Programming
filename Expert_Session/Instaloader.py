import instaloader

loader = instaloader.Instaloader()
profile_name = input("Enter the Instagram profile name: ")
loader.download_profile(profile_name, profile_pic_only=True)
print("Download completed successfully!")

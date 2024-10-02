from pytubefix import YouTube
import pymysql

# Database connect
try:
    mysql = pymysql.connect(host="localhost", user="root", password="", database="yt_download")
    print("Database connected successfully...")
except Exception as e:
    print(e)

cr = mysql.cursor()

# Table creation
create_parent_tbl = """CREATE TABLE yt_register (id INTEGER PRIMARY KEY AUTO_INCREMENT,r_name VARCHAR(50),r_number INTEGER,r_password VARCHAR(10),confirm_password VARCHAR(10))"""

create_child_table = """CREATE TABLE yt_download (id INTEGER PRIMARY KEY AUTO_INCREMENT,user_id INTEGER,title_name VARCHAR(1000),FOREIGN KEY(user_id) REFERENCES yt_register(id) ON DELETE CASCADE)"""

try:
    cr.execute(create_parent_tbl)
    cr.execute(create_child_table)
    print("Tables created successfully...")
except Exception as e:
    print(e)

class Format:
    def yt_video(self, user_id):
        url = input("Enter youtube video URL: ")
        yt = YouTube(url)
        print(f"Video Title: {yt.title}")

        # Insert title in table
        insert_data = "INSERT INTO yt_download(user_id, title_name) VALUES (%s, %s)"
        try:
            cr.execute(insert_data, (user_id, yt.title))
            mysql.commit()
            print("Title inserted successfully...")
        except Exception as e:
            print(e)

        ys = yt.streams.get_highest_resolution()
        print("Downloading...")
        ys.download()
        print("Download complete!")

    def yt_audio(self, user_id):
        url = input("Enter URL: ")
        yt = YouTube(url)
        print(f"Video Title: {yt.title}")

        # Insert title in table
        insert_data = "INSERT INTO yt_download(user_id, title_name) VALUES (%s, %s)"
        try:
            cr.execute(insert_data, (user_id, yt.title))
            mysql.commit()
            print("Title inserted successfully...")
        except Exception as e:
            print(e)

        ys = yt.streams.get_audio_only()
        print("Downloading audio...")
        ys.download()
        print("Download complete!")

class UserLogin:
    def register(self):
        self.r_name = input("Enter your name: ")
        self.r_number = int(input("Enter your number: "))
        self.r_password = input("Enter your password: ")
        self.confirm_password = input("Re-enter your password: ")

        while self.r_password != self.confirm_password:
            print("Passwords do not match. Please try again.")

        # Insert data
        insert_data = """INSERT INTO yt_register(r_name, r_number, r_password, confirm_password) VALUES (%s, %s, %s, %s)"""
        try:
            cr.execute(insert_data, (self.r_name, self.r_number, self.r_password, self.confirm_password))
            mysql.commit()
            print("Registration successful.")
        except Exception as e:
            print(e)

    def login(self):
        l_name = input("Enter your name: ")
        l_password = input("Enter your password: ")

        insert_data = "SELECT id, r_name, r_password FROM yt_register WHERE r_name = %s AND r_password = %s"
        try:
            cr.execute(insert_data, (l_name, l_password))
            result = cr.fetchone()

            if result:
                self.user_id = result[0]
                self.r_name = result[1]
                self.r_password = result[2]

                print("Login successful!")
                main(self.user_id)
            else:
                print("Name or password does not match.")
    
        except Exception as e:
            print(e)

def login_main():
    user = UserLogin()

    while True:
        print("=" * 50)
        print("1) Register")
        print("2) Login")
        print("3) Exit")
        print("=" * 50)

        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            user.register()
        elif choice == '2':
            user.login()
        elif choice == '3':
            print("Exit..")
            break
        else:
            print("Invalid choice")

def main(user_id):
    vid_aud = Format()

    while True:
        print("=" * 50)
        print("1) Download in video format")
        print("2) Download in audio format")
        print("3) Exit")
        print("=" * 50)

        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            vid_aud.yt_video(user_id)
        elif choice == '2':
            vid_aud.yt_audio(user_id)
        elif choice == '3':
            print("Logout successfully...")
            break
        else:
            print("Invalid choice")

login_main()
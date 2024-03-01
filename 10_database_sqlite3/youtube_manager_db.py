import sqlite3

conn = sqlite3.connect('youtube_videos.db')

cursor = conn.cursor()

cursor.execute(''' 
    CREATE TABLE IF NOT EXISTS videos(
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            time TEXT NOT NULL
    )
''')

def list_videos():
    cursor.execute("Select * from videos")
    for row in cursor.fetchall():
        print(row)

def add_video(name, time):
    cursor.execute("Insert into videos (name, time) values (?, ?)", (name, time))
    conn.commit()

def update_video(video_id, name, time):
    cursor.execute("Update videos set name = ?, time = ? where id = ?", (name, time, video_id))
    conn.commit()

def delete_video(video_id):
    cursor.execute("Delete from videos where id = ?", (video_id,))
    conn.commit()

def main():
    while True:
        print("\n Youtube Manager App with DB")
        print("1. List all youtube videos ")
        print("2. Add a youtube video")
        print("3. Update a youtube video details ")
        print("4. Delete a youtube video ")
        print("5. Exit the app ")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            list_videos()
        elif choice == '2':
            name = input("Enter the video name: ")
            time = input("Enter the video time: ")
            add_video(name, time)
        elif choice == '3':
            video_id = input("Enter the video ID to update: ")
            name = input("Enter the video name: ")
            time = input("Enter the video time: ")
            update_video(video_id, name, time)
        elif choice == '4':
            video_id = input("Enter the video ID to delete: ")
            delete_video(video_id)
        elif choice == '5':
            break
        else:
            print("Invalid Choice...")
    
    conn.close()

if __name__ == "__main__":
    main()
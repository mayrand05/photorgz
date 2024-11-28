import os
import shutil
from datetime import datetime

def group_photos_by_event(photo_dir, output_dir):
    
    event_name = input("Enter the event name: ")
    start_date = input("Enter the event start date (YYYY-MM-DD): ")
    end_date = input("Enter the event end date (YYYY-MM-DD): ")

  
    try:
        start_date = datetime.strptime(start_date, "%Y-%m-%d")
        end_date = datetime.strptime(end_date, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return

    event_folder = os.path.join(output_dir, event_name)
    os.makedirs(event_folder, exist_ok=True)

    
    for photo_name in os.listdir(photo_dir):
        try:
            
            photo_date = datetime.strptime(photo_name.split('.')[0], "%Y-%m-%d")

            
            if start_date <= photo_date <= end_date:
                src = os.path.join(photo_dir, photo_name)
                dest = os.path.join(event_folder, photo_name)
                shutil.move(src, dest)
                print(f"Moved: {photo_name} to {event_folder}")
        except ValueError:
            print(f"Skipping: {photo_name} (invalid date format)")

    print(f"Photos grouped in: {event_folder}")


if __name__ == "__main__":
    print("Welcome to the Photo Organizer!")

    
    photo_directory = input("Enter the full path to the folder containing your photos: ").strip()
    output_directory = input("Enter the full path to the folder where you want organized photos: ").strip()

  
    if not os.path.exists(photo_directory):
        print("The photo directory does not exist. Please check the path.")
    elif not os.path.exists(output_directory):
        print("The output directory does not exist. Please check the path.")
    else:
     
        group_photos_by_event(photo_directory, output_directory)

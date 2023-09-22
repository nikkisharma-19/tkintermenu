def show_result(result_text):
    messagebox.showinfo("Result", result_text)
    
def whatsapp():
    pwk.sendwhatmsg_instantly('+918824610711', 'Hello', 10)
    
    
def Email():
    email_sender = 'deepkumarktp@gmail.com'
    email_password = 'lkgqrxmznxulrudb'
    email_receiver = input("Enter your email: ")

    subject = 'Check out my email code'
    body = """
    """

    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())
        
    show_result("Email Sent")

        
def message():
    import twilio
    from twilio.rest import Client

    account_sid = 'AC247de1d3e0c06a9066da21cc94a7f703'
    auth_token = '62f286dd6a5cc86e9dcd1f0f173c37c1'

    client = Client(account_sid, auth_token)

    def send_sms(to_number, message):
        try:
            message = client.messages.create(
                body=message,
                from_='+14705708450',
                to=to_number
            )
            print("SMS sent successfully!")
            print("Message SID:", message.sid)
        except Exception as e:
            print("Error sending SMS:", str(e))

    recipient_number = '+918824610711'  
    sms_message = 'Hello from Twilio! Hello! How are you.'

    send_sms(recipient_number, sms_message)
    
def click_photo():

   cap=cv2.VideoCapture(0)
   cap
   status ,photo =cap.read()
   cv2.imwrite("pic.jpg",photo)
   cv2.imshow("My photo",photo)
   cv2.waitKey(5000)
   cv2.destroyAllWindows()
   cap.release()

def crop_pic():
   cap=cv2.VideoCapture(0)
   cap
   status ,photo =cap.read()
   cv2.imwrite("pic.jpg",photo)
   cv2.imshow("My photo",photo[200:540,200:430])
   cv2.waitKey(5000)
   cv2.destroyAllWindows()
   cap.release()
    

def capture_video():
    cap=cv2.VideoCapture(0)
    while True:
        status ,photo=cap.read()
        cv2.imshow("My photo",photo)
        if cv2.waitKey(5)==13:
            break
    cv2.destroyAllWindows()

def capture_crop_video():
    cap=cv2.VideoCapture(0)
    while True:
        status ,photo=cap.read()
        photo[0:200,0:200]=photo[200:400,200:400]
        cv2.imshow("My photo",photo)
        if cv2.waitKey(5)==13:
            break
    cv2.destroyAllWindows()

        
        
def launch_instance():
    region = 'ap-south-1'
    
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    
    instance_name = simpledialog.askstring("Instance Name", "Enter instance name:")
    
    if instance_name:
        ec2_client = boto3.client('ec2', region_name=region)
        response = ec2_client.run_instances(
            ImageId='ami-0da59f1af71ea4ad2',
            InstanceType='t2.micro',
            MaxCount=1,
            MinCount=1,
            TagSpecifications=[
                {
                    'ResourceType': 'instance',
                    'Tags': [
                        {
                            'Key': 'Name',
                            'Value': instance_name
                        },
                    ]
                },
            ]
        )
        
        instance_id = response['Instances'][0]['InstanceId']
        messagebox.showinfo("Instance Launched", f"Instance '{instance_id}' launched successfully!")
    else:
        messagebox.showwarning("Instance Launch", "No instance name provided.")

    
    

    
def create_bucket():
    bucket_name = simpledialog.askstring("Bucket Name", "Enter bucket name:")
    if bucket_name:
        s3_client = boto3.client('s3', region_name='ap-south-1')
        s3_client.create_bucket(
            Bucket=bucket_name,
            ACL='private',
            CreateBucketConfiguration={
                'LocationConstraint': 'ap-south-1'
            }
        )
        messagebox.showinfo("Bucket Created", f"Bucket '{bucket_name}' created successfully!")
    else:
        messagebox.showwarning("Bucket Creation", "No bucket name provided.")
        
        
        
    
def open_software(software_name):
    software_path = {
        "notepad": "notepad.exe",
        "calculator": "calc.exe",
        "paint": "mspaint.exe",
        "chrome":"chrome.exe",
        "command prompt":"cmd.exe",
        "explorer":"explorer.exe",
        "vlc":"vlc.exe",
         "task manager":"taskmgr",
        # Add more software names and paths here
    }

    if software_name in software_path:
        try:
            os.startfile(software_path[software_name])
        except Exception as e:
            status_label.config(text=f"Error: {e}")
    else:
        status_label.config(text="Software not found.")
    pass

def get_coordinates():
    location_name = simpledialog.askstring("User Input", "Enter place:")
    
    if location_name:
        geolocator = Nominatim(user_agent="location_finder")
        location = geolocator.geocode(location_name)
        
        if location is None:
            messagebox.showerror("Error", f"Coordinates not found for '{location_name}'.")
        else:
            latitude = location.latitude
            longitude = location.longitude
            result_str = f"Coordinates for '{location_name}': Latitude = {latitude}, Longitude = {longitude}."
            messagebox.showinfo("Coordinates", result_str)    

def google_search():
    search_query = input("Enter What You Want To Search for: ")
    top_5_results = search(search_query, num_results=5)
    result_text = f"Top 5 results for '{search_query}':\n"
    for i, result in enumerate(top_5_results, 1):
        result_text += f"{i}. {result}\n"
    show_result(result_text)
        

def upload_file():
    webbrowser.open("http://43.205.203.42/task1.html")
    
def object_detection():
    def detect_labels(image_path):
        aws_access_key = 'AKIAQJYDURIUH7ASYGEB'
        aws_secret_key = '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'

        client = boto3.client('rekognition', aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_key, region_name='ap-south-1')

    
        with open(image_path, 'rb') as image_file:
            image_bytes = image_file.read()

        response = client.detect_labels(Image={'Bytes': image_bytes})

        return response['Labels']

    def main():
        image_path = 'test2.jpg'
        labels = detect_labels(image_path)
    
        print("Labels in the image:")
        for label in labels:
            print(f"- {label['Name']} (Confidence: {label['Confidence']:.2f}%)")
            #show_result(- {label['Name']} (Confidence: {label['Confidence']:.2f}%))

    if _name_ == "__main__":
        main()
        
        
        
        
        
        
        
        
def game():
    def speak(text):
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
    
        
    def get_winner(user_choice, computer_choice):
        if user_choice == computer_choice:
            return "It's a tie!"
        elif (
            (user_choice == "rock" and computer_choice == "scissors") or
            (user_choice == "paper" and computer_choice == "rock") or
            (user_choice == "scissors" and computer_choice == "paper")
        ):
            return "You win!"
        else:
            return "Computer wins!"

    def get_hand_gesture(landmarks):
    # Get the tip of the index and middle fingers
        index_finger_tip = landmarks.landmark[8]
        middle_finger_tip = landmarks.landmark[12]

    # Calculate the distance between the two finger tips
        distance = ((middle_finger_tip.x - index_finger_tip.x) ** 2 +
                    (middle_finger_tip.y - index_finger_tip.y) * 2) * 0.5

    # Use the distance to determine the hand gesture
        if distance < 0.05:
            return "rock"
        elif distance < 0.07:
            return "paper"
        else:
            return "scissors"

    def main():
        cap = cv2.VideoCapture(0)

        choices = ["rock", "paper", "scissors"]

        mp_hands = mp.solutions.hands
        hands = mp_hands.Hands()

        while True:
            ret, frame = cap.read()

        # Convert the image to RGB and process it with mediapipe
            image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = hands.process(image_rgb)

            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                # Get the hand gesture from the detected landmarks
                    gesture = get_hand_gesture(hand_landmarks)

                # Display the hand gesture on the screen
                    cv2.putText(frame, gesture.capitalize(), (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

                # Computer's random choice
                    computer_choice = random.choice(choices)

                # Determine the winner and speak the result
                    winner = get_winner(gesture, computer_choice)
                    speak(winner)
                    time.sleep(3)

                    print(f"Your choice: {gesture}")
                    print(f"Computer's choice: {computer_choice}")
                    print(winner)

        # Display the video
            cv2.imshow('Rock Paper Scissors', frame)

        # Exit the game if 'q' is pressed
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()

    if _name_ == "__main__":
        main()
     
        

        
        
def hand_gesture_youtube():
    model = HandDetector()
    cap = cv2.VideoCapture(0)

    while True:
        status, photo = cap.read()
        cv2.imshow("hi", photo)
    
        if cv2.waitKey(100) == 13:
            break
        
        hands, photo = model.findHands(photo, draw=True)
    
        if hands:
            hand = hands[0]
            fingeruplist = model.fingersUp(hand)

            if fingeruplist == [0, 1, 0, 0, 0]: 
                youtube_link = "https://www.youtube.com/live/El_VOjSzvuY?feature=share"
                webbrowser.open(youtube_link)
                time.sleep(2)
            elif fingeruplist == [0, 1, 1, 0, 0]:
                youtube_link = "https://youtu.be/yUB1_sfaGqg"
                webbrowser.open(youtube_link)
                time.sleep(2)
            elif fingeruplist == [0, 1, 1, 1, 0]:
                youtube_link = "https://youtu.be/QN0BfamqA4Y"
                webbrowser.open(youtube_link)
                time.sleep(2)
            elif fingeruplist == [0, 1, 1, 1, 1]:
                youtube_link = "https://youtu.be/fr-MrAln6Y8"
                webbrowser.open(youtube_link)
                time.sleep(2)
            elif fingeruplist == [1, 1, 1, 1, 1]:
                youtube_link = "https://youtu.be/uYyc-9GO91Y"
                webbrowser.open(youtube_link)
                time.sleep(2)
            else:
                print("don't support")
    
    cv2.destroyAllWindows()
    cap.release()
def Building_image():
    #color image
    import cv2
    image3=cv2.imread("blank.jpg")
    photo1_resized = cv2.resize(image3, (700, 500))
    print(photo1_resized.shape)
    #start
    photo1_resized[0:1,:,] = [0]
    #bird
    for x in range(40,50,1):
        for y in range(300,330,x+1):
            photo1_resized[x:x+1,y:y+1,] = [0]
    #road
    photo1_resized[400:500,:,] = [0]
    #road white strip
    for x in range(0,700,100):photo1_resized[440:460,x:x+50,]=[255]
    #poll
    photo1_resized[250:400,20:22]=[0]
    photo1_resized[250:252,3:40]=[0]
    photo1_resized[247:253,0:6]=[0,0,255]
    photo1_resized[247:253,37:43]=[0,0,255]
    #building structure
    photo1_resized[100:400,50:250]=[0,255,255]#BRG
    #building window
    for x in range(120,400,60):photo1_resized[x:x+30,65:130]=[36,x+28,237]
    for x in range(120,400,60):photo1_resized[x:x+30,155:230]=[36,x+28,237]

    #person
    photo1_resized[390:400,270:271]=[0]
    photo1_resized[390:400,274:275]=[0]

    photo1_resized[389:390,266:278]=[0]

    photo1_resized[380:390,265:266]=[0]
    photo1_resized[380:390,277:278]=[0]

    photo1_resized[385:386,260:265]=[0]
    photo1_resized[385:386,277:282]=[0]

    photo1_resized[379:380,266:278]=[0]

    photo1_resized[373:379,270:271]=[0]
    photo1_resized[373:379,274:275]=[0]

    photo1_resized[372:373,270:274]=[0]

    photo1_resized[375:378,273:274]=[36,28,237]

    #poll
    photo1_resized[250:400,300:302]=[0]
    photo1_resized[250:252,280:320]=[0]
    photo1_resized[247:253,277:283]=[0,0,255]
    photo1_resized[247:253,317:323]=[0,0,255]

    #glass building
    photo1_resized[150:400,350:600]=[234,217,153]#BRG
    for x in range(370,590,30):
        photo1_resized[150:400,x:x+1]=[0]
    for x in range(180,400,30):
        photo1_resized[x:x+1,350:600]=[0]
    #poll
    photo1_resized[250:400,650:652]=[0]
    photo1_resized[250:252,630:670]=[0]
    photo1_resized[247:253,627:633]=[0,0,255]
    photo1_resized[247:253,667:673]=[0,0,255]


    cv2.imshow("building image",photo1_resized)
    cv2.waitKey()
    cv2.destroyAllWindows()    

def animated():    
    import cv2
    import numpy as np

    def cartoonize_image(image, gray_mode=False):
    # Convert image to grayscale
        if gray_mode:
            gray = image
        else:
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Apply median blur to reduce noise and smooth the image
        gray = cv2.medianBlur(gray, 5)
    
    # Detect edges in the image using adaptive thresholding
        edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
    
    # Create a color version of the image
        color = cv2.bilateralFilter(image, 9, 300, 300)
    
    # Combine the edges with the color image using a bitwise AND operation
        cartoon = cv2.bitwise_and(color, color, mask=edges)
    
        return cartoon

    def cartoonize_video():
    # Start video capture
        cap = cv2.VideoCapture(0)
    
        while True:
            ret, frame = cap.read()
            if not ret:
                break
        
        # Flip the frame horizontally for a more intuitive selfie view
            frame = cv2.flip(frame, 1)
        
        # Apply cartoonize effect to the frame
            cartoon_frame = cartoonize_image(frame)
        
        # Show the original and cartoonized frames side by side
            stacked_frames = np.hstack((frame, cartoon_frame))
            cv2.imshow("Cartoonizer", stacked_frames)
        
        # Press 'q' to exit the loop
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    
    # Release video capture and destroy windows
        cap.release()
        cv2.destroyAllWindows()

    if _name_ == "__main__":
        cartoonize_video()    


    
def open_web_page():
    url = "http://13.233.186.36/new.html" # Replace this with your desired web page URL
    webbrowser.open(url)

    


def create_button(parent, label, command):
    button = tk.Button(parent,font=("Arial",10,"bold"), text=label,width=20,height=2, command=command)
    return button


root = tk.Tk()
root.title("Main Window")
root.geometry("1200x900")
root.configure(bg="light blue")

title_label = tk.Label(root, text="Welcome to TryHards Menu",width=30,height=2, font="title_font", fg="black")
title_label.pack(pady=15)



buttons_frame = tk.Frame(root, bg="lightblue")
buttons_frame.pack(padx=20, pady=20, fill="both", expand=True)

button_ram = create_button(buttons_frame, "Find RAM Usage", command=lambda: show_result(f"RAM memory % used: {psutil.virtual_memory().percent}\nRAM Used (GB): {psutil.virtual_memory().used / 1000000000}"))
    
button_notepad = create_button(buttons_frame, "NOTEPAD",lambda: open_software("notepad"))
button_calculator = create_button(buttons_frame, "CALCULATOR", lambda: open_software("calculator"))
button_paint = create_button(buttons_frame, "PAINT", lambda: open_software("paint"))
button_chrome = create_button(buttons_frame, "CHROME", lambda: open_software("chrome"))
button_cmd = create_button(buttons_frame, "COMMAND PROMPT", lambda: open_software("command prompt"))
button_explorer = create_button(buttons_frame, "EXPLORER", lambda: open_software("explorer"))
button_object_detection = create_button(buttons_frame, "OBJECT DETECTION",object_detection)
button_taskmgr = create_button(buttons_frame, "TASK MANAGER",lambda: os.system("taskmgr"))
button_whatsapp = create_button(buttons_frame, "SEND WHATSAPP", whatsapp)
button_email = create_button(buttons_frame, "SEND EMAIl", Email)
button_message = create_button(buttons_frame, "SEND MESSAGE", message)
button_photo = create_button(buttons_frame, "CLICK PHOTO",click_photo)
button_croppic = create_button(buttons_frame, "CROP PHOTO",crop_pic)
button_video = create_button(buttons_frame, "CAPTURE VIDEO",capture_video)
button_cropvideo = create_button(buttons_frame,"CROP VIDEO",capture_crop_video)
button_image= create_button(buttons_frame,"BUILDING IMAGE",Building_image)
button_coordinates = create_button(buttons_frame,"GEO COORDINATES" ,lambda:get_coordinates())
button_searchresults = create_button(buttons_frame,"5 GOOGLE SEARCH",google_search)
button_launchinstance = create_button(buttons_frame,"LAUNCH INSTANCE",launch_instance)
button_createbucket = create_button(buttons_frame,"CREATE BUCKET",create_bucket)
button_uploadfile = create_button(buttons_frame,"UPLOAD FILE",upload_file)
button_handgesture = create_button(buttons_frame,"HAND GESTURE",hand_gesture_youtube)
button_game = create_button(buttons_frame,"ROCK PAPER SCISSOR",game)
button_animated = create_button(buttons_frame,"ANIMATED",animated)

button_notepad.grid(row=0, column=0, padx=100, pady=20)
button_calculator.grid(row=0, column=1, padx=100, pady=20)
button_paint.grid(row=0, column=2, padx=100, pady=20)
button_chrome.grid(row=0, column=3, padx=100, pady=20)
button_cmd.grid(row=1, column=0, padx=20, pady=20)
button_explorer.grid(row=1, column=1, padx=30, pady=20)
button_ram.grid(row=1, column=2, padx=10, pady=20)
button_taskmgr.grid(row=1, column=3, padx=10, pady=20)
button_whatsapp.grid(row=2, column=0, padx=20, pady=20)
button_email.grid(row=2, column=0, padx=20, pady=20)
button_message.grid(row=2, column=1, padx=30, pady=20)
button_photo.grid(row=2, column=2, padx=20, pady=20)
button_croppic.grid(row=2, column=3, padx=30, pady=20)
button_video.grid(row=3, column=0, padx=40, pady=20)
button_cropvideo.grid(row=3, column=1, padx=50, pady=20)
button_image.grid(row=3, column=2,padx=40, pady=20)
button_coordinates.grid(row=3, column=3, padx=50, pady=20)
button_searchresults.grid(row=4, column=0, padx=40, pady=20) 
button_launchinstance.grid(row=4, column=1, padx=40, pady=20)
button_createbucket.grid(row=4, column=2, padx=40, pady=20)
button_uploadfile.grid(row=4, column=3, padx=40, pady=20)
button_handgesture.grid(row=5, column=0, padx=40, pady=20)
button_object_detection.grid(row=5, column=1, padx=50, pady=20)
button_animated.grid(row=5, column=2, padx=50, pady=20)
button_game.grid(row=5, column=3, padx=50, pady=20)


root.mainloop()
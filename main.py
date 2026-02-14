import smtplib
import os
import ssl
import dotenv

dotenv.load_dotenv()
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
SENDER_EMAIL = 'minhduc6e12@gmail.com'
APP_PASS  = os.getenv('app_pass')  
RECEIVER_EMAIL = 'minhduc1q2w@gmail.com'

def main():
    print(f"--- Connecting to {SMTP_SERVER}... ---")
    
    # Tạo kết nối
    context = ssl.create_default_context()
    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.set_debuglevel(1)  #print debug output
        
        # start
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(SENDER_EMAIL, APP_PASS) #auth login
        
        # Soạn nội dung (Đây là phần DATA)
        msg = f"""  Subject: Email Test Protocol
                    From: {SENDER_EMAIL}
                    To: {RECEIVER_EMAIL}

                    Hi from the second tesst
            """
        #send
        server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, msg)
        
        print("\n>>> Success <<<")
        server.quit()
    except Exception as e:  
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
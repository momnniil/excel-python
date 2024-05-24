import cv2
import mediapipe as mp
import numpy as np
import time
import os



# mp_hands = mp.solutions.hands       
# hands = mp_hands.Hands()

data_collection = []
collecting =False
start_time = None
filename = input("enter filename for data: ")
save_path = "dataset_mp/"+filename

cap = cv2.VideoCapture(0)
if not os.path.exists("dataset_mp"):
     os.makedirs("dataset_mp")

def compute_distances(landmarks):
     distances =[]
     pairs = [(0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(0,7),(0,8),(0,9),(0,10),(0,11),(0,12),(0,13),(0,14),(0,15),(0,16),(0,17),(0,18),(0,19),(0,20),(4,8),(8,12),(12,16),(16,20)]
     reference_pair = (0,9)

     lm = landmarks.landmark

     ref_1 = np.array([lm[reference_pair[0]].x,lm[reference_pair[0]].y])
     ref_2 = np.array([lm[reference_pair[1]].x,lm[reference_pair[1]].y])

     reference_distance = np.linalg.norm(ref_1-ref_2)

     for pair in pairs:
          p1 = np.array(lm[pair[0].x,lm[pair[0]].y]) 
          p2 = np.array(lm[pair[1].x,lm[pair[1]].y]) 
          distance = np.linalg.norm(p1-p2)/reference_distance
          distances.append(distance)
     return distances



while True:
    ret,img = cap.read()
    if not ret:
        continue
    
    # img_rgb = cv2.cvtColor(img, cv2.COLOR_BAYER_BG2BGR)
    # result = hands.process(img_rgb)

    
    #         data_collection.append(distances)
    if not collecting:
        cv2.putText(img,"press space to collect data",(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
    else:
        elapsed_time = int(time.time()-start_time)
        remaining_time = 10-elapsed_time
        cv2.putText(img,f"remaining time{remaining_time}",(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
        if elapsed_time >= 10:
            break

    cv2.imshow('img',img)
    if cv2.waitKey(1) == ord(' ') and not collecting:
        collecting = True
        start_time = time.time()
    if cv2.waitKey(1)==ord('q'):
          break
np.save(save_path,np.array(data_collection))
print("success")



     






# # while True:
# #     ret, img= cap.read()
# #     if ret:
# #         cv2.imshow('img',img)
# #         imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
# #         result = hands.process(img)
# #         print(result.multi_hand_landmarks)

# #     if cv2.waitkey(1)==ord('q'):
# #         break
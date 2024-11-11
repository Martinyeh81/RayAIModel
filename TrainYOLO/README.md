# Question 3 and 4 

|Packages|Version|
|---|---|
|Python|3.11.9|
|Ray|2.20.0|
|ultralytics|8.3.27|
  
## Data
  1. The data is from Kaggle(https://www.kaggle.com/code/pkdarabi/traffic-signs-detection-using-yolov8)
  2. 總共15種Labels
  3. 圖片為416 x 416 pixels x 3 channels
  4. 使用labelImg(https://github.com/HumanSignal/labelImg?fbclid=IwY2xjawGe_fFleHRuA2FlbQIxMAABHS9x4cSMEli4qSIB_AObBBZEo5meAJX_K5yjCMdmhMspUnwcgqpUmeNtOg_aem_gRo9maKcgYEnivzIhATJaw) 畫BoundingBox並產生出yolo format(COCO format)
    
  ![Sign](https://github.com/Martinyeh81/RayAIModel/blob/main/RayXSquare/Images/RayIP.png)
  ![RayDashboardIP](https://github.com/Martinyeh81/RayAIModel/blob/main/RayXSquare/Images/RayDashboardIP.png)
## Number of calsses
  執行RayRetry.py，總共for迴圈整個流程，但讓unstable_task function有50%的機率失敗，並且最多重複三次，超過就停止
  ![Task1](https://github.com/Martinyeh81/RayAIModel/blob/main/UnstableTask/Images/question2task.png)
  ![Task2](https://github.com/Martinyeh81/RayAIModel/blob/main/UnstableTask/Images/question2answer.png)
## 答案
  ![Answer2](https://github.com/Martinyeh81/RayAIModel/blob/main/UnstableTask/Images/question2finalanswer.png)

# AWS Lambda - Quick Notes 🚀

## 📌 What is AWS Lambda?
AWS Lambda is a **serverless computing service** that allows you to run code **without managing servers**. It automatically executes functions in response to **events** and scales based on demand.

## 🔥 Key Features:
- **Serverless & Fully Managed** – No need to manage infrastructure.
- **Event-Driven Execution** – Runs only when triggered by an event.
- **Automatic Scaling** – Handles multiple requests simultaneously.
- **Pay-as-You-Go** – Charges only for execution time.
- **Multi-Language Support** – Works with Python, Node.js, Java, etc.
- **AWS Service Integration** – Easily connects with S3, DynamoDB, API Gateway, and more.

---

## 🔄 Event-Driven Architecture  
Imagine a **doorbell** at your house. The bell **only rings** when someone presses the button—this is an **event**.

- In AWS Lambda, an event could be:
  - Uploading a file to **S3**
  - Inserting data into **DynamoDB**
  - An **API request** via API Gateway
- Lambda **only runs when triggered**, saving resources and costs.

### ✅ Example:  
📸 **Image Processing**  
1. A user uploads an image to **Amazon S3**.  
2. The S3 event **triggers** a Lambda function.  
3. Lambda resizes the image and stores it in another S3 bucket.  

---

## 📈 Automatic Scaling  
Think of a **pizza shop**:  
- If **1** customer comes, **1** chef is enough.  
- If **100** customers arrive, you automatically bring in **more chefs** to serve them quickly.

Similarly, AWS Lambda:
- **Scales automatically** based on incoming events.
- Runs multiple function instances **at the same time**.
- Handles **1 request or 1 million requests** efficiently.

### ✅ Example:
If 10 users upload photos at once, Lambda **processes all 10 images at the same time** without delays.

---

## 🎯 Benefits:
✅ **No server management**  
✅ **Cost-effective** (pay only for what you use)  
✅ **High availability & scalability**  
✅ **Event-driven, real-time processing**  

❌ **Limitations**:
- **Execution time limit** (Max 15 mins per function)  
- **Cold start latency** (Slight delay when not used for a while)  
- **Temporary storage limit** (512 MB per function)  

---

## 📚 Learn More:
🔗 [AWS Lambda Documentation](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html)  
🔗 [AWS Free Tier](https://aws.amazon.com/free/)  

---

🚀 **Enjoy building with AWS Lambda!** 🚀

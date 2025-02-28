# AWS Lambda - Notes 

##  What is AWS Lambda?
AWS Lambda is a **serverless computing service** that automatically manages infrastructure, allowing you to run code without provisioning or managing servers. It executes code in response to events and automatically scales based on the workload.

## 🔥 Key Features:
- **Serverless & Fully Managed** – No need to manage infrastructure.
- **Event-Driven Execution** – Runs only when triggered by an event.
- **Automatic Scaling** – Handles multiple requests simultaneously.
- **Pay-as-You-Go** – Charges only for execution time.
- **Multi-Language Support** – Works with Python, Node.js, Java, etc.
- **AWS Service Integration** – Easily connects with ec2, S3, DynamoDB, API Gateway, and more.

---

## How it Works:
1. Write the code as a function.
2. Upload the code to AWS Lambda.
3. Configure triggers (event sources like S3, API Gateway, etc.).
4. Lambda automatically executes the function when the event occurs.
5. Monitor the execution through CloudWatch Logs.

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
🔗 [boto3 docs](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)  
🔗 [boto3 s3 docs](https://boto3.amazonaws.com/v1/documentation/api/1.9.42/guide/s3-example-creating-buckets.html/)  
🔗 [boto3 s3 docs](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html/)  


---



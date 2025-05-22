# ☁️ Serverless Contact Form on AWS (Free Tier)

This project demonstrates how to build a **fully serverless contact form** on AWS using Free Tier services. It combines static web hosting, API Gateway, AWS Lambda, and Amazon SES to collect and deliver contact messages via email — all without managing a single server.



## 🚀 Features

- 🌐 Static front-end hosted on **Amazon S3** + **CloudFront**
- 📮 Form submission via **API Gateway** and **AWS Lambda**
- 📬 Email delivery through **Amazon SES**
- 🔐 Secure access using **IAM roles with least-privilege**
- 💸 100% within the AWS Free Tier



### 🔁 Data Flow

1. **User visits the website** hosted on CloudFront, backed by an S3 bucket.
2. **User submits the contact form**, triggering a `fetch()` request to an API Gateway endpoint.
3. **API Gateway invokes a Lambda function**, which parses the form data.
4. **Lambda sends an email** via Amazon SES.



## 🧱 AWS Services Used

| Service         | Purpose                          |
|--|-|
| **S3**          | Hosts the static website         |
| **CloudFront**  | CDN for global delivery & HTTPS  |
| **Lambda**      | Handles form processing          |
| **API Gateway** | Provides RESTful endpoint         |
| **SES**         | Sends email notifications        |
| **IAM**         | Manages secure access            |



## 🧪 Setup Instructions

### ✅ Prerequisites

- AWS account with Free Tier access
- Domain email address for SES (Gmail, Outlook, etc.)
- Basic knowledge of AWS Console and HTML/JavaScript



### 📄 Step 1: Create the HTML Contact Form

Create a simple form with:

- Name (text)
- Email (email)
- Message (textarea)

Use JavaScript `fetch()` to POST the form data to your API Gateway endpoint.



### 🪣 Step 2: Upload to Amazon S3

1. Create an S3 bucket with a unique name.
2. Since I used OAC not enabling **static website hosting**.
3. Upload `login.html` and other static assets.
4. (If not using OAC) Disable **Block Public Access** and attach a public-read policy.


### 🌍 Step 3: Set Up CloudFront

1. Navigate to the CloudFront service in the AWS Console.
2. Click **Create Distribution**.
3. Under **Origin domain**, select your S3 bucket (or paste its static hosting endpoint).
4. Set the **Default root object** to `login.html`.
5. (Optional) Enable compression and viewer protocol policy (e.g., Redirect HTTP to HTTPS).
6. Click **Create distribution** and wait for deployment to finish.
7. Copy the **CloudFront domain name** (e.g., `https://d1234abcd.cloudfront.net`) — this will be your public website URL.
8. In error page, add 403 and 404 error redirection.



### 🧠 Step 4: Create the Lambda Function

1. Go to the **Lambda** service in AWS Console.
2. Click **Create function** → Choose **Author from scratch**.
3. Name your function `ContactFormHandler`.
4. Select **Python 3.11** as the runtime.
5. Create a new execution role or choose an existing one with basic Lambda permissions.
6. After the function is created, deploy your Python code that parses the request and sends an email via Amazon SES.
7. Set the function handler to `lambda_function.lambda_handler`.
8. Adjust the **timeout** to 3 seconds and **memory** to 128MB under the Configuration tab.



### 🔐 Step 5: IAM Permissions for Lambda

1. Navigate to **IAM > Roles** in the AWS Console.
2. Find and select the role automatically created for your Lambda function (e.g., `ContactFormHandler-role-*`).
3. Under the **Permissions** tab, click **Add inline policy**.
4. Use the visual editor or JSON tab to add permissions that allow `ses:SendEmail`.
5. Save the policy and confirm it appears under the attached permissions list for the role.



### ✉️ Step 6: Configure Amazon SES

1. Open **Amazon SES** in the AWS Console and go to **Verified Identities**.
2. Click **Create Identity** and choose **Email Address**.
3. Enter and submit the email address you want to verify (must be accessible).
4. Check your inbox and click the verification link sent by AWS.
5. Repeat this process for both the sender and recipient email addresses (if different).
6. Make sure SES is in the same AWS Region as your Lambda function (e.g., `us-west-1`).



### 🔁 Step 7: Test Lambda Function Manually

1. Go back to your Lambda function and click the **Test** tab.
2. Create a new test event with sample contact form data in JSON format.
3. Run the test and check the **Execution results**.
4. Navigate to **CloudWatch Logs** to confirm the email was sent (look for a `MessageId`).



### 🔌 Step 8: Create API Gateway HTTP API

1. Open **API Gateway** and select **Create API** → Choose **HTTP API**.
2. Set up a route: `POST /contact`.
3. Add integration: select **Lambda function** and choose `ContactFormHandler`.
4. Enable **CORS**:
   - Allowed Origins: your CloudFront domain
   - Allowed Methods: `POST`
   - Allowed Headers: `Content-Type`
5. Create a **deployment stage** (e.g., `prod`) and deploy the API.
6. Copy the **API endpoint URL** — you’ll use this in your HTML form’s JavaScript.

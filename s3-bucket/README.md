## Hosting a Static Website on Amazon S3 Using CloudFront with OAC

### Objective
Securely host a static website using Amazon S3 and serve it globally through CloudFront, leveraging **Origin Access Control (OAC)** to keep the S3 bucket private.

---

### Steps & Key Observations

#### 1. S3 Bucket Setup
- Created an S3 bucket in the preferred AWS region.
- Uploaded static site content, including `index.html`, to the root.
- **Did not enable public access** or S3 static website hosting (to enhance security).

#### 2. Understanding S3 Static Website Hosting
- S3 can serve static websites using a special website endpoint.
- However, this requires public access, which is not secure for production.

#### 3. CloudFront Distribution with OAC
- Created a CloudFront distribution with the S3 bucket as the origin.
- Chose the **"Single page application"** behavior.
- Enabled **Origin Access Control (OAC)** to grant CloudFront secure access.
- CloudFront automatically generated and attached a bucket policy using `AWS:SourceArn`.

#### 4. CloudFront Configuration Highlights
- Default cache behavior was sufficient for static content.
- Skipped AWS WAF and Shield to remain in the Free Tier.

#### 5. Handling `index.html` as Root Document
- Since S3 static hosting is disabled, `index.html` isn't automatically served.
- Configured CloudFront custom error responses:
  - `403 Forbidden` → `/index.html`
  - `404 Not Found` → `/index.html`
- This simulates single-page application (SPA) routing.

#### 6. Final Result
- Website is accessible via CloudFront domain (e.g., `https://d123abc4xyz567.cloudfront.net`).
- Content is secure, fast, and scalable.

---

### Key Takeaways
- S3 static hosting is easy but not secure without public access.
- **CloudFront + OAC** enables secure static hosting with global delivery.
- OAC is the modern, IAM-integrated alternative to OAI.
- Custom error responses are critical for SPA routing in private S3 setups.

---

###  Architecture Diagram
(See image in repo: `architecture.png`)

```
[ User ]
   ⬇
[ CloudFront (OAC) ]
   ⬇
[ S3 Bucket (Private, No Static Hosting) ]
```

---

### Deployment Notes
- Use `aws s3 cp` to upload content.
- Use `aws cloudfront create-distribution` or Console for setup.
- Test through CloudFront domain after cache invalidation if needed.

---

### Last Updated: May 2025

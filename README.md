# DreamTalk Optimized

This project generates high-quality talking avatar videos from an image and script.

## Setup

### 1) Backend
```bash
cd ..
cd backend
pip install -r requirements.txt
python app.py
```

### 2) Frontend
```bash
cd frontend
npm install
npm start
```

### 3) Run model in Google Colab
1. Upload `DreamTalk_colab.ipynb` to Google Colab and run all cells.
2. The notebook will wait for incoming jobs (example):

<img src="https://github.com/user-attachments/assets/188e804c-cf12-488b-82f7-f0aa3e136580" alt="Colab waiting for job"/>

3. On the website:
   - Paste your script in the **Script Content** box.
   - Upload your image in the **Avatar Image** field.
4. After generation (around 20 minutes), you will receive a high-quality video.

## Example Result

### Input image
<img src="https://github.com/user-attachments/assets/e273dfae-19b0-47d7-92e3-d48180783ba4" alt="Input image"/>

### Output videos

#### Original (without enhancement) :

<div style="text-align: center;">
   <video src="https://github.com/user-attachments/assets/2f80d54d-68bf-43ad-b384-03cc05fcece8" controls width="100%"></video>
</div>


#### Upscaled Video :

<div style="text-align: center;">
   <video width="20px" height= "10px" src="https://github.com/user-attachments/assets/4e10deb0-e443-477c-b8f8-6ec800e3fe97" controls width="100%"></video>
</div>


## 🌐 Usage
- Register or log in via the web interface.
- Upload an image and enter your script.
- Generate and preview/download your talking avatar video.
- View your generation history in the dashboard.

## 🔧 API Endpoints (Backend)
- `POST /api/auth/register` — Register a new user
- `POST /api/auth/login` — User login
- `POST /api/generate_avatar` — Generate avatar video
- `GET /api/history` — Get user’s generation history
- `GET /api/dashboard` — Get dashboard stats

## 📊 Database Schema (Example)
**Users Collection:**
```json
{
  "_id": "uuid",
  "email": "user@example.com",
  "password": "hashed_password",
  "created_at": "datetime"
}
```
**Generations Collection:**
```json
{
  "_id": "uuid",
  "user_id": "user_uuid",
  "text": "script text",
  "image_file": "filename.jpg",
  "audio_file": "filename.wav",
  "video_file": "filename.mp4",
  "created_at": "datetime",
  "status": "completed|processing|failed"
}
```

## 🔒 Security
- JWT-based authentication
- Password hashing (bcrypt)
- CORS and input validation

## 🚀 Deployment
- **Frontend:**
  ```bash
  cd frontend
  npm run build
  # Deploy the build/ folder to your static hosting
  ```
- **Backend:**
  ```bash
  cd backend
  gunicorn -w 4 -b 0.0.0.0:5001 app:app
  # Or use your preferred WSGI server
  ```

## 🤝 Contributing
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📝 License
This project is licensed under the MIT License.

## 🆘 Support
For support, please open an issue in the repository or contact the development team.

---
**Happy Avatar Generating! 🎭✨** -->











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
- Original (without enhancement): *(add video link/path)*
- Enhanced: *(add video link/path)*

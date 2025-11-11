# 🧠 AI Blog Generator

This project automatically generates high-quality blog articles using **Google Gemini AI**.  
You simply enter a list of titles (optionally with details), and the backend generates complete blog posts that are saved and displayed under `/blog`.

---

## 🚀 Features

✅ Generate full blog articles from just titles  
✅ Uses **Gemini Pro API** for high-quality content  
✅ FastAPI backend for API management  
✅ Simple frontend (HTML + JS) for interaction  
✅ Blog listing page with auto-refresh  
✅ Supports multiple article generation in one go  

---

## 🏗️ Project Structure

```
article_generator/
│
├── app/
│   ├── main.py              # FastAPI entry point (routes + server)
│   ├── generator.py         # Handles Gemini API calls
│   ├── models.py            # (Optional) Data models / Post schema
│
├── static/
│   ├── index.html           # Frontend UI for title input + generation
│   ├── blog.js              # Handles fetching + displaying posts
│   ├── style.css            # Styling for the frontend
│
├── .env                     # to store GEMINI_API_KEY
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository
```bash
https://github.com/srkthe27/Article_Generator.git
cd Article_Generator
```

### 2️⃣ Create & activate a virtual environment
```bash
python -m venv .venv
.\.venv\Scripts\activate      # On Windows
# or
source .venv/bin/activate     # On macOS/Linux
```

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Set up your Gemini API Key

```

#### via `.env` file
Create a `.env` file in the project root:

```
GEMINI_API_KEY=YOUR_REAL_API_KEY_HERE
```
---

## ▶️ Run the Server

Start your FastAPI server:
```bash
uvicorn app.main:app --reload
```

You’ll see logs like:
```
INFO:     Uvicorn running on http://127.0.0.1:8000
```

Then open [http://localhost:8000](http://localhost:8000) in your browser.

---

## 💻 How to Use

1. Visit `/` — you’ll see a text area to enter titles.  
   Format:
   ```
   Python for Beginners || include intro and key concepts
   Machine Learning Basics || overview with examples
   Future of Web Development
   ```

2. Click **“Generate Articles”**  
   → The backend sends your list to Gemini and returns full articles.  
   → The blog posts appear automatically under `/blog`.

---

## 🧱 API Endpoints

| Method | Endpoint | Description |
|---------|-----------|-------------|
| `GET` | `/api/posts` | Get all generated posts |
| `POST` | `/api/generate` | Generate articles from titles/details |
| `GET` | `/` | Frontend UI |

**Example POST body:**
```json
{
  "items": [
    { "title": "Intro to Python", "details": "Explain data types and variables" },
    { "title": "AI in Healthcare" }
  ]
}
```

---

## 🧠 Example Prompt Logic

The backend builds a combined prompt like:
```
Write a 500-word blog article titled "Intro to Python".
Explain data types, variables, and simple examples.
Make it engaging for beginners.
```

Gemini API returns the blog body, which is stored and displayed in `/blog`.

---

## 📦 Example Output

```
### Python for Beginners

Python is one of the most popular programming languages...
...
```

---

## 🧰 Tech Stack

- **Frontend:** HTML, CSS, JavaScript (Vanilla)
- **Backend:** FastAPI (Python)
- **AI Model:** Google Gemini Pro
- **HTTP Client:** httpx
- **Data Storage:** JSON / In-memory

---

## 🪄 Troubleshooting

| Issue | Cause | Fix |
|--------|--------|-----|
| 401 Unauthorized | Invalid or missing API key | Set correct `GEMINI_API_KEY` |
| 11001 getaddrinfo failed | No internet or wrong URL | Check your network & endpoint |
| Empty blog list | No generated posts yet | Click “Generate Articles” |

---

## 🧑‍💻 Future Improvements

- Add Markdown formatting for blogs  
- Add SQLite or MongoDB for persistent storage  
- Add authentication for admin posting  
- Add support for OpenAI or Mistral fallback  

---

## 🪪 License

This project is open-source under the **MIT License**.

---

### ✨ Author
**SRKTM**  
Project: *AI Blog Generator*  
FastAPI • Gemini • HTML/CSS

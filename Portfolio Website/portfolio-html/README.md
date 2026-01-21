# 🚀 Python-Based Portfolio Website - NO Node.js Required!

## What's This?
Instead of Next.js/React that requires Node.js, I've created a **pure HTML/CSS/JavaScript portfolio** that you can run with just Python.

## ✨ Features
✅ **No Node.js needed** - Just Python (already installed!)  
✅ **Fully responsive** - Mobile, tablet, and desktop  
✅ **Modern design** - Blue and amber gradient theme  
✅ **Smooth animations** - Scroll effects and transitions  
✅ **Fast loading** - Pure HTML, no build process  
✅ **Easy to customize** - Edit the HTML file directly  

## 🎯 How to Run

### Option 1: Python Script (Recommended)
```bash
python run.py
```
This will:
- Start the server on `http://localhost:3000`
- Automatically open your browser
- Show helpful status messages

### Option 2: Python Built-in Server
```bash
python -m http.server 3000
```
Then open: `http://localhost:3000`

### Option 3: From Any Directory
Navigate to the portfolio-html folder, then:
```bash
cd "c:\Users\GHOSIA\OneDrive\Desktop\Kaggle dataset Mastery\Portfolio Website\portfolio-html"
python run.py
```

## 📝 Customization

Edit `index.html` to customize:
- **Name & Title**: Line 380 (`<h1>Ayesha</h1>`)
- **Bio/Description**: Line 381-382
- **Email**: Search for `ayesha@example.com`
- **LinkedIn/GitHub**: Search for social links
- **Projects**: Update portfolio section (line 640+)
- **Services**: Update services section (line 570+)
- **Colors**: Modify `#3B82F6` (blue) and `#F59E0B` (amber)

## 📂 File Structure
```
portfolio-html/
├── index.html      ← Your entire portfolio website
├── run.py         ← Python server script
└── README.md      ← This file
```

## 🎨 Sections Included
- ✅ Hero section with CTA buttons
- ✅ About section with bio, stats, and skills
- ✅ Services section with offerings
- ✅ Portfolio section with project cards
- ✅ Contact section with form and social links
- ✅ Responsive navigation bar

## 🌐 Browser Support
- Chrome ✅
- Firefox ✅
- Safari ✅
- Edge ✅
- Mobile browsers ✅

## 🔧 Troubleshooting

**Port 3000 already in use?**
```bash
python -m http.server 5000
```
Then go to `http://localhost:5000`

**Can't run python?**
Make sure Python 3 is installed: `python --version`

**Website not loading?**
- Check you're in the correct directory
- Try refreshing the browser (Ctrl+F5 or Cmd+Shift+R)
- Check the server output for errors

## 🚀 Future Enhancements
Add to `index.html` if needed:
- Blog page (markdown to HTML converter)
- Dark mode toggle
- Contact form backend
- Image gallery lightbox
- PDF download (resume/CV)

---

**That's it!** No Node.js, no npm, no build process. Just pure Python and HTML. 🎉

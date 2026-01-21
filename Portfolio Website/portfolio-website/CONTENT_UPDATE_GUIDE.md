# CONTENT_UPDATE_GUIDE.md

## Quick Reference for Content Updates

### 📊 Where Each Content Type Lives

| Content Type | File Location | How to Update |
|---|---|---|
| Name, Title, Bio | `src/data/portfolio.js` | Edit properties |
| Profile Photo | `public/images/profile.jpg` | Replace file |
| Services | `src/data/portfolio.js` | Edit services array |
| Projects | `src/data/portfolio.js` | Edit projects array |
| Tutorials | `content/tutorials/*.md` | Create/edit .md files |
| Blogs | `content/blogs/*.md` | Create/edit .md files |
| Contact Info | `src/components/Contact.js` | Edit links |
| Colors | `tailwind.config.js` | Edit color values |

---

## 🔄 How to Update Each Section

### Updating Your Bio

**File:** `src/data/portfolio.js`

```javascript
bio: {
  short: "Quick one-liner about you",
  full: "Longer biography with 2-3 paragraphs. Can include:\n- Your background\n- Key achievements\n- Your approach\n- Fun facts"
}
```

**Pro tip:** Keep it focused on what you do and why clients should hire you.

### Adding a New Project

**File:** `src/data/portfolio.js`

```javascript
projects: [
  // ... existing projects
  {
    id: 5,
    title: "Your Project Name",
    description: "What this project does and the impact it had",
    technologies: ["Tech1", "Tech2", "Tech3"],
    image: "/images/your-project.png",
    link: "https://link-to-project"
  }
]
```

**Steps:**
1. Add a new object to the `projects` array
2. Give it a unique `id`
3. Screenshot your project or find an image
4. Save image to `public/images/your-project.png`
5. Add project object above
6. Save and reload browser

### Adding a Tutorial

**File:** Create `content/tutorials/my-tutorial.md`

```markdown
---
title: My Tutorial Name
date: 2024-02-01
readingTime: 10
category: Python
excerpt: A brief description (1-2 sentences)
---

# My Tutorial Title

## What You'll Learn

Start with an intro...

## Section 1

Your content...

### Code Example

\`\`\`python
# Your code here
\`\`\`

## Section 2

More content...

## Conclusion

Summary and next steps...
```

**Pro tips:**
- `readingTime` is estimated time to read (in minutes)
- `category` can be: Python, SQL, ML, Visualization, etc.
- Use code blocks with backticks for code
- Include practical examples

### Adding a Blog Post

Same as tutorial but save to `content/blogs/my-blog.md`

```markdown
---
title: Blog Post Title
date: 2024-02-01
readingTime: 12
category: Insights
excerpt: Brief excerpt (1-2 sentences)
---

# Blog Post Title

Your blog content...
```

### Updating Services

**File:** `src/data/portfolio.js`

```javascript
services: [
  {
    id: 1,
    icon: "📊",
    title: "Service Name",
    description: "Clear description of what you offer"
  },
  // Add more services...
]
```

**Icon Ideas:**
- Data: 📊 📈 💾 📉 🎯
- Cleaning: 🧹 ✨ 🧽 🔧
- Learning: 🤖 🧠 📚 🎓
- Tools: 💻 🔍 📱 🛠️

### Updating Skills (About Section)

**File:** `src/components/About.js`

Find this array and update:

```javascript
{['Python', 'SQL', 'Pandas', 'scikit-learn', 'Tableau', 'Power BI', 'Excel', 'Machine Learning'].map((skill) => (
  // Your skills here
))}
```

Replace with your actual skills.

### Updating Stats (About Section)

**File:** `src/components/About.js`

Find and update these hardcoded values:

```javascript
<p className="text-2xl font-bold text-blue-600">10+</p>  // ← Number
<p className="text-gray-700">Projects Completed</p>      // ← Label
```

### Updating Contact Information

**File:** `src/components/Contact.js`

Search and replace:
- `ayesha@example.com` → Your email
- `linkedin.com/in/ayesha` → Your LinkedIn URL
- `github.com/ayesha` → Your GitHub URL

### Updating Navigation

**File:** `src/components/Navbar.js`

Current sections: home, about, services, portfolio, tutorials, contact

To add a section:
1. Create new component
2. Add to navbar navigation array
3. Update main page to include it

---

## 📸 Image Management

### Supported Formats
- JPG/JPEG
- PNG
- WebP

### Where to Save
```
public/
└── images/
    ├── profile.jpg
    ├── project1.png
    ├── project2.png
    └── hero.png
```

### Image Sizes (Recommended)
- Profile photo: 400x400px
- Project screenshots: 800x600px or 1200x800px
- Hero image: 1920x1080px

### How to Optimize
1. **Use TinyPNG:** [tinypng.com](https://tinypng.com) - Free compression
2. **Use ImageOptim:** [imageoptim.com](https://imageoptim.com)
3. **Use Photopea:** [photopea.com](https://photopea.com) - Free online editor

### Using Images in Components

```javascript
// In a component
<img src="/images/filename.png" alt="Descriptive text" />

// Or with Next.js Image component
import Image from 'next/image';

<Image 
  src="/images/filename.png" 
  alt="Descriptive text"
  width={800}
  height={600}
/>
```

---

## 🎨 Customizing Appearance

### Change Color Scheme

**File:** `tailwind.config.js`

```javascript
colors: {
  primary: '#1F2937',      // Main dark color
  secondary: '#3B82F6',    // Main accent color
  accent: '#F59E0B',       // Secondary accent
  light: '#F9FAFB',        // Light background
  dark: '#111827',         // Dark background
}
```

**Color Palette Suggestions:**

Blue + Orange (Current):
```javascript
secondary: '#3B82F6',    // Blue
accent: '#F59E0B',       // Orange
```

Purple + Pink:
```javascript
secondary: '#8B5CF6',    // Purple
accent: '#EC4899',       // Pink
```

Green + Teal:
```javascript
secondary: '#10B981',    // Green
accent: '#06B6D4',       // Teal
```

### Change Fonts

**File:** `tailwind.config.js`

```javascript
fontFamily: {
  sans: ['YourFont', 'sans-serif'],
}
```

Update in globals.css too:

```css
body {
  font-family: 'YourFont', sans-serif;
}
```

### Change Button Styles

**File:** `src/styles/globals.css`

```css
.btn-primary {
  @apply px-6 py-3 bg-blue-600 text-white font-semibold rounded-lg 
         hover:bg-blue-700 transition-all duration-300 
         transform hover:scale-105;
}
```

### Add New Animations

**File:** `tailwind.config.js`

```javascript
animation: {
  'fade-in': 'fadeIn 0.6s ease-in',
  'slide-up': 'slideUp 0.6s ease-out',
  'pulse-glow': 'pulseGlow 2s ease-in-out infinite',
}
```

---

## 🔗 Managing Links

### Social Links
- LinkedIn: `https://linkedin.com/in/yourusername`
- GitHub: `https://github.com/yourusername`
- Email: `youremail@example.com`
- Portfolio: Your domain
- Blog: Your domain/blog

### External Links Format
```javascript
// Always use https://
link: "https://github.com/username/project"

// For email
link: "mailto:your@email.com"
```

---

## ✍️ Writing Better Content

### Bio Tips
- Keep it professional but personable
- Lead with your expertise
- Include your unique angle
- Mention years of experience
- End with a call-to-action

### Project Descriptions
- **Start with:** What problem did you solve?
- **Explain:** Your approach and methodology
- **Highlight:** Key results and impact
- **Technical:** Tools and technologies used

### Tutorial Writing
- **Title:** Clear and descriptive
- **Intro:** What will readers learn?
- **Steps:** Clear, numbered sections
- **Code:** Well-commented examples
- **Conclusion:** Summary and next steps
- **Resources:** Links to learn more

### Blog Post Ideas
- "5 Mistakes I Made with Data..."
- "How to [Solve Problem]"
- "Lesson Learned from [Project]"
- "Tools That Changed My Workflow"
- "Case Study: [Project Name]"

---

## 🔐 Security & Best Practices

### Protect Personal Info
- Don't publish:
  - Passwords
  - API keys
  - Private tokens
  - Personal phone numbers
  - Home address

### Contact Form Best Practices
- Add CAPTCHA (optional): protect from spam
- Use form backend: Formspree, Netlify Forms, etc.
- Validate email addresses
- Add rate limiting

### Image Best Practices
- Compress all images
- Use descriptive alt text
- Avoid personal information in photos
- Ensure images are your own or licensed

---

## 📋 Deployment Checklist

Before publishing updates:

- [ ] Tested locally (`npm run dev`)
- [ ] All links work
- [ ] Images display correctly
- [ ] Mobile responsive
- [ ] No spelling errors
- [ ] Contact info correct
- [ ] Meta tags updated (if changed)
- [ ] Build successful (`npm run build`)

---

## 🚀 How to Push Updates

```bash
# 1. Make changes to files
# 2. Test locally
npm run dev

# 3. Build for production
npm run build

# 4. Commit changes
git add .
git commit -m "Update: Added new project and blog post"

# 5. Push to GitHub
git push origin main

# 6. If on Vercel/Netlify, auto-deploys in ~1 minute
# If on GitHub Pages, manually trigger deployment
```

---

## 📅 Content Calendar

### Recommended Update Schedule

**Weekly:**
- Check contact form
- Review analytics

**Monthly:**
- Write 1 tutorial or blog
- Update 1-2 projects
- Engage on social media

**Quarterly:**
- Refresh bio/headline
- Review and update services
- Update skills list
- Add case study or project

**Yearly:**
- Redesign if needed
- Update tech stack
- Refresh brand colors
- Plan content strategy

---

## 📞 Getting Help

### Common Issues

**Images not showing?**
- File in correct folder? `public/images/`
- Path correct? `/images/filename.png`
- File exists? Check filename spelling

**Changes not appearing?**
- Hard refresh: `Ctrl+Shift+R` (Windows) or `Cmd+Shift+R` (Mac)
- Clear browser cache
- Restart dev server

**Build errors?**
```bash
# Delete node_modules and reinstall
rm -rf node_modules package-lock.json
npm install
```

### Resources
- Next.js Docs: [nextjs.org/docs](https://nextjs.org/docs)
- Tailwind CSS: [tailwindcss.com/docs](https://tailwindcss.com/docs)
- Markdown Guide: [markdownguide.org](https://www.markdownguide.org)

---

**Keep your portfolio fresh and updated! 🌟**

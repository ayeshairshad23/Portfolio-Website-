# DEPLOYMENT_GUIDE.md

## Deployment Options

Choose one of the following deployment platforms based on your preference:

### 🚀 Option 1: Vercel (Recommended)

**Easiest option with automatic deployments**

1. **Connect Repository**
   - Push your code to GitHub
   - Go to [vercel.com](https://vercel.com)
   - Click "New Project"
   - Select your repository
   - Click "Import"

2. **Configure**
   - Framework: Next.js (auto-detected)
   - Root Directory: ./portfolio-website
   - Environment Variables: (none needed for static site)

3. **Deploy**
   - Click "Deploy"
   - Your site goes live at `your-project.vercel.app`

4. **Automatic Deployments**
   - Every push to main branch auto-deploys
   - Preview deployments for pull requests

### 🌐 Option 2: Netlify

**Great for GitHub integration and built-in forms**

1. **Connect Repository**
   - Go to [netlify.com](https://netlify.com)
   - Click "New site from Git"
   - Connect your GitHub account
   - Select your repository

2. **Configure**
   - Build command: `npm run build`
   - Publish directory: `.next`
   - Environment: (none needed)

3. **Deploy**
   - Click "Deploy site"
   - Your site goes live at `your-site.netlify.app`

4. **Benefits**
   - Form submissions with Netlify Forms
   - Free SSL certificate
   - CDN deployment
   - Analytics and performance insights

### 📄 Option 3: GitHub Pages

**Free hosting directly from GitHub**

1. **Update Configuration**
   
   Edit `next.config.js`:
   ```javascript
   const nextConfig = {
     output: 'export',
     basePath: '/portfolio-website',
     assetPrefix: '/portfolio-website/',
   };
   ```

2. **Build Static Site**
   ```bash
   npm run build && npm run export
   ```

3. **Commit and Push**
   ```bash
   git add .
   git commit -m "Deploy to GitHub Pages"
   git push origin main
   ```

4. **Enable GitHub Pages**
   - Go to repository Settings
   - Scroll to "GitHub Pages"
   - Source: `gh-pages` branch
   - Save

5. **Site Goes Live**
   - At: `https://yourusername.github.io/portfolio-website`

### 🏠 Option 4: Self-Hosted Server

**For complete control**

1. **Build**
   ```bash
   npm run build
   ```

2. **Upload to Server**
   - Upload `.next` directory
   - Upload `public` directory
   - Upload `node_modules` or install on server
   - Upload `package.json` and `package-lock.json`

3. **Install and Run**
   ```bash
   npm install
   npm start
   ```

4. **Use Reverse Proxy** (Nginx/Apache)
   ```nginx
   server {
     listen 80;
     server_name yourdomain.com;
     
     location / {
       proxy_pass http://localhost:3000;
     }
   }
   ```

## Post-Deployment Checklist

- [ ] Test all links and navigation
- [ ] Verify mobile responsiveness
- [ ] Test contact form (if enabled)
- [ ] Check page load performance
- [ ] Verify social media links
- [ ] Test on different browsers
- [ ] Set up custom domain (optional)
- [ ] Enable SSL certificate
- [ ] Set up analytics (Google Analytics)
- [ ] Submit sitemap to Google Search Console

## Custom Domain

### For Vercel
1. Go to project settings
2. Add domain under "Domains"
3. Update DNS records
4. Wait for verification (usually 5-10 minutes)

### For Netlify
1. Go to Domain settings
2. Add custom domain
3. Update nameservers with registrar
4. Wait for propagation

### For GitHub Pages
1. Go to repository Settings
2. Under "Pages", add custom domain
3. Create CNAME file in repo
4. Update DNS A record

## Environment Variables (Optional)

Create `.env.local` for sensitive data:

```
NEXT_PUBLIC_SITE_URL=https://yourdomain.com
NEXT_PUBLIC_GA_ID=your-google-analytics-id
```

## Performance Optimization

1. **Image Optimization**
   - Compress images before uploading
   - Use WebP format when possible
   - Optimize for mobile

2. **Code Splitting**
   - Next.js handles automatically
   - Monitor bundle size

3. **Caching**
   - Vercel/Netlify cache automatically
   - Set cache headers on images

4. **Analytics**
   - Add Google Analytics
   - Monitor page performance
   - Track user behavior

## Troubleshooting

### Build Fails
```bash
# Clear cache and reinstall
rm -rf node_modules package-lock.json
npm install
npm run build
```

### 404 Errors on Subpages
- Check basePath in `next.config.js`
- Ensure output is set to 'export' for static export

### Images Not Loading
- Verify images are in `public/images/` folder
- Check image paths in `portfolio.js`
- Use relative paths starting with `/`

### Slow Performance
- Check image sizes
- Enable compression
- Review bundle size
- Use CDN (Vercel/Netlify do this automatically)

## Next Steps

1. Set up custom domain
2. Enable SSL certificate
3. Add Google Analytics
4. Set up monitoring/alerts
5. Create regular backup schedule
6. Plan content updates

---

**Your portfolio is now live! 🎉**

For ongoing updates and maintenance, regularly:
- Update projects and achievements
- Add new blog posts
- Refresh your bio and services
- Keep dependencies updated

/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  images: {
    unoptimized: true,
  },
  // For GitHub Pages deployment
  // basePath: '/portfolio-website',
  // assetPrefix: '/portfolio-website/',
};

module.exports = nextConfig;

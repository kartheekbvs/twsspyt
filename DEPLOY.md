# Cloudflare Pages Deployment Guide

Your Python Learning Hub is ready to be deployed to Cloudflare Pages.

## ⚙️ Deployment Settings

When setting up your project in the Cloudflare Pages dashboard:

1.  **Framework preset**: `None`
2.  **Build command**: `echo "Static Site - No Build Required"`
3.  **Build output directory**: `/` (The root directory)
4.  **Root directory**: `/`

## 🚀 Automated Build (Optional)

If you ever want to regenerate the site automatically on push, you can use the following settings:

- **Build command**: `pip install PyMuPDF && python generate_pages.ps1` (Note: Cloudflare Pages supports Python, but you'd need to ensure all scripts are compatible with the environment).

For now, since all 64 pages (including the new Resources) are pre-generated and pushed to GitHub, simply setting the **Build output directory** to `/` will work perfectly.

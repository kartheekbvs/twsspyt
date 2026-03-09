# Cloudflare Pages Deployment Guide

Your Python Learning Hub is ready to be deployed to Cloudflare Pages.

## ⚙️ Deployment Settings

When setting up your project in the Cloudflare Pages dashboard:

1.  **Framework preset**: `None`
2.  **Build command**: `python build.py`
3.  **Build output directory**: `/` (The root directory)
4.  **Root directory**: `/`

## 🚀 Automated Build (Recommended)

To ensure the site regenerates correctly on Linux (Cloudflare):

- **Build command**: `pip install -r requirements.txt && python build.py`
- **Build output directory**: `/`

This configuration replaces the previous PowerShell instructions and is fully compatible with Cloudflare's Linux environment.

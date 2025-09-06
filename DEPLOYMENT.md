# 🚀 Streamlit Cloud Deployment Guide

## 📋 Prerequisites

1. **GitHub Repository**: Code is already pushed to [Market-Research-Use-Case-Generation-Agent](https://github.com/KurraSaiKiran/Market-Research-Use-Case-Generation-Agent)
2. **Streamlit Cloud Account**: Sign up at [share.streamlit.io](https://share.streamlit.io)

## 🔧 Deployment Steps

### 1. Connect to Streamlit Cloud

1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Sign in with your GitHub account
3. Click "New app"
4. Select your repository: `KurraSaiKiran/Market-Research-Use-Case-Generation-Agent`
5. Set main file path: `streamlit_app.py`
6. Click "Deploy!"

### 2. Configure API Keys (Optional)

In Streamlit Cloud dashboard:

1. Go to your app settings
2. Click on "Secrets"
3. Add the following secrets:

```toml
# Web Search APIs
SERPER_API_KEY = "your_serper_api_key"
TAVILY_API_KEY = "your_tavily_api_key"

# Dataset Sources  
KAGGLE_USERNAME = "your_kaggle_username"
KAGGLE_KEY = "your_kaggle_api_key"
HUGGINGFACE_API_KEY = "your_huggingface_api_key"
GITHUB_TOKEN = "your_github_token"

# Optional: OpenAI
OPENAI_API_KEY = "your_openai_api_key"
```

### 3. App Configuration

The app is configured with:
- **Main file**: `streamlit_app.py`
- **Python version**: 3.8+
- **Dependencies**: Automatically installed from `requirements.txt`

## 🔑 API Keys Setup

### Required APIs (All have free tiers):

1. **Serper API** (Web Search)
   - Sign up: [serper.dev](https://serper.dev)
   - Free: 1000 queries/month
   - Add to secrets as `SERPER_API_KEY`

2. **GitHub Token** (Repositories)
   - Generate: [GitHub Settings > Tokens](https://github.com/settings/tokens)
   - Free: 5000 requests/hour
   - Add to secrets as `GITHUB_TOKEN`

3. **Kaggle API** (Datasets)
   - Get credentials: [Kaggle Account Settings](https://www.kaggle.com/settings/account)
   - Free: Unlimited
   - Add username as `KAGGLE_USERNAME` and key as `KAGGLE_KEY`

4. **HuggingFace Token** (Models)
   - Generate: [HuggingFace Settings](https://huggingface.co/settings/tokens)
   - Free: 1000 requests/month
   - Add to secrets as `HUGGINGFACE_API_KEY`

## 🎯 Fallback Mode

The system works without API keys using curated fallback data. Users will see:
- Demo industry analysis
- Template use cases
- Sample datasets and resources

## 🔄 Updates

To update the deployed app:
1. Push changes to your GitHub repository
2. Streamlit Cloud will automatically redeploy

## 📱 Access Your App

Once deployed, your app will be available at:
`https://[app-name]-[random-string].streamlit.app`

## 🛠️ Troubleshooting

### Common Issues:

1. **Import Errors**: Check `requirements.txt` includes all dependencies
2. **API Limits**: Monitor usage in respective API dashboards
3. **Secrets Not Loading**: Ensure secrets are properly formatted in TOML

### Support:
- Streamlit Community: [discuss.streamlit.io](https://discuss.streamlit.io)
- GitHub Issues: Create issues in your repository
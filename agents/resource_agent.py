import requests
import os
from typing import Dict, List

class ResourceAgent:
    def __init__(self):
        self.kaggle_key = os.getenv('KAGGLE_KEY')
        self.github_token = os.getenv('GITHUB_TOKEN')
        self.hf_token = os.getenv('HUGGINGFACE_API_KEY')
        
    def find_resources(self, use_cases: List[Dict]) -> Dict:
        """Find datasets and resources for use cases"""
        resources = {}
        
        for use_case in use_cases:
            case_name = use_case['name']
            resources[case_name] = self._search_resources(case_name, use_case['description'])
            
        return resources
    
    def _search_resources(self, use_case: str, description: str) -> List[Dict]:
        """Search for relevant datasets and resources based on actual use case"""
        print(f"[DEBUG] Searching resources for: {use_case}")
        resources = []
        
        # Extract keywords from use case and description
        keywords = self._extract_keywords(use_case, description)
        search_query = " ".join(keywords[:3])  # Use top 3 keywords
        
        # Try Kaggle search with specific keywords
        kaggle_results = self._search_kaggle(search_query)
        resources.extend(kaggle_results)
        
        # Try GitHub search with specific keywords
        github_results = self._search_github(search_query)
        resources.extend(github_results)
        
        # Add HuggingFace models with specific keywords
        hf_results = self._search_huggingface(search_query)
        resources.extend(hf_results)
        
        print(f"[DEBUG] Found {len(resources)} resources for {use_case}")
        return resources[:4]  # Limit to 4 resources per use case
    
    def _search_kaggle(self, query: str) -> List[Dict]:
        """Search Kaggle datasets using API"""
        try:
            if not self.kaggle_key:
                return self._fallback_kaggle(query)
            
            # Use Kaggle API search
            url = "https://www.kaggle.com/api/v1/datasets/list"
            headers = {
                "Authorization": f"Bearer {self.kaggle_key}"
            }
            params = {
                "search": query.replace(' ', '+'),
                "sortBy": "hottest",
                "size": 3
            }
            
            response = requests.get(url, headers=headers, params=params, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                resources = []
                
                for dataset in data[:2]:
                    resources.append({
                        "name": dataset.get('title', 'Kaggle Dataset'),
                        "type": "Kaggle Dataset",
                        "url": f"https://www.kaggle.com/datasets/{dataset.get('ref', '')}",
                        "description": dataset.get('subtitle', 'Dataset from Kaggle')[:100]
                    })
                
                return resources if resources else self._fallback_kaggle(query)
            else:
                return self._fallback_kaggle(query)
                
        except Exception as e:
            print(f"Kaggle API error: {e}")
            return self._fallback_kaggle(query)
    
    def _search_github(self, query: str) -> List[Dict]:
        """Search GitHub repositories"""
        try:
            url = "https://api.github.com/search/repositories"
            params = {
                "q": f"{query.replace(' ', '+')}+machine+learning", 
                "sort": "stars", 
                "per_page": 2
            }
            
            headers = {}
            if self.github_token and self.github_token.strip():
                headers["Authorization"] = f"Bearer {self.github_token}"
            
            response = requests.get(url, params=params, headers=headers, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                resources = []
                
                for repo in data.get('items', [])[:2]:
                    resources.append({
                        "name": repo['name'],
                        "type": "GitHub Repository", 
                        "url": repo['html_url'],
                        "description": repo.get('description', 'Machine learning repository')[:100]
                    })
                return resources
            else:
                print(f"GitHub API error: {response.status_code}")
                return self._fallback_github(query)
                
        except Exception as e:
            print(f"GitHub search error: {e}")
            return self._fallback_github(query)
    
    def _search_huggingface(self, query: str) -> List[Dict]:
        """Search HuggingFace models using API"""
        try:
            url = "https://huggingface.co/api/models"
            params = {
                "search": query.replace(' ', '+'),
                "sort": "downloads",
                "direction": -1,
                "limit": 3
            }
            
            headers = {}
            if hasattr(self, 'hf_token') and self.hf_token:
                headers["Authorization"] = f"Bearer {self.hf_token}"
            
            response = requests.get(url, params=params, headers=headers, timeout=10)
            
            if response.status_code == 200:
                models = response.json()
                resources = []
                
                for model in models[:2]:
                    model_id = model.get('modelId', '')
                    resources.append({
                        "name": model_id,
                        "type": "HuggingFace Model",
                        "url": f"https://huggingface.co/{model_id}",
                        "description": f"Downloads: {model.get('downloads', 0)}, Task: {', '.join(model.get('pipeline_tag', ['general']) if isinstance(model.get('pipeline_tag'), list) else [model.get('pipeline_tag', 'general')])}"
                    })
                
                return resources if resources else self._fallback_huggingface(query)
            else:
                return self._fallback_huggingface(query)
                
        except Exception as e:
            print(f"HuggingFace API error: {e}")
            return self._fallback_huggingface(query)
    
    def _fallback_huggingface(self, query: str) -> List[Dict]:
        """Fallback HuggingFace models"""
        model_map = {
            "predictive": {
                "model": "facebook/prophet",
                "desc": "Time series forecasting model"
            },
            "recommendation": {
                "model": "sentence-transformers/all-MiniLM-L6-v2",
                "desc": "Sentence embeddings for recommendations"
            },
            "image": {
                "model": "google/vit-base-patch16-224",
                "desc": "Vision transformer for image classification"
            },
            "text": {
                "model": "distilbert-base-uncased",
                "desc": "Lightweight BERT for text processing"
            },
            "chatbot": {
                "model": "microsoft/DialoGPT-medium",
                "desc": "Conversational AI model"
            },
            "generation": {
                "model": "gpt2",
                "desc": "Text generation model"
            }
        }
        
        # Find best match
        for key, data in model_map.items():
            if key in query.lower():
                return [{
                    "name": data["model"],
                    "type": "HuggingFace Model",
                    "url": f"https://huggingface.co/{data['model']}",
                    "description": data["desc"]
                }]
        
        # Default model
        return [{
            "name": "bert-base-uncased", 
            "type": "HuggingFace Model",
            "url": "https://huggingface.co/bert-base-uncased",
            "description": "General purpose language model for various NLP tasks"
        }]
    
    def _extract_keywords(self, use_case: str, description: str) -> List[str]:
        """Extract relevant keywords from use case and description"""
        text = (use_case + " " + description).lower()
        
        # Common AI/ML keywords
        keywords = []
        if "predictive" in text or "forecasting" in text:
            keywords.append("forecasting")
        if "recommendation" in text or "personalization" in text:
            keywords.append("recommendation")
        if "image" in text or "vision" in text:
            keywords.append("image")
        if "text" in text or "nlp" in text:
            keywords.append("text")
        if "fraud" in text or "detection" in text:
            keywords.append("fraud")
        if "healthcare" in text or "medical" in text:
            keywords.append("medical")
        if "financial" in text or "finance" in text:
            keywords.append("financial")
        if "automation" in text:
            keywords.append("automation")
        if "optimization" in text:
            keywords.append("optimization")
        if "analytics" in text or "data" in text:
            keywords.append("analytics")
        
        return keywords if keywords else ["machine learning"]
    
    def _fallback_kaggle(self, query: str) -> List[Dict]:
        return []
    
    def _fallback_github(self, query: str) -> List[Dict]:
        return []
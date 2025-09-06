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
        """Search for relevant datasets and resources"""
        resources = []
        
        # Try Kaggle search
        kaggle_results = self._search_kaggle(use_case)
        resources.extend(kaggle_results)
        
        # Try GitHub search  
        github_results = self._search_github(use_case)
        resources.extend(github_results)
        
        # Add HuggingFace models
        hf_results = self._search_huggingface(use_case)
        resources.extend(hf_results)
        
        return resources[:5]  # Limit to 5 resources per use case
    
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
    
    def _fallback_kaggle(self, query: str) -> List[Dict]:
        dataset_map = {
            "predictive": {
                "name": "Sales Forecasting Dataset",
                "url": "https://www.kaggle.com/datasets/shelvigarg/sales-forecasting-dataset",
                "desc": "Time series data for demand prediction"
            },
            "recommendation": {
                "name": "MovieLens 20M Dataset", 
                "url": "https://www.kaggle.com/datasets/grouplens/movielens-20m-dataset",
                "desc": "Movie ratings for recommendation systems"
            },
            "retail": {
                "name": "E-commerce Dataset",
                "url": "https://www.kaggle.com/datasets/carrie1/ecommerce-data",
                "desc": "Online retail transaction data"
            },
            "automotive": {
                "name": "Vehicle Dataset",
                "url": "https://www.kaggle.com/datasets/nehalbirla/vehicle-dataset-from-cardekho",
                "desc": "Car specifications and pricing data"
            },
            "fraud": {
                "name": "Credit Card Fraud Detection",
                "url": "https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud",
                "desc": "Anonymized credit card transactions"
            },
            "image": {
                "name": "ImageNet Dataset",
                "url": "https://www.kaggle.com/competitions/imagenet-object-localization-challenge",
                "desc": "Large-scale image classification dataset"
            },
            "text": {
                "name": "IMDB Movie Reviews",
                "url": "https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews",
                "desc": "Sentiment analysis dataset"
            }
        }
        
        # Find best match
        for key, data in dataset_map.items():
            if key in query.lower():
                return [{
                    "name": data["name"],
                    "type": "Kaggle Dataset",
                    "url": data["url"],
                    "description": data["desc"]
                }]
        
        # Default fallback
        return [{
            "name": f"{query.title()} Related Dataset",
            "type": "Kaggle Dataset", 
            "url": f"https://www.kaggle.com/search?q={query.replace(' ', '+')}",
            "description": f"Search results for {query} datasets on Kaggle"
        }]
    
    def _fallback_github(self, query: str) -> List[Dict]:
        return [{
            "name": f"{query.replace(' ', '-')}-ml",
            "type": "GitHub Repository",
            "url": f"https://github.com/search?q={query.replace(' ', '+')}+machine+learning",
            "description": f"ML implementation for {query}"
        }]
import requests
import os
from typing import Dict, List

class ResearchAgent:
    def __init__(self):
        self.serper_key = os.getenv('SERPER_API_KEY')
        
    def research_company_industry(self, query: str) -> Dict:
        """Research company or industry using web search"""
        try:
            if self.serper_key and self.serper_key.strip():
                return self._search_serper(query)
            else:
                return self._fallback_research(query)
        except Exception as e:
            print(f"Research API error: {e}")
            return self._fallback_research(query)
    
    def _search_serper(self, query: str) -> Dict:
        url = "https://google.serper.dev/search"
        payload = {"q": f"{query} industry analysis market size competitors"}
        headers = {
            "X-API-KEY": self.serper_key,
            "Content-Type": "application/json"
        }
        
        try:
            response = requests.post(url, json=payload, headers=headers, timeout=10)
            response.raise_for_status()
            data = response.json()
            
            return {
                "industry": self._extract_industry(query),
                "company_offerings": self._extract_company_offerings(query, data),
                "focus_areas": self._extract_focus_areas(data),
                "competitors": self._extract_competitors(data),
                "market_trends": self._extract_market_trends(data),
                "market_size": self._extract_market_size(data)
            }
        except Exception as e:
            print(f"Serper API error: {e}")
            return self._fallback_research(query)
    
    def _fallback_research(self, query: str) -> Dict:
        """Fallback when APIs unavailable"""
        industry_map = {
            "tesla": "Automotive/Electric Vehicles",
            "retail": "Retail & E-commerce", 
            "healthcare": "Healthcare & Medical",
            "finance": "Financial Services",
            "manufacturing": "Manufacturing & Industrial",
            "education": "Education Technology",
            "agriculture": "Agriculture & Food Tech",
            "energy": "Energy & Utilities",
            "logistics": "Logistics & Transportation",
            "media": "Media & Entertainment"
        }
        
        # Better industry detection
        detected_industry = "Technology"
        for key, value in industry_map.items():
            if key in query.lower():
                detected_industry = value
                break
        
        if "industry" not in query.lower():
            detected_industry = f"{query.title()} Industry"
        
        return {
            "industry": detected_industry,
            "company_offerings": self._get_fallback_offerings(query),
            "focus_areas": ["Digital transformation", "AI adoption", "Process automation", "Customer experience enhancement"],
            "competitors": [f"Leading companies in {detected_industry}", "Industry innovators", "Market disruptors"],
            "market_trends": ["AI integration", "Sustainability focus", "Digital-first approach"],
            "market_size": "Multi-billion dollar market with significant growth potential"
        }
    
    def _extract_industry(self, query: str) -> str:
        if "industry" in query.lower():
            return query.title()
        else:
            # Try to detect company and map to industry
            company_industry_map = {
                "tesla": "Automotive/Electric Vehicles",
                "apple": "Technology/Consumer Electronics",
                "amazon": "E-commerce/Cloud Computing",
                "google": "Technology/Internet Services",
                "microsoft": "Technology/Software",
                "netflix": "Media/Streaming Services"
            }
            
            for company, industry in company_industry_map.items():
                if company in query.lower():
                    return industry
            
            return f"{query.title()} Industry"
    
    def _extract_focus_areas(self, data: Dict) -> List[str]:
        focus_areas = []
        
        if 'organic' in data:
            for result in data['organic'][:5]:
                snippet = result.get('snippet', '').lower()
                title = result.get('title', '').lower()
                
                # Extract focus areas from content
                if any(word in snippet + title for word in ['automation', 'automate']):
                    focus_areas.append("Process automation")
                if any(word in snippet + title for word in ['customer', 'client', 'user']):
                    focus_areas.append("Customer experience")
                if any(word in snippet + title for word in ['digital', 'technology', 'tech']):
                    focus_areas.append("Digital transformation")
                if any(word in snippet + title for word in ['ai', 'artificial intelligence', 'machine learning']):
                    focus_areas.append("AI adoption")
                if any(word in snippet + title for word in ['efficiency', 'optimize', 'streamline']):
                    focus_areas.append("Operational efficiency")
                if any(word in snippet + title for word in ['innovation', 'innovative', 'disrupt']):
                    focus_areas.append("Innovation initiatives")
                if any(word in snippet + title for word in ['supply chain', 'logistics']):
                    focus_areas.append("Supply chain optimization")
                if any(word in snippet + title for word in ['data', 'analytics', 'insights']):
                    focus_areas.append("Data-driven decision making")
        
        # Remove duplicates and return top 5
        return list(set(focus_areas))[:5] if focus_areas else ["Digital transformation", "AI adoption", "Operational efficiency"]
    
    def _extract_competitors(self, data: Dict) -> List[str]:
        competitors = []
        
        if 'organic' in data:
            for result in data['organic'][:5]:
                title = result.get('title', '').lower()
                snippet = result.get('snippet', '').lower()
                
                # Look for competitor mentions
                if any(word in title + snippet for word in ['vs', 'versus', 'competitor', 'rival', 'alternative']):
                    # Extract company names from title
                    clean_title = result.get('title', '')[:80]
                    competitors.append(clean_title)
                
                # Look for market leader mentions
                if any(word in title + snippet for word in ['leader', 'top', 'best', 'leading']):
                    clean_title = result.get('title', '')[:80]
                    competitors.append(f"Market leader: {clean_title}")
        
        # Remove duplicates and limit
        competitors = list(set(competitors))[:4]
        
        if not competitors:
            competitors = ["Industry leaders and competitors", "Market innovators"]
        
        return competitors
    
    def _extract_market_size(self, data: Dict) -> str:
        # Try to extract market size from search results
        if 'organic' in data:
            for result in data['organic'][:3]:
                snippet = result.get('snippet', '').lower()
                if 'billion' in snippet or 'market size' in snippet:
                    return f"Market insights available - {snippet[:100]}..."
        
        return "Multi-billion dollar market with growth opportunities"
    
    def _extract_company_offerings(self, query: str, data: Dict) -> List[str]:
        """Extract company products and services from search results"""
        offerings = []
        
        if 'organic' in data:
            for result in data['organic'][:5]:
                snippet = result.get('snippet', '').lower()
                title = result.get('title', '').lower()
                
                # Extract offerings from content
                if any(word in snippet + title for word in ['products', 'services', 'solutions', 'platform']):
                    # Extract specific offerings
                    text = snippet + ' ' + title
                    if 'software' in text:
                        offerings.append("Software solutions")
                    if 'cloud' in text:
                        offerings.append("Cloud services")
                    if 'platform' in text:
                        offerings.append("Technology platform")
                    if 'mobile' in text or 'app' in text:
                        offerings.append("Mobile applications")
                    if 'data' in text or 'analytics' in text:
                        offerings.append("Data analytics services")
                    if 'consulting' in text:
                        offerings.append("Consulting services")
                    if 'hardware' in text:
                        offerings.append("Hardware products")
                    if 'ai' in text or 'artificial intelligence' in text:
                        offerings.append("AI-powered solutions")
        
        # Remove duplicates
        offerings = list(set(offerings))[:5]
        
        if not offerings:
            offerings = ["Core business solutions", "Industry-specific services", "Technology platforms"]
        
        return offerings
    
    def _get_fallback_offerings(self, query: str) -> List[str]:
        """Fallback company offerings"""
        if "retail" in query.lower():
            return ["Consumer products", "Online marketplace", "Customer services"]
        elif "healthcare" in query.lower():
            return ["Medical services", "Healthcare technology", "Patient care solutions"]
        elif "finance" in query.lower():
            return ["Financial services", "Banking solutions", "Investment products"]
        else:
            return ["Core business solutions", "Industry-specific services", "Technology platforms"]
    
    def _extract_market_trends(self, data: Dict) -> List[str]:
        """Extract market trends from search results"""
        trends = []
        
        if 'organic' in data:
            for result in data['organic'][:5]:
                snippet = result.get('snippet', '').lower()
                title = result.get('title', '').lower()
                text = snippet + ' ' + title
                
                # Extract trends from content
                if any(word in text for word in ['trend', 'trending', 'growth']):
                    if 'ai' in text or 'artificial intelligence' in text:
                        trends.append("AI integration trend")
                    if 'digital' in text:
                        trends.append("Digital transformation")
                    if 'cloud' in text:
                        trends.append("Cloud adoption")
                    if 'automation' in text:
                        trends.append("Automation trend")
                    if 'sustainability' in text or 'green' in text:
                        trends.append("Sustainability focus")
                    if 'remote' in text or 'hybrid' in text:
                        trends.append("Remote work adoption")
                    if 'data' in text:
                        trends.append("Data-driven insights")
                    if 'innovation' in text:
                        trends.append("Innovation-driven growth")
        
        # Remove duplicates
        trends = list(set(trends))[:5]
        
        if not trends:
            trends = ["AI integration", "Digital transformation", "Sustainability focus"]
        
        return trends
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
        payload = {"q": f"{query} industry trends market analysis AI use cases 2024"}
        headers = {
            "X-API-KEY": self.serper_key,
            "Content-Type": "application/json"
        }
        
        try:
            print(f"[DEBUG] Calling Serper API for: {query}")
            response = requests.post(url, json=payload, headers=headers, timeout=15)
            response.raise_for_status()
            data = response.json()
            print(f"[DEBUG] Serper API response received: {len(data.get('organic', []))} results")
            
            return {
                "industry": self._extract_industry(query),
                "company_offerings": self._extract_company_offerings(query, data),
                "focus_areas": self._extract_focus_areas(data),
                "competitors": self._extract_competitors(data),
                "market_trends": self._extract_market_trends(data),
                "market_size": self._extract_market_size(data)
            }
        except Exception as e:
            print(f"[ERROR] Serper API failed: {e}")
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
        focus_areas = set()
        
        if 'organic' in data and data['organic']:
            print(f"[DEBUG] Extracting focus areas from {len(data['organic'])} results")
            
            for result in data['organic'][:8]:
                snippet = result.get('snippet', '').lower()
                title = result.get('title', '').lower()
                text = snippet + ' ' + title
                
                # Industry-specific focus areas
                if any(word in text for word in ['automation', 'automate', 'robotic']):
                    focus_areas.add("Process automation")
                if any(word in text for word in ['customer', 'client', 'user experience', 'cx']):
                    focus_areas.add("Customer experience enhancement")
                if any(word in text for word in ['digital transformation', 'digitalization', 'digital']):
                    focus_areas.add("Digital transformation")
                if any(word in text for word in ['ai', 'artificial intelligence', 'machine learning', 'ml']):
                    focus_areas.add("AI adoption")
                if any(word in text for word in ['efficiency', 'optimize', 'streamline', 'productivity']):
                    focus_areas.add("Operational efficiency")
                if any(word in text for word in ['innovation', 'innovative', 'disrupt', 'emerging']):
                    focus_areas.add("Innovation initiatives")
                if any(word in text for word in ['supply chain', 'logistics', 'procurement']):
                    focus_areas.add("Supply chain optimization")
                if any(word in text for word in ['data analytics', 'big data', 'insights', 'business intelligence']):
                    focus_areas.add("Data-driven decision making")
                if any(word in text for word in ['sustainability', 'green', 'environmental', 'esg']):
                    focus_areas.add("Sustainability initiatives")
                if any(word in text for word in ['cybersecurity', 'security', 'privacy', 'compliance']):
                    focus_areas.add("Security and compliance")
        
        result_areas = list(focus_areas)[:6]
        print(f"[DEBUG] Extracted focus areas: {result_areas}")
        return result_areas if result_areas else ["Digital transformation", "AI adoption", "Operational efficiency"]
    
    def _extract_competitors(self, data: Dict) -> List[str]:
        competitors = set()
        
        if 'organic' in data and data['organic']:
            for result in data['organic'][:6]:
                title = result.get('title', '')
                snippet = result.get('snippet', '')
                text = (title + ' ' + snippet).lower()
                
                # Extract competitor information
                if any(word in text for word in ['vs', 'versus', 'competitor', 'rival', 'alternative', 'comparison']):
                    competitors.add(title[:70] + '...' if len(title) > 70 else title)
                
                if any(word in text for word in ['top companies', 'leading', 'market leader', 'industry leader']):
                    competitors.add(f"Leading companies: {title[:50]}...")
                
                if any(word in text for word in ['fortune 500', 'biggest', 'largest', 'major players']):
                    competitors.add(f"Major players: {title[:50]}...")
        
        result_competitors = list(competitors)[:4]
        print(f"[DEBUG] Extracted competitors: {len(result_competitors)} found")
        
        if not result_competitors:
            result_competitors = ["Industry leaders and competitors", "Market innovators"]
        
        return result_competitors
    
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
        trends = set()
        
        if 'organic' in data and data['organic']:
            for result in data['organic'][:8]:
                snippet = result.get('snippet', '').lower()
                title = result.get('title', '').lower()
                text = snippet + ' ' + title
                
                # Extract specific trends
                if any(word in text for word in ['trend', 'trending', 'growth', '2024', '2025', 'future']):
                    if any(word in text for word in ['ai', 'artificial intelligence', 'machine learning']):
                        trends.add("AI integration and adoption")
                    if any(word in text for word in ['digital transformation', 'digitalization']):
                        trends.add("Digital transformation acceleration")
                    if any(word in text for word in ['cloud', 'saas', 'paas']):
                        trends.add("Cloud-first strategies")
                    if any(word in text for word in ['automation', 'robotic process']):
                        trends.add("Intelligent automation")
                    if any(word in text for word in ['sustainability', 'green', 'esg', 'carbon']):
                        trends.add("Sustainability and ESG focus")
                    if any(word in text for word in ['remote', 'hybrid', 'flexible work']):
                        trends.add("Hybrid work models")
                    if any(word in text for word in ['data analytics', 'big data', 'data-driven']):
                        trends.add("Data-driven decision making")
                    if any(word in text for word in ['cybersecurity', 'zero trust', 'security']):
                        trends.add("Enhanced cybersecurity")
                    if any(word in text for word in ['personalization', 'customer-centric']):
                        trends.add("Hyper-personalization")
        
        result_trends = list(trends)[:5]
        print(f"[DEBUG] Extracted market trends: {result_trends}")
        
        if not result_trends:
            result_trends = ["AI integration", "Digital transformation", "Sustainability focus"]
        
        return result_trends
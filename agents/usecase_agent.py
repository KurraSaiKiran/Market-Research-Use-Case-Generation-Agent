from typing import Dict, List
import requests
import os

class UseCaseAgent:
    def __init__(self):
        self.serper_key = os.getenv('SERPER_API_KEY')
    
    def generate_use_cases(self, research_data: Dict) -> List[Dict]:
        """Generate AI/GenAI use cases based on real research data"""
        industry = research_data.get("industry", "")
        focus_areas = research_data.get("focus_areas", [])
        trends = research_data.get("market_trends", [])
        
        print(f"[DEBUG] Generating use cases for: {industry}")
        print(f"[DEBUG] Focus areas: {focus_areas}")
        
        use_cases = []
        
        # Generate use cases from focus areas
        for area in focus_areas[:4]:
            use_case = self._generate_use_case_from_focus_area(area, industry)
            if use_case and use_case not in use_cases:
                use_cases.append(use_case)
        
        # Generate use cases from market trends
        for trend in trends[:2]:
            use_case = self._generate_use_case_from_trend(trend, industry)
            if use_case and use_case not in use_cases:
                use_cases.append(use_case)
        
        # Search for industry-specific AI use cases online
        online_cases = self._search_industry_use_cases(industry)
        for case in online_cases:
            if case not in use_cases and len(use_cases) < 6:
                use_cases.append(case)
        
        # Add GenAI cases
        genai_cases = self._add_genai_cases_from_research(research_data)
        for case in genai_cases:
            if case not in use_cases and len(use_cases) < 8:
                use_cases.append(case)
        
        print(f"[DEBUG] Generated {len(use_cases)} use cases")
        return use_cases[:8]
    
    def _search_industry_use_cases(self, industry: str) -> List[Dict]:
        """Search for real AI use cases for the industry"""
        if not self.serper_key:
            return []
        
        try:
            url = "https://google.serper.dev/search"
            payload = {"q": f"{industry} AI use cases applications machine learning examples"}
            headers = {"X-API-KEY": self.serper_key, "Content-Type": "application/json"}
            
            response = requests.post(url, json=payload, headers=headers, timeout=10)
            if response.status_code == 200:
                data = response.json()
                return self._extract_use_cases_from_search(data, industry)
        except Exception as e:
            print(f"[DEBUG] Use case search failed: {e}")
        
        return []
    
    def _extract_use_cases_from_search(self, data: Dict, industry: str) -> List[Dict]:
        """Extract use cases from search results"""
        use_cases = []
        
        if 'organic' in data:
            for result in data['organic'][:5]:
                snippet = result.get('snippet', '').lower()
                title = result.get('title', '')
                
                # Extract AI/ML use cases from content
                if any(word in snippet for word in ['ai', 'machine learning', 'artificial intelligence', 'automation']):
                    if 'predictive' in snippet:
                        use_cases.append({
                            "name": f"Predictive Analytics for {industry}",
                            "description": f"AI-powered predictive modeling and forecasting for {industry}",
                            "value": "Improve decision making, reduce risks, optimize operations"
                        })
                    elif 'recommendation' in snippet or 'personalization' in snippet:
                        use_cases.append({
                            "name": f"Intelligent Recommendation System",
                            "description": f"AI-driven personalization and recommendation engine for {industry}",
                            "value": "Increase engagement, improve user experience, boost revenue"
                        })
                    elif 'optimization' in snippet:
                        use_cases.append({
                            "name": f"AI-Powered Optimization",
                            "description": f"Machine learning optimization solutions for {industry} operations",
                            "value": "Reduce costs, improve efficiency, maximize resource utilization"
                        })
        
        return use_cases[:3]
    
    def _generate_use_case_from_focus_area(self, focus_area: str, industry: str) -> Dict:
        """Generate use case based on focus area"""
        focus_area_lower = focus_area.lower()
        
        if "automation" in focus_area_lower:
            return {
                "name": f"Intelligent Automation for {industry}",
                "description": f"AI-powered process automation tailored for {industry} workflows",
                "value": "Reduce manual work by 60-80%, improve accuracy and speed"
            }
        elif "customer" in focus_area_lower:
            return {
                "name": f"AI Customer Intelligence",
                "description": f"Advanced customer analytics and experience optimization for {industry}",
                "value": "Increase customer satisfaction by 40%, reduce churn"
            }
        elif "digital" in focus_area_lower:
            return {
                "name": f"Digital AI Transformation",
                "description": f"Comprehensive AI-driven digital transformation for {industry}",
                "value": "Accelerate digital adoption, improve operational efficiency"
            }
        elif "data" in focus_area_lower:
            return {
                "name": f"AI Data Intelligence Platform",
                "description": f"Advanced data analytics and insights platform for {industry}",
                "value": "Enable data-driven decisions, unlock hidden insights"
            }
        elif "security" in focus_area_lower:
            return {
                "name": f"AI Security & Risk Management",
                "description": f"Intelligent security monitoring and risk assessment for {industry}",
                "value": "Reduce security incidents by 75%, ensure compliance"
            }
        elif "sustainability" in focus_area_lower:
            return {
                "name": f"Sustainability AI Platform",
                "description": f"AI-powered sustainability tracking and optimization for {industry}",
                "value": "Reduce environmental impact, meet ESG goals"
            }
        
        return None
    
    def _generate_use_case_from_trend(self, trend: str, industry: str) -> Dict:
        """Generate use case based on market trend"""
        trend_lower = trend.lower()
        
        if "ai integration" in trend_lower:
            return {
                "name": f"AI-First {industry} Platform",
                "description": f"Comprehensive AI integration across {industry} operations",
                "value": "Transform business model, gain competitive advantage"
            }
        elif "cloud" in trend_lower:
            return {
                "name": f"Cloud-Native AI Solutions",
                "description": f"Scalable cloud-based AI infrastructure for {industry}",
                "value": "Reduce infrastructure costs, improve scalability"
            }
        elif "cybersecurity" in trend_lower:
            return {
                "name": f"AI-Powered Cybersecurity",
                "description": f"Intelligent threat detection and response for {industry}",
                "value": "Reduce security incidents by 80%, faster threat response"
            }
        
        return None
    
    def _add_genai_cases_from_research(self, research_data: Dict) -> List[Dict]:
        """Generate GenAI cases based on research data"""
        industry = research_data.get("industry", "")
        focus_areas = research_data.get("focus_areas", [])
        
        genai_cases = []
        
        # Industry-specific content generation
        genai_cases.append({
            "name": f"GenAI Content Platform for {industry}",
            "description": f"AI-powered content generation and automation for {industry}",
            "value": "Reduce content creation time by 70%, improve personalization"
        })
        
        # Add conversational AI if customer focus exists
        if any("customer" in area.lower() for area in focus_areas):
            genai_cases.append({
                "name": f"Conversational AI Assistant",
                "description": f"Intelligent virtual assistant for {industry} customer support",
                "value": "24/7 support, reduce costs by 50%, improve satisfaction"
            })
        
        return genai_cases[:2]
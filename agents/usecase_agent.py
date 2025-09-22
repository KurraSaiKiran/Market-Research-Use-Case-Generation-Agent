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
        """Generate industry-specific use case based on focus area"""
        focus_area_lower = focus_area.lower()
        industry_lower = industry.lower()
        
        # Industry-specific use cases
        if "healthcare" in industry_lower or "medical" in industry_lower:
            if "automation" in focus_area_lower:
                return {"name": "Medical Records Automation", "description": "AI-powered patient record processing and clinical workflow automation", "value": "Reduce administrative time by 70%, improve patient care"}
            elif "data" in focus_area_lower:
                return {"name": "Clinical Decision Support System", "description": "AI-driven diagnostic assistance and treatment recommendations", "value": "Improve diagnostic accuracy by 40%, reduce medical errors"}
            elif "digital" in focus_area_lower:
                return {"name": "Telemedicine AI Platform", "description": "Digital health monitoring and remote patient care with AI", "value": "Expand healthcare access, reduce costs by 30%"}
        
        elif "finance" in industry_lower or "banking" in industry_lower:
            if "automation" in focus_area_lower:
                return {"name": "Automated Risk Assessment", "description": "AI-powered credit scoring and fraud detection system", "value": "Reduce fraud by 85%, faster loan approvals"}
            elif "data" in focus_area_lower:
                return {"name": "Financial Analytics Platform", "description": "Real-time market analysis and investment insights", "value": "Improve investment returns by 25%, reduce risks"}
        
        elif "retail" in industry_lower or "e-commerce" in industry_lower:
            if "automation" in focus_area_lower:
                return {"name": "Inventory Management AI", "description": "Automated stock optimization and demand forecasting", "value": "Reduce inventory costs by 40%, prevent stockouts"}
            elif "customer" in focus_area_lower:
                return {"name": "Personalized Shopping Experience", "description": "AI-driven product recommendations and customer journey optimization", "value": "Increase sales by 35%, improve customer retention"}
        
        elif "automotive" in industry_lower or "tesla" in industry_lower:
            if "automation" in focus_area_lower:
                return {"name": "Autonomous Vehicle Systems", "description": "AI-powered self-driving technology and safety systems", "value": "Reduce accidents by 90%, enable autonomous transport"}
            elif "data" in focus_area_lower:
                return {"name": "Vehicle Performance Analytics", "description": "Real-time vehicle diagnostics and predictive maintenance", "value": "Reduce maintenance costs by 50%, improve reliability"}
        
        # Generic fallback
        if "automation" in focus_area_lower:
            return {"name": f"Process Automation for {industry}", "description": f"AI-powered workflow automation for {industry}", "value": "Reduce manual work by 60%, improve efficiency"}
        elif "data" in focus_area_lower:
            return {"name": f"Data Intelligence Platform", "description": f"Advanced analytics and insights for {industry}", "value": "Enable data-driven decisions, unlock insights"}
        elif "digital" in focus_area_lower:
            return {"name": f"Digital Transformation Suite", "description": f"Comprehensive digitization for {industry}", "value": "Accelerate digital adoption, improve operations"}
        
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
        """Generate industry-specific GenAI cases"""
        industry = research_data.get("industry", "")
        industry_lower = industry.lower()
        
        genai_cases = []
        
        # Industry-specific GenAI solutions
        if "healthcare" in industry_lower:
            genai_cases.append({"name": "Medical Report Generator", "description": "AI-powered generation of patient reports and clinical documentation", "value": "Reduce documentation time by 80%, improve accuracy"})
            genai_cases.append({"name": "Patient Communication Assistant", "description": "GenAI chatbot for patient queries and appointment scheduling", "value": "24/7 patient support, reduce staff workload by 60%"})
        
        elif "finance" in industry_lower:
            genai_cases.append({"name": "Financial Report Automation", "description": "Automated generation of financial reports and compliance documents", "value": "Reduce reporting time by 75%, ensure compliance"})
            genai_cases.append({"name": "Investment Advisory Chatbot", "description": "AI assistant for personalized investment advice and portfolio management", "value": "Improve client engagement, reduce advisory costs"})
        
        elif "retail" in industry_lower:
            genai_cases.append({"name": "Product Description Generator", "description": "Automated creation of product descriptions and marketing content", "value": "Scale content creation by 10x, improve SEO"})
            genai_cases.append({"name": "Virtual Shopping Assistant", "description": "AI-powered shopping guide and customer service chatbot", "value": "Increase conversion by 45%, reduce support costs"})
        
        elif "automotive" in industry_lower or "tesla" in industry_lower:
            genai_cases.append({"name": "Vehicle Manual Generator", "description": "AI-generated user manuals and technical documentation", "value": "Reduce documentation costs by 70%, improve clarity"})
            genai_cases.append({"name": "Customer Service AI", "description": "Intelligent assistant for vehicle support and troubleshooting", "value": "24/7 customer support, reduce service calls by 50%"})
        
        else:
            # Generic GenAI cases
            genai_cases.append({"name": f"Content Generation Platform", "description": f"AI-powered content creation for {industry}", "value": "Reduce content creation time by 70%"})
            genai_cases.append({"name": f"Industry Assistant Chatbot", "description": f"Intelligent virtual assistant for {industry}", "value": "24/7 support, improve customer satisfaction"})
        
        return genai_cases[:2]
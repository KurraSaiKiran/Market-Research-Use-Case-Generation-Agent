from typing import Dict, List

class UseCaseAgent:
    def __init__(self):
        self.use_case_templates = {
            "automotive": [
                {"name": "Predictive Maintenance", "description": "AI-powered vehicle maintenance prediction", "value": "Reduce downtime, lower costs"},
                {"name": "Autonomous Driving", "description": "Computer vision for self-driving capabilities", "value": "Safety improvement, market differentiation"},
                {"name": "Supply Chain Optimization", "description": "ML for inventory and logistics optimization", "value": "Cost reduction, efficiency gains"}
            ],
            "retail": [
                {"name": "Demand Forecasting", "description": "AI-powered inventory prediction", "value": "Reduce stockouts, optimize inventory"},
                {"name": "Personalized Recommendations", "description": "ML recommendation engine", "value": "Increase sales, customer satisfaction"},
                {"name": "Dynamic Pricing", "description": "AI-driven price optimization", "value": "Revenue optimization, competitive advantage"}
            ],
            "healthcare": [
                {"name": "Medical Image Analysis", "description": "AI for diagnostic imaging", "value": "Improved accuracy, faster diagnosis"},
                {"name": "Drug Discovery", "description": "ML for pharmaceutical research", "value": "Accelerated development, cost reduction"},
                {"name": "Patient Risk Assessment", "description": "Predictive analytics for patient outcomes", "value": "Better care, reduced readmissions"}
            ],
            "finance": [
                {"name": "Fraud Detection", "description": "ML for real-time transaction monitoring", "value": "Risk reduction, compliance"},
                {"name": "Credit Scoring", "description": "AI-powered loan approval systems", "value": "Better decisions, reduced defaults"},
                {"name": "Algorithmic Trading", "description": "ML for automated investment strategies", "value": "Higher returns, reduced human error"}
            ],
            "manufacturing": [
                {"name": "Quality Control", "description": "Computer vision for defect detection", "value": "Reduced waste, improved quality"},
                {"name": "Production Optimization", "description": "AI for workflow and resource optimization", "value": "Increased efficiency, cost savings"},
                {"name": "Equipment Monitoring", "description": "IoT + AI for machinery health tracking", "value": "Prevent breakdowns, extend lifespan"}
            ],
            "education": [
                {"name": "Personalized Learning", "description": "AI-adaptive learning platforms", "value": "Better outcomes, engagement"},
                {"name": "Automated Grading", "description": "NLP for assignment evaluation", "value": "Time savings, consistent feedback"},
                {"name": "Student Analytics", "description": "Predictive models for student success", "value": "Early intervention, retention"}
            ],
            "agriculture": [
                {"name": "Crop Monitoring", "description": "Satellite + AI for field analysis", "value": "Higher yields, resource optimization"},
                {"name": "Precision Farming", "description": "IoT sensors with ML for smart irrigation", "value": "Water savings, improved productivity"},
                {"name": "Pest Detection", "description": "Computer vision for early pest identification", "value": "Reduced crop loss, lower pesticide use"}
            ],
            "energy": [
                {"name": "Smart Grid Management", "description": "AI for energy distribution optimization", "value": "Efficiency gains, cost reduction"},
                {"name": "Renewable Forecasting", "description": "ML for solar/wind energy prediction", "value": "Better planning, grid stability"},
                {"name": "Energy Consumption Analytics", "description": "AI for usage pattern analysis", "value": "Cost savings, sustainability"}
            ],
            "logistics": [
                {"name": "Route Optimization", "description": "AI for delivery path planning", "value": "Fuel savings, faster delivery"},
                {"name": "Warehouse Automation", "description": "Robotics + AI for inventory management", "value": "Efficiency, accuracy improvement"},
                {"name": "Demand Planning", "description": "ML for logistics capacity forecasting", "value": "Cost optimization, service quality"}
            ],
            "media": [
                {"name": "Content Recommendation", "description": "AI for personalized media suggestions", "value": "User engagement, retention"},
                {"name": "Automated Editing", "description": "AI for video/audio content processing", "value": "Production speed, cost reduction"},
                {"name": "Audience Analytics", "description": "ML for viewer behavior analysis", "value": "Better content strategy, ad targeting"}
            ]
        }
    
    def generate_use_cases(self, research_data: Dict) -> List[Dict]:
        """Generate AI/GenAI use cases based on research"""
        industry = research_data.get("industry", "").lower()
        focus_areas = research_data.get("focus_areas", [])
        offerings = research_data.get("company_offerings", [])
        
        # Generate use cases based on actual research data
        use_cases = []
        
        # Generate use cases from focus areas
        for area in focus_areas[:3]:
            use_case = self._generate_use_case_from_focus_area(area, industry)
            if use_case:
                use_cases.append(use_case)
        
        # Generate use cases from company offerings
        for offering in offerings[:2]:
            use_case = self._generate_use_case_from_offering(offering, industry)
            if use_case:
                use_cases.append(use_case)
        
        # Add industry-specific template cases if needed
        if len(use_cases) < 4:
            template_cases = self._get_template_cases(industry)
            use_cases.extend(template_cases[:4-len(use_cases)])
        
        # Add GenAI cases based on research
        genai_cases = self._add_genai_cases_from_research(research_data)
        use_cases.extend(genai_cases)
        
        return use_cases[:8]  # Limit to 8 use cases
    
    def _generic_use_cases(self) -> List[Dict]:
        return [
            {"name": "Process Automation", "description": "RPA with AI decision making", "value": "Efficiency, cost reduction"},
            {"name": "Customer Support Chatbot", "description": "GenAI-powered customer service", "value": "24/7 support, cost savings"},
            {"name": "Document Processing", "description": "AI for document analysis", "value": "Speed, accuracy improvement"}
        ]
    
    def _generate_use_case_from_focus_area(self, focus_area: str, industry: str) -> Dict:
        """Generate use case based on focus area"""
        focus_area_lower = focus_area.lower()
        
        if "automation" in focus_area_lower:
            return {
                "name": "Intelligent Process Automation",
                "description": f"AI-powered automation for {industry} processes",
                "value": "Reduce manual work by 60%, improve accuracy and speed"
            }
        elif "customer" in focus_area_lower:
            return {
                "name": "AI Customer Experience Platform",
                "description": f"Personalized customer interactions for {industry}",
                "value": "Increase customer satisfaction by 40%, reduce response time"
            }
        elif "digital" in focus_area_lower:
            return {
                "name": "Digital Transformation Suite",
                "description": f"AI-driven digital modernization for {industry}",
                "value": "Accelerate digital adoption, improve operational efficiency"
            }
        elif "ai" in focus_area_lower:
            return {
                "name": "AI Integration Platform",
                "description": f"Comprehensive AI adoption framework for {industry}",
                "value": "Enable AI-first operations, competitive advantage"
            }
        elif "efficiency" in focus_area_lower:
            return {
                "name": "Operational Intelligence System",
                "description": f"AI-powered efficiency optimization for {industry}",
                "value": "Reduce costs by 30%, optimize resource utilization"
            }
        elif "data" in focus_area_lower:
            return {
                "name": "AI Data Analytics Platform",
                "description": f"Advanced analytics and insights for {industry}",
                "value": "Data-driven decisions, predictive capabilities"
            }
        
        return None
    
    def _generate_use_case_from_offering(self, offering: str, industry: str) -> Dict:
        """Generate use case based on company offering"""
        offering_lower = offering.lower()
        
        if "software" in offering_lower:
            return {
                "name": "AI-Enhanced Software Solutions",
                "description": f"Intelligent software platform for {industry}",
                "value": "Smart automation, predictive features, user optimization"
            }
        elif "cloud" in offering_lower:
            return {
                "name": "AI Cloud Infrastructure",
                "description": f"Intelligent cloud services for {industry}",
                "value": "Scalable AI deployment, cost optimization, performance"
            }
        elif "platform" in offering_lower:
            return {
                "name": "AI-Powered Platform Enhancement",
                "description": f"Intelligent platform capabilities for {industry}",
                "value": "Enhanced user experience, automated workflows"
            }
        elif "mobile" in offering_lower or "app" in offering_lower:
            return {
                "name": "Intelligent Mobile Solutions",
                "description": f"AI-driven mobile applications for {industry}",
                "value": "Personalized experiences, predictive features"
            }
        elif "data" in offering_lower:
            return {
                "name": "AI Data Intelligence Suite",
                "description": f"Advanced data processing and insights for {industry}",
                "value": "Real-time analytics, predictive modeling"
            }
        
        return None
    
    def _get_template_cases(self, industry: str) -> List[Dict]:
        """Get template cases for industry"""
        for key in self.use_case_templates:
            if key in industry:
                return self.use_case_templates[key]
        return self._generic_use_cases()
    
    def _add_genai_cases_from_research(self, research_data: Dict) -> List[Dict]:
        """Generate GenAI cases based on research data"""
        industry = research_data.get("industry", "").lower()
        focus_areas = research_data.get("focus_areas", [])
        
        genai_cases = []
        
        # Always include content generation
        genai_cases.append({
            "name": "GenAI Content Creation",
            "description": f"AI-powered content generation for {industry} marketing and communications",
            "value": "Reduce content creation time by 70%, improve personalization"
        })
        
        # Add customer-focused GenAI if customer experience is a focus
        if any("customer" in area.lower() for area in focus_areas):
            genai_cases.append({
                "name": "Conversational AI Assistant",
                "description": f"Intelligent chatbot and virtual assistant for {industry} customers",
                "value": "24/7 support, reduce support costs by 50%, improve satisfaction"
            })
        
        # Add data analysis GenAI if data is mentioned
        if any("data" in area.lower() for area in focus_areas):
            genai_cases.append({
                "name": "AI Business Intelligence Assistant",
                "description": f"Natural language interface for {industry} data analysis and reporting",
                "value": "Democratize data access, faster insights, automated reporting"
            })
        
        return genai_cases[:2]  # Limit to 2 GenAI cases
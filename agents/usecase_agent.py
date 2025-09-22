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
        trends = research_data.get("market_trends", [])
        
        print(f"[DEBUG] Generating use cases for industry: {industry}")
        print(f"[DEBUG] Focus areas: {focus_areas}")
        print(f"[DEBUG] Market trends: {trends}")
        
        use_cases = []
        
        # Generate use cases from focus areas (priority)
        for area in focus_areas[:4]:
            use_case = self._generate_use_case_from_focus_area(area, industry)
            if use_case and use_case not in use_cases:
                use_cases.append(use_case)
        
        # Generate use cases from market trends
        for trend in trends[:2]:
            use_case = self._generate_use_case_from_trend(trend, industry)
            if use_case and use_case not in use_cases:
                use_cases.append(use_case)
        
        # Add industry-specific template cases if needed
        if len(use_cases) < 5:
            template_cases = self._get_template_cases(industry)
            for case in template_cases:
                if case not in use_cases and len(use_cases) < 5:
                    use_cases.append(case)
        
        # Add GenAI cases based on research
        genai_cases = self._add_genai_cases_from_research(research_data)
        for case in genai_cases:
            if case not in use_cases and len(use_cases) < 7:
                use_cases.append(case)
        
        print(f"[DEBUG] Generated {len(use_cases)} use cases")
        return use_cases[:7]
    
    def _generic_use_cases(self) -> List[Dict]:
        return [
            {"name": "Process Automation", "description": "RPA with AI decision making", "value": "Efficiency, cost reduction"},
            {"name": "Customer Support Chatbot", "description": "GenAI-powered customer service", "value": "24/7 support, cost savings"},
            {"name": "Document Processing", "description": "AI for document analysis", "value": "Speed, accuracy improvement"}
        ]
    
    def _generate_use_case_from_focus_area(self, focus_area: str, industry: str) -> Dict:
        """Generate use case based on focus area"""
        focus_area_lower = focus_area.lower()
        
        # Industry-specific automation
        if "automation" in focus_area_lower:
            if "healthcare" in industry:
                return {"name": "Medical Process Automation", "description": "AI-powered patient workflow and clinical process automation", "value": "Reduce administrative burden by 70%, improve patient care"}
            elif "finance" in industry:
                return {"name": "Financial Process Automation", "description": "Automated loan processing, compliance, and risk assessment", "value": "Reduce processing time by 80%, ensure regulatory compliance"}
            elif "retail" in industry:
                return {"name": "Retail Operations Automation", "description": "Automated inventory management and supply chain optimization", "value": "Reduce stockouts by 60%, optimize inventory costs"}
            else:
                return {"name": "Intelligent Process Automation", "description": f"AI-powered workflow automation for {industry}", "value": "Reduce manual work by 60%, improve accuracy"}
        
        # Industry-specific customer experience
        elif "customer" in focus_area_lower:
            if "healthcare" in industry:
                return {"name": "Patient Experience AI", "description": "Personalized patient journey optimization and care coordination", "value": "Improve patient satisfaction by 45%, reduce wait times"}
            elif "finance" in industry:
                return {"name": "Financial Advisory AI", "description": "Personalized financial advice and customer service automation", "value": "Increase customer retention by 35%, reduce service costs"}
            elif "retail" in industry:
                return {"name": "Retail Personalization Engine", "description": "AI-driven product recommendations and customer journey optimization", "value": "Increase conversion rates by 40%, boost customer loyalty"}
            else:
                return {"name": "AI Customer Experience Platform", "description": f"Personalized customer interactions for {industry}", "value": "Increase satisfaction by 40%, reduce response time"}
        
        # Industry-specific digital transformation
        elif "digital" in focus_area_lower:
            if "healthcare" in industry:
                return {"name": "Digital Health Platform", "description": "AI-powered telemedicine and digital patient management system", "value": "Expand patient reach by 300%, reduce operational costs"}
            elif "finance" in industry:
                return {"name": "Digital Banking Transformation", "description": "AI-driven mobile banking and digital financial services", "value": "Increase digital adoption by 250%, reduce branch costs"}
            else:
                return {"name": "Digital Transformation Suite", "description": f"AI-driven digital modernization for {industry}", "value": "Accelerate digital adoption, improve efficiency"}
        
        # Data and analytics
        elif "data" in focus_area_lower:
            if "healthcare" in industry:
                return {"name": "Clinical Data Intelligence", "description": "AI-powered analysis of patient data and clinical outcomes", "value": "Improve treatment outcomes by 30%, reduce costs"}
            elif "finance" in industry:
                return {"name": "Financial Risk Analytics", "description": "Real-time fraud detection and risk assessment platform", "value": "Reduce fraud losses by 85%, improve risk management"}
            else:
                return {"name": "AI Data Analytics Platform", "description": f"Advanced analytics and insights for {industry}", "value": "Data-driven decisions, predictive capabilities"}
        
        # Security and compliance
        elif "security" in focus_area_lower or "compliance" in focus_area_lower:
            return {"name": "AI Security & Compliance Suite", "description": f"Automated security monitoring and compliance management for {industry}", "value": "Reduce security incidents by 75%, ensure compliance"}
        
        # Sustainability
        elif "sustainability" in focus_area_lower:
            return {"name": "Sustainability Intelligence Platform", "description": f"AI-powered ESG tracking and carbon footprint optimization for {industry}", "value": "Reduce carbon footprint by 40%, improve ESG scores"}
        
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
    
    def _generate_use_case_from_trend(self, trend: str, industry: str) -> Dict:
        """Generate use case based on market trend"""
        trend_lower = trend.lower()
        
        if "ai integration" in trend_lower:
            return {"name": "AI-First Platform", "description": f"Comprehensive AI integration across {industry} operations", "value": "Transform business model, gain competitive advantage"}
        elif "cloud" in trend_lower:
            return {"name": "Cloud-Native AI Solutions", "description": f"Scalable cloud-based AI infrastructure for {industry}", "value": "Reduce infrastructure costs by 50%, improve scalability"}
        elif "sustainability" in trend_lower:
            return {"name": "Green AI Initiative", "description": f"AI-powered sustainability optimization for {industry}", "value": "Reduce environmental impact by 35%, meet ESG goals"}
        elif "cybersecurity" in trend_lower:
            return {"name": "AI-Powered Cybersecurity", "description": f"Intelligent threat detection and response for {industry}", "value": "Reduce security incidents by 80%, faster threat response"}
        
        return None
    
    def _add_genai_cases_from_research(self, research_data: Dict) -> List[Dict]:
        """Generate GenAI cases based on research data"""
        industry = research_data.get("industry", "").lower()
        focus_areas = research_data.get("focus_areas", [])
        
        genai_cases = []
        
        # Industry-specific content generation
        if "healthcare" in industry:
            genai_cases.append({"name": "Medical Content AI", "description": "AI-powered medical documentation and patient communication generation", "value": "Reduce documentation time by 75%, improve patient communication"})
        elif "finance" in industry:
            genai_cases.append({"name": "Financial Report Generator", "description": "Automated financial analysis and regulatory report generation", "value": "Reduce reporting time by 80%, ensure compliance accuracy"})
        else:
            genai_cases.append({"name": "GenAI Content Creation", "description": f"AI-powered content generation for {industry} marketing and communications", "value": "Reduce content creation time by 70%, improve personalization"})
        
        # Add conversational AI if customer focus exists
        if any("customer" in area.lower() for area in focus_areas):
            if "healthcare" in industry:
                genai_cases.append({"name": "Virtual Health Assistant", "description": "AI-powered patient support and medical query assistance", "value": "24/7 patient support, reduce call center load by 60%"})
            elif "finance" in industry:
                genai_cases.append({"name": "Financial Advisory Chatbot", "description": "Intelligent financial planning and investment advice assistant", "value": "Personalized advice at scale, reduce advisor workload by 40%"})
            else:
                genai_cases.append({"name": "Conversational AI Assistant", "description": f"Intelligent customer support for {industry}", "value": "24/7 support, reduce costs by 50%"})
        
        return genai_cases[:2]
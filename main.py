import os
from dotenv import load_dotenv
from agents.research_agent import ResearchAgent
from agents.usecase_agent import UseCaseAgent  
from agents.resource_agent import ResourceAgent
from agents.report_agent import ReportAgent
from agents.bonus_agent import BonusAgent

class MultiAgentResearchSystem:
    def __init__(self):
        load_dotenv()
        self.research_agent = ResearchAgent()
        self.usecase_agent = UseCaseAgent()
        self.resource_agent = ResourceAgent()
        self.bonus_agent = BonusAgent()
        self.report_agent = ReportAgent()
    
    def run_research(self, query: str) -> dict:
        """Execute the complete research workflow"""
        print(f"[INFO] Starting research for: {query}")
        
        try:
            # Step 1: Industry/Company Research
            print("[STEP 1] Agent 1: Conducting industry research...")
            research_data = self.research_agent.research_company_industry(query)
            print(f"   [OK] Found industry: {research_data['industry']}")
            
            # Step 2: Generate Use Cases
            print("[STEP 2] Agent 2: Generating AI/GenAI use cases...")
            use_cases = self.usecase_agent.generate_use_cases(research_data)
            print(f"   [OK] Generated {len(use_cases)} use cases")
            
            # Step 3: Find Resources
            print("[STEP 3] Agent 3: Finding datasets and resources...")
            resources = self.resource_agent.find_resources(use_cases)
            total_resources = sum(len(r) for r in resources.values())
            print(f"   [OK] Found {total_resources} resources")
            
            # Step 4: Generate Bonus Solutions
            print("[STEP 4] Agent 4: Generating bonus GenAI solutions...")
            bonus_solutions = self.bonus_agent.generate_bonus_solutions(research_data['industry'], use_cases)
            bonus_count = len(bonus_solutions.get('internal_solutions', [])) + len(bonus_solutions.get('customer_solutions', []))
            print(f"   [OK] Generated {bonus_count} bonus solutions")
            
            # Step 5: Generate Report
            print("[STEP 5] Report Agent: Generating final report...")
            report = self.report_agent.generate_report(query, research_data, use_cases, resources, bonus_solutions)
            
            # Save outputs
            try:
                md_file = self.report_agent.save_report(report)
                print(f"   [OK] Saved markdown: {md_file}")
            except Exception as e:
                print(f"   [WARN] Markdown save error: {e}")
                md_file = "report_save_failed.md"
            
            try:
                pdf_file = self.report_agent.export_pdf(report)
                print(f"   [OK] Saved PDF: {pdf_file}")
            except Exception as e:
                print(f"   [WARN] PDF export error: {e}")
                pdf_file = None
            
            print(f"[SUCCESS] Research complete!")
            
            return {
                "research_data": research_data,
                "use_cases": use_cases, 
                "resources": resources,
                "bonus_solutions": bonus_solutions,
                "report": report,
                "files": {"markdown": md_file, "pdf": pdf_file}
            }
            
        except Exception as e:
            print(f"[ERROR] Research failed: {str(e)}")
            raise e

def main():
    try:
        system = MultiAgentResearchSystem()
        
        # Example usage
        query = input("Enter company name or industry: ").strip()
        if not query:
            query = "Tesla Motors"  # Default example
        
        results = system.run_research(query)
    except KeyboardInterrupt:
        print("\n[INFO] Research cancelled by user")
        return
    except Exception as e:
        print(f"\n[ERROR] System error: {str(e)}")
        return
    
    # Display summary
    print(f"\n[SUMMARY]")
    print(f"- Industry: {results['research_data']['industry']}")
    print(f"- Use cases generated: {len(results['use_cases'])}")
    print(f"- Resources found: {sum(len(r) for r in results['resources'].values())}")
    bonus_count = len(results['bonus_solutions'].get('internal_solutions', [])) + len(results['bonus_solutions'].get('customer_solutions', []))
    print(f"- Bonus solutions: {bonus_count}")
    print(f"- Report files: {results['files']}")

if __name__ == "__main__":
    main()
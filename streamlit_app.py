import streamlit as st
import os
import json
from dotenv import load_dotenv
from main import MultiAgentResearchSystem

# Load environment variables at startup
load_dotenv()

st.set_page_config(
    page_title="Multi-Agent AI Research System",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

def main():
    # Clean CSS
    st.markdown("""
    <style>
    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
        padding: 2rem;
        border-radius: 15px;
        margin-bottom: 2rem;
        text-align: center;
    }
    .workflow-container {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        padding: 1.5rem;
        border-radius: 15px;
        margin: 1rem 0;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Header
    st.markdown("""
    <div class="main-header">
        <h1 style="color: white; margin: 0; font-size: 2.5rem;">🤖 Multi-Agent AI Research System</h1>
        <p style="color: rgba(255,255,255,0.9); margin: 0.5rem 0 0 0;">Comprehensive AI/GenAI Market Analysis & Use Case Generation</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Workflow
    st.markdown("### 🔄 4-Agent Intelligent Workflow")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown("""
        <div style="background: white; padding: 1rem; border-radius: 10px; text-align: center; border: 2px solid #667eea; color: #2c3e50;">
            <div style="font-size: 2rem;">📊</div>
            <div style="font-weight: bold; font-size: 1rem; margin: 0.5rem 0;">Agent 1: Research</div>
            <div style="font-size: 0.85rem; color: #666;">Industry Analysis & Trends</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="background: white; padding: 1rem; border-radius: 10px; text-align: center; border: 2px solid #667eea; color: #2c3e50;">
            <div style="font-size: 2rem;">💡</div>
            <div style="font-weight: bold; font-size: 1rem; margin: 0.5rem 0;">Agent 2: Use Cases</div>
            <div style="font-size: 0.85rem; color: #666;">AI/GenAI Solutions</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div style="background: white; padding: 1rem; border-radius: 10px; text-align: center; border: 2px solid #667eea; color: #2c3e50;">
            <div style="font-size: 2rem;">📚</div>
            <div style="font-weight: bold; font-size: 1rem; margin: 0.5rem 0;">Agent 3: Resources</div>
            <div style="font-size: 0.85rem; color: #666;">Datasets & Models</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div style="background: white; padding: 1rem; border-radius: 10px; text-align: center; border: 2px solid #667eea; color: #2c3e50;">
            <div style="font-size: 2rem;">✨</div>
            <div style="font-weight: bold; font-size: 1rem; margin: 0.5rem 0;">Agent 4: Bonus</div>
            <div style="font-size: 0.85rem; color: #666;">GenAI Opportunities</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="text-align: center; margin: 1rem 0; font-size: 1.2rem; color: #667eea;">
        📊 → 💡 → 📚 → ✨
    </div>
    """, unsafe_allow_html=True)
    
    # Sidebar
    with st.sidebar:
        st.markdown("### 📋 How to Use This Workflow")
        
        st.markdown("""
        **🔄 4-Agent Process:**
        1. **📊 Research Agent** - Analyzes industry trends, competitors, market size
        2. **💡 Use Case Agent** - Generates 5-8 tailored AI/GenAI solutions
        3. **📚 Resource Agent** - Finds real datasets from Kaggle, GitHub, HuggingFace
        4. **✨ Bonus Agent** - Creates internal & customer-facing GenAI opportunities
        
        **📝 Input Examples:**
        • Company: 'Tesla Motors', 'Apple Inc'
        • Industry: 'Healthcare Industry', 'Retail'
        
        **⚙️ Requirements:**
        • API keys required for real-time data
        • Analysis takes 30-60 seconds
        • All data fetched live from APIs
        """)
    
    # Main interface
    st.markdown("---")
    
    # Example buttons
    st.markdown("**Quick Examples:**")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        if st.button("Tesla Motors", use_container_width=True):
            st.session_state.example_query = "Tesla Motors"
    with col2:
        if st.button("Healthcare Industry", use_container_width=True):
            st.session_state.example_query = "Healthcare Industry"
    with col3:
        if st.button("Financial Services", use_container_width=True):
            st.session_state.example_query = "Financial Services"
    with col4:
        if st.button("Retail Industry", use_container_width=True):
            st.session_state.example_query = "Retail Industry"
    
    query = st.text_input(
        "🏢 Enter Company Name or Industry:",
        value=st.session_state.get('example_query', ''),
        placeholder="e.g., Tesla Motors, Healthcare Industry, Financial Services"
    )
    
    if st.button("🚀 Start AI Research", use_container_width=True):
        if query:
            # Load environment variables
            from dotenv import load_dotenv
            load_dotenv()
            
            # Progress tracking
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            try:
                system = MultiAgentResearchSystem()
                
                # Agent 1
                status_text.text("📊 Agent 1: Conducting industry research...")
                progress_bar.progress(25)
                
                # Agent 2
                status_text.text("💡 Agent 2: Generating AI/GenAI use cases...")
                progress_bar.progress(50)
                
                # Agent 3
                status_text.text("📚 Agent 3: Finding datasets and resources...")
                progress_bar.progress(75)
                
                # Agent 4
                status_text.text("✨ Agent 4: Generating bonus GenAI solutions...")
                progress_bar.progress(100)
                
                results = system.run_research(query)
                st.session_state.results = results
                
                progress_bar.empty()
                status_text.empty()
                
            except Exception as e:
                st.error(f"Error: {str(e)}")
                st.stop()
            
            results = st.session_state.get('results')
            if results:
                st.success("🎉 Research Complete!")
                
                # Metrics
                col1, col2, col3, col4 = st.columns(4)
                with col1:
                    st.metric("🏢 Industry", results['research_data']['industry'])
                with col2:
                    st.metric("💡 Use Cases", len(results['use_cases']))
                with col3:
                    st.metric("📚 Resources", sum(len(r) for r in results['resources'].values()))
                with col4:
                    bonus_count = 0
                    if 'bonus_solutions' in results:
                        bonus_count = len(results['bonus_solutions'].get('internal_solutions', [])) + len(results['bonus_solutions'].get('customer_solutions', []))
                    st.metric("✨ Bonus", bonus_count)
                
                st.markdown("---")
                
                # Tabs
                tab1, tab2, tab3, tab4, tab5 = st.tabs([
                    "📊 Research", 
                    "💡 Use Cases", 
                    "📚 Resources", 
                    "✨ Bonus", 
                    "📥 Downloads"
                ])
                
                with tab1:
                    research = results['research_data']
                    
                    col1, col2 = st.columns(2)
                    with col1:
                        st.markdown("**🎯 Offerings:**")
                        for offering in research.get('company_offerings', []):
                            st.write(f"• {offering}")
                        
                        st.markdown("**🔍 Focus Areas:**")
                        for area in research.get('focus_areas', []):
                            st.write(f"• {area}")
                    
                    with col2:
                        st.markdown("**🏆 Competitors:**")
                        for comp in research.get('competitors', []):
                            st.write(f"• {comp}")
                        
                        st.markdown("**📈 Trends:**")
                        for trend in research.get('market_trends', []):
                            st.write(f"• {trend}")
                    
                    st.info(research.get('market_size', 'Market analysis available'))
                
                with tab2:
                    for i, use_case in enumerate(results['use_cases'], 1):
                        with st.expander(f"🚀 {use_case['name']}", expanded=i<=2):
                            st.write(f"**Description:** {use_case['description']}")
                            st.write(f"**Business Value:** {use_case['value']}")
                            resource_count = len(results['resources'].get(use_case['name'], []))
                            st.caption(f"Resources available: {resource_count}")
                
                with tab3:
                    for use_case_name, resources in results['resources'].items():
                        if resources:
                            with st.expander(f"📦 {use_case_name}"):
                                for resource in resources:
                                    st.markdown(f"**[{resource['name']}]({resource['url']})** - {resource['type']}")
                                    st.caption(resource.get('description', 'No description'))
                
                with tab4:
                    if 'bonus_solutions' in results and results['bonus_solutions']:
                        bonus = results['bonus_solutions']
                        
                        st.markdown("**🏢 Internal Solutions:**")
                        for solution in bonus.get('internal_solutions', []):
                            with st.expander(f"🔧 {solution['name']}"):
                                st.write(solution['description'])
                                st.write(f"**Value:** {solution['value']}")
                        
                        st.markdown("**👥 Customer Solutions:**")
                        for solution in bonus.get('customer_solutions', []):
                            with st.expander(f"🎯 {solution['name']}"):
                                st.write(solution['description'])
                                st.write(f"**Value:** {solution['value']}")
                        
                        if 'roi_estimates' in bonus:
                            st.markdown("**💰 ROI Estimates:**")
                            roi = bonus['roi_estimates']
                            st.write(f"• Cost Savings: {roi.get('cost_savings', 'TBD')}")
                            st.write(f"• Revenue Impact: {roi.get('revenue_impact', 'TBD')}")
                            st.write(f"• Efficiency Gains: {roi.get('efficiency_gains', 'TBD')}")
                            st.write(f"• Payback Period: {roi.get('payback_period', 'TBD')}")
                    else:
                        st.info("Bonus solutions not available")
                
                with tab5:
                    st.markdown("**📥 Download Reports:**")
                    
                    col1, col2, col3 = st.columns(3)
                    with col1:
                        st.download_button(
                            "📄 Markdown",
                            data=results['report'],
                            file_name=f"{query.replace(' ', '_')}_research.md",
                            mime="text/markdown",
                            use_container_width=True
                        )
                    
                    with col2:
                        try:
                            if results['files']['pdf'] and os.path.exists(results['files']['pdf']):
                                with open(results['files']['pdf'], 'rb') as f:
                                    st.download_button(
                                        "📄 PDF", 
                                        data=f.read(),
                                        file_name=f"{query.replace(' ', '_')}_research.pdf",
                                        mime="application/pdf",
                                        use_container_width=True
                                    )
                            else:
                                st.info("PDF unavailable")
                        except:
                            st.warning("PDF unavailable")
                    
                    with col3:
                        summary_data = {
                            "query": query,
                            "industry": results['research_data']['industry'],
                            "use_cases_count": len(results['use_cases']),
                            "resources_count": sum(len(r) for r in results['resources'].values()),
                            "bonus_solutions_count": bonus_count
                        }
                        st.download_button(
                            "📊 JSON",
                            data=json.dumps(summary_data, indent=2),
                            file_name=f"{query.replace(' ', '_')}_summary.json",
                            mime="application/json",
                            use_container_width=True
                        )
                    
                    st.markdown("---")
                    st.success("✅ Analysis Complete - All 4 agents executed successfully")
                    st.info("📊 Research Agent → 💡 Use Case Agent → 📚 Resource Agent → ✨ Bonus Agent")
            else:
                st.error("No results available")
        else:
            st.error("Please enter a company name or industry")

if __name__ == "__main__":
    main()
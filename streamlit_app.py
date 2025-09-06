import streamlit as st
import os
import json
from main import MultiAgentResearchSystem

st.set_page_config(
    page_title="Multi-Agent AI Research System",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

def main():
    # Custom CSS for professional styling
    st.markdown("""
    <style>
    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
        padding: 3rem 2rem;
        border-radius: 20px;
        margin-bottom: 2rem;
        box-shadow: 0 10px 30px rgba(0,0,0,0.2);
        animation: fadeInDown 1s ease-out;
    }
    
    .workflow-container {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        padding: 2rem;
        border-radius: 20px;
        margin: 2rem 0;
        box-shadow: 0 8px 25px rgba(0,0,0,0.1);
    }
    
    .agent-card {
        background: white;
        padding: 1.5rem;
        border-radius: 15px;
        box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        transition: all 0.3s ease;
        border: 2px solid transparent;
        min-width: 180px;
        text-align: center;
    }
    
    .agent-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 35px rgba(0,0,0,0.2);
        border: 2px solid #667eea;
    }
    
    .agent-icon {
        font-size: 2.5rem;
        margin-bottom: 0.5rem;
        display: block;
    }
    
    .agent-title {
        font-weight: bold;
        color: #2c3e50;
        font-size: 1.1rem;
        margin-bottom: 0.3rem;
    }
    
    .agent-desc {
        color: #7f8c8d;
        font-size: 0.9rem;
    }
    
    .workflow-arrow {
        font-size: 2rem;
        color: #667eea;
        animation: pulse 2s infinite;
    }
    
    .custom-button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        padding: 0.75rem 2rem;
        border-radius: 25px;
        font-weight: bold;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
    }
    
    .custom-button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(102, 126, 234, 0.6);
    }
    
    .example-button {
        background: linear-gradient(135deg, #74b9ff 0%, #0984e3 100%);
        color: white;
        border: none;
        padding: 0.6rem 1.5rem;
        border-radius: 20px;
        margin: 0.3rem;
        transition: all 0.3s ease;
        box-shadow: 0 3px 10px rgba(116, 185, 255, 0.3);
        width: 100%;
    }
    
    .example-button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(116, 185, 255, 0.5);
    }
    
    @keyframes fadeInDown {
        from { opacity: 0; transform: translateY(-30px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.1); }
        100% { transform: scale(1); }
    }
    
    .metric-card {
        background: white;
        padding: 1.5rem;
        border-radius: 15px;
        box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        transition: all 0.3s ease;
        border-left: 4px solid #667eea;
    }
    
    .metric-card:hover {
        transform: translateY(-3px);
        box-shadow: 0 10px 25px rgba(0,0,0,0.15);
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Professional header
    st.markdown("""
    <div class="main-header">
        <h1 style="color: white; text-align: center; margin: 0; font-size: 3rem; font-weight: 700;">
            🤖 Multi-Agent AI Research System
        </h1>
        <p style="color: rgba(255,255,255,0.9); text-align: center; margin: 1rem 0 0 0; font-size: 1.3rem; font-weight: 300;">
            Comprehensive AI/GenAI Market Analysis & Use Case Generation
        </p>
        <div style="text-align: center; margin-top: 1.5rem;">
            <span style="background: rgba(255,255,255,0.2); padding: 0.5rem 1rem; border-radius: 20px; color: white; font-size: 0.9rem;">
                ✨ Powered by Real-Time APIs • 🚀 4-Agent Workflow • 📈 Professional Reports
            </span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Enhanced agent workflow visualization
    st.markdown("""
    <div class="workflow-container">
        <h2 style="text-align: center; color: #2c3e50; margin-bottom: 2rem; font-weight: 600;">
            🔄 Intelligent 4-Agent Workflow
        </h2>
        <div style="display: flex; justify-content: center; align-items: center; gap: 1.5rem; flex-wrap: wrap;">
            <div class="agent-card">
                <div class="agent-icon">📊</div>
                <div class="agent-title">Agent 1</div>
                <div class="agent-desc">Industry Research<br><small>Web Search & Analysis</small></div>
            </div>
            <div class="workflow-arrow">→</div>
            <div class="agent-card">
                <div class="agent-icon">💡</div>
                <div class="agent-title">Agent 2</div>
                <div class="agent-desc">Use Case Generation<br><small>AI/GenAI Solutions</small></div>
            </div>
            <div class="workflow-arrow">→</div>
            <div class="agent-card">
                <div class="agent-icon">📚</div>
                <div class="agent-title">Agent 3</div>
                <div class="agent-desc">Resource Discovery<br><small>Datasets & Models</small></div>
            </div>
            <div class="workflow-arrow">→</div>
            <div class="agent-card">
                <div class="agent-icon">✨</div>
                <div class="agent-title">Agent 4</div>
                <div class="agent-desc">Bonus Solutions<br><small>GenAI Opportunities</small></div>
            </div>
        </div>
        <div style="text-align: center; margin-top: 1.5rem;">
            <p style="color: #7f8c8d; font-style: italic;">
                Each agent processes real-time data to deliver comprehensive market insights
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Professional sidebar
    with st.sidebar:
        st.markdown("""
        <style>
        .sidebar-header {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 1rem;
            border-radius: 10px;
            text-align: center;
            margin-bottom: 1.5rem;
        }
        
        .api-status-card {
            background: #f8f9fa;
            padding: 1rem;
            border-radius: 10px;
            margin: 0.5rem 0;
            border-left: 4px solid #28a745;
        }
        
        .api-status-inactive {
            border-left-color: #ffc107;
        }
        
        .capability-item {
            background: white;
            padding: 0.8rem;
            border-radius: 8px;
            margin: 0.5rem 0;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
            border-left: 3px solid #667eea;
        }
        </style>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="sidebar-header">
            <h3 style="margin: 0;">⚙️ System Configuration</h3>
            <p style="margin: 0.5rem 0 0 0; opacity: 0.9; font-size: 0.9rem;">Real-time API Integration</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Enhanced API status check
        env_file = ".env"
        if os.path.exists(env_file):
            st.markdown("""
            <div style="background: #d4edda; color: #155724; padding: 1rem; border-radius: 8px; margin-bottom: 1rem; border: 1px solid #c3e6cb;">
                ✅ <strong>Configuration Active</strong><br>
                <small>All API keys loaded successfully</small>
            </div>
            """, unsafe_allow_html=True)
            
            # Show API status with enhanced styling
            api_keys = {
                "SERPER_API_KEY": ("🔍", "Web Search", "Real-time market research"),
                "GITHUB_TOKEN": ("🐙", "GitHub Access", "Code repositories & projects"), 
                "KAGGLE_KEY": ("📊", "Kaggle Datasets", "ML datasets & competitions"),
                "HUGGINGFACE_API_KEY": ("🤗", "HuggingFace", "Pre-trained AI models")
            }
            
            st.markdown("**🔌 API Integration Status:**")
            for key, (icon, name, desc) in api_keys.items():
                status = "active" if os.getenv(key) else "inactive"
                status_icon = "✅" if os.getenv(key) else "🟡"
                status_class = "api-status-card" if os.getenv(key) else "api-status-card api-status-inactive"
                
                st.markdown(f"""
                <div class="{status_class}">
                    <strong>{status_icon} {icon} {name}</strong><br>
                    <small style="color: #6c757d;">{desc}</small>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div style="background: #fff3cd; color: #856404; padding: 1rem; border-radius: 8px; margin-bottom: 1rem; border: 1px solid #ffeaa7;">
                ⚠️ <strong>Fallback Mode</strong><br>
                <small>Using demo data - add .env for live APIs</small>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("---")
        st.markdown("""
        <div style="text-align: center; margin: 1rem 0;">
            <h4 style="color: #667eea; margin-bottom: 1rem;">📈 System Capabilities</h4>
        </div>
        """, unsafe_allow_html=True)
        
        capabilities = [
            ("🏢", "10+ Industries", "Comprehensive sector coverage"),
            ("💡", "30+ Use Cases", "AI/GenAI solution templates"),
            ("🔄", "Real-time APIs", "Live data integration"),
            ("📄", "Multi-format Export", "MD, PDF, JSON reports"),
            ("✨", "Bonus Solutions", "GenAI opportunities")
        ]
        
        for icon, title, desc in capabilities:
            st.markdown(f"""
            <div class="capability-item">
                <strong>{icon} {title}</strong><br>
                <small style="color: #6c757d;">{desc}</small>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("---")
        st.markdown("""
        <div style="background: linear-gradient(135deg, #74b9ff 0%, #0984e3 100%); color: white; padding: 1rem; border-radius: 10px;">
            <h4 style="margin: 0 0 0.5rem 0;">🎯 Pro Tips</h4>
            <ul style="margin: 0; padding-left: 1rem; font-size: 0.9rem;">
                <li>Use specific company names for detailed analysis</li>
                <li>Try "[Industry] Industry" for sector analysis</li>
                <li>All resources include clickable links</li>
                <li>Reports available in multiple formats</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # Main interface
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Initialize session state
        if 'query' not in st.session_state:
            st.session_state.query = ""
            
        query = st.text_input(
            "🏢 Enter Company Name or Industry:",
            value=st.session_state.query,
            placeholder="e.g., Tesla Motors, Retail Industry, Healthcare"
        )
        
        # Custom styled button
        st.markdown("""
        <div style="text-align: center; margin: 2rem 0;">
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("🚀 Start AI Research", key="research_btn", help="Click to begin comprehensive AI market analysis"):
            if query:
                with st.spinner("🔍 Running multi-agent research..."):
                    try:
                        system = MultiAgentResearchSystem()
                        results = system.run_research(query)
                        st.session_state.results = results
                    except Exception as e:
                        st.error(f"Error during research: {str(e)}")
                        st.stop()
                
                # Store results in session state
                results = st.session_state.get('results')
                if results:
                    st.success("🎉 Multi-Agent Research Complete! Explore the results in the tabs below.")
                    
                    # Enhanced quick stats with custom styling
                    st.markdown("""
                    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1rem; margin: 1.5rem 0;">
                    """, unsafe_allow_html=True)
                    
                    col1, col2, col3, col4 = st.columns(4)
                    with col1:
                        st.markdown("""
                        <div class="metric-card">
                            <h3 style="color: #667eea; margin: 0;">🏢 Industry</h3>
                            <p style="font-size: 1.2rem; font-weight: bold; margin: 0.5rem 0 0 0; color: #2c3e50;">{}</p>
                        </div>
                        """.format(results['research_data']['industry']), unsafe_allow_html=True)
                    
                    with col2:
                        st.markdown("""
                        <div class="metric-card">
                            <h3 style="color: #667eea; margin: 0;">💡 Use Cases</h3>
                            <p style="font-size: 1.2rem; font-weight: bold; margin: 0.5rem 0 0 0; color: #2c3e50;">{}</p>
                        </div>
                        """.format(len(results['use_cases'])), unsafe_allow_html=True)
                    
                    with col3:
                        st.markdown("""
                        <div class="metric-card">
                            <h3 style="color: #667eea; margin: 0;">📚 Resources</h3>
                            <p style="font-size: 1.2rem; font-weight: bold; margin: 0.5rem 0 0 0; color: #2c3e50;">{}</p>
                        </div>
                        """.format(sum(len(r) for r in results['resources'].values())), unsafe_allow_html=True)
                    
                    with col4:
                        bonus_count = 0
                        if 'bonus_solutions' in results:
                            bonus_count = len(results['bonus_solutions'].get('internal_solutions', [])) + len(results['bonus_solutions'].get('customer_solutions', []))
                        st.markdown("""
                        <div class="metric-card">
                            <h3 style="color: #667eea; margin: 0;">✨ Bonus Solutions</h3>
                            <p style="font-size: 1.2rem; font-weight: bold; margin: 0.5rem 0 0 0; color: #2c3e50;">{}</p>
                        </div>
                        """.format(bonus_count), unsafe_allow_html=True)
                    
                    st.markdown("</div>", unsafe_allow_html=True)
                else:
                    st.error("No results available")
                    st.stop()
                
                # Professional tabs with enhanced styling
                st.markdown("""
                <style>
                .stTabs [data-baseweb="tab-list"] {
                    gap: 8px;
                }
                .stTabs [data-baseweb="tab"] {
                    height: 60px;
                    padding: 0px 20px;
                    background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
                    border-radius: 10px 10px 0px 0px;
                    border: 2px solid transparent;
                    transition: all 0.3s ease;
                }
                .stTabs [aria-selected="true"] {
                    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                    color: white;
                    border: 2px solid #667eea;
                }
                </style>
                """, unsafe_allow_html=True)
                
                tab1, tab2, tab3, tab4, tab5 = st.tabs([
                    "📊 Agent 1: Research", 
                    "💡 Agent 2: Use Cases", 
                    "📚 Agent 3: Resources", 
                    "✨ Agent 4: Bonus", 
                    "📈 Executive Summary"
                ])
                
                with tab1:
                    st.subheader("🏢 Industry/Company Research Results")
                    research = results['research_data']
                    
                    # Metrics row
                    col1, col2, col3 = st.columns(3)
                    with col1:
                        st.metric("Industry Classification", research['industry'])
                    with col2:
                        st.metric("Focus Areas", len(research.get('focus_areas', [])))
                    with col3:
                        st.metric("Competitors Identified", len(research.get('competitors', [])))
                    
                    # Detailed analysis
                    col_a, col_b = st.columns(2)
                    with col_a:
                        st.markdown("**🎯 Company Offerings:**")
                        for offering in research.get('company_offerings', []):
                            st.write(f"• {offering}")
                        
                        st.markdown("**🔍 Strategic Focus Areas:**")
                        for area in research.get('focus_areas', []):
                            st.write(f"• {area}")
                    
                    with col_b:
                        st.markdown("**🏆 Key Competitors:**")
                        for comp in research.get('competitors', []):
                            st.write(f"• {comp}")
                        
                        st.markdown("**📈 Market Trends:**")
                        for trend in research.get('market_trends', []):
                            st.write(f"• {trend}")
                    
                    st.info(f"**Market Size:** {research.get('market_size', 'Analysis available')}")
                
                with tab2:
                    st.subheader("💡 AI/GenAI Use Case Proposals")
                    
                    # Use case metrics
                    col1, col2, col3 = st.columns(3)
                    with col1:
                        st.metric("Total Use Cases", len(results['use_cases']))
                    with col2:
                        ai_cases = len([uc for uc in results['use_cases'] if 'AI' in uc['name'] or 'ML' in uc['name']])
                        st.metric("AI/ML Cases", ai_cases)
                    with col3:
                        genai_cases = len([uc for uc in results['use_cases'] if 'GenAI' in uc['name'] or 'Content' in uc['name'] or 'Assistant' in uc['name']])
                        st.metric("GenAI Cases", genai_cases)
                    
                    # Use cases with enhanced display
                    for i, use_case in enumerate(results['use_cases'], 1):
                        with st.expander(f"🚀 {i}. {use_case['name']}", expanded=i<=2):
                            col1, col2 = st.columns([2, 1])
                            with col1:
                                st.write(f"**📝 Description:** {use_case['description']}")
                                st.write(f"**💰 Business Value:** {use_case['value']}")
                            with col2:
                                # Resource count for this use case
                                resource_count = len(results['resources'].get(use_case['name'], []))
                                st.metric("Resources Found", resource_count)
                                st.write("**🏷️ Category:** AI/GenAI")
                
                with tab3:
                    st.subheader("📚 Datasets & Resource Assets")
                    
                    # Resource metrics
                    total_resources = sum(len(r) for r in results['resources'].values())
                    kaggle_count = sum(1 for resources in results['resources'].values() for r in resources if 'Kaggle' in r['type'])
                    github_count = sum(1 for resources in results['resources'].values() for r in resources if 'GitHub' in r['type'])
                    hf_count = sum(1 for resources in results['resources'].values() for r in resources if 'HuggingFace' in r['type'])
                    
                    col1, col2, col3, col4 = st.columns(4)
                    with col1:
                        st.metric("Total Resources", total_resources)
                    with col2:
                        st.metric("📊 Kaggle Datasets", kaggle_count)
                    with col3:
                        st.metric("🐙 GitHub Repos", github_count)
                    with col4:
                        st.metric("🤗 HF Models", hf_count)
                    
                    # Resources by use case
                    for use_case_name, resources in results['resources'].items():
                        if resources:
                            with st.expander(f"📦 Resources for {use_case_name}", expanded=False):
                                for resource in resources:
                                    col1, col2 = st.columns([3, 1])
                                    with col1:
                                        st.markdown(f"**[{resource['name']}]({resource['url']})**")
                                        st.caption(resource.get('description', 'No description available'))
                                    with col2:
                                        if resource['type'] == 'Kaggle Dataset':
                                            st.markdown(":orange[📊 Kaggle]")
                                        elif resource['type'] == 'GitHub Repository':
                                            st.markdown(":blue[🐙 GitHub]")
                                        elif resource['type'] == 'HuggingFace Model':
                                            st.markdown(":green[🤗 HuggingFace]")
                                        else:
                                            st.markdown(f":gray[{resource['type']}]")
                
                with tab4:
                    st.subheader("✨ Bonus GenAI Solutions")
                    
                    if 'bonus_solutions' in results and results['bonus_solutions']:
                        bonus = results['bonus_solutions']
                        
                        # Bonus metrics
                        internal_count = len(bonus.get('internal_solutions', []))
                        customer_count = len(bonus.get('customer_solutions', []))
                        
                        col1, col2, col3 = st.columns(3)
                        with col1:
                            st.metric("Internal Solutions", internal_count)
                        with col2:
                            st.metric("Customer Solutions", customer_count)
                        with col3:
                            st.metric("Implementation Phases", len(bonus.get('implementation_roadmap', [])))
                        
                        # Internal solutions
                        st.markdown("### 🏢 Internal-Facing Solutions")
                        for solution in bonus.get('internal_solutions', []):
                            with st.expander(f"🔧 {solution['name']}", expanded=False):
                                st.write(f"**Description:** {solution['description']}")
                                st.write(f"**Business Value:** {solution['value']}")
                                st.write(f"**Implementation:** {solution['implementation']}")
                        
                        # Customer solutions
                        st.markdown("### 👥 Customer-Facing Solutions")
                        for solution in bonus.get('customer_solutions', []):
                            with st.expander(f"🎯 {solution['name']}", expanded=False):
                                st.write(f"**Description:** {solution['description']}")
                                st.write(f"**Business Value:** {solution['value']}")
                                st.write(f"**Implementation:** {solution['implementation']}")
                        
                        # ROI estimates
                        if 'roi_estimates' in bonus:
                            st.markdown("### 💰 ROI Estimates")
                            roi = bonus['roi_estimates']
                            col1, col2 = st.columns(2)
                            with col1:
                                st.info(f"**Cost Savings:** {roi.get('cost_savings', 'TBD')}")
                                st.info(f"**Revenue Impact:** {roi.get('revenue_impact', 'TBD')}")
                            with col2:
                                st.info(f"**Efficiency Gains:** {roi.get('efficiency_gains', 'TBD')}")
                                st.info(f"**Payback Period:** {roi.get('payback_period', 'TBD')}")
                    else:
                        st.info("Bonus solutions not available in this analysis")
                
                with tab5:
                    st.subheader("📈 Executive Summary & Downloads")
                    
                    # Summary metrics
                    col1, col2, col3, col4 = st.columns(4)
                    with col1:
                        st.metric("Industry", results['research_data']['industry'])
                    with col2:
                        st.metric("Use Cases", len(results['use_cases']))
                    with col3:
                        st.metric("Resources", sum(len(r) for r in results['resources'].values()))
                    with col4:
                        bonus_count = 0
                        if 'bonus_solutions' in results:
                            bonus_count = len(results['bonus_solutions'].get('internal_solutions', [])) + len(results['bonus_solutions'].get('customer_solutions', []))
                        st.metric("Bonus Solutions", bonus_count)
                    
                    # Key insights
                    st.markdown("### 🎯 Key Insights")
                    insights_col1, insights_col2 = st.columns(2)
                    with insights_col1:
                        st.success("✅ **Industry Analysis Complete**")
                        st.success("✅ **Use Cases Identified**")
                        st.success("✅ **Resources Mapped**")
                    with insights_col2:
                        st.success("✅ **Bonus Solutions Generated**")
                        st.success("✅ **Implementation Roadmap**")
                        st.success("✅ **ROI Estimates Provided**")
                    
                    # Download section
                    st.markdown("### 📥 Download Reports")
                    col_dl1, col_dl2, col_dl3 = st.columns(3)
                    
                    with col_dl1:
                        st.download_button(
                            "📄 Download Markdown Report",
                            data=results['report'],
                            file_name=f"{query.replace(' ', '_')}_research.md",
                            mime="text/markdown",
                            use_container_width=True
                        )
                    
                    with col_dl2:
                        try:
                            if results['files']['pdf'] and os.path.exists(results['files']['pdf']):
                                with open(results['files']['pdf'], 'rb') as f:
                                    st.download_button(
                                        "📄 Download PDF Report", 
                                        data=f.read(),
                                        file_name=f"{query.replace(' ', '_')}_research.pdf",
                                        mime="application/pdf",
                                        use_container_width=True
                                    )
                            else:
                                st.info("PDF generation requires reportlab")
                        except Exception as e:
                            st.warning(f"PDF not available: {str(e)}")
                    
                    with col_dl3:
                        # Create summary JSON for download
                        summary_data = {
                            "query": query,
                            "industry": results['research_data']['industry'],
                            "use_cases_count": len(results['use_cases']),
                            "resources_count": sum(len(r) for r in results['resources'].values()),
                            "bonus_solutions_count": bonus_count
                        }
                        st.download_button(
                            "📊 Download Summary JSON",
                            data=json.dumps(summary_data, indent=2),
                            file_name=f"{query.replace(' ', '_')}_summary.json",
                            mime="application/json",
                            use_container_width=True
                        )
            else:
                st.error("Please enter a company name or industry")
    
    with col2:
        st.markdown("### 📋 Quick Start Examples")
        
        # Enhanced examples with descriptions
        examples = {
            "Tesla Motors": "🚗 Electric vehicle & energy company",
            "Retail Industry": "🛒 E-commerce & traditional retail", 
            "Healthcare Industry": "🏥 Medical services & health tech",
            "Financial Services": "💰 Banking & fintech solutions",
            "Manufacturing Industry": "🏭 Industrial & production systems",
            "Education Industry": "🎓 EdTech & learning platforms",
            "Agriculture Industry": "🌾 AgTech & farming solutions"
        }
        
        st.markdown("""
        <style>
        .example-grid {
            display: grid;
            gap: 0.8rem;
            margin-top: 1rem;
        }
        </style>
        """, unsafe_allow_html=True)
        
        for example, description in examples.items():
            if st.button(f"🎯 {example}", key=f"ex_{example}", use_container_width=True, help=f"Analyze {example}"):
                st.session_state.query = example
                st.rerun()
            st.markdown(f"<small style='color: #7f8c8d; margin-bottom: 1rem; display: block;'>{description}</small>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
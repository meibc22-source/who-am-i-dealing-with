#!/usr/bin/env python3
"""
Gradio Web Interface for "Who Am I Dealing With"
This creates a beautiful web interface for the personality analyzer.
"""

import gradio as gr
import asyncio
import json
from personality_analyzer import analyze_contact_personality

def create_demo_interface():
    """Create the main web interface"""
    
    def analyze_contact_wrapper(name, company, linkedin_url, email, context):
        """Wrapper function to run our async analyzer"""
        if not name.strip():
            return "❌ Please enter a contact name."
        
        try:
            # Run the async function
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            result = loop.run_until_complete(
                analyze_contact_personality(name, company, email, linkedin_url, context)
            )
            loop.close()
            
            if "error" in result:
                return f"❌ Error: {result['error']}"
            
            return format_analysis_output(result)
            
        except Exception as e:
            return f"❌ Unexpected error: {str(e)}"
    
    def format_analysis_output(result):
        """Format the analysis result for display"""
        contact_info = result.get('contact_info', {})
        personality = result.get('personality_profile', {})
        strategy = result.get('communication_strategy', {})
        
        output = f"""
# 👤 Contact Analysis: {contact_info.get('name', 'Unknown')}

## 📋 Basic Information
- **Company:** {contact_info.get('company', 'Unknown')}
- **Title:** {contact_info.get('title', 'Unknown')}
- **Location:** {contact_info.get('location', 'Unknown')}
- **Confidence Score:** {result.get('confidence_score', 0):.1%}

## 🧠 Personality Profile

### Communication Style
{personality.get('communication_style', 'Not available')}

### Decision Making Approach
{personality.get('decision_making', 'Not available')}

### Key Personality Traits
{format_list(personality.get('personality_traits', []))}

### Professional Motivations
{format_list(personality.get('motivations', []))}

## 💬 Communication Strategy

### Recommended Approach
{strategy.get('approach', 'Not available')}

### Optimal Timing
{strategy.get('timing', 'Standard business timing')}

### Preferred Channel
{strategy.get('channel', 'Professional email')}

### Tone Guidance
{strategy.get('tone', 'Professional and respectful')}

## 🎯 Interests & Topics
{format_list(result.get('interests', []))}

## 💼 Skills & Expertise
{format_list(result.get('skills', []))}

## ✅ Do's
{format_list(strategy.get('dos', []))}

## ❌ Don'ts
{format_list(strategy.get('donts', []))}

---
📊 **Data Sources:** {', '.join(result.get('data_sources', ['Demo Data']))}  
⏰ **Analysis Time:** {result.get('analysis_timestamp', 'Unknown')}
        """
        
        return output.strip()
    
    def format_list(items):
        """Format a list of items as markdown bullets"""
        if not items:
            return "- None identified"
        return "\n".join([f"- {item}" for item in items])
    
    # Create the main interface
    with gr.Blocks(
        title="Who Am I Dealing With - Demo",
        theme=gr.themes.Soft()
    ) as demo:
        
        # Header
        gr.Markdown("""
        # 🔍 Who Am I Dealing With - MCP Server Demo
        
        **An intelligent personality analysis tool for better communication and networking.**
        
        This demo showcases how our system analyzes contacts to provide:
        - 🧠 **Personality insights** from available data
        - 💬 **Communication strategies** tailored to individual styles  
        - 🎯 **Interest identification** for better connections
        - 📊 **Professional context** for effective outreach
        
        ---
        """)
        
        # Main interface
        with gr.Row():
            with gr.Column(scale=1):
                gr.Markdown("### 📝 Contact Information")
                
                name_input = gr.Textbox(
                    label="Full Name *",
                    placeholder="John Doe",
                    info="Required field"
                )
                
                company_input = gr.Textbox(
                    label="Company",
                    placeholder="Acme Corporation"
                )
                
                linkedin_input = gr.Textbox(
                    label="LinkedIn URL",
                    placeholder="https://linkedin.com/in/johndoe",
                    info="Optional but improves accuracy"
                )
                
                email_input = gr.Textbox(
                    label="Email Address",
                    placeholder="john@example.com"
                )
                
                context_input = gr.Textbox(
                    label="Additional Context",
                    placeholder="Any additional information about this person...",
                    lines=3,
                    info="Optional background information"
                )
                
                analyze_btn = gr.Button(
                    "🔍 Analyze Contact",
                    variant="primary",
                    size="lg"
                )
            
            with gr.Column(scale=2):
                gr.Markdown("### 📊 Analysis Results")
                analysis_output = gr.Markdown(
                    value="Enter contact information and click 'Analyze Contact' to see results.",
                )
        
        # Example inputs
        gr.Markdown("### 💡 Try These Examples")
        examples = gr.Examples(
            examples=[
                [
                    "Satya Nadella",
                    "Microsoft",
                    "",
                    "",
                    "CEO of Microsoft, known for cloud computing and AI focus"
                ],
                [
                    "Reid Hoffman",
                    "Greylock Partners",
                    "https://www.linkedin.com/in/reidhoffman/",
                    "",
                    "Co-founder of LinkedIn, venture capitalist"
                ],
                [
                    "Jane Smith",
                    "TechCorp",
                    "",
                    "jane@techcorp.com",
                    "VP of Engineering, leads AI initiatives"
                ]
            ],
            inputs=[name_input, company_input, linkedin_input, email_input, context_input],
            label="Click any example to populate the form"
        )
        
        # Footer
        gr.Markdown("""
        ---
        
        ## 🔧 About This Demo
        
        This demonstration shows our **"Who Am I Dealing With"** system in action:
        
        ### 🏗️ How It Works
        1. **Input Analysis** - Takes contact information you provide
        2. **Data Enhancement** - Enriches with professional context and insights
        3. **AI Analysis** - Uses personality analysis to understand communication style
        4. **Strategy Generation** - Provides tailored advice for effective interaction
        
        ### 🎯 Use Cases
        - **Sales Outreach** - Understand prospects before reaching out
        - **Networking Events** - Prepare for conversations with attendees
        - **Partnership Meetings** - Research stakeholders and decision makers
        - **Interview Preparation** - Understand interviewers and candidates
        
        ### 🚀 Hackathon Submission
        This project is submitted to the **Hugging Face MCP Hackathon 2025** in Track 1: MCP Server Implementation.
        
        **Tags:** `mcp-server-track` `personality-analysis` `communication-strategy` `networking`
        """)
        
        # Connect the button to the function
        analyze_btn.click(
            fn=analyze_contact_wrapper,
            inputs=[name_input, company_input, linkedin_input, email_input, context_input],
            outputs=analysis_output
        )
    
    return demo

if __name__ == "__main__":
    print("🚀 Starting 'Who Am I Dealing With' Demo Interface")
    print("=" * 50)
    
    demo = create_demo_interface()
    
    # Launch the demo
    demo.launch(
        share=True,
        server_port=7860,
        show_error=True
    )
    
    print("Demo is running! Open the provided URL to access the interface.")
    print("Press Ctrl+C to stop the server.")
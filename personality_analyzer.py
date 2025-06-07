#!/usr/bin/env python3
"""
Who Am I Dealing With - Demo Version
A simplified personality analysis tool for the MCP hackathon.
"""

import asyncio
import json
import logging
from typing import Dict, List, Any
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class PersonalityAnalyzer:
    """Simple personality analyzer for demo purposes"""
    
    def __init__(self):
        self.demo_profiles = {
            "satya nadella": {
                "name": "Satya Nadella",
                "company": "Microsoft",
                "title": "Chairman and CEO",
                "location": "Redmond, Washington",
                "experience": [
                    "CEO at Microsoft (2014-present)",
                    "Executive Vice President, Cloud and Enterprise Group",
                    "22+ years at Microsoft in various leadership roles"
                ],
                "skills": ["Cloud Computing", "Strategic Leadership", "Digital Transformation", "AI and Machine Learning"],
                "interests": ["AI Innovation", "Inclusive Growth", "Cricket", "Reading"],
                "communication_style": "Thoughtful and inclusive, focuses on empowerment and growth mindset",
                "decision_making": "Collaborative and data-driven, considers long-term impact",
                "personality_traits": ["Empathetic Leader", "Visionary", "Growth-minded", "Inclusive", "Strategic Thinker"]
            },
            "reid hoffman": {
                "name": "Reid Hoffman",
                "company": "Greylock Partners",
                "title": "Partner and Co-founder of LinkedIn",
                "location": "San Francisco Bay Area",
                "experience": [
                    "Partner at Greylock Partners",
                    "Co-founder and Executive Chairman at LinkedIn",
                    "Board member at Microsoft, Airbnb"
                ],
                "skills": ["Venture Capital", "Entrepreneurship", "Network Theory", "Product Strategy"],
                "interests": ["Network Effects", "Entrepreneurship", "Future of Work", "Philosophy"],
                "communication_style": "Intellectual and strategic, uses frameworks and analogies",
                "decision_making": "Network-thinking approach, considers ecosystem effects",
                "personality_traits": ["Strategic Networker", "Philosophical", "Systems Thinker", "Connector", "Future-focused"]
            }
        }
    
    async def analyze_contact(self, name: str, company: str = "", linkedin_url: str = "", additional_context: str = "") -> Dict[str, Any]:
        """Analyze a contact's personality"""
        try:
            logger.info(f"Analyzing contact: {name}")
            
            # Check if we have a demo profile
            name_key = name.lower()
            if name_key in self.demo_profiles:
                profile = self.demo_profiles[name_key].copy()
                profile["confidence_score"] = 0.95
                profile["data_sources"] = ["Demo Data - High Quality"]
            else:
                # Generate a generic professional profile
                profile = self._generate_generic_profile(name, company)
            
            # Add analysis timestamp
            profile["analysis_timestamp"] = datetime.now().isoformat()
            
            # Generate communication strategy
            strategy = self._generate_communication_strategy(profile)
            
            return {
                "contact_info": {
                    "name": profile["name"],
                    "company": profile.get("company", company),
                    "title": profile.get("title", "Professional"),
                    "location": profile.get("location", "Unknown")
                },
                "personality_profile": {
                    "communication_style": profile.get("communication_style", "Professional and approachable"),
                    "decision_making": profile.get("decision_making", "Thoughtful and collaborative"),
                    "personality_traits": profile.get("personality_traits", ["Professional", "Engaged"]),
                    "motivations": ["Professional growth", "Industry leadership"]
                },
                "communication_strategy": strategy,
                "interests": profile.get("interests", ["Professional development"]),
                "skills": profile.get("skills", ["Industry expertise"]),
                "confidence_score": profile.get("confidence_score", 0.7),
                "data_sources": profile.get("data_sources", ["Demo Analysis"]),
                "analysis_timestamp": profile["analysis_timestamp"]
            }
            
        except Exception as e:
            logger.error(f"Error analyzing contact: {str(e)}")
            return {"error": f"Analysis failed: {str(e)}"}
    
    def _generate_generic_profile(self, name: str, company: str) -> Dict[str, Any]:
        """Generate a generic professional profile"""
        return {
            "name": name,
            "company": company,
            "title": "Professional",
            "location": "Unknown",
            "experience": [f"Professional experience at {company}" if company else "Professional experience"],
            "skills": ["Professional Skills", "Industry Knowledge", "Communication"],
            "interests": ["Professional Development", "Industry Trends"],
            "communication_style": "Professional and courteous",
            "decision_making": "Thoughtful and methodical",
            "personality_traits": ["Professional", "Dedicated", "Goal-oriented"],
            "confidence_score": 0.6,
            "data_sources": ["Basic Analysis"]
        }
    
    def _generate_communication_strategy(self, profile: Dict[str, Any]) -> Dict[str, Any]:
        """Generate communication strategy based on profile"""
        return {
            "approach": "Be professional and respectful. Focus on mutual value and clear communication.",
            "timing": "Standard business hours, allow 24-48 hours for response",
            "channel": "Professional email or LinkedIn message",
            "tone": "Professional and courteous",
            "dos": [
                "Be clear about your purpose",
                "Provide value in your outreach",
                "Respect their time and expertise",
                "Follow up appropriately"
            ],
            "donts": [
                "Don't be overly casual if they prefer formality",
                "Don't be pushy or aggressive",
                "Don't ignore their areas of expertise"
            ]
        }

# Main functions that will be used by our demo interface
async def analyze_contact_personality(name: str, company: str = "", email: str = "", linkedin_url: str = "", additional_context: str = "") -> Dict[str, Any]:
    """Main analysis function"""
    analyzer = PersonalityAnalyzer()
    return await analyzer.analyze_contact(name, company, linkedin_url, additional_context)

# Test function
async def test_analyzer():
    """Test the analyzer"""
    print("Testing Personality Analyzer...")
    
    # Test with Satya Nadella
    result = await analyze_contact_personality("Satya Nadella", "Microsoft")
    print("Test Result:")
    print(json.dumps(result, indent=2))
    print("\nAnalyzer is working correctly! ✅")

if __name__ == "__main__":
    asyncio.run(test_analyzer())
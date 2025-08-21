"""
Simple Agent Example - Basic implementation showing core Agent Ops concepts.

This example demonstrates:
- Tool integration
- Basic error handling  
- Logging and monitoring
- Configuration management
"""

import logging
import json
from typing import Dict, Any, List
from dataclasses import dataclass
import uuid

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@dataclass
class AgentConfig:
    """Agent configuration with validation."""
    model: str = "gpt-3.5-turbo"
    temperature: float = 0.7
    max_tokens: int = 1000
    tools: List[str] = None
    
    def __post_init__(self):
        if self.tools is None:
            self.tools = ["search", "calculator"]

class Tool:
    """Base tool interface."""
    
    def __init__(self, name: str):
        self.name = name
        
    def execute(self, *args, **kwargs) -> str:
        raise NotImplementedError

class SearchTool(Tool):
    """Mock search tool for demonstration."""
    
    def __init__(self):
        super().__init__("search")
        
    def execute(self, query: str) -> str:
        """Simulate search operation."""
        logger.info(f"Searching for: {query}")
        
        # Mock search results
        results = [
            "Agent systems require careful monitoring and evaluation.",
            "Production deployments need robust error handling.",
            "Tool integration is a key component of agent architecture."
        ]
        
        return f"Search results for '{query}':\n" + "\n".join(f"- {r}" for r in results)

class CalculatorTool(Tool):
    """Simple calculator tool."""
    
    def __init__(self):
        super().__init__("calculator")
        
    def execute(self, expression: str) -> str:
        """Safely evaluate mathematical expressions."""
        try:
            # Basic safety - only allow numbers and basic operators
            allowed_chars = set('0123456789+-*/().')
            if not all(c in allowed_chars or c.isspace() for c in expression):
                return "Error: Invalid characters in expression"
                
            result = eval(expression)
            logger.info(f"Calculated: {expression} = {result}")
            return f"Result: {result}"
            
        except Exception as e:
            logger.error(f"Calculator error: {e}")
            return f"Error: Could not calculate '{expression}'"

class SimpleAgent:
    """Basic agent implementation with tool integration."""
    
    def __init__(self, config: AgentConfig = None):
        self.config = config or AgentConfig()
        self.session_id = str(uuid.uuid4())
        self.tools = self._initialize_tools()
        
        logger.info(f"Agent initialized with session {self.session_id}")
        
    def _initialize_tools(self) -> Dict[str, Tool]:
        """Initialize available tools."""
        available_tools = {
            "search": SearchTool(),
            "calculator": CalculatorTool()
        }
        
        return {name: available_tools[name] for name in self.config.tools if name in available_tools}
    
    def process_query(self, query: str) -> Dict[str, Any]:
        """Process user query and return response."""
        logger.info(f"Processing query: {query}")
        
        try:
            # Simple query routing logic
            response = self._route_query(query)
            
            result = {
                "session_id": self.session_id,
                "query": query,
                "response": response,
                "status": "success"
            }
            
            logger.info("Query processed successfully")
            return result
            
        except Exception as e:
            logger.error(f"Error processing query: {e}")
            return {
                "session_id": self.session_id,
                "query": query,
                "response": "I apologize, but I encountered an error processing your request.",
                "status": "error",
                "error": str(e)
            }
    
    def _route_query(self, query: str) -> str:
        """Route query to appropriate tool or provide direct response."""
        query_lower = query.lower()
        
        # Calculator routing
        if any(op in query for op in ['+', '-', '*', '/', 'calculate', 'math']):
            # Extract mathematical expression
            if 'calculate' in query_lower:
                expression = query.split('calculate')[-1].strip()
            else:
                expression = query.strip()
                
            if 'calculator' in self.tools:
                return self.tools['calculator'].execute(expression)
        
        # Search routing  
        if any(keyword in query_lower for keyword in ['search', 'find', 'what is', 'tell me about']):
            if 'search' in self.tools:
                return self.tools['search'].execute(query)
        
        # Default response
        return f"I understand you're asking: '{query}'. I have access to these tools: {list(self.tools.keys())}. Try asking me to search for something or calculate a math expression!"

def main():
    """Example usage of the SimpleAgent."""
    
    # Initialize agent with custom configuration
    config = AgentConfig(
        model="gpt-3.5-turbo",
        temperature=0.5,
        tools=["search", "calculator"]
    )
    
    agent = SimpleAgent(config)
    
    # Example queries
    test_queries = [
        "What is agent ops?",
        "Calculate 15 * 7 + 3",
        "Search for information about MLflow",
        "Tell me about deployment pipelines"
    ]
    
    print("🤖 Simple Agent Demo")
    print("=" * 50)
    
    for query in test_queries:
        print(f"\n👤 User: {query}")
        result = agent.process_query(query)
        print(f"🤖 Agent: {result['response']}")
        
        if result['status'] == 'error':
            print(f"❌ Error: {result.get('error', 'Unknown error')}")

if __name__ == "__main__":
    main()
# Examples

This directory contains complete, working examples that demonstrate the concepts covered in the book.

## Available Examples

### 🤖 Simple Agent (`simple-agent/`)
A basic agent implementation showing:
- Tool integration (search, calculator)
- Error handling and logging
- Configuration management
- Session tracking

**Run it:**
```bash
cd examples/simple-agent
python agent.py
```

### 🔄 Multi-Agent System (`multi-agent/`) - Coming Soon
Demonstrates:
- Agent coordination
- Shared memory
- Task delegation
- Communication patterns

### 📊 Agent Evaluation (`evaluation/`) - Coming Soon  
Shows how to:
- Create evaluation datasets
- Implement automated testing
- Measure agent performance
- Track quality metrics

### 🚀 Production Deployment (`deployment/`) - Coming Soon
Complete example of:
- Docker containerization
- API endpoints
- Health checks
- Monitoring setup

## Running Examples

Each example is self-contained and includes:
- **README.md** - Specific setup instructions
- **requirements.txt** - Dependencies (if different from main)
- **Working code** - Complete implementations you can run

### Prerequisites
Make sure you have the main book dependencies installed:
```bash
pip install -r ../requirements.txt
```

### General Pattern
```bash
cd examples/<example-name>
python main.py  # or see specific README
```

## Contributing Examples

When adding new examples:

1. **Create directory** with descriptive name
2. **Include README.md** with setup instructions  
3. **Add to this index** with brief description
4. **Test thoroughly** - examples must work out of the box
5. **Follow book concepts** - demonstrate specific Agent Ops principles

### Example Structure
```
examples/
├── your-example/
│   ├── README.md          # Setup and usage
│   ├── main.py           # Entry point
│   ├── requirements.txt  # If different from main
│   └── config/           # Configuration files
```

## Integration with Book

Examples are referenced throughout the book chapters. When working on a chapter:

1. **Run the relevant example** to see concepts in action
2. **Modify examples** to experiment with different approaches  
3. **Reference specific files** using `examples/path/to/file.py` syntax

This hands-on approach reinforces the theoretical concepts with practical implementations.
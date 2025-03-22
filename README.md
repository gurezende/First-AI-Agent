## Code Walkthrough: Product Research Crew with CrewAI

![](img/Gemini_agent1.jpeg)

This code snippet demonstrates how to use the CrewAI framework to create a multi-agent system that researches and compares different brands of a product. Let's break down the code section by section:

**1. Importing Modules:**

* `crewai`: This is the core module for creating and managing agents, tasks, and crews.
* `Task`, `Agent`, `Crew`, `Process`, `LLM`: These are specific classes from `crewai` used for defining individual components of the agent system.
* `crewai_tools.SerperDevTool`: This module provides a tool for the agent to perform web searches using the SerperDev API.
* `os`: This module is used to access environment variables, which are used to store API keys.

**2. Defining the Language Model (LLM):**

* This section initializes the Language Model (LLM) that the agents will use for processing and generating text.
* It sets the model to "groq/qwen-qwq-32b", and retrieves the API key from the environment variable `GROQ_API_KEY`. It also sets the temperature to 0.7, which controls the randomness of the model's output.
* The commented out section shows the configuration for using the OpenAI api and gpt-4 model. You can switch between these models by commenting/uncommenting the relevant section.

**3. Agent Definition:**

* This section defines an agent named `researcher`.
* `role`: Defines the role of the agent, which is a "{topic} Products Researcher". The topic variable will be replaced at runtime.
* `goal`: Specifies the agent's objective, which is to compare the performance of different brands of the given topic based on review articles and news.
* `backstory`: Provides context for the agent's role, stating that it is a product researcher that compares different brands.
* `tools`: Assigns the `SerperDevTool` to the agent, allowing it to perform web searches.
* `llm`: Assigns the defined LLM to the agent, so that it can process and generate text.

**4. Define the Research Task:**

* This section defines a task named `product_research_task`.
* `description`: Specifies the task's objective, which is to research the best brands of the given topic and compare their price average, ratings, and performance.
* `expected_output`: Describes the desired output format, which is a table comparing the brands and a recommendation for the best brand, based on a maximum of two searches on Amazon and Google US.
* `agent`: Assigns the `researcher` agent to this task.

**5. Launch the Product Researcher (main function):**

* This function, `main(topic)`, orchestrates the agent and task.
* `Crew`: Creates a crew consisting of the `researcher` agent and the `product_research_task`.
* `process`: Sets the process to `Process.sequential`, meaning the tasks will be executed in the order they are defined.
* `verbose`: Enables verbose output, which will print detailed information about the crew's execution.
* `crew.kickoff(inputs={'topic': topic})`: Starts the crew's execution, passing the `topic` as input.
* `print(result)`: Prints the final result of the crew's execution.

**6. Execution:**

* The `if __name__ == "__main__":` block ensures that the `main` function is executed only when the script is run directly.
* `main(topic="Laptop PC")`: Calls the `main` function with the topic "Laptop PC", triggering the agent to research and compare laptop brands.

**How to Run:**

1.  **Install the required libraries:**
    ```bash
    pip install crewai crewai-tools groq
    ```
2.  **Set up API keys:**
    * Obtain an API key for Groq and/or OpenAI.
    * Set the API keys as environment variables:
        * For Groq: `export GROQ_API_KEY=your_groq_api_key`
        * For OpenAI: `export OPENAI_API_KEY=your_openai_api_key`
3.  **Run the script:**
    ```bash
    python main.py
    ```
4.  **Observe the output:** The script will print the results of the agent's research, including a table comparing laptop brands and a recommendation.

**Customization:**

* You can change the `topic` variable to research different products.
* You can modify the agent's `role`, `goal`, and `backstory` to customize its behavior.
* You can add more agents and tasks to create more complex workflows.
* You can change the LLM model used.
* You can add more tools to the agent.



## Result

| **Brand**       | **Average Price** | **Performance Score (Scale 1-10)** | **Overall Rating (Out of 10)** |
|-----------------|-------------------|------------------------------------|-------------------------------|
| **Apple**       | $1,299            | 8.5                                | 9.0                         |
| **ASUS**        | $999              | 8.0                                | 8.5                         |
| **Lenovo**      | $1,099            | 7.8                                | 8.2                         |

### Recommendation:
**Best Brand: Apple (MacBook Series)**
- **Why Apple?**
  - **Performance**: MacBook Air M4 and Pro 16 (M3 Max) dominate in benchmarks, offering superior multitasking, long battery life (up to 20 hours), and Apple’s ecosystem integration.
  - **Ratings**: Consistently ranked #1 for build quality, durability, and user satisfaction (Laptop Mag, Rtings).
  - **Drawback**: Higher average price due to premium components.

**Honorable Mentions**:
- **ASUS ZenBook Series**: Combines affordability with OLED displays and strong processors (e.g., ZenBook 14 OLED).
- **Lenovo ThinkPad**: Trusted for business users with excellent keyboards and upgradability.

**Final Verdict**: Apple leads in performance and reliability, but ASUS offers a strong value proposition for most users.

---
**Sources**: Laptop Mag, Rtings, TechRadar, and Amazon/Google price tracking (2023–2025).**

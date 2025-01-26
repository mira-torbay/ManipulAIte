
# ManipulAlte



**ManipulAlte** is an AI-driven solution which could detect and analyze bias, misinformation, and propaganda in content(s) provided by the user. Through pre-trained Hugging Face models and our own bias-classifying model that we have trained using a JSON data, ManipuAlte is able to analyze text and find patterns that correlate to ulterior motives behind it. Our goal is to equip users with tools to help differentiate between objective truth and false narratives throughout various forms of content.

## Tech Stack 

### Programming Language 
- HTML
- CSS
- Javascript
- Python
  
### Librarires and Frameworks
- Transformers
- PyTorch
- Flask

## Bias Detenction AI Training 
Data based used to train bias detection ai :https://huggingface.co/datasets/shainar/BEAD
- article = {raza2024beads},
- title={BEADs: Bias Evaluation Across Domains},
- author={Raza, Shaina and Rahman, Mizanur and Zhang, Michael R},
- journal={arXiv preprint arXiv:2406.04220},
- year={2024}

The verision used was trained using a random samples of 500 data points 


## Future Plans
- **Contextual Analysis**: Incorporate background context to content that user provides so that our AI has a higher accurarcy in distinguishing between objectively truth and biased or misleading information. This will increase AI's accurarcy and make it more relevant for real-world scenarios.
- **Database Expansion**: Expand our model's database to expose our AI to more diverse bias, misinformation, and propaganda techniques.
- **Feedback Loop**: Have users be able to validate AI's analysis on a content in order to continously improve the model's performance


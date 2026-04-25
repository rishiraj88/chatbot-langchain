from openai import OpenAI

client = OpenAI()

response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {
      "role": "system",
      "content": "Provided a block of text, your task is to extract a list of keywords out of it."
    },
    {
      "role": "user",
      "content": "Generative AI (GenAI) refers to machine learning systems—often built on transformer architectures and large-scale self-supervised pretraining—that learn statistical patterns from massive datasets to produce novel content such as text, images, audio, and video; by modeling probability distributions over tokens, pixels, or waveforms these models can generate coherent continuations, translate styles, and synthesize realistic media, and their behavior is shaped by choices like temperature, top-k/top-p sampling, and prompt design while being further adapted via fine-tuning, few-shot techniques, or reinforcement learning from human feedback (RLHF); GenAI powers applications from automated drafting, ideation, and code generation to artistic exploration, design prototyping, and synthetic-data creation for machine learning pipelines, but it also raises technical and social challenges—hallucinations (confident but incorrect outputs), propagated biases from training data, copyright and licensing concerns, privacy risks mitigated by methods like differential privacy or federated learning, and significant compute and latency trade-offs that motivate compression techniques such as distillation, pruning, and quantization; multi-modal models that fuse vision, language, and audio expand capabilities but complicate evaluation, which still relies heavily on human judgment alongside metrics like BLEU, ROUGE, and FID; addressing risks requires layered approaches including content filtering, debiasing, explainability tools (attention visualization, feature attribution), model documentation (model cards), red teaming, and governance frameworks, while ongoing research focuses on improving factual reliability, uncertainty calibration, efficient on-device deployment, and aligning outputs with human values to unlock GenAI’s productivity gains responsibly."
    }
  ],
  temperature=0.5
)

print(response.choices[0].message.content)
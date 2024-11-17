# Sign Language Classification

## 🌟 Features:

- 🚀 Simple and intuitive web interface
- 🔄 Real-time text generation
- 🎯 Support for multiple Ollama models
- 🔌 Custom server URL configuration

## 📥 Installation:

### Install [uv](https://ollama.com/download) for linux:
```
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Clone the repository:
```
git clone https://github.com/ashuguptahere/sign-language-classification.git
cd sign-language-classification
```

### Download dataset from [kaggle](https://www.kaggle.com/grassknoted/asl-alphabet) using cURL and unzip it:
```
curl -L -o archive.zip https://www.kaggle.com/api/v1/datasets/download/grassknoted/asl-alphabet
unzip archive.zip
```

### Install all `uv` dependencies:
```
uv sync
```

### To split data:
```
uv run scripts/split.py
```

### To train a `sign-language-classification` model:
```
uv run scripts/train.py
```

## 🤝 Contributing:

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License:

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
Made with ❤️ by [Aashish Gupta](https://github.com/ashuguptahere)
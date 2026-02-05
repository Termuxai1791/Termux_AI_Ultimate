
#!/data/data/com.termux/files/usr/bin/bash

echo "🔧 Termux AI telepítés indul..."

pkg update -y
pkg upgrade -y

pkg install python git wget unzip -y

pip install --upgrade pip
pip install openai rich

echo "📂 AI parancs létrehozása..."

mkdir -p ~/bin

cat > ~/bin/ai <<EOF
#!/bin/bash
python ~/Termux_AI_Ultimate/ai_scripts/ai_full.py
EOF

chmod +x ~/bin/ai

echo 'export PATH=$PATH:~/bin' >> ~/.bashrc
source ~/.bashrc

echo ""
echo "✅ TELEPÍTÉS KÉSZ!"
echo "Indítás parancs: ai"
echo ""




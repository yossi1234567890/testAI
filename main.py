from tensorflow.keras.models import load_model

# Load the previously saved model
model = load_model('my_security_ai_v2.h5')

print("---セキュリティクイズ 第1問---")
question = "メールに[至急]とある場合、どうするべき?"
options = ("1: すぐにリンクをクリックする 2: 一度手を止めて、公式アプリから確認する")
correct_answer = "2"
count = 0;

print(f"\n問題:{question}")
for opt in options:
  print(opt)
#利用者の入力を受け付ける
choice = input("答えを選択してください")
if choice == correct_answer:
  print("正解! 冷静な判断が詐欺を防ぎます")
  count = count + 1;
else :
  print("不正解 すぐにリンクをクリックするとウィルスが入ったりする可能性があります")

print("---セキュリティクイズ 第2問---")
question = "URLにドット(.)が多い場合どんな危険が推測される？"
options = ("1: 公式ドメインを模倣した、深層の深いURLの可能性 2: セキュリティが非常に強固である")
correct_answer = "1"

print(f"\n問題:{question}")
for opt in options:
  print(opt)
#利用者の入力を受け付ける
choice = input("答えを選択してください")
if choice == correct_answer:
  print("正解! 冷静な判断が詐欺を防ぎます")
  count = count + 1;
else :
  print("不正解 すぐにリンクをクリックするとウィルスが入ったりする可能性があります")

print(f"現在の得点は:{count}です")

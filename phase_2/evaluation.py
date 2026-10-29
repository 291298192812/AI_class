import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path


data_dir = Path("data")
train_path = data_dir / "train.csv"
test_path = data_dir / "test.csv"

if not train_path.exists():
    cleaned_path = data_dir / "cleaned_data.csv"
    if cleaned_path.exists():
        df = pd.read_csv(cleaned_path)
        train_df = df.sample(frac=0.8, random_state=42)
        test_df = df.drop(train_df.index)
    else:
        raise FileNotFoundError("ابتدا باید src/data_loader.py اجرا شود.")
else:
    train_df = pd.read_csv(train_path)
    test_df = pd.read_csv(test_path)

all_df = pd.concat([train_df, test_df], ignore_index=True)

print("=" * 55)
print("📊 گزارش بخش داده و ارزیابی (تسک: ابراهیم یدالهی)")
print("=" * 55)


n_train = len(train_df)
n_test = len(test_df)
n_users = all_df["user_id"].nunique()
n_items = all_df["item_id"].nunique()
total_ratings = len(all_df)


total_possible = n_users * n_items
sparsity = (1.0 - (total_ratings / total_possible)) * 100

print(f"تعداد رکوردهای آموزش (Train): {n_train}")
print(f"تعداد رکوردهای آزمون (Test): {n_test}")
print(f"تعداد کاربران یکتا: {n_users}")
print(f"تعداد آیتم‌های یکتا: {n_items}")
print(f"نرخ عدم تراکم ماتریس (Sparsity Rate): {sparsity:.2f}%")


train_set = set(zip(train_df["user_id"], train_df["item_id"]))
test_set = set(zip(test_df["user_id"], test_df["item_id"]))
leakage = train_set.intersection(test_set)
print(f"تداخل داده‌ها بین آموزش و آزمون (Data Leakage): {len(leakage)} مورد")
assert len(leakage) == 0, "خطا: هم‌پوشانی نامعتبر بین Train و Test!"


print("\nتوزیع نوع آیتم‌ها:")
for itype, count in all_df["item_type"].value_counts().items():
    print(f" - {itype}: {count} تعامل")


counts = all_df["rating"].value_counts().sort_index()
plt.figure(figsize=(6, 4))
plt.bar(counts.index.astype(str), counts.values, color="#4f46e5", edgecolor="#1e1b4b")
plt.title("Rating Distribution (Evaluation)")
plt.xlabel("Rating (1-5)")
plt.ylabel("Count")
plt.grid(axis="y", linestyle="--", alpha=0.6)
plt.tight_layout()
plt.savefig(data_dir / "rating_evaluation.png", dpi=150)
print("\n✅ نمودار ارزیابی با موفقیت ذخیره شد.")
print("=" * 55)

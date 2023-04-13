import json
import random

def load_memos_from_json(json_file):
    with open(json_file, "r", encoding="utf-8") as f:
        memos = json.load(f)
    return memos

def select_memos(memos, target_length=3000):
    memos_by_tag = {}
    for memo in memos:
        for tag in memo["tags"]:
            if tag not in memos_by_tag:
                memos_by_tag[tag] = []
            memos_by_tag[tag].append(memo)

    selected_memos = []
    current_length = 0

    while current_length < target_length:
        tags = list(memos_by_tag.keys())
        random.shuffle(tags)

        for tag in tags:
            if memos_by_tag[tag]:
                memo = memos_by_tag[tag].pop()
                selected_memos.append(memo)
                current_length += len(memo["content"])

                if current_length >= target_length:
                    break

    return selected_memos, list(memos_by_tag.keys())

def memos_to_txt(memos, txt_file):
    with open(txt_file, "w", encoding="utf-8") as f:
        for memo in memos:
            tags = " ".join(f"#{tag}" for tag in memo["tags"])
            f.write(f"{memo['content']}\n{tags}\n\n")

if __name__ == "__main__":
    input_json = "data/flomo_history.json"  # 输入JSON文件名
    output_memos_txt = "data/selected_memos.txt"  # 输出TXT文件名
    output_tags_txt = 'data/tags.txt'


    memos = load_memos_from_json(input_json)
    selected_memos, tags = select_memos(memos)
    memos_to_txt(selected_memos, output_memos_txt)

    with open(output_tags_txt, "w", encoding="utf-8") as f:
        f.write("\n".join(tags))

    print(f"筛选完成。筛选后的memo已保存到 '{output_memos_txt}'。")
    print(f"筛选后的tag已保存到 '{output_tags_txt}'。")

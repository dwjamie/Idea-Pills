import re
import json

def parse_memo(memo):
    date_time_pattern = r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}"
    tag_pattern = r"#([\w/]+)"
    
    date_time = re.findall(date_time_pattern, memo)
    date_time = date_time[0] if len(date_time) > 0 else ""
    tags = re.findall(tag_pattern, memo)
    content = re.sub(date_time_pattern, "", memo).strip()
    content = re.sub(tag_pattern, "", content).strip()

    if content == "":
        return
    
    return {
        "date_time": date_time,
        "tags": tags,
        "content": content
    }

def process_txt_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        memos_raw = f.read().split("\n\n")
        
    memos = [parse_memo(memo) for memo in memos_raw if parse_memo(memo)]
    
    return memos

if __name__ == "__main__":
    file_name = "data/flomo_history.txt"  # 输入文件名
    output_file_name = "data/flomo_history.json"  # 输出文件名

    memos = process_txt_file(file_name)

    with open(output_file_name, "w", encoding='utf-8') as outfile:
        json.dump(memos, outfile, ensure_ascii=False, indent=4)

    print(f"处理完成。提取的memo已保存到 '{output_file_name}'。")

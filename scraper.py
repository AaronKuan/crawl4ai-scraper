import asyncio
from crawl4ai import AsyncWebCrawler

async def main():
    # 替換成您想抓取的目標網址
    target_url = "https://github.com/unclecode/crawl4ai"
    
    print(f"🚀 正在使用 Crawl4AI 抓取網頁: {target_url} ...")
    
    # 初始化爬蟲
    async with AsyncWebCrawler() as crawler:
        # 開始爬取並自動提取內容
        result = await crawler.arun(url=target_url)
        
        # 取得清洗過後的 Markdown 格式資料（專為 LLM 設計的友善格式）
        markdown_content = result.markdown
        
        # 將結果存入 Markdown 檔案
        with open("output.md", "w", encoding="utf-8") as f:
            f.write(markdown_content)
            
        print("✅ 網頁抓取完成，內容已成功儲存至 output.md！")

if __name__ == "__main__":
    asyncio.run(main())

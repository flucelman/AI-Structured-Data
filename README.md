# AI-Structured-Data
Call the api of the visual large model, ocr processing of the local file, by adjusting the prompt can let the large model output their own desired fixed format data. Simultaneous use of python asynchronous processing, you can process multiple files at the same time

It is convenient for AI training, embeding of blocks, formatting and so on

# Instructions 

This code invokes the Qwen-Long model, which supports the parsing and dialogue of various document formats such as Word, PDF, Markdown, EPUB, and MOBI. Additionally, it comes with a gift of 1 million koen. The output token of the Qwen-Long model is only 0.002 per 1k tokens. 

Qwen-Long is a large language model developed by Qwen for handling extremely long context scenarios. It supports input in various languages including Chinese and English, and can handle ultra-long context conversations with up to 10 million tokens (approximately 15 million characters or 15,000 pages of documents). When used in conjunction with the newly launched document service, it can parse and engage in conversations with multiple document formats such as Word, PDF, Markdown, EPUB, and MOBI. Note: Requests can be submitted directly via HTTP, supporting a length of up to 1 million tokens. For lengths exceeding this, it is recommended to submit via file. Address: [Alibaba Cloud Bailian](https://bailian.console.aliyun.com/#/model-market/detail/qwen-long?tabKey=sdk) 

Of course, you can also use other visual large models. Just follow the request format of OpenAI and modify the BASE_URL in the .env file. ---
# User Guide 

## I. Download this project: 

```
git clone https://github.com/flucelman/AI-Structured-Data.git
```


## II. According to Dependency 

```
pip install openai
```


## III. Configure API Key 

Please visit [Alibaba Cloud Bailian](https://bailian.console.aliyun.com/#/model-market/detail/qwen-long?tabKey=sdk) to obtain the API key, and modify the api-key parameter in the .env file with your own. 

## IV. Upload Documents 

Upload the file to the Alibaba BaiLian platform through the OpenAI compatible interface, save it to the platform's secure storage space, and then obtain the `file-id`. 

Before starting to upload the document, please place the file you need to convert in the /Files directory. 

After preparing the files, run: 

```
python uploadFiles.py
```


The console will prompt that the file has been uploaded. 

## V. Structuring Document Data 

```
python main.py
```


This will structure the file that was just uploaded. The format of the structured data is set by the prompt in main.py. 

If you need to modify the structured format, please modify the prompt in main.py. 

After some time, the structured data will be saved in the /bank folder. 

## VI. Deleting Documents 

If you want to delete the uploaded document, please run: 

```
python delete_all_files.py
```


## VII. Notes to Observe 

1. Before structuring the data of your document, make sure that your document has been uploaded to the Alibaba Cloud BaiLian platform. 

2. If you want to process a new document, please delete the previously uploaded document first; otherwise, the previously uploaded file will also be converted repeatedly.

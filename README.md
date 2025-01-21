# AI-Structured-Data
Call the api of the visual large model, ocr processing of the local file, by adjusting the prompt can let the large model output their own desired fixed format data. Simultaneous use of python asynchronous processing, you can process multiple files at the same time
---
# 说明

本代码调用Qwen-Long模型，可支持word、pdf、markdown、epub、mobi等多种文档格式的解析和对话。并且赠送100万koen，Qwen-Long模型的输出token仅为0.002/1k Token

Qwen-Long是在通义千问针对超长上下文处理场景的大语言模型，支持中文、英文等不同语言输入，支持最长1000万tokens(约1500万字或1.5万页文档)的超长上下文对话。配合同步上线的文档服务，可支持word、pdf、markdown、epub、mobi等多种文档格式的解析和对话。 说明：通过HTTP直接提交请求，支持1M tokens长度，超过此长度建议通过文件方式提交。地址：[阿里云百炼](https://bailian.console.aliyun.com/#/model-market/detail/qwen-long?tabKey=sdk)

当然，您也可以使用其他视觉类大模型，只需遵循OpenAI的请求格式。修改.env里面的BASE_UR即可
---
# 使用教程

## 一、下载本项目：

```
git clone https://github.com/flucelman/AI-Structured-Data.git
```

## 二、按照依赖

```
pip install openai
```

## 三、配置api-key

请访问 [阿里云百炼](https://bailian.console.aliyun.com/#/model-market/detail/qwen-long?tabKey=sdk) 获取api-key，修改.env里的api-key参数为你自己的

## 四、上传文档

将文件通过OpenAI兼容接口上传到阿里百炼平台，保存至平台安全存储空间后获取`file-id`

1.在开始上传文档之前，请您将需要转换的文件放在/Files目录下

2.准备好文件之后，运行：

```
python uploadFiles.py
```

3.控制台将提示已上传文件

## 五、进行文档结构化数据

```
python main.py
```

这将对刚才上传的文件进行结构化，结构化的格式由main.py里面的prompt设定

如果您需要修改结构化的格式，请修改main.py内的prompt

过一段时间之后，完成结构化的数据将被保存在/bank 文件夹下

## 六、删除文档

如果想要删除上传的文档，请运行：

```
python delete_all_files.py
```

## 七、注意事项

1.在进行文档结构化数据之前，确保您的文档已经上传到阿里云百炼平台

2.如果要处理新文档，请先删除之前上传的文档，否则之前上传的文件也会被重复转化

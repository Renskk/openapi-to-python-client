# openapi to python client

openapi to client 地址：<https://github.com/openapi-generators/openapi-python-client>

本项目在openapi to client基础上，修改模版文件，方便接口测试使用。

```python
# 原项目
from {{ package_name }}.models import MyDataModel
from {{ package_name }}.api.my_tag import get_my_data_model
from {{ package_name }}.types import Response

with client as client:
    my_data: MyDataModel = get_my_data_model.sync(client=client)
    # or if you need more info (e.g. status_code)
    response: Response[MyDataModel] = get_my_data_model.sync_detailed(client=client)
# -----------------------------------------------------------------------------------
# 本项目 可以使用client 可以直接调用接口方法，返回httpx.response
from {{ package_name }}.models import MyDataModel
from {{ package_name }}.api.my_tag import get_my_data_model

client = Client()
my_data = client.get_my_data_model.sync()
# 直接获取json响应
my_data = client.get_my_data_model.sync().json()
```

## 使用方法

1. 安装依赖库

   ```shell
   pip install -r requirements.txt
   ```

2. 填写配置信息

   配置信息详情：<https://github.com/openapi-generators/openapi-python-client/blob/main/README.md#configuration>

   ```yaml
   # 特别注意: url 和 path 填写二选一
   url: null # 填入线上 openapi url
   path: null # 填入本地 openapi json path
   config:
     project_name_override: demo # 生成的项目名
     package_name_override: openapi # 生成的包名
     package_version_override: null # 指定生成的客户端的包版本。如果未设置，客户端将使用 OpenAPI 规范的版本。
     use_path_prefixes_for_title_model_names: true
     field_prefix: field_
     http_timeout: 5
   
   ```

3. 命令行说明

   ```shell
   cd openapi-to-python-client
   python __main__.py --help # 获取帮助文件
   
   # 生成/更新 python client
   # 生成的client path，取决于命令行执行的path
   # 默认使用config.yaml中的配置
   python __main__.py generate # 生成一个新的 OpenAPI Client 库
   python __main__.py update # 更新现有的 OpenAPI Client 库
   ```

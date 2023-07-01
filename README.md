# 启动文档

## 后端启动

在`backend`目录下运行以下命令

```python
# 重置数据库
python manage.py makemigrations
python manage.py migrate

# 启动项目
python manage.py runserver
```



## 前端启动

安装node环境

详情：https://www.yuque.com/cerelise/qnxk3x/cnzg6dsqvn4q7ygv

安装v18.15.0

安装完成后，进入`frontend`目录

运行前先修改`package.json`

```json
   "scripts": {
     "dev": "vite --port=3000",
     "build": "vite build",
     "preview": "vite preview",
     "start": "json-server --watch reviews.json --port 5000",
     "serve": "concurrently \"npm run start\" \"npm run dev\""
   }
```

然后运行以下命令

```js
// 安装依赖
npm install

// 运行项目
npm run serve
```


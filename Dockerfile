# 使用官方的Node.js镜像作为基础镜像
FROM node:16-alpine AS builder

# 设置工作目录
WORKDIR /app

# 复制package.json和package-lock.json
COPY package*.json ./

# 安装依赖
RUN npm ci

# 复制所有源代码
COPY . .

# 构建Vue.js应用
RUN npm run build

# 使用nginx作为最终的镜像来服务静态文件
FROM nginx:alpine

# 复制构建结果到nginx的默认目录
COPY --from=builder /app/dist /usr/share/nginx/html

# 可选：暴露端口
EXPOSE 80
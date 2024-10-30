# 使用 Node.js 作为基础镜像
FROM node:18 AS builder

# 设置工作目录
WORKDIR /frontend

# 复制 package.json 和 package-lock.json (如果有的话)
COPY ./blog .

# 安装 pnpm
RUN npm install -g pnpm

# 安装依赖
RUN pnpm install

# 构建项目
RUN npm run build

# 使用 Nginx 作为基础镜像
FROM nginx:alpine

RUN rm -rf html
RUN mkdir html

WORKDIR /
# 复制构建后的文件到 Nginx 的默认目录
COPY --from=builder ./frontend/dist /usr/share/nginx/html

# 可选：自定义 Nginx 配置
COPY ./nginx.conf /etc/nginx

# 启动 Nginx
ENTRYPOINT ["nginx", "-g", "daemon off;"]
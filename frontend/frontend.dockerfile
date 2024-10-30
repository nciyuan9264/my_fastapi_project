# # 使用 Node.js 作为基础镜像
# FROM node:18 AS builder

# # 设置工作目录
# WORKDIR /frontend

# # 复制 package.json 和 package-lock.json (如果有的话)
# COPY ./blog .

# RUN rm -rf node_modules pnpm-lock.yaml

# # 安装 pnpm
# RUN npm install -g pnpm

# # 安装依赖
# RUN pnpm install

# # 构建项目
# RUN npm run build
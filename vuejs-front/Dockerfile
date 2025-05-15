# 빌드 단계: Node.js 환경에서 Vue.js 애플리케이션 빌드
# node 20 버전 사용 보안 지원
FROM node:20-alpine AS build

# 작업 디렉토리 설정
WORKDIR /app

# 패키지 파일 먼저 복사 (Docker 캐시 활용)
COPY package*.json ./

# 의존성 설치 (보안 강화)
RUN npm config set registry https://registry.npmjs.org/ && \
    npm install --no-audit --prefer-offline

# 나머지 애플리케이션 파일 복사
COPY . .

# 프로덕션 모드로 빌드
ENV NODE_ENV=production
RUN npm run build

# 프로덕션 단계: nginx를 사용하여 정적 파일 서빙
FROM nginx:alpine

# 빌드 단계에서 생성된 정적 파일 복사
COPY --from=build /app/dist /usr/share/nginx/html

# nginx 설정 파일 복사
COPY nginx.conf /etc/nginx/conf.d/default.conf

# nginx 보안 설정 강화
RUN mkdir -p /var/cache/nginx && \
    mkdir -p /var/run && \
    mkdir -p /run && \
    touch /run/nginx.pid && \
    chown -R nginx:nginx /var/cache/nginx && \
    chown -R nginx:nginx /var/run && \
    chown -R nginx:nginx /run && \
    chown -R nginx:nginx /usr/share/nginx/html && \
    chmod -R 755 /usr/share/nginx/html && \
    # nginx.conf 수정
    sed -i 's/user  nginx;/# user  nginx;/' /etc/nginx/nginx.conf && \
    # 추가 보안 설정
    chmod 644 /etc/nginx/conf.d/default.conf && \
    chown nginx:nginx /etc/nginx/conf.d/default.conf

# 비루트 사용자로 전환 (보안 강화)
USER nginx

# 포트 노출
EXPOSE 8080

# nginx 실행
CMD ["nginx", "-g", "daemon off;"] 
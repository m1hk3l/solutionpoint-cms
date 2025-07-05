FROM node:22-alpine AS build

WORKDIR /app

COPY package.json package-lock.json ./
RUN npm install

COPY . .

# Build static assets for production
RUN npm run build

# Final static file serving image
FROM nginx:stable-alpine-slim

COPY --from=build /app/dist /usr/share/nginx/html

# Expose port 80 for serving static files
EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
# Uptime Monitor 🚀
A lightweight and efficient uptime monitoring tool built with Python, designed to check the availability and response time of websites or servers. This tool helps you keep track of your website's performance and logs historical data for analysis.

---

## **Features:**
- **HTTP Status Checks:** Monitors the status code and response time of specified URLs.
- **Ping Checks:** Verifies server reachability using ICMP ping.
- **Logging:** Saves logs in CSV format with timestamps, status codes, and response times.
- **Configurable:** Easily customizable for URLs to monitor and check intervals.
- **Lightweight and Portable:** Dockerized for easy deployment and portability.

---

## **Getting Started:**

### **Prerequisites:**
- Docker installed on your system.  
  [Install Docker](https://docs.docker.com/get-docker/)

---

## **1. Pull the Docker Image**
Pull the latest image from Docker Hub:

```bash
docker pull nazmulhasan/uptime-monitor:latest
```

## **2. Run the Docker Container**

```bash
docker run -d nazmulhasan/uptime-monitor:latest
```

## **3. Run with custom container name**

```bash
docker run -d --name custom-uptime-monitor nazmulhasan/uptime-monitor:latest
```

## **4. Check if the container is running**

```bash
docker ps
```

## **5. View Historical Logs**

```bash
docker cp uptime-monitor:/app/uptime_logs.csv .
cat uptime_logs.csv
```

## **6. Upcoming planned features**

* Email alerts for downtime or slow response.
* Integration with Slack or Discord for incident notifications.
* More monitoring metrics like SSL expiry and DNS resolution.

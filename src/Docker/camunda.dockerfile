FROM camunda/camunda-bpm-platform:tomcat-7.19.0

# Enable mssql-jdbc
COPY mssql-jdbc-12.2.0.jre11.jar ./lib/

# Setup environment
ENV DB_DRIVER com.microsoft.sqlserver.jdbc.SQLServerDriver
ENV DB_URL jdbc:sqlserver://172.17.0.1;DatabaseName=Camunda;trustServerCertificate=true
ENV DB_USERNAME sa
ENV DB_PASSWORD password123!

# Startup
ENTRYPOINT ["/sbin/tini", "--"]
CMD ["./camunda.sh"]
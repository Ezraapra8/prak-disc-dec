   function dcu { docker compose up -d }
   function dcd { docker compose down }
   function dps { docker ps }
   function der { docker exec -it streaming-replication-postgres_replica-1 bash }
   function dep { docker exec -it streaming-replication-postgres_primary-1 bash }
   function dlr { docker logs streaming-replication-postgres_replica-1 }
   function dlp { docker logs streaming-replication-postgres_primary-1 }
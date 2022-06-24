CREATE TABLE IF NOT EXISTS volunteer
             (
                          v_id         INTEGER NOT NULL AUTO_INCREMENT,
                          f_name VARCHAR(30) NOT NULL,
                          l_name  VARCHAR(30) NOT NULL,
                          PRIMARY KEY (v_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE IF NOT EXISTS events
             (
                          e_id         INTEGER NOT NULL AUTO_INCREMENT,
                          name VARCHAR(30) NOT NULL,
                          date  DATE NOT NULL,
                          PRIMARY KEY (e_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE IF NOT EXISTS enrollment
             (
                          id         INTEGER NOT NULL AUTO_INCREMENT,
                          v_id         INTEGER NOT NULL,
                          e_id         INTEGER NOT NULL,
                          PRIMARY KEY (id),
                          FOREIGN KEY (e_id) REFERENCES events(e_id),
                          FOREIGN KEY (v_id) REFERENCES volunteer(v_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

LOCK TABLES `volunteer` WRITE;
INSERT INTO  `volunteer` VALUES (1,'Ben','Hesketh'),(2,'Luke','Benson'),(3,'Matt','Hunt');
LOCK TABLES `events` WRITE;
INSERT INTO  `events` VALUES (1, 'Bakesale', "2022-05-10"),(2, 'Dinner', "2022-05-25"),(3, 'Carwash', "2022-06-26");
UNLOCK TABLES;

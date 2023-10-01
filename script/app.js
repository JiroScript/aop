/*
Error: ER_NOT_SUPPORTED_AUTH_MODE: Client does not support authentication protocol requested by server; consider upgrading MySQL client
上記のエラーに対し下記をターミナルで実行することで解決できた。

ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'password'
*/
/*
expressモジュールがインストール
ターミナルまたはコマンドプロンプトを開きます。
プロジェクトのルートディレクトリに移動します（app.jsファイルが存在するディレクトリ）。
次のコマンドを実行して、expressモジュールをインストールします：

npm install express
npm install mysql
npm install cors
*/

/*
C:\Users\goths>ipconfig
Wireless LAN adapter Wi-Fi:
   IPv4 アドレス . . . . . . . . . . . .: 192.168.254.43
*/
const express = require('express');
const mysql = require('mysql');
const app = express();
const port = 3000;
const cors = require('cors');

app.use(cors());
app.use(express.static('aop'));

// Ignore favicon.ico request
app.get('/favicon.ico', (req, res) => res.status(204));

const createConnection = (dbName) => {
  const connection = mysql.createConnection({
    host: 'localhost', // <-- Set to your remote MySQL server
    user: 'root',
    password: 'mysqL-11',  // <-- Your MySQL password here
    database: dbName
  });
  
  // Reconnect if connection is lost
  connection.on('error', (err) => {
    if (err.code === 'PROTOCOL_CONNECTION_LOST') {
      createConnection(dbName);
    } else {
      throw err;
    }
  });

  return connection;
};

const executeQuery = (connection, sql, res) => {
  connection.query(sql, function (err, result) {
    if (err) {
      console.error('An error occurred: ' + err.message);
      res.status(500).send({ error: 'An error occurred: ' + err.message });
      return;
    }
    res.send(result);
  });
};

app.get('/:dbName', (req, res) => {
  const dbName = req.params.dbName;
  const location = req.query.location;
  
  if (!dbName || dbName === 'favicon.ico') {
    res.status(400).send('Bad Request');
    return;
  }

  const connection = createConnection(dbName);
  const sql = `SELECT * FROM ${location}`;

  executeQuery(connection, sql, res);
});

app.listen(port, '0.0.0.0', () => {
  console.log(`Server is running at http://localhost:${port}`);
});

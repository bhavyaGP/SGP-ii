var SolrNode = require('solr-node');
const bodyParser = require('body-parser');
port = 3001;
var client = new SolrNode({
  host: 'localhost',
  port: '8983',
  core: 'info',
  protocol: 'http'
});
const express = require('express');
const app = express();

app.set('view engine', 'ejs');
app.use(bodyParser.urlencoded({ extended: true }));

// console.log("jj")

app.post('/getProduct', function (req, res) {
  searchTerm = req.body.pname;
  
  // position = req.body.position;
  // departments = req.body.departments;
  var strQuery = client.query().q("name:" + searchTerm + "*   OR position:" + searchTerm + "* OR department_s_:" + searchTerm + "* OR ph.d:" + searchTerm + "* OR research_interests: " + searchTerm + "*");

  strQuery.sort('experience', 'asc');

  // pname:climate OR position:climate OR departments:climate
  // var strQuery = client.query().q("pname:" + pName + "*");
  // var strQuery = client.query().q("pname:yash*");
  client.search(strQuery, function (err, result) {
    if (err) {
      console.log(err);
      return;
    }
    console.log('Response:', result.response);
    res.render('index', { data: result.response })
  });
})

app.get('/searchProduct', function (req, res) {
  res.render('search');
})

app.listen(port, () => {
  console.log(`Server is running at http://localhost:${port}/`);
});
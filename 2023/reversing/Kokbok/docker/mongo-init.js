const fs = require("fs");

const recept = JSON.parse(fs.readFileSync("/unika_rena_recept.json", "utf-8"));
const topSecret = JSON.parse(fs.readFileSync("/flag_doc.json", "utf-8"));

db.createCollection('Recept');
db.Recept.insertMany(recept);

db.createCollection('Hemliga_recept');
db.Hemliga_recept.insert(topSecret);

db.createUser({ user: 'fooduser', pwd: 'lilatomat', roles: [ { role: 'read', db: 'Kokbok' } ] });

const fs = require("node:fs");

const stats = fs.statSync('../node.txt')

console.log(
  stats.isFile(), // si es un fichero
  stats.isDirectory(), // si es un directorio
  stats.isSymbolicLink(), // si es un enlace simbólico
  stats.size // tamaño en bytes
)
